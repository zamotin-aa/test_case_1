# 3. Какие слова, не относящиеся к названию рубрики чаще встречаются в описании
# “успешных” тканей, а какие наоборот у аутсайдеров?
# Вторая часть задания

import pandas as pd
from collections import Counter
import re

# Данные беру из этого файла
file_path = r'C:\Users\PC\Desktop\Стартекс тестовое\Тестовое.xlsx'

# Список рубрик
data_category = pd.read_excel(file_path, sheet_name='category_')
data_list_category = data_category['category'].tolist()

# Аутсайдеры (5 % всех продаж)
data_outsiders = pd.read_excel(file_path, sheet_name='items_C')
data_outsiders = data_outsiders[['Артикул', 'Описание']]

# Создание списка предлогов на русском языке, чтобы потом их исключить из поиска
prepositions = ["в", "на", "под", "над", "с", "и", "для", "а", "не", "при",
                "к", "у", "за", "до", "из", "от", "по", "о"]


# Объединение всех описаний в одну строку
text_combined = ' '.join(data_outsiders['Описание'].astype(str))

# Разделение текста на слова и удаление знаков препинания
words = re.findall(r'\w+', text_combined.lower())

# Подсчет частоты встречаемости слов, не входящих в список "data_list_category"
filtered_words = [
    word for word in words if word not in data_list_category and word not in prepositions]
word_freq = Counter(filtered_words)

# Разделение текста на слова, удаление знаков препинания и фильтрация предлогов
words = re.findall(r'\w+', text_combined.lower())
filtered_words = [
    word for word in words if word not in data_list_category and word not in prepositions]

# Подсчет частоты встречаемости слов, не входящих в список "data_list_category" и не являющихся предлогами
word_freq = Counter(filtered_words)

# Итог
most_common_words = word_freq.most_common(20)
for word, freq in most_common_words:
    print(word, ":", freq)

# Сохранение результатов в файл
df_result = pd.DataFrame(word_freq.most_common(30),
                         columns=['Слово', 'Частота'])
output_file_path = r'C:\Users\PC\Desktop\Стартекс тестовое\результаты_анализа_3_2.csv'
df_result.to_csv(output_file_path, index=False, encoding='utf-8')
