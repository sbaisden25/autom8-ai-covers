import os
import subprocess


def split_songs(song_directory):
    """
    This function splits songs into different components using demucs.
    
    :param song_directory: The directory where the song files are located.
    """

    # Get a list of all song files in the directory
    song_files = os.listdir(song_directory)
    
    # Iterate through each song file
    for song_file in song_files:
        
        # Join the directory path and the song file name
        song_path = os.path.join(song_directory, song_file)
        
        print(f"Processing {song_path}...")
        
        # Split the song using the 'demucs' command
        # Note: This assumes that 'demucs' is installed and added to your system's PATH
        subprocess.call(["demucs", "-n", "mdx_extra", song_path])
        
        print(f"Finished processing {song_path}.")


if __name__ == "__main__":
    # Define the directory where your songs are located
    song_directory = 'YOUR_SONG_DIRECTORY'
    
    # Call the function to start splitting songs
    split_songs(song_directory)
