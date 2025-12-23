import flet as ft
from telas.tela_base import TelaBase


class CadastroDespesas(TelaBase):
    def __init__(self, page):
        self.nome_despesa = ft.TextField(label = 'Despesa', col = 9)
        self.valor_despesa = ft.TextField(label = 'Valor', col = 3)
        self.descricao_despesa = ft.TextField(label = 'Descrição', col = 12)
        self.obs_despesa = ft.TextField(label = 'OBS', col = 6)
        self.area_formulario = ft.ResponsiveRow(controls = [
            self.nome_despesa, self.valor_despesa, self.descricao_despesa, self.obs_despesa
        ])
        self.btn_salvar_despesa = ft.ElevatedButton(text = 'Salvar', col = 3)
        self.btn_excluir_despesa = ft.ElevatedButton(text = 'Excluir', col = 3)
        self.btn_buscar_despesa = ft.ElevatedButton(text = 'Buscar', col = 2)
        self.pesquisa_despesa = ft.TextField(label = 'Buscar Despesa', icon = ft.Icons.SEARCH, col = 4, height = 32, border_radius = 16)
        self.area_botoes = ft.ResponsiveRow(controls = [
            self.btn_salvar_despesa, self.btn_excluir_despesa, self.pesquisa_despesa, self.btn_buscar_despesa
        ])
        super().__init__(page)
        self.page = page
        self.titulo = page.title = 'Despesas'
        self.controls = self.criar_conteudo()


    def criar_conteudo(self):
        return [
           self.area_formulario, self.area_botoes
        ]


    def get_view(self, route):
        coluna_principal = ft.Container(content = ft.Column(
            controls = self.criar_conteudo(),alignment = ft.MainAxisAlignment.START, spacing = 10
        ), image = ft.DecorationImage(src = 'background_tela1.jpg', fit = ft.ImageFit.COVER),
            bgcolor = ft.Colors.BLACK, expand = True
        )
        app_bar = ft.AppBar(leading = ft.IconButton(icon = ft.Icons.ARROW_BACK, on_click = lambda _: self.page.go('/principal')))
        return ft.View(route,[coluna_principal], app_bar)