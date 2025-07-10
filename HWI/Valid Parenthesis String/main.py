def fun(s, i, c):
    if c < 0:
        return False
    elif i == len(s) - 1 and c == 0:
        return True
    elif i == len(s):
        return c == 0
    elif s[i] == '(':
        return fun(s, i + 1, c + 1)
    elif s[i] == ')':
        return fun(s, i + 1, c - 1)
    elif s[i] == '*':
        return fun(s, i + 1, c + 1) or fun(s, i + 1, c - 1) or fun(s, i + 1, c)
s = "(())"
print(fun(s, 0, 0))