from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock

from cronometro import Cronometro

# Telas
class HomeScreen(Screen):
    # tela conterá relógio mundial
    pass

class AlarmeScreen(Screen):
    # multiplos alarmes, definir horário/data de cada um.
    pass

class CronometroScreen(Screen):
    # cronometro unico, contar infinitamente até pause ou encerramento
    pass

class TemporizadorScreen(Screen):
    # contagem regressiva, regredir de valor definido antes do inicio do cronometro
    pass

class PresetScreen(Screen):
    # contagem regressiva customizada
    pass

class CronosApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cronometro = Cronometro()
        
    def build(self):
        # Define o tema escuro
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"

        return Builder.load_file('interface.kv')

    def iniciar_cronometro(self):
        self.cronometro.iniciar(self.root.get_screen('cronometro').ids.cronometro_tempo)

    def pausar_cronometro(self):
        self.cronometro.pausar()

    def resetar_cronometro(self):
        self.cronometro.resetar(self.root.get_screen('cronometro').ids.cronometro_tempo)

# Executa o aplicativo
if __name__ == '__main__':
    CronosApp().run()
