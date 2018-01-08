from config.dbconfig import conn


class BankAccountDAO:
    def __init__(self):
        self.conn = conn

# =========================================================================== #
#                                 Methods                                     #
# =========================================================================== #

    def getAllCredentials(self):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBankAccountById(bid, self):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account where bid = %s;"
        cursor.execute(query, (bid,))
        result = cursor.fetchone()
        return result

    def getBankAccountByRoutingAccountNumberBankName(routing, accountNumber, BankName, self):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account where routing = %s and accountNumber = %s and BankName = %s;"
        cursor.execute(query, (routing, accountNumber, BankName, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBankAccountByRoutingAccountNumber(routing, accountNumber, self):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account where routing = %s and accountNumber = %s;"
        cursor.execute(query, (routing, accountNumber, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBankAccountByRoutingBankName(routing, BankName, self):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account where routing = %s and BankName = %s;"
        cursor.execute(query, (routing, BankName, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBankAccountByAccountNumberBankName(accountNumber, BankName, self):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account where accountNumber = %s and BankName = %s;"
        cursor.execute(query, (accountNumber, BankName, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBankAccountByRouting(routing, self):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account where routing = %s;"
        cursor.execute(query, (routing, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBankAccountByAccountNumber(accountNumber, self):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account where accountNumber = %s;"
        cursor.execute(query, (accountNumber, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBankAccountByBankNamet(BankName, self):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account where BankName = %s;"
        cursor.execute(query, (BankName, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBankAccountOfThisTransaction(tid, self):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account natural inner join transaction where tid = %s;"
        cursor.execute(query, (tid,))
        result = cursor.fetchone()
        return result

    def getBankAccountOfThisTransactionByRoutingAccountNumberBankName(tid, routing, accountNumber, BankName, self):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account natural inner join transaction where tid = %s and routing = %s and accountNumber = %s and BankName = %s;"
        cursor.execute(query, (tid, routing, accountNumber, BankName, ))
        result = cursor.fetchone()
        return result

    def getBankAccountOfThisTransactionByRoutingAccountNumber(tid, routing, accountNumber, self):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account natural inner join transaction where tid = %s and routing = %s and accountNumber = %s;"
        cursor.execute(query, (tid, routing, accountNumber, ))
        result = cursor.fetchone()
        return result

    def getBankAccountOfThisTransactionByRoutingBankName(tid, routing, BankName, self):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account natural inner join transaction where tid = %s and routing = %s and BankName = %s;"
        cursor.execute(query, (tid, routing, BankName, ))
        result = cursor.fetchone()
        return result

    def getBankAccountOfThisTransactionByAccountNumberBankName(tid, accountNumber, BankName, self):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account natural inner join transaction where tid = %s and accountNumber = %s and BankName = %s;"
        cursor.execute(query, (tid, accountNumber, BankName, ))
        result = cursor.fetchone()
        return result

    def getBankAccountOfThisTransactionByRouting(tid, routing, self):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account natural inner join transaction where tid = %s and routing = %s;"
        cursor.execute(query, (tid, routing, ))
        result = cursor.fetchone()
        return result

    def getBankAccountOfThisTransactionByAccountNumber(tid, accountNumber, self):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account natural inner join transaction where tid = %s and accountNumber = %s;"
        cursor.execute(query, (tid, accountNumber, ))
        result = cursor.fetchone()
        return result

    def getBankAccountOfThisTransactionByBankName(tid, BankName, self):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account natural inner join transaction where tid = %s and BankName = %s;"
        cursor.execute(query, (tid, BankName, ))
        result = cursor.fetchone()
        return result

    def getBankAccountOfThisSupplier(sid, self):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account natural inner join transaction where sid = %s;"
        cursor.execute(query, (sid,))
        result = cursor.fetchone()
        return result

    def getBankAccountOfThisSupplierByRoutingAccountNumberBankName(sid, routing, accountNumber, BankName, self):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account natural inner join transaction where sid = %s and routing = %s and accountNumber = %s and BankName = %s;"
        cursor.execute(query, (sid, routing, accountNumber, BankName, ))
        result = cursor.fetchone()
        return result

    def getBankAccountOfThisSupplierByRoutingAccountNumber(sid, routing, accountNumber, self):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account natural inner join transaction where sid = %s and routing = %s and accountNumber = %s;"
        cursor.execute(query, (sid, routing, accountNumber, ))
        result = cursor.fetchone()
        return result

    def getBankAccountOfThisSupplierByRoutingBankName(sid, routing, BankName, self):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account natural inner join transaction where sid = %s and routing = %s and BankName = %s;"
        cursor.execute(query, (sid, routing, BankName, ))
        result = cursor.fetchone()
        return result

    def getBankAccountOfThisSupplierByAccountNumberBankName(sid, accountNumber, BankName, self):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account natural inner join transaction where sid = %s and accountNumber = %s and BankName = %s;"
        cursor.execute(query, (sid, accountNumber, BankName, ))
        result = cursor.fetchone()
        return result

    def getBankAccountOfThisSupplierByRouting(sid, routing, self):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account natural inner join transaction where sid = %s and routing = %s;"
        cursor.execute(query, (sid, routing, ))
        result = cursor.fetchone()
        return result

    def getBankAccountOfThisSupplierByAccountNumber(sid, accountNumber, self):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account natural inner join transaction where sid = %s and accountNumber = %s;"
        cursor.execute(query, (sid, accountNumber, ))
        result = cursor.fetchone()
        return result

    def getBankAccountOfThisSupplierByBankName(sid, BankName, self):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account natural inner join transaction where sid = %s and BankName = %s;"
        cursor.execute(query, (sid, BankName, ))
        result = cursor.fetchone()
        return result