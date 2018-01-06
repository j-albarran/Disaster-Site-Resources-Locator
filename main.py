from flask import Flask, jsonify, request
from handler.resource import ResourceHandler
from handler.resource_requested import ResourceRequestedHandler
from handler.keyword import KeywordHandler
from handler.category import CategoryHandler

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

@app.route('/ResourceApp/resources', methods = ['GET', 'POST']) # By rname, rprice, rqty, rdescription, r_supply_date, r_changed_date
def handleResources():
    if request.method == 'POST':
        return ResourceHandler().insertResource(request.form)
    else:
        if not request.args:
            return ResourceHandler().getAllResources()
        else:
            return ResourceHandler().searchResources(request.args)

@app.route('/ResourceApp/resources/<int:rsid>', methods = ['GET', 'PUT', 'DELETE'])
def handleResourceById(rsid):
    if request.method == 'GET':
        return ResourceHandler().getResourceById(rsid)
    elif request.method == 'PUT':
        return ResourceHandler().updateResource(rsid, request.form)
    elif request.method == 'DELETE':
        return ResourceHandler().deleteResource(rsid)
    else:
        return jsonify(Error = "Method not allowed."), 405

@app.route('/ResourceApp/cities/<string:cname>/resources') # By rname, rprice, rqty, rdescription, r_supply_date, r_changed_date
def getResourcesByCityName(cname):
    if not request.args:
        return ResourceHandler().getResourcesByCityName(cname)
    else:
        return ResourceHandler().searchResourcesByCityName(cname, request.args)

@app.route('/ResourceApp/regions/<string:rname>/resources') # By rname, rprice, rqty, rdescription, r_supply_date, r_changed_date
def getResourcesByRegionName(rname):
    if not request.args:
        return ResourceHandler().getResourcesByRegionName(rname)
    else:
        return ResourceHandler().searchResourcesByRegionName(rname, request.args)

@app.route('/ResourceApp/suppliers/<int:sid>/resources')
def getResourcesBySupplierId(sid):
    if not request.args:
        return ResourceHandler().getResourcesBySupplierId(sid)
    else:
        return ResourceHandler().searchResourcesBySupplierId(sid, request.args)

@app.route('/ResourceApp/keywords/<int:kid>/resources') # By rname, rprice, rqty, rdescription, r_supply_date, r_changed_date
def getResourcesByKeywordId(kid):
    if not request.args:
        return ResourceHandler().getResourcesByKeywordId(kid)
    else:
        return ResourceHandler().searchResourcesByKeywordId(kid, request.args)

@app.route('/ResourceApp/categories/<string:cat_name>/resources') # By rname, rprice, rqty, rdescription, r_supply_date, r_changed_date
def getResourcesByCategoryName(cat_name):
    if not request.args:
        return ResourceHandler().getResourcesByCategoryName(cat_name)
    else:
        return ResourceHandler().searchResourcesByCategoryName(cat_name, request.args)

@app.route('/ResourceApp/transactions/<int:tid>/resources') # By rname, rprice, rqty, rdescription, r_supply_date, r_changed_date
def getResourcesByTransactionId(tid):
    if not request.args:
        return ResourceHandler().getResourcesByTransactionId(tid)
    else:
        return ResourceHandler().searchResourcesByTransactionId(tid, request.args)

@app.route('/ResourceApp/orders/<int:oid>/resources')
def getResourcesByOrderId(oid):
    if not request.args:
        return ResourceHandler().getResourcesByOrderId(oid)
    else:
        return ResourceHandler().searchResourcesByOrderId(oid, request.args)

@app.route('/ResourceApp/cities/<string:cname>/keywords/<int:kid>/resources')
def getResourcesByCityKeyword(cname, kid):
    if not request.args:
        return ResourceHandler().getResourcesByCityKeyword(cname, kid)
    else:
        return ResourceHandler().searchResourcesByCityKeyword(cname, kid, request.args)

@app.route('/ResourceApp/cities/<string:cname>/categories/<string:cat_name>/resources')
def getResourcesByCityCategory(cname, cat_name):
    if not request.args:
        return ResourceHandler().getResourcesByCityCategory(cname, cat_name)
    else:
        return ResourceHandler().searchResourcesByCityCategory(cname, cat_name, request.args)

