import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='root', passwd='root', host='127.0.0.1', port=3306)

conn.cursor().execute("DROP DATABASE IF EXISTS `pi_grupo04_2021`;")
conn.commit()

criar_tabelas = '''SET NAMES utf8;
    CREATE DATABASE `pi_grupo04_2021` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;
    USE `pi_grupo04_2021`;
    CREATE TABLE `POSTO` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `preco` float(11) NOT NULL,
      `produto` varchar(20) NOT NULL,
      `bairro` varchar(20) NOT NULL,
      `nome` varchar(50) COLLATE utf8_bin NOT NULL,
      `bandeira` varchar(50) NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;'''

conn.cursor().execute(criar_tabelas)

# inserindo POSTOS
cursor = conn.cursor()
cursor.executemany(
      'INSERT INTO pi_grupo04_2021.POSTO (id, preco, produto, bairro, nome, bandeira) VALUES (%s, %s, %s, %s, %s, %s)',
      [
            (1, 5.9, 'GASOLINA', 'BUTANTA', 'POSTO UNIVERSIDADE EIRELI', 'IPIRANGA'),
            (2, 5.3, 'ETANOL', 'JARDIM PAULISTA', 'AUTO POSTO JOSE MARIA LISBOA LTDA', 'PETROBRAS DISTRIBUIDORA S.A.'),
            (3, 5.4, 'ETANOL', 'SANTA CECILIA', 'POSTO MARECHAL LTDA', 'BRANCA')
      ])

cursor.execute('select * from pi_grupo04_2021.POSTO')
print(' -------------  POSTOS:  -------------')
for posto in cursor.fetchall():
    print(posto[1])


conn.commit()
cursor.close()
