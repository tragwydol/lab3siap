#создаём файл F1
with open("F1.txt", "w",encoding="UTF-8") as f:
    while True:
        line = input("Введите строку: ")
        if line == "":
            break
        f.write(line + "\n")

#считаем колво гласных букв в строке
def count_vowels(line):
    return sum(c.isalpha() and c in "ёуеыаоэяию" for c in line)

#находим строку с наибольшим количеством гласных букв
max_vowels = 0
max_vowels_line = 0
for i, line in enumerate(open("F1.txt",encoding='UTF-8')):
    vowels = count_vowels(line)
    #print(i,line)
    #print(vowels)
    if vowels > max_vowels:
        max_vowels = vowels
        max_vowels_line = i

print(f"Строка с наибольшим количеством гласных букв: {max_vowels_line +1}")

with open("F2.txt", "w", encoding="UTF-8") as f1:
      
        for i,line in enumerate(open("F1.txt",encoding='UTF-8')):
            print(line)
            if i != max_vowels_line:
                f1.write(line)