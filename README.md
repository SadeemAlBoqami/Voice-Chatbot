# Arabic-Voice-Chatbot-with-GUI-using-Cohere-Edge-TTS

## Description:
A voice-activated Arabic chatbot built with Python. It allows users to record their voice, transcribes it using OpenAI’s Whisper, generates smart replies using Cohere's LLM "large language model", and plays the reply back using Microsoft Edge TTS voices — all within a simple Tkinter GUI.

## Features:
-  Understands user input using speech recognition.
-  Generates smart replies using Cohere's AI language model.
-  Converts replies to natural-sounding Arabic speech using Edge-TTS.
-  Interactive graphical interface using Tkinter.

## Technologies Used:
- **Python** - the core language for building the entire project.
- **Tkinter** - To create a simple graphical user interface that the user interacts with.
- **SoundDevice + NumPy** - to record the user's voice from the microphone.
- **Whisper (OpenAI)** - to convert voice to text (Speech-to-Text).
- **Cohere API** - To analyze and respond to text using an artificial intelligence model.
- **Edge-TTS** - to convert the AI response into natural sound (Text-to-Speech).
- **subprocess/tempfile/os** - To play and manage audio files within the system.
- **Threading + asyncio** - To run different processes concurrently without hanging the interface.

## Installation:
To run this project on your local device, follow these steps:
**1- Download the project to your device, which can be done in two ways:**
 i) Using git 
1- Open cmd on your device
2- Type the following command to download the project:`git clone https://github.com/SadeemAlBoqami/Voice-Chatbot.git`
3- After the download finishes, type:`cd Voice-Chatbot` 
* Make sure Git is installed on your device, or download it from [here](https://git-scm.com/).

ii) Download as a zip file:
1- Download the [repository zip file](https://github.com/SadeemAlBoqami/Arabic-Voice-Chatbot-with-GUI-using-Cohere-Edge-TTS/archive/refs/heads/main.zip).
2- After downloading the file, unzip it anywhere on your device.
3- Open the folder and you will find the project files ready.
**2- **

