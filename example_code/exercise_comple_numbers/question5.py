from manim import *
import numpy as np
import math

class Question5(Scene):
    def construct(self):

        # Defining axes
        axes = Axes(
            x_range=[0, 1.2*PI, 1],
            y_range=[0, 2.5, 1],
            axis_config={"color": LIGHT_GRAY},
            y_length = 6,
            x_length = 10
        ).move_to(1.5*LEFT+0.5*DOWN).scale(0.9)
        labels = axes.get_axis_labels(x_label="t", y_label="h(t)")

        # Parameters and functions
        alpha = -1.9
        beta = -0.5
        omega = 8

        combined = lambda x: math.exp(beta*x) + math.exp(alpha*x)*np.cos(omega*x)

        # Creating signals on axes
        combined_signal = axes.plot(combined, color=PURPLE)
        combined_label = VGroup(
            MathTex(r"\text{Which type of LTI system may produce}",color=PURPLE),
            MathTex(r"\text{this impulse response?}",color=PURPLE),
            MathTex(r"\text{\: a) first order}",color=LIGHT_GRAY),
            MathTex(r"\text{\: b) second order}",color=LIGHT_GRAY),
            MathTex(r"\text{\: c) at least third order}",color=LIGHT_GRAY),
            ).arrange(DOWN, center=False, aligned_edge=LEFT)  
        combined_label.move_to(2*RIGHT+1.5*UP)

        VGroup(combined_label[2], combined_label[3],combined_label[4]).shift(RIGHT)

        # Animating impulse response and the question lines
        
        self.play(Create(axes), Write(labels))
        self.wait(0.5)
        self.play(Write(combined_label[0]))
        self.play(
            Write(combined_label[1]),
            Create(combined_signal),
            runtime = 0.5)
        self.wait(2)
        self.play(Write(combined_label[2]))
        self.wait(0.5)
        self.play(Write(combined_label[3]))
        self.wait(0.5)
        self.play(Write(combined_label[4]))
        self.wait(4)

        self.play(*[FadeOut(mob)for mob in self.mobjects])