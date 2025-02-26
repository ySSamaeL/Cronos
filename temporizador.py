from kivy.clock import Clock
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.app import MDApp

from plyer import notification
import os
import pygame

class Temporizador:
    def __init__(self):
        self.horas = 0
        self.minutos = 0
        self.segundos = 0
        self.evento = None
        self.horas_display = None
        self.minutos_display = None
        self.segundos_display = None

        pygame.mixer.init()

    # Inicia o temporizador e atualiza o display a cada segundo
    def iniciar(self, horas_display, minutos_display, segundos_display):
        if self.horas == 0 and self.minutos == 0 and self.segundos == 0:
            return
        if not self.evento:
            self.horas_display = horas_display
            self.minutos_display = minutos_display
            self.segundos_display = segundos_display
            self.evento = Clock.schedule_interval(self.atualizar, 1)

    # Pausa o temporizador, cancelando o evento de atualização
    def pausar(self):
        if self.evento:
            self.evento.cancel()
            self.evento = None

    # Reseta o temporizador, pausando-o e zerando o tempo
    def resetar(self, horas_display, minutos_display, segundos_display):
        self.pausar()
        self.horas = 0
        self.minutos = 0
        self.segundos = 0
        self.horas_display = horas_display
        self.minutos_display = minutos_display
        self.segundos_display = segundos_display
        self.atualizar_display()

    # Atualiza o tempo restante e o display com o tempo formatado
    def atualizar(self, dt):
        if self.horas == 0 and self.minutos == 0 and self.segundos == 0:
            self.pausar()
            self.alarmar()
            return
        if self.segundos > 0:
            self.segundos -= 1
        elif self.minutos > 0:
            self.minutos -= 1
            self.segundos = 59
        elif self.horas > 0:
            self.horas -= 1
            self.minutos = 59
            self.segundos = 59
        self.atualizar_display()

    # Atualiza o display com o tempo atual
    def atualizar_display(self):
        if self.horas_display and self.minutos_display and self.segundos_display:
            self.horas_display.text = f"{self.horas:02}"
            self.minutos_display.text = f"{self.minutos:02}"
            self.segundos_display.text = f"{self.segundos:02}"

    # Define o tempo do temporizador e atualiza o display
    def definir_tempo(self, horas, minutos, segundos, horas_display, minutos_display, segundos_display):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos
        self.horas_display = horas_display
        self.minutos_display = minutos_display
        self.segundos_display = segundos_display
        self.atualizar_display()

    # Incrementa as horas do temporizador
    def incrementar_horas(self):
        if not self.evento:
            self.horas = (self.horas + 1) % 24
            self.atualizar_display()

    # Decrementa as horas do temporizador
    def decrementar_horas(self):
        if not self.evento:
            self.horas = (self.horas - 1) % 24
            self.atualizar_display()

    # Incrementa os minutos do temporizador
    def incrementar_minutos(self):
        if not self.evento:
            self.minutos = (self.minutos + 1) % 60
            self.atualizar_display()

    # Decrementa os minutos do temporizador
    def decrementar_minutos(self):
        if not self.evento:
            self.minutos = (self.minutos - 1) % 60
            self.atualizar_display()

    # Incrementa os segundos do temporizador
    def incrementar_segundos(self):
        if not self.evento:
            self.segundos = (self.segundos + 1) % 60
            self.atualizar_display()

    # Decrementa os segundos do temporizador
    def decrementar_segundos(self):
        if not self.evento:
            self.segundos = (self.segundos - 1) % 60
            self.atualizar_display()

    # Dispara o alarme quando o tempo do temporizador acaba
    def alarmar(self):
        icon_path = os.path.join(os.path.dirname(__file__), 'assets/timersandcomplete.ico')
        sound_path = os.path.join(os.path.dirname(__file__), 'assets/somalarme.mp3')

        notification.notify(
            title="Cronos - Temporizador",
            message="O temporizador foi disparado!",
            app_name="Cronos",
            app_icon=icon_path,
            timeout=10 
        )

        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.set_volume(0.01)
        pygame.mixer.music.play()

        alarm_dialog = MDDialog(
            title="Temporizador",
            text="O temporizador foi disparado!",
            buttons=[
                MDFlatButton(
                    font_style='H6',
                    text="OK",
                    theme_text_color='Primary',
                    text_color=MDApp.get_running_app().theme_cls.primary_color,
                    on_release=lambda x: (alarm_dialog.dismiss())
                )
            ],
        )
        alarm_dialog.open()