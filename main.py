from flask import Flask, jsonify, request

from handler.cash import CashesHandler
from handler.credit_card import CreditCardsHandler
from handler.order import OrdersHandler
from handler.transaction import TransactionsHandler

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
        return RegionHandler().getSupplierRegion(sid)

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

@app.route('/ResourceApp/requesters/<int:rid>/addresses')
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

# ---------------------------------------------------------------------------- #
#                            Transaction routes                                #
# ---------------------------------------------------------------------------- #

@app.route('/ResourceApp/transactions/<int:tid>')
def getTransactions(tid):
        return TransactionsHandler().getTransaction(tid)

@app.route('/ResourceApp/transactions')
def getAllTransactions():
    if not request.args:
        return TransactionsHandler().getAllTransactions
    else:
        return TransactionsHandler().searchAllTransactions(request.args)

@app.route('/ResourceApp/regions/<string:rname>/transactions')
def getTransactionsByRegion(rname):
    if not request.args:
        return TransactionsHandler().getTransactionsByRegion(rname)
    else:
        return TransactionsHandler().searchTransactionsByRegion(rname, request.args)

@app.route('/ResourceApp/cities/<string:cname>/transactions')
def getTransactionsByCity(cname):
    if not request.args:
        return TransactionsHandler().getTransactionsByCity(cname)
    else:
        return TransactionsHandler().searchTransactionsByCity(cname,request.args)

@app.route('/ResourceApp/suppliers/<int:sid>/transactions')
def getTransactionsBySupplier(sid):
    if not request.args:
        return TransactionsHandler().getTransactionsBySupplier(sid)
    else:
        return TransactionsHandler().searchTransactionsBySupplier(sid,request.args)

@app.route('/ResourceApp/requesters/<int:rid>/transactions')
def getTransactiosbyRequester(rid):
    if not request.args:
        return TransactionsHandler().getTransactiosbyRequester(rid)
    else:
        return TransactionsHandler().searchTransactiosbyRequester(rid,request.args)

@app.route('/ResourceApp/resources/<int:rsid>/transactions')
def getTransactionsByResource(rsid):
    if not request.args:
        return TransactionsHandler().getTransactionsByResource(rsid)
    else:
        return TransactionsHandler().searchTransactionsByResource(rsid, request.args)

@app.route('/ResourceApp/keywords/<int:kid>/transactions')
def getTransactionsByKeyword(kid):
    if not request.args:
        return TransactionsHandler().getTransactionsByKeyword(kid)
    else:
        return TransactionsHandler().searchTransactionsByKeyword(kid, request.args)

@app.route('/ResourceApp/categories/<string:cat_name>/transactions')
def getTransactionsByCategory(cat_name):
    if not request.args:
        return TransactionsHandler().getTransactionsByCategory(cat_name, cat_name)
    else:
        return TransactionsHandler().searchTransactionsByCategory(cat_name, cat_name,request.args)

@app.route('/ResourceApp/orders/<int:oid>/transactions')
def getTransactionsByOrder(oid):
    if not request.args:
        return TransactionsHandler().getTransactionsByOrder(oid)
    else:
        return TransactionsHandler().searchTransactionsByOrder(oid,request.args)

@app.route('/ResourceApp/credit_cards/<int:cid>/transactions')
def getTransactionsByCreditCard(cid):
    if not request.args:
        return TransactionsHandler().getTransactionsByCreditCard(cid)
    else:
        return TransactionsHandler().searchTransactionsByCreditCard(cid, request.args)

@app.route('/ResourceApp/payments/<int:payid>/transactions')
def getTransactionsByPayment(payid):
    if not request.args:
        return TransactionsHandler().getTransactionsByPayment(payid)
    else:
        return TransactionsHandler().searchTransactionsByPayment(payid, request.args)

@app.route('/ResourceApp/regions/<string:rname>/suppliers/<int:sid>/transactions')
def getTransactionsByRegionSupplier(rname, sid):
    if not request.args:
        return TransactionsHandler().getTransactionsByRegionSupplier(rname, sid)
    else:
        return TransactionsHandler().searchTransactionsByRegionSupplier(rname, sid, request.args)

@app.route('/ResourceApp/regions/<string:rname>/requesters/<int:rid>/transactions')
def getTransactionsByRegionRequester(rname, rid):
    if not request.args:
        return TransactionsHandler().getTransactionsByRegionRequester(rname,rid)
    else:
        return TransactionsHandler().searchTransactionsByRegionRequester(rname,rid, request.args)

