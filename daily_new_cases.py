import numpy as n
import matplotlib.pyplot as p
from datetime import date, timedelta
from statistical_model import exponent, av


# Days
day1 = n.arange(0, 160.01, .01)
day2 = n.arange(0, 170, 10)

# Fitting to a logistic curve
total_cases1 = (80000)/(1+n.exp(-0.1*day1+exponent*75)) # Assumption: a satuaration number of 100000 cases is reached in 5 months.
new_cases1 = n.gradient(total_cases1, day1)
total_cases2 = (80000)/(1+n.exp(-0.1*day2+exponent*75))
new_cases2 = n.gradient(total_cases2, day2)

# Transforming the number of cases to integer values
z = []
for i in range(len(new_cases2)):
    z.append(int(new_cases2[i]))
new_cases = n.array(z)

actual = n.array([16, 40, 30, 14, 46, 29, 9, 33, 39, 36, 54, 39, 41, 40, 33, 47, 54, 69, 86, 120, 85, 103, 149, 128, 110, 139, 95, 145])
day = n.arange(1, len(actual)+1, 1)

fig, a = p.subplots()
fig.canvas.draw()

# Plotting
a.plot(day1, new_cases1, "--b", label = "Expected Curve")
#a.plot(day2, new_cases2, "og")
a.plot(day, actual, "Dr", label = "Actual Daily New Cases")
a.plot([], [], " ", label = "Average Multiplication Factor = %.2f" %av)

# Writing the number of cases on the plot
#for i, text in enumerate(new_cases):
#    p.annotate(text, (day2[i], new_cases[i]), textcoords = "offset points", xytext = (0, 10), ha = "center")

p.legend()
p.title("Egypt's COVID-19 Curve\nAssumption: 80,000 cases in 5 months")
p.grid("off")
p.xticks(range(0, 170, 10))

# Writing dates on the x-axis

labels = []
start_date = date(2020, 3, 15)
end_date = date(2020, 8, 15)
delta = timedelta(days = 10)

while start_date <= end_date:
    for i in range(0, 170, 10):
        labels.append(start_date.strftime("%d-%m"))
        start_date += delta

a.set_xticklabels(labels)

# Deleting the top and right framelines
a.spines['right'].set_visible(False)
a.spines['top'].set_visible(False)

p.show()
