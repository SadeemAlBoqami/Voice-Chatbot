# Voice-Chatbot

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

**1. Download the project to your device, which can be done in two ways:**  
i) Using git  
1- Open cmd on your device.  
2- Type the following command to download the project:`git clone https://github.com/SadeemAlBoqami/Voice-Chatbot.git`  
3- After the download finishes, type:`cd Voice-Chatbot`   
* Make sure Git is installed on your device, or download it from [here](https://git-scm.com/).  

ii) Download as a zip file:  
1- Download the [repository zip file](https://github.com/SadeemAlBoqami/Voice-Chatbot/archive/refs/heads/main.zip).  
2- After downloading the file, unzip it anywhere on your device.  
3- Open the folder and you will find the project files ready.  

**2. Open terminal in the project directory:**  
﻿﻿On Windows, open the folder, type cd in the address bar, and press Enter.  
  
**3. Create a virtual environment:**  
Run the following command to create and activate a virtual environment:  
`python -m venv venv`  
`venv\Scripts\activate`  

**4. Install dependencies:**  
`pip install -r requirements.txt`  
Or manually install: `pip install sounddevice numpy scipy gtts cohere edge-tts openai whisper`  

**5. Create your API key and Add it:**  
1- Log in to your [Cohere Dashboard](https://dashboard.cohere.com/) account and create a new API Key.  
2- Open the botCode.py file "e.g. using VS code".  
3- Find the following line:  
```py co = cohere.Client("YOUR_COHERE_API_KEY")```  
4- Replace “YOUR_COHERE_API_KEY” with your real key from the Cohere website.  
**Note:** Don't share your key with anyone, and if you upload it to GitHub make sure you delete it or regenerate it from the Cohere Dashboard.  

**6. Run the chatbot:**  
Use the following command to start the chatbot:  
`python botCode.py`  
Once turned on, you can start speaking through the interface. Your voice will be recognized and processed using Al, generate a response, and speak it using text-to-speech.  

