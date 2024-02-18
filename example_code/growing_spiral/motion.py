from manim import *

class GrowingSpiral(Scene):
    def construct(self):

        # Points for the spiral
        points = []
        num_turns = 5
        num_points_per_turn = 100
        max_radius = 3
        color = BLUE
        for i in range(num_turns * num_points_per_turn):
            theta = i * TAU / num_points_per_turn
            radius = max_radius * i / (num_turns * num_points_per_turn)
            x = radius * np.cos(theta)
            y = radius * np.sin(theta)
            point = [x, y, 0]
            points.append(point)

        # Creating spiral curve
        spiral_curve = VMobject()
        spiral_curve.set_points_smoothly(points)
        spiral_curve.set_color(color)

        # Animating
        self.play(Create(spiral_curve), run_time=3)
        self.wait()




