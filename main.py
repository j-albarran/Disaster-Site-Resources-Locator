from flask import Flask, jsonify, request

from handler.supplier import SupplierHandler
from handler.needer import NeederHandler
from handler.administrator import AdministratorHandler
from handler.person import PersonHandler
from handler.city import CityHandler

app = Flask(__name__)

#   WELCOME PAGE ROUTE
# =================================================

@app.route('/')
def greeting():
    return 'Welcome to Maria'

#   STATUSPR PAGE ROUTE
# =================================================

@app.route('/StatusPR')
def statusPR():
    return 'STATUS PR!'

#   SUPPLIERS ROUTES
# =================================================

@app.route('/StatusPR/suppliers')
def getSuppliers():
    # Listing all Suppliers
    if not request.args:
        return SupplierHandler().getAllSuppliers()
    # Searching specific suppliers (pname, plname, city)
    else:
        return SupplierHandler().searchSuppliers(request.args)

#   Looking for a supplier by ID
@app.route('/StatusPR/suppliers/<int:sid>')
def getSupplierById(sid):
    return SupplierHandler().getSupplierById(sid)


#   NEEDERS ROUTES
# =================================================

@app.route('/StatusPR/needers')
def getNeeders():
    # Listing all needers
    if not request.args:
        return NeederHandler().getAllNeeders()
    # Searching specific needers (pname, plname, city)
    else:
        return NeederHandler().searchNeeders(request.args)

# Looking for a needer by ID
@app.route('/StatusPR/needers/<int:nid>')
def getNeederById(nid):
    return NeederHandler().getNeederById(nid)


#   ADMINISTRATORS ROUTES
# =================================================

@app.route('/StatusPR/administrators')
def getAdministrators():
    # Listing all administrators
    if not request.args:
        return AdministratorHandler().getAllAdministrators()
    # Searching specific administrators
    else:
        return AdministratorHandler().searchAdmins(request.args)

# Looking for an administrator by ID
@app.route('/StatusPR/administrators/<int:aid>')
def getAdministratorById(aid):
    return AdministratorHandler().getAdministratorById(aid)


#   PERSONS ROUTES
# =================================================

# Looking for a person by ID
@app.route('/StatusPR/persons/<int:pid>')
def getPersonById(pid):
    return PersonHandler().getPersonByUniqueId(pid)

@app.route('/StatusPR/persons')
def getAllPeople():
    # Listing all persons
    if not request.args:
        return PersonHandler().getAllPersons()
    # Searching for specific persons
    else:
        return PersonHandler().searchPersons(request.args)


#   CITIES ROUTES
# =================================================
@app.route('/StatusPR/cities')
def getCities():
    # Listing all cities
    if not request.args:
        return CityHandler().getAllCities()
    # Searching for a specific city
    else:
        return CityHandler().searchCities(request.args)

# Looking or a specific city by name
@app.route('/StatusPR/cities/<string:cname>')
def getCityByName(cname):
    return CityHandler().getCitiesByName(cname)

# =================================================

if __name__ == '__main__':
    app.run()