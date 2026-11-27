 from manim import *

class WhisperingWoodsScene1(Scene):
    def construct(self):
        # ตั้งค่าพื้นหลังสีน้ำเงินเข้มเหมือนป่าตอนกลางคืน
        self.camera.background_color = "#0b132b"

        # สร้างแสงหิ่งห้อยเรืองแสงในป่า
        fireflies = VGroup(*[
            Dot(
                point=[np.random.uniform(-6, 6), np.random.uniform(-3, 3), 0],
                radius=0.06,
                color=YELLOW
            ).set_opacity(0.8)
            for _ in range(25)
        ])

        # ชื่อเรื่องแอนิเมชัน
        title = Text("Code of the Whispering Woods", font_size=40, color=BLUE_B)
        subtitle = Text("Scene 1: คืนที่โค้ดมีชีวิต", font_size=26, color=YELLOW_B).next_to(title, DOWN)

        # ตะเกียงแสงจันทร์ของลูมินา (จำลองด้วยวงกลมเรืองแสง)
        lantern_glow = Circle(radius=0.8, color=GOLD, fill_opacity=0.2, stroke_width=0)
        lantern_core = Dot(radius=0.15, color=WHITE)
        lantern = VGroup(lantern_glow, lantern_core).shift(DOWN * 1.5)

        # ลำดับภาพเคลื่อนไหว
        self.play(FadeIn(fireflies, lag_ratio=0.1), run_time=2)
        self.play(Write(title), FadeIn(subtitle, shift=UP*0.3), run_time=2)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle))
        self.play(GrowFromCenter(lantern), fireflies.animate.shift(UP * 0.5), run_time=2)
        self.play(lantern.animate.shift(RIGHT * 3), run_time=2)
        self.wait(1)
