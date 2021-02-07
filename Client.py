class Client:
    def __init__(self, client_name, summa):
        self.client_name = client_name
        self.summa = summa

    def get_client_name(self):
        return self.client_name

    def get_summa(self):
        return self.summa

    def set_summa(self, summa):
        self.summa += summa

    def __str__(self):
        return f"{self.__class__.__name__} ({self.client_name}, {self.summa})"


class Volonter(Client):
    def __init__(self, client_name, city, status):
        super().__init__(client_name, 0)
        self.city = city
        self.status = status

    def __str__(self):
        return f"{self.__class__.__name__} ({self.client_name}, {self.city}, {self.status})"


cl = Client("Ivan", 3)
print(cl)
cl.summa = 4
print(cl)
cl.set_summa(1)
print(cl)

v1 = Volonter("Fedor", "Moscow", "Volonter")
print(v1)
v2 = Volonter("Vasia", "SPb", "Volonter 80-lvl")
print(v2)