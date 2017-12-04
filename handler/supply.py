from flask import jsonify


class SupplyHandler:

    def searchSupplierResources(self, sid):
        return jsonify(Supplies = "List of Resources Supplied by specific supplier")

    def searchResourceSupplier(self, rid):
        return jsonify(Supplies = "Search all suppliers of the given resource")

    def searchAllsupplies(self):
        return jsonify(Supplies = "All supplies")

    def searchSupplies(self, args):
        qty = args.get("qty")
        supply_date = args.get("supply_date")
        if (len(args) ==2) and qty and supply_date:
            return jsonify(Supplies = "Search Supplies for a given quantity and request date")
        elif (len(args) == 1) and supply_date:
            return jsonify(Supplies = "Search Supplies for the given request date")
        elif (len(args) == 1) and qty:
            return jsonify(Supplies = "Search Supplies with the given quantity")
        return jsonify(Supplies = "Bad Request"), 404

    def searchSuppliesbyRegion(self, region):
        return jsonify(Supplies = "Search all supplies in given region")

    def searchSuppliesSuppliers(self, args):
        city = args.get("city")
        if (len(args) ==1) and city:
            return jsonify(Supplies = "Search all supplies by suppliers in given city")