@app.route('/ResourceApp/regions/<string:rname>/keywords/<int:kid>/resources')
def getResourcesByRegionKeyword(rname, kid):
    if not request.args:
        return ResourceHandler().getResourcesByRegionKeyword(rname, kid)
    else:
        return ResourceHandler().searchResourcesByRegionKeyword(rname, kid, request.args)

@app.route('/ResourceApp/regions/<string:rname>/categories/<string:cat_name>/resources')
def getResourcesByRegionCategory(rname, cat_name):
    if not request.args:
        return ResourceHandler().getResourcesByRegionCategory(rname, cat_name)
    else:
        return ResourceHandler().searchResourcesByRegionCategory(rname, cat_name, request.args)

@app.route('/ResourceApp/suppliers/<int:sid>/keywords/<int:kid>/resources')
def getResourcesBySupplierKeyword(sid, kid):
    if not request.args:
        return ResourceHandler().getResourcesBySupplierKeyword(sid, kid)
    else:
        return ResourceHandler().searchResourcesBySupplierKeyword(sid, kid, request.args)

@app.route('/ResourceApp/suppliers/<int:sid>/categories/<string:cat_name>/resources')
def getResourcesBySupplierCategory(sid, cat_name):
    if not request.args:
        return ResourceHandler().getResourcesBySupplierCategory(sid, cat_name)
    else:
        return ResourceHandler().searchResourcesBySupplierCategory(sid, cat_name, request.args)

@app.route('/ResourceApp/suppliers/<int:sid>/orders/<int:oid>/resources')
def getResourcesBySupplierOrder(sid, oid):
    if not request.args:
        return ResourceHandler().getResourcesBySupplierOrder(sid, oid)
    else:
        return ResourceHandler().searchResourcesBySupplierOrder(sid, oid, request.args)

@app.route('/ResourceApp/keywords/<int:kid>/categories/<string:cat_name>/resources')
def getResourcesByKeywordCategory(kid, cat_name):
    if not request.args:
        return ResourceHandler().getResourcesByKeywordCategory(kid, cat_name)
    else:
        return ResourceHandler().searchResourcesByKeywordCategory(kid, cat_name, request.args)

@app.route('/ResourceApp/keywords/<int:kid>/orders/<int:oid>/resources')
def getResourcesByKeywordOrder(kid, oid):
    if not request.args:
        return ResourceHandler().getResourcesByKeywordOrder(kid, oid)
    else:
        return ResourceHandler().searchResourcesByKeywordOrder(kid, oid, request.args)

@app.route('/ResourceApp/categories/<string:cat_name>/orders/<int:oid>/resources')
def getResourcesByCategoryOrder(cat_name, oid):
    if not request.args:
        return ResourceHandler().getResourcesByCategoryOrder(cat_name, oid)
    else:
        return ResourceHandler().searchResourcesByCategoryOrder(cat_name, oid, request.args)

@app.route('/ResourceApp/transactions/<int:tid>/orders/<int:oid>/resources')
def getResourcesByTransactionOrder(tid, oid):
    if not request.args:
        return ResourceHandler().getResourcesByTransactionOrder(tid, oid)
    else:
        return ResourceHandler().searchResourcesByTransactionOrder(tid, oid, request.args)

@app.route('/ResourceApp/cities/<string:cname>/keywords/<int:kid>/categories/<string:cat_name>/resources')
def getResourcesByCityKeywordCategory(cname, kid, cat_name):
    if not request.args:
        return ResourceHandler().getResourcesByCityKeywordCategory(cname, kid, cat_name)
    else:
        return ResourceHandler().searchResourcesByCityKeywordCategory(cname, kid, cat_name, request.args)

@app.route('/ResourceApp/cities/<string:cname>/keywords/<int:kid>/orders/<int:oid>/resources')
def getResourcesByCityKeywordOrder(cname, kid, oid):
    if not request.args:
        return ResourceHandler().getResourcesByCityKeywordOrder(cname, kid, oid)
    else:
        return ResourceHandler().searchResourcesByCityKeywordOrder(cname, kid, oid, request.args)

