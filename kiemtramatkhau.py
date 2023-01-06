def kiemtramk(h):
	
	n = len(h)
	ktthuong = False
	kthoa = False
	ktso = False
	ktdacbiet = False
	normalkt = "abcdefghijklmnopqrstu"
	"vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
	
	for i in range(n):
		if h[i].islower():
			ktthuong = True
		if h[i].isupper():
			kthoa = True
		if h[i].isdigit():
			ktso = True
		if h[i] not in normalkt:
			ktdacbiet = True
	print("Độ mạnh của mật khẩu là ", end = "")
	if (ktthuong and kthoa and ktso and ktdacbiet and n >= 8):
		print("Mạnh ")
		
	elif ((ktthuong or kthoa) and ktdacbiet and n >= 6):
		print("Trung bình")
	else:
		print("Yếu")

if __name__=="__main__":
	
	h=input("Nhập mật khẩu: ")
	
	kiemtramk(h)
