import numpy as n
import matplotlib.pyplot as p
from scipy.optimize import curve_fit

def exponential(x, a, b):
    return a*n.exp(b*x)

cases = n.array([126, 166, 196, 210, 256, 285, 294, 327, 366, 402, 456, 495]) # For each new day, add the number of cases for that day to this array.
day = n.arange(1, len(cases)+1, 1)

z = []
for i in range(len(cases)-1):
    z.append(cases[i+1]/cases[i])
mult = n.array(z)
av = n.average(mult)

u = [cases[len(cases)-1]]
for i in range(6):
    u.append(u[i]*av)
case_model = n.array(u)
day_model = n.arange(len(cases), len(cases)+7, 1)

FP, COV = curve_fit(exponential, day, cases)

a = p.subplot()

a.plot(day, exponential(day, *FP), "--b", label = "%.1f $e^{%.2f}$" % tuple(FP))
a.plot(day, cases, "Dr")
a.plot(day_model, case_model, ":b", label = "Average Multiplication Factor = %.2f" %av)
p.legend()
p.xlabel("Day")
p.ylabel("Confirmed Cases")
p.title("COVID-19 in Egypt")
p.grid("on")

for i, text in enumerate(cases):
    p.annotate(text, (day[i], cases[i]), textcoords = "offset points", xytext = (0, 10), ha = "center")

p.annotate(str(int(round(case_model[6]))), (day_model[6], case_model[6]), textcoords = "offset points", xytext = (0, 10), ha = "center")

a.spines['right'].set_visible(False)
a.spines['top'].set_visible(False)

p.xticks(range(1, len(cases)+8))

p.show()