@app.route('/ResourceApp/regions/<string:rname>/resources/<int:rsid>/transactions')
def getTransactionsByRegionResource(rname,rsid):
    if not request.args:
        return TransactionsHandler().getTransactionsByRegionResource(rname,rsid)
    else:
        return TransactionsHandler().searchTransactionsByRegionResource(rname,rsid,request.args)

@app.route('/ResourceApp/regions/<string:rname>/keywords/<int:kid>/transactions')
def getTransactionsByRegionKeyword(rname,kid):
    if not request.args:
        return TransactionsHandler().getTransactionsByRegionKeyword(rname, kid)
    else:
        return TransactionsHandler().searchTransactionsByRegionKeyword(rname, kid, request.args)

@app.route('/ResourceApp/regions/<string:rname>/categories/<string:cat_name>/transactions')
def getTransactionsByRegionCategory(rname,cat_name):
    if not request.args:
        return TransactionsHandler().getTransactionsByRegionCategory(rname, cat_name, cat_name)
    else:
        return TransactionsHandler().searchTransactionsByRegionCategory(rname, cat_name, cat_name, request.args)

@app.route('/ResourceApp/regions/<string:rname>/orders/<int:oid>/transactions')
def getTransactionsByRegionOrder(rname,oid):
    if not request.args:
        return TransactionsHandler().getTransactionsByRegionOrder(rname, oid)
    else:
        return TransactionsHandler().searchTransactionsByRegionOrder(rname, oid, request.args)

@app.route('/ResourceApp/cities/<string:cname>/suppliers/<int:sid>/transactions')
def getTransactionsByCitySupplier(cname,sid):
    if not request.args:
        return TransactionsHandler().getTransactionsByCitySupplier(cname,sid)
    else:
        return TransactionsHandler().searchTransactionsByCitySupplier(cname,sid,request.args)


@app.route('/ResourceApp/cities/<string:cname>/requesters/<int:rid>/transactions')
def getTransactionsByCityRequester(cname,rid):
    if not request.args:
        return TransactionsHandler().getTransactionsByCityRequester(cname, rid)
    else:
        return TransactionsHandler().searchTransactionsByCityRequester(cname, rid, request.args)

@app.route('/ResourceApp/cities/<string:cname>/resources/<int:rsid>/transactions')
def getTransactionsByCityResource(cname,rsid):
    if not request.args:
        return TransactionsHandler().getTransactionsByCityResource(cname,rsid)
    else:
        return TransactionsHandler().searchTransactionsByCityResource(cname,rsid, request.args)

@app.route('/ResourceApp/cities/<string:cname>/keywords/<int:kid>/transactions')
def getTransactionsByCityKeyword(cname, kid):
    if not request.args:
        return TransactionsHandler().getTransactionsByCityKeyword(cname, kid)
    else:
        return TransactionsHandler().searchTransactionsByCityKeyword(cname, kid,request.args)

@app.route('/ResourceApp/cities/<string:cname>/categories/<string:cat_name>/transactions')
def getTransactionsByCityCategory(cname,cat_name):
    if not request.args:
        return TransactionsHandler().getTransactionsByCityCategory(cname,cat_name, cat_name)
    else:
        return TransactionsHandler().searchTransactionsByCityCategory(cname,cat_name, cat_name,request.args)

@app.route('/ResourceApp/cities/<string:cname>/orders/<int:oid>/transactions')
def getTransactionsByCityOrder(cname,oid):
    if not request.args:
        return TransactionsHandler().getTransactionsByCityOrder(cname,oid)
    else:
        return TransactionsHandler().searchTransactionsByCityOrder(cname,oid,request.args)

@app.route('/ResourceApp/suppliers/<int:sid>/requesters/<int:rid>/transactions')
def getTransactionsBySupplierRequester(sid,rid):
    if not request.args:
        return TransactionsHandler().getTransactionsBySupplierRequester(sid,rid)
    else:
        return TransactionsHandler().searchTransactionsBySupplierRequester(sid,rid,request.args)

@app.route('/ResourceApp/suppliers/<int:sid>/resources/<int:rsid>/transactions')
def getTransactionsBySupplierResource(sid,rsid):
    if not request.args:
        return TransactionsHandler().getTransactionsBySupplierResource(sid,rsid)
    else:
        return TransactionsHandler().searchTransactionsBySupplierResource(sid,rsid, request.args)

@app.route('/ResourceApp/suppliers/<int:sid>/keywords/<int:kid>/transactions')
def getTransactionsBySupplierKeyword(sid,kid):
    if not request.args:
        return TransactionsHandler().getTransactionsBySupplierKeyword(sid,kid)
    else:
        return TransactionsHandler().searchTransactionsBySupplierKeyword(sid,kid,request.args)

