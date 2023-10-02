import os
import tkinter as tk
from tkinter import filedialog, messagebox
import pyttsx3
import speech_recognition as sr

# Function to convert voice to text
def convert_voice_to_text(audio_file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        try:
            audio = recognizer.record(source)
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Couldn't understand the audio."
        except sr.RequestError:
            return "Couldn't request results; check your network connection."

# Function to process voice note
def process_voice_note():
    if not os.path.exists("voice_notes"):
        os.makedirs("voice_notes")

    audio_file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav;*.mp3")])

    if not os.path.isfile(audio_file_path):
        messagebox.showerror("Error", "File not found. Please provide a valid file path.")
        return

    text = convert_voice_to_text(audio_file_path)

    text_output.config(state=tk.NORMAL)
    text_output.delete(1.0, tk.END)
    text_output.insert(tk.END, text)
    text_output.config(state=tk.DISABLED)

# Function to speak text
def speak_text():
    text = text_output.get(1.0, tk.END)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Create the main window
root = tk.Tk()
root.title("Voice to Text Converter")
root.geometry("400x300")

# Load a custom font (replace with your font file)
custom_font = ("Helvetica", 14)

# Create GUI elements with improved design
title_label = tk.Label(root, text="Voice to Text Converter", font=("Helvetica", 20), padx=10, pady=10)
process_button = tk.Button(root, text="Process Voice Note", command=process_voice_note, font=custom_font, bg="green", fg="white")
speak_button = tk.Button(root, text="Speak Text", command=speak_text, font=custom_font, bg="blue", fg="white")
text_output = tk.Text(root, wrap=tk.WORD, state=tk.DISABLED, font=custom_font, bg="lightgray", padx=10, pady=10)

# Place GUI elements using grid layout
title_label.grid(row=0, column=0, columnspan=2)
process_button.grid(row=1, column=0, padx=10, pady=10)
speak_button.grid(row=1, column=1, padx=10, pady=10)
text_output.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI main loop
root.mainloop()
