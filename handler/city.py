from flask import jsonify

class CityHandler:

    def getAllCities(self):
        return 'Viewing all cities'

    def getCitiesByName(self, cname):
        return 'Looking for a city by name: %s' % (cname)

    def searchCities(self, args):

        cityRegion = args.get("rname")

        if (len(args) == 1):
            return 'Looking for cities in region %s' %(cityRegion)
