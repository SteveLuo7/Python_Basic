base_dir = './files/'

def read_file(file_name):
    try:
        with open(base_dir + file_name, 'r', encoding='utf8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print('404 Not Found')


def write_json(file_name, data):
    with open(base_dir + file_name, 'w', encoding='utf8') as file:
        import json
        json.dump(data, file)
