import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._artists_list = []
        self.load_all_artists()
        self.lista_artista = []

    def load_all_artists(self):
        self._artists_list = DAO.get_all_artists()
        print(f"Artisti: {self._artists_list}")

    def load_artists_with_min_albums(self, min_albums):
        pass

    def build_graph(self, n_alb):
        # 1. Cancello il vecchio grafo prima di crearne uno nuovo
        self._graph.clear()

        # 2. Recupero i nodi dal DAO
        nodi1 = DAO.get_all_nodes()

        # 3. Applico qua il filtro sui nodi per gestire la durata inserita dall'utente
        for n in nodi1:
            if float(n['numero_album']) >= n_alb:
                # Aggiungo il nodo (ID) e salvo il nome come attributo per poi popolare il drowdown dopo (passaggio essenziale)
                self._graph.add_node(n['id'], name=n['name'])
                self.lista_artista.append(n['name'])

        # 4. Recupero gli archi dal DAO
        archi_totali = DAO.get_all_edges()

        # 5. Applico qua il filtro sugli archi, aggiungo l'arco solo se entrambi i nodi sono già nel grafo
        for row in archi_totali:
            u = row['id1']
            v = row['id2']
            w = row['peso']
            if u in self._graph.nodes and v in self._graph.nodes:
                self._graph.add_edge(u, v, weight=w)

        return len(self._graph.nodes), len(self._graph.edges)



