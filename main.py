class Telefon:
    def __init__(self, model, batareya):
        self.model = model
        self.__batareya = batareya

    def zaryad_qil(self, foiz):
        if self.__batareya + foiz <= 100:
            self.__batareya += foiz
        else:
            self.__batareya = 100
            print("Batareya 100% bo'ldi")

    def foydalan(self, foiz):
        if foiz <= self.__batareya:
            self.__batareya -= foiz
        else:
            print("Batareya yetarli emas")

    def info(self):
        print(f"Model: {self.model}")
        print(f"Batareya: {self.__batareya}%")


t1 = Telefon("iPhone 15", 50)

t1.info()

t1.zaryad_qil(30)
t1.info()

t1.foydalan(60)
t1.info()
