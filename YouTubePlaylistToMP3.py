import os
import shutil
import subprocess
from pytube import Playlist, YouTube


def download_playlist(url, destination):
    """
    Download all the songs from the given playlist URL to the specified destination directory.
    
    :param url: The URL of the YouTube playlist
    :param destination: The directory where the downloaded songs should be stored
    """
    
    # Create a Playlist object using Pytube
    playlist = Playlist(url)
    
    # Download songs from the playlist
    download_songs_from_playlist(playlist, destination)


def download_songs_from_playlist(playlist, destination):
    """
    Download songs from the playlist.
    
    :param playlist: The Playlist object containing video URLs
    :param destination: The directory where the downloaded songs should be stored
    """
    
    # Iterate through each video URL in the playlist
    for video_url in playlist.video_urls:
        download_song(video_url, destination)


def download_song(url, destination):
    """
    Download a single song from the given URL and convert it to mp3 format.
    
    :param url: The URL of the YouTube video
    :param destination: The directory where the downloaded song should be stored
    """
    
    # Create a YouTube object using Pytube
    yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
    
    # Get the highest resolution stream available as mp4
    music_stream = yt.streams.filter(file_extension="mp4").first()
    default_filename = music_stream.default_filename
    
    print(f"Downloading {default_filename}...")
    music_stream.download()
    
    # Remove spaces from the filename
    filename_no_spaces = default_filename.replace(" ", "")
    os.rename(default_filename, filename_no_spaces)
    
    # Convert the mp4 file to mp3
    new_filename = filename_no_spaces.replace("mp4", "mp3")
    print(f"Converting {filename_no_spaces} to mp3...")
    subprocess.call(f"ffmpeg -i {filename_no_spaces} {new_filename}", shell=True)
    
    # Move the mp3 file to the destination directory
    abs_destination = os.path.abspath(destination if destination else "./Downloads")
    os.makedirs(abs_destination, exist_ok=True)
    shutil.move(new_filename, os.path.join(abs_destination, new_filename))
    
    # Remove the original mp4 file
    os.remove(filename_no_spaces)


if __name__ == "__main__":
    # Example Usage:
    # Replace 'YOUR_PLAYLIST_URL' with the URL of your YouTube playlist
    # Replace 'YOUR_DESTINATION_DIRECTORY' with your desired destination directory
    download_playlist('YOUR_PLAYLIST_URL', 'YOUR_DESTINATION_DIRECTORY')
