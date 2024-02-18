from manim import *

class CombinedAnimation(Scene):
    def construct(self):
        # Display the filter formula
        filter_formula = MathTex("H(s) = \\frac{1}{s^2 + s + 1}")
        self.play(Write(filter_formula))
        self.wait(1)
        
        # Transitioning the formula to the upper right corner and making it smaller
        self.play(filter_formula.animate.scale(0.8).to_edge(UP))
        self.wait(1)

        # Setup for Bode plots
        # Magnitude Plot
        mag_axes = Axes(
            x_range=[0, 10, 1], y_range=[0, 5, 1],
            x_length=4, y_length=2,
            axis_config={"color": BLUE},
        )
        mag_label = mag_axes.get_axis_labels(x_label="f (Hz)", y_label="|H(f)| (dB)")
        mag_plot = mag_axes.plot(lambda x: 2 - 0.2 * x, color=GREEN)  # Simplified plot
        
        mag_graph = VGroup(mag_axes, mag_label, mag_plot).to_edge(LEFT)
        # Phase Plot
        phase_axes = Axes(
            x_range=[0, 10, 1], y_range=[-180, 0, 45],
            x_length=4, y_length=2,
            axis_config={"color": BLUE},
        )
        phase_label = phase_axes.get_axis_labels(x_label="f (Hz)", y_label="Phase (degrees)")
        phase_plot = phase_axes.plot(lambda x: -45 if x > 0 else 0, color=RED)  # Simplified plot
        
        phase_graph = VGroup(phase_axes, phase_label, phase_plot).next_to(mag_graph, RIGHT, buff=1)

        # Display Bode plots
        self.play(
            FadeIn(mag_graph),
            FadeIn(phase_graph),
        )
        self.wait(2)