@app.route('/ResourceApp/cities/<string:cname>/categories/<string:cat_name>/orders/<int:oid>/resources')
def getResourcesByCityCategoryOrder(cname, cat_name, oid):
    if not request.args:
        return ResourceHandler().getResourcesByCityCategoryOrder(cname, cat_name, oid)
    else:
        return ResourceHandler().searchResourcesByCityCategoryOrder(cname, cat_name, oid, request.args)

@app.route('/ResourceApp/regions/<string:rname>/keywords/<int:kid>/categories/<string:cat_name>/resources')
def getResourcesByRegionKeywordCategory(rname, kid, cat_name):
    if not request.args:
        return ResourceHandler().getResourcesByRegionKeywordCategory(rname, kid, cat_name)
    else:
        return ResourceHandler().searchResourcesByRegionKeywordCategory(rname, kid, cat_name, request.args)

@app.route('/ResourceApp/regions/<string:rname>/keywords/<int:kid>/orders/<int:oid>/resources')
def getResourcesByRegionKeywordOrder(rname, kid, oid):
    if not request.args:
        return ResourceHandler().getResourcesByRegionKeywordOrder(rname, kid, oid)
    else:
        return ResourceHandler().searchResourcesByRegionKeywordOrder(rname, kid, oid, request.args)

@app.route('/ResourceApp/regions/<string:rname>/categories/<string:cat_name>/orders/<int:oid>/resources')
def getResourcesByRegionCategoryOrder(rname, cat_name, oid):
    if not request.args:
        return ResourceHandler().getResourcesByRegionCategoryOrder(rname, cat_name, oid)
    else:
        return ResourceHandler().searchResourcesByRegionCategoryOrder(rname, cat_name, oid, request.args)

@app.route('/ResourceApp/suppliers/<int:sid>/keywords/<int:kid>/categories/<string:cat_name>/resources')
def getResourcesBySupplierKeywordCategory(sid, kid, cat_name):
    if not request.args:
        return ResourceHandler().getResourcesBySupplierKeywordCategory(sid, kid, cat_name)
    else:
        return ResourceHandler().searchResourcesBySupplierKeywordCategory(sid, kid, cat_name, request.args)

@app.route('/ResourceApp/suppliers/<int:sid>/keywords/<int:kid>/orders/<int:oid>/resources')
def getResourcesBySupplierKeywordOrder(sid, kid, oid):
    if not request.args:
        return ResourceHandler().getResourcesBySupplierKeywordOrder(sid, kid, oid)
    else:
        return ResourceHandler().searchResourcesBySupplierKeywordOrder(sid, kid, oid, request.args)

@app.route('/ResourceApp/suppliers/<int:sid>/categories/<string:cat_name>/orders/<int:oid>/resources')
def getResourcesBySupplierCategoryOrder(sid, cat_name, oid):
    if not request.args:
        return ResourceHandler().getResourcesBySupplierCategoryOrder(sid, cat_name, oid)
    else:
        return ResourceHandler().searchResourcesBySupplierCategoryOrder(sid, cat_name, oid, request.args)

@app.route('/ResourceApp/keywords/<int:kid>/categories/<string:cat_name>/orders/<int:oid>/resources')
def getResourcesByKeywordCategoryOrder(kid, cat_name, oid):
    if not request.args:
        return ResourceHandler().getResourcesByKeywordCategoryOrder(kid, cat_name, oid)
    else:
        return ResourceHandler().searchResourcesByKeywordCategoryOrder(kid, cat_name, oid, request.args)

# ---------------------------------------------------------------------------- #
#                        Resource_Requested routes                             #
# ---------------------------------------------------------------------------- #

@app.route('/ResourceApp/resources_requested', methods = ['GET', 'POST']) # By rrqty, rrdescription, rr_request_date, rr_changed_date
def handleResourcesRequested():
    if request.method == 'POST':
        return ResourceRequestedHandler().insertResourceRequested(request.form)
    else:
        if not request.args:
            return ResourceRequestedHandler().getAllResourcesRequested()
        else:
            return ResourceRequestedHandler().searchResourcesRequested(request.args)

