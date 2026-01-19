from database.DB_connect import DBConnect
from model.state import State
from model.sighting import Sighting

class DAO:
    @staticmethod
    def read_sightings():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select id, s_datetime, shape, latitude,longitude 
                    from sighting s"""

        cursor.execute(query)

        for row in cursor:
            result.append(Sighting(**row)) # in questo modo importo tutta la classe senza ricopiare tutto

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def read_all_state():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select id, name, lat, lng
                    from state s  """

        cursor.execute(query)

        for row in cursor:
            result.append(State(**row))  # in questo modo importo tutta la classe senza ricopiare tutto

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def read_all_vicini(anno, forma):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select state1, state2, count(*) as peso 
                    from neighbor n, sighting s  
                    where (n.state1=s.state  or n.state2=s.state) and YEAR(s.s_datetime)=%s
                    and s.shape=%s
                    group by state1, state2"""

        cursor.execute(query, (anno,forma))

        for row in cursor:
            result.append((row['state1'], row['state2'], row['peso']))  # in questo modo importo tutta la classe senza ricopiare tutto

        cursor.close()
        conn.close()
        return result



