from manim import *

class Solution1(Scene):
    def construct(self):

        #---------------------------------------------------------------------------------
        # PART TWO

        # The product, formulas, etc
        zk =MathTex("z^k", color=WHITE).move_to(ORIGIN)
        all_elements = MathTex("z^k= z*z*...*z", color=WHITE).next_to(ORIGIN)
        k_elements = Tex("k elements", color=BLUE, font_size = 40).next_to(all_elements[0][3::],DOWN)
        product = MathTex("z^k= \\prod_{i=1}^{k}z", color=WHITE).next_to(ORIGIN)
        product[0][3:-1].set_color(BLUE)
        sum_z2 = MathTex("z^k= \\prod_{i=1}^{k}|z|*e^{j\\arg(z)}", color=WHITE).next_to(ORIGIN)
        sum_z2[0][3:8].set_color(BLUE)
        formulas = VGroup(zk, all_elements, k_elements,product, sum_z2).move_to(ORIGIN)
        
        #Text
        text3 = Tex("The simplest method of calculating the product of two complex", font_size = 40)
        text4 = Tex("numbers is to express them in their exponential form.", font_size = 40).next_to(text3, DOWN)
        text4[0][29:44].set_color(BLUE)
        text_34 = VGroup(text3, text4).move_to(ORIGIN+2*UP)

        #Modules and phases
        text_module = Tex("The module of the product is the product of all modules:", font_size = 40).move_to(ORIGIN+2.5*UP)
        text_phase = Tex("The phase of the product is the sum of all phases:", font_size = 40).move_to(ORIGIN-0.5*UP)
        text_module[0][26:33].set_color(BLUE)
        text_phase[0][25:28].set_color(BLUE)
        moduo_zk = MathTex("|z^k| = |z|^k", color=WHITE).next_to(text_module, 3*DOWN)
        phase_zk = MathTex("\\arg(z^k) = k*\\arg(z^k)").next_to(text_phase,3*DOWN)
        
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
        self.play(FadeOut(text_34,sum_z2[0][3::], all_elements[0][0:3]))

        # Animation: final formula
        text7 = MathTex(
                    "\\text{Therefore, }",
                    "z^k",
                    "\\text{ can be presented with a formula }",
                    color=WHITE,
                    font_size=40,
                ).move_to(ORIGIN+2*UP)
        z = MathTex("z^k = |z|^k * e^{jk*\\arg(z)}", color=WHITE).move_to(ORIGIN)
        self.play(Write(text7, scale = 1.5))
        self.play(FadeIn(z, scale = 1.5))   
        self.wait(3)
        self.play(FadeOut(text7,z))

        #Animation: module of the product 
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
        self.play(FadeOut(text_module, text_phase, moduo_zk, phase_zk))
        

        '''
        # TEXT: Product of two complex numbers
        text3 = Tex("The simplest method of calculating the product of two complex", font_size = 40)
        text4 = Tex("numbers is to firstly express them in their exponential form.", font_size = 40).next_to(text3, DOWN)
        text4[0][35:50].set_color(BLUE)
        text_34 = VGroup(text3, text4)

        # Animate text and move up
        self.play(FadeIn(text_34, scale=1.3))
        self.wait(5)
        self.play(text_34.animate.move_to(ORIGIN+2.5*UP).scale(0.9))

        # Example complex numbers
        z1 = MathTex("z_1 = |z_1|*e^{j\\arg(z_1)}", color=WHITE)
        z2 = MathTex("z_2 = |z_2|*e^{j\\arg(z_2)}", color=WHITE).next_to(z1, DOWN)

        # Define the product of the complex numbers
        z_product_part1 = MathTex("z_1*z_2 =", color=WHITE)
        z_product_part2 = MathTex("|z_1|*|z_2|", color=WHITE).next_to(z_product_part1, RIGHT)
        z_product_part3 = MathTex("* e^{j(\\arg(z_1) + \\arg(z_2))}", color=WHITE).next_to(z_product_part2, RIGHT)

        product = VGroup(z_product_part1,z_product_part2,z_product_part3).next_to(z2, DOWN)
        complex = VGroup(z1, z2,z_product_part1, z_product_part2,z_product_part3).move_to(ORIGIN)

        # Animate the product
        self.play(FadeIn(z1, z2, scale = 1.5))
        self.wait(4)
        self.play(FadeIn(z_product_part1, scale = 1.5))

        # Modul of the product
        text5 = Tex("Module of the product is the product of the two original moduli.", font_size = 40).move_to(ORIGIN+2.5*UP)
        self.play(FadeOut(text_34),
                  FadeIn(text5, scale = 1.5))
        self.play(FadeIn(z_product_part2, scale = 1.5))
        self.wait(5)

        # Argment of the product
        text6 = Tex("Phase of the product is the sum of the two original phases.", font_size = 40).move_to(ORIGIN+2.5*UP)
        self.play(FadeOut(text5),
                  FadeIn(text6, scale = 1.5))
        self.play(FadeIn(z_product_part3, scale = 1.5))
        self.wait(5)
        self.play(FadeOut(text6, complex))
        '''

        #The solution
        text8 = MathTex(
                    "\\text{In this example moduo of z is}",
                    font_size=40
                ).move_to(ORIGIN+2.5*UP)
        
        z = MathTex("|z| = |\\frac{\\sqrt{2}}{2}| < 1", color=WHITE,font_size=40).next_to(text8, DOWN)
        text9 = Tex("which is smaller than 1.",font_size=40).move_to(ORIGIN+0.5*UP)
        text10 = Tex(
            "Therefore, the sequence $|z|^k$ converges to $0$.",
            font_size=40
        ).move_to(ORIGIN+UP)
        z_k = MathTex("\\lim_{k \\rightarrow +\\infty}|z|^k = \\lim_{k \\rightarrow +\\infty}|\\frac{\\sqrt{2}}{2}|^k = 0", color=WHITE,font_size=40).next_to(text10, DOWN)
        
        #Animation: the solution
        self.play(Write(text8))
        self.play(FadeIn(z[0][0:-2]))   
        self.wait(1)
        self.play(Write(text9),
                  FadeIn(z[0][-3::]))
        self.wait(1)
        self.play(FadeOut(text8, text9, z),
                  Write(text10))
        self.play(FadeIn(z_k, scale = 1.5))
        self.wait(5)














