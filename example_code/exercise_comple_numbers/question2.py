from manim import *

class Question2(Scene):
    def construct(self):
        #---------------------------------------------------------------------------------
        # PART ONE 

        # Define the text
        text1 = MathTex(
            "\\text{If z is a given complex number and $k \in \mathbb{N}$, }",
            color=WHITE,
            font_size=40
        )
        text2 = MathTex(
            "\\text{will the sequence } z^k",
            "\\text{ converge }"
            "\\text{for } k \\rightarrow +\\infty",
            "\\text{ and where?}",
            color=WHITE,
            font_size=40
        ).next_to(text1, DOWN)
        
        # Group and position the text
        text = VGroup(text1, text2)
        text.move_to(ORIGIN)

        # Animate the text
        self.play(FadeIn(text, scale=1.3))
        self.wait(3)

        #---------------------------------------------------------------------
        # Part 2: ADDING GRAPH

        # Define the graph with dots
        graph = Axes(
            x_range=(-2.9, 2.9),
            y_range=(-1.5, 1.5),
            ).scale(0.7).add_coordinates()  # Adjust the scale

        # Label the imaginary and real axes
        x_label = MathTex(
            "\\text{Re(z)}", 
            font_size=30
            ).next_to(graph.x_axis.get_end(), RIGHT)
        y_label = MathTex(
            "\\text{Im(z)}", 
            font_size=30
            ).next_to(graph.y_axis.get_end(), UP)

        #Dots of interest
        c_dot = Dot(graph.coords_to_point(0, 0), color=GREEN)
        b_dot = Dot(graph.coords_to_point(0, 1), color=RED)
        a_dot = Dot(graph.coords_to_point(1, 0), color=YELLOW)
        z_dot = Dot(graph.coords_to_point(1, 1), color=WHITE)
        lines = graph.get_lines_to_point(graph.c2p(1,1))

        # Add labels to the dots
        #c_label = MathTex(" ", color=BLUE).next_to(c_dot, DOWN+LEFT).scale(0.8)
        #b_label = MathTex(" ",color=BLUE).next_to(b_dot, LEFT).scale(0.8)
        #a_label = MathTex(" ",color=BLUE).next_to(a_dot, DOWN).scale(0.8)
        z_label = MathTex("\\text{z = 1 + 1j}",font_size=30).next_to(z_dot,UP+RIGHT)

        # Create a VGroup containing the graph and dots
        #graph1 = VGroup(graph, x_label, y_label, z_dot,z_label, graph,c_dot,c_label, b_dot, b_label, a_dot, a_label, lines).move_to(ORIGIN + DOWN)
        graph1 = VGroup(graph, x_label, y_label, z_dot,z_label, graph,c_dot, b_dot, a_dot, lines).move_to(ORIGIN + DOWN)
        
        # Add graph and dots to the scene
        # Moving text up
        self.play(
            text.animate.move_to(ORIGIN+2.5*UP).scale(0.9),
            FadeIn(graph, x_label, y_label)
            )
        self.wait(2)
        self.play(FadeIn(lines),
                  FadeIn(z_dot, scale = 10),
                  FadeIn(z_label)
                  )
        self.wait(2)
        self.play(FadeIn(a_dot, scale = 10))
        self.play(FadeIn(b_dot, scale = 10))
        self.play(FadeIn(c_dot, scale = 10))
        self.wait(5)

        # Fade out
        self.play(FadeOut(text),
                  FadeOut(graph1))
        
