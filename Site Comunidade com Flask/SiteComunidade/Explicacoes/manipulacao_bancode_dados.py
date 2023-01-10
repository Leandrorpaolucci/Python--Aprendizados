"""
1º sempre que for iniciado algum comando no banco de dados tem que ter with
2º usuario, passaremos as informações que não entram automaticas no bd, no
3º para adicionar no banco de dados é session.add + commit
4º query
meus_usuarios = Usuario.query.all() | meus_usuarios = Usuario.query.first()
"""
# with app.app_context():
#     database.create_all()

# with app.app_context():
#     usuario = Usuario(username="Leandro", email="leandro@gmail.com", senha="123456")
#     usuario2 = Usuario(username="Rita", email="rita@gmail.com", senha="123456")
#     database.session.add(usuario)
#     database.session.add(usuario2)
#     database.session.commit()

# with app.app_context():
#     meus_usuarios = Usuario.query.all()
#     print(meus_usuarios)
#     primeiro_usuario = meus_usuarios[0]


# with app.app_context():
#     meus_usuarios = Usuario.query.all()
#     print(meus_usuarios)
#     primeiro_usuario = meus_usuarios[0]
#     print(primeiro_usuario)

# with app.app_context():
#     meus_usuarios = Usuario.query.all()
#     print(meus_usuarios)
#     primeiro_usuario = Usuario.query.first()
#     print(primeiro_usuario.id)
#     print(primeiro_usuario.email)
#     print(primeiro_usuario.posts)

# with app.app_context():
#     usuario_teste = Usuario.query.filter_by(email='leandro@gmail.com').first()
#     print(usuario_teste)
#     print(usuario_teste.username)

#criação do post
# with app.app_context():
#     meu_post = Post(id_usuario=1, titulo="Primeiro post do Leandro", corpo="Leandro")
#     database.session.add(meu_post)
#     database.session.commit()

# with app.app_context():
#     post = Post.query.all()
#     print(post)

# with app.app_context():
#     post = Post.query.first()
#     print(post.titulo)
#     print(post.autor.email)


# with app.app_context():
#     database.drop_all()
#     database.create_all()
#
# from sitecomunidade import app, database
# from sitecomunidade import *
# with app.app_context():
#     database.drop_all()
#     database.create_all()