# import pandas as pd
# import os
#
# orders_path = './data/Orders.xlsx'
# output_dir = './data'
# fill_value = 1
#
# if not os.path.exists(output_dir):
#     os.makedirs(output_dir)
#
# if not os.path.exists(orders_path):
#     print(f'File: "{orders_path}" not found.')
#     exit()
#
#
# def read_excel_data(file_path):
#     try:
#         test_df = pd.read_excel(file_path, index_col=0)
#         return test_df
#     except FileNotFoundError:
#         print(f'Error: File "{file_path}" not found.')
#         return None
#     except Exception as e:
#         print(e)
#
#
# def rename_columns(test_df):
#     test_df.columns = ['Shop_1', 'Shop_2', 'Shop_3', 'Shop_4']
#     return test_df
#
#
# def fill_values(test_df, fill_value_default=0):
#     if test_df is None:
#         return None
#     renamed_df = rename_columns(test_df)
#     return renamed_df.fillna(fill_value_default)
#
#
# def save_data(df, csv_path, excel_path, json_path):
#     try:
#         if df is not None:
#             df.to_csv(csv_path, index=False)
#             df.to_excel(excel_path, index=False)
#             df.to_json(json_path, index=False)
#             return 'Файлы успешно сохранены'
#         else:
#             return 'Не удалось сохранить файлы, так как Data Frame is None'
#     except Exception as e:
#         return f'Ошибка при сохранении файлов: {e}'
#
#
# def etl():
#     test_df = read_excel_data(orders_path)
#     filled_df = fill_values(test_df, fill_value)
#     if filled_df is not None:
#         csv_path = os.path.join(output_dir, 'Orders_etl.csv')
#         excel_path = os.path.join(output_dir, 'Orders_etl.xlsx')
#         json_path = os.path.join(output_dir, 'Orders_etl.json')
#         result = save_data(filled_df, csv_path, excel_path, json_path)
#         return result
#     else:
#         return 'Обработка данных не выполнена из-за ошибки чтения файла или другого сбоя.'
#
#
# print(etl())




# import pandas as pd
# import os
# orders_path = './data/Orders.xlsx'
# output_dir = './data'
# fill_value = 1
# if not os.path.exists(output_dir):
#     os.makedirs(output_dir)
#
# if not os.path.exists(orders_path):
#     print(f"Файл {orders_path} не найден.")
#     exit()
# def rename_columns(test_df):
#     test_df.columns = ['Shop_1', 'Shop_2', 'Shop_3', 'Shop_4']
#     return test_df
# test_df = pd.read_excel(orders_path, index_col=0)
#
# def fillna_values(test_df, fill_value=0):
#     res = rename_columns(test_df)
#     return res.fillna(fill_value)
#
# def etl():
#     res = fillna_values(test_df, fill_value)
#     res.to_csv('./data/Orders_etl.csv')
#     res.to_excel('./data/Orders_etl.xlsx')
#     return 'Файлы успешно сохранены'
# result = etl()
# print(result)

# import pandas as pd
# import os
#
# orders_path = './data/Orders.xlsx'
# n = 1
#
# if not os.path.exists(orders_path):
#     print(f"Файл {orders_path} не найден.")
# else:
#     test_df = pd.read_excel(orders_path, index_col=0)
#
#
#     def rename_columns(test_df):
#         expected_columns = 4
#         if len(test_df.columns) != expected_columns:
#             print(f"Ожидалось {expected_columns} столбца, но найдено {len(test_df.columns)}.")
#             return None
#         test_df.columns = ['Shop_1', 'Shop_2', 'Shop_3', 'Shop_4']
#         return test_df
#
#
#     def fillna_values(test_df, n=0):
#         res = rename_columns(test_df)
#         if res is None:  # Проверяем успешность выполнения
#             return None
#         return res.fillna(n)
#
#
#     def etl():
#         res = fillna_values(test_df, n)
#         if res is None:
#             return 'Не удалось выполнить ETL из-за проблемы с данными.'
#
#         res.to_csv('./data/Orders_etl.csv')
#         res.to_excel('./data/Orders_etl.xlsx')
#         return 'Файлы успешно сохранены'
#
#
#     result = etl()
#     print(result)

