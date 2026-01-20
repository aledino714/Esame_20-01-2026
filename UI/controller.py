import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_create_graph(self, e):
        try:
            n_alb = float(self._view.txtNumAlbumMin.value)
        except ValueError:
            self._view.show_alert("Inserisci un numero valido per il numero di album minimi.")
            return

        self._view.txt_result.controls.clear()

        n_nodi, n_archi = self._model.build_graph(n_alb)

        self._view.txt_result.controls.append(ft.Text(f"Grafo creato: {n_nodi} nodi (artisti), {n_archi} archi"))

        self._view.update()

    def populate_dd(self):
        """ Metodo per popolare il dropdown artista """
        # 1. Svuoto le opzioni attuali
        self._view.ddArtist.options.clear()

        # 2. Ottengo la lista
        lista_artista = self._model.lista_artista

        # 3. Popolo il dropdown
        for artista in lista_artista:
            self._view.ddArtist.options.append(ft.dropdown.Option(key=artista, text=artista))

        self._view.update()

    def handle_connected_artists(self, e):
        pass


