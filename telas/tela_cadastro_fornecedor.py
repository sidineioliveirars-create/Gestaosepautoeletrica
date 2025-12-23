import flet as ft
from telas.tela_base import TelaBase


class CadastroFornecedor(TelaBase):
    def __init__(self, page):
        self.nome_fornecedor = ft.TextField(label = 'Fornecedor', col = 6)
        self.cpf_cnpj_fornecedor = ft.TextField(label = 'Cpf/Cnpj', input_filter = ft.InputFilter(allow = True, regex_string = r"[0-9]", replacement_string = ""), keyboard_type = ft.KeyboardType.NUMBER, max_length = 14, col = 3)
        self.telefone_fornecedor = ft.TextField(label = 'Telefone', col = 3)
        self.email_fornecedor = ft.TextField(label = 'E-mail', col = 6)
        self.endereco_fornecedor = ft.TextField(label = 'Endereço', col = 6)
        self.area_formulario = ft.ResponsiveRow(controls = [
            self.nome_fornecedor, self.cpf_cnpj_fornecedor, self.telefone_fornecedor, self.email_fornecedor, self.endereco_fornecedor
        ])
        self.btn_salvar_fornecedor = ft.ElevatedButton(text = 'Salvar', col = 2)
        self.btn_excluir_fornecedor = ft.ElevatedButton(text = 'Excluir', col = 2)
        self.buscar_fornecedor = ft.TextField(label = 'Buscar', icon = ft.Icons.SEARCH, height = 32, border_radius = 16, col = 6)
        self.btn_buscar_fornecedor = ft.ElevatedButton(text = 'Buscar', col = 2)
        self.area_botoes = ft.ResponsiveRow(controls = [
            self.btn_salvar_fornecedor, self.btn_excluir_fornecedor, self.buscar_fornecedor, self.btn_buscar_fornecedor
        ])
        super().__init__(page)
        self.page = page
        self.titulo = ft.title = 'Fornecedor'
        self.controls = self.criar_conteudo()


    def executar_minimizar_tela_fornecedor(self, _e):
        self.page.window.minimized = True
        self.page.update()


    def executar_maximizar_tela_fornecedor(self, _e):
        self.page.window.maximized = not self.page.window.maximized
        self.page.update()

    def nexecutar_fechar_sistema(self, _e):
        self.page.window.destroy()
        self.page.update()
    def criar_conteudo(self):
        return [
            self.area_formulario, self.area_botoes
        ]


    def get_view(self, route):
        app_bar = ft.WindowDragArea(
            content = ft.Container(
                padding = ft.padding.only(right = 5, top = 0),
                content = ft.Row(
                    alignment = ft.MainAxisAlignment.END,
                    controls = [
                        ft.IconButton(
                            icon = ft.Icons.ARROW_BACK,
                            icon_color = ft.Colors.with_opacity(0.5, "#011526"),
                            on_click = lambda _: self.page.go("/principal")
                        ),
                        ft.Container(content = ft.Row(
                            controls = [
                                ft.Text("Cadastro de Fornecedor")
                            ]
                        ),expand = True)
                    ]
                )
            )
        )
        coluna_principal = ft.Container(
            content = ft.Column(
                controls = [
                    app_bar, *self.criar_conteudo()
                ]
            ),image = ft.DecorationImage(
                src = "background_tela1.jpg",
                fit = ft.ImageFit.COVER,
            ),bgcolor = ft.Colors.BLACK,
            expand = True,
            padding = 10
        )

        return ft.View(route, [coluna_principal])