import math
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.metrics import dp

# Função para converter graus em radianos
def graus_para_radianos(angulo_graus):
    return math.radians(angulo_graus)
