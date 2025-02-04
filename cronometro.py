from kivy.clock import Clock

class Cronometro:
    def __init__(self):
        self.tempo_total = 0
        self.segundos = 0
        self.evento = None

    def iniciar(self, display_widget):
        if not self.evento:
            self.display_widget = display_widget
            self.evento = Clock.schedule_interval(self.atualizar, 0.001)

    def pausar(self):
        if self.evento:
            self.evento.cancel()
            self.evento = None

    def resetar(self, display_widget):
        self.pausar()
        self.tempo_total = 0
        display_widget.text = '00:00:00:000'

    def atualizar(self, dt):
        self.tempo_total += dt
        self.segundos = int(self.tempo_total)

        horas, resto = divmod(self.segundos, 3600)
        minutos, segundos = divmod(resto, 60)
        milissegundos = int((self.tempo_total - self.segundos) * 1000)

        self.display_widget.text = f"{horas:02}:{minutos:02}:{segundos:02}:{milissegundos:03}"
