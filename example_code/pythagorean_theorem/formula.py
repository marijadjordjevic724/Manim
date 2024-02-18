from manim import *

class HighlightFormula(Scene):
    def construct(self):
        formula = MathTex(
            "a^{2}+b^{2}=c^{2}",
            color=WHITE,
            font_size=50
        )

        # Position the formula in the center of the screen
        formula.move_to(ORIGIN)

        # Create a right triangle centered on the screen
        triangle = VGroup(
            Line(1.5 * LEFT + 1 * DOWN, 1.5 * RIGHT + 1 * DOWN, color=ORANGE, stroke_width=6),
            Line(1.5 * LEFT + 1 * DOWN, 1.5 * LEFT + 1 * UP, color=ORANGE, stroke_width=6),
            Line(1.5 * RIGHT + 1 * DOWN, 1.5 * LEFT + 1 * UP, color=ORANGE, stroke_width=6),
        )
        triangle.move_to(ORIGIN) 

        # Animate the transformation of the formula to the triangle
        self.play(Write(formula))
        # Move 'a', 'b', and 'c' and fade out the rest
        self.play(*[FadeOut(formula[0][i]) for i in range(len(formula[0])) if i not in [0, 3, 6]])
        self.play(
            formula[0][0].animate.move_to(triangle.get_left() + 0.5*LEFT),
            formula[0][3].animate.move_to(triangle.get_bottom() + 0.5 * DOWN),
            formula[0][6].animate.move_to(triangle.get_right() + 1 * LEFT + 0.5*UP)
        )

        # Animate the addition of the triangle
        self.play(Write(triangle))

        # Draw a full rectangle
        # Additional lines to complete the rectangle
        line_up = Line(1.5 * RIGHT + 1 * DOWN, 1.5 * RIGHT + 1 * UP, color=WHITE, stroke_width=6).set_opacity(0.2)  # Right side (vertical)
        line_right = Line(1.5 * LEFT + 1 * UP, 1.5 * RIGHT + 1 * UP, color=WHITE, stroke_width=6).set_opacity(0.2)  # Top side (horizontal)
    
        self.play(
            Write(line_up),
            Write(line_right)
        )

        # Add the surface area equation
        text = Text('Triangle surface area:', font_size=30, color=ORANGE).next_to(triangle, direction= RIGHT+ 0.01*UP, buff=0.5)
        self.play(Write(text))
        surface_area_eq = MathTex(
            "S = \\frac{1}{2}ab",
            color=WHITE,
            font_size=40
        ).next_to(text, direction=DOWN, buff=0.5)
        self.play(Write(surface_area_eq))

        self.wait(5)
