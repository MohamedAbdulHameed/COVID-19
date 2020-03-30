import numpy as n
import matplotlib.pyplot as p
from scipy.optimize import curve_fit

# Fitting to an exponential model
def exponential(x, a, b):
    return a*n.exp(b*x)

# Fitting to a 2nd degree polynomial
def polynomial(x, a, b, c):
    return a*x**2+b*x+c

def logistic(x, a, b, c):
    return a/(1+n.exp(-b*(x-c)))

# Current cases
cases = n.array([126, 166, 196, 210, 256, 285, 294, 327, 366, 402, 456, 495, 536, 576, 609]) # For each new day, add the number of cases for that day to this array.
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
past_expectations = n.array([1144, 930, 709, 902, 910, 809, 867, 948, 1008, 1139, 1071, 1265, 1324, 1357]) # Data are input from the Google Sheets Analysis
day_past_exp = n.arange(9, len(past_expectations)+9, 1)

# Curve fitting
fit_parameters1, covariances = curve_fit(exponential, day, cases) # Fitting current cases
fit_parameters2, covariances = curve_fit(polynomial, day_past_exp, past_expectations) # Fitting cases expected a week earlier
fit_parameters3, covariances = curve_fit(exponential, day_past_exp, past_expectations) # Fitting cases expected a week earlier
fit_parameters4, covariances = curve_fit(logistic, day, cases) # Fitting current cases

# R-squared calculation
correlation_matrix1 = n.corrcoef(day, exponential(day, *fit_parameters1))
correlation_matrix2 = n.corrcoef(day_past_exp, polynomial(day_past_exp, *fit_parameters2))
correlation_matrix3 = n.corrcoef(day_past_exp, exponential(day_past_exp, *fit_parameters3))
correlation_matrix4 = n.corrcoef(day, logistic(day, *fit_parameters4))

correlation_xy1 = correlation_matrix1[0, 1]
correlation_xy2 = correlation_matrix2[0, 1]
correlation_xy3 = correlation_matrix3[0, 1]
correlation_xy4 = correlation_matrix4[0, 1]

r_sq1 = correlation_xy1**2
r_sq2 = correlation_xy2**2
r_sq3 = correlation_xy3**2
r_sq4 = correlation_xy4**2


a = p.subplot() # Was called because it has the ability to delete top and right frameline from the plot

# Constructing lists to be used for the plot legend
FP1 = list(fit_parameters1)
FP2 = list(fit_parameters2)
FP3 = list(fit_parameters3)
FP4 = list(fit_parameters4)

FP1.append(r_sq1)
FP2.append(r_sq2)
FP3.append(r_sq3)
FP4.append(r_sq4)

# Plotting current cases
a.plot(day, cases, "Dr")
a.plot(day, exponential(day, *fit_parameters1), "--b", label = "Current Model: %.1f $e^{%.2f}$ ($R^{2}$ = %.4f)" % tuple(FP1))
a.plot(day, logistic(day, *fit_parameters4), "--b", label = "Current Model: %.2f/(1 + $e^{-%.2f (x - %.2f)}$) ($R^{2}$ = %.4f)" % tuple(FP4))


# Plotting cases expected a week later
a.plot(day_model, case_model, ":b", label = "Average Multiplication Factor = %.2f" %av)

# Plotting cases expected a week earlier
a.plot(day_past_exp, past_expectations, "Dg")
a.plot(day_past_exp, polynomial(day_past_exp, *fit_parameters2), "--c", label = "Expected Cases a Week Earlier: %.1f $x^{2}$ + %.1f x + %.1f ($R^{2}$ = %.4f)" % tuple(FP2))
a.plot(day_past_exp, exponential(day_past_exp, *fit_parameters3), "--r", label = "Expected Cases a Week Earlier: %.1f $e^{%.2f}$ ($R^{2}$ = %.4f)" % tuple(FP3))


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

# Deleting the top and right framelines
a.spines['right'].set_visible(False)
a.spines['top'].set_visible(False)

# Forcing the x-axis to integers
p.xticks(range(1, len(cases)+9))

p.show()
