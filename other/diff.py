with open("../nouns/final.txt") as f:
    x = f.read()
with open("../nouns/nouns.txt") as f:
    y = f.read()
y = y.split("^")
y = "".join(y)

# x y compare them
y = y.split("\n")
y = list(sorted(y))
x = list(sorted(x.split("\n")))
lx = len(x)

"""
for i in range(lx):
    if y[i] != x[i]:
        print(y[i], x[i])
"""

print("\n".join(y))
print("-----------")
print("\n".join(x))
