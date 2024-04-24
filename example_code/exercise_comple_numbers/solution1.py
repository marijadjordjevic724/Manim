from manim import *

class Solution1(Scene):
    def construct(self):

        #---------------------------------------------------------------------------------
        # PART TWO

        # The product, formulas, etc
        zk =MathTex("z^k", color=WHITE).move_to(ORIGIN)
        all_elements = MathTex("z^k= z\\cdot z \\cdot...\\cdot z", color=WHITE).next_to(ORIGIN)
        k_elements = Tex("k elements", color=BLUE, font_size = 40).next_to(all_elements[0][3::],DOWN)
        product = MathTex("z^k= \\prod_{i=1}^{k}z", color=WHITE).next_to(ORIGIN)
        product[0][3:-1].set_color(BLUE)
        sum_z2 = MathTex("z^k= \\prod_{i=1}^{k}|z|\\cdot e^{j\\arg(z)}", color=WHITE).next_to(ORIGIN)
        sum_z2[0][3:8].set_color(BLUE)
        sum_z_label = MathTex("\\text{Equivalently, }",font_size = 36).move_to(ORIGIN+1.5*DOWN)
        sum_z = MathTex("z^k = |z|^k\\cdot  e^{jk\\cdot \\arg(z)}", color=WHITE).next_to(sum_z_label, 1.5*DOWN)
        sum_z[0][6].set_color(BLUE)
        sum_z[0][10].set_color(BLUE)
        formulas = VGroup(zk, all_elements, k_elements,product, sum_z2).move_to(ORIGIN)
        
        #Text
        text3 = MathTex("\\text{The simplest method of calculating the product of complex}", font_size = 40)
        text4 = MathTex("\\text{numbers is to express them in their exponential form.}", font_size = 40).next_to(text3, DOWN)
        text4[0][29:44].set_color(BLUE)
        text_34 = VGroup(text3, text4).move_to(ORIGIN+2*UP).scale(0.9)

        #Modules and phases
        text_module = MathTex("\\text{The module of }","{z}^{k}", "\\text{ is the product of all modules:}", font_size = 40).move_to(ORIGIN+2.5*UP)
        text_phase = MathTex("\\text{The phase of }", "{z}^{k}","\\text{ is the sum of all phases:}", font_size = 40).move_to(ORIGIN-0.5*UP)
        moduo_zk = MathTex("|z^k| = |z|^k", color=WHITE).next_to(text_module, 3*DOWN)
        phase_zk = MathTex("\\arg(z^k) = k\\cdot \\arg(z)").next_to(text_phase,3*DOWN)
        
        #Animations
        self.play(FadeIn(all_elements[0][0:2], scale = 1.5))
        self.play(FadeIn(all_elements[0][2]))
        self.play(FadeIn(all_elements[0][3::]))
        self.play(FadeIn(k_elements))
        self.wait(2)
        self.play(FadeOut(all_elements[0][3::]),
                  ReplacementTransform(k_elements,product[0][3::]))
        self.wait(3)
        self.play(Write(text_34, scale=1.3))
        self.wait(2)
        self.play(FadeOut(product[0][3::]),
                  FadeIn(sum_z2[0][3::]))
        self.wait(3)
        self.play(FadeIn(sum_z_label, sum_z))
        self.wait(5)
        self.play(FadeOut(text_34, sum_z2[0][3::],sum_z, sum_z_label, all_elements[0][0:3]))

        #Animation: module of the product -------------------------------------------------------
        
        formulas.move_to(ORIGIN+1.5*UP)
        self.play(Write(text_module))
        product[0][3:-1].set_color(BLUE)
        self.wait(2)
        self.play(FadeIn(moduo_zk[0][0:4]))
        self.wait(0.5)
        self.play(FadeIn(moduo_zk[0][4]))
        self.play(FadeIn(moduo_zk[0][5::]))
        self.wait(2)

        #Animation: phase of the product 
        self.play(Write(text_phase))
        self.play(FadeIn(phase_zk[0][0:7]))
        self.wait(0.5)
        self.play(FadeIn(phase_zk[0][7]))
        self.play(FadeIn(phase_zk[0][8::]))
        self.wait(5)
        self.play(FadeOut(text_module, text_phase), moduo_zk.animate.move_to(2*DOWN + 5*RIGHT).scale(0.7), phase_zk.animate.move_to(3*DOWN + 5*RIGHT).scale(0.7))
        # GRAPH PRODUCT OF TWO NUMBERS-----------------------------------------------------------------
        z = complex(0.5, 0.5)
        
        # Define coordinates
        graph = Axes(
            x_range=(-2.5, 2.5),
            y_range=(-1, 1.2),
            color = DARK_GRAY,
            ).add_coordinates().move_to(ORIGIN)
        graph.set(x_length=5)
        graph.set(y_length=10)
        graph.set()
        # Label the imaginary and real axes
        x_label = MathTex("\\text{Re(z)}", font_size=30).next_to(graph.x_axis.get_end(), RIGHT)
        y_label = MathTex("\\text{Im(z)}", font_size=30).next_to(graph.y_axis.get_end(), UP)

        #Dots of interest
        z_dot = Dot(graph.coords_to_point(0.5, 0.5), color=WHITE)
        lines = graph.get_lines_to_point(graph.c2p(z.real, z.imag),color = DARK_GRAY)
        z_label = MathTex("\\text{z = 0.5 + 0.5j}",font_size=40).next_to(z_dot,UP+RIGHT)

        # Create a VGroup containing the graph and dots
        #graph1 = VGroup(graph, x_label, y_label, z_dot,z_label, graph,c_dot,c_label, b_dot, b_label, a_dot, a_label, lines).move_to(ORIGIN + DOWN)
        graph1 = VGroup(graph, x_label, y_label, z_dot,z_label, graph, lines).move_to(ORIGIN)
        
        # Add graph and dots to the scene
        self.play(FadeIn(graph, x_label, y_label))
        self.wait(2)
        self.play(FadeIn(lines),
                  FadeIn(z_dot, scale = 10),
                  FadeIn(z_label))
        self.wait(2)

        z_label_exponentional = MathTex("\\text{z = 0.7e}^{j\pi/4}",font_size=32).next_to(z_dot,UP+RIGHT)
        self.play(ReplacementTransform(z_label,z_label_exponentional))
        self.wait(2)

        # ANIMATION: ARGUMENT
        l1 = Line(graph.coords_to_point(0,0),graph.coords_to_point(0.5,0.5)).set_color(BLUE).set_opacity(1)
        z_label_exponentional[0][2:5].set_color_by_gradient(BLUE)
        self.play(Write(l1), FadeIn(z_label_exponentional[0][2:5], scope = 5))
        self.wait(2)
        
        # ANIMATION: PHASE
        sector = Sector(arc_center=graph.coords_to_point(0,0), start_angle = 0, angle=PI/4+0.045, radius= 0.5, color=GREEN).set_opacity(0.5)
        z_label_exponentional[0][7:10].set_color_by_gradient(GREEN)
        self.play(Write(sector), FadeIn(z_label_exponentional[0][7:10], scope = 5))
        self.wait(2)

        # Squared
        z_2 = z*z
        z_dot2 = Dot(graph.coords_to_point(z_2.real, z_2.imag), color=WHITE)
        z_label_exp2 = MathTex("\\text{z}^2{ = 0.5e}^{j\pi/2}",font_size=32).next_to(z_dot2,UP+LEFT)
        
        self.play(FadeIn(z_dot2, scale = 10),
                  Write(z_label_exp2))
        self.wait(2)

        # ANIMATION: ARGUMENT
        l3 = Line(graph.coords_to_point(0,0),graph.coords_to_point(z_2.real, z_2.imag)).set_color(BLUE).set_opacity(1)
        z_label_exp2[0][3:6].set_color_by_gradient(BLUE)
        self.play(Write(l3), FadeIn(z_label_exp2[0][3:6], scope = 5))
        self.wait(2)
        
        # ANIMATION: PHASE
        sector2 = Sector(arc_center=graph.coords_to_point(0,0), start_angle=0, angle=PI/2, radius=0.3, color=GREEN).set_opacity(0.7)
        z_label_exp2[0][8:11].set_color_by_gradient(GREEN)
        self.play(Write(sector2), FadeIn(z_label_exp2[0][8:11], scope = 5))
        self.wait(2)

        self.play(*[FadeOut(mob)for mob in self.mobjects])
        
        #The solution
        text8 = MathTex(
                    "\\text{In this example moduo of z is}",
                    font_size=40
                ).move_to(ORIGIN+2.5*UP)
        
        z = MathTex("|z| = |\\frac{\\sqrt{2}}{2}| < 1", color=WHITE,font_size=40).next_to(text8, DOWN)
        text9 = MathTex("\\text{which is smaller than 1.}",font_size=40).move_to(ORIGIN+0.5*UP)
        text10 = MathTex(
            "\\text{Because of that, }", "{|z|}^{k}","\\text{ will converge to 0.}",
            font_size=40
        ).move_to(ORIGIN+0.5*DOWN)
        z_k = MathTex("\\lim_{k \\rightarrow +\\infty}|z|^k = \\lim_{k \\rightarrow +\\infty}|\\frac{\\sqrt{2}}{2}|^k = 0", color=WHITE,font_size=40).next_to(text10, DOWN)
        
        #Animation: the solution
        self.play(FadeIn(text8))
        self.play(FadeIn(z[0][0:-2]))   
        self.wait(2)
        self.play(FadeIn(text9))
        self.wait(1)
        self.play(FadeIn(z[0][-2::]))
        self.wait(2)
        self.play(FadeIn(text10))
        self.wait(1)
        self.play(FadeIn(z_k, scale = 1.5))
        self.wait(5)
        self.play(FadeOut(text10, text8, text9, z), z_k.animate.move_to(3*DOWN + 4*RIGHT).scale(0.8))

        # GRAPH ANIMATION------------------------------------------------------
        # Define axes
        z = complex(0.5, 0.5)
        
        graph.move_to(ORIGIN)
        graph.set(x_length=5)
        graph.set(y_length=10)
        graph.set()
        
        # Label the imaginary and real axes
        x_label = MathTex("\\text{Re(z)}", font_size=30).next_to(graph.x_axis.get_end(), RIGHT)
        y_label = MathTex("\\text{Im(z)}", font_size=30).next_to(graph.y_axis.get_end(), UP)

        #Dots of interest
        c_dot = Dot(graph.coords_to_point(0, 0), color=GREEN)
        b_dot = Dot(graph.coords_to_point(0, 1), color=RED)
        a_dot = Dot(graph.coords_to_point(1, 0), color=YELLOW)
        z_dot = Dot(graph.coords_to_point(0.5, 0.5), color=WHITE)
        lines = graph.get_lines_to_point(graph.c2p(0.5,0.5),color = DARK_GRAY)
        z_label = MathTex("\\text{z}",font_size=40).next_to(z_dot,UP+RIGHT)

        # Create a VGroup containing the graph and dots
        #graph1 = VGroup(graph, x_label, y_label, z_dot,z_label, graph,c_dot,c_label, b_dot, b_label, a_dot, a_label, lines).move_to(ORIGIN + DOWN)
        graph1 = VGroup(graph, x_label, y_label, z_dot,z_label, graph,c_dot, b_dot, a_dot, lines).move_to(ORIGIN)
        
        self.play(FadeIn(graph, x_label, y_label))
        self.wait(2)
        self.play(FadeIn(lines),
                  FadeIn(z_dot, scale = 10),
                  FadeIn(z_label))
        self.wait(2)

        # Calculating and showing powers of z
        # Initializing variables
        new_z = z
        t = 1
        radiuss = DEFAULT_DOT_RADIUS
        
        for i in range(2, 15):
            old_z = new_z
            new_z = new_z*z
            radiuss = radiuss*0.9
            t = t*0.5

            coord_old = graph.coords_to_point(old_z.real,old_z.imag)
            coord_new = graph.coords_to_point(new_z.real,new_z.imag)
            line=Line(coord_old,coord_new).set_color(BLUE).set_opacity(0.8)
            new_z_dot= Dot(coord_new, color = BLUE, radius=radiuss)

            self.play(FadeIn(new_z_dot), Write(line))

            if i < 4:
                label = MathTex("\\text{z}^{" + str(i) + "}",font_size=40, color = BLUE).next_to(new_z_dot,LEFT+0.3*UP)
                self.play(FadeIn(label))

            self.wait(t)
        
        # Show final dot
        final_dot = Dot(graph.coords_to_point(0,0), color = WHITE)
        label = MathTex("\\text{z}^k",font_size=40).next_to(final_dot, RIGHT+DOWN)
        self.play(FadeIn(final_dot, label))
        self.wait(2)

        # Fade out everything
        self.play(*[FadeOut(mob)for mob in self.mobjects])
