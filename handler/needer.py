from flask import jsonify

class NeederHandler:

    def getAllNeeders(self):
        return 'Viewing all Needers'

    def getNeederById(self, nid):
        return 'Looking for a needer by ID: %d' % (nid)

    def searchNeeders(self, args):

        firstName = args.get("pname")
        lastName = args.get('plname')
        city = args.get('city')

        if (len(args) == 3) and firstName and lastName and city:
            return 'Looking for needers by PName, PLName and City'
        elif(len(args) == 2) and firstName and lastName:
            return 'Looking for needers by PName and PLName'
        elif(len(args) == 2) and firstName and city:
            return 'Looking for needers by PName and City'
        elif(len(args) == 2) and lastName and city:
            return 'Looking for needers by PLName and City'
        elif (len(args) == 1) and firstName:
            return 'Looking for needers by PName'
        elif (len(args) == 1) and lastName:
            return 'Looking for needers by PLName'
        elif (len(args) == 1) and city:
            return 'Looking for needers by City'


