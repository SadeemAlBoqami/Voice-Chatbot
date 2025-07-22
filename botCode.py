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

# Recording settings
SAMPLE_RATE = 44100
CHANNELS = 1
FILENAME = "user_input.wav"
audio_data = []
stream = None

# Cohere API key (replace if needed)
co = cohere.Client("YOUR_COHERE_API_KEY")

def start_recording():
    """
    Start recording audio from the microphone.
    """
    global audio_data, stream
    audio_data = []
    print("[INFO] Starting recording...")
    status_label.config(text="Recording...")
    record_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)
    stream = sd.InputStream(callback=callback, channels=CHANNELS, samplerate=SAMPLE_RATE)
    stream.start()

def callback(indata, frames, time, status):
    """
    Called for each audio block. Appends incoming audio data to the buffer.
    """
    global audio_data
    audio_data.extend(indata.copy())

def stop_recording():
    """
    Stop the recording, save audio to file, and start processing it.
    """
    global stream
    print("[INFO] Stopping recording...")
    status_label.config(text="Recording stopped. Saving...")
    record_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)

    if stream:
        stream.stop()
        stream.close()

    # Convert audio buffer to numpy array and save as WAV
    audio_np = np.array(audio_data)
    print("[INFO] Saving audio file...")
    write(FILENAME, SAMPLE_RATE, (audio_np * 32767).astype(np.int16))  # PCM 16-bit
    print(f"[INFO] Audio saved as {FILENAME}")
    status_label.config(text="Recording saved.")
    process_audio()

def process_audio():
    """
    Run Whisper ASR on the recorded audio and generate a reply.
    """
    print("[INFO] Starting speech recognition (Whisper)...")
    model = whisper.load_model("base")
    result = model.transcribe(FILENAME, language="ar")
    text = result["text"].strip()
    if text:
        print(f"[INFO] Recognized text: {text}")
        result_label.config(text="You said: " + text)
        threading.Thread(target=generate_reply, args=(text,)).start()
    else:
        print("[ERROR] No speech recognized")
        result_label.config(text="No speech was recognized.")

def generate_reply(text):
    """
    Send the recognized text to Cohere and get a reply.
    """
    print("[INFO] Sending text to Cohere for reply...")
    response = co.chat(message=text, model="command-r-plus")
    reply = response.text.strip()
    print(f"[INFO] Received reply: {reply}")
    result_label.config(text=f"Bot says: {reply}")
    text_to_speech_edge(reply)

def text_to_speech_edge(text, filename="response.mp3"):
    """
    Convert the reply text to speech using edge-tts and play it.
    """
    print("🔊 Converting reply to speech using edge-tts...")

    async def run_tts():
        try:
            communicate = edge_tts.Communicate(text=text, voice="ar-SA-ZariyahNeural")
            await communicate.save(filename)
            print(f"[INFO] Audio file saved: {filename}")

            # Play the audio (works on Windows only)
            try:
                os.startfile(filename)
            except AttributeError:
                print("[WARN] Cannot auto-play audio on this system.")
        except Exception as e:
            print(f"[ERROR] Error during TTS conversion: {e}")

    asyncio.run(run_tts())

# GUI Setup
root = tk.Tk()
root.title("Voice Assistant")

record_button = tk.Button(root, text="🎙️ Start Recording", command=start_recording)
record_button.pack()

stop_button = tk.Button(root, text="⏹️ Stop Recording", command=stop_recording, state=tk.DISABLED)
stop_button.pack()

status_label = tk.Label(root, text="Press Start to begin recording...")
status_label.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
