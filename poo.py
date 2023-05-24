class Personaje:
    def __init__(self, nombre, rango):
        self.nombre = nombre
        self.rango = rango

    def atacar(self):
        pass

    def defender(self):
        pass


class Ninja(Personaje):
    def __init__(self, nombre, rango, elemento):
        super().__init__(nombre, rango)
        self.elemento = elemento

    def atacar(self):
        print(f"El ninja {self.nombre} está atacando con su elemento {self.elemento}.")

    def defender(self):
        print(f"El ninja {self.nombre} está defendiendo.")


class NinjaEspecializado(Ninja):
    def __init__(self, nombre, rango, elemento, jutsu_especial):
        super().__init__(nombre, rango, elemento)
        self.jutsu_especial = jutsu_especial

    def atacar(self):
        print(f"El ninja especializado {self.nombre} está utilizando su jutsu especial: {self.jutsu_especial}.")



ninja1 = Ninja("Naruto", "Chūnin", "Viento")
ninja2 = NinjaEspecializado("Sasuke", "Jōnin", "Rayo", "Katto")


ninja1.atacar()
ninja2.defender()

ninja2.atacar()
ninja1.defender()