# JSON - JavaScript Object Notation
"""
Единый текстовый формат данных, был создан для хранения и передачи данных между сервисами
<filename>.json - файл в формате JSON
"""
# {
#     "id":1,
#     "author":{
#     "name":"Ed Sheeran",
#     "age":35,
#     },
#     "title":"don't"
#     "feat":false,
# } ----------------------- это JSON

#!!!!
# js object == {key:value}
# Py dict == {key:value}
# JSON == {key:value}

# Процессы Сериализации и Десираризации (Конвертация)

# Сериализация (Запись данных в JSON) - Это перевод из Python в JSON

# dump - записывает данные в файл формата JSON
# dumps - записывает данные в текст формата JSON

# Десериализация (Чтение данных из JSON) - Это процесс перевода данных из JSON в PY dict

# load - функция которая считывает данные из файла JSON 
# loads - функция которая считывает данные из текста JSON
#-------------------------------------------------------------------------------

# процесс Сериализации

# import json

# dict_={
#     "name":"Jons Snow",
#     "age":24,
#     "status":True,
#     "wife":False,
#     "children":None,
# # }
# print(dict_,type(dict_))

# json_text=json.dumps(dict_)
# print()
# print(json_text,type(json_text))

# dict_={
#     "name":"Jons Snow",
#     "age":24,
#     "status":True,
#     "wife":False,
#     "children":None,
# }
# print(dict_,type(dict_))

# with open("new.json","w") as file:
#     json.dump(dict_,file,indent=4)
#---------------------------------------------------------
# Процесс десереализации
# import json

# with open("new.json","r") as file:
#     json_data=file.read()

# print(json_data,type(json_data))
# dict_=json.loads(json_data)
# print(dict_,type(dict_))

# import json
# with open("new.json","r") as file:
#     dictt=json.load(file)
#     print(dictt,type(dictt))

#-----------------------------------------------------
from urllib.request import urlopen
import json
import pprint as pp
url="https://randomuser.me/api/"
json_data=urlopen(url)
# print(json_data,dir(json_data))
dictt=json.load(json_data)
pp.pprint(dictt)