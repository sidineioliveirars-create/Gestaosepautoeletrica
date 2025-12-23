import flet as ft
from telas.tela_base import TelaBase


class CadastroOs(TelaBase):
    def __init__(self, page):
        self.nome_cliente_os = ft.TextField(label = 'Cliente', col = 3)
        self.contato_cliente = ft.TextField(label = 'Telefone', col = 2)
        self.email_cliente = ft.TextField(label = 'E-mail', col = 4)
        self.modelo_carro_os = ft.TextField(label = 'Marca/Veículo', col = 1.5)
        self.placa_veiculo_os = ft.TextField(label = 'Placa', col = 1.5)
        self.km_atual_veiculo_os = ft.TextField(label = 'Hodômetro Atual', col = 1.5)
        self.km_anterior_veiculo_os = ft.TextField(label = 'Hodômetro Anterior', col = 1.5)
        self.informacoes_cliente_os = ft.TextField(label = 'Informações', multiline = True, col = 4.5)
        self.diagnostico_os = ft.TextField(label = 'Diágnostico', multiline = True, col = 4.5)
        self.area_formularios = ft.ResponsiveRow(controls = [
            self.nome_cliente_os, self.contato_cliente, self.email_cliente, self.modelo_carro_os, self.placa_veiculo_os, self.km_atual_veiculo_os, self.km_anterior_veiculo_os, self.informacoes_cliente_os, self.diagnostico_os,

        ])

        self.area_selecoes_dialogos = ft.ResponsiveRow(controls = [

        ])
        self.area_botoes = ft.ResponsiveRow(controls = [

        ])

        super().__init__(page)
        self.page = page
        self.controls = self.criar_conteudo()
        self.titulo = page.title = 'OS'


    def executar_minimizar_tela_os(self, _e):
        self.page.window.minimized = True
        self.page.update()


    def executar_maximizar_tela_os(self, _e):
        self.page.window.maximized = not self.page.window.maximized
        self.page.update()


    def executar_fechar_sistema(self, _e):
        self.page.window.destroy()
        self.page.update()

    def criar_conteudo(self):
        return [ ft.Column (
            controls = [
            self.area_formularios,
            ft.Divider(height = 20, color = ft.Colors.TRANSPARENT),
            self.area_selecoes_dialogos,
            ft.Divider(height = 20, color = ft.Colors.TRANSPARENT),
            self.area_botoes
            ],scroll = ft.ScrollMode.AUTO,
            expand = True,
            spacing = 20
        )
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
                            icon_color = ft.Colors.with_opacity(0.5,"#011526"),
                            padding = 10,
                            on_click = lambda _: self.page.go("/principal")
                        ),
                        ft.Container(expand = True),
                        ft.IconButton(
                            icon = ft.Icons.MINIMIZE,
                            icon_color = ft.Colors.with_opacity(0.5,"#011526"),
                            on_click = lambda _: self.executar_minimizar_tela_os(_)
                        ),
                        ft.IconButton(
                            icon = ft.Icons.DESKTOP_WINDOWS_SHARP,
                            icon_color = ft.Colors.with_opacity(0.5,"#011526"),
                            on_click = lambda _: self.executar_maximizar_tela_os(_)
                        ),
                        ft.IconButton(
                            icon = ft.Icons.CLOSE,
                            icon_color = ft.Colors.with_opacity(0.5,"#011526"),
                            on_click = lambda _: self.executar_fechar_sistema(_)
                        )
                    ]
                )
            )
        )
        coluna_principal = ft.Container(
            content = ft.Column(
                controls = [
                    app_bar,*self.criar_conteudo()
                ]
            ), image = ft.DecorationImage(
                src = "background_tela1.jpg",
                fit = ft.ImageFit.COVER,
            ),bgcolor = ft.Colors.BLACK,
            expand = True,
            padding = 10
        )
        return ft.View(route,controls = [coluna_principal],padding = 0)
