from manim import *

config.pixel_width = 720
config.pixel_height = 1280
config.frame_width = 8.0
config.frame_height = 14.22
config.frame_rate = 30

def make_char(role="hair", mouth_open=False, state="normal", flip=False):
    skin = "#ffedd8"
    outline = "#111111"
    lw = 5

    step = 0.2 if state == "walk" else 0.0
    left_leg = VGroup(
        Line([-0.22, -0.4, 0], [-0.22 - step, -1.45, 0], color=outline, stroke_width=14),
        Line([-0.22, -0.4, 0], [-0.22 - step, -1.45, 0], color=skin, stroke_width=7),
        Ellipse(width=0.36, height=0.16, color=skin, fill_opacity=1, stroke_color=outline, stroke_width=lw).move_to([-0.12 - step, -1.48, 0])
    )
    right_leg = VGroup(
        Line([0.22, -0.4, 0], [0.22 + step, -1.45, 0], color=outline, stroke_width=14),
        Line([0.22, -0.4, 0], [0.22 + step, -1.45, 0], color=skin, stroke_width=7),
        Ellipse(width=0.36, height=0.16, color=skin, fill_opacity=1, stroke_color=outline, stroke_width=lw).move_to([0.32 + step, -1.48, 0])
    )

    shorts_col = "#1d3557" if role == "hair" else "#6c757d"
    shirt_col = "#2b2d42" if role == "hair" else "#495057"

    shorts = RoundedRectangle(corner_radius=0.08, width=0.95, height=0.55, color=shorts_col, fill_opacity=1, stroke_color=outline, stroke_width=lw).move_to([0, -0.35, 0])
    torso = RoundedRectangle(corner_radius=0.18, width=0.95, height=1.15, color=shirt_col, fill_opacity=1, stroke_color=outline, stroke_width=lw).move_to([0, 0.35, 0])
    head = Circle(radius=0.56, color=skin, fill_opacity=1, stroke_color=outline, stroke_width=lw).move_to([0, 1.42, 0])

    hair = VGroup()
    if role == "hair":
        hair = VGroup(
            Line([-0.25, 1.92, 0], [-0.42, 2.12, 0], color=outline, stroke_width=6),
            Line([-0.05, 1.97, 0], [-0.12, 2.2, 0], color=outline, stroke_width=6),
            Line([0.15, 1.95, 0], [0.18, 2.15, 0], color=outline, stroke_width=6)
        )

    if state == "shock":
        eyes = VGroup(
            Circle(radius=0.08, color=outline, fill_opacity=1).move_to([0.14, 1.45, 0]),
            Circle(radius=0.08, color=outline, fill_opacity=1).move_to([0.36, 1.45, 0])
        )
        mouth = Ellipse(width=0.2, height=0.28, color="#9e2a2b", fill_opacity=1, stroke_color=outline, stroke_width=3).move_to([0.25, 1.18, 0])
        arm = VGroup(
            Line([0.25, 0.65, 0], [0.65, 1.25, 0], color=outline, stroke_width=14),
            Line([0.25, 0.65, 0], [0.65, 1.25, 0], color=skin, stroke_width=7)
        )
    else:
        eyes = VGroup(
            Ellipse(width=0.08, height=0.14, color=outline, fill_opacity=1).move_to([0.14, 1.46, 0]),
            Ellipse(width=0.08, height=0.14, color=outline, fill_opacity=1).move_to([0.36, 1.46, 0])
        )
        if mouth_open:
            mouth = Ellipse(width=0.22, height=0.18, color="#9e2a2b", fill_opacity=1, stroke_color=outline, stroke_width=3).move_to([0.25, 1.22, 0])
        else:
            mouth = Line([0.15, 1.24, 0], [0.35, 1.24, 0], color=outline, stroke_width=4)

        if state == "point":
            arm = VGroup(
                Line([0.25, 0.65, 0], [0.85, 0.75, 0], color=outline, stroke_width=14),
                Line([0.25, 0.65, 0], [0.85, 0.75, 0], color=skin, stroke_width=7)
            )
        else:
            arm = VGroup(
                Line([0.15, 0.65, 0], [0.45, 0.15, 0], color=outline, stroke_width=14),
                Line([0.15, 0.65, 0], [0.45, 0.15, 0], color=skin, stroke_width=7)
            )

    char = VGroup(left_leg, right_leg, shorts, torso, head, hair, eyes, mouth, arm)
    if flip:
        char.flip(UP)
    return char

