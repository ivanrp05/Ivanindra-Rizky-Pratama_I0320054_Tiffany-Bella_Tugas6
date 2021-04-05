#Mulai
print("Soal 3 Tugas 6 ")
print("")
print("Nama : Ivanindra Rizky P")
print("NIM : I0320054")
print("")
print("===========================")
print("")
print("Ditanya :")
print("Buatlah program dengan hasil program seperti gambar dibawah, dengan ketentuan")
print("menggunakan perintah pengulangan dan fungsi range()")
print("")
print("Jawab :")
nilai = [ ]
x = int(input("Silahkan masukkan angka : "))
while x != '' :
    nilai.append(int(x))
    x = input("Masukkan lagi angka anda :")
for a in nilai :
    for x in range(2, a):
        if a % x == 0:
            print(a, "bukan merupakan bilangan")
            break
    else:
        print(a, "merupakan bilangan prima")
print("Alhamdulillah udah selesai")
#Selesai

