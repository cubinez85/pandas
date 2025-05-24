import pandas as pd
import matplotlib.pyplot as plt
# df_orders = pd.read_csv('./data/Shop_orders.csv', index_col=0)
# print(df_orders.head())
# print(df_orders.describe())
# print(df_orders.mean())
# df_orders_centered = df_orders - df_orders.mean()
# print(df_orders_centered)
# df_orders_centered.to_csv('./Shop_orders_centered.csv')
df_clicks = pd.read_json('./data/Cite_clicks.json')
# df_clicks = pd.read_csv('./data/Shop_orders.csv', index_col=0)
# print(df_clicks.head())
# print(df_clicks.info())
# print(df_clicks.describe())
# print(df_clicks.columns)
# df_clicks.columns = ['Weekday', 'Shop_1', 'Shop_2', 'Shop_3', 'Shop_4']
# print(df_clicks.head())
plt.plot(df_clicks['Shop_3'])
plt.show()
# df_clicks = df_clicks.fillna(0)
# df_clicks = abs(df_clicks)
# df_clicks['mean'] = df_clicks.mean(axis=1)
# print(df_clicks.head())
# df_clicks.to_csv('./data/Cite_clicks_analyzed.csv')
# df_clicks.to_json('./data/Cite_clicks_analyzed.json')
# df_clicks.to_excel('./data/Cite_clicks_analyzed.xlsx')
#


# import csv
# data = []
# with open('./data/Orders_etl.csv', 'r') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         data.append(row)
#     print(data)
