import numpy as n
import matplotlib.pyplot as p

# Days
day1 = n.arange(0, 120.01, .01)
day2 = n.arange(0, 125, 5)

# Fitting to a logistic curve
total_cases1 = (sat_level*av**(30))/(1+n.exp(-0.1*day1+exponent*60))
new_cases1 = n.gradient(total_cases1, day1)
total_cases2 = (sat_level*av**(30))/(1+n.exp(-0.1*day2+exponent*60))
new_cases2 = n.gradient(total_cases2, day2)

# Transforming the number of cases to integer values
z = []
for i in range(len(new_cases2)):
    z.append(int(new_cases2[i]))
new_cases = n.array(z)

actual = n.array([16, 40, 30, 14, 46, 29, 9, 33, 39, 36, 54, 39, 41, 40, 33, 47])
day = n.arange(1, len(actual)+1, 1)

# Plotting
p.plot(day1, new_cases1, "--b", label = "Expected Daily New Cases")
p.plot(day2, new_cases, "Dg")
p.plot(day, actual, "Dr", label = "Actual Daily New Cases")

# Writing the number of cases on the plot
for i, text in enumerate(new_cases):
    p.annotate(text, (day2[i], new_cases[i]), textcoords = "offset points", xytext = (0, 10), ha = "center")

p.legend()
p.grid("on")
p.xlabel("Days Since 15 March")
p.xticks(range(0, 125, 5))

p.show()
