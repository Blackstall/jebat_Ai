import os
from knowledge_base import store_knowledge
from config import UPLOAD_FOLDER

def process_file(file_path):
    """Processes the uploaded file."""
    if file_path.endswith('.txt'):
        return learn_from_text(file_path)
    elif file_path.endswith('.mp4'):
        return learn_from_video(file_path)
    else:
        return "Unsupported file type."

def learn_from_text(file_path):
    """Extracts knowledge from a text file."""
    with open(file_path, 'r') as file:
        content = file.read()
        store_knowledge("text_file", content)
        return f"Learned from text file: {file_path}"

def learn_from_video(file_path):
    """Extracts audio from a video and processes it."""
    from moviepy.editor import VideoFileClip
    video = VideoFileClip(file_path)
    audio = video.audio
    audio.write_audiofile("temp_audio.wav")
    # Process the audio file (e.g., transcribe it)
    return f"Processed video file: {file_path}"