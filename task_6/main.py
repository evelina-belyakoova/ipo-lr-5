#Эвелина Белякова
with open('text.txt','r',encoding='utf-8') as file:#Открываем текстовый файл для чтения, а также вводим стандартную кодировку 
    text=file.read()#Читаем файл
    text_lower=text.lower()#Приводим написанный текст к нижнему регистру(к маленьким буквам все)
    words=text_lower.split()#Делим текст на слова
    unique_words=set(words)#создаем множество для хранения уникальных слов
    with open('output.txt','w',encoding='utf-8') as file:#Открываем новый файл для записи с той же кодировкой
        for word in sorted(unique_words):#Сортируем слова 
            file.write(word + "/n")#Записываем отсортированные в наш файл
    print("Уникальные слова в файле output.txt")#Выводим строку о том, в каком файле хранятся слова