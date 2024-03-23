def profile(Nama,NIM,Prodi,Hobi):
	""" function coba keyword arguments """
	print("Profile Mahasiswa UNJANI Yogyakarta")
	nama = str(input("Nama :"))
	nim = str(input("NIM :"))
	prodi = str(input("Prodi :"))
	hobi = str(input("Hobi :"))

	for key, value in enumerate (data):
		print("Mahasiswa Prodi {} UNJANI Yogyakarta".format(prodi))
		print("Dengan nama {}".format(nama))
		print("Mempunyai NIM {}".format(nim))
		print("Memiliki hobi {}".format(hobi))
	

data = {'Nama':"Puji Winar Cahyo",'NIM':"17000040",'Prodi':"Teknik Informatika",'Hobi':"coding"}
profile(**data)