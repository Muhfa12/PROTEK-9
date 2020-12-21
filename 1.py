#1
def ubahHuruf(teks, a, b):
    List = list(teks)
    tambah = "".join(List)
    ubah = tambah.replace(a, b)
    print(ubah)
ubahHuruf("MATEMATIKA", "T", "S")
