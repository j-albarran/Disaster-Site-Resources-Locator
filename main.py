from flask import Flask, jsonify, request

from handler.cash import CashesHandler
from handler.credit_card import CreditCardsHandler
from handler.order import OrdersHandler
from handler.transaction import TransactionsHandler

app = Flask(__name__)

@app.route('/')
def welcome():
    return jsonify(Welcome = 'Hello, this is the Disaster-Site-Resources-Locator project.')

# ---------------------------------------------------------------------------- #
#                                City routes                                   #
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
#                               Region routes                                  #
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
#                               Address routes                                 #
# ---------------------------------------------------------------------------- #



# ---------------------------------------------------------------------------- #
#                               Account routes                                 #
# ---------------------------------------------------------------------------- #



# ---------------------------------------------------------------------------- #
#                            Administrator routes                              #
# ---------------------------------------------------------------------------- #



# ---------------------------------------------------------------------------- #
#                              Supplier routes                                 #
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
#                             Requester routes                                 #
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
#                              Resource routes                                 #
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
#                        Resource_Requested routes                             #
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
#                               Keyword routes                                 #
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
#                              Category routes                                 #
# ---------------------------------------------------------------------------- #


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
#                              Payment routes                                  #
# ---------------------------------------------------------------------------- #

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
