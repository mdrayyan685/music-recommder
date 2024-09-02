import pygame
import os
import time
from mutagen.mp3 import MP3
from tkinter import Tk, filedialog

# Function to select music directory
def select_music_directory():
    root = Tk()
    root.withdraw()
    music_directory = filedialog.askdirectory()
    root.destroy()
    return music_directory

# Function to load music files from directory
def load_music_files(directory):
    music_files = []
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.mp3'):
                music_files.append(os.path.join(dirpath, filename))
    return music_files

# Function to display lyrics
def display_lyrics(lyrics):
    for line in lyrics:
        print(line)
        time.sleep(1)  # Adjust delay as needed

# Function to play music with synchronized lyrics
def play_music(music_file, lyrics):
    pygame.mixer.init()
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()
    audio_length = MP3(music_file).info.length
    
    display_lyrics(lyrics)
    
    # Wait for audio to finish playing
    time.sleep(audio_length)
    pygame.mixer.music.stop()

def main():
    music_directory = select_music_directory()
    music_files = load_music_files(music_directory)

    if not music_files:
        print("No music files found in the selected directory.")
        return

    for i, music_file in enumerate(music_files):
        print(f"{i+1}. {os.path.basename(music_file)}")

    selection = int(input("Enter the number of the song you want to play: ")) - 1

    if selection < 0 or selection >= len(music_files):
        print("Invalid selection.")
        return

    # Dummy lyrics (replace with actual lyrics retrieval logic)
    lyrics = ["Verse 1: Dummy lyrics for demonstration purposes.",
              "Chorus: Dummy chorus lyrics.",
              "Verse 2: More dummy lyrics.",
              "Bridge: This is just a sample."]
    
    play_music(music_files[selection], lyrics)

if __name__ == "__main__":
    main()

