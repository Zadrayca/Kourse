#калькулятор зарплаты
from datetime import datetime
now = datetime.now()
date = str((now.year, now.month, now.day))
sps = []
summa = 0
sum_all = 0
ost = 0
def instr():
    """вывод инструкций и приветствие"""
    print ("""\t Привет, я ЗП калькулятор. Я помогу тебе посчитать  твою зарплату. 	""")
def vvod ():
    """функция принимает пользовательский ввод в строго ограниченных рамках"""
    zak = None
    while zak not in range (1, 20001):
        try:
            zak = int (input("ввод заказа: "))
        except:
            continue
    return zak
def kalk (zp):
    """функция высчитывает % зарплаты"""
    if zp in range (0, 2000):
        zp *= 0.2
        return float (zp)
    elif zp in range (2000, 4000):
        zp *= 0.25
        return float (zp)
    elif zp in range (4000, 20001):
        zp *= 0.3
        return float (zp)
def result (zp, sps, zak, summa, sum_all, ost):
    print ("Заработанно с заказа: ", zp)
    sps.append (zp)
    print ("Список: ", sps)
    summa += zp
    print ("Сумма ЗП:", summa)
    sum_all += zak
    print ("Сумма всего:", sum_all)
    ost = sum_all - summa
    print ("Остаток :", ost)
    kalk = open ("kalk.txt", "a")
    kalk.write (date)
    kalk.write ("\nЗаработанно с заказа: ")
    kalk.write (str(zp))
    kalk.write ("\nСписок: ")
    kalk.write (str(sps))
    kalk.write ("\nСумма ЗП: ")
    kalk.write (str(summa))
    kalk.write ("\nСумма всего: ")
    kalk.write (str(sum_all))
    kalk.write ("\nОстаток: ")
    kalk.write (str(ost))
    kalk.write ("\n\n")
    kalk.close ()
    return sps, summa, sum_all, ost
while True:
    instr()
    zak = vvod()
    zp = kalk(zak)
    sps, summa, sum_all, ost = result (zp, sps, zak, summa, sum_all, ost)

input ("/nвведите ентер.")