import flet as ft
from telas.tela_base import TelaBase

class CadastroProduto(TelaBase):
    def __init__(self, page):
        self.nome_produto = ft.TextField(label = 'Nome', col = 6)
        self.preco_custo_produto = ft.TextField(label = 'Preço Custo', col = 3)
        self.quantidade_produto = ft.TextField(label = 'Quantidade', col = 3)
        self.marca_produto = ft.TextField(label = 'Marca', col = 3)
        self.cod_produto = ft.TextField(label = 'Codigo Barras', col = 6)
        self.area_formulario = ft.ResponsiveRow(controls = [
            self.nome_produto, self.preco_custo_produto, self.quantidade_produto, self.marca_produto, self.cod_produto
        ])
        self.btn_salvar = ft.ElevatedButton(text = 'Salvar', col = 4.5)
        self.btn_cancelar_produto = ft.ElevatedButton(text = 'Cancelar', col = 4.5)
        self.area_botoes = ft.ResponsiveRow(controls = [
            self.btn_salvar, self.btn_cancelar_produto
        ])
        super().__init__(page)
        self.page = page
        self.controls = self.criar_conteudo()
        self.page.update()


    def criar_conteudo(self):
        return [
            self.area_formulario, self.area_botoes
        ]


    def get_view(self, route):
        app_bar = ft.Row(controls = [
            ft.IconButton(
                icon = ft.Icons.ARROW_BACK, icon_color = ft.Colors.CYAN_ACCENT,
                on_click = lambda _: self.page.go('/principal'),
                padding = 0
            )
        ], spacing = 0)
        coluna_principal = ft.Container(
            content = ft.Column(
                    controls = [app_bar,
                                ft.Divider(height=5, color = ft.Colors.TRANSPARENT),
                                *self.criar_conteudo()], alignment = ft.MainAxisAlignment.START, spacing = 0
            ), image = ft.DecorationImage(src = 'background_tela1.jpg', fit = ft.ImageFit.COVER),
            bgcolor = ft.Colors.BLACK,
            expand = True,
            padding = 10
        )

        return ft.View(route,[coluna_principal], padding = 0)