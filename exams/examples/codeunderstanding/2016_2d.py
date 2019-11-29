
def f(x):
    y = 0
    while x > 0:
        y = y + x % 10
        x = int( x / 10 )
    if y >= 10:
        y = f( y )
    return y

print( f(32145) )
