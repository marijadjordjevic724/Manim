from manim import *

class Question2(Scene):
    def construct(self):
        #---------------------------------------------------------------------------------
        # PART ONE 

        # Define the text
        text1 = MathTex(
            "\\text{If } z", 
            "\\text{ is the complex number }",
            "\\text{} z = 1 + 1j", 
            "\\text{ and $k \in \mathbb{N}^+$, }",
            color=WHITE,
            font_size=40
        )
        text2 = MathTex(
            "\\text{what happens to the sequence } z^k",
            "\\text{ as }",
            "\\text{ $\lim_{k \\rightarrow +\infty} z^k$ }",
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
        a_dot = Dot(graph.coords_to_point(1, 0), color=YELLOW)
        b_dot = Dot(graph.coords_to_point(0, 1), color=RED)
        c_dot = Dot(graph.coords_to_point(0, 0), color=GREEN)
        z_dot = Dot(graph.coords_to_point(1, 1), color=WHITE)
        lines = graph.get_lines_to_point(graph.c2p(1,1))

        # Add labels to the dots
        a_label = MathTex("a",color=YELLOW).next_to(a_dot, DOWN+RIGHT).scale(0.8)
        b_label = MathTex("b",color=RED).next_to(b_dot, RIGHT).scale(0.8)
        c_label = MathTex("c", color=GREEN).next_to(c_dot, DOWN+LEFT).scale(0.8)
        z_label = MathTex("z = 1 + 1j",font_size=30).next_to(z_dot,UP+RIGHT)

        # Create a VGroup containing the graph and dots
        #graph1 = VGroup(graph, x_label, y_label, z_dot,z_label, graph,c_dot,c_label, b_dot, b_label, a_dot, a_label, lines).move_to(ORIGIN + DOWN)
        graph1 = VGroup(graph, x_label, y_label, z_dot,z_label, graph, lines).move_to(ORIGIN + DOWN)
        graph2 = VGroup(a_dot, a_label, b_dot, b_label, c_dot, c_label).move_to(ORIGIN + DOWN)

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
        self.wait(5)

        # Remove task description (to remove clutter) and show answer options

        self.play(FadeOut(text))
        self.play(
            graph1.animate.move_to(ORIGIN + 2*LEFT + 0.5*DOWN)
        )

        a_dot.move_to(graph.get_center() + (1.45)*RIGHT)
        b_dot.move_to(graph.get_center() + (1.4)*UP)
        c_dot.move_to(graph.get_center())

        a_label.next_to(a_dot, DOWN+RIGHT)
        b_label.next_to(b_dot, RIGHT)
        c_label.next_to(c_dot, DOWN+LEFT)
        
        a_answer = MathTex(
            "\\text{a. } z^k",
            "\\text{ converges to } 1 + 0j",
            color=WHITE,
            font_size=40
        ).move_to(ORIGIN + 4*RIGHT + 3.25*UP)
        b_answer = MathTex(
            "\\text{b. } z^k",
            "\\text{ converges to } 0 + 1j",
            color=WHITE,
            font_size=40
        ).move_to(ORIGIN + 4*RIGHT + 2.25*UP)
        c_answer = MathTex(
            "\\text{c. } z^k",
            "\\text{ converges to } 0 + 0j",
            color=WHITE,
            font_size=40
        ).move_to(ORIGIN + 4*RIGHT + 1.25*UP)
        d_answer = MathTex(
            "\\text{d. } z^k",
            "\\text{ diverges }",
            color=WHITE,
            font_size=40
        ).move_to(ORIGIN + 3*RIGHT + 0.25*UP)

        graph3 = VGroup(a_answer, b_answer, c_answer, d_answer)

        a_answer[0][0:2].set_color(YELLOW)
        b_answer[0][0:2].set_color(RED)
        c_answer[0][0:2].set_color(GREEN)
        d_answer[0][0:2].set_color(PURE_BLUE)

        self.play(FadeIn(a_dot, scale = 10),
                  FadeIn(a_label),
                  FadeIn(a_answer))
        self.play(FadeIn(b_dot, scale = 10),
                  FadeIn(b_label),
                  FadeIn(b_answer))
        self.play(FadeIn(c_dot, scale = 10),
                  FadeIn(c_label),
                  FadeIn(c_answer))
        self.play(FadeIn(d_answer))
        self.wait(5)

        # Fade out
        self.play(FadeOut(graph1),
                  FadeOut(graph2),
                  FadeOut(graph3))
        
