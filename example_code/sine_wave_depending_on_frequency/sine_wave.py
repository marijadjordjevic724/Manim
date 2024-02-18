from manim import *

class SineWaveScene(Scene):
    def construct(self):
        # Defining the axes
        axes = Axes(
            x_range=[-PI, PI, PI/2],
            y_range=[-1.5, 1.5, 1],
            axis_config={"color": LIGHT_GRAY},
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Sine functions with different frequencies
        sine_wave = axes.plot(lambda x: np.sin(2*x), color=DARK_BLUE)
        sine_wave2 = axes.plot(lambda x: np.sin(1*x), color=DARK_BLUE)
        sine_wave3 = axes.plot(lambda x: np.sin(4*x), color=DARK_BLUE)

        # Labels
        sine_label = MathTex(r"y = \sin(x)").next_to(sine_wave, UP)
        sine_label.shift(RIGHT*5)
        sine_label2 = MathTex(r"y = \sin( \frac{x}{2})").next_to(sine_wave2, UP)
        sine_label2.shift(RIGHT*5)
        sine_label3 = MathTex(r"y = sin(2x)").next_to(sine_wave3, UP)
        sine_label3.shift(RIGHT*5)

        # Animating the first function
        self.play(Create(axes), Write(labels))
        self.play(Create(sine_wave), Write(sine_label))
        self.wait(2)

        # Second sine wave
        self.play(ReplacementTransform(sine_label, sine_label3))
        self.play(ReplacementTransform(sine_wave, sine_wave3))
        self.wait(2)

        # Third sine wave
        self.play(ReplacementTransform(sine_label3, sine_label2))
        self.play(ReplacementTransform(sine_wave3, sine_wave2))
        self.wait(5)
