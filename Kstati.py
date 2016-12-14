import os
if os.path.exists('some_file'): #проверка существования файла
    print('exists')
    if os.path.isfile('some_file'): #Файл?
        print('really file')
    elif os.path.isdir('some_file'): # папка?
        print('really dir')



#os.path.getsize('some_file'):
# узнать размер файла
