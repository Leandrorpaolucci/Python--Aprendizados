"""

1º importação do flask, mas o flask funcionalidades iniciais

2º render_template, é a função que retorna um arquivo na função arquivo.html

→ 3º base.html, criamos a base para todas as paginas em um arquivo html e as outras paginas recebem tudo que está na → base.html

→ No espaço do html no bloco

<head>
    {% block head %}
        #código
    {% endblock %}
</head>

<head>
    {% block body %}
        #código
    {% endblock %}
</head>
{% extends 'base.html' %}
"""

"""
2º Organização estrutura do site e links

Sobre o navbar (menu), podemos colar toda estrutura navbar dentro da base html ou podemos criar um arquivo 'navbar.html'
e adicionar o parametro '{% include 'navbar.html' %}' dentro do body da base.html

FUNÇÃO DO FLASK 'url_for'
Ser importado aonde fica as funções de links @app.route('')

links - mudando para o nome da função, e padronizar os links pela função sem ter que mudar sempre o href da pagina 
assim evitamos a quebra de link caso o nome do link seja substituido no href

<a class="nav-link" href="{{ url_for('contato') }}">Contato</a>


"""

"""3º Token de segurança conhecido como csrf token para todo tipo de formulário (login/senha)
import secrets
secrets.token_hex(16)
app.config['SECRET_KEY'] = "chave"
"""

"""
4º pip install flask-wtf → Biblioteca de formulário para cada formulario
forms.py é importante para separar o local organizado depois importamos para o main

em todos os formulários
Method Not Allowed é liberar o método post na função do formulário methods
"""


"""
"""