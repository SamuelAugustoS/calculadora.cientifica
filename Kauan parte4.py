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
        # Aqui continuariam as demais condições...
