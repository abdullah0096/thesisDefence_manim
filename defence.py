import math

from manim import *
from manim_slides import Slide

DOTCOLOR = WHITE


def fun(x):
    return math.sqrt(x*x*x - 3*x + 3)


def fun2(x):
    return (x*x*x - 3*x + 3)


def getEC_points():
    points = []
    cnt = 0
    for i in range(9, -3, -1):
        cnt += 1
        points.append([i, fun(i), 0])

    for i in range(cnt-1, -1, -1):
        points.append([points[i][0], -points[i][1], 0])

    return points


def getHomogenousCurvePoints():
    points = []
    points.append([2, 15, 0])
    points.append([3.5, 11, 0])

    points.append([6, 7, 0])

    points.append([0.5, 0, 0])

    points.append([6, -7, 0])

    points.append([3.5, -11, 0])
    points.append([2, -15, 0])

    return points


def plotDotTL(s):
    dot = Dot(color=DOTCOLOR).to_corner(UL)

    s.play(FadeIn(dot), run_time=0.1)
    s.play(FadeOut(dot), run_time=0.1)


def nextScenePause(self):
    self.next_slide()
    self.start_loop()
    plotDotTL(self)
    self.end_loop()


class def_title0(Slide):
    def construct(self):

        txt_1 = Tex(
            r'\textbf{A new attack on the \\ Elliptic Curve Discrete Logarithm Problem}', font_size=48)
        author = Tex(r'\textbf{Mr. Abdullah Ansari}', color=YELLOW_B, font_size=42).next_to(
            txt_1, DOWN, buff=0.8)

        self.start_loop()
        self.play(FadeIn(txt_1), run_time=1)
        self.play(FadeIn(author), run_time=1)

        self.wait(2)
        plotDotTL(self)
        self.wait(1)

        self.play(txt_1.animate.shift(UP*2.7), author.animate.shift(UP*2.2))

        plotDotTL(self)

        topic = Tex(r'\textbf{Doctoral Thesis Defence}', color=BLUE_D,
                    font_size=36).next_to(author, DOWN, buff=0.6)
        self.play(AddTextWordByWord(topic), run_time=1)

        plotDotTL(self)

        issc = Tex(
            r'\textbf{Formerly - Interdisciplinary School of Scientific Computing}', font_size=21).to_edge(DOWN)

        date = Tex(r'\textbf{$29^{th}$ November 2023 \\ Dept. of Scientific Computing, Modeling and Simulation}',
                   font_size=20).next_to(issc, UP, buff=0.2)

        guide = Tex(
            r'\textbf{ Guide \\ Dr. Smita Bedekar \\ Associate Professor ISSC (SCMS) - SPPU}', font_size=24).next_to(date, UP, buff=0.7).shift(LEFT*4)
        coGuide = Tex(
            r'\textbf{ Co-Guide \\ Dr. Ayan Mahalanobis \\ Assistant Professor - IISER-Pune}', font_size=24).next_to(date, UP, buff=0.7).shift(RIGHT*3.5)

        self.play(FadeIn(guide), FadeIn(coGuide))
        self.wait(2)
        self.end_loop()
        self.play(FadeIn(date), AddTextWordByWord(issc), run_time=0.1)

        nextScenePause(self)


class def_scene1(Slide):
    def construct(self):

        txt1 = Tex(
            r"\textbf{$\sim$ 5,000,000,000} \\ \textbf{Internet user}", color=YELLOW)
        txt2 = Tex(
            r"\textbf{$\sim$ 14,000,000,000} \\ \textbf{Connected devices}", color=YELLOW)

        self.play(FadeIn(txt1))
        self.next_slide()

        self.play(FadeOut(txt1))
        self.play(FadeIn(txt2))
        self.next_slide()
        self.play(FadeOut(txt2))

        txt_ecdlp = Tex(
            r'\textbf{Elliptic Curve Discrete Logarithm Problem}').scale(1.2)
        self.play(FadeIn(txt_ecdlp))
        self.next_slide()
        self.play(txt_ecdlp.animate.shift(DOWN*1.8))

        img_whatsApp = ImageMobject(
            "img/WhatsApp.png").scale(0.7).shift(UP)
        txt_app1 = Tex(r'WhatsAPP \\ End to End \\ encryption',
                       color=GREEN_D).next_to(img_whatsApp, DOWN)

        self.play(FadeIn(img_whatsApp), FadeIn(txt_app1))
        self.next_slide()

        self.play(txt_app1.animate.shift(LEFT*5),
                  img_whatsApp.animate.shift(LEFT*5))

        img_UPI = ImageMobject(
            "img/UPI-Logo-vector_2.png").scale(0.7).shift(UP)
        txt_app2 = Tex(r'UPI \\ Google Pay \\ PhonePe',
                       color=BLUE_B).next_to(txt_app1, RIGHT, buff=1).next_to(img_UPI, DOWN)
        self.play(FadeIn(txt_app2), FadeIn(img_UPI))

        self.next_slide()
        self.play(txt_app2.animate.shift(LEFT*1.7),
                  img_UPI.animate.shift(LEFT*1.7))

        img_bitEth = ImageMobject(
            "img/bitEth.png").scale(0.2).next_to(img_UPI, RIGHT, buff=0.8)
        txt_app3 = Tex(r'Crypto \\ Curriencies',
                       color=YELLOW_A).next_to(img_bitEth, DOWN)
        self.play(FadeIn(txt_app3), FadeIn(img_bitEth))

        self.next_slide()

        txt_TLS = Tex(r"SSL/TLS").scale(1.3).next_to(img_bitEth,
                                                     RIGHT, buff=1)
        txt_Https = Tex(r'HTTPS \\ Email \\ etc...',
                        color=BLUE).next_to(txt_TLS, DOWN)
        self.play(FadeIn(txt_Https), FadeIn(txt_TLS))
        self.next_slide()

        grp = Group()
        grp.add(img_whatsApp, txt_app1, img_UPI, txt_app2,
                img_bitEth, txt_app3, txt_TLS, txt_Https)
        # self.play(grp.animate.shift(UP).shift(LEFT*0.4).scale(0.9))

        self.play(FadeOut(grp))
        self.play(txt_ecdlp.animate.scale(0.6).to_edge(UL), run_time=0.7)

        oneWayFun = Tex(r'\textbf{One-way Function}',
                        font_size=40).shift(UP*2.2)
        self.play(FadeIn(oneWayFun))
        self.next_slide()

        # self.play(oneWayFun.animate.set_color(DARK_GRAY), run_time=0.1)

        ellipse1 = Ellipse(width=3, height=5, stroke_width=2, color=BLUE).scale(
            0.5).next_to(oneWayFun, DOWN, buff=1).shift(LEFT*2)
        ellipse2 = Ellipse(width=3, height=5, stroke_width=2, color=RED).scale(
            0.5).next_to(ellipse1, RIGHT, buff=3)

        center_coords = ellipse1.get_center()
        dot = Dot(color=WHITE).move_to(center_coords)
        x = Tex(r'$x$').next_to(dot, LEFT)

        self.play(Create(ellipse1), Create(ellipse2), Create(dot), FadeIn(x))
        plotDotTL(self)
        self.next_slide()

        dot2 = Dot(color=WHITE).move_to(ellipse2.get_center())
        fx = Tex(r'$f(x)$').next_to(dot2, DOWN).scale(0.7)
        curved_arrow = CurvedArrow(
            start_point=ellipse1.get_center(), end_point=ellipse2.get_center(), color=WHITE, stroke_width=2)
        self.play(Create(dot2), FadeIn(fx), Create(curved_arrow))

        easy = Tex(r'Easy', font_size=28).next_to(
            curved_arrow, DOWN)
        easy2 = Tex(r'Easy : Given $x$ easy to compute $f(x)$',
                    font_size=24).next_to(ellipse1, DOWN, buff=0.8).shift(RIGHT*1.5)
        self.play(FadeIn(easy), FadeIn(easy2))
        plotDotTL(self)

        self.next_slide()
        # Create a curved arrow between the two points
        curved_arrow2 = CurvedArrow(
            start_point=ellipse2.get_center(), end_point=ellipse1.get_center(), color=YELLOW, stroke_width=2)
        curved_arrow2.tip_length = 4
        self.play(Create(curved_arrow2))
        hard = Tex(r'Hard', font_size=28, color=RED).next_to(curved_arrow2, UP)
        hard2 = Tex(r'Hard : Practically impossible to compute $f^{-1}(x)$',
                    font_size=24).next_to(easy2, DOWN, aligned_edge=LEFT, buff=0.1)

        self.play(FadeIn(hard), FadeIn(hard2))

        # self.next_slide()

        # self.play(oneWayFun[0].animate.set_color(WHITE))
        # self.play(Indicate(oneWayFun[0]))
        plotDotTL(self)
        # self.next_slide()

        # arrow = Arrow(start=ellipse2.get_center(),
        #               end=ellipse1.get_center(), color=BLUE, stroke_width=2)
        # trapdoor = Tex(r'Trapdoor', font_size=28,
        #                color=BLUE).next_to(arrow, DOWN, buff=-0.4)
        # trapdoor2 = Tex(r'Trapdoor : Auxiliary information that makes $f^{-1}(x)$ easy', font_size=24,
        #                 color=BLUE).next_to(hard2, DOWN, aligned_edge=LEFT, buff=0.1)
        # self.play(FadeIn(arrow), FadeIn(trapdoor), FadeIn(trapdoor2))

        self.next_slide()

        grp = VGroup()
        grp.add(ellipse1, ellipse2, dot, dot2, x, fx, curved_arrow,
                curved_arrow2, easy, hard, easy2, hard2)

        self.play(grp.animate.shift(LEFT*3.1))

        p = Tex(r'\textbf{$ p = 9343$}', font_size=30).next_to(
            oneWayFun, DOWN, buff=1, aligned_edge=RIGHT)
        q = Tex(r'\textbf{ $q = 313$}', font_size=30).next_to(
            p, DOWN, aligned_edge=LEFT)
        n = Tex(r'\textbf{$ n = p \times q = 2924359$}', font_size=30).next_to(
            q, DOWN, aligned_edge=LEFT)

        self.play(FadeIn(p), FadeIn(q))
        self.next_slide()

        self.play(FadeIn(n))
        n_easy = Tex(r'\textbf{Easy}', font_size=25,
                     color=GREEN).next_to(n, RIGHT)
        self.play(ScaleInPlace(n_easy, 1.4), run_time=3)
        self.wait(0.5)
        self.play(ShrinkToCenter(n_easy), run_time=2)
        self.next_slide()

        inv = Tex(r'\textbf{Given $n$, Find $p,q$ ?}', font_size=30).next_to(
            n, DOWN, aligned_edge=LEFT)
        self.play(FadeIn(inv))
        inv_hard = Tex(r'\textbf{Hard}', font_size=25,
                       color=RED).next_to(inv, RIGHT)
        self.play(ScaleInPlace(inv_hard, 1.4), run_time=3)
        self.wait(0.5)
        self.play(ShrinkToCenter(inv_hard), run_time=2)
        self.next_slide()

        # n_trap = Tex(r'\textbf{Trapdoor : If p = 9343 is given \\ then factorization is Easy}',
        #              font_size=28).next_to(inv, DOWN, aligned_edge=LEFT)
        # self.play(FadeIn(n_trap))
        # plotDotTL(self)
        # self.next_slide()

        ifp = Tex(r'\textbf{Integer Factorization Problem}', font_size=32).next_to(
            inv, DOWN, aligned_edge=LEFT)
        self.play(FadeIn(ifp))

        self.next_slide()
        self.play(FadeOut(grp), FadeOut(p), FadeOut(q), FadeOut(n),
                  FadeOut(inv), FadeOut(inv_hard))
        # self.next_slide()

        ifp2 = Tex(r'\textbf{Integer Factorization \\ problem}',
                   font_size=32).to_edge(LEFT).shift(RIGHT-0.4)

        trf1 = Transform(ifp, ifp2)
        self.play(trf1)
        self.next_slide()

        dlp = Tex(r'\textbf{Discrete logarithm \\ problem}',
                  font_size=32).next_to(ifp2, RIGHT, aligned_edge=UP, buff=1)
        ecdlp = Tex(r'\textbf{Elliptic Curve Discrete \\ Logarithm Problem}',
                    font_size=32).next_to(dlp, RIGHT, aligned_edge=UP, buff=1)

        self.play(FadeIn(dlp), FadeIn(ecdlp))

        self.next_slide()

        self.play(FadeOut(ifp2), FadeOut(ifp),
                  FadeOut(dlp), FadeOut(oneWayFun))

        self.play(ecdlp.animate.shift(LEFT*8))

        txt_3 = Tex(r'\textbf{Las Vegas \\ Algorithm}', color=BLUE,
                    font_size=45).next_to(ecdlp, RIGHT, buff=2)
        rect = Rectangle(width=txt_3.get_width() + 1,
                         height=txt_3.get_height() + 1, fill_color=BLUE)
        rect.surround(txt_3)

        self.play(FadeIn(txt_3), FadeIn(rect))

        self.next_slide()
        self.play(FadeOut(ecdlp, shift=RIGHT*4), run_time=2)

        grp = VGroup(txt_3, rect)
        self.play(grp.animate.shift(LEFT*3))

        m0 = Matrix([["a_{1,1}", "a_{1,2}", "a_{1,3}", "\dots", "a_{1,\ell}"], ["a_{2,1}", "a_{2,2}", "a_{2,3}", "\dots", "a_{2,\ell}"], ["\\vdots", "\\vdots", "\\vdots", "\ddots", "\\vdots"], ["a_{\ell,1}", "a_{\ell,2}", "a_{\ell,3}", "\dots", "a_{\ell,\ell}"]], left_bracket="(",
                    right_bracket=")").scale(0.5).next_to(grp, RIGHT)
        self.play(FadeIn(m0, shift=RIGHT), run_time=2)

        self.play(FadeOut(grp))
        self.play(m0.animate.move_to([0, 0, 0]).scale(1.4))
        # line = Line([0.6, 1, 0], [0.6, -1.1, 0])
        # line.set_stroke(width=2)
        # self.play(FadeIn(line))

        grp2 = VGroup(m0)
        self.play(grp2.animate.shift(UP*1.4))
        self.next_slide()

        highlight2 = Rectangle(
            width=1.6,
            height=1,
            color=YELLOW
        )
        highlight2.set_stroke(width=2)

        highlight2.move_to([m0.get_x()-1.75, m0.get_y()+0.55, 0])
        highlight2.shift(RIGHT*0.4)

        self.start_loop()
        self.play(DrawBorderThenFill(highlight2))

        # self.next_slide()

        self.play(highlight2.animate.shift(RIGHT*0.9), run_time=2)
        # self.next_slide()

        self.play(highlight2.animate.shift(RIGHT*0.9), run_time=2)
        # self.next_slide()

        self.play(highlight2.animate.shift(RIGHT*0.9), run_time=1)

        self.play(highlight2.animate.move_to([m0.get_x()-1.3, m0.get_y(), 0]))
        # self.next_slide()

        self.play(highlight2.animate.shift(RIGHT*0.9), run_time=1)
        # self.next_slide()

        self.play(highlight2.animate.shift(RIGHT*0.9), run_time=1)
        # self.next_slide()

        self.play(highlight2.animate.shift(RIGHT*0.9), run_time=1)
        # self.next_slide()
        self.play(FadeOut(highlight2))

        highlight3 = Rectangle(
            width=2.43,
            height=1.75,
            color=YELLOW
        )
        highlight3.set_stroke(width=2)
        highlight3.move_to([m0.get_x()-0.92, m0.get_y()+0.28, 0])
        self.play(DrawBorderThenFill(highlight3))
        # self.next_slide()

        self.play(highlight3.animate.shift(RIGHT*0.9), run_time=1)
        # self.next_slide()

        self.play(highlight3.animate.shift(RIGHT), run_time=1)
        # self.next_slide()

        self.play(highlight3.animate.move_to(
            [m0.get_x()-0.9, m0.get_y()-0.3, 0]))

        # self.next_slide()

        self.play(highlight3.animate.shift(RIGHT), run_time=1)
        self.wait(0.3)
        self.play(highlight3.animate.shift(RIGHT), run_time=0.5)

        self.end_loop()

        self.play(FadeOut(highlight3))

        txt_9 = Tex(r'\textbf{Zero Minor Problem}', color=YELLOW).scale(
            0.7).next_to(grp2, DOWN, buff=0.7)
        self.play(AddTextWordByWord(txt_9), run_time=1)

        txt_10 = Tex(r'\textbf{Find a square sub-matrix, such that the \\ determinant of this sub-matrix is zero.}',
                     color=BLUE).scale(0.7).next_to(txt_9, DOWN)
        self.play(AddTextWordByWord(txt_10), run_time=2)

        nextScenePause(self)


