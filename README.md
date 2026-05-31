# Sanchaar

Sanchaar is a speech-to-speech AI platform built on Sarvam APIs.

It accepts spoken audio, transcribes it into text, generates an AI response, converts the response back into speech, and returns both the generated text and audio output.

The project is designed with a modular architecture where Speech-to-Text (STT), Large Language Model (LLM), and Text-to-Speech (TTS) capabilities are isolated behind service layers. This allows future migration from cloud-hosted models to self-hosted deployments without changing the application architecture.

---

## Features

* Speech-to-Text using Sarvam STT
* Conversational AI using Sarvam Chat
* Text-to-Speech using Sarvam TTS
* Hindi voice interaction support
* FastAPI-based REST API
* Modular service architecture
* End-to-end speech-to-speech pipeline
* Designed for future offline and air-gapped deployments

---

## Architecture

```text
Voice Input
     │
     ▼
Speech To Text
(Sarvam STT)
     │
     ▼
Transcript
     │
     ▼
Chat Agent
(Sarvam Chat)
     │
     ▼
Response Text
     │
     ▼
Text To Speech
(Sarvam TTS)
     │
     ▼
Voice Response
```

---

## Project Structure

```text
Sanchaar/
│
├── app/
│   ├── agents/
│   │   └── chat_agent.py
│   │
│   ├── audio/
│   │
│   ├── llms/
│   │   └── sarvam_client.py
│   │
│   ├── routes/
│   │   ├── voice.py
│   │   └── webhook.py
│   │
│   ├── services/
│   │   ├── message_processor.py
│   │   └── voice_processor.py
│   │
│   ├── utils/
│   │   └── text_cleaner.py
│   │
│   └── main.py
│
├── requirements.txt
├── .env
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/achalofficial/Sanchaar.git
cd Sanchaar
```

Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file:

```env
SARVAM_API_KEY=your_api_key_here
```

---

## Running The Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

---

## API Endpoints

### Health Check

```http
GET /health
```

Response:

```json
{
  "healthy": true
}
```

---

### Voice Processing

```http
POST /voice
```

Form Data:

```text
audio=<audio_file>
```

Example:

```bash
curl -X POST \
  -F "audio=@sample.mp3" \
  http://127.0.0.1:8000/voice
```

Response:

```json
{
  "transcript": "नमस्ते, मेरा नाम अचल है।",
  "response": "नमस्ते अचल जी! मैं आपकी सहायता के लिए तैयार हूँ।",
  "audio_file": "app/audio/response.wav"
}
```

---

## Current Pipeline

```text
Audio File
     │
     ▼
Sarvam STT
     │
     ▼
Transcript
     │
     ▼
Sarvam Chat
     │
     ▼
Generated Response
     │
     ▼
Sarvam TTS
     │
     ▼
WAV Output
```

---

## Technology Stack

* Python 3.12
* FastAPI
* Uvicorn
* Sarvam SDK
* Sarvam Speech-to-Text
* Sarvam Chat
* Sarvam Text-to-Speech

---

## Roadmap

### V1

* [x] Speech-to-Text
* [x] Chat Integration
* [x] Text-to-Speech
* [x] Voice Processing API
* [x] End-to-End Speech Pipeline

### V1.1

* [ ] UUID-based audio generation
* [ ] Audio serving endpoint
* [ ] Structured logging
* [ ] Configuration management

### V1.2

* [ ] WhatsApp integration
* [ ] Voice note processing
* [ ] Voice replies

### V2

* [ ] Multi-provider architecture
* [ ] Local model support
* [ ] Self-hosted deployments

### V3

* [ ] Air-gapped deployments
* [ ] Offline speech-to-speech stack

---

## Vision

Sanchaar is being developed as a modular speech platform that can operate across cloud-hosted and self-hosted AI stacks.

The long-term goal is to provide a unified architecture where speech recognition, reasoning, and speech synthesis can be swapped between providers while keeping the application layer unchanged.

This enables future deployment scenarios ranging from cloud-native applications to fully offline and air-gapped environments.
