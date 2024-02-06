def generate(lst):
    while True:
        a = input("Введите строку: ")
        lst.append(a)
        if a == "":
            break

def spisok(lst):
    for n in range (len(lst) - 1):
        print(n + 1, lst[n])

def main(lst):
    generate(lst)
    spisok(lst)