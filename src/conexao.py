import mysql
import mysql.connector

conn = mysql.connector.connect(
    username = 'dias',
    hostname = 'localhost',
    password = 'r123',
    db = 'projeto crud'    
)

if conn.is_conected():
     print('Conectado com o banco')
else:
     print('Não conectado com o banco')