import string
import re
import time


def flatten(arr):  # Funkcja pomocnicza, która wypłaszcza tablicę (zamiana w tablice jednowymiarową)
    flatten_arr = []
    for item_arr in arr:
        for item in item_arr:
            flatten_arr.append(item)
    return flatten_arr


enc = 'utf-8'  # encoding w jakim muszę otworzyć plik tekstowy
count_size = 255  # Ilość bucketów w których umieszczam pojedyncze słowa, 255 dlatego że są to wszystkie znaki ASCII


def get_max_length(book_content_arr):  # funkcja pomocnicza do znalezienia najdłuższego słowa
    size = 0
    for word in book_content_arr:
        word_size = len(word)
        if word_size > size:
            size = word_size
    return size


def radix_sort(arr):  # Radix sort oparty na bucketach
    word_length = get_max_length(arr)
    for index in range(0, word_length):  # pętla przechodządza przez kolejne litery w słowie, od pierwszej litery do ostatniej
        buckets = [[] for i in range(count_size)]  # Tworze 255 bucketów
        for item in arr:  # pętla przechodząca przez każde słowo w tablicy
            if len(item) > index:  # Jeśli długość słowa jest większa niż index, znaczy że litera o zadanym indexie jest w tym słowie
                num = ord(item[index])  # Konwertuje litere na numer ASCII
                buckets[num].append(item)  # Wrzucam słowo, do jej odpowiedniego bucketa
            else:  # W innym wypadku tej litery tam nie ma, więc słowo mogę przerzucić do pierwszego bucketa
                buckets[0].append(item)
        arr = flatten(buckets)  # wypłaszczam tablice bucketów
    return arr


book = open("ksiazka.txt", "r", encoding=enc)
book_content = book.read().translate(string.punctuation).upper()  # usuwam znaki interpunkcyjne, zamieniam wszystkie słowa do UPPERCASE
book_content = re.sub(r'[^a-zA-Z ]+', '', book_content).split()  # usuwam wszystkie znaki poza literami, i zamieniam string książki w tablicę


start_time = time.time()
book_content = radix_sort(book_content)
print("--- %s seconds ---" % (time.time() - start_time))

text_to_save = " ".join(book_content)

text_file = open("output.txt", "w")
n = text_file.write(text_to_save)
text_file.close()