class def_nutshell2(Slide):
    def construct(self):
        txt_1 = Tex(r'Aim : Experimentally solve the zero minor problem.')
        self.play(FadeIn(txt_1))

        self.next_slide()
        self.play(txt_1.animate.shift(UP*2))
        txt_2 = Tex(r'Design, Implement and Simulate algorithms \\ to solve the zero minor problem.').next_to(
            txt_1, DOWN, buff=1.3)

        words = txt_2.split()  # Split the text into individual words

        # Create a list of TextMobjects for each word
        word_mobjects = []

        for word in words:
            word_mobjects.append(word)

        # Position the words horizontally
        for i in range(1, len(word_mobjects)):
            word_mobjects[i].next_to(word_mobjects[i-1], RIGHT)

        # Add the word mobjects to the scene
        for word in word_mobjects:
            self.play(*[Write(word) for word in word_mobjects], run_time=3)

        # self.play(AddTextLetterByLetter(txt_2), run_time=3)

        self.next_slide()
        txt_codeURL = Tex(
            r'https://bitbucket.org/abdullah0096/lasvegas-ecdlp.git').scale(0.9).next_to(txt_2, DOWN, buff=0.5)

        txt_abtCode = Tex(r' C++, NTL, openMPI \\ Known to work on $\sim$ 1500+ CPU',
                          color=YELLOW).scale(0.9).next_to(txt_codeURL, DOWN, buff=0.5)

        self.play(FadeIn(txt_codeURL), FadeIn(txt_abtCode))

        self.next_slide()
        self.play(FadeOut(txt_2), FadeOut(txt_codeURL), FadeOut(txt_abtCode))

        txt_6 = Tex(r'Do zero minor exist ?', color=BLUE).next_to(
            txt_1, DOWN, buff=1.5).scale(1.1)
        txt_7 = Tex(r'How to find a zero minor ?',
                    color=BLUE).next_to(txt_6, DOWN, buff=0.8).scale(1.2)

        self.play(Write(txt_6), run_time=3)
        self.next_slide()
        self.play(Write(txt_7), run_time=3)

        # txt_3 = Tex(r'Complexity : $\sim O(2\ell^7)$', color=RED_B).next_to(
        #     txt_1, DOWN, buff=1.5).scale(1.5)
        # self.play(Write(txt_3), run_time=3)

        # txt_4 = Tex(r'$\ell$ : Order of the matrix').next_to(
        #     txt_3, DOWN, buff=1.7).scale(0.7)
        # self.play(Write(txt_4))

        # txt_5 = Tex(
        #     r'Based on data available for upto 50-bit binary fields').next_to(txt_4, DOWN).scale(0.5)
        # self.play(Write(txt_5))

        nextScenePause(self)


class def_EC3_1(Slide):
    def construct(self):

        ecdlp = Tex(
            r'\textbf{Elliptic Curve Discrete Logarithm Problem}').scale(0.9)
        self.play(Create(ecdlp))
        plotDotTL(self)
        self.next_slide()

        self.play(FadeOut(ecdlp))

        ec = Tex(r'Elliptic curves ')

        self.play(Create(ec))
        self.next_slide()  # Waits user to press continue to go to the next slide

        self.play(ec.animate.shift(UP*2))
        equation = Tex(r'$\mathcal{E} : y^2 = x^3 + ax + b$').scale(1.4)
        self.play(Write(equation))
        self.next_slide()

        self.play(Unwrite(ec))
        self.play(equation.animate.shift(UP*2))
        EC_coefficients = Tex(r'$a = -3, b = 3$').scale(1.4)
        self.play(Write(EC_coefficients))
        equation2 = Tex(r'$\mathcal{E} : y^2 = x^3 -3x + 3$').scale(1.4)
        self.next_slide()

        self.play(Unwrite(EC_coefficients))
        self.play(TransformMatchingTex(equation, equation2))
        self.next_slide()

        # self.play(equation2.animate.scale(0.5))
        self.play(equation2.animate.to_edge(UR).scale(0.7), run_time=1)
        plane = NumberPlane(x_range=[-12, 12, 1], x_length=12,
                            y_range=[-13, 13, 1], y_length=13,
                            background_line_style={
            "stroke_color": BLUE,
            "stroke_width": 2,
            "stroke_opacity": 0.3
        }
        ).add_coordinates().to_edge(LEFT)

        self.play(DrawBorderThenFill(plane))
        ellipticCurvePoints = getEC_points()

        graph = VMobject(color=RED)
        graph.set_points_smoothly(plane.coords_to_point(
            ellipticCurvePoints))

        self.play(Create(graph), run_time=2.5)
        self.next_slide()

        grp = VGroup()
        grp.add(plane, graph)
        myRect = SurroundingRectangle(grp, color=BLUE)
        grp.add(myRect)
        self.play(grp.animate.scale(0.6).to_edge(LEFT))
        # self.play(equation2.animate.shift(LEFT))
        self.next_slide()

        Text_pointAdd = Text("Point addition", color=BLUE).next_to(
            equation2, DOWN).to_corner(
            RIGHT).scale(0.7).shift(LEFT*1.5)

        P = Dot(color=WHITE)
        P.move_to(graph.point_from_proportion(0.50))
        P_label = Tex("P", font_size=28).next_to(P, DL)

        Q = Dot(color=WHITE)
        Q.move_to(graph.point_from_proportion(0.45))
        Q_label = Text("Q", font_size=18).next_to(Q, LEFT)

        self.play(Create(P), Create(P_label), Create(Q), Create(Q_label))
        self.next_slide()

        self.play(Create(Text_pointAdd))
        self.next_slide()

        points_P_Q = Tex(
            r'$P = (x_p, y_p),    Q = (x_q, y_q$)', color=GREEN).next_to(Text_pointAdd, DOWN).scale(0.7)

        Text_R = Tex(r'$R = P + Q$').next_to(points_P_Q, DOWN).scale(0.7)

        point_AdditionFormula_Slope = Tex(
            r'$ \lambda = \frac{y_q - y_p}{x_q - x_p}  $').next_to(Text_R, DOWN).scale(0.9)

        # grp_rt = VGroup()
        # point_AdditionFormula = Tex(
        #     r'$ R = (\lambda^2 -x_p -x_q, \lambda(x_p - x_r)-y_p)$').next_to(point_AdditionFormula_Slope, DOWN).scale(0.7)

        # grp_rt.add(points_P_Q.shift(RIGHT*0.3), point_AdditionFormula_Slope,
        #            point_AdditionFormula.shift(RIGHT), Text_R)

        # self.play(FadeIn(grp_rt))

        # self.next_slide()

        l = Line(P, Q, color=GREEN, stroke_width=3)
        self.play(Create(l))
        self.next_slide()

        R = Dot(color=WHITE)
        R.move_to(graph.point_from_proportion(0.25))
        R_label = Text("R'", font_size=18).next_to(R, LEFT)

        l2 = Line(Q, R, color=GREEN, stroke_width=3)
        self.play(Create(R), Create(R_label), Create(l2))
        self.next_slide()

        Q2 = Dot(color=WHITE)
        Q2.move_to(graph.point_from_proportion(0.75))

        l3 = Line(R, Q2, color=GREEN, stroke_width=3)

        self.play(Create(Q2), Create(l3))
        R2 = Text(f"({Q.get_center()[0]:.1f}, {Q.get_center()[1]:.1f})", font_size=18).next_to(
            Q2, LEFT)
        R2 = Text("R = P+Q", font_size=18).next_to(
            Q2, RIGHT)
        self.play(Create(R2))
        self.next_slide()

        # self.play(Unwrite(grp_rt))
        # self.play(Unwrite(Text_pointAdd))
        self.play(Unwrite(l3), Unwrite(R2), Unwrite(Q2),
                  Unwrite(R), Unwrite(l2), Unwrite(l), Unwrite(R_label))

        # @TODO :: merge P and Q to a single point using animation
        self.play(Unwrite(P), Unwrite(P_label),
                  Unwrite(Q), Unwrite(Q_label))

        Text_pointDouble = Text("Point doubling", color=BLUE).next_to(
            Text_pointAdd, DOWN).to_corner(
            RIGHT).scale(0.7).shift(LEFT*1.3)

        self.play(Create(Text_pointDouble))
        self.next_slide()

        P = Dot(color=WHITE)
        P.move_to(graph.point_from_proportion(0.47))
        P_label = Text("P", font_size=18).next_to(P, UL)

        self.play(Create(P), Create(P_label))
        self.next_slide()

        tangentToCurve = TangentLine(graph, alpha=0.47, length=8, color=BLUE_D)

        self.play(Create(tangentToCurve))
        self.next_slide()

        Q = Dot(color=WHITE)
        Q.move_to(graph.point_from_proportion(0.29))
        Q_label = Text("Q", font_size=18).next_to(Q, UL)

        self.play(Create(Q), Create(Q_label))
        self.next_slide()

        R = Dot(color=WHITE)
        R.move_to(graph.point_from_proportion(0.71))
        R_label = Tex(r"$2P = P+P$").next_to(R,
                                             RIGHT).scale(.6).shift(LEFT*0.7)
        l3 = Line(Q, R, color=BLUE_D, stroke_width=3)

        self.play(Create(l3))
        self.play(Create(R), Create(R_label))
        self.next_slide()

        points_2P = Tex(
            r'$2P = P+P$').next_to(Text_pointDouble, DOWN, aligned_edge=DOWN).scale(0.8).shift(LEFT*0.7)

        self.play(Create(points_2P))
        self.next_slide()

        self.play(Unwrite(Q), Unwrite(Q_label), Unwrite(
            tangentToCurve, reverse=True), Unwrite(l3))

        l4 = Line(R, P, color=BLUE_D, stroke_width=3)
        self.play(Create(l4))
        self.next_slide()

        d1 = Dot(color=WHITE)
        d1.move_to(graph.point_from_proportion(0.567))
        self.play(Create(d1))
        self.next_slide()

        d2 = Dot(color=WHITE)
        d2.move_to(graph.point_from_proportion(0.4316))
        l5 = Line(d1, d2, color=BLUE_D, stroke_width=3)
        self.play(Uncreate(l4))
        self.play(Create(d2), Create(l5))
        self.next_slide()

        self.play(Uncreate(l5, reverse=True), Uncreate(d1))

        P3_lable = Tex(r"$3P = P+P+P$").next_to(d2,
                                                RIGHT).scale(0.6).shift(LEFT*0.5)
        P3 = Tex(r"$3P = P+P+P$").next_to(points_2P,
                                          DOWN, aligned_edge=DL, buff=0.5).scale(0.78).shift(LEFT*0.4)

        self.play(Create(P3_lable), Create(P3))
        self.next_slide()

        dot_dotDot_1 = Text('.').next_to(P3, DOWN)
        dot_dotDot_2 = Text('.').next_to(dot_dotDot_1, DOWN)
        dot_dotDot_3 = Text('.').next_to(
            dot_dotDot_2, DOWN)
        mP = Tex(r'$mP = P+P+P+...+P = Q$').next_to(dot_dotDot_3,
                                                    DOWN, aligned_edge=LEFT).scale(0.8).shift(LEFT*2)

        self.play(Create(dot_dotDot_1), Create(
            dot_dotDot_2), Create(dot_dotDot_3))
        self.play(Write(mP))
        plotDotTL(self)
        self.next_slide()

        question = Tex(r'Given $m$ and $P$ \\ Compute $Q = mP$ $\in$ $\mathcal{E}$', color=GREEN_C).next_to(
            mP, DOWN, buff=0.8).scale(0.8)
        self.play(Create(question))
        plotDotTL(self)

        self.next_slide()
        self.play(FadeOut(dot_dotDot_1), FadeOut(dot_dotDot_2), FadeOut(
            dot_dotDot_3), FadeOut(P3_lable), FadeOut(P3), FadeOut(points_2P))

        self.play(mP.animate.next_to(
            Text_pointDouble, DOWN, aligned_edge=LEFT), run_time=0.4)
        self.play(question.animate.next_to(mP, DOWN), run_time=0.3)

        txt_da = Tex(r'DOUBLE and ADD \\ Algorithm', font_size=43, color=BLUE_B).next_to(
            question, DOWN, buff=0.6)

        self.play(FadeIn(txt_da))
        # plotDotTL(self)

        nextScenePause(self)


