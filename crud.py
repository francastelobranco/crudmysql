import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='bdcrud',
)

cursor = conexao.cursor()

nome_produto = "notebook"
valor = 3000

# INSERT
# comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", "{valor}")'
# cursor.execute(comando)
# conexao.commit()  # edita o banco de dados

# READ
# comando = f'SELECT * FROM bdcrud.vendas;")'
# cursor.execute(comando)
# resultado = cursor.fetchall()  # lê o comando no banco de dados

# UPDATE
# valor = 4000
# comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit()  # edita o banco de dados

# DELETE
# produto_a_ser_deletado = "notebook"
# comando = f'DELETE FROM vendas WHERE nome_produto = "{produto_a_ser_deletado}"'
# cursor.execute(comando)
# conexao.commit()  # edita o banco de dados

cursor.close()
conexao.close()
