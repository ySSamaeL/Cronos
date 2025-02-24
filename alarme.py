from kivy.clock import Clock
from kivymd.uix.pickers import MDTimePicker
from kivymd.uix.pickers import MDDatePicker
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivymd.app import MDApp

import datetime
from datetime import datetime, timedelta

class Alarme:
    def __init__(self, display_widget):

        self.alarmesativos = []

        self.evento = None
        self.display_widget = display_widget
        self.data_selecionada = None
        self.hora_selecionada = None

        Clock.schedule_interval(self.verificar_alarmes, 1)

    def adicionar_alarme(self):
        self.adicionardata()
        
    def adicionardata(self):

        date_dialog = MDDatePicker(min_date=datetime.now().date())
        date_dialog.bind(on_save=self.salvardata, on_cancel=self.cancelardata)
        date_dialog.open()
        Window.size = (450, 751)
        Window.size = (450, 750)         

    def salvardata(self, instance, value, date_range):

        self.data_selecionada = value
        if self.data_selecionada < datetime.now().date():
            error_dialog = MDDialog(
                title="Data Inválida",
                text="Não é permitido selecionar uma data anterior à data atual.",
                buttons=[
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=MDApp.get_running_app().theme_cls.primary_color,
                        on_release=lambda x: error_dialog.dismiss()
                    )
                ],
            )
            error_dialog.open()
            return
        print(f"Data selecionada: {self.data_selecionada}")
        
        self.adicionarhora()

    def adicionarhora(self):
        time_dialog = MDTimePicker()
        hora_atual = datetime.now()
        time_dialog.set_time(hora_atual)
        time_dialog.bind(on_save=self.salvarhora, on_cancel=self.cancelarhora)
        time_dialog.open()
        Window.size = (450, 751)
        Window.size = (450, 750)

    def salvarhora(self, instance, value):
        self.hora_selecionada = value

        horaminima = (datetime.now() + timedelta(minutes=1)).time()
        print(self.hora_selecionada)
        print(horaminima)
        if self.data_selecionada == datetime.now().date() and self.hora_selecionada < datetime.now().time():
            error_dialog = MDDialog(
                title="Hora Inválida",
                text="Não é permitido selecionar um horário anterior ao horário atual.",
                buttons=[
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=MDApp.get_running_app().theme_cls.primary_color,
                        on_release=lambda x: error_dialog.dismiss()
                    )
                ],
            )
            error_dialog.open()
            return
        
        print(f"Hora selecionada: {self.hora_selecionada}")

        self.criar_alarme()

    def cancelardata(self, instance, value):
        print("Seleção data cancelada!")

    def cancelarhora(self, instance, value):
        print("Seleção hora cancelada!")

    def criar_alarme(self):
        if self.data_selecionada and self.hora_selecionada:
            alarme_layout = BoxLayout(orientation='horizontal')
            data_label = Label(text=str(self.data_selecionada))
            hora_label = Label(text=str(self.hora_selecionada))
            alarme_layout.add_widget(data_label)
            alarme_layout.add_widget(hora_label)
            self.display_widget.add_widget(alarme_layout)
            self.alarmesativos.append((self.data_selecionada, self.hora_selecionada))

    def verificar_alarmes(self, dt):
        now = datetime.now()
        print(self.alarmesativos)

        alarmesexpirados = []
        
        for data, hora in self.alarmesativos:
            alarm_time = datetime.combine(data, hora)
            if now >= alarm_time:
                self.alarmar()
                alarmesexpirados.append((data, hora))
        
        self.alarmesativos = [alarm for alarm in self.alarmesativos if alarm not in alarmesexpirados]

    def alarmar(self):
        print("ALARME CARAIOOO")
        alarm_dialog = MDDialog(
            title="Alarme",
            text="O alarme foi disparado!",
            buttons=[
                MDFlatButton(
                    text="OK",
                    theme_text_color="Custom",
                    text_color=MDApp.get_running_app().theme_cls.primary_color,
                    on_release=lambda x: alarm_dialog.dismiss()
                )
            ],
        )
        alarm_dialog.open()