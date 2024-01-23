import os
import assemblyai as aai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set AssemblyAI API key from environment variable
aai.settings.api_key = os.getenv("AAI_KEY")

# Function to perform LeMUR task or provide summary based on user input
def perform_lemur_task(transcript_id):
    # Get the transcript based on the provided ID
    transcript = aai.Transcript.get_by_id(transcript_id)

    # Prompt user for custom LeMUR task or summary
    custom_task = input("Enter a custom LeMUR task (leave blank for summary): ").strip()

    if custom_task:
        # Perform custom LeMUR task
        result = transcript.lemur.task(custom_task)
        print(result.response)
    else:
        # Perform summary task
        context = input("Enter context for the summary: ").strip()
        answer_format = input("Enter answer format for the summary: ").strip()
        result = transcript.lemur.summarize(context=context, answer_format=answer_format)
        print(result.response)

# Prompt user for transcript ID
transcript_id = input("Enter the transcript ID: ").strip()

# Perform LeMUR task or provide summary based on user input
perform_lemur_task(transcript_id)
