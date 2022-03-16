import psycopg2

conexao = psycopg2.connect(host='localhost', user='postgres', password='123',database='postgres')

cursor = conexao.cursor()

def inserir(id,nome,telefone):

    comando = f'''insert into agenda (id,nome,telefone) values ('{id}','{nome}','{telefone}')'''
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()

def ler():
    comando = f'''select * from agenda'''
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)
    cursor.close()
    conexao.close()

def editar(alvo,mudanca,valorid):
    comando = f'''UPDATE agenda SET {alvo} = {mudanca} WHERE id = {valorid}'''
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()