class def_EC3_1_1(Slide):
    def construct(self):

        mP = Tex(r'$mP = P+P+P+...+P$').scale(1.5)
        m = Tex(r'$mP$').scale(1.5)

        titleText = MarkupText(
            f'<span fgcolor="{BLUE}">DOUBLE</span> and <span fgcolor="{RED}">ADD</span> algorithm', color=WHITE)
        self.play(FadeIn(titleText))
        self.next_slide()

        self.play(titleText.animate.to_edge(UL).shift(LEFT*1.3).scale(0.7))
        mP.next_to(titleText, DOWN).scale(0.6)
        self.play(Create(mP))
        m.next_to(titleText, DOWN).scale(0.6).shift(LEFT*2.28)
        self.play(FadeIn(m))
        self.next_slide()

        self.start_loop()  # Start loop
        my_rect = Rectangle(height=m.get_height()+0.3,
                            width=(m.get_width()+0.3), color=YELLOW)
        my_rect.surround(m)
        self.play(Create(my_rect), run_time=1.5)
        self.wait(0.3)
        self.play(FadeOut(my_rect))
        self.end_loop()  # This will loop until user inputs a key

        m_bin = Tex(
            r'$ m$', color=GREEN_D).next_to(mP, DOWN, buff=0.6).scale(1).shift(LEFT*3.2)

        transformTo_m = Transform(m, m_bin)
        self.play(transformTo_m, run_time=1.3)
        m_bin2 = Tex(
            r'$= m_0 + 2m_1 + 2^2m_2 + ... +2^sm_s$', color=GREEN).next_to(m_bin, RIGHT).scale(0.8).shift(LEFT*0.8)
        self.play(Create(m_bin2, shift=RIGHT), run_time=1.3)
        self.next_slide()

        example1 = Tex(r'e.g: $m = (9)_{10} = $').next_to(
            m_bin, DOWN, buff=0.4).shift(RIGHT*1.5)
        example2 = Tex(r'$(1001)_2$').next_to(example1, RIGHT)

        self.play(FadeIn(example1), FadeIn(example2))
        example2Copy = example2.copy()
        self.play(FadeIn(example2Copy))
        self.next_slide()

        first_One = Tex(r'$1$').next_to(example1, DOWN).shift(LEFT*1.5)
        first_Zero = Tex(r'$0$').next_to(first_One, DOWN)
        seond_Zero = Tex(r'$0$').next_to(first_Zero, DOWN)
        second_One = Tex(r'$1$').next_to(seond_Zero, DOWN)

        grp = VGroup()
        grp.add(first_Zero, first_One, seond_Zero, second_One)

        trans = Transform(example2, grp)
        self.play(trans)
        self.next_slide()

        txt_firstOne = Tex(
            r'$\blacktriangleright$ DOUBLE and ADD', color=BLUE).next_to(first_One, RIGHT).scale(0.7).shift(LEFT*0.8)
        txt_secondOne = Tex(
            r'$\blacktriangleright$ DOUBLE and ADD', color=BLUE).next_to(second_One, RIGHT).scale(0.7).shift(LEFT*0.8)

        txt_firstZero = Tex(
            r'$\blacktriangleright$ DOUBLE', color=RED).next_to(first_Zero, RIGHT).scale(0.7).shift(LEFT*0.32)
        txt_secondZero = Tex(
            r'$\blacktriangleright$ DOUBLE', color=RED).next_to(seond_Zero, RIGHT).scale(0.7).shift(LEFT*0.35)

        self.play(FadeIn(txt_firstOne, shift=RIGHT), run_time=1)
        self.wait(1)
        self.play(FadeIn(txt_firstZero, shift=RIGHT), run_time=1)
        self.play(FadeIn(txt_secondZero, shift=RIGHT), run_time=1)
        self.play(FadeIn(txt_secondOne, shift=RIGHT), run_time=1)

        self.next_slide()

        complexity = Tex(r"Complexity",
                         font_size=40, color=BLUE_A).shift(RIGHT*3).shift(UP)
        complexity2 = Tex(r"$O(log_2(m))$", font_size=66).next_to(
            complexity, DOWN, buff=0.3)

        self.play(FadeIn(complexity), FadeIn(complexity2))

        grp2 = VGroup()
        grp2.add(complexity2, complexity)
        myRect = SurroundingRectangle(grp2, color=YELLOW)
        grp2.add(myRect)

        self.play(Create(myRect), run_time=2)
        self.wait(0.3)
        self.play(FadeOut(myRect))

        nextScenePause(self)


class def_EC3_2(Slide):
    def construct(self):

        txt_1 = Tex(r'$mP = Q$')
        txt_2 = Tex(r'EASY !!!', color=GREEN).next_to(
            txt_1, RIGHT).shift(RIGHT*0.5)
        self.play(Write(txt_1), run_time=2)
        self.play(ScaleInPlace(txt_2, 1.4), run_time=3)
        self.wait(0.5)
        self.play(ShrinkToCenter(txt_2), run_time=2)

        self.next_slide()

        self.play(txt_1.animate.shift(UP*3))
        self.next_slide()

        txt_3 = Tex(r'The inverse problem...').shift(UP*1.5)
        self.play(Write(txt_3), run_time=2)
        self.next_slide()

        txt_4 = Tex(r'Given $P$ and $Q \in \mathcal{E}$, Find $m$.').next_to(
            txt_3, DOWN, buff=0.5)
        self.play(FadeIn(txt_4), run_time=2)
        self.next_slide()

        txt_51 = Tex(r'Elliptic Curve Discrete Logarithm Problem',
                     color=BLUE).next_to(txt_4, DOWN, buff=1)
        txt_5 = Tex(r'$Elliptic\: Curve\: Discrete\: Logarithm\: Problem$').next_to(
            txt_4, DOWN*1.2, buff=1).scale(1.2)
        self.play(FadeIn(txt_51))
        self.wait(1)
        self.play(Unwrite(txt_3),  run_time=1)

        self.play(txt_4.animate.shift(UP),
                  txt_51.animate.shift(UP), run_time=3)

        nextScenePause(self)


class def_EC3_3(Slide):
    def construct(self):
        txt_1 = Tex(r'$1985$')
        self.play(FadeIn(txt_1), run_time=1)
        self.play(ScaleInPlace(txt_1, 1.4), run_time=3)
        self.next_slide()

        self.play(txt_1.animate.shift(UP))

        txt_2 = Tex(r'Algorithms to solve ECDLP')
        self.play(FadeIn(txt_2), run_time=1)
        self.play(Unwrite(txt_1))
        self.next_slide()

        self.play(txt_2.animate.shift(UP*3))

        # Adjust the y-coordinates as needed
        line = Line(start=2*UP, end=2.2*DOWN)
        line.set_stroke(width=2)  # Set th

        txt_3 = Tex(r"\textbf{Generic algorithms}", color=WHITE, font_size=32)
        txt_4 = Tex(r"\textbf{Special algorithms}", color=BLUE, font_size=32)

        txt_3.next_to(txt_2, 2.3*DOWN)
        txt_3.shift(2.8*LEFT)

        txt_4.next_to(txt_2, 2.3*DOWN)
        txt_4.shift(2.7*RIGHT)

        self.play(GrowFromCenter(line))
        self.play(Write(txt_3), Write(txt_4))

        self.next_slide()

        items_1 = [
            "Baby-Step Giant-Step",
            "Pollards Rho",
            "Pollards lambda",
            "Pollards kangroo",
            "Teske's r-adding walk",
            "Polig-Hellman",
            "etc..."
        ]

        items_2 = [
            "Index calculus for EC",
            "Xedni Calculus",
            "Menezes, Okamoto & Vanstone",
            "SEMAEV's (p-Tortion points)",
            "Use of Summation polynomial",
            "Summation polynomial and SAT",
            "etc..."
        ]

        bullet = "• "
        bullet_color = WHITE

        generic_algos = [
            Text(f"{bullet}{item}", color=bullet_color, font_size=24) for item in items_1]
        genericAlgo_list = VGroup(*generic_algos)
        genericAlgo_list.arrange(DOWN, aligned_edge=LEFT*2)
        genericAlgo_list.next_to(txt_3, DOWN*1.5)
        # genericAlgo_list.shift(LEFT)

        bullet_color_special = BLUE_B
        special_algos = [
            Text(f"{bullet}{item}", color=bullet_color_special, font_size=24) for item in items_2]
        specialAlgo_list = VGroup(*special_algos)
        specialAlgo_list.arrange(DOWN, aligned_edge=LEFT*2)
        specialAlgo_list.next_to(txt_4, DOWN*1.5)
        specialAlgo_list.shift(0.7*RIGHT)

        self.play(Write(genericAlgo_list), run_time=2)
        self.play(Write(specialAlgo_list), run_time=1)

        self.next_slide()

        self.play(FadeOut(genericAlgo_list), FadeOut(
            specialAlgo_list), run_time=1)

        genComplexity = Tex(r'$\sim O(\sqrt{p})$', font_size=96, color=RED_B)
        genComplexity.next_to(txt_3, 6*DOWN)
        genComplexity.shift(LEFT*0.1)

        txt_5 = Tex(r'$p$ : order of group', font_size=30).next_to(
            line, DOWN)

        speComplexity = Tex(r'$< O(\sqrt{p})$', font_size=96, color=BLUE_B)
        speComplexity.next_to(txt_4, 6*DOWN)
        speComplexity.shift(LEFT*0.1)

        self.play(FadeIn(genComplexity), FadeIn(speComplexity), run_time=1)

        txt_7 = Tex(r'Exponential complexity', font_size=30, color=RED_C).next_to(
            genComplexity, DOWN)
        txt_6 = Tex(r'Sub-exponential complexity', font_size=30, color=BLUE_C).next_to(
            speComplexity, DOWN)

        self.play(FadeIn(txt_6), FadeIn(txt_7))

        self.play(Write(txt_5))

        nextScenePause(self)


