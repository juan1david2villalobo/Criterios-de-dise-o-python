""" La clase padre se llama "ser", que tiene un (nombre, y apellidos)  y dos  métodos:


Luego defino la clase robot, que hereda de la clase "ser", con un método nuevo llamado "calculista" y redefine el método ver.

La clase humano, que también es heredada de "ser",  y define el método "calculista".

En el programa principal, se usa una variable "Lista" que contiene los dos objetos que creo (r1, y r2) que aunque son de distinto tipo, se pueden añadir a la lista sin ningún problema. """

""" se usa el principio de diseño de UNA VEZ Y SOLO UNA VEZ ya que se evita la duplicacion de logica
 se usa la ley de DEMETER ya que se miminiza el acoplamiento
  y los demas criterios como los son minima sorpresa, simplicidad, resta etc """
class ser():
    nombre=""
    apellidos=""
    def nombre(self,n,a):
        self.nombre=n
        self.apellidos=a
    def ver(self):
        print self.nombre , self.apellidos
 
class robot(ser):
    def calculista(self):
        print "mis calculos son veloces"
    def ver(self):
        print "Soy un robot...",self.nombre , self.apellidos
 
 
class humano(ser):
    def calculista(self):
        print "calculo a mano"
 
def main():
    lista = []
    r1=robot()
 
    r1.nombre("R2","D2")
    r2=humano()
    r2.nombre("Juan","villalobo")
 
    r2.ver()
    r2.calculista()
 
    r1.ver()
    r1.calculista()
 
    lista.append(r1)
    lista.append(r2)
 
    print "Listado...."
    lista[0].ver()
    lista[0].calculista()
 
    lista[1].ver()
    lista[1].calculista()
    pass
 
if __name__ == '__main__':
    main()

