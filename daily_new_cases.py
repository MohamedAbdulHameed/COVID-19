import numpy as n
import matplotlib.pyplot as p
from statistical_model import exponent

# Days
day1 = n.arange(0, 150.01, .01)
day2 = n.arange(0, 155, 5)

# Fitting to a logistic curve
total_cases1 = (70000)/(1+n.exp(-0.1*day1+exponent*70)) # Assumption: a satuaration number of 70000 cases is reached in 5 months.
new_cases1 = n.gradient(total_cases1, day1)
total_cases2 = (70000)/(1+n.exp(-0.1*day2+exponent*70))
new_cases2 = n.gradient(total_cases2, day2)

# Transforming the number of cases to integer values
z = []
for i in range(len(new_cases2)):
    z.append(int(new_cases2[i]))
new_cases = n.array(z)

actual = n.array([16, 40, 30, 14, 46, 29, 9, 33, 39, 36, 54, 39, 41, 40, 33, 47, 54, 69, 86, 120, 85, 103, 149])
day = n.arange(1, len(actual)+1, 1)

a = p.subplot()

# Plotting
a.plot(day1, new_cases1, "--b", label = "Expected Daily New Cases")
a.plot(day2, new_cases, "Dg")
a.plot(day, actual, "Dr", label = "Actual Daily New Cases")

# Writing the number of cases on the plot
for i, text in enumerate(new_cases):
    p.annotate(text, (day2[i], new_cases[i]), textcoords = "offset points", xytext = (0, 10), ha = "center")

p.legend()
p.grid("on")
p.xlabel("Days Since 15 March")
p.xticks(range(0, 155, 5))

# Deleting the top and right framelines
a.spines['right'].set_visible(False)
a.spines['top'].set_visible(False)

p.show()
