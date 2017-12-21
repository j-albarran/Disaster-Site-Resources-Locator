from flask import jsonify


class SupplyHandler:
    def __init__(self):
        self.supply = [{' sid': '1',
                          'city': 'San Juan',
                          'qty': '2',
                          'region': 'San Juan',
                          'rid': '7',
                          'supply_date': '12-13-2017'},
                         {' sid': '2',
                          'city': 'Mayaguez ',
                          'qty': '3',
                          'region': 'Mayaguez',
                          'rid': '6',
                          'supply_date': '12-14-2017'},
                         {' sid': '3',
                          'city': 'Ponce',
                          'qty': '4',
                          'region': 'Ponce',
                          'rid': '5',
                          'supply_date': '12-15-2017'},
                         {' sid': '4',
                          'city': 'Bayamon',
                          'qty': '5',
                          'region': 'San Juan',
                          'rid': '4',
                          'supply_date': '12-16-2017'},
                         {' sid': '1',
                          'city': 'San Juan',
                          'qty': '6',
                          'region': 'San Juan',
                          'rid': '3',
                          'supply_date': '12-13-2017'},
                         {' sid': '2',
                          'city': 'Mayaguez ',
                          'qty': '7',
                          'region': 'Mayaguez',
                          'rid': '2',
                          'supply_date': '12-14-2017'},
                         {' sid': '3',
                          'city': 'Ponce',
                          'qty': '6',
                          'region': 'Ponce',
                          'rid': '1',
                          'supply_date': '12-15-2017'},
                         {' sid': '4',
                          'city': 'Bayamon',
                          'qty': '5',
                          'region': 'San Juan',
                          'rid': '5',
                          'supply_date': '12-16-2017'},
                         {' sid': '12',
                          'city': 'San Juan',
                          'qty': '4',
                          'region': 'San Juan',
                          'rid': '4',
                          'supply_date': '12-13-2017'},
                         {' sid': '2',
                          'city': 'Mayaguez ',
                          'qty': '3',
                          'region': 'Mayaguez',
                          'rid': '3',
                          'supply_date': '12-14-2017'},
                         {' sid': '3',
                          'city': 'Ponce',
                          'qty': '2',
                          'region': 'Ponce',
                          'rid': '2',
                          'supply_date': '12-15-2017'},
                         {' sid': '4',
                          'city': 'Bayamon',
                          'qty': '1',
                          'region': 'San Juan',
                          'rid': '1',
                          'supply_date': '12-16-2017'}]




    def searchSupplierResources(self, sid):
        result = []
        for row in self.supply:
            if int(row[' sid']) == int(sid):
                result.append(row)
        if not result:
            return jsonify(Error="No items found"), 404
        return jsonify(Supply=result)

    def searchResourceSupplier(self, rid):
        result = []
        for row in self.supply:
            if int(row['rid']) == int(rid):
                result.append(row)
        if not result:
            return jsonify(Error="No items found"), 404
        return jsonify(Supply=result)

    def searchAllsupplies(self):
        return jsonify(Supplies = self.supply)

    def searchSupplies(self, args):
        qty = args.get("qty")
        supply_date = args.get("supply_date")
        if (len(args) ==2) and qty and supply_date:
            result = []
            for row in self.supply:
                if int(row['qty']) == int(qty) and row['supply_date'] == supply_date:
                    result.append(row)
            if not result:
                return jsonify(Error="No items found"), 404
            return jsonify(Supply=result)
        elif (len(args) == 1) and supply_date:
            result = []
            for row in self.supply:
                if row['supply_date'] == supply_date:
                    result.append(row)
            if not result:
                return jsonify(Error="No items found"), 404
            return jsonify(Supply=result)
        elif (len(args) == 1) and qty:
            result = []
            for row in self.supply:
                if int(row['qty']) == int(qty):
                    result.append(row)
            if not result:
                return jsonify(Error="No items found"), 404
            return jsonify(Supply=result)
        return jsonify(Supplies = "Bad Request"), 400

    def searchSuppliesbyRegion(self, region):
        result = []
        for row in self.supply:
            if row['region'] == region:
                result.append(row)
        if not result:
            return jsonify(Error="No items found"), 404
        return jsonify(Supply=result)

    def searchSuppliesSuppliers(self, args):
        city = args.get("city")
        if (len(args) ==1) and city:
            result = []
            for row in self.supply:
                if row['city'] == city:
                    result.append(row)
            if not result:
                return jsonify(Error="No items found"), 404
            return jsonify(Supply=result)
        return jsonify(Supplies="Bad Request"), 400
            
