from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return jsonify(Welcome = 'Hello, this is the Disaster-Site-Resources-Locator project.')

# ---------------------------------------------------------------------------- #
#                                City routes                                   #
# ---------------------------------------------------------------------------- #

@app.route('/ResourceApp/cities/<string:cname>/resources') # By rname, rprice, rqty, rdescription, r_supply_date, r_changed_date
def getResourcesByCityName(cname):
    return CityHandler().getResourcesByCityName(cname)

@app.route('/ResourceApp/cities/<string:cname>/resources_requested') # By rrqty, rrdescription, rr_request_date, rr_changed_date
def getResourcesRequestedByCityName(cname):
    return CityHandler().getResourcesRequestedByCityName(cname)

# ---------------------------------------------------------------------------- #
#                               Region routes                                  #
# ---------------------------------------------------------------------------- #

@app.route('/ResourceApp/regions/<string:rname>/resources') # By rname, rprice, rqty, rdescription, r_supply_date, r_changed_date
def getResourcesByRegionName(rname):
    return RegionHandler().getResourcesByRegionName(rname)

@app.route('/ResourceApp/regions/<string:rname>/resources_requested') # By rrqty, rrdescription, rr_request_date, rr_changed_date
def getResourcesRequestedByRegionName(rname):
    return RegionHandler().getResourcesRequestedByRegionName(rname)

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

@app.route('/ResourceApp/resources/<int:rsid>' methods = ['GET', 'PUT', 'DELETE'])
def handleResourceById(rsid):
    if request.method == 'GET':
        return ResourceHandler().getResourceById(rsid)
    elif request.method == 'PUT':
        return ResourceHandler().updateResource(rsid, request.form)
    elif request.method == 'DELETE':
        return ResourceHandler().deleteResource(rsid)
    else:
        return jsonify(Error = "Method not allowed."), 405

@app.route('/ResourceApp/resources/<int:rsid>/keywords') # By keyword
def getKeywordsByResourceId(rsid):
    return ResourceHandler().getKeywordsByResourceId(rsid)

@app.route('/ResourceApp/resources/<int:rsid>/categories')
def getCategoriesByResourceId(rsid):
    return ResourceHandler().getCategoriesByResourceId(rsid)

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

@app.route('/ResourceApp/resources_requested/<int:rrid>' methods = ['GET', 'PUT', 'DELETE'])
def handleResourceRequestedById(rrid):
    if request.method == 'GET':
        return ResourceRequestedHandler().getResourceRequestedById(rrid)
    elif request.method == 'PUT':
        return ResourceRequestedHandler().updateResourceRequested(rrid, request.form)
    elif request.method == 'DELETE':
        return ResourceRequestedHandler().deleteResourceRequested(rrid)
    else:
        return jsonify(Error = "Method not allowed."), 405

@app.route('/ResourceApp/resources_requested/<int:rrid>/keywords') # By keyword
def getKeywordsByResourceRequestedId(rrid):
    return ResourceRequestedHandler().getKeywordsByResourceRequestedId(rrid)

@app.route('/ResourceApp/resources_requested/<int:rrid>/categories')
def getCategoriesByResourceRequestedId(rrid):
    return ResourceRequestedHandler().getCategoriesByResourceRequestedId(rrid)

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

@app.route('/ResourceApp/keywords/<int:kid>/resources') # By rname, rprice, rqty, rdescription, r_supply_date, r_changed_date
def getResourcesByKeywordId(kid):
    return KeywordHandler().getResourcesByKeywordId(kid)

@app.route('/ResourceApp/keywords/<int:kid>/resources_requested') # By rrqty, rrdescription, rr_request_date, rr_changed_date
def getResourcesRequestedByKeywordId(kid):
    return KeywordHandler().getResourcesRequestedByKeywordId(kid)

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

@app.route('/ResourceApp/categories/<string:cat_name>/resources') # By rname, rprice, rqty, rdescription, r_supply_date, r_changed_date
def getResourcesByCategoryName(cat_name):
    return CategoryHandler().getResourcesByCategoryName(cat_name)

@app.route('/ResourceApp/categories/<string:cat_name>/resources_requested') # By rrqty, rrdescription, rr_request_date, rr_changed_date
def getResourcesRequestedByCategoryName(cat_name):
    return CategoryHandler().getResourcesRequestedByCategoryName(cat_name)

@app.route('/ResourceApp/categories/<string:cat_name>/categories')
def getCategoriesByCategoryName(cat_name):
    return CategoryHandler().getCategoriesByCategoryName(cat_name)

# ---------------------------------------------------------------------------- #
#                            Transaction routes                                #
# ---------------------------------------------------------------------------- #

@app.route('/ResourceApp/transactions/<int:tid>/resources') # By rname, rprice, rqty, rdescription, r_supply_date, r_changed_date
def getResourcesByTransactionId(tid):
    return TransactionHandler().getResourcesByTransactionId(tid)

@app.route('/ResourceApp/transactions/<int:tid>/categories')
def getCategoriesByTransactionId(tid):
    return TransactionHandler().getCategoriesByTransactionId(tid)

# ---------------------------------------------------------------------------- #
#                            Credit_Card routes                                #
# ---------------------------------------------------------------------------- #



# ---------------------------------------------------------------------------- #
#                              Payment routes                                  #
# ---------------------------------------------------------------------------- #



if __name__ == '__main__':
    app.run()
