# Album Dance

Split a single audio file into multiple tracks, exporting each track as an MP3 file.

`albumdance` will tag each song with metadata including title, artist, album, genre, and more.

This tool is particularly useful for processing albums, live recordings, or any audio file that contains multiple songs or segments that need to be individually tracked and tagged.

## Features

- Splits a single audio file into multiple tracks based on metadata.
- Supports various input formats (mp3, mp4, webm, etc.).
- Assigns metadata to each track, including title, artist, album, and more.
- Embeds cover art into each track.
- Ensures consistent encoding across all tracks to avoid playback issues.

## Prerequisites

Before you begin, ensure you have installed:

- Python 3.x
- FFmpeg (for audio processing and encoding)
- Required Python packages: `pydub`, `eyed3`, `pandas`, and `docopt`.

## Installation

1. Clone this repository or download the source code to your local machine.
2. Install the required Python packages:

```bash
pip install pydub eyed3 pandas docopt
```

## Usage

To use Album Dance, navigate to the directory containing the script and run:

```bash
./albumdance.py <input_media> <metadata.csv> <cover_art.jpg>
```

## Arguments:

- `<input_media>`: Path to the input media file (mp3, mp4, webm, etc.).
- `<metadata.csv>`: Path to the CSV file containing song metadata.
- `<cover_art.jpg>`: Path to the cover art image (jpg or png).

## Metadata CSV Format

The `metadata.csv` contains song metadata used to split the audio file and tag each track.

Below is the format of the CSV file along with a sample row of data:

| Column Name         | Description                                              | Example           |
| ------------------- | -------------------------------------------------------- | ----------------- |
| `title`             | The title of the track                                   | Fall Children     |
| `artist`            | The artist of the track                                  | A.F.I.            |
| `album_artist`      | The album artist                                         | A.F.I.            |
| `album`             | The album name                                           | All Hallow's - EP |
| `genre`             | The genre of the track                                   | Punk              |
| `track`             | The track number/total number of tracks in the album     | 1/4               |
| `date`              | The release date of the track                            | 1999              |
| `compilation`       | Indicates if the track is part of a compilation (0 or 1) | 0                 |
| `media_type`        | The type of media (numeric representation)               | 1                 |
| `comment`           | Any additional comments                                  | SF Punk           |
| `start_HH:MM:SS`    | The start time of the track in the input media           | 00:00:00          |
| `end_HH:MM:SS`      | The end time of the track in the input media             | 00:03:12          |
| `duration_HH:MM:SS` | The duration of the track                                | 00:03:12          |

Ensure your `metadata.csv` file follows this format. A sample file is included in the repository for reference.

Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests.

### License

This project is open source and available under the MIT License.
