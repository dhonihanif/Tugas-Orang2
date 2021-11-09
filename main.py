import os
import sys
import datetime
import string
import re

def run(runfile):
    with open(runfile,"r") as f:
        exec(f.read())

a=os.path.exists("C:/Users/Administrator/Downloads/riwayat.txt")


if a==False:
    riwayat_running = open("riwayat.txt","w")
    riwayat_running.write("0")
    riwayat_running.close()

    while True:
        print(" Tersedia File ".center(70,'-'))
        print("")
        print(f"""
1. Otomotif
2. Expression Matter
3. Consonant
4. Stop Program
""")
        x = int(input("File yang mana yang ingin anda jalankan ? : "))
        if x == 1:
            run("otomotif.py")
            riwayat_running = open("riwayat.txt","r")
            b = riwayat_running.readlines()
            riwayat_running.close()
            riwayat_running = open("riwayat.txt","w")
            riwayat_running.write(str(int(b[0])+1))
            riwayat_running.close()
            
        elif x == 2:
            run("expression_matter.py")
            riwayat_running = open("riwayat.txt","r")
            b = riwayat_running.readlines()
            riwayat_running.close()
            riwayat_running = open("riwayat.txt","w")
            riwayat_running.write(str(int(b[0])+1))
            riwayat_running.close()
            
        elif x == 3:
            run("consonant.py")
            riwayat_running = open("riwayat.txt","r")
            b = riwayat_running.readlines()
            riwayat_running.close()
            riwayat_running = open("riwayat.txt","w")
            riwayat_running.write(str(int(b[0])+1))
            riwayat_running.close()
            
        else:
            break
        
