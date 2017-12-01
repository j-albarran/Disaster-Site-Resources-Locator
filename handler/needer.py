from flask import jsonify

class NeederHandler:

    def getAllNeeders(self):
        return 'Viewing all Needers'

    def getNeederById(self, nid):
        return 'Looking for a needer by ID: %d' % (nid)




