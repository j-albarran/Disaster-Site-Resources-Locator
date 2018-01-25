from flask import jsonify

from dao.bank_account import BankAccountDAO
from dao.supplier import SupplierDAO
from dao.transaction import TransactionDAO

class BankAccountHandler:

# =========================================================================== #
#                                 Builders                                    #
# =========================================================================== #

    def build_bank_account_dict(self, row):
        result = {}
        result['bid'] = row[0]
        result['routing'] = row[1]
        result['accountNumber'] = row[2]
        result['BankName'] = row[3]
        return result

    def build_bank_account_attributes(self, bid, routing, accountNumber, BankAccount):
        result = {}
        result['bid'] = bid
        result['routing'] = routing
        result['accountNumber'] = accountNumber
        result['BankName'] = BankAccount
        return result
# =========================================================================== #
#                                 Methods                                     #
# =========================================================================== #

    # ============ #
    #    Updates   #
    # ============ #

    def addNewBankAccount(self, form):
        if len(form) != 4:
            return jsonify(Error = "Malformed post request"), 400
        else:

            routing = form['routing']
            accountNumber = form['accountNumber']
            BankName = form['BankName']
            sid = form['sid']

            if routing and accountNumber and BankName and sid:
                dao = BankAccountDAO()
                bid = dao.addNewBankAccount(routing, accountNumber, BankName, sid)
                result = self.build_bank_account_attributes(bid, routing, accountNumber, BankName)
                return jsonify(BankAccount = result), 201
            else:
                return jsonify(Error = "Unexpected attributes in post request"), 400

    #

    def updateBankAccount(self, bid, form):
        dao = BankAccountDAO()
        if not dao.getBankAccountById(bid):
            return jsonify(Error = 'Bank Account not found'), 404
        else:
            if len(form) != 3:
                return jsonify(Error = "Malformed update request"), 400

            routing = form['routing']
            accountNumber = form['accountNumber']
            BankName = form['BankName']

            if routing and accountNumber and BankName:
                dao.updateBankAccount(bid, routing, accountNumber, BankName)
                result = self.build_bank_account_attributes(bid, routing, accountNumber, BankName)
                return jsonify(BankAccount = result)
            else:
                return jsonify(Error = "Unexpected attributes in update request"), 400


    def deleteBankAccount(self, bid):
        dao = BankAccountDAO()
        if not dao.getBankAccountById(bid):
            return jsonify(Error="Bank Account not found."), 404
        else:
            dao.deleteBankAccount(bid)
            return jsonify(DeleteStatus="OK"), 200

    # ================ #
    #   Bank Accounts  #
    # ================ #

    def getAllBankAccounts(self):

        dao = BankAccountDAO()
        bank_account_list = dao.getAllBankAccounts()

        result_list = []

        for bank_account in bank_account_list:
            result = self.build_bank_account_dict(bank_account)
            result_list.append(result)
        return jsonify(Bank_Accounts=result_list)

    def getBankAccountById(self, bid):
        dao = BankAccountDAO()
        row = dao.getBankAccountById(bid)
        if not row:
            return jsonify(Error = "Bank Account Not Found"), 404
        else:
            bank_accounts = self.build_bank_account_dict(row)
            return jsonify(Bank_Account = bank_accounts)

    def searchBankAccounts(self, args):
        dao = BankAccountDAO()

        routing = args.get('routing')
        accountNumber = args.get('accountNumber')
        BankName = args.get('BankName')

        bank_accounts_list = []

        if (len(args) == 3) and routing and accountNumber and BankName:
            bank_accounts_list = dao.getBankAccountByRoutingAccountNumberBankName(routing, accountNumber, BankName)
        elif(len(args) == 2) and routing and accountNumber:
            bank_accounts_list = dao.getBankAccountByRoutingAccountNumber(routing, accountNumber)
        elif(len(args) == 2) and routing and BankName:
            bank_accounts_list = dao.getBankAccountByRoutingBankName(routing, BankName)
        elif(len(args) == 2) and accountNumber and BankName:
            bank_accounts_list = dao.getBankAccountByAccountNumberBankName(accountNumber, BankName)
        elif(len(args) == 1) and routing:
            bank_accounts_list = dao.getBankAccountByRouting(routing)
        elif(len(args) == 1) and accountNumber:
            bank_accounts_list = dao.getBankAccountByAccountNumber(accountNumber)
        elif(len(args) == 1) and BankName:
            bank_accounts_list = dao.getBankAccountByBankNamet(BankName)
        else:
            return jsonify(Error = "Malformed query string"), 400
        results_list = []
        for row in bank_accounts_list:
            result = self.build_bank_account_dict(row)
            results_list.append(result)
        return jsonify(Bank_Account = results_list)

