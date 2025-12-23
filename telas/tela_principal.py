import flet as ft


from telas.tela_base import TelaBase
from telas.tela_cadastro_cliente import CadastroCliente
from telas.tela_cadastro_produto import CadastroProduto
from telas.tela_cadastro_os import CadastroOs
from telas.tela_cadastro_despesas import CadastroDespesas
from telas.tela_cadastro_fornecedor import CadastroFornecedor
from telas.tela_gerenciar_estoque import GestaoEstoque

class TelaPrincipal(TelaBase):
    def __init__(self, page):
        self.cadastro_clientes = CadastroCliente(page)
        self.cadastro_produtos = CadastroProduto(page)
        self.cadastro_os = CadastroOs(page)
        self.cadastro_despesas = CadastroDespesas(page)
        self.cadastro_fornecedor = CadastroFornecedor(page)
        self.gestao_estoque = GestaoEstoque(page)
        self.btn_stilo_neon = ft.ButtonStyle(
            color = {
                ft.ControlState.HOVERED: ft.Colors.CYAN_ACCENT,
                ft.ControlState.DEFAULT: ft.Colors.BLACK,
            },
            bgcolor = {
                ft.ControlState.HOVERED: ft.Colors.with_opacity(0.1, ft.Colors.CYAN_ACCENT),
                ft.ControlState.DEFAULT: ft.Colors.WHITE
            },
            overlay_color = ft.Colors.with_opacity(0.2, ft.Colors.CYAN_ACCENT),
            shape = ft.RoundedRectangleBorder(radius = 10)
        )
        self.btn_cadastro_cliente = ft.ElevatedButton(text = 'Cadastrar Cliente',on_click = self.tela_cadastro_cliente, style = self.btn_stilo_neon,icon = ft.Icons.PERSON_ADD, col = 2, bgcolor = ft.Colors.with_opacity(0.3,"#011526"))
        self.btn_cadastro_produtos = ft.ElevatedButton(text = 'Cadastrar Produto', on_click = self.tela_cadastro_produtos, style = self.btn_stilo_neon,icon = ft.Icons.ADD_BOX_SHARP, col = 2, bgcolor = ft.Colors.with_opacity(0.3,"#011526"))
        self.btn_gerar_os = ft.ElevatedButton(text ='OS', on_click = self.tela_cadastro_os, style = self.btn_stilo_neon,icon = ft.Icons.CAR_REPAIR, col = 2, bgcolor = ft.Colors.with_opacity(0.3,"#011526"))
        self.btn_cadastro_fornecedor = ft.ElevatedButton(text = 'Cadastrar Fornecedor', on_click = self.tela_cadastro_fornecedor, style = self.btn_stilo_neon,icon = ft.Icons.LOCAL_SHIPPING, col = 2, bgcolor = ft.Colors.with_opacity(0.3,"#011526"))
        self.btn_cadastro_despesas = ft.ElevatedButton(text = 'Cadastrar Despesas', on_click = self.tela_cadastro_despesas, style = self.btn_stilo_neon,icon = ft.Icons.CREDIT_CARD_OUTLINED, col = 2, bgcolor = ft.Colors.with_opacity(0.3,"#011526"))
        self.btn_estoque = ft.ElevatedButton(text = 'Gerenciar Estoque', on_click = self.tela_estoque, style = self.btn_stilo_neon,icon = ft.Icons.RECEIPT_LONG, col = 2, bgcolor = ft.Colors.with_opacity(0.3,"#011526"))
        self.area_botoes = ft.ResponsiveRow(controls = [self.btn_cadastro_cliente, self.btn_cadastro_produtos, self.btn_gerar_os,
                                                        self.btn_cadastro_despesas, self.btn_cadastro_fornecedor, self.btn_estoque], alignment = ft.MainAxisAlignment.START, spacing = 10, expand=True)
        self.barra_pesquisa = ft.TextField(label='Buscar', icon=ft.Icons.FIND_IN_PAGE_SHARP, width = 250, bgcolor = ft.Colors.with_opacity(0.7, "#011526"),
                                           border_color = ft.Colors.with_opacity(0.5, ft.Colors.CYAN_ACCENT),
                                           focused_border_color = ft.Colors.CYAN_ACCENT,
                                           focused_border_width = 2,
                                           label_style = ft.TextStyle(color = ft.Colors.WHITE70),
                                           border_radius = 10)
        self.label_fluxo_caixa = ft.Text('Fluxo Caixa')
        self.fluxo_caixa = ft.TextField(label = 'Valor inicial do caixa', prefix_text = 'R$:', width = 150, bgcolor = ft.Colors.with_opacity(0.90, ft.Colors.WHITE))
        self.btn_abrir_caixa = ft.ElevatedButton('Abrir Caixa', icon = ft.Icons.PAYMENT)
        self.area_gestao_caixa = ft.Container(
            content = ft.Column([
                self.label_fluxo_caixa,
                self.fluxo_caixa,
                self.btn_abrir_caixa
            ],alignment = ft.MainAxisAlignment.START,horizontal_alignment = ft.CrossAxisAlignment.CENTER, spacing = 10),
            width = 200,
            height = 220,
            padding = 20,
            bgcolor = ft.Colors.with_opacity(0.9,color = ft.Colors.WHITE),
            border_radius = 16,
            border = ft.border.all(0.7, ft.Colors.CYAN_ACCENT)
        )

        super().__init__(page)
        self.page = page
        self.controls = self.criar_conteudo()
        self.titulo = page.title = 'S&P Auto Elétrica'
        page.update()


    def executar_minimizar(self,_e):
        self.page.window.minimized = True
        self.page.update()

    def executar_maximizar(self,_e):
        self.page.window.maximized = not self.page.window.maximized
        self.page.update()

    def executar_fechar_tela(self,_e):
        self.page.window.destroy()
        self.page.update()

    def criar_conteudo(self):
        cabecalho = ft.Container(
            content = ft.Row(controls = [ft.Text('S&P Auto Elétrica', size = 32, weight = ft.FontWeight.BOLD, color = ft.Colors.CYAN_ACCENT, italic = True,
                                                 style = ft.TextStyle(foreground = ft.Paint(gradient = ft.PaintLinearGradient((0,20),(150,20),[ft.Colors.CYAN_ACCENT, ft.Colors.PINK_ACCENT])))),ft.VerticalDivider(
                width = 30, color = ft.Colors.TRANSPARENT
            ),
                ft.Container(content = self.area_botoes,
                             expand = True,
                             alignment = ft.alignment.center
            )],alignment = ft.MainAxisAlignment.START,
                             vertical_alignment = ft.CrossAxisAlignment.CENTER
            ),
            bgcolor = ft.Colors.with_opacity(0.7, "#011526"),
            padding=ft.padding.symmetric(horizontal = 20, vertical = 10),
            border = ft.border.only(bottom = ft.BorderSide(2, ft.Colors.CYAN_ACCENT)),
            margin = ft.margin.all(10),
            shadow = ft.BoxShadow(
                spread_radius = 2,
                blur_radius = 50,
                color = ft.Colors.with_opacity(0.9, ft.Colors.CYAN_ACCENT),
                offset = ft.Offset(0,0)
            )



                )
        area_dashboard = ft.Container(
            content = ft.Column(
                controls = [
                    self.area_gestao_caixa
                ],alignment = ft.MainAxisAlignment.CENTER, horizontal_alignment = ft.CrossAxisAlignment.CENTER,

            ),padding = 10, alignment=ft.alignment.center

        )
        return [
            cabecalho, self.barra_pesquisa, area_dashboard
        ]

    def get_view(self, router):
        app_bar_responsivo = ft.WindowDragArea(
            content = ft.Container(
                padding = ft.padding.only(right = 5, top = 0),
                content = ft.Row(
                    alignment = ft.MainAxisAlignment.END,
                    controls = [
                        ft.IconButton(
                            icon = ft.Icons.MINIMIZE,
                            icon_color = ft.Colors.WHITE,
                            on_click = lambda _: self.executar_minimizar(_),
                            icon_size = 15
                        ),
                        ft.IconButton(
                            icon = ft.Icons.DESKTOP_WINDOWS_SHARP,
                            icon_color = ft.Colors.WHITE,
                            on_click = lambda _: self.executar_maximizar(_),
                            icon_size = 15
                        ),
                        ft.IconButton(
                            icon = ft.Icons.CLOSE,
                            icon_color = ft.Colors.WHITE,
                            on_click = lambda _: self.executar_fechar_tela(_),
                            icon_size = 15
                        )
                    ]
                )
            ),height = 15
        )
        view_tela_principal = ft.Container(content = ft.Column(controls = [app_bar_responsivo,*self.criar_conteudo()], alignment = ft.MainAxisAlignment.START, spacing = 10),
                                                image = ft.DecorationImage(src = "background_tela1.jpg", fit = ft.ImageFit.COVER),
                                           bgcolor = ft.Colors.BLACK, expand = True

        )
        return ft.View(router, controls = [view_tela_principal], padding = 0)


    def tela_cadastro_cliente(self, _e):
        self.page.go('/cadastro_cliente')
        self.page.update()

    def tela_cadastro_produtos(self, _e):
        self.page.go('/cadastro_produto')
        self.page.update()


    def tela_cadastro_os(self, _e):
        self.page.go('/cadastro_os')
        self.page.update()

    def tela_cadastro_fornecedor(self, _e):
        self.page.go('/cadastro_fornecedor')
        self.page.update()

    def tela_cadastro_despesas(self, _e):
        self.page.go('/cadastro_despesas')
        self.page.update()

    def tela_estoque(self, _e):
        self.page.go('/gestao_estoque')
        self.page.update()