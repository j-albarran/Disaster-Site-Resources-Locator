from flask import jsonify

class TransactionHandler:
    def searchAlltransactions(self):
        return "All Transactions"

    def searchTransaction(self, args):
        price = args.get("price")
        qty = args.get("quantity")
        purchase_date = args.get("purchase_date")
        if (len(args) ==3) and price and qty and purchase_date:
            return "Transactions with given price, quantity and purchase_date"
        if (len(args) ==2) and price and purchase_date:
            return "Transactions with given price and purchase_date"
        if (len(args) ==2) and price and qty:
            return "Transactions with given price and quantity"
        if (len(args) ==2) and qty and purchase_date:
            return "Transactions with given quantity and purchase_date"
        if (len(args) ==1) and qty:
            return "Transactions with given quantity"
        if (len(args) ==1) and purchase_date:
            return "Transactions on given purchase_date"
        if (len(args) ==1) and price:
            return "Transactions with given price"
        return "prueba"

    def searchAllResourceTransactions(self, rid):
        return "All transactions for specific resource"

    def searchResourceTransactions(self, rid, args):
        quantity = args.get("quantity")
        name = args.get("name")
        category = args.get("category")
        if (len(args) ==3) and quantity and name and category:
            return "Transactions with resouce that have the given quantity, name and category"
        if (len(args) ==2) and quantity and name:
            return "Trnasaction with resource that have the given quantity and name"
        if (len(args) ==2) and quantity and category:
            return "Transaction with resource that have the given quantity and category"
        if (len(args) ==2) and category and name:
            return "Transaction with resource that have the given category and name"
        if (len(args)==1) and quantity:
            return "Transaction with resource that have the given quantity"
        if (len(args)==1) and category:
            return "Transaction with resource that have the given category"
        if (len(args)==1) and name:
            return "Transaction with resource that have the given name"
        return "All transactions for Resource"

    def searchAllNeederTransactions(self, nid):
        return "All transactions for given needer"

    def searchNeederTransactions(self, nid, args):
        name = args.get("name")
        last_name = args.get("last_name")
        city = args.get("city")
        if len(args)==3 and name and last_name and city:
            return "Transaction of given nedeer with given name, last_name and city"
        return "All transactions for given needer"
    ## add the needer check

    def searchAllSupplierTransactions(self, sid):
        return "All transactions from given supplier"
    ## add the supplier check