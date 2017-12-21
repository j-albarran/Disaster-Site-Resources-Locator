from flask import jsonify

cities = [
    {
        'cname':'Ponce',
        'rname':'Sur'
    },
    {
        'cname' : 'Mayaguez',
        'rname' : 'Oeste'
    },
    {
        'cname' : 'Arecibo',
        'rname' : 'Norte'
    }
]

class CityHandler:

    def getAllCities(self):
        return jsonify(Cities=cities)

    def getCitiesByName(self, cname):
        result_list = []
        for city in cities:
            if city['cname'] == cname:
                result_list.append(city)
        if not result_list:
            return jsonify(Error = "City not found"), 404
        return jsonify(City = result_list)

    # Search cities by region
    def searchCities(self, args):

        cityRegion = args.get("rname")

        if (len(args) == 1):
            result_list = []
            for city in cities:
                if city['rname'] == cityRegion:
                    result_list.append(city)
            if not result_list:
                return jsonify(Error = 'No cities found'), 404
            return jsonify(Cities = result_list)
        else:
            return jsonify(Error = 'String malfunction'), 400