import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
from voice_recognition import listen, speak, listen_and_respond
from nlp_engine import NLPEngine
import os

class JebatApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Jebat AI Assistant")
        self.root.geometry("600x700")
        self.root.configure(bg="#282C34")

        # Load Icons
        self.mic_icon = self.load_icon("mic.png", (30, 30))
        self.upload_icon = self.load_icon("upload.png", (30, 30))
        self.send_icon = self.load_icon("send.png", (30, 30))

        # Chat Box
        self.chat_frame = tk.Frame(self.root, bg="#1E1E1E")
        self.chat_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.chat_history = tk.Text(self.chat_frame, bg="#3C3F41", fg="white", wrap="word", state="disabled", font=("Arial", 12))
        self.chat_history.pack(padx=10, pady=10, fill="both", expand=True)

        # Input & Buttons
        self.input_frame = tk.Frame(self.root, bg="#282C34")
        self.input_frame.pack(fill="x", padx=10, pady=5)

        self.user_input = ttk.Entry(self.input_frame, font=("Arial", 14))
        self.user_input.pack(side="left", fill="x", expand=True, padx=5, pady=5)

        self.send_button = tk.Button(self.input_frame, image=self.send_icon, command=self.process_text_input, bg="#3C3F41", bd=0)
        self.send_button.pack(side="right", padx=5)

        self.mic_button = tk.Button(self.input_frame, image=self.mic_icon, command=self.talk_to_jebat, bg="#3C3F41", bd=0)
        self.mic_button.pack(side="right", padx=5)

        self.upload_button = tk.Button(self.input_frame, image=self.upload_icon, command=self.upload_file, bg="#3C3F41", bd=0)
        self.upload_button.pack(side="right", padx=5)

        # Load NLP Engine
        self.nlp_engine = NLPEngine()

    def load_icon(self, icon_path, size):
        """Loads and resizes an icon."""
        if os.path.exists(icon_path):
            icon = Image.open(icon_path)
            icon = icon.resize(size, Image.Resampling.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
            return ImageTk.PhotoImage(icon)
        else:
            return None

    def update_chat(self, role, message):
        """Updates the chat history."""
        self.chat_history.config(state="normal")
        self.chat_history.insert("end", f"{role}: {message}\n\n")
        self.chat_history.config(state="disabled")
        self.chat_history.yview("end")

    def process_text_input(self):
        """Handles manual chat input."""
        user_text = self.user_input.get().strip()
        if user_text:
            self.update_chat("You", user_text)
            response = self.nlp_engine.generate_response(user_text)
            self.update_chat("Jebat", response)
            speak(response)  # ✅ Jebat will now speak the response
            self.user_input.delete(0, tk.END)

    def talk_to_jebat(self):
        """Handles voice input and updates chat."""
        self.update_chat("You", "🎤 Listening...")
        text = listen()
        if text:
            self.update_chat("You", text)
            response = self.nlp_engine.generate_response(text)
            self.update_chat("Jebat", response)
            speak(response)  # ✅ Jebat will now speak the response

    def upload_file(self):
        """Handles file uploads."""
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("Video Files", "*.mp4")])
        if file_path:
            self.update_chat("You", f"📁 Uploaded file: {os.path.basename(file_path)}")
            response = "File processed successfully!"  # Replace with actual processing logic
            self.update_chat("Jebat", response)
            speak(response)  # ✅ Jebat will now speak the upload response

    def run(self):
        """Starts the GUI."""
        self.root.mainloop()

# Run App
if __name__ == "__main__":
    app = JebatApp()
    app.run()
