import asyncio
import numpy as np
from scipy.io import wavfile
import edge_tts
from moviepy import VideoFileClip, AudioFileClip, CompositeAudioClip

async def make_voice():
    text = (
        "รหัสลับแห่งป่าเรืองแสง... ฉากที่ 1 คืนที่โค้ดมีชีวิต... "
        "ในคืนอันเงียบสงัดกลางป่าลึก แสงหิ่งห้อยนับสิบดวงลอยส่องสว่างนำทาง "
        "ลูมินา เด็กหญิงผู้ถือตะเกียงแสงจันทร์ กำลังเดินสำรวจไปตามเส้นทางแห่งข้อมูล "
        "แต่ทว่า... เงาประหลาดและรหัสผิดพลาดสีแดง กลับปรากฏขึ้นเบื้องหน้าของเธอ"
    )
    communicate = edge_tts.Communicate(text, "th-TH-PremwadeeNeural", rate="-8%")
    await communicate.save("voice.mp3")

asyncio.run(make_voice())

video = VideoFileClip("media/videos/scene1/480p15/WhisperingWoodsScene1.mp4")
duration = video.duration

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

voice_audio = AudioFileClip("voice.mp3")
bgm_audio = AudioFileClip("bgm.wav").subclipped(0, duration)

combined_audio = CompositeAudioClip([bgm_audio, voice_audio])
final_video = video.with_audio(combined_audio)
final_video.write_videofile("final_scene1.mp4", codec="libx264", audio_codec="aac")
