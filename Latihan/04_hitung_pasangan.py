# Latihan 4: Menghitung Pasangan
# Nama: Siti Amaliah
# NIM: 2225250223
# Kelas: 3E

n = int(input("Masukkan n: "))

count = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i + j <= n:
            count += 1

print(f"Banyak pasangan = {count}")