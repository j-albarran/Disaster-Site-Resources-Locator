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