@app.route('/ResourceApp/suppliers/<int:sid>/categories/<string:cat_name>/transactions')
def getTransactionsBySupplierCategory(sid,cat_name):
    if not request.args:
        return TransactionsHandler().getTransactionsBySupplierCategory(sid,cat_name,cat_name)
    else:
        return TransactionsHandler().searchTransactionsBySupplierCategory(sid,cat_name,cat_name,request.args)

@app.route('/ResourceApp/suppliers/<int:sid>/orders/<int:oid>/transactions')
def getTransactionsBySupplierOrder(sid,oid):
    if not request.args:
        return TransactionsHandler().getTransactionsBySupplierOrder(sid,oid)
    else:
        return TransactionsHandler().searchTransactionsBySupplierOrder(sid,oid,request.args)

@app.route('/ResourceApp/requesters/<int:rid>/resources/<int:rsid>/transactions')
def getTransactionsByRequesterResource(rid,rsid):
    if not request.args:
        return TransactionsHandler().getTransactionsByRequesterResource(rid,rsid)
    else:
        return TransactionsHandler().searchTransactionsByRequesterResource(rid,rsid,request.args)

@app.route('/ResourceApp/requesters/<int:rid>/keywords/<int:kid>/transactions')
def getTransactionsByRequesterKeyword(rid,kid):
    if not request.args:
        return TransactionsHandler().getTransactionsByRequesterKeyword(rid,kid)
    else:
        return TransactionsHandler().searchTransactionsByRequesterKeyword(rid,kid,request.args)

@app.route('/ResourceApp/requesters/<int:rid>/categories/<string:cat_name>/transactions')
def getTransactionsByRequesterCategory(rid,cat_name):
    if not request.args:
        return TransactionsHandler().getTransactionsByRequesterCategory(rid,cat_name,cat_name)
    else:
        return TransactionsHandler().searchTransactionsByRequesterCategory(rid,cat_name,cat_name,request.args)

@app.route('/ResourceApp/requesters/<int:rid>/orders/<int:oid>/transactions')
def getTransactionsByRequesterOrder(rid,oid):
    if not request.args:
        return TransactionsHandler().getTransactionsByRequesterOrder(rid,oid)
    else:
        return TransactionsHandler().searchTransactionsByRequesterOrder(rid,oid,request.args)

@app.route('/ResourceApp/resources/<int:rsid>/keywords/<int:kid>/transactions')
def getTransactionsByResourceKeyword(rsid, kid):
    if not request.args:
        return TransactionsHandler().getTransactionsByResourceKeyword(rsid,kid)
    else:
        return TransactionsHandler().searchTransactionsByResourceKeyword(rsid,kid,request.args)

@app.route('/ResourceApp/resources/<int:rsid>/orders/<int:oid>/transactions')
def getTransactionsByResourceOrder(rsid,oid):
    if not request.args:
        return TransactionsHandler().getTransactionsByResourceOrder(rsid,oid)
    else:
        return TransactionsHandler().searchTransactionsByResourceOrder(rsid,oid,request.args)

@app.route('/ResourceApp/keywords/<int:kid>/categories/<string:cat_name>/transactions')
def getTransactionsByKeywordCategory(kid,cat_name):
    if not request.args:
        return TransactionsHandler().getTransactionsByKeywordCategory(kid,cat_name,cat_name)
    else:
        return TransactionsHandler().searchTransactionsByKeywordCategory(kid,cat_name,cat_name, request.args)

@app.route('/ResourceApp/keywords/<int:kid>/orders/<int:oid>/transactions')
def getTransactionsByKeywordOrder(kid,oid):
    if not request.args:
        return TransactionsHandler().getTransactionsByKeywordOrder(kid,oid)
    else:
        return TransactionsHandler().searchTransactionsByKeywordOrder(kid,oid,request.args)

@app.route('/ResourceApp/categories/<string:cat_name>/orders/<int:oid>/transactions')
def getTransactionsByCategoryOrder(cat_name,oid):
    if not request.args:
        return TransactionsHandler().getTransactionsByCategoryOrder(cat_name,cat_name,oid)
    else:
        return TransactionsHandler().searchTransactionsByCategoryOrder(cat_name, cat_name,oid,request.args)

@app.route('/ResourceApp/regions/<string:rname>/suppliers/<int:sid>/requesters/<int:rid>/transactions')
def getTransactionsByRegionSupplierRequester(rname, sid, rid):
    if not request.args:
        return TransactionsHandler().getTransactionsByRegionSupplierRequester(rname,sid,rid)
    else:
        return TransactionsHandler().searchTransactionsByRegionSupplierRequester(rname,sid,rid,request.args)

