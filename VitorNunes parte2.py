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
