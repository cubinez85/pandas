import pandas as pd
import matplotlib.pyplot as plt


# def csv_to_json(csv_filepath, json_filepath):
#     data = []
#     with open(csv_filepath, 'r', encoding='utf-8') as csvfile:
#         csvreader = csv.DictReader(csvfile)
#         for row in csvreader:
#             data.append(row)
#
#     with open(json_filepath, 'w', encoding='utf-8') as jsonfile:
#         json.dump(data, jsonfile, indent=4, ensure_ascii=False)
#
# csv_filepath = './Shop_orders.csv'
# json_filepath = './Shop_orders.json'
# csv_to_json(csv_filepath, json_filepath)

# df_clicks = pd.read_json('./Shop_orders.json')
# plt.plot(df_clicks['Shop_3'])
# plt.show()

# def csv_to_excel(csv_filepath, excel_filepath, sheet_name='Sheet1'):
#     try:
#         df = pd.read_csv(csv_filepath, encoding='utf-8')
#         df.to_excel(excel_filepath, sheet_name=sheet_name, index=False)
#         print(f'Successfully converted {csv_filepath} to {excel_filepath}')
#     except FileNotFoundError:
#         print(f'Error: CSV file not found at {csv_filepath}')
#     except Exception as e:
#         print(e)
#
# csv_filepath = './Shop_orders.csv'
# excel_filepath = './Shop_orders.xlsx'
# csv_to_excel(csv_filepath, excel_filepath)



# df_clicks = pd.read_csv('./Shop_orders.csv')
# plt.plot(df_clicks['Shop_2'])
# plt.show()


# import pandas as pd
#
# df_orders = pd.read_csv('./Shop_orders.csv')
# print(df_orders.iloc[1])
# df_orders.iloc[[1]].to_csv('./Shop_orders_tue.csv', index=False)
# df_orders = pd.read_csv('./Shop_orders_tue.csv')
# row_series = df_orders.iloc[0]
# for index, value in row_series.items():
#     print(f'{index:<10}{value}')



# df_orders = pd.read_csv('Shop_orders.csv')
# df_orders.index = ['a', 'b', 'c', 'd', 'e', 'f', 'g'][:len(df_orders)]
# # print(df_orders)
# df_orders.to_csv('./Shop_orders_keys.csv', index=True)
# print(df_orders)



# df = pd.read_csv('./data_2/Shop_orders.csv')
# df.index = ['a', 'b', 'c', 'd', 'e', 'f', 'g'][:len(df)]
# df.index.name = 'Index'
# df.to_csv('Shop_original_keys.csv', index=True)
# print(df)


# df = pd.read_csv('./data_2/Shop_orders.csv', index_col=0)
# print(df[['Shop_1', 'Shop_2']].head())
# print(df.drop(['Shop_4'], axis=1).head())

# df = pd.read_csv('./data_2/Shop_orders_keys.csv', index_col=0)
# print(df.loc['b'])
# print(df.loc[['c', 'd']])
# df.loc[['c', 'd']].to_csv('./data/Orders_w_t.csv', index=False)
# df_or = pd.read_csv('./data/Orders_w_t.csv', index_col=0)
# print(df_or)


# df = pd.read_csv('./data_2/Shop_orders.csv', index_col=0)
# print(df)
# print(df.iloc[[1,2], [0,1]])


# df = pd.read_csv('./data/Shop_orders.csv', index_col=0)
# df.to_json('./Test_shops.json', index=False)
# data_dict = df.to_dict()
# print(data_dict)
# data_list_of_dicts = df.to_dict(orient='records')
# print(data_list_of_dicts)