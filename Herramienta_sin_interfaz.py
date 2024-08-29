
from sympy import *
class Polinomio(object):
    def __init__(self, a):
        self.Poly=a
        
    def sepTerm(self,a) -> list:

        # quitar los space
        self.Poly=a.replace(' ','')
        self.term=[]
        self.numbPar=0
        self.termA=''
    
        #Aplicarlo para cada elemento del polinomio
        for i in range(len(self.Poly)):
            self.charA = self.Poly[i]
            # Siempre que empiece el primer termino sera el primero
            if i == 0:
                self.termA = self.termA + self.charA
            # Para el ultimo caracter 
            elif i == len(self.Poly) - 1:
                self.termA = self.termA + self.charA
                self.term.append(self.termA)
            # Para otros caracteres
            else:
                # Si se encuentra parentesis, actualizamos el valor de numeroParentesis
                if self.charA == '(':
                    self.numbPar += 1
                    self.termA = self.termA + self.charA
                elif self.charA == ')':
                    self.numbPar -= 1
                    self.termA = self.termA + self.charA
                # Si se encuentra operador '+' o '-'
                elif self.charA == '+' or self.charA == '-' or self.charA == '/' or self.charA=='*':
                    # Si estamos dentro de parentesis
                    if self.numbPar > 0:
                        self.termA = self.termA + self.charA
                    # Si estamos fuera de parentesis, crea un nuevo termino
                    else:
                        self.term.append(self.termA)
                        self.termA = self.charA
                # Otros caracteres
                else:
                    self.termA = self.termA + self.charA
        print(self.term)
        return self.term 

    def Order_terms(self, b):
        self.termstts="".join(map(str, b))
        b=sorted(self.termstts)
        b=self.termstts.replace("x", "*x")
        b=b.replace('^', '**')
        b=simplify(b)
        print(b)

class FuncionPrincipal(object):
    Poly1=Polinomio(None)
    print("\n")
    print("Para la division, ingrese sus terminos entre parentesis, por ejemplo (x)/(x) ")
    print("Para la multiplicacion, ingrese sus terminos entre parentesis, por ejemplo (x)*(x) ")
    print("Solo ingresar la x como variable para los polinomios \n")
    a = input("ingresa tu polinomio \n")  
    b=Poly1.sepTerm(a)
    Poly1.Order_terms(b)