@app.route('/ResourceApp/resources_requested/<int:rrid>', methods = ['GET', 'PUT', 'DELETE'])
def handleResourceRequestedById(rrid):
    if request.method == 'GET':
        return ResourceRequestedHandler().getResourceRequestedById(rrid)
    elif request.method == 'PUT':
        return ResourceRequestedHandler().updateResourceRequested(rrid, request.form)
    elif request.method == 'DELETE':
        return ResourceRequestedHandler().deleteResourceRequested(rrid)
    else:
        return jsonify(Error = "Method not allowed."), 405

@app.route('/ResourceApp/cities/<string:cname>/resources_requested') # By rrqty, rrdescription, rr_request_date, rr_changed_date
def getResourcesRequestedByCityName(cname):
    if not request.args:
        return ResourceRequestedHandler().getResourcesRequestedByCityName(cname)
    else:
        return ResourceRequestedHandler().searchResourcesRequestedByCityName(cname, request.args)

@app.route('/ResourceApp/regions/<string:rname>/resources_requested') # By rrqty, rrdescription, rr_request_date, rr_changed_date
def getResourcesRequestedByRegionName(rname):
    if not request.args:
        return ResourceRequestedHandler().getResourcesRequestedByRegionName(rname)
    else:
        return ResourceRequestedHandler().searchResourcesRequestedByRegionName(rname, request.args)

@app.route('/ResourceApp/keywords/<int:kid>/resources_requested') # By rrqty, rrdescription, rr_request_date, rr_changed_date
def getResourcesRequestedByKeywordId(kid):
    if not request.args:
        return ResourceRequestedHandler().getResourcesRequestedByKeywordId(kid)
    else:
        return ResourceRequestedHandler().searchResourcesRequestedByKeywordId(kid, request.args)

@app.route('/ResourceApp/requesters/<int:rid>/resources_requested')
def getResourcesRequestedByRequesterId(rid):
    if not request.args:
        return ResourceRequestedHandler().getResourcesRequestedByRequesterId(rid)
    else:
        return ResourceRequestedHandler().searchResourcesRequestedByRequesterId(rid, request.args)

@app.route('/ResourceApp/categories/<string:cat_name>/resources_requested') # By rrqty, rrdescription, rr_request_date, rr_changed_date
def getResourcesRequestedByCategoryName(cat_name):
    if not request.args:
        return ResourceRequestedHandler().getResourcesRequestedByCategoryName(cat_name)
    else:
        return ResourceRequestedHandler().searchResourcesRequestedByCategoryName(cat_name, request.args)

@app.route('/ResourceApp/cities/<string:cname>/keywords/<int:kid>/resources_requested')
def getResourcesRequestedByCityKeyword(cname, kid):
    if not request.args:
        return ResourceRequestedHandler().getResourcesRequestedByCityKeyword(cname, kid)
    else:
        return ResourceRequestedHandler().searchResourcesRequestedByCityKeyword(cname, kid, request.args)

@app.route('/ResourceApp/cities/<string:cname>/categories/<string:cat_name>/resources_requested')
def getResourcesRequestedByCityCategory(cname, cay_name):
    if not request.args:
        return ResourceRequestedHandler().getResourcesRequestedByCityCategory(cname, cay_name)
    else:
        return ResourceRequestedHandler().searchResourcesRequestedByCityCategory(cname, cay_name, request.args)

@app.route('/ResourceApp/regions/<string:rname>/keywords/<int:kid>/resources_requested')
def getResourcesRequestedByRegionKeyword(rname, kid):
    if not request.args:
        return ResourceRequestedHandler().getResourcesRequestedByRegionKeyword(rname, kid)
    else:
        return ResourceRequestedHandler().searchResourcesRequestedByRegionKeyword(rname, kid, request.args)

@app.route('/ResourceApp/regions/<string:rname>/categories/<string:cat_name>/resources_requested')
def getResourcesRequestedByRegionCategory(rname, cat_name):
    if not request.args:
        return ResourceRequestedHandler().getResourcesRequestedByRegionCategory(rname, cat_name)
    else:
        return ResourceRequestedHandler().searchResourcesRequestedByRegionCategory(rname, cat_name, request.args)

