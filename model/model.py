import networkx as nx
from database.dao import DAO
from geopy import distance
from copy import copy

class Model:
    def __init__(self):
        self._map_nodi={}
        self.G=nx.Graph()

    def get_all_year(self):
        lista_anni=set()

        for o in DAO.read_sightings():
            if o.s_datetime.year>= 1910 and o.s_datetime.year<= 2015:
                lista_anni.add(o.s_datetime.year)
        return lista_anni

    def get_all_shape(self):
        shape=set() # metto un set cosi non mi conta i duplicati

        for o in DAO.read_sightings():
            shape.add(o.shape)
        return shape
    def load_map_nodi(self):
        for s in DAO.read_all_state():
            self._map_nodi[s.id]=s
        return self._map_nodi


    def build_graph(self, anno, forma ):
        #aggiugo i nodi
        self._map_nodi=self.load_map_nodi()

        lista_nodi=[id for id in self._map_nodi.keys()]
        self.G.add_nodes_from(lista_nodi)

        vicini=DAO.read_all_vicini(anno,forma)
        for (s1, s2, p) in vicini:
            self.G.add_edge(s1, s2, weight=p)
        return  self.G

    def percorso_semplice(self):
        self._best_percorso = []
        self._best_distanza = 0

        for nodo in self.G.nodes():
            self.__ricorsione(nodo,[nodo], 0, 0)
        return self._best_percorso, self._best_distanza


    def __ricorsione(self,nodo_corrente, lunghezza_parziale, peso_corrente, distanza):

        if distanza > self._best_distanza:
            self._best_percorso = lunghezza_parziale.copy()
            self._best_distanza = distanza

        for vicino in self.G.neighbors(nodo_corrente):
            if vicino in lunghezza_parziale:
                continue
            peso=self.G[nodo_corrente][vicino]['weight']
            if peso<=peso_corrente:
                continue
            s1 = self._map_nodi[nodo_corrente]  # oggetto State
            s2 = self._map_nodi[vicino]

            dist_geo = distance.geodesic(
                (s1.lat, s1.lng),
                (s2.lat, s2.lng)).km
            lunghezza_parziale.append(vicino)
            self.__ricorsione(vicino, lunghezza_parziale,peso, distanza + dist_geo )
            lunghezza_parziale.pop()



"""
    def __init__(self):
        self._lista_nodi=[]
        self.lista_connessioni=[]
        self.map_connessioni={}
        self._mappa_stato={}
        for s in DAO.read_state():
            self._mappa_stato[s.id]=s # mi creo la mappa con degli oggetti

        self._best_percorso=[]
        self._best_peso=0

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

    def percorso_semplice(self):
        self._best_percorso = []
        self._best_distanza = 0

        # scelgo tutti gli stati da cui partire
        for nodo in self.G.nodes():
            self.__ricorsione(percorso_corrente=[nodo], distanza_corrente=0,peso_ultimo=None)

        return self._best_percorso


    def __ricorsione(self, percorso_corrente, distanza_corrente, peso_ultimo):

        if distanza_corrente > self._best_distanza:
            self._best_distanza = distanza_corrente
            self._best_percorso = percorso_corrente.copy()
        # prendo l'ultimo elemento della lista
        last_node = percorso_corrente[-1]

        # esploro i vicini di last node

        for neighbor in self.G.neighbors(last_node):  # predo i nodi vicini
            if neighbor in percorso_corrente:
                continue   # se il vicino si trova gia in percorso corrente, vai avanti

            peso_arco=self.G.edges[last_node, neighbor]['weight']

            # vincolo peso crescente, il primo lo salta
            if peso_ultimo is not None and peso_arco<=peso_ultimo:
                continue

            # distanza geodesica
            coord1 = (self._mappa_stato[last_node].lat,
                      self._mappa_stato[last_node].lng)
            coord2 = (self._mappa_stato[neighbor].lat,
                      self._mappa_stato[neighbor].lng)

            dist_km = distance.geodesic(coord1, coord2).km

            percorso_corrente.append(neighbor)
            self.__ricorsione(percorso_corrente,distanza_corrente + dist_km,peso_arco)
            percorso_corrente.pop()

    def get_dettagli_percorso(self):
        dettagli = []
        for i in range(len(self._best_percorso) - 1):
            s1 = self._best_percorso[i]
            s2 = self._best_percorso[i + 1]

            peso = self.G.edges[s1, s2]['weight']

            coord1 = (self._mappa_stato[s1].lat, self._mappa_stato[s1].lng)
            coord2 = (self._mappa_stato[s2].lat, self._mappa_stato[s2].lng)

            dist_km = distance.geodesic(coord1, coord2).km

            dettagli.append((s1, s2, peso, dist_km))

        return dettagli

    # in generale metto il return quando la soluzione non soddisfa quei vincoli, quindi taglio il ramo. ui mi volfio solo salvare la soluzione migliore
    
"""







