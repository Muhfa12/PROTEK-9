#7
mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']
print("==============================================================")
print("NIM" . ljust(10), "NAMA MAHASISWA" . ljust(21),"TGL LAHIR" . ljust(15),"TEMPAT LAHIR" . ljust(12))
print("--------------------------------------------------------------")
for i in range(len(mhs)):
	v = mhs[i]
	w, x, y, z = v . split(":")
	thn, bln, tgl = y . split("-")
	tambah = ("/" . join([tgl, bln, thn]))
	print(w . ljust(10), x . ljust(21), tambah . ljust(15), z . ljust(12))
print("--------------------------------------------------------------")
