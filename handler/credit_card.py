from flask import jsonify
from dao.credit_card import CreditCardDAO


class CreditCardsHandler:
    def build_creditcards_dict(self, row):
        result = {}
        result['cid'] = row[0]
        result['card_number'] = row[1]
        result['security_code'] = row[2]
        result['ccname'] = row[3]
        result['exp_date'] = row[4]
        return result

    def build_creditcards_attributes(self, cid, card_number, security_code, ccname, exp_date, rid, addid):
        result = {}
        result['cid'] = cid
        result['card_number'] = card_number
        result['security_code'] = security_code
        result['ccname'] = ccname
        result['exp_date'] = exp_date
        result['rid'] = rid
        result['addid'] = addid
        return result

    def build_creditcardsUpdate_attributes(self, cid, card_number, security_code, ccname, exp_date):
        result = {}
        result['cid'] = cid
        result['card_number'] = card_number
        result['security_code'] = security_code
        result['ccname'] = ccname
        result['exp_date'] = exp_date
        return result

    def getAllCreditCards(self):
        dao = CreditCardDAO()
        creditcards_list = dao.getAllCreditCards() #Select cid, card_number, security_code, cname, exp_date from Credit_Card
        result_list = []
        for row in creditcards_list:
            result = self.build_creditcards_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Credit Card Not Found"), 404
        else:
            return jsonify(Credit_Cards=result_list)

    def searchAllCreditCards(self, args):
        number = args.get("card_number")
        name = args.get("ccname")
        dao = CreditCardDAO()
        creditcards_list = []
        if (len(args) == 2) and name and number:
            creditcards_list = dao.getAllCreditCardsByNameNumber(name, number)
        elif (len(args) == 1) and name:
            creditcards_list = dao.getAllCreditCardsByName(name)
        elif (len(args) == 1) and number:
            creditcards_list = dao.getAllCreditCardsByNumber(number)
        else:
            return jsonify(Credit_Cards="Bad Request"), 400
        result_list = []
        for row in creditcards_list:
            result = self.build_creditcards_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Credit Card Not Found"), 404
        else:
            return jsonify(Credit_Card=result_list)

    def getCreditCard(self, cid):
        dao = CreditCardDAO()
        creditcards_list = dao.getCreditCardById(cid) #Select cid, card_number, security_code, cname, exp_date from Credit_Card where cid = %s
        result_list = []
        for row in creditcards_list:
            result = self.build_creditcards_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Credit Card Not Found"), 404
        else:
            return jsonify(Credit_Cards=result_list)

    def searchCreditCard(self, cid, args):
        name = args.get("card_number")
        number = args.get("ccname")
        dao = CreditCardDAO()
        creditcards_list = []
        if (len(args) == 2) and name and number:
            creditcards_list = dao.getAllCreditCardsByIdNameNumber(name, number, cid)
        elif (len(args) == 1) and name:
            creditcards_list = dao.getAllCreditCardsByIdName(name, cid)
        elif (len(args) == 1) and number:
            creditcards_list = dao.getAllCreditCardsByIdNumber(number, cid)
        else:
            return jsonify(Credit_Cards="Bad Request"), 400
        result_list = []
        for row in creditcards_list:
            result = self.build_creditcards_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Credit Card Not Found"), 404
        else:
            return jsonify(Transactions=result_list)

    def insertCreditCard(self, form):
        if len(form) != 6:
            return jsonify(Error="Malformed post request"), 400
        else:
            card_number = form['card_number']
            security_code = form['security_code']
            ccname = form['ccname']
            exp_date = form['exp_date']
            rid = form['rid']
            addid = form['addid']
            if card_number and security_code and ccname and exp_date and rid and addid:
                dao = CreditCardDAO()
                cid = dao.insertCreditCard(card_number, security_code, ccname, exp_date, rid, addid)
                result = self.build_creditcards_attributes(cid, card_number, security_code, ccname, exp_date, rid, addid)
                return jsonify(Credit_Card=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteCreditCard(self, cid):
        dao = CreditCardDAO()
        if not dao.getCreditCardById(cid):
            return jsonify(Error="Credit_Card not found."), 404
        else:
            dao.deleteCreditCard(cid)
            return jsonify(DeleteStatus="OK"), 200


    def updateCreditCard(self, cid, form):
        dao = CreditCardDAO()
        if not dao.getCreditCardById(cid):
            return jsonify(Error="Credit Card not found."), 404
        else:
            if len(form) != 4:
                return jsonify(Error="Malformed update request"), 400
            else:
                card_number = form['card_number']
                security_code = form['security_code']
                ccname = form['ccname']
                exp_date = form['exp_date']
                if card_number and security_code and ccname and exp_date:
                    dao.updateCreditCard(cid, card_number, security_code, ccname, exp_date)
                    result = self.build_creditcardsUpdate_attributes(cid, card_number, security_code, ccname, exp_date)
                    return jsonify(Credit_Card=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def getCreditCardsByTransaction(self, tid):
        dao = CreditCardDAO()
        creditcards_list = dao.getAllCreditCardsByTransaction(tid) #Select cid, card_number, security_code, cname, exp_date from (Credit_Card inner join payment on payid = cid) natural inner join Order_Info natural inner join transaction where tid = %s
        result_list = []
        for row in creditcards_list:
            result = self.build_creditcards_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Credit Card Not Found"), 404
        else:
            return jsonify(Credit_Cards=result_list)

    def searchCreditCardsByTransaction(self, tid, args):
        name = args.get("card_number")
        number = args.get("ccname")
        dao = CreditCardDAO()
        creditcards_list = []
        if (len(args) == 2) and name and number:
            creditcards_list = dao.getAllCreditCardsByTransactionNameNumber(name, number, tid)
        elif (len(args) == 1) and name:
            creditcards_list = dao.getAllCreditCardsByTransactionName(name, tid)
        elif (len(args) == 1) and number:
            creditcards_list = dao.getAllCreditCardsByTransactionNumber(number, tid)
        else:
            return jsonify(Credit_Cards="Bad Request"), 400
        result_list = []
        for row in creditcards_list:
            result = self.build_creditcards_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Credit Card Not Found"), 404
        else:
            return jsonify(Credit_Cards=result_list)

    def getCreditCardsByRequester(self, rid):
        dao = CreditCardDAO()
        creditcards_list = dao.getAllCreditCardsByRequester(rid) #Select cid, card_number, security_code, cname, exp_date from Credit_Card natural inner join Requester where rid = %s;
        result_list = []
        for row in creditcards_list:
            result = self.build_creditcards_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Credit Card Not Found"), 404
        else:
            return jsonify(Credit_Cards=result_list)

    def searchCreditCardsByRequester(self, rid, args):
        name = args.get("card_number")
        number = args.get("ccname")
        dao = CreditCardDAO()
        creditcards_list = []
        if (len(args) == 2) and name and number:
            creditcards_list = dao.getAllCreditCardsByRequesterNameNumber(name, number, rid)
        elif (len(args) == 1) and name:
            creditcards_list = dao.getAllCreditCardsByRequesterName(name, rid)
        elif (len(args) == 1) and number:
            creditcards_list = dao.getAllCreditCardsByRequesterNumber(number, rid)
        else:
            return jsonify(Credit_Cards="Bad Request"), 400
        result_list = []
        for row in creditcards_list:
            result = self.build_creditcards_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Credit Card Not Found"), 404
        else:
            return jsonify(Credit_Cards=result_list)

    def getCreditCardsByOrder(self, oid):
        dao = CreditCardDAO()
        creditcards_list = dao.getAllCreditCardsByOrder(oid) #Select cid, card_number, security_code, cname, exp_date from (Credit_Card inner join payment on payid = cid) natural inner join Order_Info where oid = %s
        result_list = []
        for row in creditcards_list:
            result = self.build_creditcards_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Credit Card Not Found"), 404
        else:
            return jsonify(Credit_Cards=result_list)

    def searchCreditCardsByOrder(self, oid, args):
        name = args.get("card_number")
        number = args.get("ccname")
        dao = CreditCardDAO()
        creditcards_list = []
        if (len(args) == 2) and name and number:
            creditcards_list = dao.getAllCreditCardsByOrderNameNumber(name, number, oid)
        elif (len(args) == 1) and name:
            creditcards_list = dao.getAllCreditCardsByOrderName(name, oid)
        elif (len(args) == 1) and number:
            creditcards_list = dao.getAllCreditCardsByOrderNumber(number, oid)
        else:
            return jsonify(Credit_Cards="Bad Request"), 400
        result_list = []
        for row in creditcards_list:
            result = self.build_creditcards_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Credit Card Not Found"), 404
        else:
            return jsonify(Credit_Cards=result_list)











