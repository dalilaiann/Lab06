from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    def getAnni(self):
        """Metodo che restituisce tutti gli anni presenti"""
        return DAO.getAnni()

    def getBrands(self):
        """Metodo che restituisce tutti i brand presenti"""
        return DAO.getBrands()

    def getRetailers(self):
        """Metodo che restituisce i retailers presenti"""
        return DAO.getRetailers()

    def getTopVendite(self, anno, brand, retailer):
        """Metodo che restituisce le migliori vendite per l'anno, il brand e il retailer specificati"""
        return DAO.getTopVendite(anno, brand, retailer)

    def getAnalizzaVendite(self, anno, brand, retailer):
        """Metodo che restituisce le statistiche per l'anno, il brand e il retailer specificati"""
        return DAO.getAnalizzaVendite(anno, brand, retailer)