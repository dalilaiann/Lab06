from database.DB_connect import DBConnect
from model.Go_retailer import GoRetailer


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAnni():
        """Metodo che legge tutti gli anni distinti nel database"""
        cnx=DBConnect.get_connection()
        res=[]
        if cnx is None:
            return res
        else:
            cursor=cnx.cursor()

        query="""select distinct YEAR(date)
                 from go_daily_sales"""
        cursor.execute(query)


        for row in cursor:
            res.append(row[0])

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getBrands():
        """Metodo che legge tutti i brand distinti nel database"""
        cnx=DBConnect.get_connection()
        res=[]
        if cnx is None:
            return res
        else:
            cursor=cnx.cursor()


        query = """select distinct Product_brand
                   from go_products gp """
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row[0])

        cursor.close()
        cnx.close()
        return res


    @staticmethod
    def getRetailers():
        """Metodo che gestisce tutti i retailers diversi presenti nel database"""
        cnx = DBConnect.get_connection()
        res = []
        if cnx is None:
            return res
        else:
            cursor = cnx.cursor(dictionary=True)

        query = """select *
                   from go_retailers gr """

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(GoRetailer(**row))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getTopVendite(anno, brand, retailer):
        """Metodo che ritorna le migliori vendite presenti nel database per l'anno, il brand e il retailer specificati"""
        cnx = DBConnect.get_connection()
        res = []
        if cnx is None:
            return res
        else:
            cursor = cnx.cursor(dictionary=True)

        query = """ SELECT *
                    FROM go_daily_sales g, go_products p
                    WHERE YEAR(g.date)=COALESCE(%s, YEAR(g.date)) AND p.Product_brand=COALESCE(%s, p.Product_brand) AND g.Retailer_code=COALESCE(%s, g.Retailer_code) AND p.Product_number=g.Product_number
                    ORDER BY g.Unit_sale_price*g.Quantity DESC"""

        cursor.execute(query, (anno, brand, retailer))

        res = []
        for row in cursor:
            res.append(f"Data: {row["Date"]}; Ricavo: {row["Unit_sale_price"]*row["Quantity"]}; Retailer: {row["Retailer_code"]}; Product: {row["Product_number"]}")

        cursor.close()
        cnx.close()
        if len(res)<=5:
            return res
        else:
            return res[0:5]

    @staticmethod
    def getAnalizzaVendite(anno, brand, retailer):
        """Metodo che restituisce le migliori statistiche calcolate nel database a partire dall'anno, il brand e il retailer specificati"""
        cnx = DBConnect.get_connection()
        res = []
        if cnx is None:
            return res
        else:
            cursor = cnx.cursor(dictionary=True)

        query = """ select SUM(g.Quantity*g.Unit_sale_price) as somma, COUNT(*) as vendite, COUNT(distinct g.Retailer_code) as r, COUNT(distinct g.Product_number) as p
                    from go_daily_sales g, go_products p
                    WHERE YEAR(g.date)=COALESCE(%s, YEAR(g.date)) AND p.Product_brand=COALESCE(%s, p.Product_brand) AND g.Retailer_code=COALESCE(%s, g.Retailer_code) AND p.Product_number=g.Product_number"""

        cursor.execute(query, (anno, brand, retailer))

        res = []
        for row in cursor:
            res.append(f"Giro d'affari: {row["somma"]}\n"
                       f"Numero vendite: {row["vendite"]}\n"
                       f"Numero retailers coinvolti: {row["r"]}\n"
                       f"Numero prodotti coinvolti: {row["p"]}\n")

        cursor.close()
        cnx.close()
        return res

if __name__ == '__main__':
    print(DAO.getAnalizzaVendite(2017, "Star", "Grand choix"))
