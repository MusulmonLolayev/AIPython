def Max(*params):
    m = params[0]
    for item in params:
        if item > m:
            m = item
    return m

print(Max(5))
print(Max(5, 9))
print(Max(5, -8, 8))