from flask import Flask, jsonify, request

from handler.city import CityHandler
from handler.address import AddressHandler
from handler.account import AccountHandler
from handler.administrator import AdministratorHandler
from handler.bank_account import BankAccountHandler
from handler.credentials import CredentialsHandler
from handler.region import RegionHandler
from handler.requester import RequesterHandler
from handler.supplier import SupplierHandler


app = Flask(__name__)

@app.route('/')
def welcome():
    return jsonify(Welcome = 'Hello, this is the Disaster-Site-Resources-Locator project.')

# ------------------------------------------------------------------------------- #
#                                  City routes                                    #
# ------------------------------------------------------------------------------- #
@app.route('/ResourceApp/cities', methods = ['GET', 'POST'])
def handleCities():
    if request.method == 'POST':
        return CityHandler().addNewCity(request.form)
    else:
        if not request.args:
            return CityHandler().getAllCities()                                     #
        else:
            return CityHandler().searchCities(request.args)                         #

@app.route('/ResourceApp/cities/<string:cname>', methods = ['GET', 'PUT', 'DELETE'])
def handleCity(cname):
    if request.method == 'GET':
        return CityHandler().getCityByName(cname)                                     #
    elif request.method == 'PUT':
        return CityHandler().updateCity(cname, request.form)
    elif request.method == 'DELETE':
        return CityHandler().deleteCity(cname)
    else:
        return jsonify(Error = 'Method not supported'), 405

@app.route('/ResourceApp/regions/<string:rname>/cities')
def getCitiesOnRegion(rname):
        return CityHandler().getCitiesOnThisRegion(rname)

@app.route('/ResourceApp/accounts/<int:aid>/cities')
def getAccountCity(aid):
        return CityHandler().getAccountCity(aid)

@app.route('/ResourceApp/requesters/<int:rid>/cities')
def getRequesterCity(rid):
        return CityHandler().getRequesterCity(rid)

@app.route('/ResourceApp/administrators/<int:adminId>/cities')
def getAdministratorCity(adminId):
        return CityHandler().getAdministorCity(adminId)

@app.route('/ResourceApp/suppliers/<int:sid>/cities')
def getSupplierCity(sid):
        return CityHandler().getSupplierCity(sid)

@app.route('/ResourceApp/addresses/<int:addId>/cities')
def getCityOfThisAddress(addId):
        return CityHandler().getCityOfThisAddress(addId)

# ---------------------------------------------------------------------------- #
#                               Region routes                                  #
# ---------------------------------------------------------------------------- #
@app.route('/ResourceApp/regions', methods = ['GET', 'POST'])
def handleRegions():
    if request.method == 'POST':
        return RegionHandler().addNewRegion(request.form)
    else:
        if not request.args:
            return RegionHandler().getAllRegions()
        else:
            return RegionHandler().searchRegions(request.args)

@app.route('/ResourceApp/regions/<string:rname>', methods = ['GET', 'PUT', 'DELETE'])
def handleRegion(rname):
    if request.method == 'GET':
        return RegionHandler().getRegionByName(rname)
    elif request.method == 'PUT':
        return RegionHandler().updateRegion(rname, request.form)
    elif request.method == 'DELETE':
        return RegionHandler().deleteRegion(rname)
    else:
        return jsonify(Error = 'Method not supported'), 405

@app.route('/ResourceApp/cities/<string:cname>/regions')
def getCityRegion(cname):
    return RegionHandler().getCityRegion(cname)

@app.route('/ResourceApp/accounts/<int:aid>/regions')
def getAccountRegion(aid):
        return RegionHandler().getAccountRegion(aid)

@app.route('/ResourceApp/administrators/<int:adminId>/regions')
def getAdministratorRegion(adminId):
        return RegionHandler().getAdministorRegion(adminId)

@app.route('/ResourceApp/requesters/<int:rid>/regions')
def getRequesterRegion(rid):
        return RegionHandler().getRequesterRegion(rid)

