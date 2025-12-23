import flet as ft
from telas.tela_principal import TelaPrincipal
from telas.tela_login import TelaLogin
from telas.tela_cadastro_cliente import CadastroCliente
from telas.tela_cadastro_produto import CadastroProduto
from telas.tela_cadastro_os import CadastroOs
from telas.tela_cadastro_despesas import CadastroDespesas
from telas.tela_cadastro_fornecedor import CadastroFornecedor
from telas.tela_gerenciar_estoque import GestaoEstoque

def main(page:ft.Page):
    tela_login = TelaLogin(page)
    page.window.title_bar_hidden = True
    page.window.title_bar_buttons_hidden = True
    page.window.width = 1200
    page.window.height = 800

    def roteador_paginas(_):
        page.views.clear()
        if page.route == '/':
            view_login = tela_login.get_view(page.route)
            page.views.append(view_login)
        elif page.route.startswith('/principal'):
            page.views.clear()
            tela_principal = TelaPrincipal(page)
            view_principal = tela_principal.get_view(page.route)
            page.views.append(view_principal)
        elif page.route.startswith('/cadastro_cliente'):
            page.views.clear()
            tela_cadastro_clientes = CadastroCliente(page)
            view_tela_cadastro_clientes = tela_cadastro_clientes.get_view(page.route)
            page.views.append(view_tela_cadastro_clientes)
        elif page.route.startswith('/cadastro_produto'):
            page.views.clear()
            tela_cadastro_produto = CadastroProduto(page)
            view_tela_cadastro_produtos = tela_cadastro_produto.get_view(page.route)
            page.views.append(view_tela_cadastro_produtos)
        elif page.route.startswith('/cadastro_os'):
            page.views.clear()
            tela_cadastro_os = CadastroOs(page)
            view_tela_cadastro_os = tela_cadastro_os.get_view(page.route)
            page.views.append(view_tela_cadastro_os)
        elif page.route.startswith('/cadastro_despesas'):
            page.views.clear()
            tela_cadastro_despesas = CadastroDespesas(page)
            view_tela_cadastro_despesas = tela_cadastro_despesas.get_view(page.route)
            page.views.append(view_tela_cadastro_despesas)
        elif page.route.startswith('/cadastro_fornecedor'):
            page.views.clear()
            tela_cadastro_fornecedor = CadastroFornecedor(page)
            view_tela_cadastro_fornecedor = tela_cadastro_fornecedor.get_view(page.route)
            page.views.append(view_tela_cadastro_fornecedor)
        elif page.route.startswith('/gestao_estoque'):
            page.views.clear()
            tela_gestao_estoque = GestaoEstoque(page)
            view_tela_gestao_estoque = tela_gestao_estoque.get_view(page.route)
            page.views.append(view_tela_gestao_estoque)

        page.update()
    page.on_route_change = roteador_paginas
    page.go(page.route)

if __name__ == '__main__':
    ft.app(target=main, assets_dir="assets")