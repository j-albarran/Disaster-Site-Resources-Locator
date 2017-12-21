from flask import jsonify


class RequestHandler:
    def __init__(self):
        self.request = [{'city': 'San Juan',
                        'nid': '1',
                        'qty': '2',
                        'region': 'San Juan',
                        'rid': '7',
                        'request_date': '12-13-2017'},
                       {'city': 'Mayaguez ',
                        'nid': '2',
                        'qty': '3',
                        'region': 'Mayaguez',
                        'rid': '6',
                        'request_date': '12-14-2017'},
                       {'city': 'Ponce',
                        'nid': '3',
                        'qty': '4',
                        'region': 'Ponce',
                        'rid': '5',
                        'request_date': '12-15-2017'},
                       {'city': 'Bayamon',
                        'nid': '4',
                        'qty': '5',
                        'region': 'San Juan',
                        'rid': '4',
                        'request_date': '12-16-2017'},
                       {'city': 'San Juan',
                        'nid': '1',
                        'qty': '6',
                        'region': 'San Juan',
                        'rid': '3',
                        'request_date': '12-13-2017'},
                       {'city': 'Mayaguez ',
                        'nid': '2',
                        'qty': '7',
                        'region': 'Mayaguez',
                        'rid': '2',
                        'request_date': '12-14-2017'},
                       {'city': 'Ponce',
                        'nid': '3',
                        'qty': '6',
                        'region': 'Ponce',
                        'rid': '1',
                        'request_date': '12-15-2017'},
                       {'city': 'Bayamon',
                        'nid': '4',
                        'qty': '5',
                        'region': 'San Juan',
                        'rid': '5',
                        'request_date': '12-16-2017'},
                       {'city': 'San Juan',
                        'nid': '12',
                        'qty': '4',
                        'region': 'San Juan',
                        'rid': '4',
                        'request_date': '12-13-2017'},
                       {'city': 'Mayaguez ',
                        'nid': '2',
                        'qty': '3',
                        'region': 'Mayaguez',
                        'rid': '3',
                        'request_date': '12-14-2017'},
                       {'city': 'Ponce',
                        'nid': '3',
                        'qty': '2',
                        'region': 'Ponce',
                        'rid': '2',
                        'request_date': '12-15-2017'},
                       {'city': 'Bayamon',
                        'nid': '4',
                        'qty': '1',
                        'region': 'San Juan',
                        'rid': '1',
                        'request_date': '12-16-2017'}]

    def searchNeederResources(self, nid):
        result = []
        for row in self.request:
            if int(row['nid']) == int(nid):
                result.append(row)
        if not result:
            return jsonify(Error="No items found"), 404
        return jsonify(Supply=result)

    def searchResourceNeeder(self, rid):
        result = []
        for row in self.request:
            if int(row['rid']) == int(rid):
                result.append(row)
        if not result:
            return jsonify(Error="No items found"), 404
        return jsonify(Request=result)

    def searchAllrequest(self):
        return jsonify(Request=self.request)

    def searchRequests(self, args):
        qty = args.get("qty")
        request_date = args.get("request_date")
        if len(args) ==2 and qty and request_date:
            result = []
            for row in self.request:
                if int(row['qty']) == int(qty) and row['request_date'] == request_date:
                    result.append(row)
            if not result:
                return jsonify(Error="No items found"), 404
            return jsonify(Request=result)
        elif len(args) == 1 and qty:
            result = []
            for row in self.request:
                if int(row['qty']) == int(qty):
                    result.append(row)
            if not result:
                return jsonify(Error="No items found"), 404
            return jsonify(Request=result)
        elif len(args) ==1 and request_date:
            result = []
            for row in self.request:
                if row['request_date'] == request_date:
                    result.append(row)
            if not result:
                return jsonify(Error="No items found"), 404
            return jsonify(Request=result)
        return jsonify(Requests = "Bad Request"), 400

    def searchRequestsNeeders(self, args):
        city = args.get("city")
        if len(args) == 1 and city:
            result = []
            for row in self.request:
                if row['city'] == city:
                    result.append(row)
            if not result:
                return jsonify(Error="No items found"), 404
            return jsonify(Request=result)
        return jsonify(Requests = "Bad request"), 400

    def searchRequestbyRegion(self, region):
        result = []
        for row in self.request:
            if row['region'] == region:
                result.append(row)
        if not result:
            return jsonify(Error="No items found"), 404
        return jsonify(Request=result)