@app.route('/ResourceApp/suppliers/<int:sid>/regions')
def getSupplierRegion(sid):
        return RegionHandler().getSupplierCity(sid)

@app.route('/ResourceApp/addresses/<int:addId>/regions')
def getRegionOfThisAddress(addId):
        return RegionHandler().getRegionOfThisAddress(addId)

# ---------------------------------------------------------------------------- #
#                               Address routes                                 #
# ---------------------------------------------------------------------------- #
@app.route('/ResourceApp/addresses', methods = ['GET', 'POST'])
def getAllAddresses():
    if request.method == 'POST':
        return AddressHandler().addNewAddress(request.form)
    else:
        if not request.args:
            return AddressHandler().getAllAddresses()
        else:
            # By street, number, unit, zip_code
            return AddressHandler().searchAddresses(request.args)

@app.route('/ResourceApp/addresses/<int:addId>', methods = ['GET', 'PUT', 'DELETE'])
def getAddressById(addId):
    if request.method == 'GET':
        return AddressHandler().getAddressById(addId)
    elif request.method == 'PUT':
        return AddressHandler().updateAddress(addId, request.form)
    elif request.method == 'DELETE':
        return AddressHandler().deleteAddress(addId)
    else:
        return jsonify(Error = 'Method not allowed'), 405


@app.route('/ResourceApp/cities/<string:cname>/addresses')
def getAddressesOnThidCity(cname):
    if not request.args:
        return AddressHandler().getAddressesOnThisCity(cname)                          #
    else:
        # By street, number, unit, zip_code
        return AddressHandler().searchAddressesOnThisCity(cname, request.args)         #

@app.route('/ResourceApp/regions/<string:rname>/addresses')
def getAddressesOnThisRegion(rname):
    if not request.args:
        return AddressHandler().getAddressesOnThisRegion(rname)
        # By street, number, unit, zip_code
    else:
        return AddressHandler().searchAddressesOnThisRegion(rname, request.args)

@app.route('/ResourceApp/suppliers/<int:sid>/addresses')
def getSupplierAddress(sid):
    if not request.args:
        return AddressHandler().getSupplierAddress(sid)
    else:
        # By street, number, unit, zip_code
        return AddressHandler().searchSupplierAddress(sid, request.args)

@app.route('/ResourceApp/requester/<int:rid>/addresses')
def getRequesterAddress(rid):
    if not request.args:
        return AddressHandler().getRequesterAddress(rid)
    else:
        # By street, number, unit, zip_code
        return AddressHandler().searchRequesterAddress(rid, request.args)

@app.route('/ResourceApp/accounts/<int:aid>/addresses')
def getAccountAddress(aid):
    if not request.args:
        return AddressHandler().getAccountAddress(aid)
    else:
        # By street, number, unit, zip_code
        return AddressHandler().searchAccountAddress(aid, request.args)

@app.route('/ResourceApp/administrators/<int:adminId>/addresses')
def getAdministratorAddress(adminId):
    if not request.args:
        return AddressHandler().getAccountAddress(adminId)
    else:
        # By street, number, unit, zip_code
        return AddressHandler().searchAccountAddress(adminId, request.args)


@app.route('/ResourceApp/credit_cards/<int:cid>/addresses')
def getCreditCardAddress(cid):
    if not request.args:
        return AddressHandler().getCreditCardAddress(cid)
    # By street, number, unit, zip_code, cname
    else:
        return AddressHandler().searchCreditCardAddress(cid, request.args)

# ---------------------------------------------------------------------------- #
#                               Account routes                                 #
# ---------------------------------------------------------------------------- #

@app.route('/ResourceApp/accounts', methods = ['GET', 'POST'])
def getAllAccounts():
    if request.method == 'POST':
        return AccountHandler().addNewAccount(request.form)
    else:
        if not request.args:
            return AccountHandler().getAllAccounts()
        else:
            # Searching by afirst, alast, email, phone
            return AccountHandler().searchAccounts(request.args)

