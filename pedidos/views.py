from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Produto, Pedido


def inicio(request):
    return render(request, "pedidos/inicio.html")


def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, "pedidos/clientes.html", {"clientes": clientes})


def cadastrar_cliente(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        telefone = request.POST.get("telefone")

        Cliente.objects.create(
            nome=nome,
            telefone=telefone
        )

        return redirect("lista_clientes")

    return render(request, "pedidos/cadastrar_cliente.html")


def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == "POST":
        cliente.nome = request.POST.get("nome")
        cliente.telefone = request.POST.get("telefone")
        cliente.save()

        return redirect("lista_clientes")

    return render(
        request,
        "pedidos/editar_cliente.html",
        {"cliente": cliente}
    )


def excluir_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == "POST":
        cliente.delete()
        return redirect("lista_clientes")

    return render(
        request,
        "pedidos/excluir_cliente.html",
        {"cliente": cliente}
    )


def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, "pedidos/produtos.html", {"produtos": produtos})


def cadastrar_produto(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        categoria = request.POST.get("categoria")
        preco = request.POST.get("preco")

        Produto.objects.create(
            nome=nome,
            categoria=categoria,
            preco=preco
        )

        return redirect("lista_produtos")

    return render(request, "pedidos/cadastrar_produto.html")


def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)

    if request.method == "POST":
        produto.nome = request.POST.get("nome")
        produto.categoria = request.POST.get("categoria")
        produto.preco = request.POST.get("preco")
        produto.save()

        return redirect("lista_produtos")

    return render(
        request,
        "pedidos/editar_produto.html",
        {"produto": produto}
    )


def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id)

    if request.method == "POST":
        produto.delete()
        return redirect("lista_produtos")

    return render(
        request,
        "pedidos/excluir_produto.html",
        {"produto": produto}
    )


def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, "pedidos/pedidos.html", {"pedidos": pedidos})


def cadastrar_pedido(request):
    clientes = Cliente.objects.all()
    produtos = Produto.objects.all()

    if request.method == "POST":
        cliente_id = request.POST.get("cliente")
        produto_id = request.POST.get("produto")
        quantidade = int(request.POST.get("quantidade"))

        cliente = get_object_or_404(Cliente, id=cliente_id)
        produto = get_object_or_404(Produto, id=produto_id)

        valor_total = produto.preco * quantidade

        Pedido.objects.create(
            cliente=cliente,
            produto=produto,
            quantidade=quantidade,
            valor_total=valor_total
        )

        return redirect("lista_pedidos")

    return render(
        request,
        "pedidos/cadastrar_pedido.html",
        {
            "clientes": clientes,
            "produtos": produtos
        }
    )


def editar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)

    clientes = Cliente.objects.all()
    produtos = Produto.objects.all()

    if request.method == "POST":
        cliente_id = request.POST.get("cliente")
        produto_id = request.POST.get("produto")
        quantidade = int(request.POST.get("quantidade"))

        cliente = get_object_or_404(Cliente, id=cliente_id)
        produto = get_object_or_404(Produto, id=produto_id)

        pedido.cliente = cliente
        pedido.produto = produto
        pedido.quantidade = quantidade
        pedido.valor_total = produto.preco * quantidade
        pedido.save()

        return redirect("lista_pedidos")

    return render(
        request,
        "pedidos/editar_pedido.html",
        {
            "pedido": pedido,
            "clientes": clientes,
            "produtos": produtos
        }
    )


def excluir_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)

    if request.method == "POST":
        pedido.delete()
        return redirect("lista_pedidos")

    return render(
        request,
        "pedidos/excluir_pedido.html",
        {"pedido": pedido}
    )