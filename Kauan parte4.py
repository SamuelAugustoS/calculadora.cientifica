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
        expressao = expressao.replace("^", "**")
        expressao = expressao.replace("Mod", "%")
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
        resultado = eval(expressao, {"_builtins_": None}, nomes_permitidos)
        if isinstance(resultado, float):
            if resultado.is_integer():
                resultado = int(resultado)
            else:
                resultado = round(resultado, 2)
        return str(resultado)

    def converter_porcentagens(self, expressao):
        padrao = re.compile(r'(\d+(\.\d+)?)%')
        return padrao.sub(r'(\1/100)', expressao)
