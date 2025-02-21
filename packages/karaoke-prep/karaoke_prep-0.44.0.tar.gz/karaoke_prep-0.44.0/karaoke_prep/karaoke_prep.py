import os
import sys
import re
import glob
import logging
import tempfile
import shutil
import asyncio
import signal
import time
import fcntl
import errno
import psutil
from datetime import datetime
import importlib.resources as pkg_resources
import yt_dlp.YoutubeDL as ydl
from PIL import Image, ImageDraw, ImageFont
from lyrics_transcriber import LyricsTranscriber, OutputConfig, TranscriberConfig, LyricsConfig
from lyrics_transcriber.core.controller import LyricsControllerResult
from pydub import AudioSegment
import json
from dotenv import load_dotenv


class KaraokePrep:
    def __init__(
        self,
        # Basic inputs
        input_media=None,
        artist=None,
        title=None,
        filename_pattern=None,
        # Logging & Debugging
        dry_run=False,
        log_level=logging.DEBUG,
        log_formatter=None,
        render_bounding_boxes=False,
        # Input/Output Configuration
        output_dir=".",
        create_track_subfolders=False,
        lossless_output_format="FLAC",
        output_png=True,
        output_jpg=True,
        # Audio Processing Configuration
        clean_instrumental_model="model_bs_roformer_ep_317_sdr_12.9755.ckpt",
        backing_vocals_models=["mel_band_roformer_karaoke_aufr33_viperx_sdr_10.1956.ckpt"],
        other_stems_models=["htdemucs_6s.yaml"],
        model_file_dir=os.path.join(tempfile.gettempdir(), "audio-separator-models"),
        existing_instrumental=None,
        denoise_enabled=True,
        normalization_enabled=True,
        # Hardware Acceleration
        use_cuda=False,
        use_coreml=False,
        # Lyrics Configuration
        lyrics_artist=None,
        lyrics_title=None,
        lyrics_file=None,
        skip_lyrics=False,
        skip_transcription=False,
        skip_transcription_review=False,
        subtitle_offset_ms=0,
        # Style Configuration
        style_params_json=None,
    ):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)
        self.log_level = log_level
        self.log_formatter = log_formatter

        self.log_handler = logging.StreamHandler()

        if self.log_formatter is None:
            self.log_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - %(message)s")

        self.log_handler.setFormatter(self.log_formatter)
        self.logger.addHandler(self.log_handler)

        self.logger.debug(f"KaraokePrep instantiating with input_media: {input_media} artist: {artist} title: {title}")

        self.dry_run = dry_run
        self.extractor = None
        self.media_id = None
        self.url = None
        self.input_media = input_media
        self.artist = artist
        self.title = title
        self.filename_pattern = filename_pattern

        # Audio Processing
        self.clean_instrumental_model = clean_instrumental_model
        self.backing_vocals_models = backing_vocals_models
        self.other_stems_models = other_stems_models
        self.model_file_dir = model_file_dir
        self.existing_instrumental = existing_instrumental
        self.denoise_enabled = denoise_enabled
        self.normalization_enabled = normalization_enabled

        # Input/Output
        self.output_dir = output_dir
        self.lossless_output_format = lossless_output_format.lower()
        self.create_track_subfolders = create_track_subfolders
        self.output_png = output_png
        self.output_jpg = output_jpg

        # Hardware
        self.use_cuda = use_cuda
        self.use_coreml = use_coreml

        # Lyrics
        self.lyrics = None
        self.lyrics_artist = lyrics_artist
        self.lyrics_title = lyrics_title
        self.lyrics_file = lyrics_file
        self.skip_lyrics = skip_lyrics
        self.skip_transcription = skip_transcription
        self.skip_transcription_review = skip_transcription_review

        # Style
        self.subtitle_offset_ms = subtitle_offset_ms
        self.render_bounding_boxes = render_bounding_boxes
        self.style_params_json = style_params_json

        # Load style parameters from JSON or use defaults
        if style_params_json:
            try:
                with open(style_params_json, "r") as f:
                    self.style_params = json.loads(f.read())
            except FileNotFoundError:
                self.logger.error(f"Style parameters configuration file not found: {style_params_json}")
                sys.exit(1)
            except json.JSONDecodeError as e:
                self.logger.error(f"Invalid JSON in style parameters configuration file: {e}")
                sys.exit(1)
        else:
            # Use default values
            self.style_params = {
                "intro": {
                    "video_duration": 5,
                    "existing_image": None,
                    "background_color": "#000000",
                    "background_image": None,
                    "font": "Montserrat-Bold.ttf",
                    "artist_color": "#ffdf6b",
                    "artist_gradient": None,
                    "title_color": "#ffffff",
                    "title_gradient": None,
                    "title_region": "370, 200, 3100, 480",
                    "artist_region": "370, 700, 3100, 480",
                    "extra_text": None,
                    "extra_text_color": "#ffffff",
                    "extra_text_gradient": None,
                    "extra_text_region": "370, 1200, 3100, 480",
                    "title_text_transform": None,  # none, uppercase, lowercase, propercase
                    "artist_text_transform": None,  # none, uppercase, lowercase, propercase
                },
                "end": {
                    "video_duration": 5,
                    "existing_image": None,
                    "background_color": "#000000",
                    "background_image": None,
                    "font": "Montserrat-Bold.ttf",
                    "artist_color": "#ffdf6b",
                    "artist_gradient": None,
                    "title_color": "#ffffff",
                    "title_gradient": None,
                    "title_region": None,
                    "artist_region": None,
                    "extra_text": "THANK YOU FOR SINGING!",
                    "extra_text_color": "#ff7acc",
                    "extra_text_gradient": None,
                    "extra_text_region": None,
                    "title_text_transform": None,  # none, uppercase, lowercase, propercase
                    "artist_text_transform": None,  # none, uppercase, lowercase, propercase
                },
            }

        # Set up title format from style params
        self.title_format = {
            "background_color": self.style_params["intro"]["background_color"],
            "background_image": self.style_params["intro"]["background_image"],
            "font": self.style_params["intro"]["font"],
            "artist_color": self.style_params["intro"]["artist_color"],
            "artist_gradient": self.style_params["intro"].get("artist_gradient"),
            "title_color": self.style_params["intro"]["title_color"],
            "title_gradient": self.style_params["intro"].get("title_gradient"),
            "extra_text": self.style_params["intro"]["extra_text"],
            "extra_text_color": self.style_params["intro"]["extra_text_color"],
            "extra_text_gradient": self.style_params["intro"].get("extra_text_gradient"),
            "extra_text_region": self.style_params["intro"]["extra_text_region"],
            "title_region": self.style_params["intro"]["title_region"],
            "artist_region": self.style_params["intro"]["artist_region"],
            "title_text_transform": self.style_params["intro"].get("title_text_transform"),
            "artist_text_transform": self.style_params["intro"].get("artist_text_transform"),
        }

        # Set up end format from style params
        self.end_format = {
            "background_color": self.style_params["end"]["background_color"],
            "background_image": self.style_params["end"]["background_image"],
            "font": self.style_params["end"]["font"],
            "artist_color": self.style_params["end"]["artist_color"],
            "artist_gradient": self.style_params["end"].get("artist_gradient"),
            "title_color": self.style_params["end"]["title_color"],
            "title_gradient": self.style_params["end"].get("title_gradient"),
            "extra_text": self.style_params["end"]["extra_text"],
            "extra_text_color": self.style_params["end"]["extra_text_color"],
            "extra_text_gradient": self.style_params["end"].get("extra_text_gradient"),
            "extra_text_region": self.style_params["end"]["extra_text_region"],
            "title_region": self.style_params["end"]["title_region"],
            "artist_region": self.style_params["end"]["artist_region"],
            "title_text_transform": self.style_params["end"].get("title_text_transform"),
            "artist_text_transform": self.style_params["end"].get("artist_text_transform"),
        }

        # Store video durations and existing images
        self.intro_video_duration = self.style_params["intro"]["video_duration"]
        self.end_video_duration = self.style_params["end"]["video_duration"]
        self.existing_title_image = self.style_params["intro"]["existing_image"]
        self.existing_end_image = self.style_params["end"]["existing_image"]

        # Path to the Windows PyInstaller frozen bundled ffmpeg.exe, or the system-installed FFmpeg binary on Mac/Linux
        ffmpeg_path = os.path.join(sys._MEIPASS, "ffmpeg.exe") if getattr(sys, "frozen", False) else "ffmpeg"

        self.ffmpeg_base_command = f"{ffmpeg_path} -hide_banner -nostats"

        if self.log_level == logging.DEBUG:
            self.ffmpeg_base_command += " -loglevel verbose"
        else:
            self.ffmpeg_base_command += " -loglevel fatal"

        self.logger.debug(f"Initialized title_format with extra_text: {self.title_format['extra_text']}")
        self.logger.debug(f"Initialized title_format with extra_text_region: {self.title_format['extra_text_region']}")

        self.logger.debug(f"Initialized end_format with extra_text: {self.end_format['extra_text']}")
        self.logger.debug(f"Initialized end_format with extra_text_region: {self.end_format['extra_text_region']}")

        self.extracted_info = None
        self.persistent_artist = None

        self.logger.debug(f"KaraokePrep lossless_output_format: {self.lossless_output_format}")

        if not os.path.exists(self.output_dir):
            self.logger.debug(f"Overall output dir {self.output_dir} did not exist, creating")
            os.makedirs(self.output_dir)
        else:
            self.logger.debug(f"Overall output dir {self.output_dir} already exists")

    @staticmethod
    def parse_region(region_str):
        if region_str:
            try:
                return tuple(map(int, region_str.split(",")))
            except ValueError:
                raise ValueError(f"Invalid region format: {region_str}. Expected format: 'x,y,width,height'")
        return None

    def extract_info_for_online_media(self, input_url=None, input_artist=None, input_title=None):
        self.logger.info(f"Extracting info for input_url: {input_url} input_artist: {input_artist} input_title: {input_title}")
        if input_url is not None:
            # If a URL is provided, use it to extract the metadata
            with ydl({"quiet": True}) as ydl_instance:
                self.extracted_info = ydl_instance.extract_info(input_url, download=False)
        else:
            # If no URL is provided, use the query to search for the top result
            ydl_opts = {"quiet": "True", "format": "bestaudio", "noplaylist": "True", "extract_flat": True}
            with ydl(ydl_opts) as ydl_instance:
                query = f"{input_artist} {input_title}"
                self.extracted_info = ydl_instance.extract_info(f"ytsearch1:{query}", download=False)["entries"][0]
                if not self.extracted_info:
                    raise Exception(f"No search results found on YouTube for query: {input_artist} {input_title}")

    def parse_single_track_metadata(self, input_artist, input_title):
        """
        Parses self.extracted_info to extract URL, extractor, ID, artist and title.
        """
        # Default values if parsing fails
        self.url = None
        self.extractor = None
        self.media_id = None

        metadata_artist = ""
        metadata_title = ""

        if "url" in self.extracted_info:
            self.url = self.extracted_info["url"]
        elif "webpage_url" in self.extracted_info:
            self.url = self.extracted_info["webpage_url"]
        else:
            raise Exception(f"Failed to extract URL from input media metadata: {self.extracted_info}")

        if "extractor_key" in self.extracted_info:
            self.extractor = self.extracted_info["extractor_key"]
        elif "ie_key" in self.extracted_info:
            self.extractor = self.extracted_info["ie_key"]
        else:
            raise Exception(f"Failed to find extractor name from input media metadata: {self.extracted_info}")

        if "id" in self.extracted_info:
            self.media_id = self.extracted_info["id"]

        # Example: "Artist - Title"
        if "title" in self.extracted_info and "-" in self.extracted_info["title"]:
            metadata_artist, metadata_title = self.extracted_info["title"].split("-", 1)
            metadata_artist = metadata_artist.strip()
            metadata_title = metadata_title.strip()
        elif "uploader" in self.extracted_info:
            # Fallback to uploader as artist if title parsing fails
            metadata_artist = self.extracted_info["uploader"]
            if "title" in self.extracted_info:
                metadata_title = self.extracted_info["title"].strip()

        # If unable to parse, log an appropriate message
        if not metadata_artist or not metadata_title:
            self.logger.warning("Could not parse artist and title from the input media metadata.")

        if input_artist is None:
            self.logger.warn(f"Artist not provided as input, setting to {metadata_artist} from input media metadata...")
            self.artist = metadata_artist

        if input_title is None:
            self.logger.warn(f"Title not provided as input, setting to {metadata_title} from input media metadata...")
            self.title = metadata_title

        if self.persistent_artist:
            self.logger.debug(
                f"Resetting self.artist from {self.artist} to persistent artist: {self.persistent_artist} for consistency while processing playlist..."
            )
            self.artist = self.persistent_artist

        if self.artist and self.title:
            self.logger.info(f"Extracted url: {self.url}, artist: {self.artist}, title: {self.title}")
        else:
            self.logger.debug(self.extracted_info)
            raise Exception("Failed to extract artist and title from the input media metadata.")

    def copy_input_media(self, input_media, output_filename_no_extension):
        self.logger.debug(f"Copying media from local path {input_media} to filename {output_filename_no_extension} + existing extension")

        copied_file_name = output_filename_no_extension + os.path.splitext(input_media)[1]
        self.logger.debug(f"Target filename: {copied_file_name}")

        # Check if source and destination are the same
        if os.path.abspath(input_media) == os.path.abspath(copied_file_name):
            self.logger.info("Source and destination are the same file, skipping copy")
            return input_media

        self.logger.debug(f"Copying {input_media} to {copied_file_name}")
        shutil.copy2(input_media, copied_file_name)

        return copied_file_name

    def download_video(self, url, output_filename_no_extension):
        self.logger.debug(f"Downloading media from URL {url} to filename {output_filename_no_extension} + (as yet) unknown extension")

        ydl_opts = {
            "quiet": True,
            "format": "bv*+ba/b",  # if a combined video + audio format is better than the best video-only format use the combined format
            "outtmpl": f"{output_filename_no_extension}.%(ext)s",
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        }

        with ydl(ydl_opts) as ydl_instance:
            ydl_instance.download([url])

            # Search for the file with any extension
            downloaded_files = glob.glob(f"{output_filename_no_extension}.*")
            if downloaded_files:
                downloaded_file_name = downloaded_files[0]  # Assume the first match is the correct one
                self.logger.info(f"Download finished, returning downloaded filename: {downloaded_file_name}")
                return downloaded_file_name
            else:
                self.logger.error("No files found matching the download pattern.")
                return None

    def extract_still_image_from_video(self, input_filename, output_filename_no_extension):
        output_filename = output_filename_no_extension + ".png"
        self.logger.info(f"Extracting still image from position 30s input media")
        ffmpeg_command = f'{self.ffmpeg_base_command} -i "{input_filename}" -ss 00:00:30 -vframes 1 "{output_filename}"'
        self.logger.debug(f"Running command: {ffmpeg_command}")
        os.system(ffmpeg_command)
        return output_filename

    def convert_to_wav(self, input_filename, output_filename_no_extension):
        """Convert input audio to WAV format, with input validation."""
        # Validate input file exists and is readable
        if not os.path.isfile(input_filename):
            raise Exception(f"Input audio file not found: {input_filename}")

        if os.path.getsize(input_filename) == 0:
            raise Exception(f"Input audio file is empty: {input_filename}")

        # Validate input file format using ffprobe
        probe_command = f'ffprobe -v error -show_entries stream=codec_type -of default=noprint_wrappers=1 "{input_filename}"'
        probe_output = os.popen(probe_command).read()

        if "codec_type=audio" not in probe_output:
            raise Exception(f"No valid audio stream found in file: {input_filename}")

        output_filename = output_filename_no_extension + ".wav"
        self.logger.info(f"Converting input media to audio WAV file")
        ffmpeg_command = f'{self.ffmpeg_base_command} -n -i "{input_filename}" "{output_filename}"'
        self.logger.debug(f"Running command: {ffmpeg_command}")
        if not self.dry_run:
            os.system(ffmpeg_command)
        return output_filename

    def find_best_split_point(self, line):
        """
        Find the best split point in a line based on the specified criteria.
        """

        self.logger.debug(f"Finding best_split_point for line: {line}")
        words = line.split()
        mid_word_index = len(words) // 2
        self.logger.debug(f"words: {words} mid_word_index: {mid_word_index}")

        # Check for a comma within one or two words of the middle word
        if "," in line:
            mid_point = len(" ".join(words[:mid_word_index]))
            comma_indices = [i for i, char in enumerate(line) if char == ","]

            for index in comma_indices:
                if abs(mid_point - index) < 20 and len(line[: index + 1].strip()) <= 36:
                    self.logger.debug(
                        f"Found comma at index {index} which is within 20 characters of mid_point {mid_point} and results in a suitable line length, accepting as split point"
                    )
                    return index + 1  # Include the comma in the first line

        # Check for 'and'
        if " and " in line:
            mid_point = len(line) // 2
            and_indices = [m.start() for m in re.finditer(" and ", line)]
            for index in sorted(and_indices, key=lambda x: abs(x - mid_point)):
                if len(line[: index + len(" and ")].strip()) <= 36:
                    self.logger.debug(f"Found 'and' at index {index} which results in a suitable line length, accepting as split point")
                    return index + len(" and ")

        # If no better split point is found, try splitting at the middle word
        if len(words) > 2 and mid_word_index > 0:
            split_at_middle = len(" ".join(words[:mid_word_index]))
            if split_at_middle <= 36:
                self.logger.debug(f"Splitting at middle word index: {mid_word_index}")
                return split_at_middle

        # If the line is still too long, forcibly split at the maximum length
        forced_split_point = 36
        if len(line) > forced_split_point:
            self.logger.debug(f"Line is still too long, forcibly splitting at position {forced_split_point}")
            return forced_split_point

    def process_line(self, line):
        """
        Process a single line to ensure it's within the maximum length,
        and handle parentheses.
        """
        processed_lines = []
        iteration_count = 0
        max_iterations = 100  # Failsafe limit

        while len(line) > 36:
            if iteration_count > max_iterations:
                self.logger.error(f"Maximum iterations exceeded in process_line for line: {line}")
                break

            # Check if the line contains parentheses
            if "(" in line and ")" in line:
                start_paren = line.find("(")
                end_paren = line.find(")") + 1
                if end_paren < len(line) and line[end_paren] == ",":
                    end_paren += 1

                if start_paren > 0:
                    processed_lines.append(line[:start_paren].strip())
                processed_lines.append(line[start_paren:end_paren].strip())
                line = line[end_paren:].strip()
            else:
                split_point = self.find_best_split_point(line)
                processed_lines.append(line[:split_point].strip())
                line = line[split_point:].strip()

            iteration_count += 1

        if line:  # Add the remaining part if not empty
            processed_lines.append(line)

        return processed_lines

    def transcribe_lyrics(self, input_audio_wav, artist, title, track_output_dir):
        self.logger.info(
            f"Transcribing lyrics for track {artist} - {title} from audio file: {input_audio_wav} with output directory: {track_output_dir}"
        )

        # Check for existing files first using sanitized names
        sanitized_artist = self.sanitize_filename(artist)
        sanitized_title = self.sanitize_filename(title)
        parent_video_path = os.path.join(track_output_dir, f"{sanitized_artist} - {sanitized_title} (With Vocals).mkv")
        parent_lrc_path = os.path.join(track_output_dir, f"{sanitized_artist} - {sanitized_title} (Karaoke).lrc")

        # Check lyrics directory for existing files
        lyrics_dir = os.path.join(track_output_dir, "lyrics")
        lyrics_video_path = os.path.join(lyrics_dir, f"{sanitized_artist} - {sanitized_title} (With Vocals).mkv")
        lyrics_lrc_path = os.path.join(lyrics_dir, f"{sanitized_artist} - {sanitized_title} (Karaoke).lrc")

        # If files exist in parent directory, return early
        if os.path.exists(parent_video_path) and os.path.exists(parent_lrc_path):
            self.logger.info(f"Found existing video and LRC files in parent directory, skipping transcription")
            return {
                "lrc_filepath": parent_lrc_path,
                "ass_filepath": parent_video_path,
            }

        # If files exist in lyrics directory, copy to parent and return
        if os.path.exists(lyrics_video_path) and os.path.exists(lyrics_lrc_path):
            self.logger.info(f"Found existing video and LRC files in lyrics directory, copying to parent")
            os.makedirs(track_output_dir, exist_ok=True)
            shutil.copy2(lyrics_video_path, parent_video_path)
            shutil.copy2(lyrics_lrc_path, parent_lrc_path)
            return {
                "lrc_filepath": parent_lrc_path,
                "ass_filepath": parent_video_path,
            }

        # Create lyrics subdirectory for new transcription
        os.makedirs(lyrics_dir, exist_ok=True)
        self.logger.info(f"Created lyrics directory: {lyrics_dir}")

        # Load environment variables
        load_dotenv()
        env_config = {
            "audioshake_api_token": os.getenv("AUDIOSHAKE_API_TOKEN"),
            "genius_api_token": os.getenv("GENIUS_API_TOKEN"),
            "spotify_cookie": os.getenv("SPOTIFY_COOKIE_SP_DC"),
            "runpod_api_key": os.getenv("RUNPOD_API_KEY"),
            "whisper_runpod_id": os.getenv("WHISPER_RUNPOD_ID"),
        }

        # Create config objects for LyricsTranscriber
        transcriber_config = TranscriberConfig(
            audioshake_api_token=env_config.get("audioshake_api_token"),
        )

        lyrics_config = LyricsConfig(
            genius_api_token=env_config.get("genius_api_token"),
            spotify_cookie=env_config.get("spotify_cookie"),
            lyrics_file=self.lyrics_file,
        )

        output_config = OutputConfig(
            output_styles_json=self.style_params_json,
            output_dir=lyrics_dir,
            render_video=True,
            fetch_lyrics=True,
            run_transcription=not self.skip_transcription,
            run_correction=True,
            generate_plain_text=True,
            generate_lrc=True,
            generate_cdg=True,
            video_resolution="4k",
            enable_review=not self.skip_transcription_review,
            subtitle_offset_ms=self.subtitle_offset_ms,
        )

        # Initialize transcriber with new config objects
        transcriber = LyricsTranscriber(
            audio_filepath=input_audio_wav,
            artist=artist,
            title=title,
            transcriber_config=transcriber_config,
            lyrics_config=lyrics_config,
            output_config=output_config,
            logger=self.logger,
        )

        # Process and get results
        results: LyricsControllerResult = transcriber.process()
        self.logger.info(f"Transcriber Results Filepaths:")
        for key, value in results.__dict__.items():
            if key.endswith("_filepath"):
                self.logger.info(f"  {key}: {value}")

        # Build output dictionary
        transcriber_outputs = {}
        if results.lrc_filepath:
            transcriber_outputs["lrc_filepath"] = results.lrc_filepath
            self.logger.info(f"Moving LRC file from {results.lrc_filepath} to {parent_lrc_path}")
            shutil.copy2(results.lrc_filepath, parent_lrc_path)

        if results.ass_filepath:
            transcriber_outputs["ass_filepath"] = results.ass_filepath
            self.logger.info(f"Moving video file from {results.video_filepath} to {parent_video_path}")
            shutil.copy2(results.video_filepath, parent_video_path)

        if results.transcription_corrected:
            transcriber_outputs["corrected_lyrics_text"] = "\n".join(
                segment.text for segment in results.transcription_corrected.corrected_segments
            )
            transcriber_outputs["corrected_lyrics_text_filepath"] = results.corrected_txt

        if transcriber_outputs:
            self.logger.info(f"*** Transcriber Filepath Outputs: ***")
            for key, value in transcriber_outputs.items():
                if key.endswith("_filepath"):
                    self.logger.info(f"  {key}: {value}")

        return transcriber_outputs

    def sanitize_filename(self, filename):
        """Replace or remove characters that are unsafe for filenames."""
        # Replace problematic characters with underscores
        for char in ["\\", "/", ":", "*", "?", '"', "<", ">", "|"]:
            filename = filename.replace(char, "_")
        # Remove any trailing periods or spaces
        filename = filename.rstrip(" ")
        return filename

    def separate_audio(self, audio_file, model_name, artist_title, track_output_dir, instrumental_path, vocals_path):
        if audio_file is None or not os.path.isfile(audio_file):
            raise Exception("Error: Invalid audio source provided.")

        self.logger.debug(f"audio_file is valid file: {audio_file}")

        self.logger.info(
            f"instantiating Separator with model_file_dir: {self.model_file_dir}, model_filename: {model_name} output_format: {self.lossless_output_format}"
        )

        from audio_separator.separator import Separator

        separator = Separator(
            log_level=self.log_level,
            log_formatter=self.log_formatter,
            model_file_dir=self.model_file_dir,
            output_format=self.lossless_output_format,
        )

        separator.load_model(model_filename=model_name)
        output_files = separator.separate(audio_file)

        self.logger.debug(f"Separator output files: {output_files}")

        model_name_no_extension = os.path.splitext(model_name)[0]

        for file in output_files:
            if "(Vocals)" in file:
                self.logger.info(f"Renaming Vocals file {file} to {vocals_path}")
                os.rename(file, vocals_path)
            elif "(Instrumental)" in file:
                self.logger.info(f"Renaming Instrumental file {file} to {instrumental_path}")
                os.rename(file, instrumental_path)
            elif model_name in file:
                # Example filename 1: "Freddie Jackson - All I'll Ever Ask (feat. Najee) (Local)_(Piano)_htdemucs_6s.flac"
                # Example filename 2: "Freddie Jackson - All I'll Ever Ask (feat. Najee) (Local)_(Guitar)_htdemucs_6s.flac"
                # The stem name in these examples would be "Piano" or "Guitar"
                # Extract stem_name from the filename
                stem_name = file.split(f"_{model_name}")[0].split("_")[-1]
                stem_name = stem_name.strip("()")  # Remove parentheses if present

                other_stem_path = os.path.join(track_output_dir, f"{artist_title} ({stem_name} {model_name}).{self.lossless_output_format}")
                self.logger.info(f"Renaming other stem file {file} to {other_stem_path}")
                os.rename(file, other_stem_path)

            elif model_name_no_extension in file:
                # Example filename 1: "Freddie Jackson - All I'll Ever Ask (feat. Najee) (Local)_(Piano)_htdemucs_6s.flac"
                # Example filename 2: "Freddie Jackson - All I'll Ever Ask (feat. Najee) (Local)_(Guitar)_htdemucs_6s.flac"
                # The stem name in these examples would be "Piano" or "Guitar"
                # Extract stem_name from the filename
                stem_name = file.split(f"_{model_name_no_extension}")[0].split("_")[-1]
                stem_name = stem_name.strip("()")  # Remove parentheses if present

                other_stem_path = os.path.join(track_output_dir, f"{artist_title} ({stem_name} {model_name}).{self.lossless_output_format}")
                self.logger.info(f"Renaming other stem file {file} to {other_stem_path}")
                os.rename(file, other_stem_path)

        self.logger.info(f"Separation complete! Output file(s): {vocals_path} {instrumental_path}")

    def setup_output_paths(self, artist, title):
        if title is None and artist is None:
            raise ValueError("Error: At least title or artist must be provided")

        # If only title is provided, use it for both artist and title portions of paths
        if artist is None:
            sanitized_title = self.sanitize_filename(title)
            artist_title = sanitized_title
        else:
            sanitized_artist = self.sanitize_filename(artist)
            sanitized_title = self.sanitize_filename(title)
            artist_title = f"{sanitized_artist} - {sanitized_title}"

        track_output_dir = self.output_dir
        if self.create_track_subfolders:
            track_output_dir = os.path.join(self.output_dir, f"{artist_title}")

        if not os.path.exists(track_output_dir):
            self.logger.debug(f"Output dir {track_output_dir} did not exist, creating")
            os.makedirs(track_output_dir)

        return track_output_dir, artist_title

    def _create_gradient_mask(self, size, gradient_config):
        """Create a gradient mask for text coloring.

        Args:
            size (tuple): (width, height) of the mask
            gradient_config (dict): Configuration with keys:
                - color1: First color (hex)
                - color2: Second color (hex)
                - direction: 'horizontal' or 'vertical'
                - start: Start point of gradient transition (0-1)
                - stop: Stop point of gradient transition (0-1)
        """
        mask = Image.new("L", size)
        draw = ImageDraw.Draw(mask)

        width, height = size
        start = gradient_config["start"]
        stop = gradient_config["stop"]

        if gradient_config["direction"] == "horizontal":
            for x in range(width):
                # Calculate position in gradient (0 to 1)
                pos = x / width

                # Calculate color intensity
                if pos < start:
                    intensity = 0
                elif pos > stop:
                    intensity = 255
                else:
                    # Linear interpolation between start and stop
                    intensity = int(255 * (pos - start) / (stop - start))

                draw.line([(x, 0), (x, height)], fill=intensity)
        else:  # vertical
            for y in range(height):
                pos = y / height
                if pos < start:
                    intensity = 0
                elif pos > stop:
                    intensity = 255
                else:
                    intensity = int(255 * (pos - start) / (stop - start))

                draw.line([(0, y), (width, y)], fill=intensity)

        return mask

    def calculate_text_size_to_fit(self, draw, text, font_path, region):
        font_size = 500  # Start with a large font size
        font = ImageFont.truetype(font_path, size=font_size) if os.path.exists(font_path) else ImageFont.load_default()

        def get_text_size(text, font):
            bbox = draw.textbbox((0, 0), text, font=font)
            # Use the actual text height without the font's internal padding
            return bbox[2], bbox[3] - bbox[1]

        text_width, text_height = get_text_size(text, font)
        target_height = region[3]  # Use full region height as target

        while text_width > region[2] or text_height > target_height:
            font_size -= 10
            if font_size <= 150:
                # Split the text into two lines
                words = text.split()
                mid = len(words) // 2
                line1 = " ".join(words[:mid])
                line2 = " ".join(words[mid:])

                # Reset font size for two-line layout
                font_size = 500
                font = ImageFont.truetype(font_path, size=font_size) if os.path.exists(font_path) else ImageFont.load_default()

                while True:
                    text_width1, text_height1 = get_text_size(line1, font)
                    text_width2, text_height2 = get_text_size(line2, font)
                    total_height = text_height1 + text_height2

                    # Add a small gap between lines (10% of line height)
                    line_gap = text_height1 * 0.1
                    total_height_with_gap = total_height + line_gap

                    if max(text_width1, text_width2) <= region[2] and total_height_with_gap <= target_height:
                        return font, (line1, line2)

                    font_size -= 10
                    if font_size <= 0:
                        raise ValueError("Cannot fit text within the defined region.")
                    font = ImageFont.truetype(font_path, size=font_size) if os.path.exists(font_path) else ImageFont.load_default()

            font = ImageFont.truetype(font_path, size=font_size) if os.path.exists(font_path) else ImageFont.load_default()
            text_width, text_height = get_text_size(text, font)

        return font, text

    def _render_text_in_region(self, draw, text, font_path, region, color, gradient=None, font=None):
        """Helper method to render text within a specified region."""
        self.logger.debug(f"Rendering text: '{text}' in region: {region} with color: {color} gradient: {gradient}")

        if text is None:
            self.logger.debug("Text is None, skipping rendering")
            return region

        if region is None:
            self.logger.debug("Region is None, skipping rendering")
            return region

        if font is None:
            font, text_lines = self.calculate_text_size_to_fit(draw, text, font_path, region)
        else:
            text_lines = text

        self.logger.debug(f"Using text_lines: {text_lines}")

        x, y, width, height = region

        # Get font metrics
        ascent, descent = font.getmetrics()
        font_height = ascent + descent

        def render_text_with_gradient(text, position, bbox):
            # Convert position coordinates to integers
            position = (int(position[0]), int(position[1]))

            if gradient is None:
                draw.text(position, text, fill=color, font=font)
            else:
                # Create a temporary image for this text
                text_layer = Image.new("RGBA", (bbox[2], bbox[3]), (0, 0, 0, 0))
                text_draw = ImageDraw.Draw(text_layer)

                # Draw text in first color
                text_draw.text((0, 0), text, fill=gradient["color1"], font=font)

                # Create and apply gradient mask
                mask = self._create_gradient_mask((bbox[2], bbox[3]), gradient)

                # Create second color layer
                color2_layer = Image.new("RGBA", (bbox[2], bbox[3]), (0, 0, 0, 0))
                color2_draw = ImageDraw.Draw(color2_layer)
                color2_draw.text((0, 0), text, fill=gradient["color2"], font=font)

                # Composite using gradient mask
                text_layer.paste(color2_layer, mask=mask)

                # Paste onto main image
                draw._image.paste(text_layer, position, text_layer)

        if isinstance(text_lines, tuple):  # Two lines
            line1, line2 = text_lines
            bbox1 = draw.textbbox((0, 0), line1, font=font)
            bbox2 = draw.textbbox((0, 0), line2, font=font)

            # Calculate line heights using bounding boxes
            line1_height = bbox1[3] - bbox1[1]
            line2_height = bbox2[3] - bbox2[1]

            # Use a small gap between lines (20% of average line height)
            line_gap = int((line1_height + line2_height) * 0.1)

            # Calculate total height needed
            total_height = line1_height + line_gap + line2_height

            # Center the entire text block vertically in the region
            y_start = y + (height - total_height) // 2

            # Draw first line
            pos1 = (x + (width - bbox1[2]) // 2, y_start)
            render_text_with_gradient(line1, pos1, bbox1)

            # Draw second line
            pos2 = (x + (width - bbox2[2]) // 2, y_start + line1_height + line_gap)
            render_text_with_gradient(line2, pos2, bbox2)
        else:
            # Single line
            bbox = draw.textbbox((0, 0), text_lines, font=font)

            # Center text vertically using font metrics
            y_pos = y + (height - font_height) // 2

            position = (x + (width - bbox[2]) // 2, y_pos)
            render_text_with_gradient(text_lines, position, bbox)

        return region

    def _draw_bounding_box(self, draw, region, color):
        """Helper method to draw a bounding box around a region."""
        if region is None:
            self.logger.debug("Region is None, skipping drawing bounding box")
            return

        x, y, width, height = region
        draw.rectangle([x, y, x + width, y + height], outline=color, width=2)

    def create_video(
        self,
        extra_text,
        title_text,
        artist_text,
        format,
        output_image_filepath_noext,
        output_video_filepath,
        existing_image=None,
        duration=5,
        render_bounding_boxes=False,
        output_png=True,
        output_jpg=True,
    ):
        """Create a video with title, artist, and optional extra text."""
        self.logger.debug(f"Creating video with extra_text: '{extra_text}'")
        self.logger.debug(f"Format settings: {format}")

        resolution = (3840, 2160)  # 4K resolution
        self.logger.info(f"Creating video with format: {format}")
        self.logger.info(f"extra_text: {extra_text}, artist_text: {artist_text}, title_text: {title_text}")

        if existing_image:
            return self._handle_existing_image(existing_image, output_image_filepath_noext, output_video_filepath, duration)

        # Create or load background
        background = self._create_background(format, resolution)
        draw = ImageDraw.Draw(background)

        if format["font"] is not None:
            self.logger.info(f"Using font: {format['font']}")
            # Check if the font path is absolute
            if os.path.isabs(format["font"]):
                font_path = format["font"]
                if not os.path.exists(font_path):
                    self.logger.warning(f"Font file not found at {font_path}, falling back to default font")
                    font_path = None
            else:
                # Try to load from package resources
                try:
                    with pkg_resources.path("karaoke_prep.resources", format["font"]) as font_path:
                        font_path = str(font_path)
                except Exception as e:
                    self.logger.warning(f"Could not load font from resources: {e}, falling back to default font")
                    font_path = None

            # Render all text elements
            self._render_all_text(
                draw,
                font_path,
                title_text,
                artist_text,
                format,
                render_bounding_boxes,
            )
        else:
            self.logger.info("No font specified, skipping text rendering")

        # Save images and create video
        self._save_output_files(
            background, output_image_filepath_noext, output_video_filepath, output_png, output_jpg, duration, resolution
        )

    def _handle_existing_image(self, existing_image, output_image_filepath_noext, output_video_filepath, duration):
        """Handle case where an existing image is provided."""
        self.logger.info(f"Using existing image file: {existing_image}")
        existing_extension = os.path.splitext(existing_image)[1]

        if existing_extension == ".png":
            self.logger.info(f"Copying existing PNG image file: {existing_image}")
            shutil.copy2(existing_image, output_image_filepath_noext + existing_extension)
        else:
            self.logger.info(f"Converting existing image to PNG")
            existing_image_obj = Image.open(existing_image)
            existing_image_obj.save(output_image_filepath_noext + ".png")

        if existing_extension != ".jpg":
            self.logger.info(f"Converting existing image to JPG")
            existing_image_obj = Image.open(existing_image)
            if existing_image_obj.mode == "RGBA":
                existing_image_obj = existing_image_obj.convert("RGB")
            existing_image_obj.save(output_image_filepath_noext + ".jpg", quality=95)

        if duration > 0:
            self._create_video_from_image(output_image_filepath_noext + ".png", output_video_filepath, duration)

    def _create_background(self, format, resolution):
        """Create or load the background image."""
        if format["background_image"] and os.path.exists(format["background_image"]):
            self.logger.info(f"Using background image file: {format['background_image']}")
            background = Image.open(format["background_image"])
        else:
            self.logger.info(f"Using background color: {format['background_color']}")
            background = Image.new("RGB", resolution, color=self.hex_to_rgb(format["background_color"]))

        return background.resize(resolution)

    def _render_all_text(self, draw, font_path, title_text, artist_text, format, render_bounding_boxes):
        """Render all text elements on the image."""
        # Render title
        if format["title_region"]:
            region_parsed = self.parse_region(format["title_region"])
            region = self._render_text_in_region(
                draw, title_text, font_path, region_parsed, format["title_color"], gradient=format.get("title_gradient")
            )
            if render_bounding_boxes:
                self._draw_bounding_box(draw, region, format["title_color"])

        # Render artist
        if format["artist_region"]:
            region_parsed = self.parse_region(format["artist_region"])
            region = self._render_text_in_region(
                draw, artist_text, font_path, region_parsed, format["artist_color"], gradient=format.get("artist_gradient")
            )
            if render_bounding_boxes:
                self._draw_bounding_box(draw, region, format["artist_color"])

        # Render extra text if provided
        if format["extra_text"]:
            region_parsed = self.parse_region(format["extra_text_region"])
            region = self._render_text_in_region(
                draw, format["extra_text"], font_path, region_parsed, format["extra_text_color"], gradient=format.get("extra_text_gradient")
            )
            if render_bounding_boxes:
                self._draw_bounding_box(draw, region, format["extra_text_color"])

    def _save_output_files(
        self, background, output_image_filepath_noext, output_video_filepath, output_png, output_jpg, duration, resolution
    ):
        """Save the output image files and create video if needed."""
        # Save static background image
        if output_png:
            background.save(f"{output_image_filepath_noext}.png")

        if output_jpg:
            # Save static background image as JPG for smaller filesize
            background_rgb = background.convert("RGB")
            background_rgb.save(f"{output_image_filepath_noext}.jpg", quality=95)

        if duration > 0:
            self._create_video_from_image(f"{output_image_filepath_noext}.png", output_video_filepath, duration, resolution)

    def _create_video_from_image(self, image_path, video_path, duration, resolution=(3840, 2160)):
        """Create a video from a static image."""
        ffmpeg_command = (
            f'{self.ffmpeg_base_command} -y -loop 1 -framerate 30 -i "{image_path}" '
            f"-f lavfi -i anullsrc -c:v libx264 -r 30 -t {duration} -pix_fmt yuv420p "
            f'-vf scale={resolution[0]}:{resolution[1]} -c:a aac -shortest "{video_path}"'
        )

        self.logger.info("Generating video...")
        self.logger.debug(f"Running command: {ffmpeg_command}")
        os.system(ffmpeg_command)

    def _transform_text(self, text, transform_type):
        """Helper method to transform text based on specified type."""
        if transform_type == "uppercase":
            return text.upper()
        elif transform_type == "lowercase":
            return text.lower()
        elif transform_type == "propercase":
            return text.title()
        return text  # "none" or any other value returns original text

    def create_title_video(self, artist, title, format, output_image_filepath_noext, output_video_filepath):
        title_text = self._transform_text(title, format["title_text_transform"])
        artist_text = self._transform_text(artist, format["artist_text_transform"])
        self.create_video(
            title_text=title_text,
            artist_text=artist_text,
            extra_text=format["extra_text"],
            format=format,
            output_image_filepath_noext=output_image_filepath_noext,
            output_video_filepath=output_video_filepath,
            existing_image=self.existing_title_image,
            duration=self.intro_video_duration,
            render_bounding_boxes=self.render_bounding_boxes,
            output_png=self.output_png,
            output_jpg=self.output_jpg,
        )

    def create_end_video(self, artist, title, format, output_image_filepath_noext, output_video_filepath):
        title_text = self._transform_text(title, format["title_text_transform"])
        artist_text = self._transform_text(artist, format["artist_text_transform"])
        self.create_video(
            title_text=title_text,
            artist_text=artist_text,
            extra_text=format["extra_text"],
            format=format,
            output_image_filepath_noext=output_image_filepath_noext,
            output_video_filepath=output_video_filepath,
            existing_image=self.existing_end_image,
            duration=self.end_video_duration,
            render_bounding_boxes=self.render_bounding_boxes,
            output_png=self.output_png,
            output_jpg=self.output_jpg,
        )

    def hex_to_rgb(self, hex_color):
        """Convert hex color to RGB tuple."""
        hex_color = hex_color.lstrip("#")
        return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))

    def process_audio_separation(self, audio_file, artist_title, track_output_dir):
        from audio_separator.separator import Separator

        self.logger.info(f"Starting audio separation process for {artist_title}")

        # Define lock file path in system temp directory
        lock_file_path = os.path.join(tempfile.gettempdir(), "audio_separator.lock")

        # Try to acquire lock
        while True:
            try:
                # First check if there's a stale lock
                if os.path.exists(lock_file_path):
                    try:
                        with open(lock_file_path, "r") as f:
                            lock_data = json.load(f)
                            pid = lock_data.get("pid")
                            start_time = datetime.fromisoformat(lock_data.get("start_time"))
                            running_track = lock_data.get("track")

                            # Check if process is still running
                            if not psutil.pid_exists(pid):
                                self.logger.warning(f"Found stale lock from dead process {pid}, removing...")
                                os.remove(lock_file_path)
                            else:
                                # Calculate runtime
                                runtime = datetime.now() - start_time
                                runtime_mins = runtime.total_seconds() / 60

                                # Get process command line
                                proc = psutil.Process(pid)
                                cmd = " ".join(proc.cmdline())

                                self.logger.info(
                                    f"Waiting for other audio separation process to complete before starting separation for {artist_title}...\n"
                                    f"Currently running process details:\n"
                                    f"  Track: {running_track}\n"
                                    f"  PID: {pid}\n"
                                    f"  Running time: {runtime_mins:.1f} minutes\n"
                                    f"  Command: {cmd}\n"
                                    f"To force clear the lock and kill the process, run:\n"
                                    f"  kill {pid} && rm {lock_file_path}"
                                )
                    except (json.JSONDecodeError, KeyError, ValueError) as e:
                        self.logger.warning(f"Found invalid lock file, removing: {e}")
                        os.remove(lock_file_path)

                # Try to acquire lock
                lock_file = open(lock_file_path, "w")
                fcntl.flock(lock_file.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)

                # Write metadata to lock file
                lock_data = {
                    "pid": os.getpid(),
                    "start_time": datetime.now().isoformat(),
                    "track": f"{artist_title}",
                }
                json.dump(lock_data, lock_file)
                lock_file.flush()
                break

            except IOError as e:
                if e.errno != errno.EAGAIN:
                    raise
                # Lock is held by another process
                time.sleep(30)  # Wait 30 seconds before trying again
                continue

        try:
            separator = Separator(
                log_level=self.log_level,
                log_formatter=self.log_formatter,
                model_file_dir=self.model_file_dir,
                output_format=self.lossless_output_format,
            )

            stems_dir = self._create_stems_directory(track_output_dir)
            result = {"clean_instrumental": {}, "other_stems": {}, "backing_vocals": {}, "combined_instrumentals": {}}

            if os.environ.get("KARAOKE_PREP_SKIP_AUDIO_SEPARATION"):
                return result

            result["clean_instrumental"] = self._separate_clean_instrumental(
                separator, audio_file, artist_title, track_output_dir, stems_dir
            )
            result["other_stems"] = self._separate_other_stems(separator, audio_file, artist_title, stems_dir)
            result["backing_vocals"] = self._separate_backing_vocals(
                separator, result["clean_instrumental"]["vocals"], artist_title, stems_dir
            )
            result["combined_instrumentals"] = self._generate_combined_instrumentals(
                result["clean_instrumental"]["instrumental"], result["backing_vocals"], artist_title, track_output_dir
            )
            self._normalize_audio_files(result, artist_title, track_output_dir)

            # Create Audacity LOF file
            lof_path = os.path.join(stems_dir, f"{artist_title} (Audacity).lof")
            first_model = list(result["backing_vocals"].keys())[0]

            files_to_include = [
                audio_file,  # Original audio
                result["clean_instrumental"]["instrumental"],  # Clean instrumental
                result["backing_vocals"][first_model]["backing_vocals"],  # Backing vocals
                result["combined_instrumentals"][first_model],  # Combined instrumental+BV
            ]

            # Convert to absolute paths
            files_to_include = [os.path.abspath(f) for f in files_to_include]

            with open(lof_path, "w") as lof:
                for file_path in files_to_include:
                    lof.write(f'file "{file_path}"\n')

            self.logger.info(f"Created Audacity LOF file: {lof_path}")
            result["audacity_lof"] = lof_path

            # Launch Audacity with multiple tracks
            if sys.platform == "darwin":  # Check if we're on macOS
                if lof_path and os.path.exists(lof_path):
                    self.logger.info(f"Launching Audacity with LOF file: {lof_path}")
                    os.system(f'open -a Audacity "{lof_path}"')
                else:
                    self.logger.debug("Audacity LOF file not available or not found")

            self.logger.info("Audio separation, combination, and normalization process completed")
            return result
        finally:
            # Release lock
            fcntl.flock(lock_file.fileno(), fcntl.LOCK_UN)
            lock_file.close()
            try:
                os.remove(lock_file_path)
            except OSError:
                pass

    def _create_stems_directory(self, track_output_dir):
        stems_dir = os.path.join(track_output_dir, "stems")
        os.makedirs(stems_dir, exist_ok=True)
        self.logger.info(f"Created stems directory: {stems_dir}")
        return stems_dir

    def _separate_clean_instrumental(self, separator, audio_file, artist_title, track_output_dir, stems_dir):
        self.logger.info(f"Separating using clean instrumental model: {self.clean_instrumental_model}")
        instrumental_path = os.path.join(
            track_output_dir, f"{artist_title} (Instrumental {self.clean_instrumental_model}).{self.lossless_output_format}"
        )
        vocals_path = os.path.join(stems_dir, f"{artist_title} (Vocals {self.clean_instrumental_model}).{self.lossless_output_format}")

        result = {}
        if not self._file_exists(instrumental_path) or not self._file_exists(vocals_path):
            separator.load_model(model_filename=self.clean_instrumental_model)
            clean_output_files = separator.separate(audio_file)

            for file in clean_output_files:
                if "(Vocals)" in file and not self._file_exists(vocals_path):
                    os.rename(file, vocals_path)
                    result["vocals"] = vocals_path
                elif "(Instrumental)" in file and not self._file_exists(instrumental_path):
                    os.rename(file, instrumental_path)
                    result["instrumental"] = instrumental_path
        else:
            result["vocals"] = vocals_path
            result["instrumental"] = instrumental_path

        return result

    def _separate_other_stems(self, separator, audio_file, artist_title, stems_dir):
        self.logger.info(f"Separating using other stems models: {self.other_stems_models}")
        result = {}
        for model in self.other_stems_models:
            self.logger.info(f"Processing with model: {model}")
            result[model] = {}

            # Check if any stem files for this model already exist
            existing_stems = glob.glob(os.path.join(stems_dir, f"{artist_title} (*{model}).{self.lossless_output_format}"))

            if existing_stems:
                self.logger.info(f"Found existing stem files for model {model}, skipping separation")
                for stem_file in existing_stems:
                    stem_name = os.path.basename(stem_file).split("(")[1].split(")")[0].strip()
                    result[model][stem_name] = stem_file
            else:
                separator.load_model(model_filename=model)
                other_stems_output = separator.separate(audio_file)

                for file in other_stems_output:
                    file_name = os.path.basename(file)
                    stem_name = file_name[file_name.rfind("_(") + 2 : file_name.rfind(")_")]
                    new_filename = f"{artist_title} ({stem_name} {model}).{self.lossless_output_format}"
                    other_stem_path = os.path.join(stems_dir, new_filename)
                    if not self._file_exists(other_stem_path):
                        os.rename(file, other_stem_path)
                    result[model][stem_name] = other_stem_path

        return result

    def _separate_backing_vocals(self, separator, vocals_path, artist_title, stems_dir):
        self.logger.info(f"Separating clean vocals using backing vocals models: {self.backing_vocals_models}")
        result = {}
        for model in self.backing_vocals_models:
            self.logger.info(f"Processing with model: {model}")
            result[model] = {}
            lead_vocals_path = os.path.join(stems_dir, f"{artist_title} (Lead Vocals {model}).{self.lossless_output_format}")
            backing_vocals_path = os.path.join(stems_dir, f"{artist_title} (Backing Vocals {model}).{self.lossless_output_format}")

            if not self._file_exists(lead_vocals_path) or not self._file_exists(backing_vocals_path):
                separator.load_model(model_filename=model)
                backing_vocals_output = separator.separate(vocals_path)

                for file in backing_vocals_output:
                    if "(Vocals)" in file and not self._file_exists(lead_vocals_path):
                        os.rename(file, lead_vocals_path)
                        result[model]["lead_vocals"] = lead_vocals_path
                    elif "(Instrumental)" in file and not self._file_exists(backing_vocals_path):
                        os.rename(file, backing_vocals_path)
                        result[model]["backing_vocals"] = backing_vocals_path
            else:
                result[model]["lead_vocals"] = lead_vocals_path
                result[model]["backing_vocals"] = backing_vocals_path
        return result

    def _generate_combined_instrumentals(self, instrumental_path, backing_vocals_result, artist_title, track_output_dir):
        self.logger.info("Generating combined instrumental tracks with backing vocals")
        result = {}
        for model, paths in backing_vocals_result.items():
            backing_vocals_path = paths["backing_vocals"]
            combined_path = os.path.join(track_output_dir, f"{artist_title} (Instrumental +BV {model}).{self.lossless_output_format}")

            if not self._file_exists(combined_path):
                ffmpeg_command = (
                    f'{self.ffmpeg_base_command} -i "{instrumental_path}" -i "{backing_vocals_path}" '
                    f'-filter_complex "[0:a][1:a]amix=inputs=2:duration=longest:weights=1 1" '
                    f'-c:a {self.lossless_output_format.lower()} "{combined_path}"'
                )

                self.logger.debug(f"Running command: {ffmpeg_command}")
                os.system(ffmpeg_command)

            result[model] = combined_path
        return result

    def _normalize_audio_files(self, separation_result, artist_title, track_output_dir):
        self.logger.info("Normalizing clean instrumental and combined instrumentals")

        files_to_normalize = [
            ("clean_instrumental", separation_result["clean_instrumental"]["instrumental"]),
        ] + [("combined_instrumentals", path) for path in separation_result["combined_instrumentals"].values()]

        for key, file_path in files_to_normalize:
            if self._file_exists(file_path):
                try:
                    self._normalize_audio(file_path, file_path)  # Normalize in-place

                    # Verify the normalized file
                    if os.path.getsize(file_path) > 0:
                        self.logger.info(f"Successfully normalized: {file_path}")
                    else:
                        raise Exception("Normalized file is empty")

                except Exception as e:
                    self.logger.error(f"Error during normalization of {file_path}: {e}")
                    self.logger.warning(f"Normalization failed for {file_path}. Original file remains unchanged.")
            else:
                self.logger.warning(f"File not found for normalization: {file_path}")

        self.logger.info("Audio normalization process completed")

    def _normalize_audio(self, input_path, output_path, target_level=0.0):
        self.logger.info(f"Normalizing audio file: {input_path}")

        # Load audio file
        audio = AudioSegment.from_file(input_path, format=self.lossless_output_format.lower())

        # Calculate the peak amplitude
        peak_amplitude = float(audio.max_dBFS)

        # Calculate the necessary gain
        gain_db = target_level - peak_amplitude

        # Apply gain
        normalized_audio = audio.apply_gain(gain_db)

        # Ensure the audio is not completely silent
        if normalized_audio.rms == 0:
            self.logger.warning(f"Normalized audio is silent for {input_path}. Using original audio.")
            normalized_audio = audio

        # Export normalized audio, overwriting the original file
        normalized_audio.export(output_path, format=self.lossless_output_format.lower())

        self.logger.info(f"Normalized audio saved, replacing: {output_path}")
        self.logger.debug(f"Original peak: {peak_amplitude} dB, Applied gain: {gain_db} dB")

    def _file_exists(self, file_path):
        """Check if a file exists and log the result."""
        exists = os.path.isfile(file_path)
        if exists:
            self.logger.info(f"File already exists, skipping creation: {file_path}")
        return exists

    async def prep_single_track(self):
        # Add signal handler at the start
        loop = asyncio.get_running_loop()
        for sig in (signal.SIGINT, signal.SIGTERM):
            loop.add_signal_handler(sig, lambda s=sig: asyncio.create_task(self.shutdown(s)))

        try:
            self.logger.info(f"Preparing single track: {self.artist} - {self.title}")

            if self.input_media is not None and os.path.isfile(self.input_media):
                self.extractor = "Original"
            else:
                self.parse_single_track_metadata(input_artist=self.artist, input_title=self.title)

            self.logger.info(f"Preparing output path for track: {self.title} by {self.artist}")
            if self.dry_run:
                return None

            track_output_dir, artist_title = self.setup_output_paths(self.artist, self.title)

            processed_track = {
                "track_output_dir": track_output_dir,
                "artist": self.artist,
                "title": self.title,
                "extractor": self.extractor,
                "extracted_info": self.extracted_info,
                "lyrics": None,
                "processed_lyrics": None,
                "separated_audio": {},
            }

            processed_track["input_media"] = None
            processed_track["input_still_image"] = None
            processed_track["input_audio_wav"] = None

            if self.input_media is not None and os.path.isfile(self.input_media):
                input_wav_filename_pattern = os.path.join(track_output_dir, f"{artist_title} ({self.extractor} *.wav")
                input_wav_glob = glob.glob(input_wav_filename_pattern)

                if input_wav_glob:
                    processed_track["input_audio_wav"] = input_wav_glob[0]
                    self.logger.info(f"Input media WAV file already exists, skipping conversion: {processed_track['input_audio_wav']}")
                else:
                    output_filename_no_extension = os.path.join(track_output_dir, f"{artist_title} ({self.extractor})")

                    self.logger.info(f"Copying input media from {self.input_media} to new directory...")
                    processed_track["input_media"] = self.copy_input_media(self.input_media, output_filename_no_extension)

                    self.logger.info("Converting input media to WAV for audio processing...")
                    processed_track["input_audio_wav"] = self.convert_to_wav(processed_track["input_media"], output_filename_no_extension)

            else:
                # WebM may not always be the output format from ytdlp, but it's common and this is just a convenience cache
                input_webm_filename_pattern = os.path.join(track_output_dir, f"{artist_title} ({self.extractor} *.webm")
                input_webm_glob = glob.glob(input_webm_filename_pattern)

                input_png_filename_pattern = os.path.join(track_output_dir, f"{artist_title} ({self.extractor} *.png")
                input_png_glob = glob.glob(input_png_filename_pattern)

                input_wav_filename_pattern = os.path.join(track_output_dir, f"{artist_title} ({self.extractor} *.wav")
                input_wav_glob = glob.glob(input_wav_filename_pattern)

                if input_webm_glob and input_png_glob and input_wav_glob:
                    processed_track["input_media"] = input_webm_glob[0]
                    processed_track["input_still_image"] = input_png_glob[0]
                    processed_track["input_audio_wav"] = input_wav_glob[0]

                    self.logger.info(f"Input media files already exist, skipping download: {processed_track['input_media']} + .wav + .png")
                else:
                    if self.url:
                        output_filename_no_extension = os.path.join(track_output_dir, f"{artist_title} ({self.extractor} {self.media_id})")

                        self.logger.info(f"Downloading input media from {self.url}...")
                        processed_track["input_media"] = self.download_video(self.url, output_filename_no_extension)

                        self.logger.info("Extracting still image from downloaded media (if input is video)...")
                        processed_track["input_still_image"] = self.extract_still_image_from_video(
                            processed_track["input_media"], output_filename_no_extension
                        )

                        self.logger.info("Converting downloaded video to WAV for audio processing...")
                        processed_track["input_audio_wav"] = self.convert_to_wav(
                            processed_track["input_media"], output_filename_no_extension
                        )
                    else:
                        self.logger.warning(f"Skipping download due to missing URL.")

            if self.skip_lyrics:
                self.logger.info("Skipping lyrics fetch as requested.")
                processed_track["lyrics"] = None
                processed_track["processed_lyrics"] = None
            else:
                lyrics_artist = self.lyrics_artist or self.artist
                lyrics_title = self.lyrics_title or self.title

                # Create futures for both operations
                transcription_future = None
                separation_future = None

                self.logger.info("=== Starting Parallel Processing ===")

                if not self.skip_lyrics:
                    self.logger.info("Creating transcription future...")
                    # Run transcription in a separate thread
                    transcription_future = asyncio.create_task(
                        asyncio.to_thread(
                            self.transcribe_lyrics, processed_track["input_audio_wav"], lyrics_artist, lyrics_title, track_output_dir
                        )
                    )
                    self.logger.info(f"Transcription future created, type: {type(transcription_future)}")

                if not self.existing_instrumental:
                    self.logger.info("Creating separation future...")
                    # Run separation in a separate thread
                    separation_future = asyncio.create_task(
                        asyncio.to_thread(
                            self.process_audio_separation,
                            audio_file=processed_track["input_audio_wav"],
                            artist_title=artist_title,
                            track_output_dir=track_output_dir,
                        )
                    )
                    self.logger.info(f"Separation future created, type: {type(separation_future)}")

                self.logger.info("About to await both operations with asyncio.gather...")
                # Wait for both operations to complete
                try:
                    results = await asyncio.gather(
                        transcription_future if transcription_future else asyncio.sleep(0),
                        separation_future if separation_future else asyncio.sleep(0),
                        return_exceptions=True,
                    )
                except asyncio.CancelledError:
                    self.logger.info("Received cancellation request, cleaning up...")
                    # Cancel any running futures
                    if transcription_future and not transcription_future.done():
                        transcription_future.cancel()
                    if separation_future and not separation_future.done():
                        separation_future.cancel()
                    # Wait for futures to complete cancellation
                    await asyncio.gather(
                        transcription_future if transcription_future else asyncio.sleep(0),
                        separation_future if separation_future else asyncio.sleep(0),
                        return_exceptions=True,
                    )
                    raise

                # Handle transcription results
                if transcription_future:
                    self.logger.info("Processing transcription results...")
                    try:
                        transcriber_outputs = results[0]
                        if isinstance(transcriber_outputs, Exception):
                            self.logger.error(f"Error during lyrics transcription: {transcriber_outputs}")
                            raise transcriber_outputs  # Re-raise the exception
                        elif transcriber_outputs:
                            self.logger.info("Successfully received transcription outputs")
                            self.lyrics = transcriber_outputs.get("corrected_lyrics_text")
                            processed_track["lyrics"] = transcriber_outputs.get("corrected_lyrics_text_filepath")
                    except Exception as e:
                        self.logger.error(f"Error processing transcription results: {e}")
                        self.logger.exception("Full traceback:")
                        raise  # Re-raise the exception

                # Handle separation results
                if separation_future:
                    self.logger.info("Processing separation results...")
                    try:
                        separation_results = results[1]
                        if isinstance(separation_results, Exception):
                            self.logger.error(f"Error during audio separation: {separation_results}")
                        else:
                            self.logger.info("Successfully received separation results")
                            processed_track["separated_audio"] = separation_results
                    except Exception as e:
                        self.logger.error(f"Error processing separation results: {e}")
                        self.logger.exception("Full traceback:")

                self.logger.info("=== Parallel Processing Complete ===")

            output_image_filepath_noext = os.path.join(track_output_dir, f"{artist_title} (Title)")
            processed_track["title_image_png"] = f"{output_image_filepath_noext}.png"
            processed_track["title_image_jpg"] = f"{output_image_filepath_noext}.jpg"
            processed_track["title_video"] = os.path.join(track_output_dir, f"{artist_title} (Title).mov")

            if not self._file_exists(processed_track["title_video"]) and not os.environ.get("KARAOKE_PREP_SKIP_TITLE_END_SCREENS"):
                self.logger.info(f"Creating title video...")
                self.create_title_video(
                    self.artist, self.title, self.title_format, output_image_filepath_noext, processed_track["title_video"]
                )

            output_image_filepath_noext = os.path.join(track_output_dir, f"{artist_title} (End)")
            processed_track["end_image_png"] = f"{output_image_filepath_noext}.png"
            processed_track["end_image_jpg"] = f"{output_image_filepath_noext}.jpg"
            processed_track["end_video"] = os.path.join(track_output_dir, f"{artist_title} (End).mov")

            if not self._file_exists(processed_track["end_video"]) and not os.environ.get("KARAOKE_PREP_SKIP_TITLE_END_SCREENS"):
                self.logger.info(f"Creating end screen video...")
                self.create_end_video(self.artist, self.title, self.end_format, output_image_filepath_noext, processed_track["end_video"])

            if self.existing_instrumental:
                self.logger.info(f"Using existing instrumental file: {self.existing_instrumental}")
                existing_instrumental_extension = os.path.splitext(self.existing_instrumental)[1]

                instrumental_path = os.path.join(track_output_dir, f"{artist_title} (Instrumental Custom){existing_instrumental_extension}")

                if not self._file_exists(instrumental_path):
                    shutil.copy2(self.existing_instrumental, instrumental_path)

                processed_track["separated_audio"]["Custom"] = {
                    "instrumental": instrumental_path,
                    "vocals": None,
                }
            else:
                self.logger.info(f"Separating audio for track: {self.title} by {self.artist}")
                separation_results = self.process_audio_separation(
                    audio_file=processed_track["input_audio_wav"], artist_title=artist_title, track_output_dir=track_output_dir
                )
                processed_track["separated_audio"] = separation_results

            self.logger.info("Script finished, audio downloaded, lyrics fetched and audio separated!")

            return processed_track

        except Exception as e:
            self.logger.error(f"Error in prep_single_track: {e}")
            raise
        finally:
            # Remove signal handlers
            for sig in (signal.SIGINT, signal.SIGTERM):
                loop.remove_signal_handler(sig)

    async def shutdown(self, signal):
        """Cleanup tasks tied to the service's shutdown."""
        self.logger.info(f"Received exit signal {signal.name}...")

        tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]

        [task.cancel() for task in tasks]

        self.logger.info(f"Cancelling {len(tasks)} outstanding tasks")
        await asyncio.gather(*tasks, return_exceptions=True)

        loop = asyncio.get_running_loop()
        loop.stop()

    async def process_playlist(self):
        if self.artist is None or self.title is None:
            raise Exception("Error: Artist and Title are required for processing a local file.")

        if "entries" in self.extracted_info:
            track_results = []
            self.logger.info(f"Found {len(self.extracted_info['entries'])} entries in playlist, processing each invididually...")
            for entry in self.extracted_info["entries"]:
                self.extracted_info = entry
                self.logger.info(f"Processing playlist entry with title: {self.extracted_info['title']}")
                if not self.dry_run:
                    track_results.append(await self.prep_single_track())
                self.artist = self.persistent_artist
                self.title = None
            return track_results
        else:
            raise Exception(f"Failed to find 'entries' in playlist, cannot process")

    async def process_folder(self):
        if self.filename_pattern is None or self.artist is None:
            raise Exception("Error: Filename pattern and artist are required for processing a folder.")

        folder_path = self.input_media
        output_folder_path = os.path.join(os.getcwd(), os.path.basename(folder_path))

        if not os.path.exists(output_folder_path):
            if not self.dry_run:
                self.logger.info(f"DRY RUN: Would create output folder: {output_folder_path}")
                os.makedirs(output_folder_path)
        else:
            self.logger.info(f"Output folder already exists: {output_folder_path}")

        pattern = re.compile(self.filename_pattern)
        tracks = []

        for filename in sorted(os.listdir(folder_path)):
            match = pattern.match(filename)
            if match:
                title = match.group("title")
                file_path = os.path.join(folder_path, filename)
                self.input_media = file_path
                self.title = title

                track_index = match.group("index") if "index" in match.groupdict() else None

                self.logger.info(f"Processing track: {track_index} with title: {title} from file: {filename}")

                track_output_dir = os.path.join(output_folder_path, f"{track_index} - {self.artist} - {title}")

                if not self.dry_run:
                    track = await self.prep_single_track()
                    tracks.append(track)

                    # Move the track folder to the output folder
                    track_folder = track["track_output_dir"]
                    shutil.move(track_folder, track_output_dir)
                else:
                    self.logger.info(f"DRY RUN: Would move track folder to: {os.path.basename(track_output_dir)}")

        return tracks

    async def process(self):
        if self.input_media is not None and os.path.isdir(self.input_media):
            self.logger.info(f"Input media {self.input_media} is a local folder, processing each file individually...")
            return await self.process_folder()
        elif self.input_media is not None and os.path.isfile(self.input_media):
            self.logger.info(f"Input media {self.input_media} is a local file, youtube logic will be skipped")
            return [await self.prep_single_track()]
        else:
            self.url = self.input_media
            self.extract_info_for_online_media(input_url=self.url, input_artist=self.artist, input_title=self.title)

            if self.extracted_info and "playlist_count" in self.extracted_info:
                self.persistent_artist = self.artist
                self.logger.info(f"Input URL is a playlist, beginning batch operation with persistent artist: {self.persistent_artist}")
                return await self.process_playlist()
            else:
                self.logger.info(f"Input URL is not a playlist, processing single track")
                return [await self.prep_single_track()]