class def_LV4_1(Slide):
    def construct(self):

        txt_1 = Tex(r'Las Vegas Algorithm').scale(1.6)
        self.play(FadeIn(txt_1), run_time=2)

        self.next_slide()
        self.play(FadeOut(txt_1))

        plane = NumberPlane(x_range=[-12, 12, 1], x_length=12,
                            y_range=[-13, 13, 1], y_length=13,
                            background_line_style={
            "stroke_color": BLUE,
            "stroke_width": 2,
            "stroke_opacity": 0.3
        }
        ).add_coordinates().to_edge(LEFT)

        self.play(DrawBorderThenFill(plane))
        ellipticCurvePoints = getEC_points()

        graph = VMobject(color=RED)
        graph.set_points_smoothly(plane.coords_to_point(
            ellipticCurvePoints))

        self.play(Create(graph), run_time=3)

        self.next_slide()
        grp = VGroup()
        grp.add(plane, graph)
        myRect = SurroundingRectangle(grp, color=BLUE)
        grp.add(myRect)
        self.play(grp.animate.scale(0.6).to_edge(LEFT))

        txt_1_1 = Tex(
            r"$\mathcal{E}$ - Elliptic curve").to_edge(UR, buff=1.5).scale(0.8).shift(UL)
        self.play(FadeIn(txt_1_1), run_time=1)

        self.next_slide()
        txt_2 = Tex(r"$\mathcal{C}$ - Curve of degree $n$").next_to(
            txt_1_1, DOWN, buff=0.4).scale(0.8).shift(RIGHT*0.4)
        self.play(FadeIn(txt_2), run_time=1)

        self.next_slide()
        hCurve = getHomogenousCurvePoints()
        graph2 = VMobject(color=BLUE)

        graph2.set_points_smoothly(plane.coords_to_point(
            hCurve))
        grp.add(graph2)
        self.play(Create(graph2), run_time=2)

        P0 = Dot(color=WHITE)
        P1 = Dot(color=WHITE)
        P2 = Dot(color=WHITE)

        P0.move_to(graph2.point_from_proportion(0.16))
        P2.move_to(graph2.point_from_proportion(0.39))
        P1.move_to(graph2.point_from_proportion(0.467))

        P3 = Dot(color=WHITE)
        P4 = Dot(color=WHITE)
        P5 = Dot(color=WHITE)

        P3.move_to(graph2.point_from_proportion(0.84))
        P4.move_to(graph2.point_from_proportion(0.61))
        P5.move_to(graph2.point_from_proportion(0.533))

        self.play(Create(P0), Create(P1), Create(P2),
                  Create(P3), Create(P4), Create(P5), run_time=2)

        self.next_slide()
        txt_3 = Tex(r'If $\mathcal{C}$ intersects $\mathcal{E}$ at $3n$ points', color=BLUE).next_to(
            txt_2, DOWN, buff=0.4).scale(0.8).shift(RIGHT*0.6)
        self.play(FadeIn(txt_3), run_time=1)

        txt_4 = Tex(r'ECDLP is solved', color=GREEN).next_to(
            txt_3, DOWN, buff=0.4).scale(1.2).align_to(txt_3, LEFT)
        self.play(FadeIn(txt_4), run_time=3)

        self.next_slide()
        txt_5 = Tex(r'How can we find $\mathcal{C}$ ?').next_to(
            txt_4, DOWN, buff=0.5).scale(0.7).align_to(txt_4, LEFT)
        self.play(FadeIn(txt_5))

        self.next_slide()
        txt_6 = Tex(r'Use Linear Algebra to find $\mathcal{C}$').next_to(
            txt_5, DOWN, buff=0.4).scale(0.7).align_to(txt_5, LEFT)
        self.play(FadeIn(txt_6))

        self.next_slide()
        txt_7 = Tex(r'ECDLP reduced to a problem in \\ Linear Algebra').next_to(
            txt_6, DOWN, buff=0.4).scale(0.7).align_to(txt_6, LEFT)
        txt_8 = Tex(r'Zero Minor Problem', color=RED).next_to(
            txt_7, DOWN, buff=0.5).scale(1.1).shift(RIGHT*0.1)
        self.play(FadeIn(txt_7))
        self.play(Write(txt_8), run_time=2)

        self.next_slide()

        self.play(FadeOut(txt_8), FadeOut(txt_7), FadeOut(txt_6), FadeOut(txt_4), FadeOut(txt_3),
                  FadeOut(txt_2), FadeOut(txt_1_1), FadeOut(graph), FadeOut(
                      graph2), FadeOut(P0), FadeOut(P1), FadeOut(P2),
                  FadeOut(P3), FadeOut(P4), FadeOut(P5), FadeOut(plane), FadeOut(myRect), run_time=2)

        self.next_slide()
        self.play(txt_5.animate.scale(1/0.6).shift(LEFT*2.5))
        nextScenePause(self)


class def_LV4_2(Slide):
    def construct(self):
        txt_1 = Tex(r'Why does the existence of $\mathcal{C}$ solve ECDLP?')
        self.play(Write(txt_1))

        self.next_slide()
        # self.play(txt_1.animate.shift(UL*2))
        self.play(txt_1.animate.to_edge(UP))

        theorem_text = r"""
        \Large \textbf{Main Theorem :} \\ \par
        Let $\mathcal{E}$ be an elliptic curve over $\mathbb{F}_q$ and $P_1, P_2,...,P_\ell$ be points on that curve,
          where $\ell = 3n'$ for some positive integer $n'$. Then $\sum_{i=1}^{\ell} P_i = \mathcal{O}$ if and only if 
          there is a curve $\mathcal{C}$ over $\mathbb{F}_q$ of degree $n'$ that passes through these points. Multiplicities are 
          intersection multiplicities.
        """

        theorem = Tex(theorem_text).next_to(txt_1, DOWN, buff=0.2)
        theorem.scale(0.6)  # Adjust the scaling if needed
        self.play(Write(theorem))

        # More here later

        nextScenePause(self)


