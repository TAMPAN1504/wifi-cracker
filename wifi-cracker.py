# Tabel transformasi (komplemen hex)
transformasi = {
    '0': 'f', '1': 'e', '2': 'd', '3': 'c', '4': 'b', '5': 'a', '6': '9', '7': '8', 
    '8': '7', '9': '6', 'a': '5', 'b': '4', 'c': '3', 'd': '2', 'e': '1', 'f': '0',
    'j': 'b', 'z': '5'
}

def buat_password(input_string):
    # Mengubah input string menggunakan tabel transformasi
    password = ''.join([transformasi.get(char, char) for char in input_string.lower()])
    return password

# Input password (contoh)
input_password = input("Masukkan input string: ")
output_password = buat_password(input_password)

print(f"Password yang dihasilkan: {output_password}")
