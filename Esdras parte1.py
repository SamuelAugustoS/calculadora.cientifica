import math
import re
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.metrics import dp

# Função para converter graus em radianos
def graus_para_radianos(angulo_graus):
    return math.radians(angulo_graus)

# Ajuste das funções trigonométricas para calcular em graus
def sin_graus(angulo_graus):
    return math.sin(graus_para_radianos(angulo_graus))

def cos_graus(angulo_graus):
    return math.cos(graus_para_radianos(angulo_graus))

def tan_graus(angulo_graus):
    return math.tan(graus_para_radianos(angulo_graus))

def ex(numero):
    return math.exp(numero)
