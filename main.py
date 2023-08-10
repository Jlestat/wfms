def closest_mod_5(x):
    y = x
    while y > 0:
        if y % 5 == 0:
            return y
        y += 1


print(closest_mod_5(7))
