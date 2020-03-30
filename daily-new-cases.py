import numpy as n
import matplotlib.pyplot as p

# Days
x1 = n.arange(0, 120.01, .01)
x2 = n.arange(0, 125, 5)

# Fitting to a logistic curve
z1 = 15000/(1+n.exp(-0.1*x1+exponent*60)) # Run statistical-model.py first in the same kernel to get the value of "exponent".
z2 = n.gradient(z1, x1)
z3 = 15000/(1+n.exp(-0.1*x2+exponent*60))
z4 = n.gradient(z3, x2)

z5 = []
for i in range(len(z4)):
    z5.append(int(z4[i]))
z6 = n.array(z5)

actual = n.array([16, 40, 30, 14, 46, 29, 9, 33, 39, 36, 54, 39, 41, 40, 33, 47])
day = n.arange(1, len(actual)+1, 1)

# Plotting
p.plot(x1, z2, "--b", label = "Expected Daily New Cases")
p.plot(x2, z6, "Dg")
p.plot(day, actual, "Dr", label = "Actual Daily New Cases")

# Writing the number of cases on the plot
for i, text in enumerate(z6):
    p.annotate(text, (x2[i], z4[i]), textcoords = "offset points", xytext = (0, 10), ha = "center")

p.legend()
p.grid("on")
p.xlabel("Days Since 15 March")
p.xticks(range(0, 125, 5))

p.show()
