from peewee import (PostgresqlDatabase, Model, TextField, 
                    IntegerField, ForeignKeyField, DateTimeField)

db = PostgresqlDatabase('nome do database',port=5432,user='postgres',password='123456')

# Coloque o nome do database, port , user e password
# o database já precisa esta criado

class BaseModel(Model):
    class Meta():
        database = db

class Categoria(BaseModel):
    descricao = TextField()


class Usuarios(BaseModel):
    nome = TextField()
    email = TextField(unique=True)
    cpf = TextField(unique=True)
    telefone = IntegerField(unique=True)
    confirme = TextField()
    senha = TextField()


class Enderecos(BaseModel):
    rua = TextField()
    bairro = TextField()
    numero = IntegerField(unique=True)
    cep = TextField()
    complemento = TextField()
    usuario = ForeignKeyField(Usuarios, backref='Enderecos')# nome do usuario



class Produtos(BaseModel):
    nome_produto = TextField()
    valor = IntegerField()
    categoria = ForeignKeyField(Categoria, backref='Produtos') # nome da categoria
    quantidade = IntegerField()
    url_imagem = TextField() # url da imagem do produto



#class Historico_Precos(BaseModel):
    ##id_produto = ForeignKeyField(Produtos, backref='Historico_Precos')
    #valor = IntegerField()
    #data = DateTimeField()


#class Vendas(BaseModel):
    #id_produto = ForeignKeyField(Produtos, backref='Vendas')
    #id_cliente = ForeignKeyField(Cliente, backref='Vendas')
    #data = DateTimeField()
    #quantidade = IntegerField()
    #valorUnitario = IntegerField()
    #valorTotal = IntegerField()


db.connect()
db.create_tables([Usuarios,Produtos,Enderecos,Categoria])
db.close()
