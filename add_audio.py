import numpy as np
import scipy.io import wavfile
from gtts import gTTS
from moviepy import VideoFileClip, AudioFileClip, CompositeAudioClip

# 1. สร้างเสียงพากย์ภาษาไทยด้วย Google TTS (เสถียรบน GitHub)
text = (
    "รหัสลับแห่งป่าเรืองแสง... ฉากที่ 1 คืนที่โค้ดมีชีวิต... "
    "ในคืนอันเงียบสงัดกลางป่าลึก แสงหิ่งห้อยนับสิบดวงลอยส่องสว่างนำทาง "
    "ลูมินา เด็กหญิงผู้ถือตะเกียงแสงจันทร์ กำลังเดินสำรวจไปตามเส้นทางแห่งข้อมูล "
    "แต่ทว่า... เงาประหลาดและรหัสผิดพลาดสีแดง กลับปรากฏขึ้นเบื้องหน้าของเธอ"
)
tts = gTTS(text=text, lang="th", slow=False)
tts.save("voice.mp3")

# 2. โหลดวิดีโอแนวตั้ง 9:16 (โฟลเดอร์ 1280p15)
video = VideoFileClip("media/videos/scene1/1280p15/WhisperingWoodsScene1.mp4")
duration = video.duration

# 3. สร้างเสียงดนตรีบรรเลงแนวลึกลับชวนฝันให้ยาวเท่ากับวิดีโอ
sample_rate = 44100
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

freqs = [220.00, 261.63, 329.63, 392.00, 493.88]
music = np.zeros_like(t)

for i, f in enumerate(freqs):
    envelope = 0.5 + 0.5 * np.sin(2 * np.pi * (0.2 + i * 0.04) * t)
    music += np.sin(2 * np.pi * f * t) * envelope

fade_len = int(sample_rate * 2.5)
music[:fade_len] *= np.linspace(0, 1, fade_len)
music[-fade_len:] *= np.linspace(1, 0, fade_len)

music = (music / np.max(np.abs(music)) * 0.16 * 32767).astype(np.int16)
wavfile.write("bgm.wav", sample_rate, music)

# 4. รวมวิดีโอ + เสียงพากย์ + เสียงดนตรี
voice_audio = AudioFileClip("voice.mp3")
bgm_audio = AudioFileClip("bgm.wav").subclipped(0, duration)

combined_audio = CompositeAudioClip([bgm_audio, voice_audio])
final_video = video.with_audio(combined_audio)
final_video.write_videofile("final_scene1.mp4", codec="libx264", audio_codec="aac")
