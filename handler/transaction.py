from flask import jsonify

class TransactionHandler:
    def searchAlltransactions(self):
        return jsonify(Transactions = "All Transactions")

    def searchTransaction(self, args):
        price = args.get("price")
        qty = args.get("quantity")
        purchase_date = args.get("purchase_date")
        category = args.get("cat")
        if (len(args) ==3) and price and qty and purchase_date:
            return jsonify(Transactions = "Transactions with given price, quantity and purchase_date")
        if (len(args) ==2) and price and purchase_date:
            return jsonify(Transactions = "Transactions with given price and purchase_date")
        if (len(args) ==2) and price and qty:
            return jsonify(Transactions = "Transactions with given price and quantity")
        if (len(args) ==2) and qty and purchase_date:
            return jsonify(Transactions = "Transactions with given quantity and purchase_date")
        if (len(args) ==1) and qty:
            return jsonify(Transactions = "Transactions with given quantity")
        if (len(args) ==1) and purchase_date:
            return jsonify(Transactions = "Transactions on given purchase_date")
        if (len(args) ==1) and price:
            return jsonify(Transactions = "Transactions with given price")
        if (len(args) ==1) and category:
            return jsonify(Transactions = "Transactions from the given category")
        return jsonify(Transactions = "prueba")

    def searchAllResourceTransactions(self, rid):
        return jsonify(Transactions = "All transactions for specific resource")

    def searchResourceTransactions(self, rid, args):
        quantity = args.get("quantity")
        name = args.get("name")
        category = args.get("cat")
        if (len(args) ==3) and quantity and name and category:
            return jsonify(Transactions = "Transactions with resouce that have the given quantity, name and category")
        if (len(args) ==2) and quantity and name:
            return jsonify(Transactions = "Trnasaction with resource that have the given quantity and name")
        if (len(args) ==2) and quantity and category:
            return jsonify(Transactions = "Transaction with resource that have the given quantity and category")
        if (len(args) ==2) and category and name:
            return jsonify(Transactions = "Transaction with resource that have the given category and name")
        if (len(args)==1) and quantity:
            return jsonify(Transactions = "Transaction with resource that have the given quantity")
        if (len(args)==1) and category:
            return jsonify(Transactions = "Transaction with resource that have the given category")
        if (len(args)==1) and name:
            return jsonify(Transactions = "Transaction with resource that have the given name")
        return jsonify(Transactions = "Bad Request"), 404

    def searchAllNeederTransactions(self, nid):
        return jsonify(Transactions = "All transactions for given needer")

    def searchAllSupplierTransactions(self, sid):
        return jsonify(Transactions = "All transactions from given supplier")
## add the supplier check
