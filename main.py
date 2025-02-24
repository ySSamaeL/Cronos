from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
import datetime

from cronometro import Cronometro
from temporizador import Temporizador
from alarme import Alarme

Window.size = (450, 750)

# Telas
class HomeScreen(Screen):
    pass

class AlarmeScreen(Screen):
    pass

class CronometroScreen(Screen):
    pass

class TemporizadorScreen(Screen):
    pass

class PresetScreen(Screen):
    pass

class CronosApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cronometro = Cronometro()
        self.temporizador = Temporizador()
        self.alarme = Alarme()
        
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"

        root = Builder.load_file('interface.kv')
        self.alarme.display_widget = root.get_screen('alarme').ids.alarme_layout
        return root

    def on_start(self):
        self.iniciar_relogio()

        temporizador_screen = self.root.get_screen('temporizador')
        horas_display = temporizador_screen.ids.horas
        minutos_display = temporizador_screen.ids.minutos
        segundos_display = temporizador_screen.ids.segundos
        self.temporizador.definir_tempo(0, 0, 0, horas_display, minutos_display, segundos_display)

    def iniciar_relogio(self):
        Clock.schedule_interval(self.atualizar_relogio, 1)

    def atualizar_relogio(self, *args):
        self.root.get_screen('home').ids.relogio.text = datetime.datetime.now().strftime('%H:%M:%S')

    def iniciar_cronometro(self):
        self.cronometro.iniciar(self.root.get_screen('cronometro').ids.cronometro_tempo)

    def pausar_cronometro(self):
        self.cronometro.pausar()

    def resetar_cronometro(self):
        self.cronometro.resetar(self.root.get_screen('cronometro').ids.cronometro_tempo)

    def iniciar_temporizador(self):
        temporizador_screen = self.root.get_screen('temporizador')
        horas_display = temporizador_screen.ids.horas
        minutos_display = temporizador_screen.ids.minutos
        segundos_display = temporizador_screen.ids.segundos
        self.temporizador.iniciar(horas_display, minutos_display, segundos_display)
    
    def pausar_temporizador(self):
        self.temporizador.pausar()

    def resetar_temporizador(self):
        temporizador_screen = self.root.get_screen('temporizador')
        horas_display = temporizador_screen.ids.horas
        minutos_display = temporizador_screen.ids.minutos
        segundos_display = temporizador_screen.ids.segundos
        self.temporizador.resetar(horas_display, minutos_display, segundos_display)

    def incrementar_horas(self):
        self.temporizador.incrementar_horas(self.root.get_screen('temporizador').ids.temporizador_tempo)

    def decrementar_horas(self):
        self.temporizador.decrementar_horas(self.root.get_screen('temporizador').ids.temporizador_tempo)

    def incrementar_minutos(self):
        self.temporizador.incrementar_minutos(self.root.get_screen('temporizador').ids.temporizador_tempo)

    def decrementar_minutos(self):
        self.temporizador.decrementar_minutos(self.root.get_screen('temporizador').ids.temporizador_tempo)

    def incrementar_segundos(self):
        self.temporizador.incrementar_segundos(self.root.get_screen('temporizador').ids.temporizador_tempo)

    def decrementar_segundos(self):
        self.temporizador.decrementar_segundos(self.root.get_screen('temporizador').ids.temporizador_tempo)

    def adicionar_alarme(self):
        self.alarme.adicionar_alarme()

if __name__ == '__main__':
    CronosApp().run()
