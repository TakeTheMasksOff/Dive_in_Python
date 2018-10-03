def quadratic_equation_roots(a,b,c):
    discriminant = b ** 2 - 4 * a * c 
    print (discriminant)
    x1 = (- b - discriminant ** (1 / 2)) / (2 * a)
    x2 = (- b + discriminant ** (1 / 2)) / (2 * a)
    # print ("x1 = ",  x1)
    # print ("x2 = ",  x2)
    print (f"x1 = {x1:.0f}")
    print (f"x2 = {x2:.0f}")
