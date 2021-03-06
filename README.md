# glass_patterns
Suggest shapes to place pre-drink glasses in.
Renders solutions with manim; installation docs here: https://docs.manim.community/en/stable/installation/windows.html

Program is run with: ``manim visuals.py`` 

# Priority to-do:

- Proper support for multiple shapes (as in: 2 triangles, f.e.)
- Add visualisation for all current base shapes

# Current base shapes:

**triangle_number(n):**

$(-\frac{1}{2}+\sqrt{\frac{1}{2}^2+2\cdot n}) \in \mathbb{N}?$ 

**square number(n):**

$(\sqrt{n}) \in \mathbb{N}?$

**pentagonal number(n)**:

$(\frac{\sqrt{24\cdot n + 1}+1}{6}) \in \mathbb{N}?$

**bow_tie(n)**:

$(-\frac{1}{2}+\sqrt{\frac{1}{2}^2+n+1}) \in \mathbb{N}?$