class def_LV4_3(Slide):
    def construct(self):
        txt_1 = Tex(r'How can we find $\mathcal{C}$?').scale(1.1)
        self.play(FadeIn(txt_1), run_time=0.1)

        self.next_slide()

        # self.play(txt_1.animate.scale(0.7))
        self.play(txt_1.animate.shift(UP*3.2))
        txt_2 = """ Generate $k = 3n + 3n$ points,"""
        txt_21 = Tex(txt_2)
        self.play(Write(txt_21))

        self.play(txt_21.animate.shift(UP*2.5))
        self.next_slide()

        self.play(txt_21.animate.shift(LEFT*1.2))

        txt_4 = """ also, $k = s+t$ """
        txt_41 = Tex(txt_4).next_to(txt_21, RIGHT)
        self.play(Write(txt_41))

        self.next_slide()
        txt_3 = """\{ $n_1, n_2, n_3, ... , n_{s-1}, n_s$"""
        txt_31 = Tex(txt_3).shift(LEFT*3.7)

        txt_5 = """$, n_{s+1}, n_{s+2}, ... , n_{k-1}, n_{k}$ \} $\in \mathbb{Z}_{>0}$"""
        txt_51 = Tex(txt_5).next_to(txt_31, RIGHT)

        self.play(Write(txt_31))
        self.play(Write(txt_51))
        self.next_slide()

        self.play(Circumscribe(txt_31))
        self.play(Circumscribe(txt_31, fade_out=True))
        plotDotTL(self)

        self.next_slide()
        txt_6 = Tex(r'$P$', color=BLUE).scale(2).next_to(txt_31, DOWN)
        self.play(FadeIn(txt_6))

        self.next_slide()
        txt_7 = """\{ $P_{n_1}, P_{n_2}, P_{n_3}, ... , P_{n_{s-1}}, P_{n_s}$"""
        txt_71 = Tex(txt_7, color=BLUE_B).next_to(txt_6, DOWN)
        self.play(Write(txt_71))

        self.next_slide()
        self.play(Circumscribe(txt_51))
        self.play(Circumscribe(txt_51, fade_out=True))
        plotDotTL(self)

        self.next_slide()
        txt_62 = Tex(r'$Q$', color=YELLOW).scale(2).next_to(txt_6, RIGHT*17)
        self.play(FadeIn(txt_62))
        plotDotTL(self)

        self.next_slide()
        txt_8 = """$, Q_{n_{s+1}}, Q_{n_{s+2}}, ... , Q_{n_{k-1}}, Q_{n_{k}}$ \}"""
        txt_81 = Tex(txt_8, color=YELLOW).next_to(txt_71, RIGHT)
        self.play(Write(txt_81))

        self.next_slide()
        self.play(FadeOut(txt_6), FadeOut(txt_62))

        rn_grp = VGroup()
        rn_grp.add(txt_31)
        rn_grp.add(txt_51)
        self.play(rn_grp.animate.shift(UP*1.8))

        points_grp = VGroup()
        points_grp.add(txt_71)
        points_grp.add(txt_81)
        self.play(points_grp.animate.shift(UP*2.7).shift(RIGHT*0.4))

        self.next_slide()
        # txt_01 = Tex(r'Check if $\exists$ a curve ($\mathcal{C}$) passing through these points').next_to(points_grp, DOWN, buff=0.5)
        # self.play(Write(txt_01))

        txt_02 = """$\mathcal{C} = \sum_{i+j+k=n}{} a_{ijk}x^iy^jz^k$"""
        txt_022 = Tex(txt_02).next_to(points_grp, DOWN, buff=0.5).scale(1.4)
        self.play(Write(txt_022))

        # self.next_slide()
        # txt_031 = Tex(r'$P=[x:y:z]$ substitute in $\mathcal{C}$').next_to(txt_022, DOWN, buff=0.3).shift(LEFT*2)
        # self.play(Write(txt_031))

        self.next_slide()
        txt_032 = Tex(r'$\overline{P}$ : Value of $\mathcal{C}$ when $x,y,z \in P=[x:y:z]$ substitute in $\mathcal{C}$', color=YELLOW_B).next_to(
            txt_022, DOWN)
        self.play(Write(txt_032))

        self.next_slide()
        txt_033 = Tex(r'$\overline{Q}$ : Value of $\mathcal{C}$ when $x,y,z \in Q=[x:y:z]$ substitute in $\mathcal{C}$').next_to(
            txt_032, DOWN)
        self.play(Write(txt_033))

        self.next_slide()
        self.play(FadeOut(txt_022), FadeOut(points_grp), FadeOut(rn_grp))

        grp1 = VGroup()
        grp1.add(txt_032)
        grp1.add(txt_033)

        self.play(grp1.animate.shift(UP*2.9).scale(0.6))

        self.next_slide()
        mat = Matrix([[r"\textbf{$\overline{P}_1$}"], ["\overline{P}_2"], ["\overline{P}_3"], ["\\vdots"], ["\overline{P}_s"], ["\\vdots"], ["\overline{Q}_1"], ["\overline{Q}_2"], ["\overline{Q}_3"], ["\\vdots"], ["\overline{Q}_k"]], left_bracket="(",
                     right_bracket=")").scale(.4).next_to(grp1, DOWN)
        mat.set_color(YELLOW)
        self.play(Write(mat))

        self.next_slide()
        txt_034 = Tex(r'$\mathcal{M} = $').next_to(mat, LEFT)
        self.play(FadeIn(txt_034))

        self.next_slide()
        grp2 = VGroup()
        grp2.add(txt_034, mat)
        self.play(grp2.animate.shift(LEFT*5))

        self.next_slide()
        txt_035 = Tex(r'ker($\mathcal{M}$) = $\mathcal{K}$ =').next_to(
            mat, RIGHT).scale(0.7)
        self.play(FadeIn(txt_035))

        m0 = Matrix([["a_{1,1}", "a_{1,2}", "a_{1,3}", "\dots", "a_{1,\ell}", "0", "\dots", "0", "1"], ["a_{2,1}", "a_{2,2}", "a_{2,3}", "\dots", "a_{2,\ell}", "0", "\dots", "1", "0"], ["\\vdots", "\\vdots", "\\vdots", "\ddots", "\\vdots", "\\vdots", "\ddots", "\\vdots", "\\vdots"], ["a_{\ell,1}", "a_{\ell,2}", "a_{\ell,3}", "\dots", "a_{\ell,\ell}", "1", "\dots", "0", "0"]], left_bracket="(",
                    right_bracket=")").scale(0.6).next_to(txt_035, RIGHT)

        self.next_slide()
        self.play(Write(m0, shift=RIGHT), run_time=2)
        self.play(FadeOut(txt_21), FadeOut(txt_41))

        self.next_slide()
        self.play(FadeOut(txt_034), FadeOut(mat),
                  FadeOut(grp1), FadeOut(txt_035))
        self.play(m0.animate.shift(UL*2.2))

        self.next_slide()
        self.play(m0.animate.shift(DOWN))
        txt_041 = Tex(
            r'$n_1\:\:\:\:n_2\:\:\:\:\:\: n_3\:\:\:\:\: ... \:\:\:\:\:\:n_{\ell} \:\:\:\: n_{\ell+1} \:\: ... \:\: n_{k-1}\:\:\:\: n_k$', color=YELLOW).scale(0.75).next_to(m0, UP).shift(RIGHT*0.2)
        self.play(Write(txt_041))

        self.next_slide()

        L = Tex(r"$\ell = 3n$").scale(0.8).next_to(txt_041, UP)
        self.play(FadeIn(L))
        self.next_slide()

        row_brace = Brace(m0, direction=LEFT)
        # row_text = row_brace.get_text("Rows = l")

        col_brace = Brace(m0, direction=DOWN)
        # col_text = col_brace.get_text("Columns = 2l")

        # Position row and column labels
        row_brace.next_to(m0, LEFT, buff=SMALL_BUFF)
        # row_text.next_to(row_brace, LEFT, buff=SMALL_BUFF)

        col_brace.next_to(m0, DOWN, buff=SMALL_BUFF)
        # col_text.next_to(col_brace, DOWN, buff=SMALL_BUFF)

        # Add row and column labels to the scene
        rows = Tex(r"$\ell$").next_to(m0, LEFT, buff=0.7)
        cols = Tex(r"$2 \times \ell$").next_to(m0, DOWN, buff=0.4)
        self.play(FadeIn(row_brace), FadeIn(rows))
        self.play(FadeIn(col_brace), FadeIn(cols))

        self.next_slide()
        # self.play(FadeOut(col_brace), FadeOut(
        #     row_brace), FadeOut(rows), FadeOut(cols))

        underbrace = Brace(m0, direction=DOWN,
                           buff=1).scale(0.4).shift(RIGHT*2.3)
        lZeros = Tex(r"$\ell - 1$ zeros",
                     color=YELLOW).next_to(underbrace, DOWN)

        # Add the underbrace and the description to the scene
        self.play(FadeIn(underbrace), FadeIn(lZeros))

        self.next_slide()
        grp_k = VGroup()
        grp_k.add(m0, row_brace, col_brace, rows,
                  cols, underbrace, lZeros, txt_041, L)

        self.play(grp_k.animate.scale(0.9).shift(UP))

        txt_lZ = Tex(
            r"If the left kernel contains a vector with $\ell$ zeros, \\ ECDLP is solved.", font_size=40).next_to(grp_k, DOWN, buff=1)

        self.play(FadeIn(txt_lZ))

        self.next_slide()

        self.play(FadeOut(txt_lZ), FadeOut(row_brace), FadeOut(col_brace), FadeOut(
            rows), FadeOut(cols), FadeOut(underbrace), FadeOut(lZeros), FadeOut(txt_041))

        m01 = Matrix([["a_{1,1}", "a_{1,2}", "a_{1,3}", "\dots", "a_{1,\ell}"], ["a_{2,1}", "a_{2,2}", "a_{2,3}", "\dots", "a_{2,\ell}"], ["\\vdots", "\\vdots", "\\vdots", "\\ddots", "\\vdots"], ["a_{\ell,1}", "a_{\ell,2}", "a_{\ell,3}", "\dots", "a_{\ell,\ell}"]], left_bracket="(",
                     right_bracket=")").scale(0.6).next_to(m0, DOWN, buff=0.6)
        txt_2 = Tex(r'$\mathcal{A} = $').next_to(m01, LEFT)
        grp_m2 = VGroup()
        grp_m2.add(m01, txt_2)

        trans_grp_m2 = TransformFromCopy(m0, grp_m2)

        self.play(trans_grp_m2)
        self.play(FadeOut(L))
        # self.next_slide()

        nextScenePause(self)


class def_LV4_4(Slide):
    def construct(self):
        txt_1 = Tex(r"Non-Singular matrix $(\mathcal{A})$").to_edge(UL)
        self.play(Create(txt_1))
        plotDotTL(self)

        self.next_slide()
        m0 = Matrix([["a_{1,1}", "a_{1,2}", "a_{1,3}", "\dots", "a_{1,\ell}"], ["a_{2,1}", "a_{2,2}", "a_{2,3}", "\dots", "a_{2,\ell}"], ["\\vdots", "\\vdots", "\\vdots", "\\ddots", "\\vdots"], ["a_{\ell,1}", "a_{\ell,2}", "a_{\ell,3}", "\dots", "a_{\ell,\ell}"]], left_bracket="(",
                    right_bracket=")").scale(0.5).next_to(txt_1, DOWN, buff=0.4).shift(RIGHT*4).scale(1.2)
        txt_2 = Tex(r'$\mathcal{A} = $').next_to(m0, LEFT)
        self.play(Create(m0), Create(txt_2))
        plotDotTL(self)

        txt_3 = Tex(
            r'Row Sum constant ($p-1$) - for $\mathcal{A}$').next_to(txt_2, DOWN).shift(DOWN)
        self.play(Write(txt_3))

        txt_4 = Tex(r'- Row Sum $0$ for $\mathcal{K}$', color=BLUE_C).next_to(
            txt_3, DOWN).shift(LEFT*1.84).scale(0.7)
        self.play(Write(txt_4))

        txt_5 = Tex(r'- Row Sum remains constant after row-operations',
                    color=BLUE_C).next_to(txt_4, DOWN, buff=0.3).scale(0.7).shift(RIGHT*2.35)
        self.play(Write(txt_5))
        self.next_slide()

        txt_6 = Tex(r'Increasing size of $\mathcal{A}$ (maybe) helpful').next_to(
            txt_5, DOWN, buff=0.3).shift(LEFT*0.3)
        self.play(Write(txt_6))

        txt_7 = Tex(r'Dim($\mathcal{A}$) = $\ell \times \ell = 3n \times 3n = 3log_2(p) \times 3log_2(p)$').next_to(
            txt_6, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(txt_7))

        nextScenePause(self)


class def_impl5(Slide):
    def construct(self):
        txt_1 = Tex(r"Implementing Details").to_edge(UL)
        self.play(Create(txt_1))
        plotDotTL(self)

        txt_2 = Tex(r'ToDo...')
        self.play(FadeIn(txt_2))

        nextScenePause(self)


