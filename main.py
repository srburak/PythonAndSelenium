print("burak")
#string
title = "Taşıt Kredisi"
print(title)
title = "İhtiyaç Kredisi"
print(title)

#int
maturity = 36
ekvade = 6

#float
monthlyPayment  = 200.50

#bool
yukselisteMi = False

# matamatiksel oparetörler (+,-,*,/)
print(ekvade + maturity)
print(ekvade - maturity)
print(ekvade * maturity)
print(maturity / ekvade)

# % => mod operatörü
print(maturity % 5)


yeniVade = maturity / 2
fiyat = 100
indirimliFiyat = fiyat - 20
print(yeniVade)
print(indirimliFiyat)

# Mantıksal opertörler (True and False)
print(1 == 1) # Eşittir
print(1 <= 2) # Büyük eşit
print(1 < 2) # Büyük
print(1 >= 2) # Kücük eşit
print(1 > 2) # Kücük
print(1 != 1) # Eşit olmama
print(1 != 2) # Eşit olmama

# or , and

#or => veya
print(1 > 2 or 5 > 2)

#and => ve
print(1 > 2 and 5 > 2)
print(1 > 2 or 5 > 2 and 3 > 2)

print(1 > 2 and 5 > 2 or 3 > 2)
print(1 > 2 and 5 > 2 and 3 > 2)

# Karar Yapıları (if , else)
sayi1 = 20
sayi2 = 20

if sayi1 > sayi2:
    print("sayi 1 sayi 2 büyüktür")
elif sayi1 == sayi2:
    print("İki sayi eşittir")
else:
    print("sayi 1 sayi 2 den küçüktür")