@app.route('/ResourceApp/regions/<string:rname>/suppliers/<int:sid>/resources/<int:rsid>/transactions')
def getTransactionsByRegionSupplierResource(rname,sid,rsid):
    if not request.args:
        return TransactionsHandler().getTransactionsByRegionSupplierResource(rname, sid, rsid)
    else:
        return TransactionsHandler().searchTransactionsByRegionSupplierResource(rname, sid, rsid, request.args)

@app.route('/ResourceApp/regions/<string:rname>/suppliers/<int:sid>/keywords/<int:kid>/transactions')
def getTransactionsByRegionSupplierKeyword(rname,sid,kid):
    if not request.args:
        return TransactionsHandler().getTransactionsByRegionSupplierKeyword(rname,sid,kid)
    else:
        return TransactionsHandler().searchTransactionsByRegionSupplierKeyword(rname,sid,kid,request.args)

@app.route('/ResourceApp/regions/<string:rname>/suppliers/<int:sid>/categories/<string:cat_name>/transactions')
def getTransactionsByRegionSupplierCategory(rname,sid,cat_name):
    if not request.args:
        return TransactionsHandler().getTransactionsByRegionSupplierCategory(rname, sid, cat_name, cat_name)
    else:
        return TransactionsHandler().searchTransactionsByRegionSupplierCategory(rname, sid, cat_name, cat_name, request.args)

@app.route('/ResourceApp/regions/<string:rname>/suppliers/<int:sid>/orders/<int:oid>/transactions')
def getTransactionsByRegionSupplierOrder(rname,sid,oid):
    if not request.args:
        return TransactionsHandler().getTransactionsByRegionSupplierOrder(rname,sid,oid)
    else:
        return TransactionsHandler().searchTransactionsByRegionSupplierOrder(rname,sid,oid,request.args)

@app.route('/ResourceApp/regions/<string:rname>/requesters/<int:rid>/resources/<int:rsid>/transactions')
def getTransactionsByRegionRequesterResource(rname, rid, rsid):
    if not request.args:
        return TransactionsHandler().getTransactionsByRegionRequesterResource(rname,rid,rsid)
    else:
        return TransactionsHandler().searchTransactionsByRegionRequesterResource(rname,rid,rsid, request.args)

@app.route('/ResourceApp/regions/<string:rname>/requesters/<int:rid>/keywords/<int:kid>/transactions')
def getTransactionsByRegionRequesterKeyword(rname,rid,kid):
    if not request.args:
        return TransactionsHandler().getTransactionsByRegionRequesterKeyword(rname, rid,kid)
    else:
        return TransactionsHandler().searchTransactionsByRegionRequesterKeyword(rname,rid,kid, request.args)

@app.route('/ResourceApp/regions/<string:rname>/requesters/<int:rid>/categories/<string:cat_name>/transactions')
def getTransactionsByRegionRequesterCategory(rname, rid, cat_name):
    if not request.args:
        return TransactionsHandler().getTransactionsByRegionRequesterCategory(rname,rid,cat_name, cat_name)
    else:
        return TransactionsHandler().searchTransactionsByRegionRequesterCategory(rname,rid,cat_name, cat_name,request.args)

@app.route('/ResourceApp/regions/<string:rname>/requesters/<int:rid>/orders/<int:oid>/transactions')
def getTransactionsByRegionRequesterOrder(rname, rid, oid):
    if not request.args:
        return TransactionsHandler().getTransactionsByRegionRequesterOrder(rname,rid,oid)
    else:
        return TransactionsHandler().searchTransactionsByRegionRequesterOrder(rname,rid,oid,request.args)

@app.route('/ResourceApp/regions/<string:rname>/resources/<int:rsid>/keywords/<int:kid>/transactions')
def getTransactionsByRegionResourceKeyword(rname,rsid, kid):
    if not request.args:
        return TransactionsHandler().getTransactionsByRegionResourceKeyword(rname,rsid,kid)
    else:
        return TransactionsHandler().searchTransactionsByRegionResourceKeyword(rname,rsid,kid,request.args)

@app.route('/ResourceApp/regions/<string:rname>/resources/<int:rsid>/orders/<int:oid>/transactions')
def getTransactionsByRegionResourceOrder(rname,rsid, oid):
    if not request.args:
        return TransactionsHandler().getTransactionsByRegionResourceOrder(rname, rsid,oid)
    else:
        return TransactionsHandler().searchTransactionsByRegionResourceOrder(rname, rsid,oid,request.args)