def speech_bubble(text_str, speaker="left", border_col="#ffd166"):
    box = RoundedRectangle(corner_radius=0.3, width=6.4, height=1.8, color=WHITE, fill_opacity=0.96, stroke_width=5, stroke_color=border_col)
    txt = Text(text_str, font="Loma", font_size=26, color="#111111", line_spacing=1.3).move_to(box.get_center())
    if speaker == "left":
        tail = Polygon([-1.8, -0.9, 0], [-1.2, -0.9, 0], [-2.1, -1.45, 0], color=WHITE, fill_opacity=1, stroke_color=border_col, stroke_width=4)
    else:
        tail = Polygon([1.2, -0.9, 0], [1.8, -0.9, 0], [2.1, -1.45, 0], color=WHITE, fill_opacity=1, stroke_color=border_col, stroke_width=4)
    return VGroup(tail, box, txt).move_to([0, 2.3, 0])

class WhisperingWoodsScene1(Scene):
    def construct(self):
        # ==========================================
        # ฉากที่ 1 (0 - 9.5 วิ): หน้าตึกร้างยามเย็น ทั้งคู่เดินเข้ามาคุยกัน
        # ==========================================
        bg1 = VGroup(
            Rectangle(width=9, height=15, stroke_width=0).set_color_by_gradient("#1d3557", "#457b9d", "#e07a5f"),
            Circle(radius=0.9, color="#fefae0", fill_opacity=0.9, stroke_width=0).move_to([2.2, 5.2, 0]),
            Rectangle(width=6.0, height=8.5, color="#2b2d42", fill_opacity=1, stroke_color="#111111", stroke_width=4).move_to([1.2, 0.5, 0]),
            Rectangle(width=9, height=4.5, color="#3d405b", fill_opacity=1, stroke_color="#111111", stroke_width=4).move_to([0, -5.2, 0])
        )
        self.add(bg1)

        c1 = make_char("hair", False, "walk").move_to([-3.2, -1.8, 0])
        c2 = make_char("bald", False, "walk", flip=True).move_to([-1.2, -1.8, 0])
        self.add(c1, c2)

        # เดินเข้ามาในฉาก 3 ก้าว
        for i in range(3):
            self.play(
                Transform(c1, make_char("hair", False, "walk" if i%2==0 else "normal").move_to(c1.get_center() + RIGHT*0.45)),
                Transform(c2, make_char("bald", False, "walk" if i%2==1 else "normal", flip=True).move_to(c2.get_center() + RIGHT*0.45)),
                run_time=0.7, rate_func=linear
            )

        # ตัวละครที่ 1 (ผมสั้น) พูดพร้อมขยับปาก
        b1 = speech_bubble("เฮ้ย! นายได้ยินเสียงเคาะ\nจากชั้นบนของตึกนี้ไหม?", "left", "#e63946")
        self.play(FadeIn(b1, scale=0.8), run_time=0.5)
        for m in range(6):
            self.play(Transform(c1, make_char("hair", m%2==0, "point").move_to(c1.get_center())), run_time=0.55)
        self.wait(1.0)

        # ==========================================
        # ฉากที่ 2 (9.5 - 20.5 วิ): เปลี่ยนฉากเข้ามาในโถงทางเดินหน้าห้อง 404
        # ==========================================
        bg2 = VGroup(
            Rectangle(width=9, height=15, color="#14141d", fill_opacity=1, stroke_width=0),
            Polygon([-4.5, 7.5, 0], [-1.5, 3.5, 0], [-1.5, -3.2, 0], [-4.5, -7.5, 0], color="#1f1f2e", fill_opacity=1, stroke_color="#111111", stroke_width=4),
            Rectangle(width=9, height=4.5, color="#252535", fill_opacity=1, stroke_color="#111111", stroke_width=4).move_to([0, -5.2, 0]),
            Rectangle(width=2.3, height=4.4, color="#582f0e", fill_opacity=1, stroke_color="#111111", stroke_width=5).move_to([2.1, -0.8, 0]),
            Text("404", font="Loma", font_size=36, color="#ffd166").move_to([2.1, 0.7, 0]),
            Line([1.5, -0.5, 0], [2.4, -1.1, 0], color="#ff595e", stroke_width=4),
            Line([1.6, -0.9, 0], [2.5, -1.4, 0], color="#ff595e", stroke_width=4)
        )

        self.play(FadeOut(bg1), FadeOut(b1), FadeIn(bg2), run_time=0.8)
        c1.move_to([-2.2, -1.8, 0])
        c2.move_to([-0.3, -1.8, 0])

        # ตัวละครที่ 2 (หัวโล้น) พูดโต้ตอบพร้อมขยับปาก
        b2 = speech_bubble("แปลกมาก... ห้อง 404 ถูกล็อก\nแต่มีรอยขีดข่วนสดใหม่!", "right", "#4cc9f0")
        self.play(FadeIn(b2, scale=0.8), run_time=0.5)
        for m in range(7):
            self.play(Transform(c2, make_char("bald", m%2==0, "normal", flip=False).move_to(c2.get_center())), run_time=0.55)
        self.wait(1.2)

        # ==========================================
        # ฉากที่ 3 (20.5 - 30 วิ): ซูมหน้าประตู ดวงตาสีแดงโผล่ + ทั้งคู่ร้องตกใจ!
        # ==========================================
        bg3 = VGroup(
            Rectangle(width=9, height=15, color="#09090d", fill_opacity=1, stroke_width=0),
            Rectangle(width=5.5, height=9.5, color="#3d220c", fill_opacity=1, stroke_color="#111111", stroke_width=6).move_to([1.5, 0.2, 0]),
            Text("404", font="Loma", font_size=54, color="#ff595e").move_to([1.5, 3.2, 0]),
            Rectangle(width=9, height=4.2, color="#1a1a24", fill_opacity=1, stroke_color="#111111", stroke_width=4).move_to([0, -5.2, 0])
        )
        self.play(FadeOut(bg2), FadeOut(b2), FadeIn(bg3), run_time=0.7)

        c1_shock = make_char("hair", True, "shock").move_to([-2.3, -1.9, 0])
        c2_shock = make_char("bald", True, "shock").move_to([-0.5, -1.9, 0])
        eyes = VGroup(
            Ellipse(width=0.65, height=0.28, color="#ff595e", fill_opacity=1, stroke_color="#111111", stroke_width=4).move_to([1.0, 0.5, 0]),
            Ellipse(width=0.65, height=0.28, color="#ff595e", fill_opacity=1, stroke_color="#111111", stroke_width=4).move_to([2.1, 0.5, 0])
        )
        b3 = speech_bubble("เฮ้ย!! มีบางอย่างกำลัง\nจ้องออกมาจากข้างใน!", "left", "#ff595e")

        self.play(
            Transform(c1, c1_shock),
            Transform(c2, c2_shock),
            FadeIn(eyes, scale=0.3),
            FadeIn(b3, scale=0.8),
            run_time=0.6
        )
        self.play(Flash(eyes, color="#ff595e", line_length=0.7), Wiggle(c1), Wiggle(c2), run_time=1.2)
        self.wait(6.0)
    