@app.route('/ResourceApp/accounts/<int:aid>', methods = ['GET', 'PUT', 'DELETE'])
def getAccountById(aid):
    if request.method == 'GET':
        return AccountHandler().getAccountById(aid)
    elif request.method == 'PUT':
        return AccountHandler().updateAccount(aid, request.form)
    elif request.method == 'DELETE':
        return AccountHandler().deleteAccount(aid)
    else:
        return jsonify(Error = 'Method not allowed'), 405

@app.route('/ResourceApp/cities/<string:cname>/accounts')
def getAccountsOnCity(cname):
    if not request.args:
        return AccountHandler().getAccountsOnThisCity(cname)
        # Sarching by afirst, alast, username, email, phone
    else:
        return AccountHandler().searchAccountsOnThisCity(cname, request.args)

@app.route('/ResourceApp/regions/<string:rname>/accounts')
def getAccountsOnRegion(rname):
    if not request.args:
        return AccountHandler().getAccountsOnThisRegion(rname)
        # Sarching by afirst, alast, username, email, phone
    else:
        return AccountHandler().searchAccountsOnThisRegion(rname, request.args)

@app.route('/ResourceApp/addresses/<int:addId>/accounts')
def getAccountsWithAddressID(addId):
    if not request.args:
        return AccountHandler().getAccountsOnThisAddressID(addId)
        # Searching by afirst, alast, email, phone
    else:
        return AccountHandler().searchAccountsOnThisAddressID(addId, request.args)

@app.route('/ResourceApp/credentials/<string:username>/account')
def getAccountWithThisUsername(username):
    if not request.args:
        return AccountHandler().getAccountWithThisUsername(username)
    else:
        return AccountHandler().searchAccountWithThisUsername(username, request.args)

# ---------------------------------------------------------------------------- #
#                            Administrator routes                              #
# ---------------------------------------------------------------------------- #

@app.route('/ResourceApp/administrators', methods = ['GET', 'POST'])
def getAllAdministrators():
    if request.method == 'POST':
        return AdministratorHandler().addNewAdministrator(request.form)
    else:
        if not request.args:
            return AdministratorHandler().getAllAdministrators()
        else:
            # Sarching by afirst, alast, username, email, phone
            return AdministratorHandler().searchAdministrators(request.args)

@app.route('/ResourceApp/administrators/<int:adminId>', methods = ['GET', 'PUT', 'DELETE'])
def getAdministratorById(adminId):
    if request.method == 'GET':
        return AdministratorHandler().getAdministratorById(adminId)
    elif request.method == 'PUT':
        return AdministratorHandler().updateAdministrator(adminId, request.form)
    elif request.method == 'DELETE':
        return AdministratorHandler().deleteAdministrator(adminId)
    else:
        return jsonify(Error = 'Method not allowed'), 405

@app.route('/ResourceApp/cities/<string:cname>/administrators')
def getAdministratorsOnThisCity(cname):
    if not request.args:
        return AdministratorHandler().getAdministratorsOnThisCity(cname)
    # Searching by afirst, alast, email, phone
    else:
        return AdministratorHandler().searchAdministratorsOnThisCity(cname, request.args)

@app.route('/ResourceApp/regions/<string:rname>/administrators')
def getAdministratorsOnThisRegion(rname):
    if not request.args:
        return AdministratorHandler().getAdministratorsOnThisRegion(rname)
    # Searching by afirst, alast, username, email, phone
    else:
        return AdministratorHandler().searchAdministratorsOnThisRegion(request.args, rname)

@app.route('/ResourceApp/addresses/<int:addId>/administrators')
def getAdministratorsOnThisAddressID(addId):
    if not request.args:
        return AdministratorHandler().getAdministratorsOnThisAddressID(addId)
    # Searching by afirst, alast, username, email, phone
    else:
        return AdministratorHandler().searchAdministratorsOnThisAddressID(addId, request.args)