@app.route('/ResourceApp/keywords/<int:kid>/requesters/<int:rid>/resources_requested')
def getResourcesRequestedByKeywordRequester(kid, rid):
    if not request.args:
        return ResourceRequestedHandler().getResourcesRequestedByKeywordRequester(kid, rid)
    else:
        return ResourceRequestedHandler().searchResourcesRequestedByKeywordRequester(kid, rid, request.args)

@app.route('/ResourceApp/keywords/<int:kid>/categories/<string:cat_name>/resources_requested')
def getResourcesRequestedByKeywordCategory(kid, cat_name):
    if not request.args:
        return ResourceRequestedHandler().getResourcesRequestedByKeywordCategory(kid, cat_name)
    else:
        return ResourceRequestedHandler().searchResourcesRequestedByKeywordCategory(kid, cat_name, request.args)

@app.route('/ResourceApp/requesters/<int:rid>/categories/<string:cat_name>/resources_requested')
def getResourcesRequestedByRequesterCategory(rid, cat_name):
    if not request.args:
        return ResourceRequestedHandler().getResourcesRequestedByRequesterCategory(rid, cat_name)
    else:
        return ResourceRequestedHandler().searchResourcesRequestedByRequesterCategory(rid, cat_name, request.args)

@app.route('/ResourceApp/cities/<string:cname>/keywords/<int:kid>/categories/<string:cat_name>/resources_requested')
def getResourcesRequestedByCityKeywordCategory(cname, kid, cat_name):
    if not request.args:
        return ResourceRequestedHandler().getResourcesRequestedByCityKeywordCategory(cname, kid, cat_name)
    else:
        return ResourceRequestedHandler().searchResourcesRequestedByCityKeywordCategory(cname, kid, cat_name, request.args)

@app.route('/ResourceApp/regions/<string:rname>/keywords/<int:kid>/categories/<string:cat_name>/resources_requested')
def getResourcesRequestedByRegionKeywordCategory(rname, kid, cat_name):
    if not request.args:
        return ResourceRequestedHandler().getResourcesRequestedByRegionKeywordCategory(rname, kid, cat_name)
    else:
        return ResourceRequestedHandler().searchResourcesRequestedByRegionKeywordCategory(rname, kid, cat_name, request.args)

@app.route('/ResourceApp/keywords/<int:kid>/requesters/<int:rid>/categories/<string:cat_name>/resources_requested')
def getResourcesRequestedByKeywordRequesterCategory(kid, rid, cat_name):
    if not request.args:
        return ResourceRequestedHandler().getResourcesRequestedByKeywordRequesterCategory(kid, rid, cat_name)
    else:
        return ResourceRequestedHandler().searchResourcesRequestedByKeywordRequesterCategory(kid, rid, cat_name, request.args)


# ---------------------------------------------------------------------------- #
#                               Keyword routes                                 #
# ---------------------------------------------------------------------------- #

@app.route('/ResourceApp/keywords', methods = ['GET', 'POST']) # By keyword
def handleKeywords():
    if request.method == 'POST':
        return KeywordHandler().insertKeyword(request.form)
    else:
        if not request.args:
            return KeywordHandler().getAllKeywords()
        else:
            return KeywordHandler().searchKeywords(request.args)

@app.route('/ResourceApp/keywords/<int:kid>', methods = ['GET', 'PUT', 'DELETE'])
def handleKeywordById(kid):
    if request.method == 'GET':
        return KeywordHandler().getKeywordById(kid)
    elif request.method == 'PUT':
        return KeywordHandler().updateKeyword(kid, request.form)
    elif request.method == 'DELETE':
        return KeywordHandler().deleteKeyword(kid)
    else:
        return jsonify(Error = "Method not allowed."), 405

@app.route('/ResourceApp/resources/<int:rsid>/keywords') # By keyword
def getKeywordsByResourceId(rsid):
    if not request.args:
        return KeywordHandler().getKeywordsByResourceId(rsid)
    else:
        return KeywordHandler().searchKeywordsByResourceId(rsid, request.args)

