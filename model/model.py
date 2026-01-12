import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self._lista_nodi=[]
        self.lista_connessioni=[]
        self.map_connessioni={}

        self.G=nx.Graph()
        pass

    def get_stati(self):
        lista_nodi=DAO.read_state()
        for s in lista_nodi:
            self._lista_nodi.append(s.id) # mi ricordo che devo mettere per entrabi gli id
        return self._lista_nodi


    def build_graph(self, anno, forma):

        # nodi

        self._lista_nodi=self.get_stati()
        self.G.add_nodes_from(self._lista_nodi)

        # archi

        archi=DAO.read_all_connessioni(anno, forma)

        for s1, s2, peso in archi:
            self.G.add_edge(s1, s2, weight=peso)


        return self.G



