import string
import re
import time


signs = [".", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]  # Tablica znakow z ktorej wyciagam indeks
enc = 'utf-8'  # encoding w jakim muszę otworzyć plik tekstowy

def get_max_length(book_content_arr):  # funkcja pomocnicza do znalezienia najdłuższego słowa
    size = 0
    for word in book_content_arr:
        word_size = len(word)
        if word_size > size:
            size = word_size
    return size


def set_same_size(arr, size):  # dodaje kropki to słów które są mniejsze niż największe słowo w tablicy
    same_size_arr = []
    
    for word in arr:
        new_arr = ['.' * (size - len(word))]
        same_size_arr.append(word + ''.join(new_arr))

    return same_size_arr


def revert_to_proper_size(arr):  # usuwa niepotrzebne kropki po sortowaniu
    index = 0
    for word in arr:
        arr[index] = re.sub('[.]', '', word)
        index += 1


def counting_sort_for_letters(arr, index):
    count = [0] * len(signs)  # tablica do zliczania
    output = [0] * len(arr)  # tablica która bedzie zawierac wynik końcowy

    # zliczam ilosc wystapien danej litery
    for item in arr:
        idx = signs.index(item[index])
        count[idx] += 1

    # kumuluje
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # przepisywanie
    for j in range(len(arr) - 1, -1, -1):
        idx = signs.index(arr[j][index])
        count[idx] -= 1
        output[count[idx]] = arr[j]
    return output


def radix_sort(arr, world_length):
    for i in range(world_length - 1, -1, -1):
        arr = counting_sort_for_letters(arr, i)
    return arr


book = open("ksiazka.txt", "r", encoding=enc)
book_content = book.read().translate(string.punctuation).upper()  # usuwam znaki interpunkcyjne, zamieniam wszystkie słowa do UPPERCASE
book_content = re.sub(r'[^a-zA-Z ]+', '', book_content).split()  # usuwam wszystkie znaki poza literami, i zamieniam string książki w tablicę

word_length = get_max_length(book_content)
book_content = set_same_size(book_content, word_length)

start_time = time.time()
book_content = radix_sort(book_content, word_length)
print("--- %s seconds ---" % (time.time() - start_time))
revert_to_proper_size(book_content)


text_to_save = " ".join(book_content)

text_file = open("output.txt", "w")
n = text_file.write(text_to_save)
text_file.close()



