    def calcular_expressao(self, expressao):
        expressao = expressao.replace("√", "math.sqrt")
        expressao = expressao.replace("sin", "sin_graus")
        expressao = expressao.replace("cos", "cos_graus")
        expressao = expressao.replace("tan", "tan_graus")
        
        nomes_permitidos = {
            "math": math,
            "exp": math.exp,
            "log": math.log10,
            "pi": math.pi,
            "e": math.e,
            "sin_graus": sin_graus,
            "cos_graus": cos_graus,
            "tan_graus": tan_graus
        }
        resultado = eval(expressao, {"__builtins__": None}, nomes_permitidos)
        return "{:.2f}".format(resultado)

class CalculatorScreen(Screen):
    pass

class HistoryScreen(Screen):
    pass

if __name__ == "__main__":
    CalculatorApp().run()
