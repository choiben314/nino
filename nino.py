import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("./data/elnino.csv")

df.columns = [col.strip() for col in df.columns]

# df['Air Temp'] = pd.to_numeric(df['Air Temp'], errors = 'coerce')
# df['Sea Surface Temp'] = pd.to_numeric(df['Sea Surface Temp'], errors = 'coerce')

df['Zonal Winds'] = pd.to_numeric(df['Zonal Winds'], errors = 'coerce')
df['Meridional Winds'] = pd.to_numeric(df['Meridional Winds'], errors = 'coerce')

sns.jointplot(x="Zonal Winds", y="Meridional Winds", data = df, height = 7)

plt.show()

# print(df.describe())