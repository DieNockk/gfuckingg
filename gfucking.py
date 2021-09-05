import time

secilen_islem = int(input("""
-----------------------------
         DieNock's
         made   it
             ! 

        1. SQL scanner
        2. nmap port and script scanner
-----------------------------
"""))



if secilen_islem == 1:
    print(" Sql taraması başlatılıyor")
    time.sleep(3)
    istek_ip = int(input(" Tarama yapılıcak ip'i giriniz : "))
    time.sleep(2)
    print("ip taranıyor....")
    time.sleep(2)
    print("Sonuç : ")


elif secilen_islem == 2:
    print("Nmap taraması başlatılıyor")
    time.sleep(3)
    nmap_ip = int(input(" Taranıcak ip'i giriniz : "))
    time.sleep(2)
    print("İp taranıyor.....")
    time.sleep(2)
    print(" Sonuç ")

breakpoint
