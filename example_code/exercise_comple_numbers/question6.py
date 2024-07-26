from manim import *
import numpy as np
import math

class Question6(Scene):
    def construct(self):

        # Defining axes
        axes = Axes(
            x_range=[0, 2.2*PI, 1],
            y_range=[-0.9, 2.5, 1],
            axis_config={"color": LIGHT_GRAY},
            y_length = 7,
            x_length = 11
        ).move_to(0.7*LEFT+0.3*DOWN).scale(0.85)
        labels = axes.get_axis_labels(x_label="t", y_label="h(t)").scale(0.95)

        # Parameters and functions
        alpha = -1.8
        beta = -0.25
        omega1 = 20
        omega2 = 3

        combined = lambda x: math.exp(alpha*x)*np.cos(omega1*x) + math.exp(beta*x)*np.cos(omega2*x)

        # Creating signals on axes
        combined_signal = axes.plot(combined, color=PURPLE)
        combined_label = VGroup(
            MathTex(r"\text{Which type of LTI system may}",color=PURPLE),
            MathTex(r"\text{produce this impulse response?}",color=PURPLE),
            MathTex(r"\text{\: a) first order}",color=LIGHT_GRAY),
            MathTex(r"\text{\: b) second order}",color=LIGHT_GRAY),
            MathTex(r"\text{\: c) third order}",color=LIGHT_GRAY),
            MathTex(r"\text{\: d) at least fourth order}",color=LIGHT_GRAY),
            ).arrange(DOWN, center=False, aligned_edge=LEFT).scale(0.9)
        combined_label.move_to(1.5*UP+2.7*RIGHT)

        VGroup(combined_label[2], combined_label[3],combined_label[4],combined_label[5]).shift(RIGHT)

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
        self.wait(0.5)
        self.play(Write(combined_label[5]))
        self.wait(4)

        self.play(*[FadeOut(mob)for mob in self.mobjects])