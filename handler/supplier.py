from flask import jsonify

class SupplierHandler:

    def getAllSuppliers(self):
        return 'Viewing all suppliers'

    def getSupplierById(self, sid):
        return 'Looking for a supplier by ID: %d' % (sid)


