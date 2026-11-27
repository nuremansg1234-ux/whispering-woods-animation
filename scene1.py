from manim import *
import random

# ตั้งค่าสัดส่วนวิดีโอแนวตั้ง 9:16 (HD 720x1280)
config.pixel_width = 720
config.pixel_height = 1280
config.frame_width = 8.0
config.frame_height = 14.22

class WhisperingWoodsScene1(Scene):
    def construct(self):
        self.camera.background_color = "#070d1f"

        # 1. ดวงจันทร์และแสงจันทร์ด้านบนของจอแนวตั้ง
        moon_glow = Circle(radius=1.5, color=BLUE_A, fill_opacity=0.12, stroke_width=0).move_to([1.8, 4.8, 0])
        moon = Circle(radius=0.65, color="#fefae0", fill_opacity=0.9, stroke_width=0).move_to(moon_glow.get_center())
        moon_group = VGroup(moon_glow, moon)

        # 2. เงาต้นไม้ในป่าเรืองแสง (จัดระยะให้พอดีกับจอแนวตั้ง)
        trees = VGroup()
        tree_positions = [-3.2, -1.8, -0.4, 1.2, 2.8]
        for x in tree_positions:
            trunk = Rectangle(width=0.35, height=6.5, color="#0d1b2a", fill_opacity=1, stroke_width=0).move_to([x, -2.5, 0])
            leaves = Triangle(color="#1b263b", fill_opacity=0.95, stroke_width=0).scale(1.5).move_to([x, 0.5, 0])
            trees.add(VGroup(trunk, leaves))

        # พื้นดินป่าด้านล่าง
        ground = Rectangle(width=10, height=3.5, color="#050914", fill_opacity=1, stroke_width=0).move_to(DOWN * 5.5)

        # 3. ฝูงหิ่งห้อยเรืองแสงกระจายเต็มจอแนวตั้ง
        fireflies = VGroup(*[
            Dot(
                point=[random.uniform(-3.6, 3.6), random.uniform(-4.0, 5.5), 0],
                radius=random.uniform(0.04, 0.08),
                color=YELLOW
            ).set_opacity(random.uniform(0.5, 0.9))
            for _ in range(35)
        ])

        # 4. ชื่อเรื่องและชื่อตอน (ปรับขนาดตัวอักษรให้พอดีจอแนวตั้ง)
        title = Text("Code of the\nWhispering Woods", font_size=38, color=BLUE_B, line_spacing=1.2)
        subtitle = Text("ฉากที่ 1: คืนที่โค้ดมีชีวิต", font_size=26, color=YELLOW_B).next_to(title, DOWN, buff=0.4)
        title_box = VGroup(title, subtitle).move_to(UP * 2.2)

        # 5. ตัวละครลูมินา (ชุดคลุมสีคราม + ตะเกียงแสงจันทร์)
        cloak = Triangle(color="#3a86ff", fill_opacity=0.95, stroke_width=0).scale(0.55)
        head = Circle(radius=0.22, color="#ffcdb2", fill_opacity=1, stroke_width=0).next_to(cloak, UP, buff=-0.05)
        lantern_glow = Circle(radius=0.75, color=GOLD, fill_opacity=0.25, stroke_width=0).next_to(cloak, RIGHT, buff=0.1)
        lantern_core = Dot(radius=0.12, color=WHITE).move_to(lantern_glow.get_center())
        lumina = VGroup(cloak, head, lantern_glow, lantern_core).move_to([-2.5, -3.5, 0])

        # 6. สัญลักษณ์โค้ดเตือนภัยสีแดง
        error_glow = Circle(radius=1.1, color=RED, fill_opacity=0.25, stroke_width=0).move_to([1.8, -1.2, 0])
        error_text = Text("<ERROR:\nLOOP_OPEN>", font_size=22, color=RED_B).move_to(error_glow.get_center())
        error_signal = VGroup(error_glow, error_text)

        # --- ลำดับแอนิเมชันรวมประมาณ 30 วินาที ---
        self.play(FadeIn(moon_group), FadeIn(trees), FadeIn(ground), run_time=2.5)
        self.play(FadeIn(fireflies, lag_ratio=0.05), run_time=2.0)
        self.play(Write(title), FadeIn(subtitle, shift=UP * 0.2), run_time=2.5)
        self.wait(1.5)

        self.play(FadeOut(title_box), FadeIn(lumina, shift=RIGHT * 0.5), run_time=2.0)
        self.play(
            lumina.animate.shift(RIGHT * 2.0),
            fireflies.animate.shift(UP * 0.5 + LEFT * 0.3),
            run_time=4.5,
            rate_func=linear
        )
        self.wait(1.0)

        self.play(
            lumina.animate.shift(RIGHT * 1.5),
            lantern_glow.animate.scale(1.3),
            fireflies.animate.shift(DOWN * 0.4 + RIGHT * 0.3),
            run_time=4.5,
            rate_func=linear
        )
        self.wait(1.0)

        self.play(FadeIn(error_signal), lantern_glow.animate.set_color(RED_A), run_time=2.0)
        self.play(
            error_glow.animate.scale(1.4),
            lumina.animate.shift(LEFT * 0.4),
            run_time=2.5
        )
        self.wait(2.0)
        
