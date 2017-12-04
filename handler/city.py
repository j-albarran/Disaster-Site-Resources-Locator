from flask import jsonify

class CityHandler:

    def getAllCities(self):
        return jsonify(Cities = 'Viewing all cities')

    def getCitiesByName(self, cname):
        return jsonify(Cities = 'Looking for a city by name: %s' % (cname))

    def searchCities(self, args):

        cityRegion = args.get("rname")

        if (len(args) == 1):
            return jsonify(Cities = 'Looking for cities in region %s' %(cityRegion))
