from flask import jsonify
from dao.transaction import TransactionDAO


class TransactionsHandler:
    def build_transaction_dict(self, row):
        result = {}
        # tid, tprice, tqty, tdate, tstatus
        result['tid'] = row[0]
        result['tprice'] = row[1]
        result['tqty'] = row[2]
        result['tdate'] = row[3]
        result['tstatus'] = row[4]
        return result

    def getTransaction(self, tid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionById(tid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    @property
    def getAllTransactions(self):
        dao = TransactionDAO()
        transactions_list = dao.getAllTransactions()
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchAllTransactions(self, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByPriceQtyDateStatus(price, qty, date, status)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByPriceQtyDate(price, qty, date)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByPriceQtyStatus(price, qty, status)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByPriceDateStatus(price, date, status)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByQtyDateStatus(qty, date, status)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByPriceQty(price, qty)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByPriceDate(price, date)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByPriceStatus(price, status)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByQtyDate(qty, date)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByQtyStatus(qty, status)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByDateStatus(date, status)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByPrice(price)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByQty(qty)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByDate(date)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByStatus(status)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByRegion(self, rname):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByRegion(rname)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByRegion(self, rname, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionPriceQtyDateStatus(price, qty, date, status, rname)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByRegionPriceQtyDate(price, qty, date, rname)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByRegionPriceQtyStatus(price, qty, status, rname)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByRegionPriceDateStatus(price, date, status, rname)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionQtyDateStatus(qty, date, status, rname)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByRegionPriceQty(price, qty, rname)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByRegionPriceDate(price, date, rname)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByRegionPriceStatus(price, status, rname)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByRegionQtyDate(qty, date, rname)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByRegionQtyStatus(qty, status, rname)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByRegionDateStatus(date, status, rname)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByRegionPrice(price, rname)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByRegionQty(qty, rname)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByRegionDate(date, rname)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByRegionStatus(status, rname)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByCity(self, cname):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByCity(cname)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByCity(self, cname, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByCityPriceQtyDateStatus(price, qty, date, status, cname)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByCityPriceQtyDate(price, qty, date, cname)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByCityPriceQtyStatus(price, qty, status, cname)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByCityPriceDateStatus(price, date, status, cname)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByCityQtyDateStatus(qty, date, status, cname)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByCityPriceQty(price, qty, cname)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByCityPriceDate(price, date, cname)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByCityPriceStatus(price, status, cname)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByCityQtyDate(qty, date, cname)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByCityQtyStatus(qty, status, cname)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByCityDateStatus(date, status, cname)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByCityPrice(price, cname)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByCityQty(qty, cname)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByCityDate(date, cname)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByCityStatus(status, cname)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsBySupplier(self, sid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsBySupplier(sid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsBySupplier(self, sid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsBySupplierPriceQtyDateStatus(price, qty, date, status, sid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsBySupplierPriceQtyDate(price, qty, date, sid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsBySupplierPriceQtyStatus(price, qty, status, sid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsBySupplierPriceDateStatus(price, date, status, sid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsBySupplierQtyDateStatus(qty, date, status, sid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsBySupplierPriceQty(price, qty, sid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsBySupplierPriceDate(price, date, sid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsBySupplierPriceStatus(price, status, sid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsBySupplierQtyDate(qty, date, sid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsBySupplierQtyStatus(qty, status, sid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsBySupplierDateStatus(date, status, sid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsBySupplierPrice(price, sid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsBySupplierQty(qty, sid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsBySupplierDate(date, sid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsBySupplierStatus(status, sid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactiosbyRequester(self, rid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByRequester(rid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactiosbyRequester(self, rid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByRequesterPriceQtyDateStatus(price, qty, date, status, rid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByRequesterPriceQtyDate(price, qty, date, rid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByRequesterPriceQtyStatus(price, qty, status, rid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByRequesterPriceDateStatus(price, date, status, rid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByRequesterQtyDateStatus(qty, date, status, rid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByRequesterPriceQty(price, qty, rid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByRequesterPriceDate(price, date, rid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByRequesterPriceStatus(price, status, rid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByRequesterQtyDate(qty, date, rid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByRequesterQtyStatus(qty, status, rid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByRequesterDateStatus(date, status, rid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByRequesterPrice(price, rid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByRequesterQty(qty, rid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByRequesterDate(date, rid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByRequesterStatus(status, rid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByResource(self, rsid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByResource(rsid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByResource(self, rsid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByResourcePriceQtyDateStatus(price, qty, date, status, rsid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByResourcePriceQtyDate(price, qty, date, rsid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByResourcePriceQtyStatus(price, qty, status, rsid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByResourcePriceDateStatus(price, date, status, rsid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByResourceQtyDateStatus(qty, date, status, rsid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByResourcePriceQty(price, qty, rsid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByResourcePriceDate(price, date, rsid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByResourcePriceStatus(price, status, rsid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByResourceQtyDate(qty, date, rsid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByResourceQtyStatus(qty, status, rsid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByResourceDateStatus(date, status, rsid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByResourcePrice(price, rsid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByResourceQty(qty, rsid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByResourceDate(date, rsid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByResourceStatus(status, rsid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByKeyword(self, kid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByKeyword(kid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByKeyword(self, kid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByKeywordPriceQtyDateStatus(price, qty, date, status, kid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByKeywordPriceQtyDate(price, qty, date, kid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByKeywordPriceQtyStatus(price, qty, status, kid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByKeywordPriceDateStatus(price, date, status, kid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByKeywordQtyDateStatus(qty, date, status, kid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByKeywordPriceQty(price, qty, kid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByKeywordPriceDate(price, date, kid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByKeywordPriceStatus(price, status, kid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByKeywordQtyDate(qty, date, kid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByKeywordQtyStatus(qty, status, kid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByKeywordDateStatus(date, status, kid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByKeywordPrice(price, kid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByKeywordQty(qty, kid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByKeywordDate(date, kid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByKeywordStatus(status, kid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByCategory(self, cat_name, cat_pname):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByCategory(cat_name, cat_pname)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByCategory(self, cat_name, cat_pname, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByCategoryPriceQtyDateStatus(price, qty, date, status, cat_name,
                                                                                   cat_pname)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByCategoryPriceQtyDate(price, qty, date, cat_name, cat_pname)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByCategoryPriceQtyStatus(price, qty, status, cat_name, cat_pname)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByCategoryPriceDateStatus(price, date, status, cat_name,
                                                                                cat_pname)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByCategoryQtyDateStatus(qty, date, status, cat_name, cat_pname)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByCategoryPriceQty(price, qty, cat_name, cat_pname)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByCategoryPriceDate(price, date, cat_name, cat_pname)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByCategoryPriceStatus(price, status, cat_name, cat_pname)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByCategoryQtyDate(qty, date, cat_name, cat_pname)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByCategoryQtyStatus(qty, status, cat_name, cat_pname)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByCategoryDateStatus(date, status, cat_name, cat_pname)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByCategoryPrice(price, cat_name, cat_pname)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByCategoryQty(qty, cat_name, cat_pname)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByCategoryDate(date, cat_name, cat_pname)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByCategoryStatus(status, cat_name, cat_pname)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByOrder(self, oid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByOrder(oid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByOrder(self, oid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByOrderPriceQtyDateStatus(price, qty, date, status, oid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByOrderPriceQtyDate(price, qty, date, oid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByOrderPriceQtyStatus(price, qty, status, oid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByOrderPriceDateStatus(price, date, status, oid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByOrderQtyDateStatus(qty, date, status, oid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByOrderPriceQty(price, qty, oid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByOrderPriceDate(price, date, oid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByOrderPriceStatus(price, status, oid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByOrderQtyDate(qty, date, oid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByOrderQtyStatus(qty, status, oid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByOrderDateStatus(date, status, oid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByOrderPrice(price, oid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByOrderQty(qty, oid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByOrderDate(date, oid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByOrderStatus(status, oid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByCreditCard(self, cid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByCreditCard(cid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByCreditCard(self, cid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByCreditCardPriceQtyDateStatus(price, qty, date, status, cid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByCreditCardPriceQtyDate(price, qty, date, cid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByCreditCardPriceQtyStatus(price, qty, status, cid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByCreditCardPriceDateStatus(price, date, status, cid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByCreditCardQtyDateStatus(qty, date, status, cid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByCreditCardPriceQty(price, qty, cid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByCreditCardPriceDate(price, date, cid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByCreditCardPriceStatus(price, status, cid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByCreditCardQtyDate(qty, date, cid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByCreditCardQtyStatus(qty, status, cid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByCreditCardDateStatus(date, status, cid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByCreditCardPrice(price, cid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByCreditCardQty(qty, cid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByCreditCardDate(date, cid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByCreditCardStatus(status, cid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByPayment(self, payid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByPayment(payid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByPayment(self, payid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByPaymentPriceQtyDateStatus(price, qty, date, status, payid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByPaymentPriceQtyDate(price, qty, date, payid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByPaymentPriceQtyStatus(price, qty, status, payid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByPaymentPriceDateStatus(price, date, status, payid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByPaymentQtyDateStatus(qty, date, status, payid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByPaymentPriceQty(price, qty, payid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByPaymentPriceDate(price, date, payid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByPaymentPriceStatus(price, status, payid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByPaymentQtyDate(qty, date, payid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByPaymentQtyStatus(qty, status, payid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByPaymentDateStatus(date, status, payid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByPaymentPrice(price, payid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByPaymentQty(qty, payid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByPaymentDate(date, payid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByPaymentStatus(status, payid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByRegionSupplier(self, rname, sid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByRegionSupplier(rname, sid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByRegionSupplier(self, rname, sid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierPriceQtyDateStatus(price, qty, date, status,
                                                                                         rname, sid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByRegionSupplierPriceQtyDate(price, qty, date, rname, sid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierPriceQtyStatus(price, qty, status, rname, sid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierPriceDateStatus(price, date, status, rname, sid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierQtyDateStatus(qty, date, status, rname, sid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByRegionSupplierPriceQty(price, qty, rname, sid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByRegionSupplierPriceDate(price, date, rname, sid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierPriceStatus(price, status, rname, sid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByRegionSupplierQtyDate(qty, date, rname, sid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierQtyStatus(qty, status, rname, sid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierDateStatus(date, status, rname, sid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByRegionSupplierPrice(price, rname, sid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByRegionSupplierQty(qty, rname, sid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByRegionSupplierDate(date, rname, sid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierStatus(status, rname, sid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByRegionRequester(self, rname, rid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByRegionRequester(rname, rid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByRegionRequester(self, rname, rid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterPriceQtyDateStatus(price, qty, date, status,
                                                                                          rname, rid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByRegionRequesterPriceQtyDate(price, qty, date, rname, rid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterPriceQtyStatus(price, qty, status, rname, rid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterPriceDateStatus(price, date, status, rname, rid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterQtyDateStatus(qty, date, status, rname, rid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByRegionRequesterPriceQty(price, qty, rname, rid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByRegionRequesterPriceDate(price, date, rname, rid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterPriceStatus(price, status, rname, rid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByRegionRequesterQtyDate(qty, date, rname, rid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterQtyStatus(qty, status, rname, rid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterDateStatus(date, status, rname, rid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByRegionRequesterPrice(price, rname, rid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByRegionRequesterQty(qty, rname, rid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByRegionRequesterDate(date, rname, rid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterStatus(status, rname, rid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByRegionResource(self, rname, rsid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByRegionResource(rname, rsid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByRegionResource(self, rname, rsid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionResourcePriceQtyDateStatus(price, qty, date, status,
                                                                                         rname, rsid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByRegionResourcePriceQtyDate(price, qty, date, rname, rsid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByRegionResourcePriceQtyStatus(price, qty, status, rname, rsid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByRegionResourcePriceDateStatus(price, date, status, rname, rsid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionResourceQtyDateStatus(qty, date, status, rname, rsid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByRegionResourcePriceQty(price, qty, rname, rsid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByRegionResourcePriceDate(price, date, rname, rsid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByRegionResourcePriceStatus(price, status, rname, rsid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByRegionResourceQtyDate(qty, date, rname, rsid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByRegionResourceQtyStatus(qty, status, rname, rsid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByRegionResourceDateStatus(date, status, rname, rsid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByRegionResourcePrice(price, rname, rsid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByRegionResourceQty(qty, rname, rsid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByRegionResourceDate(date, rname, rsid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByRegionResourceStatus(status, rname, rsid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByRegionKeyword(self, rname, kid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByRegionKeyword(rname, kid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByRegionKeyword(self, rname, kid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionKeywordPriceQtyDateStatus(price, qty, date, status, rname,
                                                                                        kid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByRegionKeywordPriceQtyDate(price, qty, date, rname, kid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByRegionKeywordPriceQtyStatus(price, qty, status, rname, kid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByRegionKeywordPriceDateStatus(price, date, status, rname, kid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionKeywordQtyDateStatus(qty, date, status, rname, kid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByRegionKeywordPriceQty(price, qty, rname, kid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByRegionKeywordPriceDate(price, date, rname, kid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByRegionKeywordPriceStatus(price, status, rname, kid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByRegionKeywordQtyDate(qty, date, rname, kid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByRegionKeywordQtyStatus(qty, status, rname, kid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByRegionKeywordDateStatus(date, status, rname, kid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByRegionKeywordPrice(price, rname, kid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByRegionKeywordQty(qty, rname, kid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByRegionKeywordDate(date, rname, kid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByRegionKeywordStatus(status, rname, kid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByRegionCategory(self, rname, cat_name, cat_pname):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByRegionCategory(rname, cat_name, cat_pname)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByRegionCategory(self, rname, cat_name, cat_pname, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionCategoryPriceQtyDateStatus(price, qty, date, status,
                                                                                         rname, cat_name, cat_pname)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByRegionCategoryPriceQtyDate(price, qty, date, rname, cat_name,
                                                                                   cat_pname)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByRegionCategoryPriceQtyStatus(price, qty, status, rname,
                                                                                     cat_name, cat_pname)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByRegionCategoryPriceDateStatus(price, date, status, rname,
                                                                                      cat_name, cat_pname)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionCategoryQtyDateStatus(qty, date, status, rname, cat_name,
                                                                                    cat_pname)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByRegionCategoryPriceQty(price, qty, rname, cat_name, cat_pname)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByRegionCategoryPriceDate(price, date, rname, cat_name, cat_pname)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByRegionCategoryPriceStatus(price, status, rname, cat_name,
                                                                                  cat_pname)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByRegionCategoryQtyDate(qty, date, rname, cat_name, cat_pname)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByRegionCategoryQtyStatus(qty, status, rname, cat_name, cat_pname)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByRegionCategoryDateStatus(date, status, rname, cat_name,
                                                                                 cat_pname)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByRegionCategoryPrice(price, rname, cat_name, cat_pname)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByRegionCategoryQty(qty, rname, cat_name, cat_pname)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByRegionCategoryDate(date, rname, cat_name, cat_pname)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByRegionCategoryStatus(status, rname, cat_name, cat_pname)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByRegionOrder(self, rname, oid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByRegionOrder(rname, oid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByRegionOrder(self, rname, oid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionOrderPriceQtyDateStatus(price, qty, date, status, rname,
                                                                                      oid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByRegionOrderPriceQtyDate(price, qty, date, rname, oid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByRegionOrderPriceQtyStatus(price, qty, status, rname, oid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByRegionOrderPriceDateStatus(price, date, status, rname, oid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionOrderQtyDateStatus(qty, date, status, rname, oid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByRegionOrderPriceQty(price, qty, rname, oid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByRegionOrderPriceDate(price, date, rname, oid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByRegionOrderPriceStatus(price, status, rname, oid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByRegionOrderQtyDate(qty, date, rname, oid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByRegionOrderQtyStatus(qty, status, rname, oid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByRegionOrderDateStatus(date, status, rname, oid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByRegionOrderPrice(price, rname, oid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByRegionOrderQty(qty, rname, oid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByRegionOrderDate(date, rname, oid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByRegionOrderStatus(status, rname, oid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByCitySupplier(self, cname, sid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByCitySupplier(cname, sid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByCitySupplier(self, cname, sid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByCitySupplierPriceQtyDateStatus(price, qty, date, status, cname,
                                                                                       sid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByCitySupplierPriceQtyDate(price, qty, date, cname, sid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByCitySupplierPriceQtyStatus(price, qty, status, cname, sid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByCitySupplierPriceDateStatus(price, date, status, cname, sid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByCitySupplierQtyDateStatus(qty, date, status, cname, sid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByCitySupplierPriceQty(price, qty, cname, sid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByCitySupplierPriceDate(price, date, cname, sid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByCitySupplierPriceStatus(price, status, cname, sid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByCitySupplierQtyDate(qty, date, cname, sid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByCitySupplierQtyStatus(qty, status, cname, sid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByCitySupplierDateStatus(date, status, cname, sid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByCitySupplierPrice(price, cname, sid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByCitySupplierQty(qty, cname, sid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByCitySupplierDate(date, cname, sid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByCitySupplierStatus(status, cname, sid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByCityRequester(self, cname, rid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByCityRequester(cname, rid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByCityRequester(self, cname, rid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByCityRequesterPriceQtyDateStatus(price, qty, date, status, cname,
                                                                                        rid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByCityRequesterPriceQtyDate(price, qty, date, cname, rid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByCityRequesterPriceQtyStatus(price, qty, status, cname, rid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByCityRequesterPriceDateStatus(price, date, status, cname, rid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByCityRequesterQtyDateStatus(qty, date, status, cname, rid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByCityRequesterPriceQty(price, qty, cname, rid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByCityRequesterPriceDate(price, date, cname, rid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByCityRequesterPriceStatus(price, status, cname, rid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByCityRequesterQtyDate(qty, date, cname, rid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByCityRequesterQtyStatus(qty, status, cname, rid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByCityRequesterDateStatus(date, status, cname, rid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByCityRequesterPrice(price, cname, rid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByCityRequesterQty(qty, cname, rid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByCityRequesterDate(date, cname, rid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByCityRequesterStatus(status, cname, rid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByCityResource(self, cname, rsid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByCityResource(cname, rsid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByCityResource(self, cname, rsid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByCityResourcePriceQtyDateStatus(price, qty, date, status, cname,
                                                                                       rsid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByCityResourcePriceQtyDate(price, qty, date, cname, rsid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByCityResourcePriceQtyStatus(price, qty, status, cname, rsid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByCityResourcePriceDateStatus(price, date, status, cname, rsid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByCityResourceQtyDateStatus(qty, date, status, cname, rsid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByCityResourcePriceQty(price, qty, cname, rsid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByCityResourcePriceDate(price, date, cname, rsid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByCityResourcePriceStatus(price, status, cname, rsid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByCityResourceQtyDate(qty, date, cname, rsid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByCityResourceQtyStatus(qty, status, cname, rsid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByCityResourceDateStatus(date, status, cname, rsid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByCityResourcePrice(price, cname, rsid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByCityResourceQty(qty, cname, rsid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByCityResourceDate(date, cname, rsid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByCityResourceStatus(status, cname, rsid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByCityKeyword(self, cname, kid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByCityKeyword(cname, kid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByCityKeyword(self, cname, kid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByCityKeywordPriceQtyDateStatus(price, qty, date, status, cname,
                                                                                      kid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByCityKeywordPriceQtyDate(price, qty, date, cname, kid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByCityKeywordPriceQtyStatus(price, qty, status, cname, kid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByCityKeywordPriceDateStatus(price, date, status, cname, kid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByCityKeywordQtyDateStatus(qty, date, status, cname, kid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByCityKeywordPriceQty(price, qty, cname, kid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByCityKeywordPriceDate(price, date, cname, kid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByCityKeywordPriceStatus(price, status, cname, kid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByCityKeywordQtyDate(qty, date, cname, kid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByCityKeywordQtyStatus(qty, status, cname, kid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByCityKeywordDateStatus(date, status, cname, kid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByCityKeywordPrice(price, cname, kid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByCityKeywordQty(qty, cname, kid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByCityKeywordDate(date, cname, kid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByCityKeywordStatus(status, cname, kid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByCityCategory(self, cname, cat_name, cat_pname):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByCityCategory(cname, cat_name, cat_pname)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByCityCategory(self, cname, cat_name, cat_pname, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByCityCategoryPriceQtyDateStatus(price, qty, date, status, cname,
                                                                                       cat_name, cat_pname)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByCityCategoryPriceQtyDate(price, qty, date, cname, cat_name,
                                                                                 cat_pname)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByCityCategoryPriceQtyStatus(price, qty, status, cname, cat_name,
                                                                                   cat_pname)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByCityCategoryPriceDateStatus(price, date, status, cname,
                                                                                    cat_name, cat_pname)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByCityCategoryQtyDateStatus(qty, date, status, cname, cat_name,
                                                                                  cat_pname)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByCityCategoryPriceQty(price, qty, cname, cat_name, cat_pname)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByCityCategoryPriceDate(price, date, cname, cat_name, cat_pname)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByCityCategoryPriceStatus(price, status, cname, cat_name,
                                                                                cat_pname)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByCityCategoryQtyDate(qty, date, cname, cat_name, cat_pname)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByCityCategoryQtyStatus(qty, status, cname, cat_name, cat_pname)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByCityCategoryDateStatus(date, status, cname, cat_name, cat_pname)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByCityCategoryPrice(price, cname, cat_name, cat_pname)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByCityCategoryQty(qty, cname, cat_name, cat_pname)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByCityCategoryDate(date, cname, cat_name, cat_pname)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByCityCategoryStatus(status, cname, cat_name, cat_pname)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByCityOrder(self, cname, oid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByCityOrder(cname, oid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByCityOrder(self, cname, oid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByCityOrderPriceQtyDateStatus(price, qty, date, status, cname,
                                                                                    oid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByCityOrderPriceQtyDate(price, qty, date, cname, oid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByCityOrderPriceQtyStatus(price, qty, status, cname, oid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByCityOrderPriceDateStatus(price, date, status, cname, oid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByCityOrderQtyDateStatus(qty, date, status, cname, oid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByCityOrderPriceQty(price, qty, cname, oid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByCityOrderPriceDate(price, date, cname, oid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByCityOrderPriceStatus(price, status, cname, oid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByCityOrderQtyDate(qty, date, cname, oid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByCityOrderQtyStatus(qty, status, cname, oid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByCityOrderDateStatus(date, status, cname, oid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByCityOrderPrice(price, cname, oid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByCityOrderQty(qty, cname, oid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByCityOrderDate(date, cname, oid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByCityOrderStatus(status, cname, oid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsBySupplierRequester(self, sid, rid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsBySupplierRequester(sid, rid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsBySupplierRequester(self, sid, rid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsBySupplierRequesterPriceQtyDateStatus(price, qty, date, status,
                                                                                            sid, rid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsBySupplierRequesterPriceQtyDate(price, qty, date, sid, rid)
        elif (len(args) == 3) and price and qty and status:
            sutransactions_list = dao.getAllTransactionsBySupplierRequesterPriceQtyStatus(price, qty, status, sid, rid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsBySupplierRequesterPriceDateStatus(price, date, status, sid, rid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsBySupplierRequesterQtyDateStatus(qty, date, status, sid, rid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsBySupplierRequesterPriceQty(price, qty, sid, rid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsBySupplierRequesterPriceDate(price, date, sid, rid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsBySupplierRequesterPriceStatus(price, status, sid, rid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsBySupplierRequesterQtyDate(qty, date, sid, rid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsBySupplierRequesterQtyStatus(qty, status, sid, rid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsBySupplierRequesterDateStatus(date, status, sid, rid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsBySupplierRequesterPrice(price, sid, rid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsBySupplierRequesterQty(qty, sid, rid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsBySupplierRequesterDate(date, sid, rid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsBySupplierRequesterStatus(status, sid, rid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsBySupplierResource(self, sid, rsid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsBySupplierResource(sid, rsid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsBySupplierResource(self, sid, rsid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsBySupplierResourcePriceQtyDateStatus(price, qty, date, status,
                                                                                           sid, rsid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsBySupplierResourcePriceQtyDate(price, qty, date, sid, rsid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsBySupplierResourcePriceQtyStatus(price, qty, status, sid, rsid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsBySupplierResourcePriceDateStatus(price, date, status, sid, rsid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsBySupplierResourceQtyDateStatus(qty, date, status, sid, rsid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsBySupplierResourcePriceQty(price, qty, sid, rsid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsBySupplierResourcePriceDate(price, date, sid, rsid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsBySupplierResourcePriceStatus(price, status, sid, rsid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsBySupplierResourceQtyDate(qty, date, sid, rsid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsBySupplierResourceQtyStatus(qty, status, sid, rsid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsBySupplierResourceDateStatus(date, status, sid, rsid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsBySupplierResourcePrice(price, sid, rsid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsBySupplierResourceQty(qty, sid, rsid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsBySupplierResourceDate(date, sid, rsid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsBySupplierResourceStatus(status, sid, rsid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsBySupplierKeyword(self, sid, kid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsBySupplierKeyword(sid, kid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsBySupplierKeyword(self, sid, kid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsBySupplierKeywordPriceQtyDateStatus(price, qty, date, status, sid,
                                                                                          kid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsBySupplierKeywordPriceQtyDate(price, qty, date, sid, kid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsBySupplierKeywordPriceQtyStatus(price, qty, status, sid, kid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsBySupplierKeywordPriceDateStatus(price, date, status, sid, kid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsBySupplierKeywordQtyDateStatus(qty, date, status, sid, kid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsBySupplierKeywordPriceQty(price, qty, sid, kid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsBySupplierKeywordPriceDate(price, date, sid, kid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsBySupplierKeywordPriceStatus(price, status, sid, kid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsBySupplierKeywordQtyDate(qty, date, sid, kid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsBySupplierKeywordQtyStatus(qty, status, sid, kid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsBySupplierKeywordDateStatus(date, status, sid, kid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsBySupplierKeywordPrice(price, sid, kid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsBySupplierKeywordQty(qty, sid, kid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsBySupplierKeywordDate(date, sid, kid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsBySupplierKeywordStatus(status, sid, kid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsBySupplierCategory(self, sid, cat_name, cat_pname):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsBySupplierCategory(sid, cat_name, cat_pname)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsBySupplierCategory(self, sid, cat_name, cat_pname, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsBySupplierCategoryPriceQtyDateStatus(price, qty, date, status,
                                                                                           sid, cat_name, cat_pname)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsBySupplierCategoryPriceQtyDate(price, qty, date, sid, cat_name,
                                                                                     cat_pname)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsBySupplierCategoryPriceQtyStatus(price, qty, status, sid,
                                                                                       cat_name, cat_pname)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsBySupplierCategoryPriceDateStatus(price, date, status, sid,
                                                                                        cat_name, cat_pname)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsBySupplierCategoryQtyDateStatus(qty, date, status, sid, cat_name,
                                                                                      cat_pname)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsBySupplierCategoryPriceQty(price, qty, sid, cat_name, cat_pname)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsBySupplierCategoryPriceDate(price, date, sid, cat_name, cat_pname)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsBySupplierCategoryPriceStatus(price, status, sid, cat_name,
                                                                                    cat_pname)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsBySupplierCategoryQtyDate(qty, date, sid, cat_name, cat_pname)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsBySupplierCategoryQtyStatus(qty, status, sid, cat_name, cat_pname)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsBySupplierCategoryDateStatus(date, status, sid, cat_name,
                                                                                   cat_pname)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsBySupplierCategoryPrice(price, sid, cat_name, cat_pname)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsBySupplierCategoryQty(qty, sid, cat_name, cat_pname)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsBySupplierCategoryDate(date, sid, cat_name, cat_pname)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsBySupplierCategoryStatus(status, sid, cat_name, cat_pname)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsBySupplierOrder(self, sid, oid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsBySupplierOrder(sid, oid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsBySupplierOrder(self, sid, oid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsBySupplierOrderPriceQtyDateStatus(price, qty, date, status, sid,
                                                                                        oid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsBySupplierOrderPriceQtyDate(price, qty, date, sid, oid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsBySupplierOrderPriceQtyStatus(price, qty, status, sid, oid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsBySupplierOrderPriceDateStatus(price, date, status, sid, oid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsBySupplierOrderQtyDateStatus(qty, date, status, sid, oid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsBySupplierOrderPriceQty(price, qty, sid, oid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsBySupplierOrderPriceDate(price, date, sid, oid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsBySupplierOrderPriceStatus(price, status, sid, oid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsBySupplierOrderQtyDate(qty, date, sid, oid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsBySupplierOrderQtyStatus(qty, status, sid, oid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsBySupplierOrderDateStatus(date, status, sid, oid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsBySupplierOrderPrice(price, sid, oid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsBySupplierOrderQty(qty, sid, oid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsBySupplierOrderDate(date, sid, oid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsBySupplierOrderStatus(status, sid, oid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByRequesterResource(self, rid, rsid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByRequesterResource(rid, rsid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByRequesterResource(self, rid, rsid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByRequesterResourcePriceQtyDateStatus(price, qty, date, status,
                                                                                            rid, rsid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByRequesterResourcePriceQtyDate(price, qty, date, rid, rsid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByRequesterResourcePriceQtyStatus(price, qty, status, rid, rsid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByRequesterResourcePriceDateStatus(price, date, status, rid, rsid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByRequesterResourceQtyDateStatus(qty, date, status, rid, rsid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByRequesterResourcePriceQty(price, qty, rid, rsid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByRequesterResourcePriceDate(price, date, rid, rsid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByRequesterResourcePriceStatus(price, status, rid, rsid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByRequesterResourceQtyDate(qty, date, rid, rsid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByRequesterResourceQtyStatus(qty, status, rid, rsid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByRequesterResourceDateStatus(date, status, rid, rsid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByRequesterResourcePrice(price, rid, rsid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByRequesterResourceQty(qty, rid, rsid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByRequesterResourceDate(date, rid, rsid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByRequesterResourceStatus(status, rid, rsid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByRequesterKeyword(self, rid, kid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByRequesterKeyword(rid, kid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByRequesterKeyword(self, rid, kid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByRequesterKeywordPriceQtyDateStatus(price, qty, date, status,
                                                                                           rid, kid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByRequesterKeywordPriceQtyDate(price, qty, date, rid, kid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByRequesterKeywordPriceQtyStatus(price, qty, status, rid, kid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByRequesterKeywordPriceDateStatus(price, date, status, rid, kid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByRequesterKeywordQtyDateStatus(qty, date, status, rid, kid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByRequesterKeywordPriceQty(price, qty, rid, kid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByRequesterKeywordPriceDate(price, date, rid, kid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByRequesterKeywordPriceStatus(price, status, rid, kid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByRequesterKeywordQtyDate(qty, date, rid, kid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByRequesterKeywordQtyStatus(qty, status, rid, kid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByRequesterKeywordDateStatus(date, status, rid, kid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByRequesterKeywordPrice(price, rid, kid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByRequesterKeywordQty(qty, rid, kid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByRequesterKeywordDate(date, rid, kid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByRequesterKeywordStatus(status, rid, kid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByRequesterCategory(self, rid, cat_name, cat_pname):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByRequesterCategory(rid, cat_name, cat_pname)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByRequesterCategory(self, rid, cat_name, cat_pname, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByRequesterCategoryPriceQtyDateStatus(price, qty, date, status,
                                                                                            rid, cat_name, cat_pname)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByRequesterCategoryPriceQtyDate(price, qty, date, rid, cat_name,
                                                                                      cat_pname)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByRequesterCategoryPriceQtyStatus(price, qty, status, rid,
                                                                                        cat_name, cat_pname)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByRequesterCategoryPriceDateStatus(price, date, status, rid,
                                                                                         cat_name, cat_pname)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByRequesterCategoryQtyDateStatus(qty, date, status, rid, cat_name,
                                                                                       cat_pname)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByRequesterCategoryPriceQty(price, qty, rid, cat_name, cat_pname)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByRequesterCategoryPriceDate(price, date, rid, cat_name,
                                                                                   cat_pname)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByRequesterCategoryPriceStatus(price, status, rid, cat_name,
                                                                                     cat_pname)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByRequesterCategoryQtyDate(qty, date, rid, cat_name, cat_pname)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByRequesterCategoryQtyStatus(qty, status, rid, cat_name,
                                                                                   cat_pname)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByRequesterCategoryDateStatus(date, status, rid, cat_name,
                                                                                    cat_pname)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByRequesterCategoryPrice(price, rid, cat_name, cat_pname)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByRequesterCategoryQty(qty, rid, cat_name, cat_pname)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByRequesterCategoryDate(date, rid, cat_name, cat_pname)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByRequesterCategoryStatus(status, rid, cat_name, cat_pname)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByRequesterOrder(self, rid, oid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByRequesterOrder(rid, oid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByRequesterOrder(self, rid, oid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByRequesterOrderPriceQtyDateStatus(price, qty, date, status, rid,
                                                                                         oid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByRequesterOrderPriceQtyDate(price, qty, date, rid, oid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByRequesterOrderPriceQtyStatus(price, qty, status, rid, oid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByRequesterOrderPriceDateStatus(price, date, status, rid, oid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByRequesterOrderQtyDateStatus(qty, date, status, rid, oid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByRequesterOrderPriceQty(price, qty, rid, oid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByRequesterOrderPriceDate(price, date, rid, oid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByRequesterOrderPriceStatus(price, status, rid, oid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByRequesterOrderQtyDate(qty, date, rid, oid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByRequesterOrderQtyStatus(qty, status, rid, oid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByRequesterOrderDateStatus(date, status, rid, oid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByRequesterOrderPrice(price, rid, oid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByRequesterOrderQty(qty, rid, oid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByRequesterOrderDate(date, rid, oid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByRequesterOrderStatus(status, rid, oid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByResourceKeyword(self, rsid, kid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByResourceKeyword(rsid, kid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByResourceKeyword(self, rsid, kid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByResourceKeywordPriceQtyDateStatus(price, qty, date, status,
                                                                                          rsid, kid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByResourceKeywordPriceQtyDate(price, qty, date, rsid, kid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByResourceKeywordPriceQtyStatus(price, qty, status, rsid, kid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByResourceKeywordPriceDateStatus(price, date, status, rsid, kid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByResourceKeywordQtyDateStatus(qty, date, status, rsid, kid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByResourceKeywordPriceQty(price, qty, rsid, kid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByResourceKeywordPriceDate(price, date, rsid, kid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByResourceKeywordPriceStatus(price, status, rsid, kid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByResourceKeywordQtyDate(qty, date, rsid, kid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByResourceKeywordQtyStatus(qty, status, rsid, kid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByResourceKeywordDateStatus(date, status, rsid, kid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByResourceKeywordPrice(price, rsid, kid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByResourceKeywordQty(qty, rsid, kid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByResourceKeywordDate(date, rsid, kid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByResourceKeywordStatus(status, rsid, kid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByResourceOrder(self, rsid, oid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByResourceOrder(rsid, oid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByResourceOrder(self, rsid, oid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByResourceOrderPriceQtyDateStatus(price, qty, date, status, rsid,
                                                                                        oid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByResourceOrderPriceQtyDate(price, qty, date, rsid, oid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByResourceOrderPriceQtyStatus(price, qty, status, rsid, oid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByResourceOrderPriceDateStatus(price, date, status, rsid, oid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByResourceOrderQtyDateStatus(qty, date, status, rsid, oid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByResourceOrderPriceQty(price, qty, rsid, oid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByResourceOrderPriceDate(price, date, rsid, oid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByResourceOrderPriceStatus(price, status, rsid, oid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByResourceOrderQtyDate(qty, date, rsid, oid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByResourceOrderQtyStatus(qty, status, rsid, oid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByResourceOrderDateStatus(date, status, rsid, oid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByResourceOrderPrice(price, rsid, oid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByResourceOrderQty(qty, rsid, oid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByResourceOrderDate(date, rsid, oid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByResourceOrderStatus(status, rsid, oid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByKeywordCategory(self, kid, cat_name, cat_pname):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByKeywordCategory(kid, cat_name, cat_pname)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByKeywordCategory(self, kid, cat_name, cat_pname, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByKeywordCategoryPriceQtyDateStatus(price, qty, date, status, kid,
                                                                                          cat_name, cat_pname)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByKeywordCategoryPriceQtyDate(price, qty, date, kid, cat_name,
                                                                                    cat_pname)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByKeywordCategoryPriceQtyStatus(price, qty, status, kid, cat_name,
                                                                                      cat_pname)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByKeywordCategoryPriceDateStatus(price, date, status, kid,
                                                                                       cat_name, cat_pname)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByKeywordCategoryQtyDateStatus(qty, date, status, kid, cat_name,
                                                                                     cat_pname)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByKeywordCategoryPriceQty(price, qty, kid, cat_name, cat_pname)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByKeywordCategoryPriceDate(price, date, kid, cat_name, cat_pname)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByKeywordCategoryPriceStatus(price, status, kid, cat_name,
                                                                                   cat_pname)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByKeywordCategoryQtyDate(qty, date, kid, cat_name, cat_pname)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByKeywordCategoryQtyStatus(qty, status, kid, cat_name, cat_pname)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByKeywordCategoryDateStatus(date, status, kid, cat_name,
                                                                                  cat_pname)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByKeywordCategoryPrice(price, kid, cat_name, cat_pname)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByKeywordCategoryQty(qty, kid, cat_name, cat_pname)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByKeywordCategoryDate(date, kid, cat_name, cat_pname)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByKeywordCategoryStatus(status, kid, cat_name, cat_pname)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByKeywordOrder(self, kid, oid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByKeywordOrder(kid, oid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByKeywordOrder(self, kid, oid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByKeywordOrderPriceQtyDateStatus(price, qty, date, status, kid,
                                                                                       oid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByKeywordOrderPriceQtyDate(price, qty, date, kid, oid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByKeywordOrderPriceQtyStatus(price, qty, status, kid, oid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByKeywordOrderPriceDateStatus(price, date, status, kid, oid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByKeywordOrderQtyDateStatus(qty, date, status, kid, oid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByKeywordOrderPriceQty(price, qty, kid, oid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByKeywordOrderPriceDate(price, date, kid, oid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByKeywordOrderPriceStatus(price, status, kid, oid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByKeywordOrderQtyDate(qty, date, kid, oid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByKeywordOrderQtyStatus(qty, status, kid, oid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByKeywordOrderDateStatus(date, status, kid, oid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByKeywordOrderPrice(price, kid, oid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByKeywordOrderQty(qty, kid, oid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByKeywordOrderDate(date, kid, oid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByKeywordOrderStatus(status, kid, oid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByCategoryOrder(self, cat_name, cat_pname, oid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByCategoryOrder(cat_name, cat_pname, oid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByCategoryOrder(self, cat_name, cat_pname, oid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByCategoryOrderPriceQtyDateStatus(price, qty, date, status,
                                                                                        cat_name, cat_pname, oid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByCategoryOrderPriceQtyDate(price, qty, date, cat_name, cat_pname,
                                                                                  oid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByCategoryOrderPriceQtyStatus(price, qty, status, cat_name,
                                                                                    cat_pname, oid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByCategoryOrderPriceDateStatus(price, date, status, cat_name,
                                                                                     cat_pname, oid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByCategoryOrderQtyDateStatus(qty, date, status, cat_name,
                                                                                   cat_pname, oid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByCategoryOrderPriceQty(price, qty, cat_name, cat_pname, oid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByCategoryOrderPriceDate(price, date, cat_name, cat_pname, oid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByCategoryOrderPriceStatus(price, status, cat_name, cat_pname,
                                                                                 oid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByCategoryOrderQtyDate(qty, date, cat_name, cat_pname, oid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByCategoryOrderQtyStatus(qty, status, cat_name, cat_pname, oid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByCategoryOrderDateStatus(date, status, cat_name, cat_pname, oid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByCategoryOrderPrice(price, cat_name, cat_pname, oid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByCategoryOrderQty(qty, cat_name, cat_pname, oid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByCategoryOrderDate(date, cat_name, cat_pname, oid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByCategoryOrderStatus(status, cat_name, cat_pname, oid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByRegionSupplierRequester(self, rname, sid, rid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByRegionSupplierRequester(rname, sid, rid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByRegionSupplierRequester(self, rname, sid, rid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierRequesterPriceQtyDateStatus(price, qty, date,
                                                                                                  status, rname, sid,
                                                                                                  rid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByRegionSupplierRequesterPriceQtyDate(price, qty, date, rname,
                                                                                            sid, rid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierRequesterPriceQtyStatus(price, qty, status, rname,
                                                                                              sid, rid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierRequesterPriceDateStatus(price, date, status,
                                                                                               rname, sid, rid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierRequesterQtyDateStatus(qty, date, status, rname,
                                                                                             sid, rid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByRegionSupplierRequesterPriceQty(price, qty, rname, sid, rid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByRegionSupplierRequesterPriceDate(price, date, rname, sid, rid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierRequesterPriceStatus(price, status, rname, sid,
                                                                                           rid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByRegionSupplierRequesterQtyDate(qty, date, rname, sid, rid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierRequesterQtyStatus(qty, status, rname, sid, rid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierRequesterDateStatus(date, status, rname, sid, rid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByRegionSupplierRequesterPrice(price, rname, sid, rid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByRegionSupplierRequesterQty(qty, rname, sid, rid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByRegionSupplierRequesterDate(date, rname, sid, rid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierRequesterStatus(status, rname, sid, rid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByRegionSupplierResource(self, rname, sid, rsid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByRegionSupplierResource(rname, sid, rsid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByRegionSupplierResource(self, rname, sid, rsid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierResourcePriceQtyDateStatus(price, qty, date,
                                                                                                 status, rname, sid,
                                                                                                 rsid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByRegionSupplierResourcePriceQtyDate(price, qty, date, rname, sid,
                                                                                           rsid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierResourcePriceQtyStatus(price, qty, status, rname,
                                                                                             sid, rsid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierResourcePriceDateStatus(price, date, status,
                                                                                              rname, sid, rsid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierResourceQtyDateStatus(qty, date, status, rname,
                                                                                            sid, rsid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByRegionSupplierResourcePriceQty(price, qty, rname, sid, rsid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByRegionSupplierResourcePriceDate(price, date, rname, sid, rsid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierResourcePriceStatus(price, status, rname, sid,
                                                                                          rsid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByRegionSupplierResourceQtyDate(qty, date, rname, sid, rsid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierResourceQtyStatus(qty, status, rname, sid, rsid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierResourceDateStatus(date, status, rname, sid, rsid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByRegionSupplierResourcePrice(price, rname, sid, rsid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByRegionSupplierResourceQty(qty, rname, sid, rsid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByRegionSupplierResourceDate(date, rname, sid, rsid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierResourceStatus(status, rname, sid, rsid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByRegionSupplierKeyword(self, rname, sid, kid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByRegionSupplierKeyword(rname, sid, kid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByRegionSupplierKeyword(self, rname, sid, kid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierKeywordPriceQtyDateStatus(price, qty, date,
                                                                                                status, rname, sid, kid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByRegionSupplierKeywordPriceQtyDate(price, qty, date, rname, sid,
                                                                                          kid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierKeywordPriceQtyStatus(price, qty, status, rname,
                                                                                            sid, kid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierKeywordPriceDateStatus(price, date, status, rname,
                                                                                             sid, kid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierKeywordQtyDateStatus(qty, date, status, rname,
                                                                                           sid, kid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByRegionSupplierKeywordPriceQty(price, qty, rname, sid, kid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByRegionSupplierKeywordPriceDate(price, date, rname, sid, kid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierKeywordPriceStatus(price, status, rname, sid, kid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByRegionSupplierKeywordQtyDate(qty, date, rname, sid, kid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierKeywordQtyStatus(qty, status, rname, sid, kid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierKeywordDateStatus(date, status, rname, sid, kid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByRegionSupplierKeywordPrice(price, rname, sid, kid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByRegionSupplierKeywordQty(qty, rname, sid, kid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByRegionSupplierKeywordDate(date, rname, sid, kid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierKeywordStatus(status, rname, sid, kid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByRegionSupplierCategory(self, rname, sid, cat_name, cat_pname):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByRegionSupplierCategory(rname, sid, cat_name, cat_pname)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByRegionSupplierCategory(self, rname, sid, cat_name, cat_pname, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierCategoryPriceQtyDateStatus(price, qty, date,
                                                                                                 status, rname, sid,
                                                                                                 cat_name, cat_pname)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByRegionSupplierCategoryPriceQtyDate(price, qty, date, rname, sid,
                                                                                           cat_name, cat_pname)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierCategoryPriceQtyStatus(price, qty, status, rname,
                                                                                             sid, cat_name, cat_pname)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierCategoryPriceDateStatus(price, date, status,
                                                                                              rname, sid, cat_name,
                                                                                              cat_pname)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierCategoryQtyDateStatus(qty, date, status, rname,
                                                                                            sid, cat_name, cat_pname)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByRegionSupplierCategoryPriceQty(price, qty, rname, sid, cat_name,
                                                                                       cat_pname)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByRegionSupplierCategoryPriceDate(price, date, rname, sid,
                                                                                        cat_name, cat_pname)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierCategoryPriceStatus(price, status, rname, sid,
                                                                                          cat_name, cat_pname)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByRegionSupplierCategoryQtyDate(qty, date, rname, sid, cat_name,
                                                                                      cat_pname)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierCategoryQtyStatus(qty, status, rname, sid,
                                                                                        cat_name, cat_pname)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierCategoryDateStatus(date, status, rname, sid,
                                                                                         cat_name, cat_pname)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByRegionSupplierCategoryPrice(price, rname, sid, cat_name,
                                                                                    cat_pname)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByRegionSupplierCategoryQty(qty, rname, sid, cat_name, cat_pname)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByRegionSupplierCategoryDate(date, rname, sid, cat_name,
                                                                                   cat_pname)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierCategoryStatus(status, rname, sid, cat_name,
                                                                                     cat_pname)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByRegionSupplierOrder(self, rname, sid, oid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByRegionSupplierOrder(rname, sid, oid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByRegionSupplierOrder(self, rname, sid, oid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierOrderPriceQtyDateStatus(price, qty, date, status,
                                                                                              rname, sid, oid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByRegionSupplierOrderPriceQtyDate(price, qty, date, rname, sid,
                                                                                        oid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierOrderPriceQtyStatus(price, qty, status, rname,
                                                                                          sid, oid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierOrderPriceDateStatus(price, date, status, rname,
                                                                                           sid, oid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierOrderQtyDateStatus(qty, date, status, rname, sid,
                                                                                         oid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByRegionSupplierOrderPriceQty(price, qty, rname, sid, oid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByRegionSupplierOrderPriceDate(price, date, rname, sid, oid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierOrderPriceStatus(price, status, rname, sid, oid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByRegionSupplierOrderQtyDate(qty, date, rname, sid, oid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierOrderQtyStatus(qty, status, rname, sid, oid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierOrderDateStatus(date, status, rname, sid, oid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByRegionSupplierOrderPrice(price, rname, sid, oid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByRegionSupplierOrderQty(qty, rname, sid, oid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByRegionSupplierOrderDate(date, rname, sid, oid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByRegionSupplierOrderStatus(status, rname, sid, oid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByRegionRequesterResource(self, rname, rid, rsid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByRegionRequesterResource(rname, rid, rsid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByRegionRequesterResource(self, rname, rid, rsid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterResourcePriceQtyDateStatus(price, qty, date,
                                                                                                  status, rname, rid,
                                                                                                  rsid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByRegionRequesterResourcePriceQtyDate(price, qty, date, rname,
                                                                                            rid, rsid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterResourcePriceQtyStatus(price, qty, status, rname,
                                                                                              rid, rsid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterResourcePriceDateStatus(price, date, status,
                                                                                               rname, rid, rsid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterResourceQtyDateStatus(qty, date, status, rname,
                                                                                             rid, rsid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByRegionRequesterResourcePriceQty(price, qty, rname, rid, rsid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByRegionRequesterResourcePriceDate(price, date, rname, rid, rsid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterResourcePriceStatus(price, status, rname, rid,
                                                                                           rsid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByRegionRequesterResourceQtyDate(qty, date, rname, rid, rsid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterResourceQtyStatus(qty, status, rname, rid, rsid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterResourceDateStatus(date, status, rname, rid,
                                                                                          rsid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByRegionRequesterResourcePrice(price, rname, rid, rsid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByRegionRequesterResourceQty(qty, rname, rid, rsid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByRegionRequesterResourceDate(date, rname, rid, rsid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterResourceStatus(status, rname, rid, rsid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByRegionRequesterKeyword(self, rname, rid, kid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByRegionRequesterKeyword(rname, rid, kid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByRegionRequesterKeyword(self, rname, rid, kid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterKeywordPriceQtyDateStatus(price, qty, date,
                                                                                                 status, rname, rid,
                                                                                                 kid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByRegionRequesterKeywordPriceQtyDate(price, qty, date, rname, rid,
                                                                                           kid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterKeywordPriceQtyStatus(price, qty, status, rname,
                                                                                             rid, kid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterKeywordPriceDateStatus(price, date, status,
                                                                                              rname, rid, kid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterKeywordQtyDateStatus(qty, date, status, rname,
                                                                                            rid, kid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByRegionRequesterKeywordPriceQty(price, qty, rname, rid, kid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByRegionRequesterKeywordPriceDate(price, date, rname, rid, kid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterKeywordPriceStatus(price, status, rname, rid,
                                                                                          kid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByRegionRequesterKeywordQtyDate(qty, date, rname, rid, kid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterKeywordQtyStatus(qty, status, rname, rid, kid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterKeywordDateStatus(date, status, rname, rid, kid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByRegionRequesterKeywordPrice(price, rname, rid, kid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByRegionRequesterKeywordQty(qty, rname, rid, kid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByRegionRequesterKeywordDate(date, rname, rid, kid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterKeywordStatus(status, rname, rid, kid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByRegionRequesterCategory(self, rname, rid, cat_name, cat_pname):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByRegionRequesterCategory(rname, rid, cat_name, cat_pname)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByRegionRequesterCategory(self, rname, rid, cat_name, cat_pname, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterCategoryPriceQtyDateStatus(price, qty, date,
                                                                                                  status, rname, rid,
                                                                                                  cat_name, cat_pname)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByRegionRequesterCategoryPriceQtyDate(price, qty, date, rname,
                                                                                            rid, cat_name, cat_pname)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterCategoryPriceQtyStatus(price, qty, status, rname,
                                                                                              rid, cat_name, cat_pname)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterCategoryPriceDateStatus(price, date, status,
                                                                                               rname, rid, cat_name,
                                                                                               cat_pname)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterCategoryQtyDateStatus(qty, date, status, rname,
                                                                                             rid, cat_name, cat_pname)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByRegionRequesterCategoryPriceQty(price, qty, rname, rid,
                                                                                        cat_name, cat_pname)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByRegionRequesterCategoryPriceDate(price, date, rname, rid,
                                                                                         cat_name, cat_pname)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterCategoryPriceStatus(price, status, rname, rid,
                                                                                           cat_name, cat_pname)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByRegionRequesterCategoryQtyDate(qty, date, rname, rid, cat_name,
                                                                                       cat_pname)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterCategoryQtyStatus(qty, status, rname, rid,
                                                                                         cat_name, cat_pname)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterCategoryDateStatus(date, status, rname, rid,
                                                                                          cat_name, cat_pname)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByRegionRequesterCategoryPrice(price, rname, rid, cat_name,
                                                                                     cat_pname)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByRegionRequesterCategoryQty(qty, rname, rid, cat_name, cat_pname)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByRegionRequesterCategoryDate(date, rname, rid, cat_name,
                                                                                    cat_pname)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterCategoryStatus(status, rname, rid, cat_name,
                                                                                      cat_pname)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByRegionRequesterOrder(self, rname, rid, oid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByRegionRequesterOrder(rname, rid, oid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByRegionRequesterOrder(self, rname, rid, oid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterOrderPriceQtyDateStatus(price, qty, date, status,
                                                                                               rname, rid, oid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByRegionRequesterOrderPriceQtyDate(price, qty, date, rname, rid,
                                                                                         oid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterOrderPriceQtyStatus(price, qty, status, rname,
                                                                                           rid, oid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterOrderPriceDateStatus(price, date, status, rname,
                                                                                            rid, oid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterOrderQtyDateStatus(qty, date, status, rname, rid,
                                                                                          oid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByRegionRequesterOrderPriceQty(price, qty, rname, rid, oid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByRegionRequesterOrderPriceDate(price, date, rname, rid, oid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterOrderPriceStatus(price, status, rname, rid, oid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByRegionRequesterOrderQtyDate(qty, date, rname, rid, oid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterOrderQtyStatus(qty, status, rname, rid, oid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterOrderDateStatus(date, status, rname, rid, oid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByRegionRequesterOrderPrice(price, rname, rid, oid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByRegionRequesterOrderQty(qty, rname, rid, oid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByRegionRequesterOrderDate(date, rname, rid, oid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByRegionRequesterOrderStatus(status, rname, rid, oid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByRegionResourceKeyword(self, rname, rsid, kid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByRegionResourceKeyword(rname, rsid, kid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByRegionResourceKeyword(self, rname, rsid, kid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionResourceKeywordPriceQtyDateStatus(price, qty, date,
                                                                                                status, rname, rsid,
                                                                                                kid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByRegionResourceKeywordPriceQtyDate(price, qty, date, rname, rsid,
                                                                                          kid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByRegionResourceKeywordPriceQtyStatus(price, qty, status, rname,
                                                                                            rsid, kid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByRegionResourceKeywordPriceDateStatus(price, date, status, rname,
                                                                                             rsid, kid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionResourceKeywordQtyDateStatus(qty, date, status, rname,
                                                                                           rsid, kid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByRegionResourceKeywordPriceQty(price, qty, rname, rsid, kid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByRegionResourceKeywordPriceDate(price, date, rname, rsid, kid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByRegionResourceKeywordPriceStatus(price, status, rname, rsid,
                                                                                         kid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByRegionResourceKeywordQtyDate(qty, date, rname, rsid, kid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByRegionResourceKeywordQtyStatus(qty, status, rname, rsid, kid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByRegionResourceKeywordDateStatus(date, status, rname, rsid, kid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByRegionResourceKeywordPrice(price, rname, rsid, kid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByRegionResourceKeywordQty(qty, rname, rsid, kid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByRegionResourceKeywordDate(date, rname, rsid, kid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByRegionResourceKeywordStatus(status, rname, rsid, kid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByRegionResourceOrder(self, rname, rsid, oid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByRegionResourceOrder(rname, rsid, oid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByRegionResourceOrder(self, rname, rsid, oid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionResourceOrderPriceQtyDateStatus(price, qty, date, status,
                                                                                              rname, rsid, oid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByRegionResourceOrderPriceQtyDate(price, qty, date, rname, rsid,
                                                                                        oid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByRegionResourceOrderPriceQtyStatus(price, qty, status, rname,
                                                                                          rsid, oid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByRegionResourceOrderPriceDateStatus(price, date, status, rname,
                                                                                           rsid, oid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionResourceOrderQtyDateStatus(qty, date, status, rname, rsid,
                                                                                         oid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByRegionResourceOrderPriceQty(price, qty, rname, rsid, oid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByRegionResourceOrderPriceDate(price, date, rname, rsid, oid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByRegionResourceOrderPriceStatus(price, status, rname, rsid, oid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByRegionResourceOrderQtyDate(qty, date, rname, rsid, oid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByRegionResourceOrderQtyStatus(qty, status, rname, rsid, oid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByRegionResourceOrderDateStatus(date, status, rname, rsid, oid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByRegionResourceOrderPrice(price, rname, rsid, oid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByRegionResourceOrderQty(qty, rname, rsid, oid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByRegionResourceOrderDate(date, rname, rsid, oid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByRegionResourceOrderStatus(status, rname, rsid, oid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByRegionKeywordCategory(self, rname, kid, cat_name, cat_pname):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByRegionKeywordCategory(rname, kid, cat_name, cat_pname)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByRegionKeywordCategory(self, rname, kid, cat_name, cat_pname, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionKeywordCategoryPriceQtyDateStatus(price, qty, date,
                                                                                                status, rname, kid,
                                                                                                cat_name, cat_pname)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByRegionKeywordCategoryPriceQtyDate(price, qty, date, rname, kid,
                                                                                          cat_name, cat_pname)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByRegionKeywordCategoryPriceQtyStatus(price, qty, status, rname,
                                                                                            kid, cat_name, cat_pname)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByRegionKeywordCategoryPriceDateStatus(price, date, status, rname,
                                                                                             kid, cat_name, cat_pname)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionKeywordCategoryQtyDateStatus(qty, date, status, rname,
                                                                                           kid, cat_name, cat_pname)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByRegionKeywordCategoryPriceQty(price, qty, rname, kid, cat_name,
                                                                                      cat_pname)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByRegionKeywordCategoryPriceDate(price, date, rname, kid,
                                                                                       cat_name, cat_pname)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByRegionKeywordCategoryPriceStatus(price, status, rname, kid,
                                                                                         cat_name, cat_pname)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByRegionKeywordCategoryQtyDate(qty, date, rname, kid, cat_name,
                                                                                     cat_pname)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByRegionKeywordCategoryQtyStatus(qty, status, rname, kid,
                                                                                       cat_name, cat_pname)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByRegionKeywordCategoryDateStatus(date, status, rname, kid,
                                                                                        cat_name, cat_pname)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByRegionKeywordCategoryPrice(price, rname, kid, cat_name,
                                                                                   cat_pname)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByRegionKeywordCategoryQty(qty, rname, kid, cat_name, cat_pname)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByRegionKeywordCategoryDate(date, rname, kid, cat_name, cat_pname)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByRegionKeywordCategoryStatus(status, rname, kid, cat_name,
                                                                                    cat_pname)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByRegionKeywordOrder(self, rname, kid, oid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByRegionKeywordOrder(rname, kid, oid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByRegionKeywordOrder(self, rname, kid, oid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionKeywordOrderPriceQtyDateStatus(price, qty, date, status,
                                                                                             rname, kid, oid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByRegionKeywordOrderPriceQtyDate(price, qty, date, rname, kid,
                                                                                       oid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByRegionKeywordOrderPriceQtyStatus(price, qty, status, rname, kid,
                                                                                         oid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByRegionKeywordOrderPriceDateStatus(price, date, status, rname,
                                                                                          kid, oid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionKeywordOrderQtyDateStatus(qty, date, status, rname, kid,
                                                                                        oid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByRegionKeywordOrderPriceQty(price, qty, rname, kid, oid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByRegionKeywordOrderPriceDate(price, date, rname, kid, oid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByRegionKeywordOrderPriceStatus(price, status, rname, kid, oid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByRegionKeywordOrderQtyDate(qty, date, rname, kid, oid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByRegionKeywordOrderQtyStatus(qty, status, rname, kid, oid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByRegionKeywordOrderDateStatus(date, status, rname, kid, oid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByRegionKeywordOrderPrice(price, rname, kid, oid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByRegionKeywordOrderQty(qty, rname, kid, oid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByRegionKeywordOrderDate(date, rname, kid, oid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByRegionKeywordOrderStatus(status, rname, kid, oid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByRegionCategoryOrder(self, rname, cat_name, cat_pname, oid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByRegionCategoryOrder(rname, cat_name, cat_pname, oid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByRegionCategoryOrder(self, rname, cat_name, cat_pname, oid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionCategoryOrderPriceQtyDateStatus(price, qty, date, status,
                                                                                              rname, cat_name,
                                                                                              cat_pname, oid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByRegionCategoryOrderPriceQtyDate(price, qty, date, rname,
                                                                                        cat_name, cat_pname, oid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByRegionCategoryOrderPriceQtyStatus(price, qty, status, rname,
                                                                                          cat_name, cat_pname, oid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByRegionCategoryOrderPriceDateStatus(price, date, status, rname,
                                                                                           cat_name, cat_pname, oid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByRegionCategoryOrderQtyDateStatus(qty, date, status, rname,
                                                                                         cat_name, cat_pname, oid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByRegionCategoryOrderPriceQty(price, qty, rname, cat_name,
                                                                                    cat_pname, oid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByRegionCategoryOrderPriceDate(price, date, rname, cat_name,
                                                                                     cat_pname, oid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByRegionCategoryOrderPriceStatus(price, status, rname, cat_name,
                                                                                       cat_pname, oid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByRegionCategoryOrderQtyDate(qty, date, rname, cat_name,
                                                                                   cat_pname, oid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByRegionCategoryOrderQtyStatus(qty, status, rname, cat_name,
                                                                                     cat_pname, oid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByRegionCategoryOrderDateStatus(date, status, rname, cat_name,
                                                                                      cat_pname, oid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByRegionCategoryOrderPrice(price, rname, cat_name, cat_pname, oid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByRegionCategoryOrderQty(qty, rname, cat_name, cat_pname, oid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByRegionCategoryOrderDate(date, rname, cat_name, cat_pname, oid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByRegionCategoryOrderStatus(status, rname, cat_name, cat_pname,
                                                                                  oid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByCitySupplierRequester(self, cname, sid, rid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByCitySupplierRequester(cname, sid, rid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByCitySupplierRequester(self, cname, sid, rid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByCitySupplierRequesterPriceQtyDateStatus(price, qty, date,
                                                                                                status, cname, sid, rid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByCitySupplierRequesterPriceQtyDate(price, qty, date, cname, sid,
                                                                                          rid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByCitySupplierRequesterPriceQtyStatus(price, qty, status, cname,
                                                                                            sid, rid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByCitySupplierRequesterPriceDateStatus(price, date, status, cname,
                                                                                             sid, rid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByCitySupplierRequesterQtyDateStatus(qty, date, status, cname,
                                                                                           sid, rid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByCitySupplierRequesterPriceQty(price, qty, cname, sid, rid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByCitySupplierRequesterPriceDate(price, date, cname, sid, rid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByCitySupplierRequesterPriceStatus(price, status, cname, sid, rid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByCitySupplierRequesterQtyDate(qty, date, cname, sid, rid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByCitySupplierRequesterQtyStatus(qty, status, cname, sid, rid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByCitySupplierRequesterDateStatus(date, status, cname, sid, rid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByCitySupplierRequesterPrice(price, cname, sid, rid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByCitySupplierRequesterQty(qty, cname, sid, rid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByCitySupplierRequesterDate(date, cname, sid, rid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByCitySupplierRequesterStatus(status, cname, sid, rid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByCitySupplierResource(self, cname, sid, rsid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByCitySupplierResource(cname, sid, rsid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByCitySupplierResource(self, cname, sid, rsid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByCitySupplierResourcePriceQtyDateStatus(price, qty, date, status,
                                                                                               cname, sid, rsid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByCitySupplierResourcePriceQtyDate(price, qty, date, cname, sid,
                                                                                         rsid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByCitySupplierResourcePriceQtyStatus(price, qty, status, cname,
                                                                                           sid, rsid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByCitySupplierResourcePriceDateStatus(price, date, status, cname,
                                                                                            sid, rsid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByCitySupplierResourceQtyDateStatus(qty, date, status, cname, sid,
                                                                                          rsid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByCitySupplierResourcePriceQty(price, qty, cname, sid, rsid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByCitySupplierResourcePriceDate(price, date, cname, sid, rsid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByCitySupplierResourcePriceStatus(price, status, cname, sid, rsid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByCitySupplierResourceQtyDate(qty, date, cname, sid, rsid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByCitySupplierResourceQtyStatus(qty, status, cname, sid, rsid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByCitySupplierResourceDateStatus(date, status, cname, sid, rsid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByCitySupplierResourcePrice(price, cname, sid, rsid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByCitySupplierResourceQty(qty, cname, sid, rsid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByCitySupplierResourceDate(date, cname, sid, rsid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByCitySupplierResourceStatus(status, cname, sid, rsid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByCitySupplierKeyword(self, cname, sid, kid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByCitySupplierKeyword(cname, sid, kid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByCitySupplierKeyword(self, cname, sid, kid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByCitySupplierKeywordPriceQtyDateStatus(price, qty, date, status,
                                                                                              cname, sid, kid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByCitySupplierKeywordPriceQtyDate(price, qty, date, cname, sid,
                                                                                        kid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByCitySupplierKeywordPriceQtyStatus(price, qty, status, cname,
                                                                                          sid, kid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByCitySupplierKeywordPriceDateStatus(price, date, status, cname,
                                                                                           sid, kid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByCitySupplierKeywordQtyDateStatus(qty, date, status, cname, sid,
                                                                                         kid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByCitySupplierKeywordPriceQty(price, qty, cname, sid, kid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByCitySupplierKeywordPriceDate(price, date, cname, sid, kid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByCitySupplierKeywordPriceStatus(price, status, cname, sid, kid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByCitySupplierKeywordQtyDate(qty, date, cname, sid, kid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByCitySupplierKeywordQtyStatus(qty, status, cname, sid, kid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByCitySupplierKeywordDateStatus(date, status, cname, sid, kid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByCitySupplierKeywordPrice(price, cname, sid, kid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByCitySupplierKeywordQty(qty, cname, sid, kid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByCitySupplierKeywordDate(date, cname, sid, kid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByCitySupplierKeywordStatus(status, cname, sid, kid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByCitySupplierCategory(self, cname, sid, cat_name, cat_pname):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByCitySupplierCategory(cname, sid, cat_name, cat_pname)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByCitySupplierCategory(self, cname, sid, cat_name, cat_pname, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByCitySupplierCategoryPriceQtyDateStatus(price, qty, date, status,
                                                                                               cname, sid, cat_name,
                                                                                               cat_pname)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByCitySupplierCategoryPriceQtyDate(price, qty, date, cname, sid,
                                                                                         cat_name, cat_pname)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByCitySupplierCategoryPriceQtyStatus(price, qty, status, cname,
                                                                                           sid, cat_name, cat_pname)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByCitySupplierCategoryPriceDateStatus(price, date, status, cname,
                                                                                            sid, cat_name, cat_pname)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByCitySupplierCategoryQtyDateStatus(qty, date, status, cname, sid,
                                                                                          cat_name, cat_pname)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByCitySupplierCategoryPriceQty(price, qty, cname, sid, cat_name,
                                                                                     cat_pname)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByCitySupplierCategoryPriceDate(price, date, cname, sid, cat_name,
                                                                                      cat_pname)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByCitySupplierCategoryPriceStatus(price, status, cname, sid,
                                                                                        cat_name, cat_pname)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByCitySupplierCategoryQtyDate(qty, date, cname, sid, cat_name,
                                                                                    cat_pname)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByCitySupplierCategoryQtyStatus(qty, status, cname, sid, cat_name,
                                                                                      cat_pname)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByCitySupplierCategoryDateStatus(date, status, cname, sid,
                                                                                       cat_name, cat_pname)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByCitySupplierCategoryPrice(price, cname, sid, cat_name,
                                                                                  cat_pname)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByCitySupplierCategoryQty(qty, cname, sid, cat_name, cat_pname)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByCitySupplierCategoryDate(date, cname, sid, cat_name, cat_pname)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByCitySupplierCategoryStatus(status, cname, sid, cat_name,
                                                                                   cat_pname)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByCitySupplierOrder(self, cname, sid, oid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByCitySupplierOrder(cname, sid, oid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByCitySupplierOrder(self, cname, sid, oid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByCitySupplierOrderPriceQtyDateStatus(price, qty, date, status,
                                                                                            cname, sid, oid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByCitySupplierOrderPriceQtyDate(price, qty, date, cname, sid, oid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByCitySupplierOrderPriceQtyStatus(price, qty, status, cname, sid,
                                                                                        oid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByCitySupplierOrderPriceDateStatus(price, date, status, cname,
                                                                                         sid, oid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByCitySupplierOrderQtyDateStatus(qty, date, status, cname, sid,
                                                                                       oid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByCitySupplierOrderPriceQty(price, qty, cname, sid, oid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByCitySupplierOrderPriceDate(price, date, cname, sid, oid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByCitySupplierOrderPriceStatus(price, status, cname, sid, oid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByCitySupplierOrderQtyDate(qty, date, cname, sid, oid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByCitySupplierOrderQtyStatus(qty, status, cname, sid, oid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByCitySupplierOrderDateStatus(date, status, cname, sid, oid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByCitySupplierOrderPrice(price, cname, sid, oid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByCitySupplierOrderQty(qty, cname, sid, oid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByCitySupplierOrderDate(date, cname, sid, oid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByCitySupplierOrderStatus(status, cname, sid, oid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByCityRequesterResource(self, cname, rid, rsid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByCityRequesterResource(cname, rid, rsid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByCityRequesterResource(self, cname, rid, rsid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByCityRequesterResourcePriceQtyDateStatus(price, qty, date,
                                                                                                status, cname, rid,
                                                                                                rsid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByCityRequesterResourcePriceQtyDate(price, qty, date, cname, rid,
                                                                                          rsid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByCityRequesterResourcePriceQtyStatus(price, qty, status, cname,
                                                                                            rid, rsid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByCityRequesterResourcePriceDateStatus(price, date, status, cname,
                                                                                             rid, rsid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByCityRequesterResourceQtyDateStatus(qty, date, status, cname,
                                                                                           rid, rsid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByCityRequesterResourcePriceQty(price, qty, cname, rid, rsid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByCityRequesterResourcePriceDate(price, date, cname, rid, rsid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByCityRequesterResourcePriceStatus(price, status, cname, rid,
                                                                                         rsid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByCityRequesterResourceQtyDate(qty, date, cname, rid, rsid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByCityRequesterResourceQtyStatus(qty, status, cname, rid, rsid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByCityRequesterResourceDateStatus(date, status, cname, rid, rsid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByCityRequesterResourcePrice(price, cname, rid, rsid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByCityRequesterResourceQty(qty, cname, rid, rsid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByCityRequesterResourceDate(date, cname, rid, rsid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByCityRequesterResourceStatus(status, cname, rid, rsid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByCityRequesterKeyword(self, cname, rid, kid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByCityRequesterKeyword(cname, rid, kid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByCityRequesterKeyword(self, cname, rid, kid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByCityRequesterKeywordPriceQtyDateStatus(price, qty, date, status,
                                                                                               cname, rid, kid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByCityRequesterKeywordPriceQtyDate(price, qty, date, cname, rid,
                                                                                         kid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByCityRequesterKeywordPriceQtyStatus(price, qty, status, cname,
                                                                                           rid, kid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByCityRequesterKeywordPriceDateStatus(price, date, status, cname,
                                                                                            rid, kid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByCityRequesterKeywordQtyDateStatus(qty, date, status, cname, rid,
                                                                                          kid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByCityRequesterKeywordPriceQty(price, qty, cname, rid, kid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByCityRequesterKeywordPriceDate(price, date, cname, rid, kid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByCityRequesterKeywordPriceStatus(price, status, cname, rid, kid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByCityRequesterKeywordQtyDate(qty, date, cname, rid, kid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByCityRequesterKeywordQtyStatus(qty, status, cname, rid, kid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByCityRequesterKeywordDateStatus(date, status, cname, rid, kid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByCityRequesterKeywordPrice(price, cname, rid, kid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByCityRequesterKeywordQty(qty, cname, rid, kid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByCityRequesterKeywordDate(date, cname, rid, kid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByCityRequesterKeywordStatus(status, cname, rid, kid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByCityRequesterCategory(self, cname, rid, cat_name, cat_pname):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByCityRequesterCategory(cname, rid, cat_name, cat_pname)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByCityRequesterCategory(self, cname, rid, cat_name, cat_pname, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByCityRequesterCategoryPriceQtyDateStatus(price, qty, date,
                                                                                                status, cname, rid,
                                                                                                cat_name, cat_pname)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByCityRequesterCategoryPriceQtyDate(price, qty, date, cname, rid,
                                                                                          cat_name, cat_pname)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByCityRequesterCategoryPriceQtyStatus(price, qty, status, cname,
                                                                                            rid, cat_name, cat_pname)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByCityRequesterCategoryPriceDateStatus(price, date, status, cname,
                                                                                             rid, cat_name, cat_pname)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByCityRequesterCategoryQtyDateStatus(qty, date, status, cname,
                                                                                           rid, cat_name, cat_pname)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByCityRequesterCategoryPriceQty(price, qty, cname, rid, cat_name,
                                                                                      cat_pname)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByCityRequesterCategoryPriceDate(price, date, cname, rid,
                                                                                       cat_name, cat_pname)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByCityRequesterCategoryPriceStatus(price, status, cname, rid,
                                                                                         cat_name, cat_pname)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByCityRequesterCategoryQtyDate(qty, date, cname, rid, cat_name,
                                                                                     cat_pname)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByCityRequesterCategoryQtyStatus(qty, status, cname, rid,
                                                                                       cat_name, cat_pname)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByCityRequesterCategoryDateStatus(date, status, cname, rid,
                                                                                        cat_name, cat_pname)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByCityRequesterCategoryPrice(price, cname, rid, cat_name,
                                                                                   cat_pname)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByCityRequesterCategoryQty(qty, cname, rid, cat_name, cat_pname)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByCityRequesterCategoryDate(date, cname, rid, cat_name, cat_pname)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByCityRequesterCategoryStatus(status, cname, rid, cat_name,
                                                                                    cat_pname)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByCityRequesterOrder(self, cname, rid, oid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByCityRequesterOrder(cname, rid, oid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByCityRequesterOrder(self, cname, rid, oid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByCityRequesterOrderPriceQtyDateStatus(price, qty, date, status,
                                                                                             cname, rid, oid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByCityRequesterOrderPriceQtyDate(price, qty, date, cname, rid,
                                                                                       oid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByCityRequesterOrderPriceQtyStatus(price, qty, status, cname, rid,
                                                                                         oid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByCityRequesterOrderPriceDateStatus(price, date, status, cname,
                                                                                          rid, oid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByCityRequesterOrderQtyDateStatus(qty, date, status, cname, rid,
                                                                                        oid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByCityRequesterOrderPriceQty(price, qty, cname, rid, oid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByCityRequesterOrderPriceDate(price, date, cname, rid, oid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByCityRequesterOrderPriceStatus(price, status, cname, rid, oid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByCityRequesterOrderQtyDate(qty, date, cname, rid, oid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByCityRequesterOrderQtyStatus(qty, status, cname, rid, oid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByCityRequesterOrderDateStatus(date, status, cname, rid, oid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByCityRequesterOrderPrice(price, cname, rid, oid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByCityRequesterOrderQty(qty, cname, rid, oid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByCityRequesterOrderDate(date, cname, rid, oid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByCityRequesterOrderStatus(status, cname, rid, oid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByCityResourceKeyword(self, cname, rsid, kid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByCityResourceKeyword(cname, rsid, kid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByCityResourceKeyword(self, cname, rsid, kid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByCityResourceKeywordPriceQtyDateStatus(price, qty, date, status,
                                                                                              cname, rsid, kid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByCityResourceKeywordPriceQtyDate(price, qty, date, cname, rsid,
                                                                                        kid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByCityResourceKeywordPriceQtyStatus(price, qty, status, cname,
                                                                                          rsid, kid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByCityResourceKeywordPriceDateStatus(price, date, status, cname,
                                                                                           rsid, kid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByCityResourceKeywordQtyDateStatus(qty, date, status, cname, rsid,
                                                                                         kid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByCityResourceKeywordPriceQty(price, qty, cname, rsid, kid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByCityResourceKeywordPriceDate(price, date, cname, rsid, kid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByCityResourceKeywordPriceStatus(price, status, cname, rsid, kid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByCityResourceKeywordQtyDate(qty, date, cname, rsid, kid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByCityResourceKeywordQtyStatus(qty, status, cname, rsid, kid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByCityResourceKeywordDateStatus(date, status, cname, rsid, kid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByCityResourceKeywordPrice(price, cname, rsid, kid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByCityResourceKeywordQty(qty, cname, rsid, kid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByCityResourceKeywordDate(date, cname, rsid, kid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByCityResourceKeywordStatus(status, cname, rsid, kid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByCityResourceOrder(self, cname, rsid, oid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByCityResourceOrder(cname, rsid, oid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByCityResourceOrder(self, cname, rsid, oid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByCityResourceOrderPriceQtyDateStatus(price, qty, date, status,
                                                                                            cname, rsid, oid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByCityResourceOrderPriceQtyDate(price, qty, date, cname, rsid,
                                                                                      oid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByCityResourceOrderPriceQtyStatus(price, qty, status, cname, rsid,
                                                                                        oid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByCityResourceOrderPriceDateStatus(price, date, status, cname,
                                                                                         rsid, oid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByCityResourceOrderQtyDateStatus(qty, date, status, cname, rsid,
                                                                                       oid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByCityResourceOrderPriceQty(price, qty, cname, rsid, oid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByCityResourceOrderPriceDate(price, date, cname, rsid, oid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByCityResourceOrderPriceStatus(price, status, cname, rsid, oid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByCityResourceOrderQtyDate(qty, date, cname, rsid, oid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByCityResourceOrderQtyStatus(qty, status, cname, rsid, oid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByCityResourceOrderDateStatus(date, status, cname, rsid, oid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByCityResourceOrderPrice(price, cname, rsid, oid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByCityResourceOrderQty(qty, cname, rsid, oid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByCityResourceOrderDate(date, cname, rsid, oid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByCityResourceOrderStatus(status, cname, rsid, oid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByCityKeywordCategory(self, cname, kid, cat_name, cat_pname):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByCityKeywordCategory(cname, kid, cat_name, cat_pname)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByCityKeywordCategory(self, cname, kid, cat_name, cat_pname, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByCityKeywordCategoryPriceQtyDateStatus(price, qty, date, status,
                                                                                              cname, kid, cat_name,
                                                                                              cat_pname)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByCityKeywordCategoryPriceQtyDate(price, qty, date, cname, kid,
                                                                                        cat_name, cat_pname)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByCityKeywordCategoryPriceQtyStatus(price, qty, status, cname,
                                                                                          kid, cat_name, cat_pname)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByCityKeywordCategoryPriceDateStatus(price, date, status, cname,
                                                                                           kid, cat_name, cat_pname)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByCityKeywordCategoryQtyDateStatus(qty, date, status, cname, kid,
                                                                                         cat_name, cat_pname)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByCityKeywordCategoryPriceQty(price, qty, cname, kid, cat_name,
                                                                                    cat_pname)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByCityKeywordCategoryPriceDate(price, date, cname, kid, cat_name,
                                                                                     cat_pname)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByCityKeywordCategoryPriceStatus(price, status, cname, kid,
                                                                                       cat_name, cat_pname)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByCityKeywordCategoryQtyDate(qty, date, cname, kid, cat_name,
                                                                                   cat_pname)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByCityKeywordCategoryQtyStatus(qty, status, cname, kid, cat_name,
                                                                                     cat_pname)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByCityKeywordCategoryDateStatus(date, status, cname, kid,
                                                                                      cat_name, cat_pname)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByCityKeywordCategoryPrice(price, cname, kid, cat_name, cat_pname)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByCityKeywordCategoryQty(qty, cname, kid, cat_name, cat_pname)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByCityKeywordCategoryDate(date, cname, kid, cat_name, cat_pname)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByCityKeywordCategoryStatus(status, cname, kid, cat_name,
                                                                                  cat_pname)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByCityKeywordOrder(self, cname, kid, oid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByCityKeywordOrder(cname, kid, oid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByCityKeywordOrder(self, cname, kid, oid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByCityKeywordOrderPriceQtyDateStatus(price, qty, date, status,
                                                                                           cname, kid, oid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByCityKeywordOrderPriceQtyDate(price, qty, date, cname, kid, oid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByCityKeywordOrderPriceQtyStatus(price, qty, status, cname, kid,
                                                                                       oid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByCityKeywordOrderPriceDateStatus(price, date, status, cname, kid,
                                                                                        oid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByCityKeywordOrderQtyDateStatus(qty, date, status, cname, kid,
                                                                                      oid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByCityKeywordOrderPriceQty(price, qty, cname, kid, oid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByCityKeywordOrderPriceDate(price, date, cname, kid, oid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByCityKeywordOrderPriceStatus(price, status, cname, kid, oid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByCityKeywordOrderQtyDate(qty, date, cname, kid, oid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByCityKeywordOrderQtyStatus(qty, status, cname, kid, oid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByCityKeywordOrderDateStatus(date, status, cname, kid, oid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByCityKeywordOrderPrice(price, cname, kid, oid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByCityKeywordOrderQty(qty, cname, kid, oid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByCityKeywordOrderDate(date, cname, kid, oid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByCityKeywordOrderStatus(status, cname, kid, oid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByCityCategoryOrder(self, cname, cat_name, cat_pname, oid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByCityCategoryOrder(cname, cat_name, cat_pname, oid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByCityCategoryOrder(self, cname, cat_name, cat_pname, oid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByCityCategoryOrderPriceQtyDateStatus(price, qty, date, status,
                                                                                            cname, cat_name, cat_pname,
                                                                                            oid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByCityCategoryOrderPriceQtyDate(price, qty, date, cname, cat_name,
                                                                                      cat_pname, oid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByCityCategoryOrderPriceQtyStatus(price, qty, status, cname,
                                                                                        cat_name, cat_pname, oid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByCityCategoryOrderPriceDateStatus(price, date, status, cname,
                                                                                         cat_name, cat_pname, oid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByCityCategoryOrderQtyDateStatus(qty, date, status, cname,
                                                                                       cat_name, cat_pname, oid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByCityCategoryOrderPriceQty(price, qty, cname, cat_name,
                                                                                  cat_pname, oid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByCityCategoryOrderPriceDate(price, date, cname, cat_name,
                                                                                   cat_pname, oid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByCityCategoryOrderPriceStatus(price, status, cname, cat_name,
                                                                                     cat_pname, oid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByCityCategoryOrderQtyDate(qty, date, cname, cat_name, cat_pname,
                                                                                 oid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByCityCategoryOrderQtyStatus(qty, status, cname, cat_name,
                                                                                   cat_pname, oid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByCityCategoryOrderDateStatus(date, status, cname, cat_name,
                                                                                    cat_pname, oid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByCityCategoryOrderPrice(price, cname, cat_name, cat_pname, oid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByCityCategoryOrderQty(qty, cname, cat_name, cat_pname, oid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByCityCategoryOrderDate(date, cname, cat_name, cat_pname, oid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByCityCategoryOrderStatus(status, cname, cat_name, cat_pname, oid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsBySupplierRequesterResource(self, sid, rid, rsid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsBySupplierRequesterResource(sid, rid, rsid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsBySupplierRequesterResource(self, sid, rid, rsid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsBySupplierRequesterResourcePriceQtyDateStatus(price, qty, date,
                                                                                                    status, sid, rid,
                                                                                                    rsid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsBySupplierRequesterResourcePriceQtyDate(price, qty, date, sid,
                                                                                              rid, rsid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsBySupplierRequesterResourcePriceQtyStatus(price, qty, status, sid,
                                                                                                rid, rsid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsBySupplierRequesterResourcePriceDateStatus(price, date, status,
                                                                                                 sid, rid, rsid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsBySupplierRequesterResourceQtyDateStatus(qty, date, status, sid,
                                                                                               rid, rsid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsBySupplierRequesterResourcePriceQty(price, qty, sid, rid, rsid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsBySupplierRequesterResourcePriceDate(price, date, sid, rid, rsid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsBySupplierRequesterResourcePriceStatus(price, status, sid, rid,
                                                                                             rsid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsBySupplierRequesterResourceQtyDate(qty, date, sid, rid, rsid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsBySupplierRequesterResourceQtyStatus(qty, status, sid, rid, rsid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsBySupplierRequesterResourceDateStatus(date, status, sid, rid,
                                                                                            rsid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsBySupplierRequesterResourcePrice(price, sid, rid, rsid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsBySupplierRequesterResourceQty(qty, sid, rid, rsid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsBySupplierRequesterResourceDate(date, sid, rid, rsid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsBySupplierRequesterResourceStatus(status, sid, rid, rsid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsBySupplierRequesterKeyword(self, sid, rid, kid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsBySupplierRequesterKeyword(sid, rid, kid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsBySupplierRequesterKeyword(self, sid, rid, kid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsBySupplierRequesterKeywordPriceQtyDateStatus(price, qty, date,
                                                                                                   status, sid, rid,
                                                                                                   kid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsBySupplierRequesterKeywordPriceQtyDate(price, qty, date, sid, rid,
                                                                                             kid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsBySupplierRequesterKeywordPriceQtyStatus(price, qty, status, sid,
                                                                                               rid, kid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsBySupplierRequesterKeywordPriceDateStatus(price, date, status,
                                                                                                sid, rid, kid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsBySupplierRequesterKeywordQtyDateStatus(qty, date, status, sid,
                                                                                              rid, kid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsBySupplierRequesterKeywordPriceQty(price, qty, sid, rid, kid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsBySupplierRequesterKeywordPriceDate(price, date, sid, rid, kid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsBySupplierRequesterKeywordPriceStatus(price, status, sid, rid,
                                                                                            kid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsBySupplierRequesterKeywordQtyDate(qty, date, sid, rid, kid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsBySupplierRequesterKeywordQtyStatus(qty, status, sid, rid, kid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsBySupplierRequesterKeywordDateStatus(date, status, sid, rid, kid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsBySupplierRequesterKeywordPrice(price, sid, rid, kid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsBySupplierRequesterKeywordQty(qty, sid, rid, kid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsBySupplierRequesterKeywordDate(date, sid, rid, kid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsBySupplierRequesterKeywordStatus(status, sid, rid, kid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsBySupplierRequesterCategory(self, sid, rid, cat_name, cat_pname):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsBySupplierRequesterCategory(sid, rid, cat_name, cat_pname)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsBySupplierRequesterCategory(self, sid, rid, cat_name, cat_pname, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsBySupplierRequesterCategoryPriceQtyDateStatus(price, qty, date,
                                                                                                    status, sid, rid,
                                                                                                    cat_name, cat_pname)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsBySupplierRequesterCategoryPriceQtyDate(price, qty, date, sid,
                                                                                              rid, cat_name, cat_pname)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsBySupplierRequesterCategoryPriceQtyStatus(price, qty, status, sid,
                                                                                                rid, cat_name,
                                                                                                cat_pname)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsBySupplierRequesterCategoryPriceDateStatus(price, date, status,
                                                                                                 sid, rid, cat_name,
                                                                                                 cat_pname)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsBySupplierRequesterCategoryQtyDateStatus(qty, date, status, sid,
                                                                                               rid, cat_name, cat_pname)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsBySupplierRequesterCategoryPriceQty(price, qty, sid, rid,
                                                                                          cat_name, cat_pname)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsBySupplierRequesterCategoryPriceDate(price, date, sid, rid,
                                                                                           cat_name, cat_pname)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsBySupplierRequesterCategoryPriceStatus(price, status, sid, rid,
                                                                                             cat_name, cat_pname)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsBySupplierRequesterCategoryQtyDate(qty, date, sid, rid, cat_name,
                                                                                         cat_pname)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsBySupplierRequesterCategoryQtyStatus(qty, status, sid, rid,
                                                                                           cat_name, cat_pname)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsBySupplierRequesterCategoryDateStatus(date, status, sid, rid,
                                                                                            cat_name, cat_pname)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsBySupplierRequesterCategoryPrice(price, sid, rid, cat_name,
                                                                                       cat_pname)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsBySupplierRequesterCategoryQty(qty, sid, rid, cat_name, cat_pname)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsBySupplierRequesterCategoryDate(date, sid, rid, cat_name,
                                                                                      cat_pname)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsBySupplierRequesterCategoryStatus(status, sid, rid, cat_name,
                                                                                        cat_pname)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsBySupplierRequesterOrder(self, sid, rid, oid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsBySupplierRequesterOrder(sid, rid, oid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsBySupplierRequesterOrder(self, sid, rid, oid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsBySupplierRequesterOrderPriceQtyDateStatus(price, qty, date,
                                                                                                 status, sid, rid, oid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsBySupplierRequesterOrderPriceQtyDate(price, qty, date, sid, rid,
                                                                                           oid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsBySupplierRequesterOrderPriceQtyStatus(price, qty, status, sid,
                                                                                             rid, oid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsBySupplierRequesterOrderPriceDateStatus(price, date, status, sid,
                                                                                              rid, oid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsBySupplierRequesterOrderQtyDateStatus(qty, date, status, sid, rid,
                                                                                            oid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsBySupplierRequesterOrderPriceQty(price, qty, sid, rid, oid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsBySupplierRequesterOrderPriceDate(price, date, sid, rid, oid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsBySupplierRequesterOrderPriceStatus(price, status, sid, rid, oid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsBySupplierRequesterOrderQtyDate(qty, date, sid, rid, oid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsBySupplierRequesterOrderQtyStatus(qty, status, sid, rid, oid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsBySupplierRequesterOrderDateStatus(date, status, sid, rid, oid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsBySupplierRequesterOrderPrice(price, sid, rid, oid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsBySupplierRequesterOrderQty(qty, sid, rid, oid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsBySupplierRequesterOrderDate(date, sid, rid, oid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsBySupplierRequesterOrderStatus(status, sid, rid, oid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsBySupplierResourceKeyword(self, sid, rsid, kid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsBySupplierResourceKeyword(sid, rsid, kid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsBySupplierResourceKeyword(self, sid, rsid, kid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsBySupplierResourceKeywordPriceQtyDateStatus(price, qty, date,
                                                                                                  status, sid, rsid,
                                                                                                  kid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsBySupplierResourceKeywordPriceQtyDate(price, qty, date, sid, rsid,
                                                                                            kid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsBySupplierResourceKeywordPriceQtyStatus(price, qty, status, sid,
                                                                                              rsid, kid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsBySupplierResourceKeywordPriceDateStatus(price, date, status, sid,
                                                                                               rsid, kid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsBySupplierResourceKeywordQtyDateStatus(qty, date, status, sid,
                                                                                             rsid, kid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsBySupplierResourceKeywordPriceQty(price, qty, sid, rsid, kid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsBySupplierResourceKeywordPriceDate(price, date, sid, rsid, kid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsBySupplierResourceKeywordPriceStatus(price, status, sid, rsid,
                                                                                           kid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsBySupplierResourceKeywordQtyDate(qty, date, sid, rsid, kid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsBySupplierResourceKeywordQtyStatus(qty, status, sid, rsid, kid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsBySupplierResourceKeywordDateStatus(date, status, sid, rsid, kid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsBySupplierResourceKeywordPrice(price, sid, rsid, kid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsBySupplierResourceKeywordQty(qty, sid, rsid, kid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsBySupplierResourceKeywordDate(date, sid, rsid, kid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsBySupplierResourceKeywordStatus(status, sid, rsid, kid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsBySupplierResourceOrder(self, sid, rsid, oid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsBySupplierResourceOrder(sid, rsid, oid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsBySupplierResourceOrder(self, sid, rsid, oid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsBySupplierResourceOrderPriceQtyDateStatus(price, qty, date,
                                                                                                status, sid, rsid, oid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsBySupplierResourceOrderPriceQtyDate(price, qty, date, sid, rsid,
                                                                                          oid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsBySupplierResourceOrderPriceQtyStatus(price, qty, status, sid,
                                                                                            rsid, oid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsBySupplierResourceOrderPriceDateStatus(price, date, status, sid,
                                                                                             rsid, oid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsBySupplierResourceOrderQtyDateStatus(qty, date, status, sid, rsid,
                                                                                           oid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsBySupplierResourceOrderPriceQty(price, qty, sid, rsid, oid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsBySupplierResourceOrderPriceDate(price, date, sid, rsid, oid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsBySupplierResourceOrderPriceStatus(price, status, sid, rsid, oid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsBySupplierResourceOrderQtyDate(qty, date, sid, rsid, oid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsBySupplierResourceOrderQtyStatus(qty, status, sid, rsid, oid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsBySupplierResourceOrderDateStatus(date, status, sid, rsid, oid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsBySupplierResourceOrderPrice(price, sid, rsid, oid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsBySupplierResourceOrderQty(qty, sid, rsid, oid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsBySupplierResourceOrderDate(date, sid, rsid, oid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsBySupplierResourceOrderStatus(status, sid, rsid, oid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsBySupplierKeywordCategory(self, sid, kid, cat_name, cat_pname):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsBySupplierKeywordCategory(sid, kid, cat_name, cat_pname)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsBySupplierKeywordCategory(self, sid, kid, cat_name, cat_pname, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsBySupplierKeywordCategoryPriceQtyDateStatus(price, qty, date,
                                                                                                  status, sid, kid,
                                                                                                  cat_name, cat_pname)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsBySupplierKeywordCategoryPriceQtyDate(price, qty, date, sid, kid,
                                                                                            cat_name, cat_pname)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsBySupplierKeywordCategoryPriceQtyStatus(price, qty, status, sid,
                                                                                              kid, cat_name, cat_pname)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsBySupplierKeywordCategoryPriceDateStatus(price, date, status, sid,
                                                                                               kid, cat_name, cat_pname)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsBySupplierKeywordCategoryQtyDateStatus(qty, date, status, sid,
                                                                                             kid, cat_name, cat_pname)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsBySupplierKeywordCategoryPriceQty(price, qty, sid, kid, cat_name,
                                                                                        cat_pname)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsBySupplierKeywordCategoryPriceDate(price, date, sid, kid,
                                                                                         cat_name, cat_pname)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsBySupplierKeywordCategoryPriceStatus(price, status, sid, kid,
                                                                                           cat_name, cat_pname)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsBySupplierKeywordCategoryQtyDate(qty, date, sid, kid, cat_name,
                                                                                       cat_pname)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsBySupplierKeywordCategoryQtyStatus(qty, status, sid, kid,
                                                                                         cat_name, cat_pname)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsBySupplierKeywordCategoryDateStatus(date, status, sid, kid,
                                                                                          cat_name, cat_pname)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsBySupplierKeywordCategoryPrice(price, sid, kid, cat_name,
                                                                                     cat_pname)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsBySupplierKeywordCategoryQty(qty, sid, kid, cat_name, cat_pname)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsBySupplierKeywordCategoryDate(date, sid, kid, cat_name, cat_pname)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsBySupplierKeywordCategoryStatus(status, sid, kid, cat_name,
                                                                                      cat_pname)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsBySupplierKeywordOrder(self, sid, kid, oid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsBySupplierKeywordOrder(sid, kid, oid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsBySupplierKeywordOrder(self, sid, kid, oid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsBySupplierKeywordOrderPriceQtyDateStatus(price, qty, date, status,
                                                                                               sid, kid, oid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsBySupplierKeywordOrderPriceQtyDate(price, qty, date, sid, kid,
                                                                                         oid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsBySupplierKeywordOrderPriceQtyStatus(price, qty, status, sid, kid,
                                                                                           oid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsBySupplierKeywordOrderPriceDateStatus(price, date, status, sid,
                                                                                            kid, oid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsBySupplierKeywordOrderQtyDateStatus(qty, date, status, sid, kid,
                                                                                          oid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsBySupplierKeywordOrderPriceQty(price, qty, sid, kid, oid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsBySupplierKeywordOrderPriceDate(price, date, sid, kid, oid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsBySupplierKeywordOrderPriceStatus(price, status, sid, kid, oid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsBySupplierKeywordOrderQtyDate(qty, date, sid, kid, oid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsBySupplierKeywordOrderQtyStatus(qty, status, sid, kid, oid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsBySupplierKeywordOrderDateStatus(date, status, sid, kid, oid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsBySupplierKeywordOrderPrice(price, sid, kid, oid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsBySupplierKeywordOrderQty(qty, sid, kid, oid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsBySupplierKeywordOrderDate(date, sid, kid, oid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsBySupplierKeywordOrderStatus(status, sid, kid, oid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsBySupplierCategoryOrder(self, sid, cat_name, cat_pname, oid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsBySupplierCategoryOrder(sid, cat_name, cat_pname, oid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsBySupplierCategoryOrder(self, sid, cat_name, cat_pname, oid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsBySupplierCategoryOrderPriceQtyDateStatus(price, qty, date,
                                                                                                status, sid, cat_name,
                                                                                                cat_pname, oid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsBySupplierCategoryOrderPriceQtyDate(price, qty, date, sid,
                                                                                          cat_name, cat_pname, oid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsBySupplierCategoryOrderPriceQtyStatus(price, qty, status, sid,
                                                                                            cat_name, cat_pname, oid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsBySupplierCategoryOrderPriceDateStatus(price, date, status, sid,
                                                                                             cat_name, cat_pname, oid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsBySupplierCategoryOrderQtyDateStatus(qty, date, status, sid,
                                                                                           cat_name, cat_pname, oid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsBySupplierCategoryOrderPriceQty(price, qty, sid, cat_name,
                                                                                      cat_pname, oid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsBySupplierCategoryOrderPriceDate(price, date, sid, cat_name,
                                                                                       cat_pname, oid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsBySupplierCategoryOrderPriceStatus(price, status, sid, cat_name,
                                                                                         cat_pname, oid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsBySupplierCategoryOrderQtyDate(qty, date, sid, cat_name,
                                                                                     cat_pname, oid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsBySupplierCategoryOrderQtyStatus(qty, status, sid, cat_name,
                                                                                       cat_pname, oid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsBySupplierCategoryOrderDateStatus(date, status, sid, cat_name,
                                                                                        cat_pname, oid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsBySupplierCategoryOrderPrice(price, sid, cat_name, cat_pname, oid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsBySupplierCategoryOrderQty(qty, sid, cat_name, cat_pname, oid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsBySupplierCategoryOrderDate(date, sid, cat_name, cat_pname, oid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsBySupplierCategoryOrderStatus(status, sid, cat_name, cat_pname,
                                                                                    oid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByRequesterResourceKeyword(self, rid, rsid, kid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByRequesterResourceKeyword(rid, rsid, kid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByRequesterResourceKeyword(self, rid, rsid, kid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByRequesterResourceKeywordPriceQtyDateStatus(price, qty, date,
                                                                                                   status, rid, rsid,
                                                                                                   kid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByRequesterResourceKeywordPriceQtyDate(price, qty, date, rid,
                                                                                             rsid, kid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByRequesterResourceKeywordPriceQtyStatus(price, qty, status, rid,
                                                                                               rsid, kid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByRequesterResourceKeywordPriceDateStatus(price, date, status,
                                                                                                rid, rsid, kid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByRequesterResourceKeywordQtyDateStatus(qty, date, status, rid,
                                                                                              rsid, kid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByRequesterResourceKeywordPriceQty(price, qty, rid, rsid, kid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByRequesterResourceKeywordPriceDate(price, date, rid, rsid, kid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByRequesterResourceKeywordPriceStatus(price, status, rid, rsid,
                                                                                            kid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByRequesterResourceKeywordQtyDate(qty, date, rid, rsid, kid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByRequesterResourceKeywordQtyStatus(qty, status, rid, rsid, kid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByRequesterResourceKeywordDateStatus(date, status, rid, rsid, kid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByRequesterResourceKeywordPrice(price, rid, rsid, kid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByRequesterResourceKeywordQty(qty, rid, rsid, kid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByRequesterResourceKeywordDate(date, rid, rsid, kid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByRequesterResourceKeywordStatus(status, rid, rsid, kid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByRequesterResourceOrder(self, rid, rsid, oid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByRequesterResourceOrder(rid, rsid, oid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByRequesterResourceOrder(self, rid, rsid, oid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByRequesterResourceOrderPriceQtyDateStatus(price, qty, date,
                                                                                                 status, rid, rsid, oid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByRequesterResourceOrderPriceQtyDate(price, qty, date, rid, rsid,
                                                                                           oid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByRequesterResourceOrderPriceQtyStatus(price, qty, status, rid,
                                                                                             rsid, oid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByRequesterResourceOrderPriceDateStatus(price, date, status, rid,
                                                                                              rsid, oid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByRequesterResourceOrderQtyDateStatus(qty, date, status, rid,
                                                                                            rsid, oid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByRequesterResourceOrderPriceQty(price, qty, rid, rsid, oid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByRequesterResourceOrderPriceDate(price, date, rid, rsid, oid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByRequesterResourceOrderPriceStatus(price, status, rid, rsid, oid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByRequesterResourceOrderQtyDate(qty, date, rid, rsid, oid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByRequesterResourceOrderQtyStatus(qty, status, rid, rsid, oid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByRequesterResourceOrderDateStatus(date, status, rid, rsid, oid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByRequesterResourceOrderPrice(price, rid, rsid, oid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByRequesterResourceOrderQty(qty, rid, rsid, oid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByRequesterResourceOrderDate(date, rid, rsid, oid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByRequesterResourceOrderStatus(status, rid, rsid, oid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByRequesterKeywordCategory(self, rid, kid, cat_name, cat_pname):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByRequesterKeywordCategory(rid, kid, cat_name, cat_pname)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByRequesterKeywordCategory(self, rid, kid, cat_name, cat_pname, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByRequesterKeywordCategoryPriceQtyDateStatus(price, qty, date,
                                                                                                   status, rid, kid,
                                                                                                   cat_name, cat_pname)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByRequesterKeywordCategoryPriceQtyDate(price, qty, date, rid, kid,
                                                                                             cat_name, cat_pname)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByRequesterKeywordCategoryPriceQtyStatus(price, qty, status, rid,
                                                                                               kid, cat_name, cat_pname)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByRequesterKeywordCategoryPriceDateStatus(price, date, status,
                                                                                                rid, kid, cat_name,
                                                                                                cat_pname)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByRequesterKeywordCategoryQtyDateStatus(qty, date, status, rid,
                                                                                              kid, cat_name, cat_pname)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByRequesterKeywordCategoryPriceQty(price, qty, rid, kid, cat_name,
                                                                                         cat_pname)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByRequesterKeywordCategoryPriceDate(price, date, rid, kid,
                                                                                          cat_name, cat_pname)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByRequesterKeywordCategoryPriceStatus(price, status, rid, kid,
                                                                                            cat_name, cat_pname)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByRequesterKeywordCategoryQtyDate(qty, date, rid, kid, cat_name,
                                                                                        cat_pname)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByRequesterKeywordCategoryQtyStatus(qty, status, rid, kid,
                                                                                          cat_name, cat_pname)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByRequesterKeywordCategoryDateStatus(date, status, rid, kid,
                                                                                           cat_name, cat_pname)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByRequesterKeywordCategoryPrice(price, rid, kid, cat_name,
                                                                                      cat_pname)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByRequesterKeywordCategoryQty(qty, rid, kid, cat_name, cat_pname)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByRequesterKeywordCategoryDate(date, rid, kid, cat_name,
                                                                                     cat_pname)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByRequesterKeywordCategoryStatus(status, rid, kid, cat_name,
                                                                                       cat_pname)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByRequesterKeywordOrder(self, rid, kid, oid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByRequesterKeywordOrder(rid, kid, oid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByRequesterKeywordOrder(self, rid, kid, oid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByRequesterKeywordOrderPriceQtyDateStatus(price, qty, date,
                                                                                                status, rid, kid, oid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByRequesterKeywordOrderPriceQtyDate(price, qty, date, rid, kid,
                                                                                          oid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByRequesterKeywordOrderPriceQtyStatus(price, qty, status, rid,
                                                                                            kid, oid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByRequesterKeywordOrderPriceDateStatus(price, date, status, rid,
                                                                                             kid, oid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByRequesterKeywordOrderQtyDateStatus(qty, date, status, rid, kid,
                                                                                           oid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByRequesterKeywordOrderPriceQty(price, qty, rid, kid, oid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByRequesterKeywordOrderPriceDate(price, date, rid, kid, oid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByRequesterKeywordOrderPriceStatus(price, status, rid, kid, oid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByRequesterKeywordOrderQtyDate(qty, date, rid, kid, oid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByRequesterKeywordOrderQtyStatus(qty, status, rid, kid, oid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByRequesterKeywordOrderDateStatus(date, status, rid, kid, oid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByRequesterKeywordOrderPrice(price, rid, kid, oid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByRequesterKeywordOrderQty(qty, rid, kid, oid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByRequesterKeywordOrderDate(date, rid, kid, oid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByRequesterKeywordOrderStatus(status, rid, kid, oid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByRequesterCategoryOrder(self, rid, cat_name, cat_pname, oid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByRequesterCategoryOrder(rid, cat_name, cat_pname, oid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByRequesterCategoryOrder(self, rid, cat_name, cat_pname, oid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByRequesterCategoryOrderPriceQtyDateStatus(price, qty, date,
                                                                                                 status, rid, cat_name,
                                                                                                 cat_pname, oid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByRequesterCategoryOrderPriceQtyDate(price, qty, date, rid,
                                                                                           cat_name, cat_pname, oid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByRequesterCategoryOrderPriceQtyStatus(price, qty, status, rid,
                                                                                             cat_name, cat_pname, oid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByRequesterCategoryOrderPriceDateStatus(price, date, status, rid,
                                                                                              cat_name, cat_pname, oid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByRequesterCategoryOrderQtyDateStatus(qty, date, status, rid,
                                                                                            cat_name, cat_pname, oid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByRequesterCategoryOrderPriceQty(price, qty, rid, cat_name,
                                                                                       cat_pname, oid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByRequesterCategoryOrderPriceDate(price, date, rid, cat_name,
                                                                                        cat_pname, oid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByRequesterCategoryOrderPriceStatus(price, status, rid, cat_name,
                                                                                          cat_pname, oid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByRequesterCategoryOrderQtyDate(qty, date, rid, cat_name,
                                                                                      cat_pname, oid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByRequesterCategoryOrderQtyStatus(qty, status, rid, cat_name,
                                                                                        cat_pname, oid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByRequesterCategoryOrderDateStatus(date, status, rid, cat_name,
                                                                                         cat_pname, oid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByRequesterCategoryOrderPrice(price, rid, cat_name, cat_pname,
                                                                                    oid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByRequesterCategoryOrderQty(qty, rid, cat_name, cat_pname, oid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByRequesterCategoryOrderDate(date, rid, cat_name, cat_pname, oid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByRequesterCategoryOrderStatus(status, rid, cat_name, cat_pname,
                                                                                     oid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByResourceKeywordCategory(self, rsid, kid, cat_name, cat_pname):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByResourceKeywordCategory(rsid, kid, cat_name, cat_pname)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByResourceKeywordCategory(self, rsid, kid, cat_name, cat_pname, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByResourceKeywordCategoryPriceQtyDateStatus(price, qty, date,
                                                                                                  status, rsid, kid,
                                                                                                  cat_name, cat_pname)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByResourceKeywordCategoryPriceQtyDate(price, qty, date, rsid, kid,
                                                                                            cat_name, cat_pname)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByResourceKeywordCategoryPriceQtyStatus(price, qty, status, rsid,
                                                                                              kid, cat_name, cat_pname)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByResourceKeywordCategoryPriceDateStatus(price, date, status,
                                                                                               rsid, kid, cat_name,
                                                                                               cat_pname)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByResourceKeywordCategoryQtyDateStatus(qty, date, status, rsid,
                                                                                             kid, cat_name, cat_pname)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByResourceKeywordCategoryPriceQty(price, qty, rsid, kid, cat_name,
                                                                                        cat_pname)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByResourceKeywordCategoryPriceDate(price, date, rsid, kid,
                                                                                         cat_name, cat_pname)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByResourceKeywordCategoryPriceStatus(price, status, rsid, kid,
                                                                                           cat_name, cat_pname)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByResourceKeywordCategoryQtyDate(qty, date, rsid, kid, cat_name,
                                                                                       cat_pname)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByResourceKeywordCategoryQtyStatus(qty, status, rsid, kid,
                                                                                         cat_name, cat_pname)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByResourceKeywordCategoryDateStatus(date, status, rsid, kid,
                                                                                          cat_name, cat_pname)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByResourceKeywordCategoryPrice(price, rsid, kid, cat_name,
                                                                                     cat_pname)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByResourceKeywordCategoryQty(qty, rsid, kid, cat_name, cat_pname)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByResourceKeywordCategoryDate(date, rsid, kid, cat_name,
                                                                                    cat_pname)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByResourceKeywordCategoryStatus(status, rsid, kid, cat_name,
                                                                                      cat_pname)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByResourceKeywordOrder(self, rsid, kid, oid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByResourceKeywordOrder(rsid, kid, oid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByResourceKeywordOrder(self, rsid, kid, oid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByResourceKeywordOrderPriceQtyDateStatus(price, qty, date, status,
                                                                                               rsid, kid, oid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByResourceKeywordOrderPriceQtyDate(price, qty, date, rsid, kid,
                                                                                         oid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByResourceKeywordOrderPriceQtyStatus(price, qty, status, rsid,
                                                                                           kid, oid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByResourceKeywordOrderPriceDateStatus(price, date, status, rsid,
                                                                                            kid, oid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByResourceKeywordOrderQtyDateStatus(qty, date, status, rsid, kid,
                                                                                          oid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByResourceKeywordOrderPriceQty(price, qty, rsid, kid, oid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByResourceKeywordOrderPriceDate(price, date, rsid, kid, oid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByResourceKeywordOrderPriceStatus(price, status, rsid, kid, oid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByResourceKeywordOrderQtyDate(qty, date, rsid, kid, oid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByResourceKeywordOrderQtyStatus(qty, status, rsid, kid, oid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByResourceKeywordOrderDateStatus(date, status, rsid, kid, oid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByResourceKeywordOrderPrice(price, rsid, kid, oid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByResourceKeywordOrderQty(qty, rsid, kid, oid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByResourceKeywordOrderDate(date, rsid, kid, oid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByResourceKeywordOrderStatus(status, rsid, kid, oid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def getTransactionsByKeywordCategoryOrder(self, kid, cat_name, cat_pname, oid):
        dao = TransactionDAO()
        transactions_list = dao.getTransactionsByKeywordCategoryOrder(kid, cat_name, cat_pname, oid)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def searchTransactionsByKeywordCategoryOrder(self, kid, cat_name, cat_pname, oid, args):
        price = args.get("tprice")
        qty = args.get("tqty")
        date = args.get("tdate")
        status = args.get("tstatus")
        dao = TransactionDAO()
        transactions_list = []
        if (len(args) == 4) and price and qty and date and status:
            transactions_list = dao.getAllTransactionsByKeywordCategoryOrderPriceQtyDateStatus(price, qty, date, status,
                                                                                               kid, cat_name, cat_pname,
                                                                                               oid)
        elif (len(args) == 3) and price and qty and date:
            transactions_list = dao.getAllTransactionsByKeywordCategoryOrderPriceQtyDate(price, qty, date, kid,
                                                                                         cat_name, cat_pname, oid)
        elif (len(args) == 3) and price and qty and status:
            transactions_list = dao.getAllTransactionsByKeywordCategoryOrderPriceQtyStatus(price, qty, status, kid,
                                                                                           cat_name, cat_pname, oid)
        elif (len(args) == 3) and price and date and status:
            transactions_list = dao.getAllTransactionsByKeywordCategoryOrderPriceDateStatus(price, date, status, kid,
                                                                                            cat_name, cat_pname, oid)
        elif (len(args) == 3) and qty and date and status:
            transactions_list = dao.getAllTransactionsByKeywordCategoryOrderQtyDateStatus(qty, date, status, kid,
                                                                                          cat_name, cat_pname, oid)
        elif (len(args) == 2) and price and qty:
            transactions_list = dao.getAllTransactionsByKeywordCategoryOrderPriceQty(price, qty, kid, cat_name,
                                                                                     cat_pname, oid)
        elif (len(args) == 2) and price and date:
            transactions_list = dao.getAllTransactionsByKeywordCategoryOrderPriceDate(price, date, kid, cat_name,
                                                                                      cat_pname, oid)
        elif (len(args) == 2) and price and status:
            transactions_list = dao.getAllTransactionsByKeywordCategoryOrderPriceStatus(price, status, kid, cat_name,
                                                                                        cat_pname, oid)
        elif (len(args) == 2) and qty and date:
            transactions_list = dao.getAllTransactionsByKeywordCategoryOrderQtyDate(qty, date, kid, cat_name, cat_pname,
                                                                                    oid)
        elif (len(args) == 2) and qty and status:
            transactions_list = dao.getAllTransactionsByKeywordCategoryOrderQtyStatus(qty, status, kid, cat_name,
                                                                                      cat_pname, oid)
        elif (len(args) == 2) and date and status:
            transactions_list = dao.getAllTransactionsByKeywordCategoryOrderDateStatus(date, status, kid, cat_name,
                                                                                       cat_pname, oid)
        elif (len(args) == 1) and price:
            transactions_list = dao.getAllTransactionsByKeywordCategoryOrderPrice(price, kid, cat_name, cat_pname, oid)
        elif (len(args) == 1) and qty:
            transactions_list = dao.getAllTransactionsByKeywordCategoryOrderQty(qty, kid, cat_name, cat_pname, oid)
        elif (len(args) == 1) and date:
            transactions_list = dao.getAllTransactionsByKeywordCategoryOrderDate(date, kid, cat_name, cat_pname, oid)
        elif (len(args) == 1) and status:
            transactions_list = dao.getAllTransactionsByKeywordCategoryOrderStatus(status, kid, cat_name, cat_pname,
                                                                                   oid)
        else:
            return jsonify(Transactions="Bad Request"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

























































































































































































































































































































































