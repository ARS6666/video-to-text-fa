# video-to-text-fa
A fast and practical Python tool for transcribing long video files using OpenAI Whisper.
This project speeds up transcription by increasing audio playback speed before processing,
making it ideal for long videos (1+ hour), especially in Persian (Farsi).

---

## 🚀 Features

- 🎥 Transcribe video files directly (MP4, MKV, etc.)
- ⚡ Speed up audio (e.g. 1.25x – 1.5x) before transcription
- 🧠 High-quality speech-to-text using OpenAI Whisper
- 🇮🇷 Excellent performance for Persian (Farsi)
- 📄 Save transcript to text file
- 🛠 Simple and extensible Python code

---

## 📦 Requirements

- Python 3.8+
- ffmpeg
- OpenAI Whisper

---

## 🔧 Installation

### 1. Install ffmpeg

**Linux**
```bash
sudo apt install ffmpeg
macOS

brew install ffmpeg


Windows
Download from: https://ffmpeg.org/download.html

(Add ffmpeg to PATH)

2. Install Python dependencies
pip install openai-whisper ffmpeg-python
