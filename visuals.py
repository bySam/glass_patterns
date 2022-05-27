from manim import * 
from math import sqrt
import shapes

class GlassDisplay(Scene):
    def construct(self):

        n = int(input("Which number do you wish to test? "))

        for solution in shapes.general_search(n)[:3]:   #First three ("best") solutions.
                                                        #
            print(solution)
            if solution[0] == 'triangle':
                text = Text("Triangle with rows: 1, 2, ..., ")
                glasses = self.triangle(solution[1])
                self.play(Create(glasses))
                self.play(Write(text))
                self.wait(5)
                self.remove(glasses)

            if solution[0] == 'square':
                self.add(self.square(solution[1]))

    def square(self, n):
        glasses = VGroup(*[Circle(radius=0.25) for _ in range(n)])
        glasses.arrange_in_grid(int(sqrt(n)),int(sqrt(n)))
        return glasses

    def triangle(self, n):
        row = 1
        glasses = VGroup()

        while row <= shapes.triangle_number(n)[1]:
            for i in VGroup(*[Circle(radius=0.25) for item in range(row)]).arrange().shift(DOWN*(row-(shapes.triangle_number(n)[1]+1)/2)*0.8):
                glasses.add(i)
            row += 1


        return glasses
