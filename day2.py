from human import Human


faiz = 1.59
vade = "36"
krediAdi = "İhtiyaç Kredisi"
print(int(vade) + 10) # değişkenin türünü değiştirme  --- String bir ifade int ifadesine dönüşebilecek yapıda olması lazım 
print("----------------------------------------------------------------------")

vade = 36#int(input("Lütfen istediğiniz vade miktarını giriniz : "))
print(vade)
vade = vade + 12

print("----------------------------------------------------------------------")
#string interpolation
# 12 ve 13 satır aynı görevi görüyor sadece birinde tip dönüşümü yaptık diğerinde "format" fonksiyonunu kullandık
print("Sçtiğiniz vade sonucu ortaya çıkan vade : " + str(vade))
print("Sçtiğiniz vade sonucu ortaya çıkan vade : {vadeSayisi}".format(vadeSayisi=vade))

print("----------------------------------------------------------------------")
isim = "Burak"#input("İsim Giriniz : ")
metin = "Merhaba {name}".format(name = isim)
print(metin)

print("----------------------------------------------------------------------")
#f-string
metin = f"Hoşgeldiniz {isim}"
print(metin)

print("----------------------------------------------------------------------")

# listeler ve döngüler
dizi =["İhtiyaç Kredis" , 10 , 2.5] #listelerde farklı formattaki veriler tutulabilir 
print(dizi)

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
print(krediler[0])
print(len(krediler)) #listenin eleman sayısını gösterir

krediler.append("Özel Kredi") # Bir listeye yeni bir eleman eklemek için kullanılır listenin en sonuna ekler !!
print(krediler)

krediler.append("X Kredisi")
print(krediler)

krediler.pop() #Listeden eleman siler, eğer index yazılmaz ise son elemanı siler
print(krediler)

krediler.append("Taşıt Kredisi")
print(krediler)

krediler.remove("Taşıt Kredisi") # pop fonkiyonu index bazlı çalışırken remove fonkiyonu değer bazlı çalışır
print(krediler)

krediler.extend(["Y Kredisi" , "Z Kredisi"]) # Birden fazla eleman eklemek için kullanılır
print(krediler)


#for

for i in range(10):
    print(i)

print("**************************************")

for i in range(5,10): # istediğin elemandan başlayıp istediğin elemanda bitiri
    print(i)

print("**************************************")

for i in range(0,51,10): # Bunda ise 0 sayısından 50 sayısına kadar 10'ar 10'ar arttırı
    print(i)

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
for kredi in krediler:
    print(kredi)

print("**************************************")

for i in range(len(krediler)):
    print(krediler[i])

print("**************************************")

i = 0
while i < 10:
    print("x")
    i = i + 1
print("y")

print("**************************************")
while True:
    print("x")
    break
print("**********Son Döngü**************")

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
i = 0
while i < len(krediler):
    i += 1
    print(krediler[i])
    if krediler[i] == "Konut Kredisi":
        break

#fonksiyonlar

def calculate():
    print(100 - 20)

def calculateWithParams(fiyat,indirim):
    print(fiyat - indirim)

def sayHello(name):
    print(f"Merhaba {name}")

calculate()
calculateWithParams(50,10)
sayHello("Burak")

def calculateAndReturn(price,discount):
    return price - discount

yeniFiyat = calculateAndReturn(200,50)
print(yeniFiyat + 10)

def calculatePrice(price,discount):
    print(price-discount)

def calculatePriceAndReturn(price,discount):
    return price-discount

print("*****************************")
fonk1 = calculatePrice(100,50)
fonk2 = calculatePriceAndReturn(300,100)
print(fonk1)
print(fonk2)
print("*****************************")

human1 = Human("Burak")
#human1.name = "Enes"
human1.talk("Merhaba")
human1.walk()
print(human1)

human2 = Human("Halit")
#human2.name = "Cem"
human2.talk("Selam")
human2.walk()
print(human2)

Human("Melike").talk("Merhaba")