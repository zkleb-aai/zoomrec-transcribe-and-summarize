import os
import subprocess
import assemblyai as aai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set AssemblyAI API key from environment variable
aai.settings.api_key = os.getenv("AAI_KEY")

def convert_to_mp3(mkv_path):
    # Create the "mp3s" folder if it doesn't exist
    mp3_folder = "mp3s"
    os.makedirs(mp3_folder, exist_ok=True)

    # Extract the filename and extension from the provided path
    file_name, file_extension = os.path.splitext(os.path.basename(mkv_path))

    # Build the output MP3 file path
    mp3_path = os.path.join(mp3_folder, f"{file_name}.mp3")

    # Run ffmpeg command to convert MKV to MP3
    command = ["ffmpeg", "-i", mkv_path, "-q:a", "0", "-map", "a", mp3_path]
    subprocess.run(command)

    return mp3_path

def transcribe_audio(audio_url):
    # Create a transcriber instance
    transcriber = aai.Transcriber()

    # Transcribe the audio
    transcript = transcriber.transcribe(audio_url)

    return transcript

def main():
    # Prompt user for the path to the MKV file
    mkv_path = input("Enter the path to the MKV file: ").strip()

    # Check if the file exists
    if not os.path.exists(mkv_path):
        print("Error: The specified file does not exist.")
        return

    
    # Perform the conversion to MP3
    mp3_path = convert_to_mp3(mkv_path)
    print(f"\nConversion and transcription complete.\n")
    print(f"MP3 file stored at: {mp3_path}")
    # Transcribe the audio using AssemblyAI
    audio_url = f"./{(mp3_path)}"
    transcript = transcribe_audio(audio_url)

    # Print a message indicating the conversion and transcription are complete
    
    print(f"Transcription:\n{transcript.text}")
    print(f"\nTranscript ID:{transcript.id}")

if __name__ == "__main__":
    main()
