import flet as ft
from abc import ABC, abstractmethod


class TelaBase(ABC, ft.ResponsiveRow):
    def __init__(self, page:ft.Page):
        self.logo = page.window.icon = "logosp.ico"
        super().__init__()


    @abstractmethod
    def criar_conteudo(self):
        pass


    @abstractmethod
    def get_view(self,router):
        pass