from flask import jsonify

class AdministratorHandler:

    def getAllAdministrators(self):
        return 'Viewing all Administrators'

    def getAdministratorById(self, aid):
        return 'Looking for a admin by ID: %d' % (aid)