@app.route('/ResourceApp/regions/<string:rname>/keywords/<int:kid>/categories/<string:cat_name>/transactions')
def getTransactionsByRegionKeywordCategory(rname,kid,cat_name):
    if not request.args:
        return TransactionsHandler().getTransactionsByRegionKeywordCategory(rname,kid,cat_name,cat_name)
    else:
        return TransactionsHandler().searchTransactionsByRegionKeywordCategory(rname,kid,cat_name, cat_name, request.args)

@app.route('/ResourceApp/regions/<string:rname>/keywords/<int:kid>/orders/<int:oid>/transactions')
def getTransactionsByRegionKeywordOrder(rname,kid,oid):
    if not request.args:
        return TransactionsHandler().getTransactionsByRegionKeywordOrder(rname,kid,oid)
    else:
        return TransactionsHandler().searchTransactionsByRegionKeywordOrder(rname,kid,oid,request.args)

@app.route('/ResourceApp/regions/<string:rname>/categories/<string:cat_name>/orders/<int:oid>/transactions')
def getTransactionsByRegionCategoryOrder(rname,cat_name,oid):
    if not request.args:
        return TransactionsHandler().getTransactionsByRegionCategoryOrder(rname, cat_name,cat_name, oid)
    else:
        return TransactionsHandler().searchTransactionsByRegionCategoryOrder(rname, cat_name,cat_name, oid, request.args)

@app.route('/ResourceApp/cities/<string:cname>/suppliers/<int:sid>/requesters/<int:rid>/transactions')
def getTransactionsByCitySupplierRequester(cname,sid,rid):
    if not request.args:
        return TransactionsHandler().getTransactionsByCitySupplierRequester(cname,sid,rid)
    else:
        return TransactionsHandler().searchTransactionsByCitySupplierRequester(cname,sid,rid,request.args)

@app.route('/ResourceApp/cities/<string:cname>/suppliers/<int:sid>/resources/<int:rsid>/transactions')
def getTransactionsByCitySupplierResource(cname,sid,rsid):
    if not request.args:
        return TransactionsHandler().getTransactionsByCitySupplierResource(cname,sid,rsid)
    else:
        return TransactionsHandler().searchTransactionsByCitySupplierResource(cname,sid,rsid,request.args)
@app.route('/ResourceApp/cities/<string:cname>/suppliers/<int:sid>/keywords/<int:kid>/transactions')
def getTransactionsByCitySupplierKeyword(cname,sid,kid):
    if not request.args:
        return TransactionsHandler().getTransactionsByCitySupplierKeyword(cname,sid,kid)
    else:
        return TransactionsHandler().searchTransactionsByCitySupplierKeyword(cname,sid,kid,request.args)

@app.route('/ResourceApp/cities/<string:cname>/suppliers/<int:sid>/categories/<string:cat_name>/transactions')
def getTransactionsByCitySupplierCategory(cname,sid,cat_name):
    if not request.args:
        return TransactionsHandler().getTransactionsByCitySupplierCategory(cname,sid,cat_name,cat_name)
    else:
        return TransactionsHandler().searchTransactionsByCitySupplierCategory(cname,sid,cat_name,cat_name,request.args)

@app.route('/ResourceApp/cities/<string:cname>/suppliers/<int:sid>/orders/<int:oid>/transactions')
def getTransactionsByCitySupplierOrder(cname,sid,oid):
    if not request.args:
        return TransactionsHandler().getTransactionsByCitySupplierOrder(cname,sid,oid)
    else:
        return TransactionsHandler().searchTransactionsByCitySupplierOrder(cname,sid,oid,request.args)

@app.route('/ResourceApp/cities/<string:cname>/requesters/<int:rid>/resources/<int:rsid>/transactions')
def getTransactionsByCityRequesterResource(cname,rid,rsid):
    if not request.args:
        return TransactionsHandler().getTransactionsByCityRequesterResource(cname,rid,rsid)
    else:
        return TransactionsHandler().searchTransactionsByCityRequesterResource(cname,rid,rsid,request.args)

@app.route('/ResourceApp/cities/<string:cname>/requesters/<int:rid>/keywords/<int:kid>/transactions')
def getTransactionsByCityRequesterKeyword(cname,rid,kid):
    if not request.args:
        return TransactionsHandler().getTransactionsByCityRequesterKeyword(cname,rid,kid)
    else:
        return TransactionsHandler().searchTransactionsByCityRequesterKeyword(cname,rid,kid,request.args)

@app.route('/ResourceApp/cities/<string:cname>/requesters/<int:rid>/categories/<string:cat_name>/transactions')
def getTransactionsByCityRequesterCategory(cname,rid,cat_name):
    if not request.args:
        return TransactionsHandler().getTransactionsByCityRequesterCategory(cname,rid,cat_name,cat_name)
    else:
        return TransactionsHandler().searchTransactionsByCityRequesterCategory(cname,rid,cat_name,cat_name,request.args)

