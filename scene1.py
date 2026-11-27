from manim import *

# ตั้งค่าแนวตั้ง 9:16 (720x1280) 30 FPS มาตรฐานช่อง
config.pixel_width = 720
config.pixel_height = 1280
config.frame_width = 8.0
config.frame_height = 14.22
config.frame_rate = 30

def create_channel_character(role="hair", pose="idle", face="normal", flip=False):
    skin = "#ffedd8"
    outline = "#111111"
    lw = 5

    # ขาและเท้าลายเส้นหนาเอกลักษณ์
    step = 0.22 if pose == "walk" else 0.0
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

    # เสื้อผ้าแยกตามตัวละคร
    if role == "hair":
        shorts_col = "#1d3557"
        shirt_col = "#2b2d42"
    else:
        shorts_col = "#adb5bd"
        shirt_col = "#4a4e69"

    shorts = RoundedRectangle(corner_radius=0.08, width=0.95, height=0.55, color=shorts_col, fill_opacity=1, stroke_color=outline, stroke_width=lw).move_to([0, -0.35, 0])
    torso = RoundedRectangle(corner_radius=0.18, width=0.95, height=1.15, color=shirt_col, fill_opacity=1, stroke_color=outline, stroke_width=lw).move_to([0, 0.35, 0])

    # หัวกลมและใบหน้าเอกลักษณ์ (ไม่มีผ้าคาดหัว)
    head = Circle(radius=0.56, color=skin, fill_opacity=1, stroke_color=outline, stroke_width=lw).move_to([0, 1.42, 0])

    # ทรงผมสั้นเรียบๆ สำหรับตัวละครหลัก (ส่วนอีกคนหัวโล้น)
    headgear = VGroup()
    if role == "hair":
        hair1 = Line([-0.25, 1.92, 0], [-0.42, 2.12, 0], color=outline, stroke_width=6)
        hair2 = Line([-0.05, 1.97, 0], [-0.12, 2.2, 0], color=outline, stroke_width=6)
        hair3 = Line([0.15, 1.95, 0], [0.18, 2.15, 0], color=outline, stroke_width=6)
        headgear = VGroup(hair1, hair2, hair3)

    # ดวงตาและปากแสดงอารมณ์
    if face == "shock":
        eyes = VGroup(
            Circle(radius=0.08, color=outline, fill_opacity=1).move_to([0.14, 1.45, 0]),
            Circle(radius=0.08, color=outline, fill_opacity=1).move_to([0.36, 1.45, 0])
        )
        mouth = Ellipse(width=0.18, height=0.26, color="#9e2a2b", fill_opacity=1, stroke_color=outline, stroke_width=3).move_to([0.25, 1.18, 0])
    elif face == "talk":
        eyes = VGroup(
            Ellipse(width=0.08, height=0.14, color=outline, fill_opacity=1).move_to([0.14, 1.46, 0]),
            Ellipse(width=0.08, height=0.14, color=outline, fill_opacity=1).move_to([0.36, 1.46, 0])
        )
        mouth = Sector(radius=0.16, start_angle=PI, angle=PI, color=WHITE, fill_opacity=1, stroke_color=outline, stroke_width=4).move_to([0.25, 1.25, 0])
    else:
        eyes = VGroup(
            Ellipse(width=0.08, height=0.14, color=outline, fill_opacity=1).move_to([0.14, 1.46, 0]),
            Ellipse(width=0.08, height=0.14, color=outline, fill_opacity=1).move_to([0.36, 1.46, 0])
        )
        mouth = Arc(radius=0.14, start_angle=-2.6, angle=2.0, color=outline, stroke_width=4).move_to([0.25, 1.26, 0])

    # แขนแสดงท่าทาง
    if pose == "point":
        arm = VGroup(
            Line([0.25, 0.65, 0], [0.85, 0.75, 0], color=outline, stroke_width=14),
            Line([0.25, 0.65, 0], [0.85, 0.75, 0], color=skin, stroke_width=7)
        )
    elif face == "shock":
        arm = VGroup(
            Line([0.25, 0.65, 0], [0.65, 1.25, 0], color=outline, stroke_width=14),
            Line([0.25, 0.65, 0], [0.65, 1.25, 0], color=skin, stroke_width=7)
        )
    else:
        arm = VGroup(
            Line([0.15, 0.65, 0], [0.45, 0.15, 0], color=outline, stroke_width=14),
            Line([0.15, 0.65, 0], [0.45, 0.15, 0], color=skin, stroke_width=7)
        )

    char = VGroup(left_leg, right_leg, shorts, torso, head, headgear, eyes, mouth, arm)
    if flip:
        char.flip(UP)
    return char

