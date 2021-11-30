from models import Posto

SQL_DELETA_POSTO = 'delete from posto where id = %s'
SQL_POSTO_POR_ID = 'SELECT id, preco, produto, endereco, bairro, nome, bandeira FROM posto where id = %s'
SQL_ATUALIZA_POSTO = 'UPDATE posto SET preco=%s, produto=%s, endereco=%s, bairro=%s, nome=%s, bandeira=%s where id = %s'
SQL_BUSCA_POSTOS = 'SELECT id, preco, produto, endereco, bairro, nome, bandeira FROM posto'
SQL_CRIA_POSTO = 'INSERT INTO posto (preco, produto, endereco, bairro, nome, bandeira) values (%s, %s, %s, %s, %s, %s)'
SQL_BUSCA_POSTO_PELO_BAIRRO = 'SELECT id, preco, produto, endereco, bairro, nome, bandeira FROM posto WHERE UPPER(bairro) LIKE %s'


class PostoDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, posto):
        cursor = self.__db.connection.cursor()

        if (posto.id):
            cursor.execute(SQL_ATUALIZA_POSTO, (posto.preco, posto.produto, posto.endereco, posto.bairro, posto.nome, posto.bandeira, posto.id))
        else:
            cursor.execute(SQL_CRIA_POSTO, (posto.preco, posto.produto, posto.endereco, posto.bairro, posto.nome, posto.bandeira))
            posto.id = cursor.lastrowid
        self.__db.connection.commit()
        return posto

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_POSTOS)
        postos = traduz_postos(cursor.fetchall())
        return postos

    def busca_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_POSTO_POR_ID, (id,))
        tupla = cursor.fetchone()
        return Posto(tupla[1], tupla[2], tupla[3], id=tupla[0])

    def busca_por_bairro(self, bairro):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_POSTO_PELO_BAIRRO, ('%'+bairro.upper()+'%',))
        # data = cursor.fetchone()
        # if data:
        #     print("teeeem!" + bairro)
        # else:
        #     print("não tem bairrooo!")
        #return bairro
        postos = traduz_postos(cursor.fetchall())
        return postos

    #def listar_por_bairro(self):
    #    cursor = self.__db.connection.cursor()

    def deletar(self, id):
        self.__db.connection.cursor().execute(SQL_DELETA_POSTO, (id, ))
        self.__db.connection.commit()


def traduz_postos(postos):
    def cria_posto_com_tupla(tupla):
        return Posto(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], id=tupla[0])
    return list(map(cria_posto_com_tupla, postos))


def traduz_postos_por_bairro(postos):
     def busca_postos_por_bairro(tupla):
         return Posto(tupla[0], tupla[1], tupla[3], tupla[4], tupla[5], tupla[6], bairro=tupla[2])
     return list(map(busca_postos_por_bairro, postos))