@app.route('/ResourceApp/cities/<string:cname>/requesters/<int:rid>/orders/<int:oid>/transactions')
def getTransactionsByCityRequesterOrder(cname,rid,oid):
    if not request.args:
        return TransactionsHandler().getTransactionsByCityRequesterOrder(cname,rid,oid)
    else:
        return TransactionsHandler().searchTransactionsByCityRequesterOrder(cname,rid,oid,request.args)

@app.route('/ResourceApp/cities/<string:cname>/resources/<int:rsid>/keywords/<int:kid>/transactions')
def getTransactionsByCityResourceKeyword(cname,rsid,kid):
    if not request.args:
        return TransactionsHandler().getTransactionsByCityResourceKeyword(cname,rsid,kid)
    else:
        return TransactionsHandler().searchTransactionsByCityResourceKeyword(cname,rsid,kid,request.args)

@app.route('/ResourceApp/cities/<string:cname>/resources/<int:rsid>/orders/<int:oid>/transactions')
def getTransactionsByCityResourceOrder(cname,rsid,oid):
    if not request.args:
        return TransactionsHandler().getTransactionsByCityResourceOrder(cname,rsid,oid)
    else:
        return TransactionsHandler().searchTransactionsByCityResourceOrder(cname,rsid,oid,request.args)

@app.route('/ResourceApp/cities/<string:cname>/keywords/<int:kid>/categories/<string:cat_name>/transactions')
def getTransactionsByCityKeywordCategory(cname,kid,cat_name):
    if not request.args:
        return TransactionsHandler().getTransactionsByCityKeywordCategory(cname,kid,cat_name,cat_name)
    else:
        return TransactionsHandler().searchTransactionsByCityKeywordCategory(cname,kid,cat_name,cat_name,request.args)

@app.route('/ResourceApp/cities/<string:cname>/keywords/<int:kid>/orders/<int:oid>/transactions')
def getTransactionsByCityKeywordOrder(cname,kid,oid):
    if not request.args:
        return TransactionsHandler().getTransactionsByCityKeywordOrder(cname,kid,oid)
    else:
        return TransactionsHandler().searchTransactionsByCityKeywordOrder(cname,kid,oid,request.args)

@app.route('/ResourceApp/cities/<string:cname>/categories/<string:cat_name>/orders/<int:oid>/transactions')
def getTransactionsByCityCategoryOrder(cname,cat_name,oid):
    if not request.args:
        return TransactionsHandler().getTransactionsByCityCategoryOrder(cname,cat_name,cat_name,oid)
    else:
        return TransactionsHandler().searchTransactionsByCityCategoryOrder(cname,cat_name,cat_name,oid,request.args)

@app.route('/ResourceApp/suppliers/<int:sid>/requesters/<int:rid>/resources/<int:rsid>/transactions')
def getTransactionsBySupplierRequesterResource(sid,rid,rsid):
    if not request.args:
        return TransactionsHandler().getTransactionsBySupplierRequesterResource(sid,rid,rsid)
    else:
        return TransactionsHandler().searchTransactionsBySupplierRequesterResource(sid,rid,rsid,request.args)

@app.route('/ResourceApp/suppliers/<int:sid>/requesters/<int:rid>/keywords/<int:kid>/transactions')
def getTransactionsBySupplierRequesterKeyword(sid,rid,kid):
    if not request.args:
        return TransactionsHandler().getTransactionsBySupplierRequesterKeyword(sid,rid,kid)
    else:
        return TransactionsHandler().searchTransactionsBySupplierRequesterKeyword(sid,rid,kid,request.args)
@app.route('/ResourceApp/suppliers/<int:sid>/requesters/<int:rid>/categories/<string:cat_name>/transactions')
def getTransactionsBySupplierRequesterCategory(sid,rid,cat_name):
    if not request.args:
        return TransactionsHandler().getTransactionsBySupplierRequesterCategory(sid,rid,cat_name,cat_name)
    else:
        return TransactionsHandler().searchTransactionsBySupplierRequesterCategory(sid,rid,cat_name,cat_name,request.args)

@app.route('/ResourceApp/suppliers/<int:sid>/requesters/<int:rid>/orders/<int:oid>/transactions')
def getTransactionsBySupplierRequesterOrder(sid,rid,oid):
    if not request.args:
        return TransactionsHandler().getTransactionsBySupplierRequesterOrder(sid,rid,oid)
    else:
        return TransactionsHandler().searchTransactionsBySupplierRequesterOrder(sid,rid,oid,request.args)

