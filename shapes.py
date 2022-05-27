#"Discriminant" is loosely used to mean x in sqrt(x), despite this not being the correct term.

from math import sqrt

def triangle_number(n):
    discriminant = (1/2)**2+2*n

    if discriminant > 0: #We don't want to take sqrt() of a negative number - that causes an error!
        if -(1/2)+sqrt(discriminant) > 0 and (-(1/2)+sqrt(discriminant)).is_integer(): #is solution a natural number?
            return (True,-(1/2)+sqrt(discriminant)) #n is a triangle number then! Returns: (True, the solution)
    return (False,None)

def square_number(n): #Note: square numbers are also "rhombus" numbers. ie: two triangles that share the long row
    if n > 0: #We don't want to take sqrt() of a negative number - that causes an error!
        if (sqrt(n)).is_integer(): #is solution a natural number?
            return (True,sqrt(n)) #n is a square number then! Returns: (True, the solution)
    return (False,None)

def pentagonal_number(n): #https://en.wikipedia.org/wiki/Pentagonal_number#Tests_for_pentagonal_numbers
    discriminant = 24*n+1

    if discriminant > 0: #We don't want to take sqrt() of a negative number - that causes an error!
        if ((sqrt(discriminant)+1)/6).is_integer(): #is solution a natural number?
            return (True,(sqrt(discriminant)+1)/6) #n is a pentagonal number then! Returns: (True, the solution)
    return (False,None)

def bow_tie(n): #Two triangles with a shared middle-point.
    discriminant = (1/2)**2+n+1

    if discriminant > 0: #We don't want to take sqrt() of a negative number - that causes an error!
        if (-(1/2)+sqrt((1/2)**2+n+1)).is_integer(): #is solution a natural number?
            return (True,-(1/2)+sqrt((1/2)**2+n+1)) #n is a bow_tie-number then! Returns: (True, the solution)
    return (False,None)

def factors(n):
    return set(
        factor for i in range(1, int(sqrt(n)) + 1) if n % i == 0
        for factor in (i, n//i)
    )

def general_search(n):
    suggestions = []
    for factor in factors(n):
        #For each suggestion found, it appends: (type, factor, solution)
        #solutions can be: triangle longest row, square side length, etc.
        #it also needs to append "multiple". ie: if a solution is two triangles, for example - this is not yet done.

        if triangle_number(factor)[0]: #if True
            suggestions.append(("triangle",factor,triangle_number(factor)[1]))

        if square_number(factor)[0]: #if True
            suggestions.append(("square",factor,square_number(factor)[1]))

        if bow_tie(factor)[0]: #if True
            suggestions.append(("bowtie",factor,bow_tie(factor)[1]))

        if square_number(factor-2): #if True
            suggestions.append(("rhombus+2",factor,square_number(factor-2)[1])) #Remember: square+2 = rhombus+2


        if factor >= 0.2*n and factor <= 0.8*n and n/factor >= 0.2*n and n/factor <= 0.8*n: #can be made much nicer
                                                                                            #checks for rectangles where no side is extremely long or short.
            suggestions.append(("rectangle",factor,n/factor))


    return sorted(suggestions,key=lambda x: x[1], reverse=True) #Returns the solutions sorted by factor size
                                                                #So a solution with "size" 20 is prefered over two solutions with "size" 10, etc.