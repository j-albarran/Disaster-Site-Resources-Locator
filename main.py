from flask import Flask, jsonify, request
from handler.supplier import SupplierHandler
from handler.needer import NeederHandler
from handler.administrator import AdministratorHandler
from handler.person import PersonHandler

app = Flask(__name__)

@app.route('/')
def greeting():
    return 'Welcome to Maria'

@app.route('/StatusPR/suppliers')
def getSuppliers():
    return SupplierHandler().getAllSuppliers()

@app.route('/StatusPR/suppliers/<int:sid>')
def getSupplierById(sid):
    return SupplierHandler().getSupplierById(sid)

@app.route('/StatusPR/needers')
def getNeeders():
    return NeederHandler().getAllNeeders()

@app.route('/StatusPR/needers/<int:nid>')
def getNeederById(nid):
    return NeederHandler().getNeederById(nid)

@app.route('/StatusPR/administrators')
def getAdministrators():
    return AdministratorHandler().getAllAdministrators()

@app.route('/StatusPR/administrators/<int:aid>')
def getAdministratorById(aid):
    return AdministratorHandler().getAdministratorById(aid)

@app.route('/StatusPR/persons/<int:pid>')
def getPersonById(pid):
    return PersonHandler().getPersonByUniqueId(pid)

@app.route('/StatusPR/persons')
def getAllPeople():
    if not request.args:
        return PersonHandler().getAllPersons()
    else:
        return PersonHandler().searchPersons(request.args)

if __name__ == '__main__':
    app.run()