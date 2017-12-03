from flask import Flask, jsonify, request
from handler.supply import SupplyHandler
from handler.transaction import TransactionHandler
from handler.request import RequestHandler
from handler.resources import ResourceHandler
from handler.categories import CategoryHandler
from handler.regions import RegionHandler
from handler.supplier import SupplierHandler
from handler.needer import NeederHandler
from handler.administrator import AdministratorHandler
from handler.person import PersonHandler
from handler.city import CityHandler

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Hello, this is the Disaster-Site-Resources-Locator project.'

# ---------------------------------------------------------------------------- #
#                              Resource routes                                 #
# ---------------------------------------------------------------------------- #

@app.route('/ResourceApp/resources')
def getAllResources():
    # Get all resources
    if not request.args:
        return ResourceHandler().getAllResources()
    # Get all resources by attributes (rname, rqty, rcategory)
    else:
        return ResourceHandler().searchResources(request.args)

# Get resource by ID
@app.route('/ResourceApp/resources/<int:id>')
def getResourceById(id):
    return ResourceHandler().getResourceById(id)

@app.route('/ResourceApp/resources/available')
def getResourcesAvailable():
    # Get all resources available now
    if not request.args:
        return ResourceHandler().getResourcesAvailable()
    # Get all resources available by attributes (adate, rname)
    # Get all resources at a given moment
    # Get all resources available in a region
    else:
        return ResourceHandler().searchResourcesAvailable(request.args)

# Get all resources needed now
@app.route('/ResourceApp/resources/needed')
def getResourcesNeeded():
    # Get all resources needed now
    if not request.args:
        return ResourceHandler().getResourcesNeeded()
    # Get all resources needed by attributes (ndate, rname)
    # Get all resources needed at a given moment
    # Get all resources needed in a regions
    else:
        return ResourceHandler.searchResourcesNeeded(request.args)

# ---------------------------------------------------------------------------- #
#                              Category routes                                 #
# ---------------------------------------------------------------------------- #

# Get all categories
@app.route('/ResourceApp/categories')
def getAllCategories():
    return CategoryHandler().getAllCategories()

# Get category by name
@app.route('/ResourceApp/categories/<string:name>')
def getCategoryByName(name):
    return CategoryHandler().getCategoryByName(name)

# ---------------------------------------------------------------------------- #
#                              Region routes                                   #
# ---------------------------------------------------------------------------- #

# Get all regions
@app.route('/ResourceApp/regions')
def getAllRegions():
    return RegionHandler().getAllRegions()

# Get region by name
@app.route('/ResourceApp/regions/<string:name>')
def getRegionByName(name):
    return RegionHandler().getRegionByName(name)


# ---------- Supply Related -------------

@app.route('/ResourceApp/supplier/<int:sid>/resources')
def getSupplierResources(sid):
    return SupplyHandler().searchSupplierResources(sid)

@app.route('/ResourceApp/resource/<int:rid>/suppliers')
def getResourceSuppliers(rid):
    return SupplyHandler().searchResourceSupplier(rid)

@app.route('/ResourceApp/supply')
def getSupplies():
    if not request.args:
        return SupplyHandler().searchAllsupplies()
    else:
        return SupplyHandler().searchSupplies(request.args) #qty and date



# ------------ Request Related --------------

@app.route('/ResourceApp/needer/<int:nid>/resources')
def getNeederResources(nid):
    return RequestHandler().searchNeederResources(nid)

@app.route('/ResourceApp/resource/<int:rid>/needer')
def getResourceNeeder(rid):
    return RequestHandler().searchResourceNeeder(rid)

@app.route('/ResourceApp/request')
def getRequests():
    if not request.args:
        return RequestHandler().searchAllrequest()
    else:
        return RequestHandler().searchRequests(request.args) #qty and date

# ------------- Transaction Related -------------

@app.route('/ResourceApp/transactions')
def getTransactions():
    if not request.args:
        return TransactionHandler().searchAlltransactions()
    else:
        return TransactionHandler().searchTransaction(request.args) #qty and date and price

@app.route('/ResourceApp/resource/<int:rid>/needer/supplier')
def getResourceTransactions(rid):
    if not request.args:
        return TransactionHandler().searchAllResourceTransactions(rid)
    else:
        return TransactionHandler().searchResourceTransactions(rid, request.args) #qty and date and price

@app.route('/ResourceApp/needer/<int:nid>/resource/supplier')
def getNeederTransactions(nid):
    return TransactionHandler().searchAllNeederTransactions(nid)

@app.route('/ResourceApp/supplier/<int:sid>/resource/needer')
def getSupplierTransactions(sid):
    return TransactionHandler().searchAllSupplierTransactions(sid)


#   STATUSPR PAGE ROUTE
# =================================================

@app.route('/ResourceApp')
def statusPR():
    return 'STATUS PR!'

#   SUPPLIERS ROUTES
# =================================================

@app.route('/ResourceApp/suppliers')
def getSuppliers():
    # Listing all Suppliers
    if not request.args:
        return SupplierHandler().getAllSuppliers()
    # Searching specific suppliers (pname, plname, city)
    else:
        return SupplierHandler().searchSuppliers(request.args)

#   Looking for a supplier by ID
@app.route('/ResourceApp/suppliers/<int:sid>')
def getSupplierById(sid):
    return SupplierHandler().getSupplierById(sid)


#   NEEDERS ROUTES
# =================================================

@app.route('/ResourceApp/needers')
def getNeeders():
    # Listing all needers
    if not request.args:
        return NeederHandler().getAllNeeders()
    # Searching specific needers (pname, plname, city)
    else:
        return NeederHandler().searchNeeders(request.args)

# Looking for a needer by ID
@app.route('/ResourceApp/needers/<int:nid>')
def getNeederById(nid):
    return NeederHandler().getNeederById(nid)


#   ADMINISTRATORS ROUTES
# =================================================

@app.route('/ResourceApp/administrators')
def getAdministrators():
    # Listing all administrators
    if not request.args:
        return AdministratorHandler().getAllAdministrators()
    # Searching specific administrators
    else:
        return AdministratorHandler().searchAdmins(request.args)

# Looking for an administrator by ID
@app.route('/ResourceApp/administrators/<int:aid>')
def getAdministratorById(aid):
    return AdministratorHandler().getAdministratorById(aid)


#   PERSONS ROUTES
# =================================================

# Looking for a person by ID
@app.route('/ResourceApp/persons/<int:pid>')
def getPersonById(pid):
    return PersonHandler().getPersonByUniqueId(pid)

@app.route('/ResourceApp/persons')
def getAllPeople():
    # Listing all persons
    if not request.args:
        return PersonHandler().getAllPersons()
    # Searching for specific persons
    else:
        return PersonHandler().searchPersons(request.args)


#   CITIES ROUTES
# =================================================
@app.route('/ResourceApp/cities')
def getCities():
    # Listing all cities
    if not request.args:
        return CityHandler().getAllCities()
    # Searching for a specific city
    else:
        return CityHandler().searchCities(request.args)

# Looking or a specific city by name
@app.route('/ResourceApp/cities/<string:cname>')
def getCityByName(cname):
    return CityHandler().getCitiesByName(cname)

if __name__ == '__main__':
    app.run()
