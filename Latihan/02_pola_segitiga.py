# Latihan 2: Pola Segitiga
# Nama: Siti Amaliah
# NIM: 2225250223
# Kelas: 3E

n = int(input("Masukkan n: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()