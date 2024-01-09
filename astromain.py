import tkinter as tk

# Создаем словарь компонентов и заполняем его значениями по умолчанию
components = {
    'Соединение': 0,
    'Смола': 0,
    'Органика': 0,
    'Кварц': 0,
    'Стекло': 0,
    'Керамика': 0,
    'Вольфрам': 0,
    'Углерод': 0,
    'Железо': 0,
    'Медь': 0,
    'Алюминий': 0,
    'Аммоний': 0,
    'Графит': 0,
    'Титан': 0,
    'Литий': 0,
    'Цинк': 0,
    'Астрониум': 0,
    'МЕТАН': 0,
    'СЕРА': 0,
    'АРГОН': 0,
    'ВОДОРОД': 0,
    'АЗОТ': 0,
    'ГЕЛИЙ': 0
}
# Создаем словарь предметов и заполняем его значениями по умолчанию
items = {
    'Силикон': ['Смола', 'Кварц', 'МЕТАН'],
    'Резина': ['Смола', 'Органика'],
    'Пластик': ['Соединение', 'Углерод'],
    'Порох': ['Углерод', 'Углерод', 'СЕРА'],
    'Сталь': ['Железо', 'Углерод', 'АРГОН'],
    'Карбид вольфрама': ['Вольфрам', 'Углерод'],
    'Титановый сплав': ['Вольфрам', 'Углерод'],
    'Алюминиевый сплав': ['Медь', 'Алюминий'],
    'Гидразин': ['Аммоний', 'Аммоний', 'ВОДОРОД'],
    'Графен': ['Аммоний', 'Аммоний', 'ВОДОРОД', 'Графит'],
}
# Создаем словарь объектов и заполняем его значениями по умолчанию
objects = {
    # Малые (1 ячейка)
    'Алмаз': {'Графен': 2},
    'Трактор': {'Алюминий': 2},
    'Прицеп': {'Алюминий': 1, 'Соединение': 1},
    'Вагонетка': {'Алюминий': 1, 'Соединение': 1},
    # Средние (2 ячейки)
    'Большой склад': {'Керамика': 3},
    'Большой амбар А': {'Алюминий': 2, 'Сталь': 1},
    'Большой амбар Б': {'Сталь': 3},
    # Большие (4 ячейки)
    'Локомотив': {'Смола': 2, 'Алюминий': 1, 'Медь': 1},
    'Вагон': {'Смола': 2, 'Алюминий': 1},
    'Хим. лаборатория': {'Силикон': 1, 'Титан': 1},
}


def calculate_components():
    global components
    # Запрашиваем у пользователя количество объектов для каждого объекта
    num_objects = {}
    for obj in objects:
        num = int(objects_entry[obj].get())
        num_objects[obj] = num
    # Проходимся по каждому объекту и вычисляем количество компонентов
    for obj, comp_dict in objects.items():
        for item, count in comp_dict.items():
            if item in items:
                for comp in items[item]:
                    components[comp] += count * num_objects[obj]
            else:
                components[item] += count * num_objects[obj]
    # Выводим результат
    result_text.delete('1.0', tk.END)
    for comp, count in components.items():
        if count > 0:
            result_text.insert(tk.END, f'{count} {comp}\n')
    result_text.insert(tk.END, '-' * 20 + '\n')
    # Вычисляем и выводим итоговую сумму компонентов
    total_components = sum(components.values())
    result_text.insert(tk.END, f'Итого: {total_components} компонентов\n')
    # Обнуляем значения компонентов для следующего объекта
    components = {comp: 0 for comp in components}


def clear_components():
    pass


# Создаем окно
root = tk.Tk()
root.title('Калькулятор ресурсов Astroneer')

# Создаем виджеты для ввода количества объектов
objects_entry = {}
for i, obj in enumerate(objects):
    label = tk.Label(root, text=obj)
    label.grid(row=i, column=0)
    entry = tk.Entry(root)
    entry.grid(row=i, column=1)
    # вставка начальных данных
    entry.insert(0, '0')
    objects_entry[obj] = entry

# Создаем кнопку для запуска расчета
calculate_button = tk.Button(root, text='Рассчитать', command=calculate_components)
calculate_button.grid(row=len(objects), column=0, columnspan=2)

# Создаем кнопку для очистки расчета
clear_button = tk.Button(root, text='Очистить', command=clear_components)
clear_button.grid(row=len(objects), column=0, columnspan=1)

# Создаем виджет для вывода результата
result_text = tk.Text(root)
result_text.grid(row=len(objects) + 1, column=0, columnspan=2)

root.mainloop()
