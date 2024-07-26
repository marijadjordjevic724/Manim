from manim import *
import numpy as np
import math

class Question7(Scene):
    def construct(self):

        # Defining axes
        axes = Axes(
            x_range=[0, 3, 0.5],
            y_range=[0, 1, 0.2],
            axis_config={"color": LIGHT_GRAY, "include_numbers": True},
            y_length = 6,
            x_length = 10
        ).move_to(0.2*LEFT+0.3*DOWN).scale(0.85)
        labels = axes.get_axis_labels(x_label="t", y_label="h(t)").scale(0.95)

        # Parameters and functions
        alpha = -10
        beta = -2

        combined = lambda x: math.exp(alpha*x) + 2*x*math.exp(beta*x)

        # Creating signals on axes
        combined_signal = axes.plot(combined, color=PURPLE)
        combined_label = VGroup(
            MathTex(r"\text{Which type of LTI system may}",color=PURPLE),
            MathTex(r"\text{produce this impulse response?}",color=PURPLE),
            MathTex(r"\text{\: a) first order}",color=LIGHT_GRAY),
            MathTex(r"\text{\: b) second order}",color=LIGHT_GRAY),
            MathTex(r"\text{\: c) at least third order}",color=LIGHT_GRAY),
            ).arrange(DOWN, center=False, aligned_edge=LEFT).scale(0.9)
        combined_label.move_to(1.5*UP+2.7*RIGHT)

        VGroup(combined_label[2], combined_label[3],combined_label[4]).shift(RIGHT)

        # Animating impulse response and the question lines
        self.play(Create(axes), Write(labels))
        self.wait(0.5)
        self.play(Write(combined_label[0]))
        self.play(
            Create(combined_signal),
            Write(combined_label[1]),
            runtime = 0.5
            )
        self.wait(2)
        self.play(Write(combined_label[2]))
        self.wait(0.5)
        self.play(Write(combined_label[3]))
        self.wait(0.5)
        self.play(Write(combined_label[4]))
        self.wait(4)

        self.play(*[FadeOut(mob)for mob in self.mobjects])