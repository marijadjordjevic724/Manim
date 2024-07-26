from manim import *
import numpy as np
import math

class Solution6(Scene):
    def construct(self):

        # Defining axes
        axes = Axes(
            x_range=[0, 2.2*PI, 1],
            y_range=[-0.9, 2.5, 1],
            axis_config={"color": LIGHT_GRAY},
            y_length = 7,
            x_length = 11
        ).move_to(0.7*LEFT+0.3*DOWN).scale(0.85)
        axes1 = axes.copy()
        axes1.move_to(2*UP+ 2.5*LEFT).scale(0.45),
        axes2 = axes.copy()
        axes2.move_to(1.7*DOWN + 2.5*LEFT).scale(0.45)
        labels = axes.get_axis_labels(x_label="t", y_label="h(t)").scale(0.9)
        axes3 = axes.copy().move_to(2.5*LEFT+2*UP).scale(0.5)

        # Parameters and functions
        alpha = -1.8
        beta = -0.25
        omega1 = 20
        omega2 = 3

        f1 = lambda x: math.exp(alpha*x)*np.cos(omega1*x)
        f2 = lambda x: math.exp(beta*x)*np.cos(omega2*x)
        combined = lambda x: math.exp(alpha*x)*np.cos(omega1*x) + math.exp(beta*x)*np.cos(omega2*x)

        # Creating signals on axes
        function1 = axes.plot(f1, color=BLUE_C)
        function2 = axes.plot(f2, color=RED_B)
        combined_signal = axes.plot(combined, color=PURPLE)
        combined_label = VGroup(
            MathTex(r"\text{Notice that this LTI impulse response is}",color=LIGHT_GRAY),
            MathTex(r"\text{a sum of two decaying oscillatory behaviours}",color=LIGHT_GRAY)
        ).arrange(DOWN, center=False, aligned_edge = RIGHT).move_to(1.8*RIGHT+2.5*UP).scale(0.95)
        # Animating combined signal first
        self.play(Create(axes), Write(labels))
        self.wait(0.5)
        self.play(Write(combined_label[0]),Create(combined_signal))
        self.wait(1)
        self.play(Write(combined_label[1]), runtime = 1)
        self.wait(3)

        # Animating the separation into two signals
        self.play(
            ReplacementTransform(combined_signal, VGroup(function1, function2)),
            runtime=1
        )
        self.wait(3)


        # SECOND PART 

        # Seperating two signals into two graphs
        self.play(FadeOut(labels, combined_label))
        
        # Creating signals on axis1 and axis2
        function1_seperate = axes1.plot(f1, color=BLUE_C)
        function2_seperate = axes2.plot(f2, color=RED_B)

        function1_label = VGroup(
            MathTex(r'&\text{Behaves like } e^{\alpha t} \cdot \cos(\omega_1 t)', color=BLUE_C),
            MathTex(r'&\cdot \text{ frequency } \omega_1', color=LIGHT_GRAY),
            MathTex(r'&\cdot \text{ decay factor } \alpha ', color=LIGHT_GRAY),
            MathTex(r'&\cdot \text{ 2nd order subsystem}', color=LIGHT_GRAY)
        ).arrange(DOWN, center=False, aligned_edge=LEFT).next_to(axes1, RIGHT).scale(0.9)
        
        function2_label = VGroup(
            MathTex(r'&\text{Behaves like } e^{\beta t}\cdot \cos(\omega_2 t)', color=RED_B),
            MathTex(r'&\cdot \text{ smaller frequency: } \omega_2<\omega_1 ', color=LIGHT_GRAY),
            MathTex(r'&\cdot \text{ decaying slower: }\beta>\alpha', color=LIGHT_GRAY),
            MathTex(r'&\cdot \text{ 2nd order subsystem}', color=LIGHT_GRAY)
        ).arrange(DOWN, center=False, aligned_edge=LEFT).next_to(axes2, RIGHT).scale(0.9)

        self.play(
            ReplacementTransform(axes, VGroup(axes1, axes2)),
            ReplacementTransform(function1,function1_seperate),
            ReplacementTransform(function2,function2_seperate),
            runtime = 0.2
            )
        self.wait(2)

        self.play(Write(function1_label[0]))
        self.wait(1)
        self.play(Write(function2_label[0]))
        self.wait(2)

        text = MathTex(r'\alpha,\beta < 0', color=LIGHT_GRAY).next_to(axes1, DOWN)
        text.scale(0.8)
        self.play(Write(text), runtime = 0.1)
        self.wait(2)

        self.play(Write(function1_label[1]), runtime = 0.1)
        self.wait(1)
        self.play(Write(function1_label[2]), runtime = 0.1)
        self.wait(2)
        self.play(Write(function1_label[3]), runtime = 0.1)
        self.wait(2)

        self.play(Write(function2_label[1]), runtime = 0.1)
        self.wait(1)
        self.play(Write(function2_label[2]), runtime = 0.1)
        self.wait(2)
        self.play(Write(function2_label[3]), runtime = 0.1)
        self.wait(3)

        #Switching back to one graph
        combined_signal = axes3.plot(combined, color=PURPLE)

        #Adding final deductions
        formula = MathTex(
            r' e^{\alpha t} \cdot \cos(\omega_1 t) + e^{\beta t}\cdot \cos(\omega_2 t)', color=PURPLE
        ).move_to(2.5*UP+2*RIGHT)
        combined_label = VGroup(
            MathTex(r'&\text{Our LTI impulse response consists of two distinct', color=LIGHT_GRAY),
            MathTex(r'&\text{modes corresponding to 2nd order subsystems}', color=LIGHT_GRAY),
            MathTex(r'&\text{  } \Rightarrow \text{ system is at least 4th order}', color=PURPLE)
        ).arrange(DOWN).scale(0.95).move_to(1.5*DOWN)

        self.play(
            FadeOut(
                function1_label[3],
                function1_label[2],
                function1_label[1], 
                function2_label[3],
                function2_label[2],
                function2_label[1],
                text, 
                axes1, 
                axes2),
            ReplacementTransform(
                VGroup(function1_seperate, function2_seperate), 
                combined_signal),
            Create(axes3),
            ReplacementTransform(
                VGroup(function1_label[0],function2_label[0]), 
                formula),
            runtime = 0.2
            )
        self.wait(3)
        self.play(Write(combined_label[0]))
        self.play(Write(combined_label[1]), runtime = 0.1)
        self.wait(1)
        self.play(Write(combined_label[2]), runtime = 0.1)
        self.wait(4)
        
        self.play(*[FadeOut(mob)for mob in self.mobjects])



