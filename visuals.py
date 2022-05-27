from manim import * 
from math import sqrt
import shapes

class GlassDisplay(Scene):
    def construct(self):

        x = int(input("Which number do you wish to test? "))

        for solution in shapes.general_search(x)[:3]:   #First three ("best") solutions.
                                                        #
            print(solution)
            if solution[0] == 'triangle':
                text = Text("Triangle with rows: 1, 2, ... , " + str(int(solution[2]))).shift(UP*3)
                glasses = self.triangle(solution[1])

                self.play(Write(text))
                self.play(Create(glasses))
                self.wait(3)
                self.remove(glasses)
                self.remove(text)

            if solution[0] == 'square':
                text = Text("Square with side length: " + str(int(solution[2]))).shift(UP*3) 
                glasses = self.square(solution[1])

                self.play(Write(text))
                self.play(Create(glasses))
                self.wait(3)
                self.remove(glasses)
                self.remove(text)

            

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
