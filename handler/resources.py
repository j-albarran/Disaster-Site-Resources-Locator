from flask import Flask, jsonify

class ResourceHandler:
    def getAllResources(self):
        return jsonify(Resources = "All resources")

    def getResourceById(self, id):
        return jsonify(Resources = "Resource with id " + str(id))

    def searchResources(self, args):
        RName = args.get("RName")
        RCategory = args.get("RCategory")
        RQty = args.get("RQty")
        # resources_list = []
        if len(args) == 3 and RName and RCategory and RQty:
            resources_list = "RName and RCategory and RQty"
        elif len(args) == 2 and RName and RCategory:
            resources_list = "RName and RCategory"
        elif len(args) == 2 and RCategory and RQty:
            resources_list = "RCategory and RQty"
        elif len(args) == 2 and RName and RQty:
            resources_list = "RName and RQty"
        elif len(args) == 1 and RName:
            resources_list = "RName"
        elif len(args) == 1 and RCategory:
            resources_list = "RCategory"
        elif len(args) == 1 and RQty:
            resources_list = "RQty"
        else:
            return jsonify(Error = "Malformed query string"), 400
        return jsonify(Resources = resources_list)
