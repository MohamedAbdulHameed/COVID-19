import numpy as n
import matplotlib.pyplot as p
from scipy.optimize import curve_fit

# Fitting to an exponential-growth model
def exponential(x, a, b):
    return a*n.exp(b*x)

# Current cases
cases = n.array([126, 166, 196, 210, 256, 285, 294, 327, 366, 402, 456, 495, 536]) # For each new day, add the number of cases for that day to this array.
day = n.arange(1, len(cases)+1, 1)

# Expectations a week later
z = []
for i in range(len(cases)-1):
    z.append(cases[i+1]/cases[i])
mult = n.array(z)
av = n.average(mult)

u = [cases[len(cases)-1]]
for i in range(7):
    u.append(u[i]*av)
case_model = n.array(u)
day_model = n.arange(len(cases), len(cases)+8, 1)

# Expectations a week earlier
past_expectations = n.array([1144, 930, 709, 902, 910]) # Data are input from the Google Sheets Analysis
day_past_exp = n.arange(9, len(past_expectations)+9, 1)

# Curve fitting
fit_parameters1, covariances = curve_fit(exponential, day, cases) # Fitting current cases
fit_parameters2, covariances = curve_fit(exponential, day_past_exp, past_expectations) # Fitting cases expected a week earlier

a = p.subplot() # Was called because it has the ability to delete top and right frameline from the plot

# Plotting current cases
a.plot(day, exponential(day, *fit_parameters1), "--b", label = "Current Model: %.1f $e^{%.2f}$" % tuple(fit_parameters1))
a.plot(day, cases, "Dr")

# Plotting cases expected a week later
a.plot(day_model, case_model, ":b", label = "Average Multiplication Factor = %.2f" %av)

# Plotting cases expected a week earlier
a.plot(day_past_exp, past_expectations, "Dg")
a.plot(day_past_exp, exponential(day_past_exp, *fit_parameters2), "--c", label = "Expected Cases a Week Earlier: %.1f $e^{%.2f}$" % tuple(fit_parameters2))

p.legend()
p.xlabel("Day")
p.ylabel("Confirmed Cases")
p.title("COVID-19 in Egypt")
p.grid("on")

# Writing the number of cases above points
for i, text in enumerate(cases):
    p.annotate(text, (day[i], cases[i]), textcoords = "offset points", xytext = (0, 10), ha = "center")

for i, text in enumerate(past_expectations):
    p.annotate(text, (day_past_exp[i], past_expectations[i]), textcoords = "offset points", xytext = (0, 10), ha = "center")

# Writing the number of cases expected a week later
p.annotate(str(int(round(case_model[7]))), (day_model[7], case_model[7]), textcoords = "offset points", xytext = (0, 10), ha = "center")

# Deleting the top and right framelines
a.spines['right'].set_visible(False)
a.spines['top'].set_visible(False)

# Forcing the x-axis to integers
p.xticks(range(1, len(cases)+9))

p.show()