# import pandas as pd
# test_df = pd.read_excel('./data/Orders.xlsx', index_col=0)
# print(len(test_df.columns))
# test_df_res = pd.read_excel('./data/Orders_etl.xlsx', index_col=0)
# print(len(test_df_res.columns))


# import pandas as pd
# import os
#
# orders_path = './data/Orders.xlsx'
# n = 1
#
#
# def rename_columns(test_df):
#     if test_df.shape[1] != 4:
#         print(f"Неверное количество столбцов: {test_df.shape[1]} (ожидалось 4)")
#         return None
#     test_df.columns = ['Shop_1', 'Shop_2', 'Shop_3', 'Shop_4']
#     return test_df
#
#
# def fillna_values(test_df, n=0):
#     res = rename_columns(test_df)
#     if res is None:
#         return None
#     return res.fillna(n)
#
#
# def etl():
#     if not os.path.exists(orders_path):
#         print(f"Файл {orders_path} не найден.")
#         return None
#     try:
#         test_df = pd.read_excel(orders_path, index_col=0)
#     except Exception as e:
#         print(f"Ошибка при загрузке файла: {e}")
#         return None
#
#     res = fillna_values(test_df, n)
#     if res is None:
#         return 'Ошибка при обработке данных'
#
#     try:
#         res.to_csv('./data/Orders_etl.csv', index=False)
#         res.to_excel('./data/Orders_etl.xlsx', index=False)
#     except Exception as e:
#         print(f"Ошибка при сохранении файлов: {e}")
#         return None
#     return 'Файлы успешно сохранены'
#
#
# result = etl()
# print(result)


# import pandas as pd

# def rename_columns(test_df):
#     test_df.columns = [f'Shop_{i+1}' for i in range(len(test_df.columns))]
#     return test_df
#
# orders_path = './data/Orders.xlsx'
# test_df = pd.read_excel(orders_path, index_col=0)
#
# def fillna_values(test_df, n=0):
#     res = rename_columns(test_df)
#     return res.fillna(n)
# n = 1
#
# def etl():
#     res = fillna_values(test_df, n)
#     res.to_csv('./data/Orders_etl.csv', index=False)
#     res.to_excel('./data/Orders_etl.xlsx', index=False)
#     return 'Файлы успешно сохранены'
#
# result = etl()
# print(result)






# import pandas as pd
# # import os
# def rename_columns():
#     orders_path = './data/Orders.xlsx'
#
#     # # Проверка существования файла
#     if not os.path.exists(orders_path):
#         print(f"Файл {orders_path} не найден.")
#         return None
#
#     # Загрузка данных из Excel
#     test_df = pd.read_excel(orders_path)
#
#     # Проверка количества столбцов
#     expected_columns = 5
#     if len(test_df.columns) != expected_columns:
#         print(f"Ожидалось {expected_columns} столбца, но найдено {len(test_df.columns)}.")
#         return None
#
#     # Переименование столбцов
#     test_df.columns = ['Weekday', 'Shop_1', 'Shop_2', 'Shop_3', 'Shop_4']
#
#     # Сохранение в новый файл
#     result_path = './data/result_Orders.xlsx'
#     test_df.to_excel(result_path, index=False)
#     return test_df
#
#
# # Вызов функции и печать результата
# result_df = rename_columns()
# if result_df is not None:
#     print(result_df)
# def f():
#     res = rename_columns()
#     return res
# print(f)

# df = pd.read_csv('./data/Shop_orders.csv', index_col=0)
# df.to_excel('./data/Orders.xlsx')