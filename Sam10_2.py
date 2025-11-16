def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            if not content:
                raise Exception(f'Файл {file_name} - пустой')
            print(f'Содержимое файла {file_name} :\n{content}')
    except Exception as e:
        print(e)

file_name = 'secret.txt'
read_file(file_name)
file_name = 'secret2.txt'
read_file(file_name)