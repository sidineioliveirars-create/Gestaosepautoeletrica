import flet as ft
from telas.tela_base import TelaBase
from telas.tela_principal import TelaPrincipal

class TelaLogin(TelaBase):
    def __init__(self, page):
        self.tela_principal = TelaPrincipal(page)
        self.entrada_usuario = ft.TextField(label = 'Usuário',autofocus = True)
        self.entrada_senha = ft.TextField(label = 'Senha',can_reveal_password = True, password = True)
        self.area_entradas = ft.ResponsiveRow(controls = [self.entrada_usuario, self.entrada_senha])
        self.btn_entrar = ft.ElevatedButton(text = 'Entrar', on_click = self.abrir_sistema, col=6)
        self.btn_cadastrar_usuario = ft.ElevatedButton(text = 'Cadastrar-se',col=6)
        self.area_botoes = ft.ResponsiveRow(controls = [self.btn_entrar, self.btn_cadastrar_usuario])
        super().__init__(page)
        self.page = page
        self.titulo = page.title = 'Login'
        self.controls = self.criar_conteudo()
        page.update()
    def criar_conteudo(self):
        return [
            self.area_entradas, self.area_botoes
        ]


    def get_view(self, router):
        coluna_principal = ft.Column(controls = self.controls,expand=True)
        return ft.View(router,[coluna_principal])


    def abrir_sistema(self, _e):
        self.page.go('/principal/')
        self.page.update()