@app.route('/ResourceApp/resources_requested/<int:rrid>/keywords') # By keyword
def getKeywordsByResourceRequestedId(rrid):
    if not request.args:
        return KeywordHandler().getKeywordsByResourceRequestedId(rrid)
    else:
        return KeywordHandler().searchKeywordsByResourceRequestedId(rrid, request.args)

@app.route('/ResourceApp/categories/<string:cat_name>/keywords')
def getKeywordsByCategoryName(cat_name):
    if not request.args:
        return KeywordHandler().getKeywordsByCategoryName(cat_name)
    else:
        return KeywordHandler().searchKeywordsByCategoryName(cat_name, request.args)

# ---------------------------------------------------------------------------- #
#                              Category routes                                 #
# ---------------------------------------------------------------------------- #

@app.route('/ResourceApp/categories', methods = ['GET', 'POST'])
def handleCategories():
    if request.method == 'POST':
        return CategoryHandler().insertCategory(request.form)
    else:
        if not request.args:
            return CategoryHandler().getAllCategories()
        else:
            return CategoryHandler().searchCategories(request.args)

@app.route('/ResourceApp/categories/<string:cat_name>', methods = ['GET', 'PUT', 'DELETE'])
def handleCategoryById(cat_name):
    if request.method == 'GET':
        return CategoryHandler().getCategoryById(cat_name)
    elif request.method == 'PUT':
        return CategoryHandler().updateCategory(cat_name, request.form)
    elif request.method == 'DELETE':
        return CategoryHandler().deleteCategory(cat_name)
    else:
        return jsonify(Error = "Method not allowed."), 405

@app.route('/ResourceApp/cities/<string:cname>/categories')
def getCategoriesByCityName(cname):
    if not request.args:
        return CategoryHandler().getCategoriesByCityName(cname)
    else:
        return CategoryHandler().searchCategoriesByCityName(cname, request.args)

@app.route('/ResourceApp/regions/<string:rname>/categories')
def getCategoriesByRegionName(rname):
    if not request.args:
        return CategoryHandler().getCategoriesByRegionName(rname)
    else:
        return CategoryHandler().searchCategoriesByRegionName(rname, request.args)

@app.route('/ResourceApp/resources/<int:rsid>/categories')
def getCategoriesByResourceId(rsid):
    if not request.args:
        return CategoryHandler().getCategoriesByResourceId(rsid)
    else:
        return CategoryHandler().searchCategoriesByResourceId(rsid, request.args)

@app.route('/ResourceApp/keywords/<int:kid>/categories')
def getCategoriesByKeywordId(kid):
    if not request.args:
        return CategoryHandler().getCategoriesByKeywordId(kid)
    else:
        return CategoryHandler().searchCategoriesByKeywordId(kid, request.args)

@app.route('/ResourceApp/resources_requested/<int:rrid>/categories')
def getCategoriesByResourceRequestedId(rrid):
    if not request.args:
        return CategoryHandler().getCategoriesByResourceRequestedId(rrid)
    else:
        return CategoryHandler().searchCategoriesByResourceRequestedId(rrid, request.args)

@app.route('/ResourceApp/categories/<string:cat_name>/categories')
def getCategoriesByCategoryName(cat_name):
    if not request.args:
        return CategoryHandler().getCategoriesByCategoryName(cat_name)
    else:
        return CategoryHandler().searchCategoriesByCategoryName(cat_name, request.args)

@app.route('/ResourceApp/transactions/<int:tid>/categories')
def getCategoriesByTransactionId(tid):
    if not request.args:
        return CategoryHandler().getCategoriesByTransactionId(tid)
    else:
        return CategoryHandler().searchCategoriesByTransactionId(tid, request.args)

# ---------------------------------------------------------------------------- #
#                            Transaction routes                                #
# ---------------------------------------------------------------------------- #



# ---------------------------------------------------------------------------- #
#                            Credit_Card routes                                #
# ---------------------------------------------------------------------------- #



# ---------------------------------------------------------------------------- #
#                              Payment routes                                  #
# ---------------------------------------------------------------------------- #



if __name__ == '__main__':
    app.run()
