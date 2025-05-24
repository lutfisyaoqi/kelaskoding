import random

def random_number_generate(nilai):
    list_data = []
    for i in range(nilai):
        nilai_acak = random.randrange(1, 100)
        list_data.append(nilai_acak)
    return list_data

def bubble_sort(data):
    panjang_data = len(data)
    for i in range(panjang_data):
        for j in range(0, panjang_data - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

def selection_sort(data):
    panjang_data = len(data)
    for i in range(panjang_data):
        indeks_min = i
        for j in range(i+1, panjang_data):
            if data[j] < data[indeks_min]:
                indeks_min = j
        data[i], data[indeks_min] = data[indeks_min], data[i]
    return data

def main():
    banyak_data = int(input("Banyak data yang dibuat: "))
    list_data = random_number_generate(banyak_data)
    print("List data sebelum diurutkan:")
    print(list_data)

    print("\nPilih metode pengurutan:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    pilihan = input("Masukkan pilihan (1/2): ")

    if pilihan == '1':
        list_data_terurut = bubble_sort(list_data.copy())
        print("List data setelah diurutkan dengan Bubble Sort:")
    elif pilihan == '2':
        list_data_terurut = selection_sort(list_data.copy())
        print("List data setelah diurutkan dengan Selection Sort:")
    else:
        print("Pilihan tidak valid!")
        return

    print(list_data_terurut)

if __name__ == "__main__":
    main()
