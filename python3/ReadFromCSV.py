import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import style

style.use("ggplot")
df = pd.read_csv("C:\\Users\Test\Desktop\SalesData.csv")
x = df["SalesID"].as_matrix()
y = df["ProductPrice"].as_matrix()
plt.xlabel("SalesID")
plt.ylabel("ProductPrice")
plt.title("Sales Analysis")
plt.plot(x, y)
plt.show()
