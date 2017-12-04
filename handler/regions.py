from flask import Flask, jsonify

class RegionHandler:
    def getAllRegions(self):
        return jsonify(Regions = "All regions")

    def getRegionByName(self, name):
        return jsonify(Regions = "Region with name " + name)
