from manimlib.imports import*

class Square(Scene):

    def construct(self):
        circle = Circle(radius = 2 , color = ORANGE)

        horizontalLines = []
        for i in range(5):
            horizontalLine = Line(np.array([-2.5,0,0]),np.array([2.5,0,0])).shift(UP*2)
            horizontalLine.set_color(BLUE_D)
            horizontalLine.shift(DOWN*i*1)
            horizontalLines.append(horizontalLine)

        verticalLines = []
        for j in range(5):
            verticalLine = Line(np.array([0,2.5,0]) , np.array([0,-2.5,0])).shift(LEFT*2)
            verticalLine.set_color(BLUE_D)
            verticalLine.shift(RIGHT * j * 1)
            verticalLines.append(verticalLine)


        self.play(FadeIn(circle))
        self.wait(2.5)
        self.play(*[FadeIn(h) for h in horizontalLines[0:5]],*[FadeIn(v) for v in verticalLines[0:5]])
        self.wait(4)


        #使网格线变密，从间隔1到间隔0.5，圆形的直径是2
        horizontalLine1 = []
        for i in range(10):
            horizontalLine = Line(np.array([-2.5,0,0]),np.array([2.5,0,0])).shift(UP*2)
            horizontalLine.set_color(BLUE_D)
            horizontalLine.shift(DOWN*i*0.5)
            horizontalLine1.append(horizontalLine)

        verticalLines = []
        for j in range(10):
            verticalLine = Line(np.array([0,2.5,0]) , np.array([0,-2.5,0])).shift(LEFT*2)
            verticalLine.set_color(BLUE_D)
            verticalLine.shift(RIGHT * j * 0.5)
            verticalLines.append(verticalLine)

        self.play(*[FadeIn(h) for h in horizontalLine1[0:9]],*[FadeIn(v) for v in verticalLines[0:9]])
        self.wait(4)


        #使网格线变密，从间隔0.5到间隔0.25，圆形的直径是2
        horizontalLine2 = []
        for i in range(18):
            horizontalLine1 = Line(np.array([-2.5,0,0]),np.array([2.5,0,0])).shift(UP*2)
            horizontalLine1.set_color(BLUE_D)
            horizontalLine1.shift(DOWN*i*0.25)
            horizontalLine2.append(horizontalLine1)

        verticalLines = []
        for j in range(18):
            verticalLine = Line(np.array([0,2.5,0]) , np.array([0,-2.5,0])).shift(LEFT*2)
            verticalLine.set_color(BLUE_D)
            verticalLine.shift(RIGHT * j * 0.25)
            verticalLines.append(verticalLine)

        self.play(*[FadeIn(h) for h in horizontalLine2[0:17]],*[FadeIn(v) for v in verticalLines[0:17]])
        self.wait(4)

class Pi(Scene):

    def construct(self):
        Basecircle = Circle(radius = 2 , color = ORANGE)
        InscribedSquare = Square(side_length = 2.8 , color = GREEN_D)                   #圆内接正方形
        SircunscribedSquare = Square(side_length = 4 , color = BLUE_D)                  #圆外切正方形

        InscribedPolygon6 = RegularPolygon(n = 6 , color = GREEN).scale(1.98)           #圆内切正六边形
        SircunscribedPolygon6 = RegularPolygon(n = 6 ).scale(2.35)                      #圆外接正六边形

        InscribedPolygon8 = RegularPolygon(n=8 , color = GREEN).scale(1.98)              # 圆内切正八边形
        SircunscribedPolygon8 = RegularPolygon(n=8).scale(2.2)                           # 圆外接正八边形

        InscribedPolygon12 = RegularPolygon(n=12 , color = GREEN).scale(1.98)            # 圆内切正八边形
        SircunscribedPolygon12 = RegularPolygon(n=12).scale(2.1)                         # 圆外接正八边形

        four = TexMobject(" 2.828 <\\pi < 4").next_to(Basecircle , DOWN , buff = 1)
        four[0][0].set_color(GREEN_D)
        four[0][1].set_color(GREEN_D)
        four[0][2].set_color(GREEN_D)
        four[0][3].set_color(GREEN_D)
        four[0][4].set_color(GREEN_D)
        four[0][6].set_color(ORANGE)
        four[0][8].set_color(BLUE_D)

        six = TexMobject(" 3 <\\pi< 3.464").next_to(Basecircle , DOWN , buff = 1)
        six[0][0].set_color(GREEN_D)
        six[0][2].set_color(ORANGE)
        six[0][4].set_color(BLUE_D)
        six[0][5].set_color(BLUE_D)
        six[0][6].set_color(BLUE_D)
        six[0][7].set_color(BLUE_D)
        six[0][8].set_color(BLUE_D)

        eight = TexMobject(" 3.061 < \\pi < 3.313").next_to(Basecircle , DOWN , buff = 1)
        eight[0][0].set_color(GREEN_D)
        eight[0][1].set_color(GREEN_D)
        eight[0][2].set_color(GREEN_D)
        eight[0][3].set_color(GREEN_D)
        eight[0][4].set_color(GREEN_D)
        # eight[0][5].set_color(BLUE_D)
        eight[0][6].set_color(ORANGE)
        eight[0][8].set_color(BLUE_D)
        eight[0][9].set_color(BLUE_D)
        eight[0][10].set_color(BLUE_D)
        eight[0][11].set_color(BLUE_D)
        eight[0][12].set_color(BLUE_D)


        twelve = TexMobject(" 3.105 < \\pi < 3.215").next_to(Basecircle , DOWN , buff = 1)
        twelve[0][0].set_color(GREEN_D)
        twelve[0][1].set_color(GREEN_D)
        twelve[0][2].set_color(GREEN_D)
        twelve[0][3].set_color(GREEN_D)
        twelve[0][4].set_color(GREEN_D)
        # twelve[0][5].set_color(BLUE_D)
        twelve[0][6].set_color(ORANGE)
        twelve[0][8].set_color(BLUE_D)
        twelve[0][9].set_color(BLUE_D)
        twelve[0][10].set_color(BLUE_D)
        twelve[0][11].set_color(BLUE_D)
        twelve[0][12].set_color(BLUE_D)


        self.play(FadeIn(Basecircle))
        self.wait(1)

        self.play(FadeIn(InscribedSquare))
        self.wait(1)

        self.play(FadeIn(SircunscribedSquare))
        self.wait(2)

        self.play(FadeIn(four))                                                                 #显示圆周率区间
        self.wait(4)

        self.play(ReplacementTransform(InscribedSquare,InscribedPolygon6) , run_time = 2)            #4边变6边
        self.wait(2)
        self.play(ReplacementTransform(SircunscribedSquare,SircunscribedPolygon6) , run_time = 2)
        self.play(ReplacementTransform(four, six))
        self.wait(4)


        self.play(ReplacementTransform(InscribedPolygon6, InscribedPolygon8), run_time=2)            #6边变8边
        self.wait(2)
        self.play(ReplacementTransform(SircunscribedPolygon6, SircunscribedPolygon8), run_time=2)
        self.play(ReplacementTransform(six, eight))
        self.wait(4)
        #
        self.play(ReplacementTransform(InscribedPolygon8, InscribedPolygon12), run_time=2)            #8边变12边
        self.wait(2)
        self.play(ReplacementTransform(SircunscribedPolygon8, SircunscribedPolygon12), run_time=2)
        self.play(ReplacementTransform(eight, twelve))
        self.wait(4)
