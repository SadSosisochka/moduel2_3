spisok = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
count = 0
spisok.remove(0)
while count < len(spisok):
    if spisok[count] > 0:
        print(spisok[count])
        count += 1
        continue
    break
