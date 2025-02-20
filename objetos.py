from pprint import pprint

def semaforo(colores):
    colores = colores.lower()
    acceso = "Eso no es un color"
    if colores=="verde":
        acceso="Puede pasar"
    elif colores== "rojo":
        acceso="No puede pasar"
    elif colores == "amarillo":
        acceso="espere"
    return acceso

#print(semaforo("RoJO"))


ejemplo = {
    "direccion": "https://www.youtube.com/user",
    "usuario": {
        "id": 34567,
        "user": "joaquinbonita31",
        "password": "joaquin_la_mas_bonita_de_peru",
    },
    "historial": ["www.pronhub.com", "www.stackoverflow.com", "www.youtube.com"]
}

print(ejemplo["historial"][0])
print(ejemplo["usuario"]["id"])
usuario = ejemplo["usuario"]["user"]

def validar_contraseña(nombre):
    usuario = ejemplo["usuario"]["user"]
    contraseña = ejemplo["usuario"]["password"]
    if nombre in usuario and nombre in contraseña:
        return "La contraseña es correcta"
    else:
        return "La contraseña NO es correcta"

test = validar_contraseña("joaquin")
print(test)

def cambiar_contraseña():
    contraseña=ejemplo["usuario"]["password"] + "123"
    ejemplo["usuario"]["password"]=contraseña
    return contraseña
print(cambiar_contraseña())
pprint (ejemplo)

 
class Perro:
    raza="Pitbull"

    def ladrar(self):
        return "Guau"

coco=Perro()
print(coco.raza)
print(coco.ladrar())


class Animal:
    def __init__(self, especie, nombre, edad):
        self.especie = especie
        self.nombre = nombre
        self.edad = edad
        if self.edad < 0:
            self.edad = "Esa edad no es valida"

    def comer(self, alimento):
        alimentos_permitidos = ("pienso", "carne", "chaufa")
        if alimento in alimentos_permitidos:
            print(f"El {self.especie} que se llama {self.nombre} esta comiendo {alimento}")
        else:
            print("Eso no se lo come ni harto vino")

coco = Animal("gato", "Coco", 4)
coco.comer("carne")

class Persona:
    def __init__(self,nombre,edad,trabajo):
        self.nombre = nombre
        self.edad = edad
        self.trabajo = trabajo

    def chambear(self,lugar):
        print(f"El nombre es {self.nombre} esta trabajando {self.trabajo} en {lugar}")


class Enamorado(Persona):
    def besarse(self,enamorado):
        print(f"{self.nombre} esta besando a {enamorado.nombre}")


josi= Enamorado("Josi",31,"Analista de datos")
Joaquin = Enamorado("Joaquin", 30,"Programador")

Joaquin.chambear("En su casa")
josi.besarse(Joaquin)

class Edificio():
    def __init__(self,tipo,direccion):
        self.tipo=tipo
        self.direccion=direccion

class Hospital(Edificio):
    def curar_enfermos(self,persona):
        print(f"Estoy curando a {persona.nombre}")


class pokemones:
    def __init__(self,nombre,vida = 100):
        self.nombre=nombre
        self.vida = vida

    def pelear(self,otro):
        self.vida = self.vida - 10  # El que pega -10 vida
        otro.vida = otro.vida - 20  # Y el que recibe -20 vida
        self._vivo_o_muerto()  # Compruebo si YO me he muerto
        otro._vivo_o_muerto()  # Compruebo si EL OTRO ha muerto
        print(f"El pokemon {self.nombre} esta peleando con {otro.nombre} ")

    def _vivo_o_muerto(self):  # Esto comprueba si un pokemon muere
        if self.vida <= 0:
            print("El pokemon ha muerto")
            self.vida = 0

class agua(pokemones):
    tipo="agua"

class fuego(pokemones):
    tipo="fuego"
 
class aire(pokemones):
    tipo="aire"


pescado=agua("brayan")
volcan=fuego("llamita")
huracan=aire("viento")

pescado.pelear(huracan)
pescado.pelear(huracan)
volcan.pelear(huracan)
volcan.pelear(huracan)
volcan.pelear(huracan)
volcan.pelear(huracan)
volcan.pelear(huracan)
volcan.pelear(huracan)
print(pescado.vida)
print(huracan.vida)

