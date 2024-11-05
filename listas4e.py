class Nodo:
    def __init__(self):
        self.dato=None
        self.otro=None

    def setDato(self,valor):
        self.dato = valor

    def setOtro(self,valor):
        self.otro = valor

# def buscar(val):  #este metodo no se puede hacer dentro de la clase pq en la clase NOdo no se puede crear mas de un valor
#     a=x
#     t=False
#     while a !=None:
#         if a.dato == val:
#             t=True
#         a=a.otro
#     return t
class  BagNodo:
    def __init__(self):
        self.raiz=Nodo()
        self.primero=True

    def mostrar(self):
        a=self.raiz
        print(a.dato)
        while a != None:
            a=a.otro
            if a != None:
                print(a.dato)

    def buscar(self,val):  #este metodo no se puede hacer dentro de la clase pq en la clase NOdo no se puede crear mas de un valor
        a=self.raiz
        t=False
        while a !=None and not(t):
            if a.dato == val:
                t=True
            a=a.otro
        return t

    def agregar(self,val):
        if self.primero:
            self.raiz.setDato(int(val))
            a=self.raiz
            self.primero=False
        else:
            ne=Nodo()
            ne.setDato(int(val))
            a=self.raiz
            while a.otro !=None:
                a=a.otro
            a.otro=ne

    def promedio(self):
        c=0
        s=0
        t=self.raiz
        while t is not None:
            s+=t.dato
            c+=1
            t=t.otro
        return s/c
        
    
    def borrar(self,val):
        a=self.raiz
        while a != None:
            a=a.otro
            if a == val:
                self.agregar(None)
    def length(self): #SACAR EL TAMAÑO DE LA LISTA
        c=0
        t=self.raiz
        while t != None:
            c+=1
            t=t.otro
        return c
    #encontrar el minimo
    def minimo(self):
        if not self.raiz or self.raiz.dato is None:
            print("La lista está vacía.")
            return None
        min_val = self.raiz.dato
        t = self.raiz.otro
        while t :
            if t.dato < min_val:
                min_val = t.dato
                t = t.otro
        return min_val
    def prom(self):
        suma = 0
        tam = self.t 
        for i in range(self.t):
            x = self.show(i)
            if x is not None:
                suma += int(x)
                return suma / tam if tam > 0 else None



# print(x.dato)
# print(x.otro.dato)




# v=int(input("Introduce el valor a buscar: "))
# if buscar(v):
#     print("El valor existe")
# else:
#     print("El valor no existe")