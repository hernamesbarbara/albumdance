#!/usr/bin/env python

"""
Usage:
    albumdance.py <input_media> <metadata> <cover_art>

Options:
    -h --help     Show this screen.

Arguments:
    input_media   Path to the input media file (mp3, mp4, webm, etc.).
    metadata      Path to the CSV file containing song metadata.
    cover_art     Path to the cover art image (jpg or png).
"""

import os
import pandas as pd
from pydub import AudioSegment
import eyed3
from docopt import docopt
import subprocess


def parse_duration(duration_str):
    """Converts a duration string in HH:MM:SS format to milliseconds."""
    h, m, s = map(int, duration_str.split(':'))
    return ((h * 3600) + (m * 60) + s) * 1000


def main(args):
    input_media = args['<input_media>']
    metadata_path = args['<metadata>']
    cover_art_path = args['<cover_art>']

    # Read the CSV metadata
    df = pd.read_csv(metadata_path)

    # Determine the album name and create an output directory named after it
    album_name = df['album'].iloc[0]
    output_dir = os.path.join(os.getcwd(), album_name)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Load the input media file
    if input_media.endswith('.mp3'):
        audio = AudioSegment.from_mp3(input_media)
    elif input_media.endswith('.mp4'):
        audio = AudioSegment.from_file(input_media, 'mp4')
    elif input_media.endswith('.webm'):
        audio = AudioSegment.from_file(input_media, 'webm')
    else:
        print("Unsupported file format")
        return

    start_time = 0
    for index, row in df.iterrows():
        # Calculate missing start and end times if necessary
        if pd.isna(row['start_HH:MM:SS']):
            df.at[index, 'start_HH:MM:SS'] = str(
                pd.to_timedelta(start_time, unit='ms'))
        if pd.isna(row['end_HH:MM:SS']):
            duration_ms = parse_duration(row['duration_HH:MM:SS'])
            end_time = start_time + duration_ms
            df.at[index, 'end_HH:MM:SS'] = str(
                pd.to_timedelta(end_time, unit='ms'))
            start_time = end_time

        # Extract and convert the track
        start_ms = parse_duration(row['start_HH:MM:SS'])
        end_ms = parse_duration(row['end_HH:MM:SS'])
        track_audio = audio[start_ms:end_ms]
        intermediate_track_path = os.path.join(
            output_dir, f"{row['title']}_temp.mp3")
        final_track_path = os.path.join(output_dir, f"{row['title']}.mp3")

        # Export using pydub (temporary file)
        track_audio.export(intermediate_track_path, format="mp3")

        # Re-encode the audio file using ffmpeg for consistent encoding
        ffmpeg_cmd = [
            "ffmpeg", "-i", intermediate_track_path, "-ab", "192k", "-map_metadata", "0",
            "-metadata", f"comment={row['comment']}",
            "-metadata", f"album={row['album']}",
            "-metadata", f"genre={row['genre']}",
            "-metadata", f"date={row['date']}",
            "-metadata", f"title={row['title']}",
            "-metadata", f"artist={row['artist']}",
            "-metadata", f"track={row['track']}",
            final_track_path
        ]

        try:
            subprocess.run(ffmpeg_cmd, check=True)
            # Delete the temporary file after re-encoding
            os.remove(intermediate_track_path)
        except subprocess.CalledProcessError as e:
            print(f"Error during re-encoding: {e}")
            continue

        # Assign metadata using eyed3 (optional since ffmpeg already does it)
        # You can remove this part if ffmpeg's metadata assignment is sufficient
        track_file = eyed3.load(final_track_path)
        if track_file.tag is None:
            track_file.initTag()

        track_file.tag.title = str(row['title'])
        track_file.tag.artist = str(row['artist'])
        track_file.tag.album = str(row['album'])
        track_file.tag.recording_date = str(row['date'])
        track_file.tag.genre = str(row['genre'])
        track_file.tag.comments.set(row['comment'])

        # Add cover art
        with open(cover_art_path, 'rb') as img_file:
            track_file.tag.images.set(
                3, img_file.read(), 'image/jpeg', 'Cover art')

        track_file.tag.save()

    print(f"Processing complete. Tracks saved to {output_dir}")


if __name__ == "__main__":
    arguments = docopt(__doc__)
    main(arguments)
