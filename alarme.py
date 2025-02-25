from kivy.clock import Clock
from kivymd.uix.pickers import MDTimePicker, MDDatePicker
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivymd.app import MDApp
from kivymd.uix.list import OneLineAvatarIconListItem, IconLeftWidget, IconRightWidget 
import datetime
from datetime import datetime, timedelta

class Alarme:
    def __init__(self, alarmes_lista):
        self.alarmesativos = []
        self.evento = None
        self.alarmes_lista = alarmes_lista
        self.data_selecionada = None
        self.hora_selecionada = None

        Clock.schedule_interval(self.verificar_alarmes, 1)

    def __str__(self):
        return f"{self.data_selecionada.strftime('%d/%m/%Y')} - {self.hora_selecionada.strftime('%H:%M')}" if self.data_selecionada and self.hora_selecionada else ""

    def adicionar_alarme(self):
        self.adicionar_data()
        
    def adicionar_data(self):
        date_dialog = MDDatePicker(min_date=datetime.now().date())
        date_dialog.bind(on_save=self.salvar_data, on_cancel=self.cancelar_data)
        date_dialog.open()
        Window.size = (450, 751)
        Window.size = (450, 750)         

    def salvar_data(self, instance, value, date_range):
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
        self.adicionar_hora()

    def adicionar_hora(self):
        time_dialog = MDTimePicker()
        horaatual = (datetime.now() + timedelta(minutes=1)).time()
        time_dialog.set_time(horaatual)
        time_dialog.bind(on_save=self.salvar_hora, on_cancel=self.cancelar_hora)
        time_dialog.open()
        Window.size = (450, 751)
        Window.size = (450, 750)

    def salvar_hora(self, instance, value):
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

    def cancelar_data(self, instance, value):
        print("Seleção data cancelada!")

    def cancelar_hora(self, instance, value):
        print("Seleção hora cancelada!")

    def criar_alarme(self):
        if self.data_selecionada and self.hora_selecionada:
            # Cria um novo objeto Alarme
            novo_alarme = Alarme(self.alarmes_lista)
            novo_alarme.data_selecionada = self.data_selecionada
            novo_alarme.hora_selecionada = self.hora_selecionada
            self.alarmesativos.append(novo_alarme)
            self.atualizar_lista_alarmes()

    def atualizar_lista_alarmes(self):
        self.alarmes_lista.clear_widgets()
        for alarme in self.alarmesativos:
            # Cria o item do alarme
            alarme_item = OneLineAvatarIconListItem(
                IconLeftWidget(icon="pencil", on_release=self.criar_editar_alarme_callback(alarme)),
                IconRightWidget(
                    icon="trash-can",
                    on_release=self.criar_remover_alarme_callback(alarme)
                ),
                text=str(alarme)
            )
            # Adiciona o item à lista de alarmes
            self.alarmes_lista.add_widget(alarme_item)

    def criar_editar_alarme_callback(self, alarme):
        def editar_alarme_callback(instance):
            self.editar_alarme(alarme)
        return editar_alarme_callback

    def criar_remover_alarme_callback(self, alarme):
        def remover_alarme_callback(instance):
            self.remover_alarme(alarme)
        return remover_alarme_callback

    def editar_alarme(self, alarme):
        # Abre o diálogo de edição para o alarme selecionado
        self.data_selecionada = alarme.data_selecionada
        self.hora_selecionada = alarme.hora_selecionada

        date_dialog = MDDatePicker(min_date=datetime.now().date())
        date_dialog.bind(on_save=lambda instance, value, date_range: self.salvar_data_edicao(instance, value, date_range, alarme), on_cancel=self.cancelar_data)
        date_dialog.open()
        Window.size = (450, 751)
        Window.size = (450, 750)

    def salvar_data_edicao(self, instance, value, date_range, alarme):
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
        self.adicionarhora_edicao(alarme)

    def adicionarhora_edicao(self, alarme):
        time_dialog = MDTimePicker()
        horaatual = (datetime.now() + timedelta(minutes=1)).time()
        time_dialog.set_time(horaatual)
        time_dialog.bind(on_save=lambda instance, value: self.salvar_hora_edicao(instance, value, alarme), on_cancel=self.cancelar_hora)
        time_dialog.open()
        Window.size = (450, 751)
        Window.size = (450, 750)

    def salvar_hora_edicao(self, instance, value, alarme):
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
        self.atualizar_alarme(alarme)

    def atualizar_alarme(self, alarme):
        alarme.data_selecionada = self.data_selecionada
        alarme.hora_selecionada = self.hora_selecionada
        self.atualizar_lista_alarmes()

    def verificar_alarmes(self, dt):
        now = datetime.now()
        alarmesexpirados = []
        
        for alarme in self.alarmesativos:
            alarm_time = datetime.combine(alarme.data_selecionada, alarme.hora_selecionada)
            if now >= alarm_time:
                self.alarmar()
                alarmesexpirados.append(alarme)
    
        self.alarmesativos = [alarm for alarm in self.alarmesativos if alarm not in alarmesexpirados]
        
        
    def remover_alarme(self, alarme):
        # Remove o alarme da lista de alarmes ativos
        self.alarmesativos.remove(alarme)
        # Atualiza a lista de widgets
        self.atualizar_lista_alarmes()

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
                on_release=lambda x: (alarm_dialog.dismiss(), self.atualizar_lista_alarmes())
            )
            ],
        )
        alarm_dialog.bind(on_dismiss=lambda x: self.atualizar_lista_alarmes())
        alarm_dialog.open()