import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff\
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.ddAnno=None
        self.ddBrand=None
        self.ddRetalier=None
        self.btnTopVendite=None
        self.btnAnalizzaVendite=None
        self.txt_result = None


    def load_interface(self):
        # title
        self._title = ft.Text("Analizza vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW 1
        self.ddAnno=ft.Dropdown(label="anno", width=300)
        self._controller.fillddAnno()
        self.ddBrand=ft.Dropdown(label="brand", width=300)
        self._controller.fillddBrand()
        self.ddRetailer=ft.Dropdown(label="retailer", width=600)
        self._controller.fillddRetailer()
        row1=ft.Row([self.ddAnno, self.ddBrand, self.ddRetailer], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        #ROW 2
        self.btnTopVendite=ft.ElevatedButton(text="Top vendite", width=200, on_click=self._controller.handleTopVendite)
        self.btnAnalizzaVendite=ft.ElevatedButton(text="Analizza vendite", width=250, on_click=self._controller.handleAnalizzaVendite)
        row2=ft.Row([self.btnTopVendite, self.btnAnalizzaVendite], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
