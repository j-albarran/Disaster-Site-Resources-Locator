from config.dbconfig import conn


class BankAccountDAO:
    def __init__(self):
        self.conn = conn

# =========================================================================== #
#                                 Methods                                     #
# =========================================================================== #

    def getAllBankAccounts(self):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBankAccountById(self,bid):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account where bid = %s;"
        cursor.execute(query, (bid,))
        result = cursor.fetchone()
        return result

    def getBankAccountByRoutingAccountNumberBankName(self,routing, accountNumber, BankName):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account where routing = %s and accountNumber = %s and BankName = %s;"
        cursor.execute(query, (routing, accountNumber, BankName, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBankAccountByRoutingAccountNumber(self,routing, accountNumber):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account where routing = %s and accountNumber = %s;"
        cursor.execute(query, (routing, accountNumber, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBankAccountByRoutingBankName(self,routing, BankName):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account where routing = %s and BankName = %s;"
        cursor.execute(query, (routing, BankName, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBankAccountByAccountNumberBankName(self,accountNumber, BankName):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account where accountNumber = %s and BankName = %s;"
        cursor.execute(query, (accountNumber, BankName, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBankAccountByRouting(self,routing):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account where routing = %s;"
        cursor.execute(query, (routing, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBankAccountByAccountNumber(self,accountNumber):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account where accountNumber = %s;"
        cursor.execute(query, (accountNumber, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBankAccountByBankNamet(self,BankName):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account where BankName = %s;"
        cursor.execute(query, (BankName, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBankAccountOfThisTransaction(self,tid):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account natural inner join transaction where tid = %s;"
        cursor.execute(query, (tid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBankAccountOfThisTransactionByRoutingAccountNumberBankName(self,tid, routing, accountNumber, BankName):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account natural inner join transaction where tid = %s and routing = %s and accountNumber = %s and BankName = %s;"
        cursor.execute(query, (tid, routing, accountNumber, BankName, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBankAccountOfThisTransactionByRoutingAccountNumber(self,tid, routing, accountNumber):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account natural inner join transaction where tid = %s and routing = %s and accountNumber = %s;"
        cursor.execute(query, (tid, routing, accountNumber, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBankAccountOfThisTransactionByRoutingBankName(self,tid, routing, BankName):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account natural inner join transaction where tid = %s and routing = %s and BankName = %s;"
        cursor.execute(query, (tid, routing, BankName, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBankAccountOfThisTransactionByAccountNumberBankName(self,tid, accountNumber, BankName):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account natural inner join transaction where tid = %s and accountNumber = %s and BankName = %s;"
        cursor.execute(query, (tid, accountNumber, BankName, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBankAccountOfThisTransactionByRouting(self,tid, routing):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account natural inner join transaction where tid = %s and routing = %s;"
        cursor.execute(query, (tid, routing, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBankAccountOfThisTransactionByAccountNumber(self,tid, accountNumber):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account natural inner join transaction where tid = %s and accountNumber = %s;"
        cursor.execute(query, (tid, accountNumber, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBankAccountOfThisTransactionByBankName(self,tid, BankName):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account natural inner join transaction where tid = %s and BankName = %s;"
        cursor.execute(query, (tid, BankName, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBankAccountOfThisSupplier(self,sid):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account natural inner join transaction where sid = %s;"
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBankAccountOfThisSupplierByRoutingAccountNumberBankName(self,sid, routing, accountNumber, BankName):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account natural inner join transaction where sid = %s and routing = %s and accountNumber = %s and BankName = %s;"
        cursor.execute(query, (sid, routing, accountNumber, BankName, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBankAccountOfThisSupplierByRoutingAccountNumber(self,sid, routing, accountNumber):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account natural inner join transaction where sid = %s and routing = %s and accountNumber = %s;"
        cursor.execute(query, (sid, routing, accountNumber, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBankAccountOfThisSupplierByRoutingBankName(self,sid, routing, BankName):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account natural inner join transaction where sid = %s and routing = %s and BankName = %s;"
        cursor.execute(query, (sid, routing, BankName, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBankAccountOfThisSupplierByAccountNumberBankName(self,sid, accountNumber, BankName):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account natural inner join transaction where sid = %s and accountNumber = %s and BankName = %s;"
        cursor.execute(query, (sid, accountNumber, BankName, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBankAccountOfThisSupplierByRouting(self,sid, routing):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account natural inner join transaction where sid = %s and routing = %s;"
        cursor.execute(query, (sid, routing, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBankAccountOfThisSupplierByAccountNumber(self,sid, accountNumber):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account natural inner join transaction where sid = %s and accountNumber = %s;"
        cursor.execute(query, (sid, accountNumber, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBankAccountOfThisSupplierByBankName(self,sid, BankName):
        cursor = self.conn.cursor()
        query = "select bid, routing, accountNumber, BankName from bank_account natural inner join transaction where sid = %s and BankName = %s;"
        cursor.execute(query, (sid, BankName, ))
        result = []
        for row in cursor:
            result.append(row)
        return result