# ================ #
#    Suppliers     #
# ================ #

    def getBankAccountOfThisSupplier(self, sid):

        dao = BankAccountDAO()
        daoSup = SupplierDAO()

        if not daoSup.getSupplierById(sid):
            return jsonify(Error = 'Supplier Not Found'), 404

        bank_accounts_list = dao.getBankAccountOfThisSupplier(sid)
        results_list = []

        for row in bank_accounts_list:
            result = self.build_bank_account_dict(row)
            results_list.append(result)
        return jsonify(Bank_Account = results_list)

    def searchBankAccountOfThisSupplier(self, sid, args):

        dao = BankAccountDAO()
        daoSup = SupplierDAO()

        if not daoSup.getSupplierById(sid):
            return jsonify(Error = 'Supplier Not Found'), 404

        routing = args.get('routing')
        accountNumber = args.get('accountNumber')
        BankName = args.get('BankName')

        bank_accounts_list = []

        if (len(args) == 3) and routing and accountNumber and BankName:
            bank_accounts_list = dao.getBankAccountOfThisSupplierByRoutingAccountNumberBankName(sid, routing, accountNumber, BankName)
        elif(len(args) == 2) and routing and accountNumber:
            bank_accounts_list = dao.getBankAccountOfThisSupplierByRoutingAccountNumber(sid, routing, accountNumber)
        elif(len(args) == 2) and routing and BankName:
            bank_accounts_list = dao.getBankAccountOfThisSupplierByRoutingBankName(sid, routing, BankName)
        elif(len(args) == 2) and accountNumber and BankName:
            bank_accounts_list = dao.getBankAccountOfThisSupplierByAccountNumberBankName(sid, accountNumber, BankName)
        elif(len(args) == 1) and routing:
            bank_accounts_list = dao.getBankAccountOfThisSupplierByRouting(sid, routing)
        elif(len(args) == 1) and accountNumber:
            bank_accounts_list = dao.getBankAccountOfThisSupplierByAccountNumber(sid, accountNumber)
        elif(len(args) == 1) and BankName:
            bank_accounts_list = dao.getBankAccountOfThisSupplierByBankName(sid, BankName)
        else:
            return jsonify(Error = "Malformed query string"), 400
        results_list = []
        for row in bank_accounts_list:
            result = self.build_bank_account_dict(row)
            results_list.append(result)
        return jsonify(Bank_Account = results_list)

    # ================ #
    #  Transactions    #
    # ================ #

    def getBankAccountOfThisTransaction(self, tid):

        dao = BankAccountDAO()
        daoTran = TransactionDAO()

        if not daoTran.getTransactionById(tid):
            return jsonify(Error = 'Transaction Not Found'), 404

        bank_accounts_list = dao.getBankAccountOfThisTransaction(tid)
        result_list = []
        for row in bank_accounts_list:
            result = self.build_bank_account_dict(row)
            result_list.append(result)
        return jsonify(Bank_Account = result_list)

    def seatchBankAccountOfThisTransaction(self, tid, args):

        dao = BankAccountDAO()
        daoTran = TransactionDAO()

        if not daoTran.getTransactionById(tid):
            return jsonify(Error = 'Transaction Not Found'), 404

        routing = args.get('routing')
        accountNumber = args.get('accountNumber')
        BankName = args.get('BankName')

        bank_accounts_list = []

        if (len(args) == 3) and routing and accountNumber and BankName:
            bank_accounts_list = dao.getBankAccountOfThisTransactionByRoutingAccountNumberBankName(tid, routing, accountNumber, BankName)
        elif(len(args) == 2) and routing and accountNumber:
            bank_accounts_list = dao.getBankAccountOfThisTransactionByRoutingAccountNumber(tid, routing, accountNumber)
        elif(len(args) == 2) and routing and BankName:
            bank_accounts_list = dao.getBankAccountOfThisTransactionByRoutingBankName(tid, routing, BankName)
        elif(len(args) == 2) and accountNumber and BankName:
            bank_accounts_list = dao.getBankAccountOfThisTransactionByAccountNumberBankName(tid, accountNumber, BankName)
        elif(len(args) == 1) and routing:
            bank_accounts_list = dao.getBankAccountOfThisTransactionByRouting(tid, routing)
        elif(len(args) == 1) and accountNumber:
            bank_accounts_list = dao.getBankAccountOfThisTransactionByAccountNumber(tid, accountNumber)
        elif(len(args) == 1) and BankName:
            bank_accounts_list = dao.getBankAccountOfThisTransactionByBankName(tid, BankName)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []

        for row in bank_accounts_list:
            result = self.build_bank_account_dict(row)
            result_list.append(result)
        return jsonify(Bank_Account = result_list)