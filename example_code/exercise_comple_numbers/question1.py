from manim import *

class Question1(Scene):
    def construct(self):
        #---------------------------------------------------------------------------------
        # PART ONE 

        # Define the text
        text1 = MathTex(
            "\\text{If z is a given complex number,  will the sequence }",
            color=WHITE,
            font_size=40,
        )
        text2 = MathTex(
            "z^k",
            "\\text{ converge }"
            "\\text{for } k \\rightarrow +\\infty",
            "\\text{ and where?}",
            color=WHITE,
            font_size=40,
        ).next_to(text1, DOWN)
        
        # Group and position the text
        text = VGroup(text1, text2)
        text.move_to(ORIGIN)

        # Animate the text
        self.play(FadeIn(text, scale=1.3))
        self.wait(3)

        # Define the graph with dots
        graph = Axes(
            x_range=(-1, 1),
            y_range=(-1, 1),
            axis_config={"color": WHITE},
            tips=False,
            color = LIGHT_GRAY
        ).scale(0.5)  # Adjust the scale

        # Set the same length for both axes
        graph.width = 1
        graph.height = 4

        c_dot = Dot(color=RED).move_to(ORIGIN)
        b_dot = Dot(color=GREEN).move_to(UP*1.6)
        a_dot = Dot(color=BLUE).move_to(RIGHT*1.6)
        z_dot = Dot(color=WHITE).move_to(0.8*RIGHT+0.8*UP)

        # Label the imaginary and real axes
        x_label = Tex("Re(z)", color=LIGHT_GRAY).next_to(graph.x_axis.get_end(), RIGHT).scale(0.8)
        y_label = Tex("Im(z)", color=LIGHT_GRAY).next_to(graph.y_axis.get_end(), UP).scale(0.8)

        # Add labels to the dots
        c_label = Tex("c", color=RED).next_to(c_dot, DOWN+LEFT).scale(0.8)
        b_label = Tex("b",color=GREEN).next_to(b_dot, LEFT).scale(0.8)
        a_label = Tex("a",color=BLUE).next_to(a_dot, DOWN).scale(0.8)
        z_label = MathTex("z",color=LIGHT_GRAY,font_size=30).next_to(z_dot, RIGHT*1.5 + UP).scale(1.2)

        # Create a VGroup containing the graph and dots
        graph1 = VGroup(z_dot,z_label, graph, x_label,y_label,c_dot,c_label, b_dot, b_label, a_dot, a_label).move_to(ORIGIN + DOWN)
        
        # Add graph and dots to the scene
        #Moving text up
        self.play(text.animate.move_to(ORIGIN+2.5*UP).scale(0.9),
                  FadeIn(z_dot,z_label, scale = 1),
                  FadeIn(graph, x_label,y_label, scale = 1))
        self.wait(2)
        self.play(FadeIn(a_dot, a_label, scale = 1.5))
        self.play(FadeIn(b_dot, b_label, scale = 1.5))
        self.play(FadeIn(c_dot,c_label, scale = 1.5))
        self.wait(5)

        # Fade out
        self.play(FadeOut(text, scale = 1.5),
                  FadeOut(graph1, scale = 1.5))
        
