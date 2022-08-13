def list_files():  # Нужный список файлов, если в директории много фалов
    import os
    directory_files_all = os.listdir(path='.')
    list_directory = []
    for directory in directory_files_all:
        if directory == '1.txt' or directory == '2.txt' or directory == '3.txt':
            list_directory.append(directory)
    return list_directory


def dict_files():  # Словарь {количетсво строк: 'название файла'}
    result = {}
    for file_name in list_files():
        with open(file_name) as name:
            result[len(name.readlines())] = file_name
    return result


def list_files_ascending():  # Отсортированный список файлов по кол-во строк
    list_files_ascending_tmp = []
    dict_tmp = dict_files().copy()
    for _ in range(len(dict_tmp)):
        min_str = min(dict_tmp)
        list_files_ascending_tmp.append(dict_tmp[min(dict_tmp)])
        del dict_tmp[min_str]
    return list_files_ascending_tmp


def result_file(list_of_files):  # Создание итогового файла
    for name in list_of_files:
        with open(name) as file:
            len_file = len(file.readlines())
            file.seek(0)
            text_file = file.read()
            with open('result_task3.txt', 'a') as result_file_tmp:
                result_file_tmp.write(f'{name}\n')
                result_file_tmp.write(f'{str(len_file)}\n')
                result_file_tmp.write(f'{text_file}\n')


def deleting_last_line():  # Удаление пустой строки в итоговом файле
    with open('result_task3.txt') as file:
        lines = file.read()
        lines = lines[:-1]

    with open('result_task3.txt', 'w') as file:
        file.writelines(lines)


result_file(list_files_ascending())
deleting_last_line()
