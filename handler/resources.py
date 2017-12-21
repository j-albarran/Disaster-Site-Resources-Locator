from flask import Flask, jsonify

resources = [
    {
        'rid' : 1,
        'rqty' : 63,
        'rname' : 'tuna',
        'rcategory' : 'canned_food'
    },
    {
        'rid' : 2,
        'rqty' : 4,
        'rname' : 'shirt',
        'rcategory' : 'clothing'
    },
    {
        'rid' : 3,
        'rqty' : 1,
        'rname' : 'bag_of_ice',
        'rcategory' : 'ice'
    },
    {
        'rid' : 4,
        'rqty' : 15,
        'rname' : 'aa_batteries',
        'rcategory' : 'batteries'
    },
    {
        'rid' : 5,
        'rqty' : 9,
        'rname' : 'defibrillator',
        'rcategory' : 'medical_devices'
    }
]

requests = [
    {
        'nid' : 1,
        'rid' : 4,
        'qty' : 2,
        'request_date' : '08122017'
    },
    {
        'nid': 2,
        'rid': 3,
        'qty': 1,
        'request_date': '04102017'
    },
    {
        'nid': 3,
        'rid': 2,
        'qty': 5,
        'request_date': '02012016'
    }
]

class ResourceHandler:
    def getAllResources(self):
        return jsonify(Resources = resources)

    def getResourceById(self, id):
        for resource in resources:
            if resource['rid'] == id:
                return jsonify(Resource = resource)
        return jsonify(Error = "Not found!"), 404

    def searchResources(self, args):
        rname = args.get("rname")
        rcategory = args.get("rcategory")
        rqty = args.get("rqty")
        resources_list = []
        if len(args) == 3 and rname and rcategory and rqty:
            for resource in resources:
                if resource['rname'] == rname and resource['rcategory'] == rcategory and resource['rqty'] == int(rqty):
                    resources_list.append(resource)
        elif len(args) == 2 and rname and rcategory:
            for resource in resources:
                if resource['rname'] == rname and resource['rcategory'] == rcategory:
                    resources_list.append(resource)
        elif len(args) == 2 and rcategory and rqty:
            for resource in resources:
                if resource['rcategory'] == rcategory and resource['rqty'] == int(rqty):
                    resources_list.append(resource)
        elif len(args) == 2 and rname and rqty:
            for resource in resources:
                if resource['rname'] == rname and resource['rqty'] == int(rqty):
                    resources_list.append(resource)
        elif len(args) == 1 and rname:
            for resource in resources:
                if resource['rname'] == rname:
                    resources_list.append(resource)
        elif len(args) == 1 and rcategory:
            for resource in resources:
                if resource['rcategory'] == rcategory:
                    resources_list.append(resource)
        elif len(args) == 1 and rqty:
            for resource in resources:
                if resource['rqty'] == int(rqty):
                    resources_list.append(resource)
        else:
            return jsonify(Error = "Malformed query string"), 400
        if not resources_list:
            return jsonify(Error = "Not found!"), 404
        else:
            return jsonify(Resources = resources_list)

    def getResourcesAvailable(self):
        resources_list = []
        for resource in resources:
            if resource['rqty'] > 0:
                resources_list.append(resource)
        if not resources_list:
            return jsonify(Error="Not found!"), 404
        else:
            return jsonify(Available_Resources = resources_list)

    def searchResourcesAvailable(self, args):
        adate = args.get("adate")
        rname = args.get("rname")
        resources_list = []
        if len(args) == 2 and adate and rname:
            for resource in resources:
                if resource['adate'] == adate and resource['rname'] == rname:
                    resources_list.append(resource)
        elif len(args) == 1 and adate:
            for resource in resources:
                if resource['adate'] == adate:
                    resources_list.append(resource)
        elif len(args) == 1 and rname:
            for resource in resources:
                if resource['rname'] == rname:
                    resources_list.append(resource)
        else:
            return jsonify(Error = "Malformed query string"), 400
        if not resources_list:
            return jsonify(Error="Not found!"), 404
        else:
            return jsonify(Available_Resources = resources_list)

    def getResourcesNeeded(self):
        resource_list = []
        for resource in resources:
            for request in requests:
                if resource['rid'] == request['rid']:
                    resource_list.append(resource)
        if not resource_list:
            return jsonify(Error="Not found!"), 404
        else:
            return jsonify(Needed_Resources = resource_list)

    def searchResourcesNeeded(self, args):
        ndate = args.get("ndate")
        rname = args.get("rname")
        resources_list = []
        if len(args) == 2 and ndate and rname:
            for resource in resources:
                for request in requests:
                    if resource['ndate'] == ndate and resource['rname'] == rname and resource['rid'] == request['rid']:
                        resources_list.append(resource)
        elif len(args) == 1 and ndate:
            for resource in resources:
                for request in requests:
                    if resource['ndate'] == ndate and resource['rid'] == request['rid']:
                        resources_list.append(resource)
        elif len(args) == 1 and rname:
            for resource in resources:
                for request in requests:
                    if resource['rname'] == rname and resource['rid'] == request['rid']:
                        resources_list.append(resource)
        else:
            return jsonify(Error="Malformed query string"), 400
        if not resources_list:
            return jsonify(Error="Not found!"), 404
        else:
            return jsonify(Needed_Resources = resources_list)