from kivy.clock import Clock

class Temporizador:
    def __init__(self):
        self.horas = 0
        self.minutos = 0
        self.segundos = 0
        self.evento = None
        self.display_widget = None

    def iniciar(self, display_widget):
        if not self.evento:
            self.display_widget = display_widget
            self.evento = Clock.schedule_interval(self.atualizar, 1)

    def pausar(self):
        if self.evento:
            self.evento.cancel()
            self.evento = None

    def resetar(self, display_widget):
        self.pausar()
        self.horas = 0
        self.minutos = 0
        self.segundos = 0
        display_widget.text = '00:00:00'

    def atualizar(self, dt):
        if self.horas == 0 and self.minutos == 0 and self.segundos == 0:
            self.pausar()
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
        if self.display_widget:
            self.display_widget.text = f"{self.horas:02}:{self.minutos:02}:{self.segundos:02}"

    def incrementar_horas(self):
        self.horas = (self.horas + 1) % 100
        self.atualizar_display()

    def decrementar_horas(self):
        self.horas = (self.horas - 1) % 100
        self.atualizar_display()

    def incrementar_minutos(self):
        self.minutos = (self.minutos + 1) % 60
        self.atualizar_display()

    def decrementar_minutos(self):
        self.minutos = (self.minutos - 1) % 60
        self.atualizar_display()

    def incrementar_segundos(self):
        self.segundos = (self.segundos + 1) % 60
        self.atualizar_display()

    def decrementar_segundos(self):
        self.segundos = (self.segundos - 1) % 60
        self.atualizar_display()
