from manim import *

class SquareWave(Scene):
    def construct(self):
        # Creating axes
        axes = Axes(
            x_range=[-3*PI, 3*PI, PI/2],
            y_range=[-1.5, 1.5, 1],
            x_length=8,
            y_length=4,
            axis_config={"color": WHITE},
            tips=False
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        title = Text("Formation of a Square Wave", font_size=24).to_edge(UP)
        self.play(Write(title))
        self.play(Create(axes), Write(axes_labels), run_time=1)

        # Plot the square wave 
        square_wave_graph = axes.plot(lambda x: np.sign(np.sin(x)), color=GREEN)
        self.wait(1)
        self.play(Create(square_wave_graph), run_time=6)
        self.wait(2)
