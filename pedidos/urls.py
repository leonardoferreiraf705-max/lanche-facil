from django.urls import path
from . import views


urlpatterns = [
    path("", views.inicio, name="inicio"),

    path("clientes/", views.lista_clientes, name="lista_clientes"),
    path("clientes/cadastrar/", views.cadastrar_cliente, name="cadastrar_cliente"),
    path("clientes/editar/<int:id>/", views.editar_cliente, name="editar_cliente"),
    path("clientes/excluir/<int:id>/", views.excluir_cliente, name="excluir_cliente"),

    path("produtos/", views.lista_produtos, name="lista_produtos"),
    path("produtos/cadastrar/", views.cadastrar_produto, name="cadastrar_produto"),
    path("produtos/editar/<int:id>/", views.editar_produto, name="editar_produto"),
    path("produtos/excluir/<int:id>/", views.excluir_produto, name="excluir_produto"),

    path("pedidos/", views.lista_pedidos, name="lista_pedidos"),
    path("pedidos/cadastrar/", views.cadastrar_pedido, name="cadastrar_pedido"),
    path("pedidos/editar/<int:id>/", views.editar_pedido, name="editar_pedido"),
    path("pedidos/excluir/<int:id>/", views.excluir_pedido, name="excluir_pedido"),
]