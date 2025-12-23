import flet as ft
from telas.tela_base import TelaBase
class CadastroCliente(TelaBase):
    def __init__(self, page):
        self.nome_cliente = ft.TextField(label = 'Nome', col = 6)
        self._cpf_cliente = ft.TextField(label = 'CPF', col = 4)
        self.data_nascimento = ft.TextField(label = 'Ano Nascimento', col = 2)
        self.endereco = ft.TextField(label = 'Endereço', col = 8)
        self.email = ft.TextField(label = 'E-mail', col = 4)
        self.telefone = ft.TextField(label = 'Telefone', col = 2)
        self.busca_cliente = ft.TextField(label = 'Buscar Cliente', col = 4, height = 32, border_radius = 16, icon = ft.Icons.SEARCH)
        self.btn_salvar_cliente = ft.ElevatedButton(text = 'Salvar', col = 3)
        self.btn_excluir_cliente = ft.ElevatedButton(text = 'Excluir', col = 3)
        self.btn_pesquisar_cliente = ft.ElevatedButton(text = 'Buscar', col = 2)
        self.area_formulario = ft.ResponsiveRow(controls = [self.nome_cliente, self._cpf_cliente, self.data_nascimento,
                                                            self.endereco, self.email, self.telefone,
        ])
        self.area_botoes = ft.ResponsiveRow(controls = [
            self.btn_salvar_cliente, self.btn_excluir_cliente, self.busca_cliente, self.btn_pesquisar_cliente
        ])
        super().__init__(page)
        self.page = page
        self.titulo = page.title = 'Cadastro Clientes'
        self.controls = self.criar_conteudo()


    def executar_minimizar(self,_e):
        self.page.window.minimized = True
        self.page.update()


    def executar_maximizar(self, _e):
        self.page.window.maximized = not self.page.window.maximized
        self.page.update()


    def executar_fechar_tela(self, _e):
        self.page.window.destroy()
        self.page.update()


    def criar_conteudo(self):
        formularios_cadastro_clientes = ft.Container(
            content = ft.Column(controls = [
                self.area_formulario
            ])
        )
        area_botoes_cadastro_cliente = ft.Container(
            content = ft.Column(controls = [
                self.area_botoes
            ])
        )
        return [
            formularios_cadastro_clientes, area_botoes_cadastro_cliente
        ]


    def get_view(self, router):
        app_bar = ft.Row(controls = [
            ft.IconButton(
                icon = ft.Icons.ARROW_BACK, icon_color = ft.Colors.CYAN_ACCENT,
                on_click = lambda _:self.page.go('/principal'),
                padding = 10
            ),
            ft.Container(content = ft.Row(
                            controls = [
                              ft.Text("Cadastro de Clientes")
                            ]
            ),expand = True),
            ft.IconButton(
                icon = ft.Icons.MINIMIZE,
                icon_color = ft.Colors.WHITE70,
                on_click = lambda _: self.executar_minimizar(_)
            ),
            ft.IconButton(
                icon = ft.Icons.DESKTOP_WINDOWS_SHARP,
                icon_color = ft.Colors.WHITE70,
                on_click = lambda _: self.executar_maximizar(_)
            ),
            ft.IconButton(
                icon = ft.Icons.CLOSE,
                icon_color = ft.Colors.WHITE70,
                on_click = lambda _: self.executar_fechar_tela(_)
            )
        ], spacing = 0
        )
        app_bar_responsivo = ft.WindowDragArea(
            content = app_bar,
            maximizable = True
        )
        coluna_principal = ft.Container(
            content = ft.Column(controls = [
                                app_bar_responsivo,
                ft.Divider(height = 5, color = ft.Colors.TRANSPARENT),
                *self.criar_conteudo()
        ], alignment = ft.MainAxisAlignment.START, spacing = 0
            ),image = ft.DecorationImage(src = 'background_tela1.jpg', fit = ft.ImageFit.COVER),
            bgcolor = ft.Colors.BLACK, expand = True,
            padding = 10
        )

        return ft.View(router,controls = [coluna_principal], padding = 0, spacing = 0)