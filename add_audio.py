import numpy as np
from scipy.io import wavfile
from gtts import gTTS
from moviepy import VideoFileClip, AudioFileClip, CompositeAudioClip

# 1. สร้างเสียงพากย์ภาษาไทยแนวลึกลับระทึกขวัญ
text = (
    "ห้องปิดตายหมายเลข 404... เที่ยงคืนตรง ณ อาคารร้าง มีเสียงเคาะปริศนาดังมาจากชั้นบนสุด... "
    "นักสืบเงา ค่อยๆ ย่องเข้าไปพร้อมลำแสงไฟฉายในความมืด... "
    "ประตูถูกล็อกสนิทจากด้านใน แต่กลับมีรอยขีดข่วนสดใหม่ปรากฏอยู่... "
    "ทันใดนั้น... ดวงตาสีแดงปริศนา ก็ลืมขึ้นจากในเงามืด!"
)
tts = gTTS(text=text, lang="th", slow=False)
tts.save("voice.mp3")

# 2. โหลดวิดีโอแนวตั้ง 9:16
video = VideoFileClip("media/videos/scene1/1280p15/WhisperingWoodsScene1.mp4")
duration = video.duration

# 3. สร้างดนตรีประกอบโทนลึกลับ/ระทึกขวัญ (Minor / Diminished)
sample_rate = 44100
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# โน้ตเสียงต่ำชวนขนลุก (C2, Eb2, F#2, G3)
freqs = [65.41, 77.78, 92.50, 196.00]
music = np.zeros_like(t)

for i, f in enumerate(freqs):
    pulse = 0.4 + 0.6 * np.sin(2 * np.pi * (0.35 + i * 0.08) * t)
    music += np.sin(2 * np.pi * f * t) * pulse

fade_len = int(sample_rate * 2.0)
music[:fade_len] *= np.linspace(0, 1, fade_len)
music[-fade_len:] *= np.linspace(1, 0, fade_len)

music = (music / np.max(np.abs(music)) * 0.22 * 32767).astype(np.int16)
wavfile.write("bgm.wav", sample_rate, music)

# 4. รวมภาพ + เสียงพากย์ + ดนตรีระทึกขวัญ
voice_audio = AudioFileClip("voice.mp3")
bgm_audio = AudioFileClip("bgm.wav").subclipped(0, duration)

combined_audio = CompositeAudioClip([bgm_audio, voice_audio])
final_video = video.with_audio(combined_audio)
final_video.write_videofile("final_scene1.mp4", codec="libx264", audio_codec="aac")
