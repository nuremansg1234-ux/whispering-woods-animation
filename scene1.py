from manim import *
import random

class WhisperingWoodsScene1(Scene):
    def construct(self):
        self.camera.background_color = "#070d1f"

        # 1. ดวงจันทร์และแสงจันทร์บนท้องฟ้า
        moon_glow = Circle(radius=1.5, color=BLUE_A, fill_opacity=0.12, stroke_width=0).move_to(UL * 2.5 + RIGHT * 1.5)
        moon = Circle(radius=0.65, color="#fefae0", fill_opacity=0.9, stroke_width=0).move_to(moon_glow.get_center())
        moon_group = VGroup(moon_glow, moon)

        # 2. เงาต้นไม้ในป่าเรืองแสง (ฉากหลัง)
        trees = VGroup()
        tree_positions = [-5.5, -3.8, -1.8, 1.5, 3.6, 5.4]
        for x in tree_positions:
            trunk = Rectangle(width=0.35, height=4.5, color="#0d1b2a", fill_opacity=1, stroke_width=0).move_to([x, -1.5, 0])
            leaves = Triangle(color="#1b263b", fill_opacity=0.95, stroke_width=0).scale(1.6).move_to([x, 0.8, 0])
            trees.add(VGroup(trunk, leaves))

        # พื้นดินป่า
        ground = Rectangle(width=15, height=2.2, color="#050914", fill_opacity=1, stroke_width=0).move_to(DOWN * 3.2)

        # 3. ฝูงหิ่งห้อยเรืองแสง 35 ดวง
        fireflies = VGroup(*[
            Dot(
                point=[random.uniform(-6.5, 6.5), random.uniform(-2.2, 3.2), 0],
                radius=random.uniform(0.04, 0.08),
                color=YELLOW
            ).set_opacity(random.uniform(0.5, 0.9))
            for _ in range(35)
        ])

        # 4. ชื่อเรื่องและชื่อตอน
        title = Text("Code of the Whispering Woods", font_size=36, color=BLUE_B)
        subtitle = Text("ฉากที่ 1: คืนที่โค้ดมีชีวิต", font_size=26, color=YELLOW_B).next_to(title, DOWN)
        title_box = VGroup(title, subtitle).move_to(UP * 0.5)

        # 5. ตัวละครลูมินา (ชุดคลุมสีคราม + ตะเกียงแสงจันทร์)
        cloak = Triangle(color="#3a86ff", fill_opacity=0.95, stroke_width=0).scale(0.55)
        head = Circle(radius=0.22, color="#ffcdb2", fill_opacity=1, stroke_width=0).next_to(cloak, UP, buff=-0.05)
        lantern_glow = Circle(radius=0.75, color=GOLD, fill_opacity=0.25, stroke_width=0).next_to(cloak, RIGHT, buff=0.1)
        lantern_core = Dot(radius=0.12, color=WHITE).move_to(lantern_glow.get_center())
        lumina = VGroup(cloak, head, lantern_glow, lantern_core).move_to([-4.5, -2.0, 0])

        # 6. สัญลักษณ์โค้ดเตือนภัยสีแดง (ช่วงท้ายฉาก)
        error_glow = Circle(radius=1.0, color=RED, fill_opacity=0.25, stroke_width=0).move_to([4.5, -0.5, 0])
        error_text = Text("<ERROR: LOOP_OPEN>", font_size=22, color=RED_B).move_to(error_glow.get_center())
        error_signal = VGroup(error_glow, error_text)

        # --- ลำดับแอนิเมชันรวมประมาณ 30 วินาที ---
        # ช่วงที่ 1 (0-7 วิ): เปิดฉากท้องฟ้า ต้นไม้ หิ่งห้อย และชื่อเรื่อง
        self.play(FadeIn(moon_group), FadeIn(trees), FadeIn(ground), run_time=2.5)
        self.play(FadeIn(fireflies, lag_ratio=0.05), run_time=2.0)
        self.play(Write(title), FadeIn(subtitle, shift=UP * 0.2), run_time=2.5)
        self.wait(1.5)

        # ช่วงที่ 2 (8.5-16 วิ): ลูมินาปรากฏตัวพร้อมตะเกียงและเดินสำรวจป่า
        self.play(FadeOut(title_box), FadeIn(lumina, shift=RIGHT * 0.5), run_time=2.0)
        self.play(
            lumina.animate.shift(RIGHT * 3.5),
            fireflies.animate.shift(UP * 0.4 + LEFT * 0.3),
            run_time=4.5,
            rate_func=linear
        )
        self.wait(1.0)

        # ช่วงที่ 3 (16-24 วิ): ลูมินาเดินต่อและหิ่งห้อยลอยวนรอบตะเกียง
        self.play(
            lumina.animate.shift(RIGHT * 2.5),
            lantern_glow.animate.scale(1.3),
            fireflies.animate.shift(DOWN * 0.3 + RIGHT * 0.4),
            run_time=4.5,
            rate_func=linear
        )
        self.wait(1.0)

        # ช่วงที่ 4 (24-30 วิ): สัญญาณ Error สีแดงปรากฏขึ้น ลูมินาหันมองด้วยความตกใจ
        self.play(FadeIn(error_signal), lantern_glow.animate.set_color(RED_A), run_time=2.0)
        self.play(
            error_glow.animate.scale(1.4),
            lumina.animate.shift(LEFT * 0.4),
            run_time=2.5
        )
        self.wait(2.0)
        
