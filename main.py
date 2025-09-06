from utils import konversi_suhu

print("=== KONVERSI SUHU ===")
try:
    nilai = float(input("Masukkan nilai suhu: "))
    dari = input("Dari satuan (C/F/K): ")
    ke = input("Ke satuan (C/F/K): ")
    hasil = konversi_suhu(nilai, dari, ke)
    if isinstance(hasil, str):
        print(hasil)
    else:
        satuan_dict = {"c": "°C", "f": "°F", "k": "K"}
        print(f"Hasil: {nilai}{satuan_dict[dari.lower()]} = {hasil:.2f}{satuan_dict[ke.lower()]}")
except ValueError:
    print("Error: Nilai suhu harus berupa angka.")
