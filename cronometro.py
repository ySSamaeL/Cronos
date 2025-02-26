from kivy.clock import Clock

class Cronometro:
    def __init__(self):
        self.tempo_total = 0
        self.evento = None
        self.display_widget = None

    # Inicia o cronômetro e atualiza o display_widget a cada milissegundo
    def iniciar(self, display_widget):
        if not self.evento:
            self.display_widget = display_widget
            self.evento = Clock.schedule_interval(self.atualizar, 0.001)

    # Pausa o cronômetro, cancelando o evento de atualização
    def pausar(self):
        if self.evento:
            self.evento.cancel()
            self.evento = None

    # Reseta o cronômetro, pausando-o e zerando o tempo total
    def resetar(self, display_widget):
        self.pausar()
        self.tempo_total = 0
        display_widget.text = '00:00:00:000'

    # Atualiza o tempo total e o display_widget com o tempo formatado
    def atualizar(self, dt):
        self.tempo_total += dt
        segundos_totais = int(self.tempo_total)
        horas, resto = divmod(segundos_totais, 3600)
        minutos, segundos = divmod(resto, 60)
        milissegundos = int((self.tempo_total - segundos_totais) * 1000)
        self.display_widget.text = f"{horas:02}:{minutos:02}:{segundos:02}:{milissegundos:03}"
