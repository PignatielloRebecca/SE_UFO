from database.DB_connect import DBConnect
from model.state import State
from model.sighting import Sighting

class DAO:
    @staticmethod
    def read_state():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select *
                    from state """

        cursor.execute(query)

        for row in cursor:
            result.append(State(**row)) # in questo modo importo tutta la classe senza ricopiare tutto

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def read_sighting():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select *
                    from sighting
                     ORDER BY s_datetime ASC"""

        cursor.execute(query)

        for row in cursor:
            result.append(Sighting(**row))  # in questo modo importo tutta la classe senza ricopiare tutto

        cursor.close()
        conn.close()
        return result
    @staticmethod

    def read_all_connessioni(anno, forma ):
            conn = DBConnect.get_connection()

            result = []

            cursor = conn.cursor(dictionary=True)
            query = """SELECT n.state1 AS id1, n.state2 AS id2,
                        COUNT(s.id) AS peso
                        FROM neighbor n, sighting s
                        WHERE (s.state = n.state1 OR s.state = n.state2)
                        AND YEAR(s.s_datetime) = %s
                        AND s.shape =%s
                        GROUP BY n.state1, n.state2 """

            cursor.execute(query, (anno, forma,))

            for row in cursor:
                result.append((row["id1"], row["id2"], row["peso"]))  # in questo modo importo tutta la classe senza ricopiare tutto

            cursor.close()
            conn.close()
            return result

    # nell'ultima query trovo il peso degli avvistamenti degli archi confinanti




