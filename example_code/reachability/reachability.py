from manim import *

class ReachabilityMatrix(Scene):
    def construct(self):
        # Defininig the system matrix F and input matrix g 
        F = [[1, 2],
             [0, 3]]
        g = [[1],
             [0]]

        # Displaying F and g matrices
        matrix_F = Matrix(F)
        matrix_g = Matrix(g)
        matrix_F.scale(0.8)
        matrix_g.scale(0.8)
        matrix_F.shift(2*UP)
        matrix_g.next_to(matrix_F, 8*DOWN)
        label_F = Text("State  matrix  F:",font_size=22).next_to(matrix_F, UP)
        label_g = Text("Input  to  state  matrix  g:",font_size=22).next_to(matrix_g, UP)
        self.play(Write(label_F), Write(matrix_F), Write(label_g), Write(matrix_g))
        self.wait(4)
        self.play(FadeOut(matrix_F), FadeOut(matrix_g), FadeOut(label_F), FadeOut(label_g))
        self.wait(1)

        # Reachability matrix R
        reachability_matrix = [
            ["g", "Fg"]]
        matrix_R = Matrix(reachability_matrix)
        matrix_R.scale(0.8)
        matrix_R.move_to(ORIGIN)
        text_R = Text("Reachability  matrix:",font_size=22).next_to(matrix_R, 1.5*UP)
        self.play(Write(text_R), Write(matrix_R))
        self.wait(1)
        #Calculated reachability matrix
        new_reachability_matrix = [
            [1,1],
            [0,0]
        ]
        new_matrix_R = Matrix(new_reachability_matrix)
        new_matrix_R.scale(0.8)
        new_matrix_R.move_to(ORIGIN)

        #Transforming the formula to actual numbers
        self.play(Transform(matrix_R, new_matrix_R))
        self.wait(1)

        #Conclusion in red
        conclusion = Text("The  pair  (F, g)  is  not  reachable.",font_size=22, color = RED).next_to(new_matrix_R, DOWN)
        self.play(Write(conclusion))
        self.wait(2)
        self.play(FadeOut(new_matrix_R),FadeOut(matrix_R), FadeOut(text_R), FadeOut(conclusion))
        self.wait(1)

