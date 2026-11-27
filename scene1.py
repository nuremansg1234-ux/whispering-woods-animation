from manim import *
import random

# ตั้งค่าสัดส่วนแนวตั้ง 9:16 (720x1280) สำหรับ TikTok / Reels / Shorts
config.pixel_width = 720
config.pixel_height = 1280
config.frame_width = 8.0
config.frame_height = 14.22

def make_detective_stickman(state="walk", color=WHITE):
    # หัวและหมวกนักสืบ
    head = Circle(radius=0.32, color=color, stroke_width=5, fill_color="#050508", fill_opacity=1).move_to([0, 1.0, 0])
    hat_brim = Line([-0.55, 1.25, 0], [0.55, 1.25, 0], color=GRAY_B, stroke_width=5)
    hat_top = Polygon([-0.32, 1.25, 0], [0.32, 1.25, 0], [0.22, 1.55, 0], [-0.22, 1.55, 0], color=GRAY_B, fill_opacity=1, stroke_width=3)
    
    # แววตาแสดงอารมณ์
    if state == "shock":
        eyes = VGroup(
            Circle(radius=0.07, color=RED_B, fill_opacity=1).move_to([-0.11, 1.02, 0]),
            Circle(radius=0.07, color=RED_B, fill_opacity=1).move_to([0.11, 1.02, 0])
        )
    else:
        eyes = VGroup(
            Dot(point=[-0.11, 1.02, 0], radius=0.04, color=color),
            Dot(point=[0.11, 1.02, 0], radius=0.04, color=color)
        )

    body = Line([0, 0.68, 0], [0, -0.25, 0], color=color, stroke_width=5)

    # ท่าทางแขนและไฟฉาย
    if state == "shock":
        left_arm = Line([0, 0.5, 0], [-0.48, 0.95, 0], color=color, stroke_width=5)
        right_arm = Line([0, 0.5, 0], [0.48, 0.95, 0], color=color, stroke_width=5)
        flashlight = VGroup()
    else:
        left_arm = Line([0, 0.5, 0], [-0.35, 0.0, 0], color=color, stroke_width=5)
        right_arm = Line([0, 0.5, 0], [0.55, 0.45, 0], color=color, stroke_width=5)
        # ไฟฉายและลำแสงสีเหลืองสลัว
        torch = Rectangle(width=0.25, height=0.1, color=GRAY_A, fill_opacity=1).move_to([0.65, 0.45, 0])
        beam = Polygon([0.78, 0.5, 0], [3.8, 1.6, 0], [3.8, -0.7, 0], [0.78, 0.4, 0], color=YELLOW, fill_opacity=0.18, stroke_width=0)
        flashlight = VGroup(torch, beam)

    left_leg = Line([0, -0.25, 0], [-0.32, -1.1, 0], color=color, stroke_width=5)
    right_leg = Line([0, -0.25, 0], [0.32, -1.1, 0], color=color, stroke_width=5)

    return VGroup(head, hat_brim, hat_top, eyes, body, left_arm, right_arm, left_leg, right_leg, flashlight)

