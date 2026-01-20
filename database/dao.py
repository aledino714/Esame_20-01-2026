from database.DB_connect import DBConnect
from model.artist import Artist

class DAO:

    @staticmethod
    def get_all_artists():

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ 
                SELECT *
                FROM artist a
                """
        cursor.execute(query)
        for row in cursor:
            artist = Artist(id=row['id'], name=row['name'])
            result.append(artist)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_all_nodes():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT ar.id, ar.name, COUNT(*) as numero_album
                    FROM artist ar, album al
                    WHERE ar.id = al.artist_id
                """

        cursor.execute(query)

        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_all_edges():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT DISTINCT a1.artist_id as id1, a2.artist_id as id2, COUNT(*) as peso
                    FROM album a1, album a2, track t1, track t2
                    WHERE t1.genre_id = t2.genre_id
                """

        cursor.execute(query)

        for row in cursor:
            # RIGA CRUCIALE:
            # row è {'id1': 12, 'id2': 45, 'peso' : 2}, così salvo (12, 45, 2)
            result.append((row['id1'], row['id2'], row['peso']))

        cursor.close()
        conn.close()
        return result