# ---------------------------------------------------------------------------- #
#                              Supplier routes                                 #
# ---------------------------------------------------------------------------- #
@app.route('/ResourceApp/suppliers', methods = ['GET', 'POST'])
def searchSuppliers():
    if request.method == 'POST':
        return SupplierHandler().addNewSupplier(request.form)
    else:
        if not request.args:
            return SupplierHandler().getAllSuppliers()
        else:
            # Searching by afirst, alast, email, phone
            return SupplierHandler().searchSuppliers(request.args)

@app.route('/ResourceApp/suppliers/<int:sid>', methods = ['GET', 'PUT', 'DELETE'])
def getSupplierById(sid):
    if request.method == 'GET':
        return SupplierHandler().getSupplierById(sid)
    elif request.method == 'PUT':
        return SupplierHandler().updateSupplier(sid, request.form)
    elif request.method == 'DELETE':
        return SupplierHandler().deleteSupplier(sid)
    else:
        return jsonify(Error = 'Method not allowed'), 405

@app.route('/ResourceApp/cities/<string:cname>/suppliers')
def getSuppliersOnThisCity(cname):
    if not request.args:
        return SupplierHandler().getSuppliersOnThisCity(cname)
    # Searching by afirst, alast, email, phone
    else:
        return SupplierHandler().searchSuppliersOnThisCity(cname, request.args)

@app.route('/ResourceApp/regions/<string:rname>/suppliers')
def getSuppliersOnThisRegion(rname):
    if not request.args:
        return SupplierHandler().getSuppliersOnThisRegion(rname)
    # Searching by afirst, alast, email, phone
    else:
        return SupplierHandler().searchSuppliersOnThisRegion(request.args, rname)

@app.route('/ResourceApp/addresses/<int:addId>/suppliers')
def getSuppliersOnThisAddressID(addId):
    if not request.args:
        return SupplierHandler().getSuppliersOnThisAddressID(addId)
    # Searching by afirst, alast, username, email, phone
    else:
        return SupplierHandler().searchSuppliersOnThisAddressID(addId, request.args)

@app.route('/ResourceApp/bank_accounts/<int:bid>/suppliers')
def getSupplierOfThisBankAccount(bid):
    if not request.args:
        return SupplierHandler().getSupplierOfThisBankAccount(bid)
    else:
        return SupplierHandler().searchSupplierOfThisBankAccount(bid, request.args)

@app.route('/ResourceApp/resources/<int:rsid>/suppliers')
def getSuppliersOfThisResource(rsid):
    if not request.args:
        return SupplierHandler().getSuppliersOfThisResource(rsid)
    else:
        return SupplierHandler().searchSuppliersOfThisResource(rsid, request.args)

@app.route('/ResourceApp/cities/<string:cname>/resources/<int:rsid>/suppliers')
def getSuppliersOfThisResourceOnThisCity(cname, rsid):
    if not request.args:
        return SupplierHandler().getSupplierOfThisResourceOnThisCity(cname, rsid)
    else:
        return SupplierHandler().searchSupplierOfThisResourceOnThisCity(cname, rsid, request.args)

@app.route('/ResourceApp/regions/<string:rname>/resources/<int:rsid>/suppliers')
def getSuppliersOfThisResourceOnThisRegion(rname, rsid):
    if not request.args:
        return SupplierHandler().getSupplierOfThisResourceOnThisRegion(rname, rsid)
    else:
        return SupplierHandler().searchSupplierOfThisResourceOnThisRegion(rname, rsid, request.args)

@app.route('/ResourceApp/categories/<string:cat_name>/suppliers')
def getSuppliersOfThisCategory(cat_name):
    if not request.args:
        return SupplierHandler().getSuppliersOfThisCategory(cat_name)
    else:
        return SupplierHandler().searchSuppliersOfThisCategory(cat_name, request.args)

