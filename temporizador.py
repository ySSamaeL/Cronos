from kivy.clock import Clock

class Temporizador:
    def __init__(self):
        self.horas = 0
        self.minutos = 0
        self.segundos = 0
        self.evento = None
        self.horas_display = None
        self.minutos_display = None
        self.segundos_display = None

    def iniciar(self, horas_display, minutos_display, segundos_display):
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
