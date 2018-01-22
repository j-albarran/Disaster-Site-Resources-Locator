from flask import jsonify
from dao.cash import CashDAO


class CashesHandler:
    def build_cashes_dict(self, row):
        result = {}
        result['cashid'] = row[0]
        return result

    def build_cashes_attributes(self, cashid):
        result = {}
        result['cashid'] = cashid
        return result

    def getAllCashes(self):
        dao = CashDAO()
        cashes_list = dao.getAllCashes()
        result_list = []
        for row in cashes_list:
            result = self.build_cashes_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Cash Not Found"), 404
        else:
            return jsonify(Cashes=result_list)

    def getCashesById(self, cashid):
        dao = CashDAO()
        cashes_list = dao.getCashById(cashid)
        result_list = []
        for row in cashes_list:
            result = self.build_cashes_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Cash Not Found"), 404
        else:
            return jsonify(Cashes=result_list)

    def insertCash(self, form):
        if len(form) != 1:
            return jsonify(Error="Malformed post request"), 400
        else:
            dao = CashDAO()
            rid = form['rid']
            cashid = dao.insertCash(rid)
            result = self.build_cashes_attributes(cashid)
            return jsonify(Cash=result), 201

    def deleteCash(self, cashid):
        dao = CashDAO()
        if not dao.getCashById(cashid):
            return jsonify(Error="Cash not found."), 404
        else:
            dao.deleteCash(cashid)
            return jsonify(DeleteStatus="OK"), 200

    def getCashesByTransaction(self, tid):
        dao = CashDAO()
        cashes_list = dao.getCashesByTransaction(tid)
        result_list = []
        for row in cashes_list:
            result = self.build_cashes_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Cash Not Found"), 404
        else:
            return jsonify(Cashes=result_list)

    def getCashesByRequester(self, rid):
        dao = CashDAO()
        cashes_list = dao.getCashesByRequester(rid)
        result_list = []
        for row in cashes_list:
            result = self.build_cashes_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Cash Not Found"), 404
        else:
            return jsonify(Cashes=result_list)

    def getCashesByOrder(self, oid):
        dao = CashDAO()
        cashes_list = dao.getCashesByOrder(oid)
        result_list = []
        for row in cashes_list:
            result = self.build_cashes_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Cash Not Found"), 404
        else:
            return jsonify(Cashes=result_list)

    def build_cash_attributes(self, cashid):
        pass