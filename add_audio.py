import subprocess
import numpy as np
from scipy.io import wavfile
from gtts import gTTS
from moviepy import VideoFileClip, AudioFileClip, CompositeAudioClip

# ฟังก์ชันสร้างเสียงพูดผู้ชายโทนทุ้มต่ำด้วย ffmpeg (ไม่ยานคาง)
def make_deep_male_voice(text, out_wav, pitch_factor=0.78):
    gTTS(text=text, lang="th", slow=False).save("temp_tts.mp3")
    # ปรับ Pitch ลงให้ทุ้มลึก และปรับความเร็วชดเชยให้พูดจังหวะปกติ
    tempo = 1.08 / pitch_factor
    cmd = [
        "ffmpeg", "-y", "-i", "temp_tts.mp3",
        "-af", f"asetrate=24000*{pitch_factor},aresample=44100,atempo={tempo},bass=g=6",
        out_wav
    ]
    subprocess.run(cmd, check=True)

# 1. สร้างเสียงพูดตัวละครที่ 1 (วินาทีที่ 2.5): โทนทุ้มนุ่ม
make_deep_male_voice("เฮ้ย! นายได้ยินเสียงเคาะ จากชั้นบนของตึกนี้ไหม?", "line1.wav", pitch_factor=0.80)

# 2. สร้างเสียงพูดตัวละครที่ 2 (วินาทีที่ 10.5): โทนทุ้มต่ำขรึมกว่า
make_deep_male_voice("แปลกมาก... ห้อง 404 ถูกล็อก แต่มีรอยขีดข่วนสดใหม่!", "line2.wav", pitch_factor=0.73)

# 3. สร้างเสียงร้องตกใจตัวละครที่ 1 (วินาทีที่ 21.2): โทนทุ้มตื่นเต้น
make_deep_male_voice("เฮ้ย! มีบางอย่างกำลัง จ้องออกมาจากข้างใน!", "line3.wav", pitch_factor=0.82)

# โหลดวิดีโอ 30 FPS
video = VideoFileClip("media/videos/scene1/1280p30/WhisperingWoodsScene1.mp4")
duration = video.duration
sr = 44100
total_samples = int(sr * duration)
t = np.linspace(0, duration, total_samples, endpoint=False)

# 4. สร้างเสียงเอฟเฟกต์ (SFX) ตรงตามจังหวะฉาก
sfx = np.zeros(total_samples)

def add_impact(time_sec, freq_start, freq_end, dur_sec, vol):
    start_idx = int(time_sec * sr)
    length = int(dur_sec * sr)
    if start_idx + length >= total_samples:
        return
    local_t = np.linspace(0, dur_sec, length, endpoint=False)
    freqs = np.linspace(freq_start, freq_end, length)
    wave = np.sin(2 * np.pi * freqs * local_t) * np.exp(-local_t * (6.0 / dur_sec))
    sfx[start_idx:start_idx + length] += wave * vol

# เสียงเดิน 3 ก้าว (วินาที 0.3, 1.0, 1.7)
for st in [0.3, 1.0, 1.7]:
    add_impact(st, 90, 40, 0.15, 0.5)

# เสียงเคาะประตูดังมาจากข้างบน (วินาที 6.5, 7.0, 7.5)
for kt in [6.5, 7.0, 7.5]:
    add_impact(kt, 135, 50, 0.25, 0.85)

# เสียงเปลี่ยนฉาก (Whoosh) ตอนวินาที 9.5 และ 20.5
add_impact(9.5, 220, 60, 0.4, 0.5)
add_impact(20.5, 250, 50, 0.45, 0.6)

# เสียงกระแทกตกใจตอนดวงตาสีแดงโผล่ (วินาที 21.0)
add_impact(21.0, 180, 25, 1.8, 0.95)

# ดนตรีพื้นหลังแนวลึกลับ
bgm = np.zeros(total_samples)
for i, f in enumerate([65.41, 77.78, 92.50, 130.81]):
    pulse = 0.4 + 0.6 * np.sin(2 * np.pi * (0.35 + i * 0.08) * t)
    bgm += np.sin(2 * np.pi * f * t) * pulse
bgm = (bgm / np.max(np.abs(bgm))) * 0.15

env_mix = np.clip(bgm + sfx, -1.0, 1.0)
fade_len = int(sr * 1.0)
env_mix[:fade_len] *= np.linspace(0, 1, fade_len)
env_mix[-fade_len:] *= np.linspace(1, 0, fade_len)
wavfile.write("env_audio.wav", sr, (env_mix * 32767).astype(np.int16))

# 5. จัดวางเสียงพูดของแต่ละตัวละครให้ตรงกับบอลลูนคำพูดในแต่ละฉาก
v1 = AudioFileClip("line1.wav").with_start(2.5)
v2 = AudioFileClip("line2.wav").with_start(10.5)
v3 = AudioFileClip("line3.wav").with_start(21.2)
env = AudioFileClip("env_audio.wav").subclipped(0, duration)

final_audio = CompositeAudioClip([env, v1, v2, v3])
final_video = video.with_audio(final_audio)
final_video.write_videofile("final_scene1.mp4", codec="libx264", audio_codec="aac")
    
