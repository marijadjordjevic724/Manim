from manim import *
import numpy as np
import math

class Solution7(Scene):
    def construct(self):

        # Defining axes
        axes = Axes(
            x_range=[0, 3, 0.5],
            y_range=[0, 1, 0.2],
            axis_config={"color": LIGHT_GRAY, "include_numbers": True},
            y_length = 6,
            x_length = 10
        ).move_to(0.7*LEFT+0.3*DOWN).scale(0.85)
        axes1 = axes.copy()
        axes1.move_to(2*UP+ 2.5*LEFT).scale(0.45),
        axes2 = axes.copy()
        axes2.move_to(1.7*DOWN + 2.5*LEFT).scale(0.45)
        labels = axes.get_axis_labels(x_label="t", y_label="h(t)").scale(0.9)
        axes3 = axes.copy().move_to(2.5*LEFT+2*UP).scale(0.5)

        # Parameters and functions
        alpha = -10
        beta = -2

        f1 = lambda x: math.exp(alpha*x)
        f2 = lambda x: 2*x*math.exp(beta*x)
        combined = lambda x: math.exp(alpha*x) + 2*x*math.exp(beta*x)
        
        # Creating signals on axes
        function1 = axes.plot(f1, color=BLUE_C)
        function2 = axes.plot(f2, color=RED_B)
        combined_signal = axes.plot(combined, color=PURPLE)
        combined_label = VGroup(
            MathTex(r"\text{From observing LTI impulse response,}",color=LIGHT_GRAY),
            MathTex(r"\text{one can extract information that will}",color=LIGHT_GRAY),
             MathTex(r"\text{help identify possible modes.}",color=LIGHT_GRAY),
        ).arrange(DOWN, center=False, aligned_edge = LEFT).move_to(1.8*RIGHT+1.5*UP).scale(0.90)
        
        # Animating combined signal first
        self.play(Create(axes), Write(labels))
        self.wait(0.5)
        self.play(Write(combined_label[0]),Create(combined_signal))
        self.play(Write(combined_label[1]), runtime = 1)
        self.play(Write(combined_label[2]), runtime = 1)
        self.wait(3)
        self.play(FadeOut(combined_label))

        # Deductions
        deductions = VGroup(
            MathTex(r"\cdot\text{ Stable system}\Rightarrow\text{ all modes are stable}",color=LIGHT_GRAY),
            MathTex(r"\cdot \text{ No noticeable oscillatory behaviour}",color=LIGHT_GRAY),
            MathTex(r"\cdot \text{ Initially, function is exponentially decreasing}",color=LIGHT_GRAY),
            MathTex(r"\Rightarrow \text{ fast decreasing 1st order mode}",color=BLUE_C),
            MathTex(r"\cdot \text{ Function is not monotonically decreasing}",color=LIGHT_GRAY),
            MathTex(r" \text{ but exibits exponential behaviour asymptotically}",color=LIGHT_GRAY),
            MathTex(r"\Rightarrow \text{ slower decreasing 2nd order mode}",color=RED_B)
        ).arrange(DOWN, center=False, aligned_edge = LEFT).move_to(3*RIGHT+UP).scale(0.7)
        
        self.play(Write(deductions[0]))
        self.wait(1)
        self.play(Write(deductions[1]))
        self.wait(1)
        self.play(Write(deductions[2]))
        self.wait(0.5)
        self.play(Write(deductions[3]))
        self.wait(1)
        self.play(Create(function1))
        self.wait(1)
        self.play(Write(deductions[4]))
        self.wait(0.5)
        self.play(Write(deductions[5]))
        self.wait(0.5)
        self.play(Write(deductions[6]))
        self.wait(1)
        self.play(Create(function2))
        self.wait(2)

        # Animating the separation into two signals
        self.play(
            FadeOut(combined_signal),
            runtime=1
        )
        self.wait(3)


        # SECOND PART 

        # Seperating two signals into two graphs
        self.play(FadeOut(labels, deductions))
        
        # Creating signals on axis1 and axis2
        function1_seperate = axes1.plot(f1, color=BLUE_C)
        function2_seperate = axes2.plot(f2, color=RED_B)

        function1_label = VGroup(
            MathTex(r'&\text{First mode: } e^{-10t}', color=BLUE_C),
            MathTex(r'&\cdot \text{ 1st order subsystem}', color=LIGHT_GRAY)
        ).arrange(DOWN, center=False, aligned_edge=LEFT).next_to(axes1, RIGHT).scale(0.9)
        
        function2_label = VGroup(
            MathTex(r'&\text{Second mode: } 2t \cdot e^{-2t}', color=RED_B),
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

        self.play(Write(function1_label[1]), runtime = 0.1)
        self.wait(2)
        self.play(Write(function2_label[1]), runtime = 0.1)
        self.wait(2)

        #Switching back to one graph
        combined_signal = axes3.plot(combined, color=PURPLE)

        #Adding final deductions
        formula = MathTex(
            r' e^{-10t} + 2t \cdot e^{-2t}', color=PURPLE
        ).move_to(2.5*UP+2*RIGHT)
        combined_label = VGroup(
            MathTex(r'&\text{Our LTI impulse response consists of two distinct', color=LIGHT_GRAY),
            MathTex(r'&\text{modes corresponding to 1st and 2nd order subsystems}', color=LIGHT_GRAY),
            MathTex(r'&\text{  } \Rightarrow \text{ system is at least 3rd order}', color=PURPLE)
        ).arrange(DOWN).scale(0.95).move_to(1.5*DOWN)

        self.play(
            FadeOut(
                function1_label[1], 
                function2_label[1],
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



