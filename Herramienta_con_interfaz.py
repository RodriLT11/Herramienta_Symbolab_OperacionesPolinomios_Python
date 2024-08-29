from sympy import *
from typing import List
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora de Simplificacion de Polinomios")

        self.label = QLabel()
        self.button = QPushButton("Solucion")
        self.button2 = QPushButton("Instrucciones")
        self.button.clicked.connect(self.boton1)
        self.button2.clicked.connect(self.boton2)
        self.textbox = QLineEdit()
        # self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.textbox)
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        layout.addWidget(self.button2)

        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

    def boton1(self):
        textboxValue1 = self.textbox.text()
        textboxValue1 = str(self.textbox.text())
        Separar = Polinomio.sepTerm(self, textboxValue1)
        Symp = Polinomio.Order_terms(self, Separar)
        Separar = str(Separar)
        Symp = str(Symp)
        QMessageBox.question(self, 'Solucion', "Simplificacion de:    " + textboxValue1 + "   Es: \n" +
                             "Ordenado de menor a mayor    " + Separar + "\nTerminos ordenados:" + Symp, QMessageBox.Ok)

    def boton2(self):
        self.label.setText(
            "ingresa para solo la x un 1 al principio ejemplo: (1x)*(1x) \n ingresa para la division parentesis ejemplo: (1x)/(1x), Solo usa una variable (1x)")

class Polinomio():
    def _init_(self, textboxValue1):
        self.Poly = textboxValue1

    def sepTerm(self, textboxValue) -> list:
        # quitar los space
        self.Poly = textboxValue.replace(' ', '')
        self.term = []
        self.numbPar = 0
        self.termA = ''

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
                elif self.charA == '+' or self.charA == '-' or self.charA == '/' or self.charA == '*':
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
        return self.term

    def Order_terms(self, b):
        self.termstts = "".join(map(str, b))
        b = sorted(self.termstts, reverse=True)
        
        b = self.termstts.replace("x", "*x")
        
        b = b.replace('^', '**')
        
        b = simplify(b)
        b_str = str(b)
        b_str = b_str.replace('*x', 'x')
        b_str = b_str.replace('**', '^')
        return b_str


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
