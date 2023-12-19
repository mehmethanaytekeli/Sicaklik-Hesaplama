derece=int(input("kaç derece?"))
deger1=int(input("1(Celsius) 2(Fahrande) 3(Kelvin)"))
deger2=int(input("1(Celsius) 2(Fahrande) 3(Kelvin)"))
def fahcf(derece):
    return ((derece/100)*180)+32
def fahkf(derece):
    return (((derece-273)/100)*180)+32
def celfc(derece):
    return ((derece-32)/180)*100
def celkc(derece):
    return ((derece-273)/100)*100
def kelcf (derece):
    return ((derece/100)*180)+32
def kelkf (derece):
    return (((derece-273)/100)*180)+32
if (deger1==1 and deger2==1):
    print("celsiustan celsiusa dönüşümün cevabı aynıdır")
elif (deger1==1 and deger2==2):
    print(fahcf(derece))
elif (deger1==1 and deger2==3):
    print(kelcf(derece))
elif (deger1 == 2 and deger2 == 2):
    print("fahrandeden fahranedeye dönüşümün cevabı aynıdır")
elif (deger1 == 2 and deger2 == 1):
    print(celfc(derece))
elif (deger1 == 2 and deger2 == 3):
    print(kelkf(derece))
elif (deger1 == 3 and deger2 == 3):
    print("kelvinden kelvine dönüşümün cevabı aynıdır")
elif (deger1 == 3 and deger2 == 1):
    print(celkc(derece))
elif (deger1 == 3 and deger2 == 2):
    print(celfc(derece))
else:
    print("deger yanlış")