@app.route('/ResourceApp/suppliers/<int:sid>/resources/<int:rsid>/keywords/<int:kid>/transactions')
def getTransactionsBySupplierResourceKeyword(sid,rsid,kid):
    if not request.args:
        return TransactionsHandler().getTransactionsBySupplierResourceKeyword(sid,rsid,kid)
    else:
        return TransactionsHandler().searchTransactionsBySupplierResourceKeyword(sid,rsid,kid,request.args)

@app.route('/ResourceApp/suppliers/<int:sid>/resources/<int:rsid>/orders/<int:oid>/transactions')
def getTransactionsBySupplierResourceOrder(sid,rsid,oid):
    if not request.args:
        return TransactionsHandler().getTransactionsBySupplierResourceOrder(sid,rsid,oid)
    else:
        return TransactionsHandler().searchTransactionsBySupplierResourceOrder(sid,rsid,oid,request.args)

@app.route('/ResourceApp/suppliers/<int:sid>/keywords/<int:kid>/categories/<string:cat_name>/transactions')
def getTransactionsBySupplierKeywordCategory(sid,kid,cat_name):
    if not request.args:
        return TransactionsHandler().getTransactionsBySupplierKeywordCategory(sid,kid,cat_name,cat_name)
    else:
        return TransactionsHandler().searchTransactionsBySupplierKeywordCategory(sid,kid,cat_name, cat_name,request.args)

@app.route('/ResourceApp/suppliers/<int:sid>/keywords/<int:kid>/orders/<int:oid>/transactions')
def getTransactionsBySupplierKeywordOrder(sid,kid,oid):
    if not request.args:
        return TransactionsHandler().getTransactionsBySupplierKeywordOrder(sid,kid,oid)
    else:
        return TransactionsHandler().searchTransactionsBySupplierKeywordOrder(sid,kid,oid,request.args)

@app.route('/ResourceApp/suppliers/<int:sid>/categories/<string:cat_name>/orders/<int:oid>/transactions')
def getTransactionsBySupplierCategoryOrder(sid,cat_name,oid):
    if not request.args:
        return TransactionsHandler().getTransactionsBySupplierCategoryOrder(sid,cat_name,cat_name,oid)
    else:
        return TransactionsHandler().searchTransactionsBySupplierCategoryOrder(sid,cat_name, cat_name,oid,request.args)

@app.route('/ResourceApp/requesters/<int:rid>/resources/<int:rsid>/keywords/<int:kid>/transactions')
def getTransactionsByRequesterResourceKeyword(rid,rsid,kid):
    if not request.args:
        return TransactionsHandler().getTransactionsByRequesterResourceKeyword(rid,rsid,kid)
    else:
        return TransactionsHandler().searchTransactionsByRequesterResourceKeyword(rid,rsid,kid,request.args)

@app.route('/ResourceApp/requesters/<int:rid>/resources/<int:rsid>/orders/<int:oid>/transactions')
def getTransactionsByRequesterResourceOrder(rid,rsid,oid):
    if not request.args:
        return TransactionsHandler().getTransactionsByRequesterResourceOrder(rid,rsid,oid)
    else:
        return TransactionsHandler().searchTransactionsByRequesterResourceOrder(rid,rsid,oid,request.args)

@app.route('/ResourceApp/requesters/<int:rid>/keywords/<int:kid>/categories/<string:cat_name>/transactions')
def getTransactionsByRequesterKeywordCategory(rid,kid,cat_name):
    if not request.args:
        return TransactionsHandler().getTransactionsByRequesterKeywordCategory(rid,kid,cat_name, cat_name)
    else:
        return TransactionsHandler().searchTransactionsByRequesterKeywordCategory(rid,kid,cat_name, cat_name,request.args)

@app.route('/ResourceApp/requesters/<int:rid>/keywords/<int:kid>/orders/<int:oid>/transactions')
def getTransactionsByRequesterKeywordOrder(rid,kid,oid):
    if not request.args:
        return TransactionsHandler().getTransactionsByRequesterKeywordOrder(rid,kid,oid)
    else:
        return TransactionsHandler().searchTransactionsByRequesterKeywordOrder(rid,kid,oid,request.args)

@app.route('/ResourceApp/requesters/<int:rid>/categories/<string:cat_name>/orders/<int:oid>/transactions')
def getTransactionsByRequesterCategoryOrder(rid,cat_name,oid):
    if not request.args:
        return TransactionsHandler().getTransactionsByRequesterCategoryOrder(rid,cat_name, cat_name,oid)
    else:
        return TransactionsHandler().searchTransactionsByRequesterCategoryOrder(rid,cat_name, cat_name,oid,request.args)

