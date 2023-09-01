class Human:
    #name = "Burak"
    def __init__(self,name):
        self.name = name
        print("Bir Human instance'i üretildi!!!")
    def __str__(self):
        return f"STR Fonksiyonundan dönen değer : {self.name}"
    def talk(self,sentence):
        print(f"{self.name} : {sentence}")
    def walk(self):
        print("Human is walk...")