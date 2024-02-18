from manim import *

class CameraOrientationChange(ThreeDScene): 
    def construct(self):
        cube = Cube(color = DARK_GRAY)
        axes = ThreeDAxes()
        self.add(axes)
        self.play(Create(cube))
        self.wait(1)

        # Change camera orientation
        self.move_camera(
            phi=60 * DEGREES,  # Tilt the camera 
            theta=60 * DEGREES,  # Rotate the camera
            run_time=2
        )
        self.play(cube.animate.set_color(BLUE_C))
        self.wait(1)
        
        # Resetting camera to another position
        self.move_camera(
            phi=-45 * DEGREES, 
            theta=-45 * DEGREES,  
            run_time=2
        )
        self.wait(1)

        self.play(Uncreate(cube))
        self.wait(5)
