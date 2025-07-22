import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import tkinter as tk
import whisper
import threading
import cohere
import asyncio
import edge_tts
import os

# Audio recording settings
SAMPLE_RATE = 44100  # Sample rate in Hz
CHANNELS = 1         # Mono audio
FILENAME = "user_input.wav"  # Output WAV file name
audio_data = []      # Buffer to store recorded audio
stream = None        # Global variable to hold the recording stream

# Cohere API client
co = cohere.Client("YOUR_COHERE_API_KEY")  # Replace this key with your key

def start_recording():
    """
    Start capturing audio from microphone and store it in audio_data buffer.
    """
    global audio_data, stream
    audio_data = []
    print("[INFO] Starting recording...")
    status_label.config(text="Recording...")
    record_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)

    # Open the audio input stream
    stream = sd.InputStream(callback=callback, channels=CHANNELS, samplerate=SAMPLE_RATE)
    stream.start()

def callback(indata, frames, time, status):
    """
    This callback is triggered automatically by sounddevice to collect incoming audio data.
    """
    global audio_data
    audio_data.extend(indata.copy())  # Append current buffer to global audio data

def stop_recording():
    """
    Stop recording, save audio to a WAV file, and trigger processing.
    """
    global stream
    print("[INFO] Stopping recording...")
    status_label.config(text="Recording stopped. Saving...")
    record_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)

    if stream:
        stream.stop()
        stream.close()

    # Convert list to NumPy array
    audio_np = np.array(audio_data)

    # Save audio to 16-bit PCM WAV file
    print("[INFO] Saving audio file...")
    write(FILENAME, SAMPLE_RATE, (audio_np * 32767).astype(np.int16))
    print(f"[INFO] Audio saved as {FILENAME}")
    status_label.config(text="Recording saved.")

    # Process the saved audio file (speech recognition)
    process_audio()

def process_audio():
    """
    Run Whisper speech recognition on the saved audio file and display the result.
    """
    print("[INFO] Starting speech recognition (Whisper)...")
    model = whisper.load_model("base")
    result = model.transcribe(FILENAME, language="ar")
    text = result["text"].strip()

    if text:
        print(f"[INFO] Recognized text: {text}")
        result_label.config(text="You said: " + text)

        # Call Cohere in a separate thread to avoid freezing the GUI
        threading.Thread(target=generate_reply, args=(text,)).start()
    else:
        print("[ERROR] No speech recognized")
        result_label.config(text="No speech recognized")

def generate_reply(text):
    """
    Send transcribed text to Cohere's chatbot and get a reply.
    """
    print("[INFO] Sending text to Cohere for reply...")
    response = co.chat(message=text, model="command-r-plus")
    reply = response.text.strip()

    print(f"[INFO] Received reply: {reply}")
    result_label.config(text=f"Bot says: {reply}")

    # Convert the reply to speech and play it
    text_to_speech_edge(reply)

def text_to_speech_edge(text, filename="response.mp3"):
    """
    Convert the reply text to speech using Edge TTS and save it as an MP3 file.
    """
    print("🔊 Converting reply to speech using edge-tts...")

    async def run_tts():
        try:
            communicate = edge_tts.Communicate(text=text, voice="ar-SA-ZariyahNeural")
            await communicate.save(filename)
            print(f"[INFO] Audio file saved: {filename}")

            # Attempt to play the audio file (Windows only)
            try:
                os.startfile(filename)
            except AttributeError:
                print("[WARN] Unable to auto-play the file on this OS.")
        except Exception as e:
            print(f"[ERROR] Error during text-to-speech conversion: {e}")

    asyncio.run(run_tts())


# ------------------- GUI SETUP -------------------

# Create main window
root = tk.Tk()
root.title("Voice Assistant")

# Start Recording Button
record_button = tk.Button(root, text="🎙️ Start Recording", command=start_recording)
record_button.pack()

# Stop Recording Button
stop_button = tk.Button(root, text="⏹️ Stop Recording", command=stop_recording, state=tk.DISABLED)
stop_button.pack()

# Status Label (e.g., recording, saved, error messages)
status_label = tk.Label(root, text="Click Start to begin recording...")
status_label.pack()

# Result Label (recognized text and bot reply)
result_label = tk.Label(root, text="")
result_label.pack()

# Run the GUI loop
root.mainloop()
