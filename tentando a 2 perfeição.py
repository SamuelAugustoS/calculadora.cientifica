import math
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
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
            self.expressao += "//"
            text_input.text = self.expressao
        elif texto_botao in ["^", "yx"]:
            self.expressao += "**"
            text_input.text = self.expressao
        elif texto_botao == "√":
            self.expressao += "√("
            text_input.text = self.expressao
        elif texto_botao == "ex":
            self.expressao += "exp("
            text_input.text = self.expressao
        elif texto_botao in ["sin", "cos", "tan", "log"]:
            self.expressao += f"{texto_botao}("
            text_input.text = self.expressao
        elif texto_botao == "x":
            self.expressao += "*"
            text_input.text += "x"
        elif texto_botao == "(-)":
            self.expressao += "-"
            text_input.text = self.expressao
        elif texto_botao == "()":
            if not self.expressao or self.expressao[-1] in ["+", "-", "x", "÷", "^", "(", ")", "√"]:
                self.expressao += "("
            else:
                self.expressao += ")"
            text_input.text = self.expressao
        elif texto_botao == "π":
            self.expressao += str(math.pi)
            text_input.text = self.expressao
        elif texto_botao == "%":
            try:
                # Se houver um resultado anterior, calcule a porcentagem em relação a ele
                if self.resultado:
                    self.expressao = str(float(self.resultado) / 100)
                # Se não, verifique se a expressão termina com um número e, se sim, divida esse número por 100
                elif self.expressao and self.expressao[-1].isdigit():
                    index = len(self.expressao) - 1
                    while index >= 0 and self.expressao[index].isdigit():
                        index -= 1
                    numero_anterior = self.expressao[index + 1:]
                    resultado_porcentagem = float(numero_anterior) / 100
                    self.expressao = self.expressao[:index + 1] + str(resultado_porcentagem)
                # Se não houver número anterior e nenhum resultado calculado, apenas adicione "0.01" à expressão
                else:
                    self.expressao += "0.01"
                text_input.text = self.expressao
            except Exception as e:
                print(f"Erro ao lidar com o operador '%': {e}")
        elif texto_botao == "Hist":
            self.root.current = 'history'
        else:
            if texto_botao == "÷":
                texto_botao = "/"
            self.expressao += texto_botao
            text_input.text = self.expressao

    def calcular_expressao(self, expressao):
        expressao = expressao.replace("√", "math.sqrt")
        expressao = expressao.replace("sin", "sin_graus")
        expressao = expressao.replace("cos", "cos_graus")
        expressao = expressao.replace("tan", "tan_graus")
        expressao = expressao.replace("log", "math.log10")
        expressao = expressao.replace("exp", "math.exp")
        
        nomes_permitidos = {
            "math": math,
            "exp": math.exp,
            "pi": math.pi,
            "e": math.e,
            "sin_graus": sin_graus,
            "cos_graus": cos_graus,
            "tan_graus": tan_graus
        }
        
        resultado = eval(expressao, {"__builtins__": None}, nomes_permitidos)
        
        # Se a expressão contém uma das funções que devem ser formatadas como decimal
        if isinstance(resultado, float):
            if resultado.is_integer():
                resultado = int(resultado)
            else:
                resultado = round(resultado, 2)

        return str(resultado)

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
