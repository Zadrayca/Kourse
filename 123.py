tar = int(input("Введите количество тарелок: "))
fairy = float(input("Введите количество Фейри: "))
while tar > 0 and fairy > 0:
    print (tar, " тарелок и", fairy, "Фейри осталось")
    tar -= 1
    fairy -= 0.5
print ("Остаток тарелок -", tar, "остаток Фейри -", fairy)