@app.route('/ResourceApp/resources/<int:rsid>/keywords/<int:kid>/categories/<string:cat_name>/transactions')
def getTransactionsByResourceKeywordCategory(rsid,kid,cat_name):
    if not request.args:
        return TransactionsHandler().getTransactionsByResourceKeywordCategory(rsid,kid,cat_name, cat_name)
    else:
        return TransactionsHandler().searchTransactionsByResourceKeywordCategory(rsid,kid,cat_name, cat_name,request.args)

@app.route('/ResourceApp/resources/<int:rsid>/keywords/<int:kid>/orders/<int:oid>/transactions')
def getTransactionsByResourceKeywordOrder(rsid,kid,oid):
    if not request.args:
        return TransactionsHandler().getTransactionsByResourceKeywordOrder(rsid,kid,oid)
    else:
        return TransactionsHandler().searchTransactionsByResourceKeywordOrder(rsid,kid,oid,request.args)

@app.route('/ResourceApp/keywords/<int:kid>/categories/<string:cat_name>/orders/<int:oid>/transactions')
def getTransactionsByKeywordCategoryOrder(kid,cat_name,oid):
    if not request.args:
        return TransactionsHandler().getTransactionsByKeywordCategoryOrder(kid,cat_name,cat_name,oid)
    else:
        return TransactionsHandler().searchTransactionsByKeywordCategoryOrder(kid,cat_name,cat_name,oid,request.args)

# ---------------------------------------------------------------------------- #
#                            Credit_Card routes                                #
# ---------------------------------------------------------------------------- #

@app.route('/ResourceApp/credit_cards')
def getAllCreditCards():
    if not request.args:
        return CreditCardsHandler().getAllCreditCards()
    else:
        return CreditCardsHandler().searchAllCreditCards(request.args)


@app.route('/ResourceApp/credit_cards/<int:cid>')
def getCreditCardsById(cid):
    if not request.args:
        return CreditCardsHandler().getCreditCard(cid)
    else:
        return CreditCardsHandler().searchCreditCard(cid, request.args)


@app.route('/ResourceApp/transactions/<int:tid>/credit_cards')
def getCreditCardsByTransaction(tid):
    if not request.args:
        return CreditCardsHandler().getCreditCardsByTransaction(tid)
    else:
        return CreditCardsHandler().searchCreditCardsByTransaction(tid, request.args)


@app.route('/ResourceApp/requesters/<int:rid>/credit_cards')
def getCreditCardsByRequester(rid):
    if not request.args:
        return CreditCardsHandler().getCreditCardsByRequester(rid)
    else:
        return CreditCardsHandler().searchCreditCardsByRequester(rid, request.args)


@app.route('/ResourceApp/orders/<int:oid>/credit_cards')
def getCreditCardsByOrder(oid):
    if not request.args:
        return CreditCardsHandler().getCreditCardsByOrder(oid)
    else:
        return CreditCardsHandler().searchCreditCardsByOrder(oid, request.args)

# ---------------------------------------------------------------------------- #
#                              Cash routes                                  #
# ---------------------------------------------------------------------------- #

@app.route('/ResourceApp/cashes')
def getAllCashes():
    return CashesHandler().getAllCashes()



@app.route('/ResourceApp/cashes/<int:cashid>')
def getCashesById(cashid):
    return CashesHandler().getCashesById(cashid)



@app.route('/ResourceApp/transactions/<int:tid>/cashes')
def getCashesByTransaction(tid):
    return CashesHandler().getCashesByTransaction(tid)



@app.route('/ResourceApp/requesters/<int:rid>/cashes')
def getCashesByRequester(rid):
    return CashesHandler().getCashesByRequester(rid)

@app.route('/ResourceApp/orders/<int:oid>/cashes')
def getCashesByOrder(oid):
    return CashesHandler().getCashesByOrder(oid)

# ---------------------------------------------------------------------------- #
#                              Order routes                                  #
# ---------------------------------------------------------------------------- #


@app.route('/ResourceApp/orders')
def getAllOrders():
    if not request.args:
        return OrdersHandler().getAllOrders()
    else:
        return OrdersHandler().searchAllOrders(request.args)


@app.route('/ResourceApp/orders/<int:oid>')
def getOrdersById(oid):
    if not request.args:
        return OrdersHandler().getOrdersById(oid)
    else:
        return OrdersHandler().searchOrdersById(oid, request.args)


@app.route('/ResourceApp/requesters/<int:rid>/orders')
def getOrdersByRequester(rid):
    if not request.args:
        return OrdersHandler().getOrdersByRequester(rid)
    else:
        return OrdersHandler().searchOrdersByRequester(rid, request.args)

if __name__ == '__main__':
    app.run()
