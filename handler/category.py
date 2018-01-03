from flask import Flask, jsonify

class CategoryHandler:

    def build_category_dict(self, row):
        result = {}
        result['cat_name'] = row[0]
        return result

    def build_category_attributes(self, cat_name):
        result = {}
        result['cat_name'] = cat_name
        return result

    def getAllCategories(self):
        dao = CategoryDAO()
        category_list = dao.getAllCategories()
        result_list = []
        for row in category_list:
            result = self.build_category_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error = "Categories Not Found"), 404
        else:
            return jsonify(Categories = result_list)

    def searchCategories(self, args):
        pass

    def getCategoryByName(self, cat_name):
        dao = CategoryDAO()
        category = dao.getCategoryByName(cat_name)
        if not category:
            return jsonify(Error = "Category Not Found"), 404
        else:
            result = self.build_category_dict(category)
            return jsonify(Category = result)

    def insertCategory(self, form):
        dao = CategoryDAO()
        if len(form) != 1:
            return jsonify(Error = "Malformed Post Request"), 400
        else:
            cat_name = form['cat_name']
            if cat_name:
                if not dao.getCategoryByName(cat_name):
                    dao.insert(cat_name)
                    result = self.build_category_attributes(cat_name)
                    return jsonify(Category = result), 201
                else:
                    return jsonify(Error = "Category already exists")
            else:
                return jsonify(Error = "Unexpected attributes in post request"), 400

    def updateCategory(self, cat_name, form):
        dao = CategoryDAO()
        if not dao.getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            cat_name = form['cat_name']
            if cat_name:
                dao.updateCategory(cat_name)
                result = self.build_category_attributes(cat_name)
                return jsonify(Category = result), 201
            else:
                return jsonify(Error = "Unexpected attributes in post request"), 400

    def deleteCategory(self, cat_name):
        dao = CategoryDAO()
        if not dao.getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            dao.delete(cat_name)
            return jsonify(DeleteStatus = "OK"), 200

    def getCategoriesByCityName(self, cname):
        if not CityDAO().getCityByName(cname):
            return jsonify(Error = "City Not Found"), 404
        else:
            category_list = CategoryDAO().getCategoriesByCityName(cname)
            result_list = []
            for row in category_list:
                result = self.build_category_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Categories Not Found"), 404
            else:
                return jsonify(Categories = result_list)

    def searchCategoriesByCityName(self, cname, args):
        pass

    def getCategoriesByRegionName(self, rname):
        if not RegionDAO().getRegionByName(rname):
            return jsonify(Error = "Region Not Found"), 404
        else:
            category_list = CategoryDAO().getCategoriesByRegionName(rname)
            result_list = []
            for row in category_list:
                result = self.build_category_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Categories Not Found"), 404
            else:
                return jsonify(Categories = result_list)

    def searchCategoriesByRegionName(self, rname, args):
        pass

    def getCategoriesByResourceId(self, rsid):
        if not ResourceDAO().getResourceById(rsid):
            return jsonify(Error = "Resource Not Found"), 404
        else:
            category_list = CategoryDAO().getCategoriesByResourceId(rsid)
            result_list = []
            for row in category_list:
                result = self.build_category_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Categories Not Found"), 404
            else:
                return jsonify(Categories = result_list)

    def searchCategoriesByResourceId(self, rsid, args):
        pass

    def getCategoriesByKeywordId(self, kid):
        if not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        else:
            category_list = CategoryDAO().getCategoriesByKeywordId(kid)
            result_list = []
            for row in category_list:
                result = self.build_category_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Categories Not Found"), 404
            else:
                return jsonify(Categories = result_list)

    def searchCategoriesByKeywordId(self, kid, args):
        pass

    def getCategoriesByResourceRequestedId(self, rrid):
        if not ResourceRequestedDAO().getResourceRequestedById(rrid):
            return jsonify(Error = "ResourceRequested Not Found"), 404
        else:
            category_list = CategoryDAO().getCategoriesByResourceRequestedId(rrid)
            result_list = []
            for row in category_list:
                result = self.build_category_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Categories Not Found"), 404
            else:
                return jsonify(Categories = result_list)

    def searchCategoriesByResourceRequestedId(self, rrid, args):
        pass

    def getCategoriesByCategoryName(self, cat_name):
        if not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            category_list = CategoryDAO().getCategoriesByCategoryName(cat_name)
            result_list = []
            for row in category_list:
                result = self.build_category_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Categories Not Found"), 404
            else:
                return jsonify(Categories = result_list)

    def searchCategoriesByCategoryName(self, cat_name, args):
        pass

    def getCategoriesByTransactionId(self, tid):
        if not TransactionDAO().getTransactionById(tid):
            return jsonify(Error = "Transaction Not Found"), 404
        else:
            category_list = CategoryDAO().getCategoriesByTransactionId(tid)
            result_list = []
            for row in category_list:
                result = self.build_category_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Categories Not Found"), 404
            else:
                return jsonify(Categories = result_list)

    def searchCategoriesByTransactionId(self, tid, args):
        pass
