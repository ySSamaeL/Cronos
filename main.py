from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock

# Telas
class HomeScreen(Screen):
    # tela conterá relógio mundial
    pass

class AlarmeScreen(Screen):
    # multiplos alarmes, definir horário/data de cada um.""
    pass

class CronometroScreen(Screen):
    # cronometro unico, contar infinitamente até pause ou encerramento" 
    pass

class TemporizadorScreen(Screen):
    # contagem regressiva, regredir de valor definido antes do inicio do cronometro"
    pass

class PresetScreen(Screen):
    # contagem regressiva customizada
    pass

class CronosApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cronometro_tempo = 0
        self.cronometro_milisec = 0
        self.cronometro_segundos = 0

        self.temporizador_segundos = 0
        self.temporizador_milisec = 0
        
        self.cronometro_event = None
        self.temporizador_event = None
            
    def build(self):

        # Define o tema escuro
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"

        # Carrega o arquivo KV
        return Builder.load_file('interface.kv')

    def iniciar_cronometro(self):
        if not self.cronometro_event:
            self.cronometro_event = Clock.schedule_interval(self.atualizar_cronometro, 0.001)
    

    def pausar_cronometro(self):
        if self.cronometro_event:
            self.cronometro_event.cancel()
            self.cronometro_event = None

    def resetar_cronometro(self):
        self.pausar_cronometro()
        self.cronometro_tempo = 0
        self.cronometro_milisec = 0
        self.cronometro_segundos = 0
        self.root.get_screen('cronometro').ids.cronometro_tempo.text = '00:00:00:000'

    def atualizar_cronometro(self, dt):

        # Atualizamos o delta tempo com os milissegundos como parte decimal)
        self.cronometro_tempo += dt
        self.cronometro_segundos = int(self.cronometro_tempo)

        # Calcula horas, minutos, segundos e milissegundos
        horas, resto = divmod(self.cronometro_segundos, 3600)  # Converte para inteiro
        minutos, segundos = divmod(resto, 60)
        milissegundos = int((self.cronometro_tempo - self.cronometro_segundos) * 1000)  # Extrai os milissegundos

        # Atualiza o texto com formatação adequada
        self.root.get_screen('cronometro').ids.cronometro_tempo.text = (f"{horas:02}:{minutos:02}:{segundos:02}:{milissegundos:03}")


# Executa o aplicativo
if __name__ == '__main__':
    CronosApp().run()