else:
    x = input("Apakah anda ingin running lagi? : ")
    if x.startswith("y") or x.startswith("Y") or x.startswith("i"):
        while True:
            print(" Tersedia File ".center(70,'-'))
            print("")
            print(f"""
1. Otomotif
2. Expression Matter
3. Consonant
4. Stop Program
""")
            x = int(input("File yang mana yang ingin anda jalankan ? : "))
            if x == 1:
                run("otomotif.py")
                riwayat_running = open("riwayat.txt","r")
                b = riwayat_running.readlines()
                riwayat_running.close()
                riwayat_running = open("riwayat.txt","w")
                riwayat_running.write(str(int(b[0])+1))
                riwayat_running.close()
                
            elif x == 2:
                run("expression_matter.py")
                riwayat_running = open("riwayat.txt","r")
                b = riwayat_running.readlines()
                riwayat_running.close()
                riwayat_running = open("riwayat.txt","w")
                riwayat_running.write(str(int(b[0])+1))
                riwayat_running.close()
                
            elif x == 3:
                run("consonant.py")
                riwayat_running = open("riwayat.txt","r")
                b = riwayat_running.readlines()
                riwayat_running.close()
                riwayat_running = open("riwayat.txt","w")
                riwayat_running.write(str(int(b[0])+1))
                riwayat_running.close()
                
            else:
                print(" Struktur Data ".center(70,'-'))
                print(f"""
1. Sorting
2. Searching
3. Stack
4. Queue
""")
                pilih = int(input("No berapa yang ingin anda pilih? : "))
                if pilih==1:
                    print(f"""
1. Otomotif
2. Expression Matter
3. Consonant
4. Stop Program
""")
                    inputt = int(input("No berapa yang ingin anda pilih? : "))
                    if inputt==1:
                        otomotif = open("histori.txt","r")
                        listt = otomotif.readlines()
                        inputt2 = input("Anda ingin sorting berurut dari depan atau belakang? : ")
                        if inputt2 == "depan":
                            listt.sort()
                            for i in listt:
                                print(i)
                        elif inputt2=="belakang":
                            listt.sort(reverse = True)
                            for i in listt:
                                print(i)
                        else:
                            print("Tidak ada menu selain itu")
                    elif inputt==2:
                        exp = open("express.txt","r")
                        listt = exp.readlines()
                        inputt2 = input("Anda ingin sorting berurut dari depan atau belakang? : ")
                        if inputt2 == "depan":
                            listt.sort()
                            for i in listt:
                                print(i)
                        elif inputt2=="belakang":
                            listt.sort(reverse = True)
                            for i in listt:
                                print(i)
                        else:
                            print("Tidak ada menu selain itu")

                    elif inputt==3:
                        con = open("consonant.txt","r")
                        listt = con.readlines()
                        inputt2 = input("Anda ingin sorting berurut dari depan atau belakang? : ")
                        if inputt2 == "depan":
                            listt.sort()
                            for i in listt:
                                print(i)
                        elif inputt2=="belakang":
                            listt.sort(reverse = True)
                            for i in listt:
                                print(i)
                        else:
                            print("Tidak ada menu selain itu")
                    else:
                        print("Tidak ada menu selain itu")
                elif pilih==2:
                    print(f"""
1. Otomotif
2. Expression Matter
3. Consonant
4. Stop Program
""")
                    
                    inputt = int(input("No berapa yang ingin anda pilih? : "))
                    if inputt==1:
                        otomotif = open("histori.txt","r")
                        listt = otomotif.readlines()
                        print("Data Otomotif")
                        for i,j in zip(range(1,len(listt)+1),listt):
                            print(i,j)
                        inputt2 = int(input("Anda ingin searching apa no berapa? : "))
                        try:
                            print(listt[inputt2])

                        except:
                            print("Data tidak ditemukan")
                            
                    elif inputt==2:
                        exp = open("express.txt","r")
                        listt = exp.readlines()
                        print("Data Expression Matter")
                        for i,j in zip(range(1,len(listt)+1),listt):
                            print(i,j)
                        inputt2 = int(input("Anda ingin searching apa no berapa? : "))
                        try:
                            print(listt[inputt2])
                        except:
                            print("Data tidak ditemukan")
                         
                    elif inputt==3:
                        con = open("consonant.txt","r")
                        listt = con.readlines()
                        print("Data Consonant")
                        for i,j in zip(range(1,len(listt)+1),listt):
                            print(i,j)
                        inputt2 = int(input("Anda ingin searching apa? : "))
                        try:
                            print(listt[inputt2])
                            
                        except:
                            print("Data tidak ditemukan")

                    else:
                        print("Tidak ada selain itu")

                elif pilih==3:
                    print("Stack")
                    print("1. Menambahkan data")
                    print("2. Menghapus data")
                    print("3. Jumlah keseluruhan data")
                    print("")
                    inputt = int(input("Anda mau pilih no berapa? : "))
                    if inputt==1:
                        print("Data")
                        print(f"""
1. Otomotif
2. Expression Matter
3. Consonant
""")
                        inputt2 = int(input("No berapa yang ingin anda tambah datanya? : "))
                        if inputt2==1:
                            run("otomotif.py")
                            riwayat_running = open("riwayat.txt","r")
                            a = riwayat_running.readlines()
                            riwayat_running.close()
                            riwayat_running = open("riwayat.txt","w")
                            riwayat_running.write(f"{int(a[0]) + 1}")
                            riwayat_running.close()
                        elif inputt2==2:
                            run("expression_matter.py")
                            riwayat_running = open("riwayat.txt","r")
                            a = riwayat_running.readlines()
                            riwayat_running.close()
                            riwayat_running = open("riwayat.txt","w")
                            riwayat_running.write(f"{int(a[0]) + 1}")
                            riwayat_running.close()
                        elif inputt2==3:
                            run("consonant.py")
                            riwayat_running = open("riwayat.txt","r")
                            a = riwayat_running.readlines()
                            riwayat_running.close()
                            riwayat_running = open("riwayat.txt","w")
                            riwayat_running.write(f"{int(a[0]) + 1}")
                            riwayat_running.close()
                        else:
                            print("Tidak ada selain itu")
                    elif inputt==2:
                        print("Data")
                        print(f"""
1. Otomotif
2. Expression Matter
3. Consonant
""")
                        inputt2= int(input("No berapa yang ingin anda hapus datanya? : "))
                        if inputt2==1:
                            histori = open("histori.txt","r")
                            b = histori.readlines()
                            histori.close()
                            for i,j in zip(range(len(b)),b):
                                print(i,j)
                            inputt3 = input("Mana yang ingin anda hapus")
                            if inputt3 in b:
                                for i in range(len(b)):
                                    if b[i]==inputt3:
                                        b.remove(i)
                            else:
                                print("Data tidak ditemukan")
                        elif inputt2==2:
                            exp = open("express.txt","r")
                            b = exp.readlines()
                            exp.close()
                            for i,j in zip(range(len(b)),b):
                                print(i,j)
                            inputt3 = input("Mana yang ingin anda hapus")
                            if inputt3 in b:
                                for i in range(len(b)):
                                    if b[i]==inputt3:
                                        b.remove(i)
                            else:
                                print("Data tidak ditemukan")
                        elif inputt2==3:
                            con = open("consonant.txt","r")
                            b = con.readlines()
                            con.close()
                            for i,j in zip(range(len(b)),b):
                                print(i,j)
                            inputt3 = input("Mana yang ingin anda hapus")
                            if inputt3 in b:
                                for i in range(len(b)):
                                    if b[i]==inputt3:
                                        b.remove(i)
                            else:
                                print("Data tidak ditemukan")
                        else:
                            print("Maaf tidak ada selain itu")
                    elif inputt==3:
                        print("Data")
                        print(f"""
1. Otomotif
2. Expression Matter
3. Consonant
""")
                        inputt2= int(input("No berapa yang ingin anda hapus datanya? : "))
                        if inputt2==1:
                            histori = open("histori.txt","r")
                            aa = histori.readlines()
                            histori.close()
                            bb=[]
                            for i in aa:
                                if i!='-'*70 and i!='\n':
                                    bb.append(i)
                            print("Jumlah data",len(bb))
                        elif inputt2==2:
                            exp = open("express.txt","r")
                            aa = exp.readlines()
                            exp.close()
                            bb = []
                            for i in aa:
                                if i!='\n':
                                    bb.append(i)
                            print("Jumlah data",len(bb))
                        elif inputt2==3:
                            con = open("consonant.txt","r")
                            aa = con.readlines()
                            con.close()
                            bb = []
                            for i in aa:
                                if i!='\n':
                                    bb.append(i)
                            print("Jumlah data",len(bb))
                        else:
                            print("Tidak ada selain itu")

                    else:
                        print("Tidak ada selain itu")

                elif pilih==4:
                    print("Queue")
                    print("1. Mengecek banyak data")
                    inputt = int(input("No berapa yang ingin anda pilih ? : "))
                    if inputt==1:
                        print("Data")
                        print(f"""
1. Otomotif
2. Expression Matter
3. Consonant
""")
                        inputt2 = int(input("No berapa yang ingin anda pilih ? : "))
                        if inputt2==1:
                            histori = open("histori.txt","r")
                            aa = histori.readlines()
                            histori.close()
                            bb=[]
                            for i in aa:
                                if i!='-'*70 and i!='\n':
                                    bb.append(i)
                            print("Jumlah data",len(bb))
                        elif inputt2==2:
                            exp = open("express.txt","r")
                            aa = exp.readlines()
                            exp.close()
                            bb = []
                            for i in aa:
                                if i!='\n':
                                    bb.append(i)
                            print("Jumlah data",len(bb))
                        elif inputt2==3:
                            con = open("consonant.txt","r")
                            aa = con.readlines()
                            con.close()
                            bb = []
                            for i in aa:
                                if i!='\n':
                                    bb.append(i)
                            print("Jumlah data",len(bb))
                        else:
                            print("Tidak ada selain itu")
                    else:
                        print("Tidak ada selain itu")
                else:
                    print("tidak ada selain itu")
                    
    else:
        print("ok")
        
