from flask import jsonify


class RequestHandler:
    def searchNeederResources(self, nid):
        return jsonify(Requests = "Search Resources need by needer")

    def searchResourceNeeder(self, rid):
        return jsonify(Requests = "Search Needer for an specific resource")

    def searchAllrequest(self):
        return jsonify(Requests = "All request of resources")

    def searchRequests(self, args):
        qty = args.get("qty")
        request_date = args.get("request_date")
        if len(args) ==2 and qty and request_date:
            return jsonify(Requests = "Request of resources with given quantity and request date")
        elif len(args) == 1 and qty:
            return jsonify(Requests = "Request of resources with given quantity")
        elif len(args) ==1 and request_date:
            return jsonify(Requests = "request of resources on given date")
        return jsonify(Requests = "Bad Request"), 400

    def searchRequestsNeeders(self, args):
        city = args.get("city")
        if len(args) == 1 and city:
            return jsonify(Requests = "Request of resources in given city")
        return jsonify(Requests = "Bad request"), 400

    def searchRequestbyRegion(self, region):
        return jsonify(Requests = "Request of resources in given region")