class WhisperingWoodsScene1(Scene):
    def construct(self):
        # พื้นหลังสีดำสนิทแนวลึกลับ
        self.camera.background_color = "#050508"

        # 1. ประตูปริศนาหมายเลข 404 ฝั่งขวา
        door_frame = Rectangle(width=2.0, height=3.8, color=GRAY_D, stroke_width=4, fill_color="#0e0e14", fill_opacity=1).move_to([2.1, -1.6, 0])
        door_knob = Dot(point=[1.35, -1.7, 0], radius=0.08, color=GOLD)
        door_num = Text("404", font_size=34, color=RED_C).move_to([2.1, -0.3, 0])
        door = VGroup(door_frame, door_knob, door_num)

        # พื้นห้องและฝุ่นลอยในความมืด
        floor = Line([-4, -3.5, 0], [4, -3.5, 0], color=GRAY_D, stroke_width=4)
        dust = VGroup(*[
            Dot(point=[random.uniform(-3.6, 3.6), random.uniform(-3.2, 5.5), 0], radius=0.03, color=GRAY_B).set_opacity(0.4)
            for _ in range(30)
        ])

        # ฟังก์ชันสร้างกล่องซับไตเติลสไตล์ TikTok / Shorts
        def show_caption(text_str, border_col=GRAY_B, text_col=WHITE):
            bg = RoundedRectangle(corner_radius=0.2, width=7.0, height=1.7, color=BLACK, fill_opacity=0.8, stroke_width=2, stroke_color=border_col)
            txt = Text(text_str, font_size=26, color=text_col, line_spacing=1.3).move_to(bg.get_center())
            return VGroup(bg, txt).move_to([0, -5.2, 0])

        detective = make_detective_stickman("walk", WHITE).move_to([-2.4, -2.4, 0])

        # --- ลำดับเหตุการณ์รวมประมาณ 30 วินาที ---
        # ช่วงที่ 1 (0 - 6.5 วิ): เปิดชื่อเรื่องแนวลึกลับ
        title = Text("ห้องปิดตายหมายเลข 404", font_size=36, color=RED_B)
        sub = Text("คดีปริศนาที่ไม่มีใครกล้าเปิด", font_size=24, color=GRAY_B).next_to(title, DOWN, buff=0.3)
        title_group = VGroup(title, sub).move_to([0, 2.5, 0])

        cap1 = show_caption("เที่ยงคืนตรง ณ อาคารร้าง...\nมีเสียงเคาะดังมาจากห้อง 404")
        self.play(FadeIn(floor), FadeIn(door), FadeIn(dust), Write(title_group), FadeIn(cap1), run_time=2.5)
        self.wait(4.0)

        # ช่วงที่ 2 (6.5 - 15 วิ): นักสืบ Stickman ส่องไฟฉายเดินเข้ามา
        cap2 = show_caption("นักสืบเงา ค่อยๆ ย่องเข้าไป\nพร้อมลำแสงไฟฉายในความมืด")
        self.play(FadeOut(title_group), ReplacementTransform(cap1, cap2), FadeIn(detective), run_time=1.5)
        self.play(
            detective.animate.shift(RIGHT * 2.1),
            dust.animate.shift(UP * 0.3 + LEFT * 0.2),
            run_time=6.5,
            rate_func=linear
        )

        # ช่วงที่ 3 (15 - 22 วิ): ตรวจสอบหน้าประตูและเจอเงาบางอย่าง
        cap3 = show_caption("ประตูถูกล็อกสนิทจากด้านใน...\nแต่กลับมีรอยขีดข่วนสดใหม่!")
        question_mark = Text("?", font_size=48, color=YELLOW).next_to(detective, UP, buff=0.2)
        self.play(ReplacementTransform(cap2, cap3), FadeIn(question_mark, shift=UP * 0.2), run_time=1.5)
        self.wait(5.5)

        # ช่วงที่ 4 (22 - 30 วิ): ดวงตาสีแดงโผล่ในความมืด! นักสืบตกใจ
        cap4 = show_caption("ทันใดนั้น... ดวงตาปริศนา\nก็ลืมขึ้นจากในเงามืด!", RED_B, RED_A)
        monster_eyes = VGroup(
            Ellipse(width=0.35, height=0.16, color=RED, fill_opacity=1).move_to([1.85, -1.4, 0]),
            Ellipse(width=0.35, height=0.16, color=RED, fill_opacity=1).move_to([2.35, -1.4, 0])
        )
        shocked_detective = make_detective_stickman("shock", RED_A).move_to(detective.get_center() + LEFT * 0.6)

        self.play(
            FadeOut(question_mark),
            ReplacementTransform(cap3, cap4),
            FadeIn(monster_eyes, scale=0.5),
            Transform(detective, shocked_detective),
            run_time=1.5
        )
        self.play(Flash(monster_eyes, color=RED, line_length=0.4), run_time=1.5)
        self.wait(5.0)
        
