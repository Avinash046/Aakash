import webbrowser
import os

def handle(command):
    command = command.lower()
    if 'music' in command or 'song' in command:
        print("Aakash: Opening YouTube Music...")
        webbrowser.open('https://music.youtube.com/')
    elif 'movie' in command or 'video' in command:
        print("Aakash: Opening YouTube Movies...")
        webbrowser.open('https://www.youtube.com/movies')
    elif 'play' in command and 'file' in command:
        # Example: play file /path/to/song.mp3
        parts = command.split()
        for i, part in enumerate(parts):
            if part == 'file' and i+1 < len(parts):
                file_path = parts[i+1]
                if os.path.exists(file_path):
                    print(f"Aakash: Playing local file: {file_path}")
                    os.system(f'xdg-open "{file_path}"')
                else:
                    print("Aakash: File not found.")
                break
        else:
            print("Aakash: Please specify a valid file path after 'play file'.")
    else:
        print("Aakash: Please specify if you want to play music, a movie, or a local file.")