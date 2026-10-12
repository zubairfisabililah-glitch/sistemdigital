desimal = int(input("Masukkan bilangan desimal: "))

# validasi input
if desimal < 0:
    print("Masukkan bilangan desimal yang valid (>= 0).")

# Jika angka 0
elif desimal == 0:
    print("0 dalam octal adalah 0")

else:
    angka = desimal
    octal = ""
    proses = ""

    # Perulangan pembagian dengan 8
    while angka > 0:
        hasilBagi = angka // 8
        sisa = angka % 8

        # Menyimpan proses
        proses += (
            str(angka) +
            " ÷ 8 = " +
            str(hasilBagi) +
            " sisa = " +
            str(sisa) +
            "\n"
        )

        # Sisa dimasukkan ke depan
        octal = str(sisa) + octal

        # Angka berikutnya
        angka = hasilBagi

    # Menampilkan hasil
    print()
    print("Bilangan Desimal:", desimal)
    print()
    print("Tahapan Perhitungan:")
    print(proses)
    print("Baca sisa dari bawah ke atas:")
    print(octal)
    print()
    print(
        "Jadi,",
        desimal,
        "desimal =",
        octal,
        "octal"
    )
