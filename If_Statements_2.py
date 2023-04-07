def maximum(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
result = maximum(509, 500, 90)
print(result)

