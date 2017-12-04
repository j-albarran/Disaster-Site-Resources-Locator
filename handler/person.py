from flask import jsonify

class PersonHandler:

    def getAllPersons(self):
        return 'Viewing all Persons registered'

    def getPersonByUniqueId(self, pid):
       return 'Looking for a person by ID: %d' %(pid)

    def searchPersons(self, args):

        firstName = args.get("pname")
        lastName = args.get('plname')
        city = args.get('city')

        if (len(args) == 3) and firstName and lastName and city:
            return 'Looking for a Person by PName, PLName and City'
        elif(len(args) == 2) and firstName and lastName:
            return 'Looking for Persons by PName and PLName'
        elif(len(args) == 2) and firstName and city:
            return 'Looking for Persons by PName and City'
        elif(len(args) == 2) and lastName and city:
            return 'Looking for Persons by PLName and City'
        elif (len(args) == 1) and firstName:
            return 'Looking for Persons by PName'
        elif (len(args) == 1) and lastName:
            return 'Looking for Persons by PLName'
        elif (len(args) == 1) and city:
            return 'Looking for Persons by City'


