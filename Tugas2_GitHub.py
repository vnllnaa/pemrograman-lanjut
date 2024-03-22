def profile(Nama,NIM,Prodi,Hobi):
	""" function coba keyword arguments """
	print("Profile Mahasiswa UNJANI Yogyakarta")
	nama = int(input("Nama :"))
	nim = int(input("NIM :"))
	prodi = int(input("Prodi :"))
	hobi = int(input("Hobi :"))

data = {'Nama':"Puji Winar Cahyo",'NIM':"17000040",'Prodi':"Teknik Informatika",'Hobi':"coding"}
profile(**data)
