from flask import jsonify

class AdministratorHandler:

    def getAllAdministrators(self):
        return 'Viewing all Administrators'

    def getAdministratorById(self, aid):
        return 'Looking for a admin by ID: %d' % (aid)

    def searchAdmins(self, args):

        firstName = args.get("pname")
        lastName = args.get('plname')
        city = args.get('city')

        if (len(args) == 3) and firstName and lastName and city:
            return 'Looking for administrators by PName, PLName and City'
        elif(len(args) == 2) and firstName and lastName:
            return 'Looking for administrators by PName and PLName'
        elif(len(args) == 2) and firstName and city:
            return 'Looking for administrators by PName and City'
        elif(len(args) == 2) and lastName and city:
            return 'Looking for administrators by PLName and City'
        elif (len(args) == 1) and firstName:
            return 'Looking for administrators by PName'
        elif (len(args) == 1) and lastName:
            return 'Looking for administrators by PLName'
        elif (len(args) == 1) and city:
            return 'Looking for administrators by City'
