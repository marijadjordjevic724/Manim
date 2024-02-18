from manim import *

class JordanFormAnimation(Scene):
    def construct(self):
        # The original matrix
        original_matrix = [[5, 4, 2, 1], [0, 1, -1, -1], [-1, -1, 3, 0],[1, 1, -1, 2]]

        # The Jordan form
        jordan_form = [[1, 0, 0, 0], [0, 2, 0, 0], [0, 0, 4, 1],[0, 0, 0, 4]]

        # Visual representations of the matrices
        original_matrix_tex = Matrix(original_matrix)
        jordan_form_tex = Matrix(jordan_form)
        text1 = Text('Original Matrix', font_size=30, color=BLUE).next_to(original_matrix_tex, direction=UP)
        text2 = Text('Jordan Form', font_size=30, color=BLUE).next_to(jordan_form_tex, direction=UP)
        
        # Add matrices to the scene
        self.play(Write(text1))
        self.play(Write(original_matrix_tex))
        self.wait(3)

        # Animating transformation to Jordan form
        self.play(Transform(text1, text2))
        self.play(Transform(original_matrix_tex, jordan_form_tex))
        self.wait(3)
