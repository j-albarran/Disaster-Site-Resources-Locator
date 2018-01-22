from flask import jsonify
from dao.order import OrderDAO


class OrdersHandler:
    def build_orders_dict(self, row):
        result = {}
        result['oid'] = row[0]
        result['odate'] = row[1]
        result['oprice'] = row[2]
        result['ostatus'] = row[3]
        return result

    def build_order_attributes(self,oid, odate, oprice, ostatus, payid):
        result = {}
        result['oid'] = oid
        result['odate'] = odate
        result['oprice'] = oprice
        result['ostatus'] = ostatus
        result['payid'] = payid
        return result

    def build_orderUpdate_attributes(self,oid, odate, oprice, ostatus):
        result = {}
        result['oid'] = oid
        result['odate'] = odate
        result['oprice'] = oprice
        result['ostatus'] = ostatus
        return result

    def getAllOrders(self):
        dao = OrderDAO()
        orders_list = dao.getAllOrders() #Select oid, odate, oprice, ostatus from Order_Info
        result_list = []
        for row in orders_list:
            result = self.build_orders_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Order Not Found"), 404
        else:
            return jsonify(Orders=result_list)

    def searchAllOrders(self, args):
        date = args.get("odate")
        price = args.get("oprice")
        status = args.get("ostatus")
        dao = OrderDAO()
        orders_list = []
        if (len(args) == 3) and date and price and status:
            orders_list = dao.getAllOrdersByDatePriceStatus(date, price, status)
        elif (len(args) == 2) and date and price:
            orders_list = dao.getAllOrdersByDatePrice(date, price)
        elif (len(args) == 2) and date and status:
            orders_list = dao.getAllOrdersByDateStatus(date, status)
        elif (len(args) == 2) and price and status:
            orders_list = dao.getAllOrdersByPriceStatus(price, status)
        elif (len(args) == 1) and date:
            orders_list = dao.getAllOrdersByDate(date)
        elif (len(args) == 1) and price:
            orders_list = dao.getAllOrdersByPrice(price)
        elif (len(args) == 1) and status:
            orders_list = dao.getAllOrdersByStatus(status)
        else:
            return jsonify(Orders="Bad Request"), 400
        result_list = []
        for row in orders_list:
            result = self.build_orders_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Order Not Found"), 404
        else:
            return jsonify(Orders=result_list)

    def getOrdersById(self, oid):
        dao = OrderDAO()
        orders_list = dao.getOrderById(oid) #Select oid, odate, oprice, ostatus from Order_Info where oid = %s
        result_list = []
        for row in orders_list:
            result = self.build_orders_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Order Not Found"), 404
        else:
            return jsonify(Orders=result_list)

    def searchOrdersById(self, oid, args):
        date = args.get("odate")
        price = args.get("oprice")
        status = args.get("ostatus")
        dao = OrderDAO()
        orders_list = []
        if (len(args) == 3) and date and price and status:
            orders_list = dao.getAllOrdersByIdDatePriceStatus(date, price, status ,id)
        elif (len(args) == 2) and date and price:
            orders_list = dao.getAllOrdersByIdDatePrice(date, price, id)
        elif (len(args) == 2) and date and status:
            orders_list = dao.getAllOrdersByIdDateStatus(date, status, id)
        elif (len(args) == 2) and price and status:
            orders_list = dao.getAllOrdersByIdPriceStatus(price, status, id)
        elif (len(args) == 1) and date:
            orders_list = dao.getAllOrdersByIdDate(date, id)
        elif (len(args) == 1) and price:
            orders_list = dao.getAllOrdersByIdPrice(price, id)
        elif (len(args) == 1) and status:
            orders_list = dao.getAllOrdersByIdStatus(status, id)
        else:
            return jsonify(Orders="Bad Request"), 400
        result_list = []
        for row in orders_list:
            result = self.build_orders_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Order Not Found"), 404
        else:
            return jsonify(Orders=result_list)


    def insertOrder(self, form):
        if len(form) != 4:
            print(len(form))
            print(form)
            return jsonify(Error="Malformed post request"), 400
        else:
            odate = form['odate']
            oprice = form['oprice']
            ostatus = form['ostatus']
            payid = form['payid']
            if odate and oprice and ostatus and payid:
                dao = OrderDAO()
                oid = dao.insertOrder(odate, oprice, ostatus, payid)
                result = self.build_order_attributes(oid, odate, oprice, ostatus, payid)
                return jsonify(Order=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteOrder(self, oid):
        dao = OrderDAO()
        if not dao.getOrderById(oid):
            return jsonify(Error="Order not found."), 404
        else:
            dao.deleteOrder(oid)
            return jsonify(DeleteStatus="OK"), 200

    def updateOrder(self, oid, form):
        dao = OrderDAO()
        if not dao.getOrderById(oid):
            return jsonify(Error="Order not found."), 404
        else:
            if len(form) != 3:
                return jsonify(Error="Malformed update request"), 400
            else:
                odate = form['odate']
                oprice = form['oprice']
                ostatus = form['ostatus']
                if odate and oprice and ostatus:
                    dao.updateOrder(oid, odate, oprice, ostatus)
                    result = self.build_orderUpdate_attributes(oid, odate, oprice, ostatus)
                    return jsonify(Order=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def getOrdersByRequester(self, rid):
        dao = OrderDAO()
        orders_list = dao.getAllOrdersByRequester(rid) #Select oid, odate, oprice, ostatus from Order_Info where rid = %s
        result_list = []
        for row in orders_list:
            result = self.build_orders_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Order Not Found"), 404
        else:
            return jsonify(Orders=result_list)

    def searchOrdersByRequester(self, rid, args):
        date = args.get("odate")
        price = args.get("oprice")
        status = args.get("ostatus")
        dao = OrderDAO()
        orders_list = []
        if (len(args) == 3) and date and price and status:
            orders_list = dao.getAllOrdersByRequesterDatePriceStatus(date, price, status, rid)
        elif (len(args) == 2) and date and price:
            orders_list = dao.getAllOrdersByRequesterDatePrice(date, price, rid)
        elif (len(args) == 2) and date and status:
            orders_list = dao.getAllOrdersByRequesterDateStatus(date, status, rid)
        elif (len(args) == 2) and price and status:
            orders_list = dao.getAllOrdersByRequesterPriceStatus(price, status, rid)
        elif (len(args) == 1) and date:
            orders_list = dao.getAllOrdersByRequesterDate(date, rid)
        elif (len(args) == 1) and price:
            orders_list = dao.getAllOrdersByRequesterPrice(price, rid)
        elif (len(args) == 1) and status:
            orders_list = dao.getAllOrdersByRequesterStatus(status, rid)
        else:
            return jsonify(Orders="Bad Request"), 400
        result_list = []
        for row in orders_list:
            result = self.build_orders_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Order Not Found"), 404
        else:
            return jsonify(Orders=result_list)

    def getOrdersBySupplier(self, sid):
        dao = OrderDAO()
        orders_list = dao.getAllOrdersBySupplier(sid) #Select oid, odate, oprice, ostatus from Order_Info where rid = %s
        result_list = []
        for row in orders_list:
            result = self.build_orders_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Order Not Found"), 404
        else:
            return jsonify(Orders=result_list)

    def searchOrdersBySupplier(self, sid, args):
        date = args.get("odate")
        price = args.get("oprice")
        status = args.get("ostatus")
        dao = OrderDAO()
        orders_list = []
        if (len(args) == 3) and date and price and status:
            orders_list = dao.getAllOrdersBySupplierDatePriceStatus(date, price, status, sid)
        elif (len(args) == 2) and date and price:
            orders_list = dao.getAllOrdersBySupplierDatePrice(date, price, sid)
        elif (len(args) == 2) and date and status:
            orders_list = dao.getAllOrdersBySupplierDateStatus(date, status, sid)
        elif (len(args) == 2) and price and status:
            orders_list = dao.getAllOrdersBySupplierPriceStatus(price, status, sid)
        elif (len(args) == 1) and date:
            orders_list = dao.getAllOrdersBySupplierDate(date, sid)
        elif (len(args) == 1) and price:
            orders_list = dao.getAllOrdersBySupplierPrice(price, sid)
        elif (len(args) == 1) and status:
            orders_list = dao.getAllOrdersBySupplierStatus(status, sid)
        else:
            return jsonify(Orders="Bad Request"), 400
        result_list = []
        for row in orders_list:
            result = self.build_orders_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Order Not Found"), 404
        else:
            return jsonify(Orders=result_list)

    def getOrdersByTransaction(self, tid):
        dao = OrderDAO()
        orders_list = dao.getAllOrdersByTransaction(tid) #Select oid, odate, oprice, ostatus from Order_Info where rid = %s
        result_list = []
        for row in orders_list:
            result = self.build_orders_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Order Not Found"), 404
        else:
            return jsonify(Orders=result_list)

    def searchOrdersByTransaction(self, tid, args):
        date = args.get("odate")
        price = args.get("oprice")
        status = args.get("ostatus")
        dao = OrderDAO()
        orders_list = []
        if (len(args) == 3) and date and price and status:
            orders_list = dao.getAllOrdersByTransactionDatePriceStatus(date, price, status, tid)
        elif (len(args) == 2) and date and price:
            orders_list = dao.getAllOrdersByTransactionDatePrice(date, price, tid)
        elif (len(args) == 2) and date and status:
            orders_list = dao.getAllOrdersByTransactionDateStatus(date, status, tid)
        elif (len(args) == 2) and price and status:
            orders_list = dao.getAllOrdersByTransactionPriceStatus(price, status, tid)
        elif (len(args) == 1) and date:
            orders_list = dao.getAllOrdersByTransactionDate(date, tid)
        elif (len(args) == 1) and price:
            orders_list = dao.getAllOrdersByTransactionPrice(price, tid)
        elif (len(args) == 1) and status:
            orders_list = dao.getAllOrdersByTransactionStatus(status, tid)
        else:
            return jsonify(Orders="Bad Request"), 400
        result_list = []
        for row in orders_list:
            result = self.build_orders_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Order Not Found"), 404
        else:
            return jsonify(Orders=result_list)
