from flask import jsonify

class SupplierHandler:

    def getAllSuppliers(self):
        return 'Viewing all suppliers'

    def getSupplierById(self, sid):
        return 'Looking for a supplier by ID: %d' % (sid)

    def searchSuppliers(self, args):

        firstName = args.get("pname")
        lastName = args.get('plname')
        city = args.get('city')

        if (len(args) == 3) and firstName and lastName and city:
            return 'Looking for suppliers by PName, PLName and City'
        elif(len(args) == 2) and firstName and lastName:
            return 'Looking for suppliers by PName and PLName'
        elif(len(args) == 2) and firstName and city:
            return 'Looking for suppliers by PName and City'
        elif(len(args) == 2) and lastName and city:
            return 'Looking for suppliers by PLName and City'
        elif (len(args) == 1) and firstName:
            return 'Looking for suppliers by PName'
        elif (len(args) == 1) and lastName:
            return 'Looking for suppliers by PLName'
        elif (len(args) == 1) and city:
            return 'Looking for suppliers by City'
        