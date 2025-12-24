import subprocess
import whisper
import tempfile
import os

VIDEO_URL = "https://aimedic.arvanvod.ir/w6LGOQvYxm/xWAmnvm8yw/h_1080_1200k.mp4"
FAST_AUDIO = "audio_1_5x.wav"
TRANSCRIPT_FILE = "transcript.txt"
SPEED = 1.5

subprocess.run([
    "ffmpeg",
    "-i", VIDEO_URL,
    "-vn",
    "-ac", "1",
    "-ar", "16000",
    "-filter:a", f"atempo={SPEED}",
    FAST_AUDIO,
    "-y"
], check=True)

print("✅ Audio saved:", FAST_AUDIO)

model = whisper.load_model("medium")
result = model.transcribe(FAST_AUDIO, language="fa")

print("=== TRANSCRIPT ===")
print(result["text"])

with open(TRANSCRIPT_FILE, "w", encoding="utf-8") as f:
    f.write(result["text"])

print(f"✅ Transcript saved to {TRANSCRIPT_FILE}")
