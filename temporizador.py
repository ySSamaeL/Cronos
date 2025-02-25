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

    def iniciar(self, horas_display, minutos_display, segundos_display):
        if self.horas == 0 and self.minutos == 0 and self.segundos == 0:
            return
        if not self.evento:
            self.horas_display = horas_display
            self.minutos_display = minutos_display
            self.segundos_display = segundos_display
            self.evento = Clock.schedule_interval(self.atualizar, 1)
            

    def pausar(self):
        if self.evento:
            self.evento.cancel()
            self.evento = None

    def resetar(self, horas_display, minutos_display, segundos_display):
        self.pausar()
        self.horas = 0
        self.minutos = 0
        self.segundos = 0
        self.horas_display = horas_display
        self.minutos_display = minutos_display
        self.segundos_display = segundos_display
        self.atualizar_display()

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

    def atualizar_display(self):
        if self.horas_display and self.minutos_display and self.segundos_display:
            self.horas_display.text = f"{self.horas:02}"
            self.minutos_display.text = f"{self.minutos:02}"
            self.segundos_display.text = f"{self.segundos:02}"

    def definir_tempo(self, horas, minutos, segundos, horas_display, minutos_display, segundos_display):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos
        self.horas_display = horas_display
        self.minutos_display = minutos_display
        self.segundos_display = segundos_display
        self.atualizar_display()

    def incrementar_horas(self):
        if not self.evento:
            self.horas = (self.horas + 1) % 24
            self.atualizar_display()

    def decrementar_horas(self):
        if not self.evento:
            self.horas = (self.horas - 1) % 24
            self.atualizar_display()

    def incrementar_minutos(self):
        if not self.evento:
            self.minutos = (self.minutos + 1) % 60
            self.atualizar_display()

    def decrementar_minutos(self):
        if not self.evento:
            self.minutos = (self.minutos - 1) % 60
            self.atualizar_display()

    def incrementar_segundos(self):
        if not self.evento:
            self.segundos = (self.segundos + 1) % 60
            self.atualizar_display()

    def decrementar_segundos(self):
        if not self.evento:
            self.segundos = (self.segundos - 1) % 60
            self.atualizar_display()

    def alarmar(self):

        icon_path = os.path.join(os.path.dirname(__file__), 'assets/timersandcomplete.ico')
        sound_path = os.path.join(os.path.dirname(__file__), 'assets/somalarme.mp3')

        notification.notify(
            title="Cronos - Temporizador",
            message="O temporizador foi disparado!",
            app_name="Cronos",
            app_icon=icon_path,
            timeout=10  # Tempo em segundos que a notificação será exibida
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
                theme_text_color= 'Primary',
                text_color=MDApp.get_running_app().theme_cls.primary_color,
                on_release=lambda x: (alarm_dialog.dismiss())
            )
            ],
        )
        alarm_dialog.open()
