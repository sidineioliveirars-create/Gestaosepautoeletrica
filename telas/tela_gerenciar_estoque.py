import flet as ft
from telas.tela_base import TelaBase


class GestaoEstoque(TelaBase):
    def __init__(self, page):
        self.label = ft.Text('Estoque')
        super().__init__(page)
        self.page = page
        self.titulo = page.title = 'Estoque'
        self.controls = self.criar_conteudo()


    def criar_conteudo(self):
        return [
            self.label
        ]


    def get_view(self, route):
        coluna_principal = ft.Column(controls = self.controls)
        app_bar = ft.AppBar(leading = ft.IconButton(icon = ft.Icons.ARROW_BACK, on_click = lambda _: self.page.go('/principal')))
        return ft.View(route, [coluna_principal], app_bar)