@app.route('/ResourceApp/transactions/<int:tid>/suppliers')
def getSupplierOfThisTransaction(tid):
    if not request.args:
        return SupplierHandler().getSupplierOfThisTransaction(tid)
    else:
        return SupplierHandler().searchSupplierOfThisTransaction(tid, request.args)

@app.route('/ResourceApp/orders_info/<int:oid>/suppliers')
def getSuppliersOfThisOrder(oid):
    if not request.args:
        return SupplierHandler().getSuppliersOfThisOrderInfo(oid)
    else:
        return SupplierHandler().searchSuppliersOfThisOrderInfo(oid)

# ---------------------------------------------------------------------------- #
#                             Requester routes                                 #
# ---------------------------------------------------------------------------- #

@app.route('/ResourceApp/requesters', methods = ['GET', 'POST'])
def searchRequesters():
    if request.method == 'POST':
        return RequesterHandler().addNewRequester(request.form)
    else:
        if not request.args:
            return RequesterHandler().getAllRequesters()
        else:
            # Searching by afirst, alast, username, email, phone
            return RequesterHandler().searchRequesters(request.args)

@app.route('/ResourceApp/requesters/<int:rid>', methods = ['GET', 'PUT', 'DELETE'])
def getRequesterById(rid):
    if request.method == 'GET':
        return RequesterHandler().getRequesterById(rid)
    elif request.method == 'PUT':
        return RequesterHandler().updateRequester(rid, request.form)
    elif request.method == 'DELETE':
        return RequesterHandler().deleteRequester(rid)
    else:
        return jsonify(Error = 'Method not allowed'), 405

@app.route('/ResourceApp/cities/<string:cname>/requesters')
def getRequestersOnThisCity(cname):
    if not request.args:
        return RequesterHandler().getRequestersOnThisCity(cname)
    # Searching by afirst, alast, username, email, phone
    else:
        return RequesterHandler().searchRequestersOnThisCity(cname, request.args)

@app.route('/ResourceApp/regions/<string:rname>/requesters')
def getRequestersOnThisRegion(rname):
    if not request.args:
        return RequesterHandler().getRequestersOnThisRegion(rname)
    # Searching by afirst, alast, username, email, phone
    else:
        return RequesterHandler().searchRequestersOnThisRegion(request.args, rname)

@app.route('/ResourceApp/addresses/<int:addId>/requesters')
def getRequestersOnThisAddressID(addId):
    if not request.args:
        return RequesterHandler().getRequestersOnThisAddressID(addId)
    # Searching by afirst, alast, username, email, phone
    else:
        return RequesterHandler().searchRequestersOnThisAddressID(addId, request.args)

@app.route('/ResourceApp/resources/<int:rsid>/requesters')
def getRequestersOfThisResource(rsid):
    if not request.args:
        return RequesterHandler().getRequestersOfThisResource(rsid)
    else:
        return RequesterHandler().searchRequestersOfThisResource(rsid, request.args)

@app.route('/ResourceApp/resources_requested/<int:rrid>/requesters')
def getRequestersOfThisResourceRequested(rrid):
    if not request.args:
        return RequesterHandler().getRequestersOfThisResourceRequested(rrid)
    else:
        return RequesterHandler().searchRequestersOfThisResourceRequested(rrid, request.args)

@app.route('/ResourceApp/categories/<string:cat_name>/requesters')
def getRequestersOfThisCategory(cat_name):
    if not request.args:
        return RequesterHandler().getRequestersOfThisCategory(cat_name)
    else:
        return RequesterHandler().searchRequestersOfThisCategory(cat_name, request.args)

@app.route('/ResourceApp/transactions/<int:tid>/requesters')
def getRequesterOfThisTransaction(tid):
    if not request.args:
        return RequesterHandler().getRequestersOfThisTransaction(tid)
    else:
        return RequesterHandler().searchRequestersOfThisTransaction(tid, request.args)

