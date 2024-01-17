# from matplotlib import pyplot as plt
import matplotlib.pyplot as plt

x=[12,13,14,23,26,34,38,39,40,46]
y=[33465,12234,767,8453,786,4546,352525,898967,786574,3252352,]

plt.plot(x,y)
plt.xlabel("Ages")
plt.ylabel("Median salary(USD)")
plt.title("salaries by ages")
plt.show()