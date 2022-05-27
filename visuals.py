from visuals import * 
from math import sqrt
import shapes

class OpeningManim(Scene):
    def construct(self):
        self.add(self.triangle(15))
    

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
