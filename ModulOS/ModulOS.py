import os

print("Имя сиситемы:", os.name)

print("Имя пользователя:", os.environ["username"])

print("Рабочая папка:", os.getcwd())

os.chdir("c:\\") #смена рабочей папке
print("Рабочая папка теперь:", os.getcwd())

os.mkdir("tmp") #создание папки

os.makedirs("tmp2\\tmp3") #Создание множества папок

print("Путь c:\\tmp2\\tmp3 существует", os.path.exists("c:\\tmp2\\tmp3"))

os.startfile("tmp.txt") #запуск файла

os.rename("tmp", "temp") #переименовывает папки

print("Путь c:\\tmp2 содержит:")
for i in os.walk('c:\\tmp2'): print(i) #перечисление ветвей c:\\tmp2

input("Нажмите кнопку для продолжения")

os.rmdir("temp") #удаляет папку temp
os.remove("tmp.txt") #удаляет файл
os.removedirs("tmp2\\tmp3") #удаляет папку и все вложенные пустые папки
print("Удалились все временные файлы")