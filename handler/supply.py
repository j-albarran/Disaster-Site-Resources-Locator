from flask import jsonify


class SupplyHandler:

    def searchSupplierResources(self, sid):
        return "List of Resources Supplied by specific supplier"

    def searchResourceSupplier(self, rid):
        return "Search all suppliers of the given resource"

    def searchAllsupplies(self):
        return "All supplies"

    def searchSupplies(self, args):
        qty = args.get("quantity")
        request_date = args.get("request_date")
        if (len(args) ==2) and qty and request_date:
            return "Search Supplies for a given quantity and request date"
        elif (len(args) == 1) and request_date:
            return "Search Supplies for the given request date"
        elif (len(args) == 1) and qty:
            return "Search Supplies with the given quantity"
        return "all supplies"