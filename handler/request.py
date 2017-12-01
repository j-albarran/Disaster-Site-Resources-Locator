from flask import jsonify


class RequestHandler:
    def searchNeederResources(self, nid):
        return "prueba"

    def searchResourceNeeder(self, rid):
        return "prueba"

    def searchAllrequest(self):
        return "prueba"

    def searchRequests(self, args):
        qty = args.get("quantity")
        return "prueba"