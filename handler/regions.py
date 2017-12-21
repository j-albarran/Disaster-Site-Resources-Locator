from flask import Flask, jsonify

regions = [
    {
        'rname' : 'bayamon'
    },
    {
        'rname': 'mayaguez'
    },
    {
        'rname': 'ponce'
    },
    {
        'rname': 'san_juan'
    },
    {
        'rname': 'arecibo'
    },
    {
        'rname': 'carolina'
    },
    {
        'rname': 'caguas'
    }
]

class RegionHandler:
    def getAllRegions(self):
        region_list = []
        for region in regions:
            region_list.append(region)
        if not region_list:
            return jsonify(Error="Not found!"), 404
        else:
            return jsonify(Regions = region_list)

    def getRegionByName(self, name):
        result = None
        for region in regions:
            if region['rname'] == name:
                result = region
        if not result:
            return jsonify(Error="Not found!"), 404
        else:
            return jsonify(Region = result)