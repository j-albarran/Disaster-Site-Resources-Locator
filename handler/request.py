from flask import jsonify


class RequestHandler:
    def searchNeederResources(self, nid):
        return "Search Resources need by needer"

    def searchResourceNeeder(self, rid):
        return "Search Needer for an specific resource"

    def searchAllrequest(self):
        return "All request of resources"

    def searchRequests(self, args):
        qty = args.get("qty")
        request_date = args.get("request_date")
        if len(args) ==2 and qty and request_date:
            return "Request of resources with given quantity and request date"
        elif len(args) == 1 and qty:
            return "Request of resources with given quantity"
        elif len(args) ==1 and request_date:
            return "request of resources on given date"
        return "Bad Request", 404

    def searchRequestsNeeders(self, args):
        city = args.get("city")
        if len(args) == 1 and city:
            return "Request of resources in given city"

    def searchRequestbyRegion(self, region):
        return "Request of resources in given region"
