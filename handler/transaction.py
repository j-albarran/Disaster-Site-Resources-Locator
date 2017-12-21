from flask import jsonify

class TransactionHandler:
    def __init__(self):
        self.transactions = [{'category': 'water',
                              'name': 'botella',
                              'nid': '4',
                              'price': '1',
                              'purchase_date': '12-13-2017',
                              'quantity': '2',
                              'rid': '9',
                              'sid': '1',
                              'tid': '1'},
                             {'category': 'food',
                              'name': 'salchicha',
                              'nid': '5',
                              'price': '2',
                              'purchase_date': '12-14-2017',
                              'quantity': '4',
                              'rid': '8',
                              'sid': '2',
                              'tid': '2'},
                             {'category': 'drugs',
                              'name': 'tylenol',
                              'nid': '6',
                              'price': '2.5',
                              'purchase_date': '12-15-2017',
                              'quantity': '6',
                              'rid': '7',
                              'sid': '3',
                              'tid': '3'},
                             {'category': 'water',
                              'name': 'galon',
                              'nid': '7',
                              'price': '1',
                              'purchase_date': '12-16-2017',
                              'quantity': '8',
                              'rid': '6',
                              'sid': '4',
                              'tid': '4'},
                             {'category': 'food',
                              'name': 'jamonilla',
                              'nid': '8',
                              'price': '3',
                              'purchase_date': '12-13-2017',
                              'quantity': '9',
                              'rid': '5',
                              'sid': '5',
                              'tid': '5'},
                             {'category': 'drugs',
                              'name': 'benadryl',
                              'nid': '2',
                              'price': '5',
                              'purchase_date': '12-14-2017',
                              'quantity': '7',
                              'rid': '4',
                              'sid': '6',
                              'tid': '6'},
                             {'category': 'fuel',
                              'name': 'gas',
                              'nid': '3',
                              'price': '3.6',
                              'purchase_date': '12-15-2017',
                              'quantity': '5',
                              'rid': '3',
                              'sid': '1',
                              'tid': '7'},
                             {'category': 'water',
                              'name': 'botella',
                              'nid': '4',
                              'price': '1',
                              'purchase_date': '12-16-2017',
                              'quantity': '3',
                              'rid': '2',
                              'sid': '2',
                              'tid': '8'},
                             {'category': 'food',
                              'name': 'oreo',
                              'nid': '5',
                              'price': '2',
                              'purchase_date': '12-13-2017',
                              'quantity': '1',
                              'rid': '1',
                              'sid': '3',
                              'tid': '9'},
                             {'category': 'drugs',
                              'name': 'tylenol',
                              'nid': '6',
                              'price': '2.5',
                              'purchase_date': '12-14-2017',
                              'quantity': '3',
                              'rid': '9',
                              'sid': '4',
                              'tid': '10'},
                             {'category': 'water',
                              'name': 'botella',
                              'nid': '7',
                              'price': '1',
                              'purchase_date': '12-15-2017',
                              'quantity': '4',
                              'rid': '8',
                              'sid': '5',
                              'tid': '11'},
                             {'category': 'food',
                              'name': 'galleta',
                              'nid': '1',
                              'price': '3',
                              'purchase_date': '12-16-2017',
                              'quantity': '6',
                              'rid': '7',
                              'sid': '6',
                              'tid': '12'},
                             {'category': 'drugs',
                              'name': 'antibiotico',
                              'nid': '2',
                              'price': '5',
                              'purchase_date': '12-13-2017',
                              'quantity': '8',
                              'rid': '6',
                              'sid': '1',
                              'tid': '13'},
                             {'category': 'fuel',
                              'name': 'diesel',
                              'nid': '3',
                              'price': '3.6',
                              'purchase_date': '12-14-2017',
                              'quantity': '9',
                              'rid': '5',
                              'sid': '2',
                              'tid': '14'},
                             {'category': 'water',
                              'name': 'botella',
                              'nid': '4',
                              'price': '1',
                              'purchase_date': '12-15-2017',
                              'quantity': '9',
                              'rid': '4',
                              'sid': '3',
                              'tid': '15'},
                             {'category': 'food',
                              'name': 'leche',
                              'nid': '9',
                              'price': '2',
                              'purchase_date': '12-16-2017',
                              'quantity': '5',
                              'rid': '3',
                              'sid': '4',
                              'tid': '16'},
                             {'category': 'drugs',
                              'name': 'benadryl',
                              'nid': '8',
                              'price': '2.5',
                              'purchase_date': '12-13-2017',
                              'quantity': '4',
                              'rid': '2',
                              'sid': '5',
                              'tid': '17'},
                             {'category': 'water',
                              'name': 'galon',
                              'nid': '6',
                              'price': '1',
                              'purchase_date': '12-14-2017',
                              'quantity': '3',
                              'rid': '1',
                              'sid': '6',
                              'tid': '18'},
                             {'category': 'food',
                              'name': 'pan',
                              'nid': '4',
                              'price': '3',
                              'purchase_date': '12-15-2017',
                              'quantity': '4',
                              'rid': '2',
                              'sid': '7',
                              'tid': '19'}]

    def searchAlltransactions(self):
        return jsonify(Transactions = self.transactions)

    def searchTransaction(self, args):
        price = args.get("price")
        qty = args.get("quantity")
        purchase_date = args.get("purchase_date")
        category = args.get("cat")
        if (len(args) ==3) and price and qty and purchase_date:
            result = []
            for row in self.transactions:
                if row['price'] == price and row['quantity'] == qty and row['purchase_date'] == purchase_date:
                    result.append(row)
            if not result:
                return jsonify(Error="No items found"), 404
            return jsonify(Transactions = result)
        if (len(args) ==2) and price and purchase_date:
            result = []
            for row in self.transactions:
                if row['price'] == price and row['purchase_date'] == purchase_date:
                    result.append(row)
            if not result:
                return jsonify(Error="No items found"), 404
            return jsonify(Transactions=result)
        if (len(args) ==2) and price and qty:
            result = []
            for row in self.transactions:
                if row['price'] == price and row['quantity'] == qty:
                    result.append(row)
            if not result:
                return jsonify(Error="No items found"), 404
            return jsonify(Transactions=result)
        if (len(args) ==2) and qty and purchase_date:
            result = []
            for row in self.transactions:
                if row['quantity'] == qty and row['purchase_date'] == purchase_date:
                    result.append(row)
            if not result:
                return jsonify(Error="No items found"), 404
            return jsonify(Transactions=result)
        if (len(args) ==1) and qty:
            result = []
            for row in self.transactions:
                if row['quantity'] == qty:
                    result.append(row)
            if not result:
                return jsonify(Error="No items found"), 404
            return jsonify(Transactions=result)
        if (len(args) ==1) and purchase_date:
            result = []
            for row in self.transactions:
                if row['purchase_date'] == purchase_date:
                    result.append(row)
            if not result:
                return jsonify(Error="No items found"), 404
            return jsonify(Transactions=result)
        if (len(args) ==1) and price:
            result = []
            for row in self.transactions:
                if row['price'] == price:
                    result.append(row)
            if not result:
                return jsonify(Error="No items found"), 404
            return jsonify(Transactions=result)
        if (len(args) ==1) and category:
            result = []
            for row in self.transactions:
                if row['category'] == category:
                    result.append(row)
            if not result:
                return jsonify(Error="No items found"), 404
            return jsonify(Transactions=result)
        return jsonify(Transactions = "Bad Request"), 400

    def searchAllResourceTransactions(self, rid):
        result = []
        print(rid)
        for row in self.transactions:
            if int(row['rid']) == rid:
                result.append(row)
                print(row)
        if not result:
            return jsonify(Error="No items found"), 404
        return jsonify(Transactions=result)

    def searchResourceTransactions(self, rid, args):
        qty = args.get("quantity")
        name = args.get("name")
        category = args.get("cat")
        if (len(args) ==3) and qty and name and category:
            result = []
            for row in self.transactions:
                if row['name'] == name and row['quantity'] == qty and row['cat'] == category and int(row['rid']) == rid:
                    result.append(row)
            if not result:
                return jsonify(Error="No items found"), 404
            return jsonify(Transactions=result)
        if (len(args) ==2) and qty and name:
            result = []
            for row in self.transactions:
                if row['name'] == name and row['quantity'] == qty and int(row['rid']) == rid:
                    result.append(row)
            if not result:
                return jsonify(Error="No items found"), 404
            return jsonify(Transactions=result)
        if (len(args) ==2) and qty and category:
            result = []
            for row in self.transactions:
                if row['quantity'] == qty and row['cat'] == category and int(row['rid']) == rid:
                    result.append(row)
            if not result:
                return jsonify(Error="No items found"), 404
            return jsonify(Transactions=result)
        if (len(args) ==2) and category and name:
            result = []
            for row in self.transactions:
                if row['name'] == name and row['cat'] == category and int(row['rid']) == rid:
                    result.append(row)
            if not result:
                return jsonify(Error="No items found"), 404
            return jsonify(Transactions=result)
        if (len(args)==1) and qty:
            result = []
            for row in self.transactions:
                if row['quantity'] == qty and int(row['rid']) == rid:
                    result.append(row)
            if not result:
                return jsonify(Error="No items found"), 404
            return jsonify(Transactions=result)
        if (len(args)==1) and category:
            result = []
            for row in self.transactions:
                if row['cat'] == category and int(row['rid']) == rid:
                    result.append(row)
            if not result:
                return jsonify(Error="No items found"), 404
            return jsonify(Transactions=result)
        if (len(args)==1) and name:
            result = []
            for row in self.transactions:
                if row['name'] == name and int(row['rid']) == rid:
                    result.append(row)
            if not result:
                return jsonify(Error="No items found"), 404
            return jsonify(Transactions=result)
        return jsonify(Transactions = "Bad Request"), 400

    def searchAllNeederTransactions(self, nid):
        result = []
        for row in self.transactions:
            if int(row['nid']) == nid:
                result.append(row)
        if not result:
            return jsonify(Error="No items found"), 404
        return jsonify(Transactions=result)

    def searchAllSupplierTransactions(self, sid):
        result = []
        for row in self.transactions:
            if row['sid'] == sid:
                result.append(row)
        if not result:
            return jsonify(Error="No items found"), 404
        return jsonify(Transactions=result)
## add the supplier check
