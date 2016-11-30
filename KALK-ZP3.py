#калькулятор зарплаты
from datetime import datetime
now = datetime.now()
date = str((now.year, now.month, now.day))
w = []
e = 0
y = 0
r = 0
def instr():
    """вывод инструкций и приветствие"""
    print ("""\t Привет, я ЗП калькулятор. Я помогу тебе посчитать  твою зарплату. 	""")
def vod():
    """ввод"""
    a = None 
    while a not in range (1, 20000):
        try:
            a = int(input("\n ввод заказа: "))
        except:
            continue 
    return a
def kalk (z):
    """kalkyl"""
    if float(z) <= float("1999"):
        y = z * float(0.2)
        return y
    elif float(z) >= float("2000") and float(z) <= float("3999"):
        y = z * 0.25
        return y
    elif float(z) >= float ("4000"):
        y = z * 0.3
        return y 
def result (q,t):
    print ("Заработано с заказа: ", int(q))
    w.append(int(q))
    print ("Список: ", w)
    global e
    e += q 
    print ("Сумма ЗП: ", int(e))
    global r
    r += t
    print ("Сумма всего: ", r) 
    o = int(r) - int(e)
    print ("Остаток: ", o)
    kalk = open("kalk.txt", "a")
    kalk.write(date)
    kalk.write("\nЗаработанно с заказа: ")
    kalk.write(str(q))
    kalk.write("\nСписок: ")
    kalk.write(str(w))
    kalk.write("\nСумма ЗП: ")
    kalk.write(str(e))
    kalk.write("\nСумма всего: ")
    kalk.write(str(r))
    kalk.write("\nОстаток: ")
    kalk.write(str(o))
    kalk.write("\n")
    kalk.close()
def main ():
    while True:
        instr ()
        x = vod ()
        y = kalk (x) 
        result (y,x)
main ()
input ("\введите enter ")