@app.route('/ResourceApp/credit_cards/<int:cid>/requesters')
def getRequestersWithThisCreditCard(cid):
    if not request.args:
        return RequesterHandler().getRequestersOfThisCreditCard(cid)
    else:
        return RequesterHandler().searchRequestersOfThisCreditCard(cid, request.args)

@app.route('/ResourceApp/payments/<int:payid>/requesters')
def getRequesterOfThisPayment(payid):
    if not request.args:
        return RequesterHandler().getRequestersOfThisPayment(payid)
    else:
        return RequesterHandler().searchRequestersOfThisPayment(payid, request.args)

@app.route('/ResourceApp/orders_info/<int:oid>/requesters')
def getRequesterOfThisOrder(oid):
    if not request.args:
        return RequesterHandler().getRequestersOfThisOrderInfo(oid)
    else:
        return RequesterHandler().searchRequestersOfThisOrderInfo(oid, request.args)

# ---------------------------------------------------------------------------- #
#                              Bank Account routes                             #
# ---------------------------------------------------------------------------- #
@app.route('/ResourceApp/bank_accounts', methods = ['GET', 'POST'])
def searchBankAccounts():
    if request.method == 'POST':
        return BankAccountHandler().addNewBankAccount(request.form)
    else:
        if not request.args:
            return BankAccountHandler().getAllBankAccounts()
        else:
            # Sarching by routing, accountNumber, accountOwner
            return BankAccountHandler().searchBankAccounts(request.args)

@app.route('/ResourceApp/bank_accounts/<int:bid>', methods = ['GET', 'PUT', 'DELETE'])
def getBankAccountById(bid):
    if request.method == 'GET':
        return BankAccountHandler().getBankAccountById(bid)
    elif request.method == 'PUT':
        return BankAccountHandler().updateBankAccount(bid, request.form)
    elif request.method == 'DELETE':
        return BankAccountHandler().deleteBankAccount(bid)
    else:
        return jsonify(Error = 'Method not supported'), 405

@app.route('/ResourceApp/suppliers/<int:sid>/bank_accounts')
def getBankAccountOfThisSupplier(sid):
    if not request.args:
        return BankAccountHandler().getBankAccountOfThisSupplier(sid)
    else:
        return BankAccountHandler().searchBankAccountOfThisSupplier(sid, request.args)

@app.route('/ResourceApp/transactions/<int:tid>/bank_accounts')
def getBankAccountOfThisTransaction(tid):
    if not request.args:
        return BankAccountHandler().getBankAccountOfThisTransaction(tid)
    else:
        return BankAccountHandler().searchBankAccountOfThisTransaction(tid, request.args)

# ---------------------------------------------------------------------------- #
#                              Credentials                                     #
# ---------------------------------------------------------------------------- #
@app.route('/ResourceApp/credentials', methods = ['GET', 'POST'])
def searchCredentials():
    if request.method == 'POST':
        return CredentialsHandler().addCredentials(request.form)
    else:
        if not request.args:
            return CredentialsHandler().getAllCredentials()
        else:
            #Searching by username, password
            return CredentialsHandler().searchCredentials(request.args)

@app.route('/ResourceApp/credentials/<string:username>', methods = ['GET', 'PUT', 'DELETE'])
def getCredentialsByUsername(username):
    if request.method == 'GET':
        return CredentialsHandler().getCredentialsByUsername(username)
    elif request.method == 'PUT':
        return CredentialsHandler().updateCredentials(username, request.form)
    elif request.method == 'DELETE':
        return CredentialsHandler().deleteCredentials(username)
    else:
        return jsonify(Error = 'Method not supported'), 405

@app.route('/ResourceApp/accounts/<int:aid>/credentials')
def getAccountCredentials(aid):
    if not request.args:
        return CredentialsHandler().getAccountCredentials(aid)
    else:
        return CredentialsHandler().searchAccountCredentials(aid, request.args)


if __name__ == '__main__':
    app.run()