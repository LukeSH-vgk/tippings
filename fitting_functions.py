def linear(m, x, b):
    return m*x+b

def slope_units(x_units,Y_units):
    a = Y_units + "/" + x_units
    return a

def print_equ(m,b,x_units,y_units):
    print("y =",m, slope_units(x_units,y_units), "x +", b , y_units)
