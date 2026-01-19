import flet as ft
from database.dao import DAO
from datetime import datetime
from geopy import distance

class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def populate_dd_year(self):
        return self._model.get_all_year()


    def populate_dd_shape(self):
        return self._model.get_all_shape()

        """ Metodo per popolare i dropdown """
        """"        
        sighting=DAO.read_sighting()
        lista_anni=[]
        lista_forme=[]

        # popolo dropdown anni
        for s in sighting:
            if 1910 <= s.s_datetime.year <= 2014:
                lista_anni.append(s.s_datetime.year)
        anni=sorted(set(lista_anni))
        for a in anni:  # devo ciclare sulle liste che voglio aggiungere
            self._view.dd_year.options.append(ft.dropdown.Option(str(a)))  # vuole sempre una striga

        self._view.page.update()

        # popolo dropdown forme
        for s in sighting:
            lista_forme.append(s.shape)
        forme=sorted(set(lista_forme))
        for f in forme:  # devo ciclare sulle liste che voglio aggiungere
            self._view.dd_shape.options.append(ft.dropdown.Option(str(f)))
        self._view.page.update()

        # TODO
    """

    def handle_graph(self, e):
        """ Handler per gestire creazione del grafo """
        anno=int(self._view.dd_year.value )
        forma=self._view.dd_shape.value

        self._model.build_graph(anno, forma)

        lista_somme=[]

        # per ogni nodo devo mettere la somma=0
        # non è la somma totale ma per ogni nodo devo fare la somma
        # visto che mi chiede la somm di entrambi
        for nodo in self._model.G.nodes():
            somma=0

            for vicino in self._model.G.neighbors(nodo):
                peso=self._model.G[nodo][vicino]['weight']
                somma+=peso
            lista_somme.append((nodo, somma))

        for (n,s) in lista_somme:
            self._view.lista_visualizzazione_1.controls.append(ft.Text(f" {n}---> {s} "))
        self._view.page.update()


    """
        lista_somme=[]
        try:
            anno=self._view.dd_year.value
        except ValueError:
            self._view.alert.show_alert('inserire un anno ')
            return
        try:
            forma = self._view.dd_shape.value
        except ValueError:
            self._view.alert.show_alert('inserire una forma ')
            return

        self._model.build_graph(anno, forma)

        # in questo modo posso iterare sui vari nodi

        for nodo in self._model.G.nodes(): # itero sui vari nodi
            somma=0

            # preso tutti gli archi adiacenti a quel nodo
            for u, v, attr in self._model.G.edges(nodo, data=True):  # se metto data=True mi restituisce anche i pesi
                somma+=attr['weight'] # itero sugli edges

            lista_somme.append((nodo, somma))

        self._view.lista_visualizzazione_1.controls.append(ft.Text(f" Numero vertici: {self._model.G.number_of_nodes()} Numero di archi {self._model.G.number_of_edges()} "))

        for nodo, somma in lista_somme:
            self._view.lista_visualizzazione_1.controls.append(ft.Text(f" Nodo {nodo}, somma pesi su archi = {somma}"))

        self._view.update()


        # TODO
    """

    def handle_path(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del cammino """

        cammino, distanza= self._model.percorso_semplice()

        self._view.lista_visualizzazione_2.controls.append(ft.Text(f"peso totale {distanza}"))

        for i in range(len(cammino)-1):
            n1=cammino[i]
            n2=cammino[i+1]

            # per ogni stato mi calcolo il peso
            peso=self._model.G[n1][n2]['weight']


            # la distanza geo
            s1=self._model._map_nodi[n1]
            s2=self._model._map_nodi[n2]

            dist_geo = distance.geodesic(
                (s1.lat, s1.lng),
                (s2.lat, s2.lng)).km

            self._view.lista_visualizzazione_2.controls.append(ft.Text(f"{n1}---> {n2} con peso {peso} e distanza {dist_geo:.2f} "))
        self._view.page.update()

    """

        # controllare che il grafo dia gia stato creato

        if self._model.G is None or self._model.G.number_of_nodes() == 0:
            self._view.alert.show_alert('creare un grafo prima')
            return
        # richiamo la funzione
        self._model.percorso_semplice()
        percorso = self._model._best_percorso
        distanza_tot = self._model._best_distanza
        dettagli = self._model.get_dettagli_percorso()

        self._view.lista_visualizzazione_2.controls.clear()

        if len(percorso) < 2:
            self._view.lista_visualizzazione_2.controls.append(
                ft.Text("Nessun percorso valido trovato")
            )
            self._view.update()
            return
        self._view.lista_visualizzazione_2.controls.append(
            ft.Text(f"peso cammino massimo: {distanza_tot}"))

        for s1, s2, peso, dist in dettagli:
            self._view.lista_visualizzazione_2.controls.append(
                ft.Text(f"{s1} → {s2} | peso = {peso} | distanza = {dist:.2f} km"))
        self._view.update()

        # TODO




# for nodo in self._model.G.nodes() --> itero sui vai nodi
# self.G.edges(nodo) --> itero sui vari archi--> se metto data = tru mi teine traccia anche del peso

"""
