from manim import *

class SineWaveScene(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-PI, PI, PI/2],
            y_range=[-1.5, 1.5, 1],
            axis_config={"color": LIGHT_GRAY},
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y")
        amplitude_scale = 0.3 
        sine_wave = axes.plot(lambda x: amplitude_scale*np.sin(8*x), color=DARK_BLUE)
        sine_label = MathTex(r"\text{Sine Wave}").next_to(sine_wave, 3*UP)
        sine_label.shift(RIGHT*5)
 
        # Creating the ramp signal
        ramp_signal = axes.plot(lambda x: max(x / PI, 0), color=DARK_BLUE)
        ramp_label = MathTex(r"\text{Ramp Signal}").next_to(ramp_signal, UP)
        ramp_label.shift(RIGHT*5)

        # Animating the creation of the axes, sine wave, and labels
        self.play(Create(axes), Write(labels))
        self.play(Create(sine_wave), Write(sine_label))
        self.wait(2)

        # Replacing the sine wave with the ramp signal
        self.play(ReplacementTransform(sine_label, ramp_label))
        self.play(ReplacementTransform(sine_wave, ramp_signal))
        self.wait(2)

        # Creating the combined signal (ramp signal plus sine wave)
        combined_signal = axes.plot(lambda x: max(x / PI, 0) + amplitude_scale*np.sin(8*x), color=DARK_BLUE)
        combined_label = MathTex(r"\text{Combined Signal}").next_to(combined_signal, UP)
        combined_label.shift(RIGHT*5)

        # Animating the combination of ramp signal and sine wave
        self.play(ReplacementTransform(ramp_label, combined_label))
        self.play(ReplacementTransform(ramp_signal, combined_signal))
        self.wait(5)
