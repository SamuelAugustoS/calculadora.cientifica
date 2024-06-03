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

class CalculatorApp(App):
    def build(self):
        Window.size = (400, 600)
        self.expressao = ""
        self.resultado = ""
        self.historico = []
        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(CalculatorScreen(name='calculator'))
        self.screen_manager.add_widget(HistoryScreen(name='history'))
        return self.screen_manager

    def on_button_press(self, instance):
        texto_botao = instance.text
        text_input = self.root.get_screen('calculator').ids.text_input

        if texto_botao == "=":
            try:
                self.resultado = self.calcular_expressao(self.expressao)
                self.historico.append(f"{self.expressao} = {self.resultado}")
                self.atualizar_historico()
                self.expressao = self.resultado
            except Exception as e:
                self.resultado = "Erro"
                print(f"Erro: {e}")
            text_input.text = self.resultado
        elif texto_botao == "<-":
            self.expressao = self.expressao[:-1]
            text_input.text = self.expressao
        elif texto_botao == "C":
            self.expressao = ""
            self.resultado = ""
            text_input.text = ""
        elif texto_botao == "Mod":
            self.expressao += " Mod "
            text_input.text = self.expressao
        elif texto_botao in ["^", "yx"]:
            self.expressao += "^"
            text_input.text = self.expressao
        elif texto_botao == "√":
            self.expressao += "√("
            text_input.text = self.expressao
        elif texto_botao == "ex":
            self.expressao += "ex("
            text_input.text = self.expressao
        elif texto_botao in ["sin", "cos", "tan", "log"]:
            self.expressao += f"{texto_botao}("
            text_input.text = self.expressao
        elif texto_botao == "x":
            self.expressao += "x"
            text_input.text = self.expressao
        elif texto_botao == "(-)":
            self.expressao += "-"
            text_input.text = self.expressao
        elif texto_botao == "()":
            if not self.expressao or self.expressao[-1] in ["+", "-", "*", "/", "^", "(", ")", "√"]:
                self.expressao += "("
            else:
                self.expressao += ")"
            text_input.text = self.expressao
        elif texto_botao == "π":
            self.expressao += str(math.pi)
            text_input.text = self.expressao
        elif texto_botao == "%":
            self.expressao += "%"
            text_input.text = self.expressao
        elif texto_botao == "Hist":
            self.root.current = 'history'
        else:
            if texto_botao == "÷":
                texto_botao = "/"
            self.expressao += texto_botao
            text_input.text = self.expressao.replace("/", "÷")

    def calcular_expressao(self, expressao):
        expressao = expressao.replace("x", "*")
        expressao = expressao.replace("√", "math.sqrt")
        expressao = expressao.replace("sin", "sin_graus")
        expressao = expressao.replace("cos", "cos_graus")
        expressao = expressao.replace("tan", "tan_graus")
        expressao = expressao.replace("log", "math.log10")
        expressao = expressao.replace("exp", "math.exp")
        expressao = expressao.replace("ex", "ex")
        expressao = expressao.replace("÷", "/")

        # Substitua "Mod" por "%"
        expressao = expressao.replace("Mod", "%")

        # Substitua porcentagens pela operação correta
        expressao = self.converter_porcentagens(expressao)
        
        nomes_permitidos = {
            "math": math,
            "exp": math.exp,
            "pi": math.pi,
            "e": math.e,
            "sin_graus": sin_graus,
            "cos_graus": cos_graus,
            "tan_graus": tan_graus,
            "ex": ex
        }
        
        resultado = eval(expressao, {"__builtins__": None}, nomes_permitidos)
        
        # Se a expressão contém uma das funções que devem ser formatadas como decimal
        if isinstance(resultado, float):
            if resultado.is_integer():
                resultado = int(resultado)
            else:
                resultado = round(resultado, 2)

        return str(resultado)

    def converter_porcentagens(self, expressao):
        # Encontra todas as ocorrências de números seguid
        padrao = re.compile(r'(\d+(\.\d+)?)%')
        # Substitui 'n%' por 'n/100'
        return padrao.sub(r'(\1/100)', expressao)

    def atualizar_historico(self):
        history_label = self.root.get_screen('history').ids.history_label
        history_label.text = '\n'.join(self.historico)

    def back_to_calculator(self):
        self.root.current = 'calculator'


class CalculatorScreen(Screen):
    pass


class HistoryScreen(Screen):
    pass


if __name__ == "__main__":
    CalculatorApp().run()
