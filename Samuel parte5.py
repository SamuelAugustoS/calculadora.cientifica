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
    
