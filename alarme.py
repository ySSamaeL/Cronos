from kivy.clock import Clock
import datetime 
from kivymd.uix.pickers import MDTimePicker
from kivymd.uix.pickers import MDDatePicker

class Alarme:
    def __init__(self):
        self.alarmescriados = []
        self.evento = None
        self.display_widget = None

    def adicionar_alarme():
        
        dataescolhida = MDDatePicker()
        dataescolhida.open()

        horaescolhida = MDTimePicker() 
        horaescolhida.open()

        pass
    
    pass