class def_minor6(Slide):
    def construct(self):
        txt_1 = Tex(r"Minors to solve ECDLP").to_edge(UL)
        self.play(Create(txt_1))
        plotDotTL(self)

        self.next_slide()
        m0 = Matrix([["a_{1,1}", "a_{1,2}", "a_{1,3}", "\dots", "a_{1,\ell}"], ["a_{2,1}", "a_{2,2}", "a_{2,3}", "\dots", "a_{2,\ell}"], ["\\vdots", "\\vdots", "\\vdots", "\\ddots", "\\vdots"], ["a_{\ell,1}", "a_{\ell,2}", "a_{\ell,3}", "\dots", "a_{\ell,\ell}"]], left_bracket="(",
                    right_bracket=")").scale(0.5).next_to(txt_1, DOWN, buff=0.4).shift(RIGHT*4).scale(1.2)
        txt_2 = Tex(r'$\mathcal{A} = $').next_to(m0, LEFT)
        grp0 = VGroup()
        grp0.add(m0, txt_2)
        self.play(Create(grp0))
        grp01 = grp0.copy()
        self.add(grp01)
        plotDotTL(self)

        self.next_slide()

        m1 = Matrix([["70", "18", "01", "17", "10"], ["10", "13", "54", "43", "48"], ["23", "43", "08", "24", "57"], ["29", "21", "56", "61", "48"], ["49", "38", "21", "46", "27"]], left_bracket="(",
                    right_bracket=")").scale(.6).next_to(m0, DOWN, buff=1.1)

        trans1 = TransformFromCopy(m0, m1)

        self.play(trans1)
        self.next_slide()

        rect2 = Rectangle(
            width=1.4,
            height=0.83,
            color=GREEN)

        rect2.set_stroke(width=2)
        rect2.move_to([m1.get_x()-1.2, m1.get_y()+0.7, 0])
        self.play(Write(rect2))
        self.next_slide()

        grp_m = VGroup()
        grp_m.add(m1, rect2)
        self.play(grp_m.animate.shift(LEFT*3))

        minor = Matrix([["70", "18"], ["10", "13"]], left_bracket="|",
                       right_bracket="|").scale(.5).next_to(grp_m, RIGHT, buff=0.5, aligned_edge=UP).shift(RIGHT*2)

        trans_minor = TransformFromCopy(rect2, minor)
        self.play(trans_minor)

        self.next_slide()

        txt_4 = Tex(r'$(70 \times 13) - (18 \times 10) \: mod \: 73$',
                    color=BLUE_B).next_to(minor, DOWN).scale(0.7)
        txt_5 = Tex(r'$ 910 - 180 \: mod \: 73$',
                    color=BLUE_B).next_to(txt_4, DOWN).scale(0.7)
        txt_6 = Tex(r'$34 - 34 = 0$',
                    color=BLUE_B).next_to(txt_5, DOWN).scale(0.7)
        txt_7 = Tex(r'$0$', color=BLUE_B).next_to(txt_6, DOWN).scale(0.7)

        self.play(AddTextWordByWord(txt_4), run_time=2)
        self.play(AddTextWordByWord(txt_5), run_time=2)
        self.play(AddTextWordByWord(txt_6), run_time=2)

        self.next_slide()

        self.play(FadeOut(txt_4), FadeOut(txt_5),
                  FadeOut(txt_6), FadeOut(txt_7), FadeOut(minor))

        txt_8 = Tex(r'$R_{1} \: - \: 70 \: \times \: R_{2}$', color=BLUE).scale(0.8).next_to(
            grp_m, RIGHT, buff=0.5, aligned_edge=UP).shift(RIGHT*2).shift(UP*0.5)
        self.play(FadeIn(txt_8))
        self.next_slide()

        m3 = Matrix([["00", "00", "61", "08", "39"], ["10", "13", "54", "43", "48"], ["23", "43", "08", "24", "57"], ["29", "21", "56", "61", "48"], ["49", "38", "21", "46", "27"]], left_bracket="(",
                    right_bracket=")").scale(.6).next_to(txt_8, DOWN).align_to(m1, UP)

        self.play(FadeIn(m3))

        self.next_slide()
        self.play(FadeOut(m1), FadeOut(m3), FadeOut(txt_8), FadeOut(rect2))

        txt_end = Tex(
            r'A Zero-Minor in a non-singular matrix solves ECDLP', color=BLUE).next_to(m0, DOWN, buff=1)

        self.play(Write(txt_end))

        self.next_slide()

        self.play(Unwrite(txt_end))

        # # The 2 minor experiment
        # self.next_slide()
        # txt_2 = Tex(r'All 2-Minor algorithm',
        #             color=BLUE_C).next_to(txt_2, DOWN).shift(DOWN).to_edge(LEFT)
        # self.play(FadeIn(txt_2))

        # self.next_slide()

        # table_2M = MathTable(
        #     [["\mathbb{F}_q", "Avg. \: kernel \: count", "\log_2(p)", "No. \: of \: rows \: in \: \mathcal{A}"],
        #      ["2^{40}", "113.4", "39", "360"],
        #      ["2^{43}", "716.3", "42", "387"],
        #      ["2^{46}", "4406.26", "45", "414"]],
        #     include_outer_lines=False,
        #     line_config={"stroke_width": 2},
        #     h_buff=0.6,
        #     v_buff=0.3,
        # ).scale(0.7).next_to(txt_2, DOWN).shift(RIGHT*3)

        # self.play(Write(table_2M))
        # plotDotTL(self)

        # self.next_slide()
        # self.play(FadeOut(table_2M), FadeOut(txt_2))

        txt_3 = Tex(r'Gaussian Elimination Schur Complement', color=RED_C).next_to(
            txt_2, DOWN).shift(DOWN).to_edge(LEFT)
        self.play(Write(txt_3))

        self.next_slide()
        txt_2 = Tex(r'$\mathcal{A} = $').next_to(txt_3, DOWN, buff=1)
        m1 = Matrix([["A", "B"], ["C", "D"]], left_bracket="(",
                    right_bracket=")").scale(0.5).next_to(txt_2, RIGHT, buff=0.4).scale(1.5)
        grp1 = VGroup()
        grp1.add(m1, txt_2)

        trans1 = Transform(grp0, grp1)
        self.play(trans1)
        self.play(Uncreate(grp1), run_time=0.1)

        self.next_slide()
        self.play(grp0.animate.shift(LEFT*1.5))

        self.next_slide()
        txt_41 = Tex(r'$\Longrightarrow$').next_to(grp0, RIGHT, buff=0.3)
        txt_4 = Tex("""$\mathcal{A}' = \:$""").next_to(txt_41, RIGHT, buff=0.3)
        m2 = Matrix([["E\'", "F\'"], ["G\'", "H\'"]], left_bracket="(",
                    right_bracket=")").scale(0.5).next_to(txt_4, RIGHT, buff=0.4).scale(1.5)

        grp2 = VGroup()
        grp2.add(m2, txt_4)
        self.play(Write(txt_41))
        self.play(FadeIn(grp2, shift=RIGHT), run_time=2)
        plotDotTL(self)

        self.next_slide()
        self.play(FadeOut(grp0))
        m2 = Matrix([["a_{1,1}", "a_{1,2}", "a_{1,3}", "a_{1,4}", "a_{1,5}"], ["a_{2,1}", "a_{2,2}", "a_{2,3}", "a_{2,4}", "a_{2,5}"], ["a_{1,1}", "a_{1,2}", "a_{1,3}", "a_{1,5}", "a_{1,5}"], ["a_{1,1}", "a_{1,2}", "a_{1,3}", "a_{1,5}", "a_{1,5}"], ["a_{1,1}", "a_{1,2}", "a_{1,3}", "a_{1,5}", "a_{1,5}"]], left_bracket="(",
                    right_bracket=")").scale(0.5).next_to(txt_41, LEFT, buff=0.5).shift(DOWN*0.3)
        txt_m2 = Tex(r'$\mathcal{A} = $').next_to(m2, LEFT)
        self.play(Write(m2), Write(txt_m2), run_time=0.5)

        l1 = Line([-4.1, -0.5, 0], [-4.1, -2.45, 0])
        l2 = Line([-4.7, -0.85, 0], [-1.5, -0.85, 0])

        l1.set_stroke(width=2)
        l2.set_stroke(width=2)

        self.play(Write(l1), Write(l2))

        self.next_slide()
        self.play(FadeOut(grp2))
        txt_m3 = Tex("""$\mathcal{A}' = $""").next_to(txt_41, RIGHT)

        l3 = Line([2.18, -0.5, 0], [2.18, -2.5, 0])
        l4 = Line([1.5, -0.83, 0], [4.7, -0.83, 0])
        l3.set_stroke(width=2)
        l4.set_stroke(width=2)

        m3 = Matrix([["a_{1,1}", "a_{1,2}", "a_{1,3}", "a_{1,4}", "a_{1,5}"],
                     ["0", "a_{2,2}'", "a_{2,3}'", "a_{2,4}'", "a_{2,5}'"],
                     ["0", "a_{3,2}'", "a_{3,3}'", "a_{3,4}'", "a_{3,5}'"],
                     ["0", "a_{4,2}'", "a_{4,3}'", "a_{4,4}'", "a_{4,5}'"],
                     ["0", "a_{5,2}'", "a_{5,3}'", "a_{5,4}'", "a_{5,5}'"]], left_bracket="(",
                    right_bracket=")").scale(0.5).next_to(txt_m3, RIGHT*0.4, buff=0.5)

        grp3 = VGroup()
        grp3.add(m3, txt_m3)
        grp3.shift(DOWN*0.3)
        self.play(txt_41.animate.shift(DOWN*0.3))
        self.play(Write(grp3), run_time=0.5)
        self.play(Write(l3), Write(l4))

        self.next_slide()

        rect = Rectangle(width=2.56, height=1.6, color=YELLOW,
                         stroke_width=2).move_to([3.5, -1.7, 0])

        self.start_loop()
        self.play(Write(rect))
        self.wait(0.3)
        self.play(FadeOut(rect))
        self.end_loop()

        rect21 = Rectangle(width=1.2, height=0.8, color=RED,
                           stroke_width=2).move_to([3.45, -1.6, 0])
        self.play(FadeIn(rect21))
        grp3.add(rect21, l3, l4)

        self.next_slide()
        self.play(FadeOut(m2), FadeOut(txt_m2), FadeOut(
            txt_41), FadeOut(l1), FadeOut(l2))
        self.play(FadeOut(txt_1), FadeOut(grp01))

        self.play(txt_3.animate.to_edge(UP))
        self.play(grp3.animate.next_to(txt_3, DOWN).shift(LEFT*1.4))

        self.next_slide()
        txt_20 = Tex("""$\Longrightarrow$ $\mathcal{A}' = $""").next_to(
            grp3, RIGHT, buff=0.5)
        m4 = Matrix([["E\'", "F\'"],
                     ["0", "H\'"]], left_bracket="[",
                    right_bracket="]").scale(1.3).next_to(txt_20, RIGHT, buff=0.2)

        self.play(FadeIn(m4, shift=RIGHT), Write(txt_20))
        plotDotTL(self)

        self.next_slide()
        rect1 = Rectangle(width=1.4, height=1, color=BLUE, fill_color=BLUE_D,
                          stroke_width=2, fill_opacity=0.5).move_to([2.2, 2.3, 0])
        rect2 = Rectangle(width=1.85, height=1.2, color=YELLOW, fill_color=YELLOW_B,
                          stroke_width=2, fill_opacity=0.5).move_to([3.9, 1.3, 0])

        self.play(Write(rect1))
        plotDotTL(self)

        self.next_slide()
        self.play(Write(rect2))
        plotDotTL(self)

        self.next_slide()
        txt_m1 = Tex(r""" $E' = $""").next_to(
            grp3, DOWN*2, buff=0.5).scale(0.7)
        m1 = Matrix([["a_{1,1}", "a_{1,2}", "a_{1,3}", "\dots", "a_{1,\ell'}"],
                    ["a_{2,1}", "a_{2,2}", "a_{2,3}", "\dots", "a_{2,\ell'}"],
                    ["\\vdots", "\\vdots", "\\vdots", "\\ddots", "\\vdots"],
                    ["a_{\ell',1}", "a_{\ell',2}", "a_{\ell',3}", "\dots", "a_{\ell',\ell'}"]], left_bracket="(",
                    right_bracket=")").scale(0.5).next_to(txt_m1, RIGHT, buff=0.1)
        grp1 = VGroup()
        grp1.add(txt_m1, m1)
        grp1.shift(LEFT*1.6)
        t1 = Transform(rect1, grp1)
        self.play(t1)

        self.next_slide()
        txt_row = MathTex(r"\alpha = \{1, 2, 3, ... ,\ell' \}, \: \beta = \{1, 2, 3, ... ,\ell' \}", color=BLUE).next_to(
            grp3, DOWN).scale(0.7).shift(RIGHT*5.8)
        self.play(Write(txt_row))

        self.next_slide()

        txt_row2 = MathTex(r"\alpha' = \{r_1, r_2 \}, \: \beta' = \{ c_1, c_2 \}", color=YELLOW).next_to(
            txt_row, DOWN).scale(0.7).align_to(txt_row, LEFT)

        t2 = Transform(rect2, txt_row2)
        self.play(t2)

        self.next_slide()
        self.play(FadeOut(rect1))

        self.play(Uncreate(txt_row2), run_time=0.1)
        self.play(txt_row.animate.shift(LEFT*6), rect2.animate.shift(LEFT*6))

        txt_m4 = Tex(r""" det($A'[\alpha , \alpha'|\beta , \beta']) = det$""").next_to(
            txt_row2, RIGHT).scale(0.6).shift(LEFT)
        m4 = Matrix([["a_{1,1}", "a_{1,3}", "a_{1,4}"],
                     ["0", "a_{3,3}'", "a_{3,4}'"],
                     ["0", "a_{4,3}'", "a_{4,4}'"]], left_bracket="(",
                    right_bracket=")").scale(0.5).next_to(txt_m4, RIGHT)
        txt_m41 = Tex(r' $=\:\:0$').next_to(m4, RIGHT)

        grp4 = VGroup()
        grp4.add(txt_m4, m4, txt_m41).shift(LEFT*4)

        t3 = Transform(rect21, grp4)
        self.play(t3)

        self.next_slide()
        equation = MathTex(
            r"\det(\mathcal{A}[1,2,3,...,\ell', \alpha'|1,2,3,...,\ell', \beta']) = 0").next_to(grp4, DOWN, buff=0.5).shift(LEFT*3)

        self.play(Create(equation))
        plotDotTL(self)

        self.next_slide()
        self.play(FadeOut(equation), FadeOut(rect21), FadeOut(
            txt_row), FadeOut(txt_row2), FadeOut(rect2))

        table_GESC = MathTable(
            [[r"\textbf{$\mathbb{F}_q$}", r"\textbf{Avg. \: kernel \: count}", r"\textbf{$\log_2(p)$}", r"\textbf{No. \: of \: rows \: in \: $\mathcal{A}$}"],
             ["2^{40}", "2.8", "39", "360"],
             ["2^{41}", "3", "40", "369"],
             ["2^{42}", "6", "41", "378"],
             ["2^{43}", "11", "42", "387"],
             ["2^{44}", "17", "43", "396"],
             ["2^{45}", "53", "44", "405"],
             ["2^{46}", "40", "45", "414"],
             ["2^{47}", "126", "46", "423"],
             ["2^{48}", "186", "47", "432"],
             ["2^{49}", "367", "48", "441"],
             ["2^{50}", "887", "49", "450"]
             ],
            include_outer_lines=False,
            line_config={"stroke_width": 0.5},
            h_buff=0.6,
            v_buff=0.3
        ).scale(0.5).shift(1.5*DOWN)
        table_GESC.set_color(YELLOW)

        image1 = ImageMobject("img/graph.jpg")
        image1.scale(0.7).next_to(m3, DOWN).shift(RIGHT*2.5)
        self.play(FadeIn(image1))
        # nextScenePause(self)

        # self.play(Write(table_GESC))

        nextScenePause(self)


