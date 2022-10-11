import pandas as pd
import numpy as np


csv_data = pd.read_csv('2018_centralpark_data.csv')

gray = csv_data['Primary Fur Color'].value_counts()['Gray']
red = csv_data['Primary Fur Color'].value_counts()['Cinnamon']
black = csv_data['Primary Fur Color'].value_counts()['Black']

data = {'Fur Color': ['Gray', 'Red', 'Black'], 'Count': [gray, red, black]}

df = pd.DataFrame.from_dict(data)
df.to_csv('squirrel_count.csv')


# output_csv = pd.to_csv('squirrel_countl.csv')

# data = pd.read_csv('weather_data.csv')
# # print(data)

# # data_d = data.to_dict()
# # temps_l = data['temp'].to_list()

# # avg_temp = sum(temps_l) / len(temps_l)
# # print(avg_temp)

# # print(timeit.timeit(lambda: statistics.mean(temps_l), number=10000))

# # temps_np = np.array(temps_l)
# # print(timeit.timeit(lambda: np.mean(temps_np), number=10000))

# # print(timeit.timeit(lambda: data['temp'].mean(), number=10000))

# print(data)
# print(data[data.temp == data.temp.max()])

# data.temp = data.temp.apply(lambda x: (x * 9 / 5) + 32)
