import math

def find_roots(a, b, c):
    square = (b*b) - (4*a*c)
    pre_root = math.sqrt(square)
    root1 = ((-b)-pre_root)/(2*a)
    root2 = ((-b)+pre_root)/(2*a)

    return root1, root2

print(find_roots(2, 10, 8));