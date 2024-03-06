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

Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests.

### License

This project is open source and available under the MIT License.
