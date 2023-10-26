import pandas as pd
import numpy as np
import ast

file_path = r'C:\Users\PC\Desktop\Стартекс тестовое\items.csv'
data = pd.read_csv(file_path, header=None)


# Функция для распаковки коллекции и сохранения в другом столбце в читаемом виде
def unpack_collection(data):
    try:
        data_dict = ast.literal_eval(data)
        result = ""
        for key, value in data_dict.items():
            if isinstance(value, list):
                result += f"{key}: #(lf)"
                for item in value:
                    result += f" - {item} #(lf)"
            else:
                result += f"{key}: #(lf) {value} #(lf)"
        return result
    except (ValueError, SyntaxError) as e:
        return f"Error: {e}"


data['new_column'] = data[1].apply(unpack_collection)

print(data)
