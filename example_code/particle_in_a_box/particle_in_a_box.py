from manim import *

class ParticleInABox(Scene):
    def construct(self):
        # Creating the box and the particle
        box = Rectangle(height=2, width=9, color=BLUE, stroke_width=2)
        box.shift(UP)
        particle = Dot(color=YELLOW)
        particle.move_to(box.get_bottom()+UP)

        # Animation: Move the particle in the box with visual effects
        self.play(Create(box))
        self.wait(1)
        self.play(GrowFromCenter(particle))
        self.wait(1)
        self.play(
            particle.animate.shift(3 * RIGHT).set_color(RED),  # Move particle and change color
            box.animate.set_color(RED),  # Change color of the box
            rate_func=there_and_back,
            run_time=2
        )
        self.play(
            particle.animate.shift(4 * LEFT).set_color(GREEN),  # Move particle and change color
            box.animate.set_color(GREEN),  # Change color of the box
            rate_func=there_and_back,
            run_time=2
        )
        self.play(
            particle.animate.shift(2 * RIGHT).set_color(BLUE),  # Move particle and change color
            box.animate.set_color(BLUE),  # Change color of the box
            rate_func=there_and_back,
            run_time=1
        )
        self.wait(1)
