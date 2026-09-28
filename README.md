# Lanchê Fácil

Sistema de gerenciamento de pedidos da lanchonete Lanchê Fácil, desenvolvido em Django para a disciplina de Desenvolvimento Web (UFRA).

## Funcionalidades

- CRUD de Clientes (cadastrar, listar, editar e excluir)
- CRUD de Produtos (cadastrar, listar, editar e excluir)
- CRUD de Pedidos (cadastrar, listar, editar e excluir)
- Cálculo do valor total do pedido (preço do produto x quantidade)
- Confirmação em JavaScript antes de excluir um pedido
- Interface responsiva com Bootstrap

## Tecnologias

- Python
- Django
- SQLite
- HTML, CSS e Bootstrap
- JavaScript
- Gunicorn (deploy)

## Como rodar o projeto

1. Clone o repositório:

    git clone https://github.com/leonardoferreiraf705-max/lanche-facil.git
    cd lanche-facil

2. Instale as dependências:

    pip install -r requirements.txt

3. Aplique as migrações:

    python manage.py migrate

4. Inicie o servidor:

    python manage.py runserver

5. Acesse http://127.0.0.1:8000 no navegador.

## Deploy

Aplicação publicada: https://lanche-facil.onrender.com

## Equipe

Nome da equipe: Lanchê Fácil

- Leonardo Ferreira Lopes
- Antônio Carlos Silva de Oliveira
- Viviane do Socorro Pantoja
- Adriana Nazaré Pereira
