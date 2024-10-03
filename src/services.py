from conexao import*

def enviar_dados(nome, email, senha):
    criar_usuario(nome, email, senha)

def criar_usuario(nome, email, senha):
    if conn.is_conected():
        print('Banco conectado!')

        cursor = conn.cursor()

        sql = 'insert into usuario (nome, email, senha) values'
        values = (nome, email, senha)

        cursor .execute(sql, values)
        conn.commit()
        conn.close()
        conn.close()


    else:
        print('Falha ao tentar conectar com o banco')

def listar_usuario():
    if conn.is_conected():
        print('Banco de dados conectadcom sucesso;')

        cursor = conn.cursor()

        cursor.execute('select ID, nome, email from usuario;')

        usuario = cursor.fetchall()
        return usuario
    else:
        print('Falha ao conectar com o banco de dados!')

def remover_usuario():
    if conn.is_connected():
        print('Banco conectado com sucesso!')

    cursor = conn.cursor

    sql_select = 'select ID, nome, email from usuario where email=%s;'
    cursor.execute(sql_select,(email,))

    usuario = cursor.fetchone()
    if usuario:
        print('usuario encontrado!')
        sql_delete = 'delete from usuario where email=%s'
        cursor.execute(sql_delete, (email,))
        print('Usuario deletado com sucesso!')
        conn.commit()
        cursor.close()
        conn.close()
else:
print('Usuario não encontrado!')