class def_APM7(Slide):
    def construct(self):
        txt_1 = Tex(r"Almost Principal Minors to solve ECDLP").to_edge(UL)
        self.play(Create(txt_1))
        plotDotTL(self)

        self.next_slide()

        txt_2 = Tex("""$\mathcal{A}' = $""").next_to(txt_1, 5*DOWN)
        m0 = Matrix([["E\'", "F\'"],
                     ["0", "H\'"]], left_bracket="[",
                    right_bracket="]").scale(1.3).next_to(txt_2, RIGHT, buff=0.2)

        self.play(Create(m0), Write(txt_2))
        plotDotTL(self)

        self.next_slide()
        #########
        rect1 = Rectangle(width=1.4, height=1, color=BLUE, fill_color=BLUE_D,
                          stroke_width=2, fill_opacity=0.5).move_to([-0.63, 2.1, 0])
        rect2 = Rectangle(width=1.85, height=1.2, color=YELLOW, fill_color=YELLOW_B,
                          stroke_width=2, fill_opacity=0.5).move_to([1, 1.1, 0])

        self.play(Write(rect1))
        plotDotTL(self)

        self.next_slide()
        self.play(Write(rect2))

        plotDotTL(self)
        self.next_slide()

        txt_3 = Tex("""$E':$ Principal Minor """).next_to(m0, DOWN, buff=0.3)
        txt_4 = MathTex(r"\alpha = \beta ", color=RED_B).next_to(txt_3, RIGHT)
        self.play(Write(txt_3))
        self.next_slide()

        self.play(txt_3.animate.shift(LEFT*1.2))
        self.play(Write(txt_4))
        self.next_slide()

        equation = MathTex(
            r"\mathcal{A}[1,2,3,...,\ell', r_1, r_2|1,2,3,...,\ell', c_1, c_2]").next_to(txt_3, DOWN*1.2, buff=0.3).shift(LEFT*2).scale(0.8)
        txt_5 = Tex(" Almost Principal Minor", color=BLUE_B).next_to(
            equation, RIGHT).scale(0.8)

        self.play(Create(equation))

        plotDotTL(self)
        self.next_slide()

        txt_6 = Tex(r"$\{r_1,\: r_2\: |\: c_1,\: c_2\}$ $\Longrightarrow$ Deviations",
                    color=YELLOW).next_to(equation, DOWN).shift(RIGHT*3).scale(0.8)
        self.play(Write(txt_6))
        self.next_slide()

        self.play(Write(txt_5))
        self.next_slide()

        self.play(FadeOut(txt_6), FadeOut(txt_5), FadeOut(equation))

        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{xcolor}")

        # txt_7 = r"""$\alpha = \{ 1, 2, 3, 4, 5, 13, 14 \} \hspace{4ex} \text{and} \hspace{4ex} \beta = \{ 1, 2, 3, 4, 5, 19, 17 \}$"""
        # equation2 = Tex(txt_7, tex_template=myTemplate).next_to(txt_3 , DOWN).scale(0.6)

        txt_7 = Tex(r'Almost Principal Minor - Example').next_to(txt_3,
                                                                 DOWN).scale(0.8).shift(3*LEFT)
        txt_ex1 = MarkupText('Row = { 1, 2, 3, 4, 5, <span foreground="YELLOW">13, 15</span>}     Col =  { 1, 2, 3, 4, 5, <span foreground="YELLOW">17, 19</span>}').next_to(
            txt_7, DOWN).scale(0.4).align_to(txt_7, LEFT)
        txt_ex2 = MarkupText('Row =  {<span foreground="YELLOW">1, 3, </span> 12, 13, 14, 15, 16}     Col =  {12, 13, 14, 15, 16, <span foreground="YELLOW">18, 19</span>} ').next_to(
            txt_ex1, DOWN).scale(0.4).align_to(txt_7, LEFT)
        txt_ex3 = MarkupText('Row/Col =  {1, 2, 3, <span foreground="RED">7, 9,</span> 12, 13, 14,}  - Not an APM').next_to(
            txt_ex2, DOWN).scale(0.4).align_to(txt_ex2, LEFT)

        self.play(Write(txt_7), run_time=0.3)
        self.play(Write(txt_ex1), run_time=0.5)
        plotDotTL(self)

        self.next_slide()
        self.play(Write(txt_ex2), run_time=0.5)
        plotDotTL(self)

        self.next_slide()
        self.play(Write(txt_ex3), run_time=0.5)
        plotDotTL(self)

        self.next_slide()
        self.play(FadeOut(rect1), FadeOut(rect2), FadeOut(txt_7), FadeOut(txt_ex1), FadeOut(
            txt_ex2), FadeOut(txt_ex3), FadeOut(txt_3), FadeOut(txt_4), FadeOut(txt_2), FadeOut(m0), run_time=2)

        txt_8 = Tex(r'- APM advantage', color=BLUE).next_to(txt_1,
                                                            DOWN).align_to(txt_1, LEFT).shift(RIGHT*0.4)
        self.play(Write(txt_8))

        self.next_slide()
        txt_9 = Tex(r'- For 35 bits input , $\mathcal{A}_{105 \times 105}$',
                    color=BLUE_C).next_to(txt_8, DOWN).align_to(txt_8, LEFT)
        txt_10 = Tex(r'- Total Minors : \\ 90,492,479,540,310,008,180,848,641,429,024,900,729,436,748,166,512,078,795,468,413',
                     color=YELLOW).scale(0.6).next_to(txt_9, DOWN, aligned_edge=LEFT)
        txt_11 = Tex(r'- APM : 50,61,21,19,195',
                     color=WHITE).next_to(txt_10, DOWN).align_to(txt_10, LEFT)

        self.play(Write(txt_9))
        self.next_slide()
        self.play(Write(txt_10), run_time=4)
        self.play(Write(txt_11))

        self.next_slide()
        self.play(FadeOut(txt_9), FadeOut(txt_10),
                  FadeOut(txt_11), FadeOut(txt_8))

        txt_12 = Tex(r'Experiment - APM 3D').next_to(txt_1, DOWN).align_to(
            txt_1, LEFT).shift(RIGHT*0.4)
        txt_13 = Tex(r'- Fix Principal Minor size : $2 \times 2$').next_to(txt_12,
                                                                           DOWN).align_to(txt_12, LEFT).align_to(txt_12, LEFT)
        txt_14 = Tex(r'- $\forall$ PM test all 3 deviations').next_to(txt_13,
                                                                      DOWN).align_to(txt_13, LEFT).align_to(txt_13, LEFT)
        txt_15 = Tex(r'- $\mathbb{F}_{35}$ to $\mathbb{F}_{47}$ binary input requires $< 2$ Kernel ',
                     color=BLUE).next_to(txt_14, DOWN).align_to(txt_14, LEFT).align_to(txt_14, LEFT)

        self.play(Write(txt_12))
        self.play(Write(txt_13))
        self.play(Write(txt_14))
        self.play(Write(txt_15))

        self.next_slide()
        image = ImageMobject("img/chart_SIAM_1.png").scale(1.1)
        image.next_to(txt_15, DOWN*1).shift(RIGHT*1.4)
        self.play(FadeIn(image), run_time=3)

        nextScenePause(self)


