from kivy.clock import Clock
import datetime 
from kivymd.uix.pickers import MDTimePicker
from kivymd.uix.pickers import MDDatePicker
from kivy.core.window import Window

class Alarme:
    def __init__(self):
        self.alarmesativos = []
        self.evento = None
        self.display_widget = None

    def adicionar_alarme(self):
        
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_savedata, on_cancel=self.on_canceldata)
        date_dialog.open()
        Window.size = (450, 751)
        Window.size = (450, 750)
        
        time_dialog = MDTimePicker()
        time_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        time_dialog.open()
        Window.size = (450, 751)
        Window.size = (450, 750)

    def on_savedata(self, instance, value, date_range):

        '''
        Events called when the "OK" dialog box button is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;
        :param value: selected date;
        :type value: <class 'datetime.date'>;
        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        '''

        print(instance, value, date_range)

    def on_canceldata(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''
    def on_save(self, instance, value):
        print(instance, value)
    def on_cancel(self, instance, value):
        pass