class WhisperingWoodsScene1(Scene):
    def construct(self):
        # ฉากหลังลงสีไล่เฉดยามพลบค่ำปนลึกลับ
        sky = Rectangle(width=9.0, height=15.0, stroke_width=0).set_color_by_gradient("#14213d", "#2b2d42", "#e07a5f")
        building = Rectangle(width=6.8, height=9.0, color="#1d1e2c", fill_opacity=0.95, stroke_color="#111111", stroke_width=4).move_to([0.8, 1.0, 0])
        ground = Rectangle(width=9.0, height=4.2, color="#2b2d42", fill_opacity=1, stroke_color="#111111", stroke_width=4).move_to([0, -5.2, 0])
        trim = Rectangle(width=9.0, height=0.35, color="#e07a5f", fill_opacity=1, stroke_color="#111111", stroke_width=3).move_to([0, -3.1, 0])

        # ประตูห้อง 404
        door = VGroup(
            Rectangle(width=1.9, height=3.8, color="#582f0e", fill_opacity=1, stroke_color="#111111", stroke_width=5).move_to([2.4, -1.2, 0]),
            Text("404", font="Loma", font_size=32, color="#ffd166").move_to([2.4, 0.1, 0])
        )

        self.add(sky, building, ground, trim, door)

        def show_caption(text_str, text_col=WHITE):
            bg = RoundedRectangle(corner_radius=0.25, width=7.2, height=1.7, color="#111111", fill_opacity=0.9, stroke_width=4, stroke_color="#e63946")
            txt = Text(text_str, font="Loma", font_size=26, color=text_col, line_spacing=1.35).move_to(bg.get_center())
            return VGroup(bg, txt).move_to([0, -5.3, 0])

        # ตัวละครคู่หูเอกลักษณ์ประจำช่อง
        char1 = create_channel_character("hair", "idle", "talk").move_to([-2.1, -1.65, 0])
        char2 = create_channel_character("bald", "idle", "normal", flip=True).move_to([-0.2, -1.65, 0])

        # --- ลำดับเรื่องราว 30 วินาที ---
        cap1 = show_caption("คืนนี้... มีเสียงเคาะปริศนา\nดังมาจากห้องปิดตาย 404", "#ffd166")
        self.play(FadeIn(char1), FadeIn(char2), FadeIn(cap1), run_time=1.5)
        self.play(Wiggle(door, scale_value=1.03), run_time=1.5)
        self.wait(3.5)

        # ตัวละครหลักชี้ไปที่ประตูและพูด
        cap2 = show_caption("นายได้ยินไหม... ห้องนี้ถูกล็อก\nตายมาสิบปีแล้วนะ!")
        char1_point = create_channel_character("hair", "point", "talk").move_to(char1.get_center())
        self.play(ReplacementTransform(cap1, cap2), Transform(char1, char1_point), run_time=1.0)
        self.wait(6.5)

        # คู่หูหันไปมองประตูด้วยความสงสัย
        cap3 = show_caption("แต่ทำไม... ถึงมีรอยขีดข่วน\nสดใหม่อยู่หน้าประตูได้ล่ะ?")
        char2_look = create_channel_character("bald", "idle", "talk", flip=False).move_to(char2.get_center())
        q_mark = Text("?", font="Loma", font_size=50, color="#ffd166").next_to(char2, UP, buff=0.2)
        self.play(ReplacementTransform(cap2, cap3), Transform(char2, char2_look), FadeIn(q_mark), run_time=1.0)
        self.wait(6.5)

        # ดวงตาสีแดงโผล่ในประตู! ทั้งคู่ตกใจ
        cap4 = show_caption("ทันใดนั้น! ดวงตาสีแดงปริศนา\nก็จ้องมองออกมาจากด้านใน!", "#ff595e")
        eyes_404 = VGroup(
            Ellipse(width=0.38, height=0.16, color="#ff595e", fill_opacity=1, stroke_color="#111111", stroke_width=3).move_to([2.15, -1.0, 0]),
            Ellipse(width=0.38, height=0.16, color="#ff595e", fill_opacity=1, stroke_color="#111111", stroke_width=3).move_to([2.65, -1.0, 0])
        )
        c1_shock = create_channel_character("hair", "idle", "shock").move_to(char1.get_center() + LEFT * 0.3)
        c2_shock = create_channel_character("bald", "idle", "shock").move_to(char2.get_center() + LEFT * 0.3)

        self.play(
            FadeOut(q_mark),
            ReplacementTransform(cap3, cap4),
            FadeIn(eyes_404, scale=0.4),
            Transform(char1, c1_shock),
            Transform(char2, c2_shock),
            run_time=0.8
        )
        self.play(Flash(eyes_404, color="#ff595e", line_length=0.5), Wiggle(char1), Wiggle(char2), run_time=1.2)
        self.wait(6.0)
        
