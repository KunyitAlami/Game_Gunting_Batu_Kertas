import random

exit = False
#kita membuat keadaan awal dari variabel exit adaalah False
user_point = 0
computer_point = 0

while exit == False:
    pilihan = ["Gunting", "Batu", "Kertas"]
    #kita membuat variabel pilihan untuk dipilih oleh user dan computer
    user_input = input("Pilihlah antara Gunting, Batu, dan Kertas : ")
    #kita menyuruh user untuk memasukan pilihannya
    computer_input = random.choice(pilihan)
    #kita memakai modul random untuk membuat komputer memilih pilihannya

    #kita membuat if jika user memilih untuk exit atau keluar
    if user_input != "Gunting" and user_input != "Batu" and user_input != "Kertas":
        print("Input Tidak Valid!")

    if user_input == "exit":
        print("Game Telah Berakhir")
        print("Skor Anda adalah ", user_point)
        print("Skor Komputer adalah ", computer_point)
        exit = True

    
    #kita membuat keadaan if jika user memilih gunting
    if (user_input == "Gunting" or user_input == "gunting"):
        if computer_input == "Gunting":
            print("Anda Memilih Gunting")
            print("Computer Memilih Gunting")
            print("Hasil nya Seimbang")
           
        elif computer_input == "Batu":
            print("Anda Memilih Gunting")
            print("Computer Memilih Batu")
            print("Computer Menang!")
            computer_point += 1
        
        elif computer_input =="Kertas":
            print("Anda Memilih Gunting")
            print("Computer Memilih Kertas")
            print("Anda Menang!")
            user_point += 1
    
    #kita membuat keadaan if jika user memilih Batu
    if (user_input == "Batu" or user_input == "batu"):
        if computer_input == "Gunting":
            print("Anda Memilih Batu")
            print("Computer Memilih Gunting")
            print("Anda Menang!")
            user_point += 1
           
        elif computer_input == "Batu":
            print("Anda Memilih Batu")
            print("Computer Memilih Batu")
            print("Hasilnya Seimbang")
        
        elif computer_input =="Kertas":
            print("Anda Memilih Batu")
            print("Computer Memilih Kertas")
            print("Computer Menang!")
            computer_point += 1
    
    #kita membuat keadaan if jika user memilih Kertas
    if (user_input == "Kertas" or user_input == "kertas"):
        if computer_input == "Gunting":
            print("Anda Memilih Kertas")
            print("Computer Memilih Gunting")
            print("Computer Menang!")
            computer_point +=1
           
        elif computer_input == "Batu":
            print("Anda Memilih Kertas")
            print("Computer Memilih Batu")
            print("Anda Menang!")
            user_point += 1
        
        elif computer_input =="Kertas":
            print("Anda Memilih Kertas")
            print("Computer Memilih Kertas")
            print("Hasilnya Seimbang")

        







