while 1:
    print("""
    [1] Toplama
    [2] Çıkarma
    """)
    sayi = input("Lütfen yapmak istediğiniz işlemi tuşlayın: ")
    if sayi.isdigit():
        if sayi == "1":
            top1 = input("İlk sayıyı giriniz: ")
            top2 = input("İkinci sayıyı giriniz: ")
            if top1.isdigit():
              if top2.isdigit():
                top1 = float(top1)
                top2 = float(top2)
                print(top1 + top2)
                while 8:
                    print("Başa alalım mı?")
                    cvp1=input("Evet için [e], hayır için [h] yazınız.")
                    if cvp1 in ("e", "evet", "y","yes"):
                        break
                    elif cvp1 in ("h","hayır","no","n"):
                        print("Uygulamadan çıkıyorum...")
                        quit()
                    else:
                        print("Lütfen geçerli bir cevap giriniz.")
                        continue
              else:
                print("Lütfen sayı giriniz.")
            else:
                print("Lütfen sayı giriniz.")
                continue
        elif sayi == "2":
            cik1 = input("Lütfen ilk sayıyı giriniz: ")
            cik2 = input("Lütfen ikinci sayıyı giriniz: ")
            if cik1.isdigit():
                if cik2.isdigit():
                    while 3:
                        print("[1] =",cik1,"sayısından",cik2,"sayısını çıkarmak istiyorum")
                        print("[2] =",cik2,"sayısından",cik1,"sayısını çıkarmak istiyorum")
                        gir=input("lütfen yanıtınızı giriniz: ")
                        if gir in ("1","bir","b","one"):
                            cik1 = float(cik1)
                            cik2 = float(cik2)
                            print(cik1 - cik2)
                            while 4:
                                tekrar = input("Başa alalım mı? [e] = evet, [h] hayır: ")
                                if tekrar in ("e","evet","yes"):
                                    break
                                elif tekrar in ("h", "hayır", "no"):
                                    print("Programdan çıkılıyor...")
                                    quit()
                                else:
                                    print("Lütfen geçerli bir cevap veriniz.")
                                    continue
                        elif gir in ("2","iki","two"):
                            print(float(cik2) - float(cik1))
                            tekrar = input("Başa alalım mı? [e] = evet, [h] hayır: ")
                            if tekrar in ("e","evet","yes"):
                                break
                            elif tekrar in ("h", "hayır", "no"):
                                print("Programdan çıkılıyor...")
                                quit()
                            else:
                                print("Lütfen geçerli bir cevap veriniz.")
                                continue
                            break
                        else:
                            print("Lütfen geçerli bir sayı giriniz!")
                            continue
                        break
                else:
                    print("Lütfen sayı giriniz.")
                    continue
            else:
                print("Lütfen sayı giriniz.")
                continue
        else:
            print("Lütfen 1 veya 2 yazınız!")
            continue
    elif sayi == "":
        print("Alanı boş bırakmayınız!")
        continue
    else:
        print("Lütfen bir sayı giriniz!")
        continue