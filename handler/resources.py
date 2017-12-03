from flask import Flask, jsonify

class ResourceHandler:
    def getAllResources(self):
        return jsonify(Resources = "All resources")

    def getResourceById(self, id):
        return jsonify(Resources = "Resource with id " + str(id))

    def searchResources(self, args):
        rname = args.get("rname")
        rcategory = args.get("rcategory")
        rqty = args.get("rqty")
        # resources_list = []
        if len(args) == 3 and rname and rcategory and rqty:
            resources_list = "rname and rcategory and rqty"
        elif len(args) == 2 and rname and rcategory:
            resources_list = "rname and rcategory"
        elif len(args) == 2 and rcategory and rqty:
            resources_list = "rcategory and rqty"
        elif len(args) == 2 and rname and rqty:
            resources_list = "rname and rqty"
        elif len(args) == 1 and rname:
            resources_list = "rname"
        elif len(args) == 1 and rcategory:
            resources_list = "rcategory"
        elif len(args) == 1 and rqty:
            resources_list = "rqty"
        else:
            return jsonify(Error = "Malformed query string"), 400
        return jsonify(Resources = resources_list)

    def getResourcesAvailable(self):
        return jsonify(Resources = "All resources available now")

    def searchResourcesAvailable(self, args):
        adate = args.get("adate")
        rname = args.get("rname")
        # resources_list = []
        if len(args) == 2 and adate and rname:
            resources_list = "adate and rname"
        elif len(args) == 1 and adate:
            resources_list = "adate"
        elif len(args) == 1 and rname:
            resources_list = "rname"
        else:
            return jsonify(Error = "Malformed query string"), 400
        return jsonify(Resources = resources_list)

    def getResourcesNeeded(self):
        return jsonify(Resources = "All resources needed now")

    def searchResourcesNeeded(self, args):
        ndate = args.get("ndate")
        rname = args.get("rname")
        # resources_list = []
        if len(args) == 2 and ndate and rname:
            resources_list = "ndate and rname"
        elif len(args) == 1 and ndate:
            resources_list = "ndate"
        elif len(args) == 1 and rname:
            resources_list = "rname"
        else:
            return jsonify(Error = "Malformed query string"), 400
        return jsonify(Resources = resources_list)
