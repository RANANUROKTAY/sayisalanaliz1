#02220224004 - RANA NUR OKTAY - İLK ÖDEV
cos=0.809016994
(print("\n"))
print("--- Cos fonksiyonunu Taylor Serisi ile acmak ---")
print("Cos(π/5) fonksiyonunun gercek degeri =0,809016994\n")
pi= 3.1415926535
print("π sayimiz=")
print(pi)

print("\nCos fonksiyonu icin Taylor Serisi=")
print("1-(x**2/2!)+(x**4/4!)-(x**6/6!)+(x**8/8!).....+([-1]**n])*(x**2n)/(2n)!....  seklindedir.")
print("Burada x yerine π/5 ifadesini koyup oyle islem yapacagiz.\n")
print("Eger tek terim acacaksak:")
dict1 = {'TerimTuru': 'TekAdet','Hata Orani':'TekliHata'}
print(dict1)
print("Cos fonksiyonunun tek terim icin degeri 1-(x**2/2!) formulu ile hesaplanir. ")
A=0.802607912
teklisonuc=cos-A
print("Bu deger= 0.802607912 dir.")
print("Kesme hatamiz su formulle hesaplanır = (Kesme Hatasi=Gercek Deger-Hesaplanan Deger)")
print("Yani hata payımız=")
print(teklisonuc)
dict1 = {'TerimTuru': 'TekAdet','Hata Orani':'0.00640908200000001'}
print(dict1)
print("\n")
print("Eger iki terim acacaksak:")
dict2 = {'TerimTuru': 'IkiAdet','Hata Orani':'IkiliHata'}
print(dict2)
print("Cos fonksiyonunun iki terim icin degeri 1-(x**2/2!)+(x**4/4!) formulu ile hesaplanir. ")
print("Bu deger= 0.809101851 dir.")
B=0.809101851
ikilisonuc=cos-B
print("Kesme hatamiz yine formulle hesaplanır.)")
print("Yani hata payımız=")
print(ikilisonuc)
dict2 = {'TerimTuru': 'IkiAdet','Hata Orani':'-8.485699999993823e-05'}
print(dict2)
print("Bu deger hatalidir.")





