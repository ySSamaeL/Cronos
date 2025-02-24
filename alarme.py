from kivy.clock import Clock
import datetime 
from kivymd.uix.pickers import MDTimePicker
from kivymd.uix.pickers import MDDatePicker
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Alarme:
    def __init__(self):
        self.alarmesativos = []
        self.evento = None
        self.display_widget = None
        self.data_selecionada = None
        self.hora_selecionada = None

    def adicionar_alarme(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.salvardata, on_cancel=self.cancelardata)
        date_dialog.open()
        Window.size = (450, 751)
        Window.size = (450, 750)
        
        time_dialog = MDTimePicker()
        time_dialog.bind(on_save=self.salvarhora, on_cancel=self.cancelarhora)
        time_dialog.open()
        Window.size = (450, 751)
        Window.size = (450, 750)

    def salvardata(self, instance, value, date_range):
        self.data_selecionada = value
        print(f"Data selecionada: {self.data_selecionada}")
        
    def salvarhora(self, instance, value):
        self.hora_selecionada = value
        print(f"Hora selecionada: {self.hora_selecionada}")
        self.criar_alarme_visual()

    def cancelardata(self, instance, value):
        pass

    def cancelarhora(self, instance, value):
        pass

    def criar_alarme_visual(self):
        if self.data_selecionada and self.hora_selecionada:
            alarme_layout = BoxLayout(orientation='horizontal')
            data_label = Label(text=str(self.data_selecionada))
            hora_label = Label(text=str(self.hora_selecionada))
            alarme_layout.add_widget(data_label)
            alarme_layout.add_widget(hora_label)
            self.display_widget.add_widget(alarme_layout)
            self.alarmesativos.append((self.data_selecionada, self.hora_selecionada))