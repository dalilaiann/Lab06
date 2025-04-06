import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._ddRetailerValue = None
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillddAnno(self):
        """Metodo che riempie il dropdown di anno"""
        anni=self._model.getAnni()
        self._view.ddAnno.options.append(ft.dropdown.Option("Nessuna opzione"))
        if anni!=[]:
            for anno in anni:
                self._view.ddAnno.options.append(ft.dropdown.Option(anno))
            self._view.update_page()
        else:
            self._view.create_alert("Non ci sono anni disponibili")
            self._view.update_page()

    def fillddBrand(self):
        """Metodo che riempie il dropdown brand"""
        brands = self._model.getBrands()
        self._view.ddBrand.options.append(ft.dropdown.Option("Nessuna opzione"))
        if brands!= []:
            for brand in brands:
                self._view.ddBrand.options.append(ft.dropdown.Option(brand))
                self._view.update_page()
        else:
            self._view.create_alert("Non ci sono brand disponibili")
            self._view.update_page()

    def fillddRetailer(self):
        """Metodo che riempie il dropdown di retailer"""
        retailers = self._model.getRetailers()
        self._view.ddRetailer.options.append(ft.dropdown.Option("Nessuna opzione"))
        if retailers != []:
            for retailer in retailers:
                self._view.ddRetailer.options.append(ft.dropdown.Option(key=retailer.Retailer_code, text=retailer.Retailer_name, data=retailer, on_click=self.read_retailer))
            self._view.update_page()
        else:
            self._view.create_alert("Non ci sono retailers disponibili")
            self._view.update_page()

    def read_retailer(self, e):
        self._ddRetailerValue=e.control.data

    def handleTopVendite(self, e):
        """Metodo che gestisce la stampa delle top 5 vendite"""
        self._view.txt_result.controls.clear()

        anno=self._view.ddAnno.value
        if anno=="Nessuna opzione":
            anno=None
        elif anno is None:
            self._view.create_alert("Seleziona un anno!")
            self._view.update_page()
            return

        brand=self._view.ddBrand.value
        if brand=="Nessuna opzione":
            brand=None
        elif brand is None:
            self._view.create_alert("Seleziona un brand!")
            self._view.update_page()
            return

        if self._view.ddRetailer.value=="Nessuna opzione":
            retailer=None
        elif self._view.ddRetailer.value is None:
            self._view.create_alert("Seleziona un Retailer!")
            self._view.update_page()
            return
        else:
            retailer = self._ddRetailerValue.Retailer_code

        res=self._model.getTopVendite(anno, brand, retailer)

        if res!=[]:
            for r in res:
                self._view.txt_result.controls.append(ft.Text(r))
                self._view.update_page()
        else:
            self._view.txt_result.controls.append(ft.Text("Non esiste una classifica per l'anno, il brand e il retailer specificati."))
            self._view.update_page()


    def handleAnalizzaVendite(self, e):
        """Metodo che analizza le vendite totali"""
        self._view.txt_result.controls.clear()

        anno = self._view.ddAnno.value
        if anno == "Nessuna opzione":
            anno = None
        elif anno is None:
            self._view.create_alert("Seleziona un anno!")
            self._view.update_page()
            return

        brand = self._view.ddBrand.value
        if brand == "Nessuna opzione":
            brand = None
        elif brand is None:
            self._view.create_alert("Seleziona un brand!")
            self._view.update_page()
            return

        if self._view.ddRetailer.value == "Nessuna opzione":
            retailer = None
        elif self._view.ddRetailer.value is None:
            self._view.create_alert("Seleziona un Retailer!")
            self._view.update_page()
            return
        else:
            retailer = self._ddRetailerValue.Retailer_code

        res = self._model.getAnalizzaVendite(anno, brand, retailer)

        if res != []:
            self._view.txt_result.controls.append(ft.Text("Statistiche vendite: "))
            for r in res:
                self._view.txt_result.controls.append(ft.Text(r))
                self._view.update_page()
        else:
            self._view.txt_result.controls.append(ft.Text("Non esiste una classifica per l'anno, il brand e il retailer specificati."))
            self._view.update_page()


