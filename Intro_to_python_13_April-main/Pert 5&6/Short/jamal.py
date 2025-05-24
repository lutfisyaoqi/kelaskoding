def input_manual(nilai):
    list_data = []
    for i in range(nilai):
        angka = int(input(f"Masukkan angka ke-{i+1}: "))
        list_data.append(angka)
    return list_data

def bubble_sort(data):
    panjang_data = len(data)
    for i in range(panjang_data):
        for j in range(0, panjang_data - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

def main():
    banyak_data = int(input("Banyak data yang ingin diinputkan: "))
    list_data = input_manual(banyak_data)
    
    print("List data sebelum diurutkan:")
    print(list_data)

    list_data_terurut = bubble_sort(list_data)
    print("List data setelah diurutkan:")
    print(list_data_terurut)

if __name__ == "__main__":
    main()
