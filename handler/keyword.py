from flask import Flask, jsonify
from dao.keyword import KeywordDAO
from dao.resource import ResourceDAO
from dao.resource_requested import ResourceRequestedDAO
from dao.category import CategoryDAO

class KeywordHandler:

    def build_keyword_dict(self, row):
        result = {}
        result['kid'] = row[0]
        result['keyword'] = row[1]
        return result

    def build_keyword_attributes(self, kid, keyword):
        result = {}
        result['kid'] = kid
        result['keyword'] = keyword
        return result

    def getAllKeywords(self):
        dao = KeywordDAO()
        keyword_list = dao.getAllKeywords()
        result_list = []
        for row in keyword_list:
            result = self.build_keyword_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error = "Keywords Not Found"), 404
        else:
            return jsonify(Keywords = result_list)

    def searchKeywords(self, args):
        keyword = args.get('keyword')
        dao = KeywordDAO()
        keyword_list = []
        if (len(args) == 1) and keyword:
            keyword_list = dao.getKeywordsByKeyword(keyword)
        else:
            return jsonify(Error = "Malformed Query String"), 400
        result_list = []
        for row in keyword_list:
            result = self.build_keyword_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error = "Keyword Not Found"), 404
        else:
            return jsonify(Keywords = result_list)

    def getKeywordById(self, kid):
        dao = KeywordDAO()
        keyword = dao.getKeywordById(kid)
        if not keyword:
            return jsonify(Error = "Keyword Not Found"), 404
        else:
            result = self.build_keyword_dict(keyword)
            return jsonify(Keyword = result)

    def insertKeyword(self, form):
        if len(form) != 1:
            return jsonify(Error = "Malformed Post Request"), 400
        else:
            keyword = form['keyword']
            if keyword:
                dao = KeywordDAO()
                kid = dao.insert(keyword)
                result = self.build_keyword_attributes(kid, keyword)
                return jsonify(Keyword = result), 201
            else:
                return jsonify(Error = "Unexpected attributes in post request"), 400

    def updateKeyword(self, kid, form):
        dao = KeywordDAO()
        if not dao.getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        else:
            if len(form) != 1:
                return jsonify(Error = "Malformed Update Request"), 400
            else:
                keyword = form['keyword']
                if keyword:
                    dao.update(kid, keyword)
                    result = self.build_keyword_attributes(kid, keyword)
                    return jsonify(Keyword = result), 200
                else:
                    return jsonify(Error = "Unexpected attributes in update request"), 400

    def deleteKeyword(self, kid):
        dao = KeywordDAO()
        if not dao.getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        else:
            dao.delete(kid)
            return jsonify(DeleteStatus = "OK"), 200

    def getKeywordsByResourceId(self, rsid):
        if not ResourceDAO().getResourceById(rsid):
            return jsonify(Error = "Resource Not Found"), 404
        else:
            keyword_list = KeywordDAO().getKeywordsByResourceId(rsid)
            result_list = []
            for row in keyword_list:
                result = self.build_keyword_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Keywords Not Found"), 404
            else:
                return jsonify(Keywords = result_list)

    def searchKeywordsByResourceId(self, rsid, args):
        if not ResourceDAO().getResourceById(rsid):
            return jsonify(Error = "Resource Not Found"), 404
        else:
            keyword = args.get('keyword')
            dao = KeywordDAO()
            keyword_list = []
            if (len(args) == 1) and keyword:
                keyword_list = dao.getKeywordsByResourceIdByKeyword(rsid, keyword)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in keyword_list:
                result = self.build_keyword_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Keyword Not Found"), 404
            else:
                return jsonify(Keywords = result_list)

    def getKeywordsByResourceRequestedId(self, rrid):
        if not ResourceRequestedDAO().getResourceRequestedById(rrid):
            return jsonify(Error = "ResourceRequested Not Found"), 404
        else:
            keyword_list = KeywordDAO().getKeywordsByResourceRequestedId(rrid)
            result_list = []
            for row in keyword_list:
                result = self.build_keyword_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Keywords Not Found"), 404
            else:
                return jsonify(Keywords = result_list)

    def searchKeywordsByResourceRequestedId(self, rrid, args):
        if not ResourceRequestedDAO().getResourceRequestedById(rrid):
            return jsonify(Error = "ResourceRequested Not Found"), 404
        else:
            keyword = args.get('keyword')
            dao = KeywordDAO()
            keyword_list = []
            if (len(args) == 1) and keyword:
                keyword_list = dao.getKeywordsByResourceRequestedIdByKeyword(rrid, keyword)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in keyword_list:
                result = self.build_keyword_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Keyword Not Found"), 404
            else:
                return jsonify(Keywords = result_list)

    def getKeywordsByCategoryName(self, cat_name):
        if not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            keyword_list = KeywordDAO().getKeywordsByCategoryName(cat_name)
            result_list = []
            for row in keyword_list:
                result = self.build_keyword_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Keywords Not Found"), 404
            else:
                return jsonify(Keywords = result_list)

    def searchKeywordsByCategoryName(self, cat_name, args):
        if not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            keyword = args.get('keyword')
            dao = KeywordDAO()
            keyword_list = []
            if (len(args) == 1) and keyword:
                keyword_list = dao.getKeywordsByCategoryNameByKeyword(cat_name, keyword)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in keyword_list:
                result = self.build_keyword_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Keyword Not Found"), 404
            else:
                return jsonify(Keywords = result_list)
