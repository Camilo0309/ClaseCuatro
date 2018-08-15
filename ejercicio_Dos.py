print('')
print('.................')
print('MENU DE OPCIONES')
print('.................')
print('1. Crear usuario')
print('2. Crear Post')
print('3. Crear Comment')
print('4. buscar Usuario')
print('')
opcion = int(input('QUE OPCION DESEA REALIZAR ?'))
print('')

class Usuario:
    id_user = 0
    nombre_user = ""
    pass_user = ""

    def __init__(self, id_user, nombre_user, pass_user):
        self.id_user = id_user
        self.nombre_user = nombre_user
        self.pass_user = pass_user

class Post:
    id_post = ""
    desc_post = ""

    def __init__(self, id_post, desc_post):
        self.id_post = id_post
        self.desc_post = desc_post


class Comment:
    id_comment = 0
    desc_comment = ""

    def __init__(self, id_comment, desc_comment):
        self.id_comment = id_comment
        self.desc_comment = desc_comment