class def_conclusion8(Slide):
    def construct(self):

        txt_1 = Tex(r"Last Slide : Conclusion").to_edge(UL)
        self.play(Create(txt_1))

        txt_1_1 = Tex(r"- A Zero-Minor in non-singular matrix solves ECDLP",
                      color=BLUE).scale(0.8).next_to(txt_1, DOWN, aligned_edge=LEFT)
        self.play(Write(txt_1_1), run_time=0.5)
        self.next_slide()

        txt10 = Tex(
            r"- Do zero minor exist ?").next_to(txt_1_1, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(Write(txt10), run_time=0.5)

        txt_1_2 = Tex(r"--- GESC and APM-3D show that zero minors exist", color=BLUE).scale(
            0.7).next_to(txt10, DOWN, aligned_edge=LEFT)
        self.play(Write(txt_1_2), run_time=0.5)
        self.next_slide()

        txt20 = Tex(
            r"- How to find a zero minor ?").next_to(txt_1_2, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(Write(txt20), run_time=0.5)

        self.next_slide()
        txt_2 = Tex(r'--- Too many minor : cannot test all of them', color=BLUE).scale(
            0.7).next_to(txt20, DOWN, aligned_edge=LEFT).align_to(txt_1, LEFT)
        self.play(Write(txt_2), run_time=0.5)

        self.next_slide()
        txt_3 = Tex(r'--- Totally positive matrix : Positive determinant for all sub-matrices.').scale(
            0.7).next_to(txt_2, DOWN, aligned_edge=LEFT)
        self.play(Write(txt_3), run_time=0.5)

        self.next_slide()
        txt_4 = Tex(r' --- Test all connected minors that include the first row or column.',
                    color=BLUE).scale(0.7).next_to(txt_3, DOWN, aligned_edge=LEFT)
        self.play(Write(txt_4), run_time=0.5)

        self.next_slide()
        txt_5 = Tex(r' - Initial Minors : A small set of minors that is sufficient to test').scale(0.9).next_to(
            txt_4, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(Write(txt_5), run_time=0.5)

        self.next_slide()
        self.play(FadeOut(txt_2), FadeOut(txt_3), FadeOut(
            txt_4), run_time=1)
        self.play(txt_5.animate.shift(UP*1.6), run_time=0.5)

        txt_6 = Tex(r' Conjecture (Initial Minors) \\ For a matrix $\mathcal{A}$, there exists a set of initial minors, whose cardinality is bounded by a sub-exponential function of the size of the matrix', color=YELLOW).scale(
            0.8).next_to(txt_5, DOWN, buff=0.5).align_to(txt_5, LEFT).shift(RIGHT*0.45)
        self.play(Write(txt_6), run_time=0.5)

        self.next_slide()

        # self.play(txt_6.animate.shift(UP*2.4), run_time=0.5)

        # image = ImageMobject("img/Initial_minors_3.png")
        # image.next_to(txt_1, DOWN*9).shift(RIGHT*5.3).scale(1.1)
        # self.play(FadeIn(image), run_time=3)

        grp_sk = VGroup()
        grp_sk.add(txt_1_1, txt20, txt10, txt_1_2, txt_5)

        txt_con = Tex(
            r' Conjecture (Initial Minors) \\ For a matrix $\mathcal{A}$, there exists a set of \\ initial minors, whose cardinality is bounded \\ by a sub-exponential function of the size \\ of the matrix', color=YELLOW)
        txt_con.scale(0.7).next_to(txt_5, DOWN, aligned_edge=LEFT, buff=1.2)

        trans_con = Transform(txt_6, txt_con)
        self.play(grp_sk.animate.scale(0.9).next_to(
            txt_1, DOWN, aligned_edge=LEFT), trans_con)
        # self.play(trans_con)

        # Create a regular hexagon
        larger_hexagon = RegularPolygon(
            n=6, color=YELLOW_B, fill_opacity=0.5).scale(1.5).next_to(txt_con, RIGHT, buff=1)

        initialMin = Text(r"Initial Minors", color=BLACK,
                          weight=BOLD).scale(0.4)
        initialMin.move_to(larger_hexagon.get_center()+(DOWN/2))

        gesc = Text(r"GESC", color=WHITE, weight=BOLD).scale(0.4)

        # Create a smaller hexagon
        smaller_hexagon = RegularPolygon(
            n=6,  start_angle=47 * DEGREES, color=RED, fill_opacity=0.2).scale(0.7).next_to(txt_con)

        # Calculate the dimensions of the bounding box around the larger hexagon
        width = larger_hexagon.get_width()
        height = larger_hexagon.get_height()

        smaller_hexagon.move_to(larger_hexagon.get_center()+(RIGHT+0.25)+UP/2)
        # smaller_hexagon.move_to((RIGHT+0.25)+UP/2)
        gesc.move_to(smaller_hexagon.get_center())
        gesc.rotate(5)

        # Display the larger and smaller hexagons
        self.play(FadeIn(larger_hexagon), FadeIn(initialMin))

        self.next_slide()
        self.play(Create(smaller_hexagon), FadeIn(gesc))

        circle_radius = smaller_hexagon.get_width()*0.8
        circle = Circle(radius=circle_radius, color=BLUE, fill_opacity=0.3)
        circle.move_to(smaller_hexagon.get_center()+(LEFT/2.6))
        cirText = Text(r"APM", color=WHITE,
                       weight=BOLD).scale(0.4)
        cirText.move_to(circle.get_center()+(UP/1.4))
        self.next_slide()

        self.play(Create(circle), FadeIn(cirText))

        grp_im = VGroup()
        grp_im.add(larger_hexagon, initialMin,
                   smaller_hexagon, gesc, circle, cirText)

        nextScenePause(self)


class def_publication8_1(Slide):
    def construct(self):

        txt0 = Tex(r'Publications, conferences \& workshops').to_edge(
            UP).to_edge(LEFT)
        self.play(FadeIn(txt0))

        # # List of publications
        # publications = [
        #     r"1. \textbf{Ansari Abdullah}, Ayan Mahalanobis, and Vivek M Mallick. A new    method for solving the elliptic curve discrete logarithm problem. Journal of Groups, complexity, cryptology, 12, 2021",
        #     r"2. Mahalanobis Ayan, Mallick Vivek Mohan, and \textbf{Ansari Abdullah}. A las vegas algorithm to solve the elliptic curve discrete logarithm problem. In International Conference on Cryptology in India, pages 215-227. Springer, 2018.",
        #     r"3. \textbf{Ansari Abdullah}, Gajera Hardik, and Mahalanobis Ayan. On improvements of the r-adding walk in a finite field of characteristic 2. Journal of Discrete Mathematical Sciences and Cryptography 19.1 (2016): 13-38.",
        #     r"4. \textbf{Ansari Abdullah}, Using Oblique elimination to solve ECDLP, presented in Second international conference on Modern Computing Trends and Technology - India, 2022.",
        #     r"5. Workshop on - Theory and practive of Side-channel attacks in cryptography by Prof. Chester Rebeiro, IIT Madras.",
        #     r"6. \textbf{Ansari Abdullah}, Ayan Mahalanobis, Minors solve the elliptic curve discrete logarithm problem - Submitted to the Journal of Experimental Mathematics."
        # ]

        # # Create a Text object for each publication
        # publication_texts = [Tex(pub, font_size=10) for pub in publications]

        # # Positioning the Text objects on the screen
        # for i, pub_text in enumerate(publication_texts):
        #     pub_text.next_to(txt0, DOWN, aligned_edge=LEFT)
        #     pub_text.shift(i * 1.4 * DOWN)

        # # Add the Text objects to the scene
        # self.play(*[Write(pub_text) for pub_text in publication_texts])

        image1 = ImageMobject("img/pub_lst.jpg")
        image1.scale(0.9).next_to(txt0, DOWN, aligned_edge=LEFT)
        self.play(FadeIn(image1))
        nextScenePause(self)


class def_questions9(Slide):
    def construct(self):
        txt_1 = Tex(r'Questions ???')
        self.play(FadeIn(txt_1))

        self.next_slide()

        self.play(FadeOut(txt_1), run_time=0.8)
        txt_2 = Tex(r'Thank You !!!')
        self.play(FadeIn(txt_2))

        nextScenePause(self)


class sw(Slide):
    def construct(self):
        # Opening crawl text
        opening_crawl_text = """
        Custom Credits
        Your Name

        Directed by: Director Name
        Produced by: Producer Name
        Music by: Composer Name
        Special Effects: VFX Artist
        Costume Design: Costume Designer
        Editing: Editor Name
        Starring:
          - Actor 1
          - Actor 2
          - Actor 3
          - Actor 4
          - Actor 5
        """

       # Create a text object
        crawl_text = Text(opening_crawl_text, font="Monospace",
                          t2c={"Custom Credits": YELLOW})
        crawl_text.scale(0.7)

        # Set the initial position below the screen
        crawl_text.next_to(ORIGIN, DOWN, buff=0.2)

        # Add the text to the scene and scroll it upwards
        self.play(Write(crawl_text), crawl_text.animate.shift(UP * 10),
                  run_time=len(opening_crawl_text) * 0.04, rate_func=linear)

        # Wait for a moment at the end
        self.wait(2)


class mc(Slide):
    def construct(self):
        # List of text to scroll
        text_list = [
            "Item 1",
            "Item 2",
            "Item 3",
            "Item 4",
            "Item 5",
            "Item 1",
            "Item 2",
            "Item 3",
            "Item 4",
            "Item 5",
            "Item 1",
            "Item 2",
            "Item 3",
            "Item 4",
            "Item 5",
            "Item 1",
            "Item 2",
            "Item 3",
            "Item 4",
            "Item 5",
        ]

        # Create text objects
        text_objects = [Tex(item, font_size=36, color=WHITE)
                        for item in text_list]

        # Arrange text objects in a column
        text_group = VGroup(*text_objects).arrange(DOWN, aligned_edge=LEFT)

        # Set the starting position at the top of the screen
        text_group.move_to(UP * 3)

        # Loop through each text item
        for text_item in reversed(text_objects):
            # Scroll text to the bottom of the screen
            self.play(
                text_group.animate.to_edge(DOWN),
                run_time=2,
                rate_func=rate_functions.ease_in_out_sine,
            )

            # Fade out the current text item
            self.play(
                FadeOut(text_item),
                run_time=0.5,
            )

            # Remove the faded out item from the text group
            text_group.remove(text_item)

        # Wait for a moment at the end
        self.wait(2)


class ms1(Slide):
    def construct(self):
        # Create a text object
        # text = Tex(r"1. \textbf{Ansari Abdullah}, Ayan Mahalanobis, and Vivek M Mallick. A new    method for solving the elliptic curve discrete logarithm problem. Journal of Groups, complexity, cryptology, 12, 2021", font_size=26).shift(UP)

        # text2 = Tex(
        #     r'This is supposed to be a very long sentence so that it is displayed across the screen in maning. lets see if it works. Looks like it is a but something...', font_size=26, size=0.5)

        # # Get the width of the screen
        # screen_width = self.camera.frame_width/1.3

        # # Set the width of the text object to the width of the screen
        # text.set_width(screen_width)

        # # Add the text object to the scene
        # self.add(text)
        # self.play(FadeIn(text), FadeIn(text2))

        long_string = "Problems: First, 'size' changes the spacing between two strings, which it should not. " \
            "Second, when exceeding a specific width (pre-scale), the line is wrapped, which is ok but " \
            "should be configurable."
        self.add(VGroup(Text(long_string, size=0.25), Text(
            long_string).scale(0.25)).arrange(DOWN, aligned_edge=LEFT))

        self.play(FadeIn(long_string))


class pl1(Slide):
    def construct(self):
        txt0 = Tex(r'Publications, conferences \& workshops.').to_edge(
            UP).to_edge(LEFT)
        self.play(FadeIn(txt0))

        p1 = Tex(r"1. \textbf{Ansari Abdullah}, Ayan Mahalanobis, and Vivek M Mallick. A new method for solving the elliptic curve discrete logarithm problem. Journal of Groups, complexity, cryptology, 12, 2021", font_size=24)
        p1.next_to(txt0, DOWN, aligned_edge=LEFT)
        p1.set_width(100)
        self.play(FadeIn(p1))


class bracket(Slide):
    def construct(self):
        # Create a matrix
        matrix = Matrix([
            ["a", "b", "c"],
            ["d", "e", "f"],
            ["g", "h", "i"]
        ])

        # Add the matrix to the scene
        self.play(Create(matrix))

        # Add row and column labels
        row_brace = Brace(matrix, direction=LEFT)
        row_text = row_brace.get_text("Rows")

        col_brace = Brace(matrix, direction=DOWN)
        col_text = col_brace.get_text("Columns")

        # Position row and column labels
        row_brace.next_to(matrix, LEFT, buff=SMALL_BUFF)
        row_text.next_to(row_brace, LEFT, buff=SMALL_BUFF)

        col_brace.next_to(matrix, DOWN, buff=SMALL_BUFF)
        col_text.next_to(col_brace, DOWN, buff=SMALL_BUFF)

        # Add row and column labels to the scene
        self.play(Create(row_brace), Write(row_text))
        self.play(Create(col_brace), Write(col_text))

        # Wait for a moment
        self.wait(2)

        # Remove the matrix, row and column labels from the scene
        self.play(FadeOut(matrix), FadeOut(row_brace), FadeOut(
            row_text), FadeOut(col_brace), FadeOut(col_text))


class cir(Slide):
    def construct(self):
        small_poly = RegularPolygon(n=6).scale(0.7)
        big_poly = RegularPolygon(n=6, start_angle=30 *
                                  DEGREES, color=GREEN).scale(1.4)
        poly_3 = RegularPolygon(n=10, color=RED)

        poly_group = Group(small_poly, big_poly, poly_3).scale(
            1.5).arrange(buff=1)
        self.add(poly_group)
        self.play(FadeIn(small_poly), FadeIn(big_poly), FadeIn(poly_3))

        # Create a circle that encompasses the smaller pentagon
        # circle = Circle(radius=1, color=BLUE, fill_opacity=0.3).shift(
        #     np.array([0, 0, 0]))

        # # Display the larger pentagon, smaller pentagon, and circle
        # self.play(Create(larger_pentagon))
        # self.play(Create(smaller_pentagon))
        # self.play(Create(circle))
        # self.wait(3)


class hex(Slide):
    def construct(self):
        # Create a regular hexagon
        larger_hexagon = RegularPolygon(
            n=6, color=YELLOW_B, fill_opacity=0.5).scale(1.5)

        initialMin = Text(r"Initial Minors", color=BLACK,
                          weight=BOLD).scale(0.4)
        initialMin.move_to(larger_hexagon.get_center()+(DOWN/2))

        gesc = Text(r"GESC", color=WHITE, weight=BOLD).scale(0.4)

        # Create a smaller hexagon
        smaller_hexagon = RegularPolygon(
            n=6,  start_angle=47 * DEGREES, color=RED, fill_opacity=0.2).scale(0.7)

        # Calculate the dimensions of the bounding box around the larger hexagon
        width = larger_hexagon.get_width()
        height = larger_hexagon.get_height()

        smaller_hexagon.move_to((RIGHT+0.25)+UP/2)
        gesc.move_to(smaller_hexagon.get_center())
        gesc.rotate(5)

        # Display the larger and smaller hexagons
        self.play(FadeIn(larger_hexagon), FadeIn(initialMin))

        # self.next_slide()
        self.play(Create(smaller_hexagon), FadeIn(gesc))

        circle_radius = smaller_hexagon.get_width()*0.8
        circle = Circle(radius=circle_radius, color=BLUE, fill_opacity=0.3)
        circle.move_to(smaller_hexagon.get_center()+(LEFT/2.6))
        cirText = Text(r"APM", color=WHITE,
                       weight=BOLD).scale(0.4)
        cirText.move_to(circle.get_center()+(UP/1.4))
        self.play(Create(circle), FadeIn(cirText))


class tmp(Slide):
    def construct(self):

        txt1 = Tex(
            r"\textbf{$\sim$ 5,000,000,000} \\ \textbf{Internet user}", color=YELLOW)
        txt2 = Tex(
            r"\textbf{$\sim$ 14,000,000,000} \\ \textbf{Connected devices}", color=YELLOW)

        self.play(FadeIn(txt1))
        self.next_slide()

        self.play(FadeOut(txt1))
        self.play(FadeIn(txt2))
        self.next_slide()
        self.play(FadeOut(txt2))

        txt_ecdlp = Tex(
            r'\textbf{Elliptic Curve Discrete Logarithm Problem}').scale(1.2)
        self.play(FadeIn(txt_ecdlp))
        self.next_slide()
        self.play(txt_ecdlp.animate.shift(DOWN*1.8))

        img_whatsApp = ImageMobject(
            "img/WhatsApp.png").scale(0.7).shift(UP)
        txt_app1 = Tex(r'WhatsAPP \\ End to End \\ encryption',
                       color=GREEN_D).next_to(img_whatsApp, DOWN)

        self.play(FadeIn(img_whatsApp), FadeIn(txt_app1))
        self.next_slide()

        self.play(txt_app1.animate.shift(LEFT*5),
                  img_whatsApp.animate.shift(LEFT*5))

        img_UPI = ImageMobject(
            "img/UPI-Logo-vector_2.png").scale(0.7).shift(UP)
        txt_app2 = Tex(r'UPI \\ Google Pay \\ PhonePe',
                       color=BLUE_B).next_to(txt_app1, RIGHT, buff=1).next_to(img_UPI, DOWN)
        self.play(FadeIn(txt_app2), FadeIn(img_UPI))

        self.next_slide()
        self.play(txt_app2.animate.shift(LEFT*1.7),
                  img_UPI.animate.shift(LEFT*1.7))

        img_bitEth = ImageMobject(
            "img/bitEth.png").scale(0.2).next_to(img_UPI, RIGHT, buff=0.8)
        txt_app3 = Tex(r'Crypto \\ Curriencies',
                       color=YELLOW_A).next_to(img_bitEth, DOWN)
        self.play(FadeIn(txt_app3), FadeIn(img_bitEth))

        self.next_slide()

        txt_TLS = Tex(r"SSL/TLS").scale(1.3).next_to(img_bitEth,
                                                     RIGHT, buff=1)
        txt_Https = Tex(r'HTTPS \\ Email \\ etc...',
                        color=BLUE).next_to(txt_TLS, DOWN)
        self.play(FadeIn(txt_Https), FadeIn(txt_TLS))
        self.next_slide()

        grp = Group()
        grp.add(img_whatsApp, txt_app1, img_UPI, txt_app2,
                img_bitEth, txt_app3, txt_TLS, txt_Https)
        # self.play(grp.animate.shift(UP).shift(LEFT*0.4).scale(0.9))

        self.play(FadeOut(grp))
        self.play(txt_ecdlp.animate.scale(0.6).to_edge(UL), run_time=0.7)
