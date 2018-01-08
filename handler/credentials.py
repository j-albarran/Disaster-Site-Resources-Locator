from flask import jsonify

from dao.credentials import CredentialDAO
from dao.account import AccountDAO

class CredentialsHandler:

# =========================================================================== #
#                                 Builders                                    #
# =========================================================================== #

    def build_credential_dict(self, row):
        result = {}
        result['username'] = row[0]
        result['password'] = row[1]
        return result

# =========================================================================== #
#                                 Methods                                     #
# =========================================================================== #

# ================ #
#    Credentials   #
# ================ #

    def getAllCredentials(self):

        dao = CredentialDAO()

        credentials_list = dao.getAllCredentials()
        result_list = []

        for credential in credentials_list:
            result = self.build_credential_dict(credential)
            result_list.append(result)
        return jsonify(Credentials=result_list)

    def getCredentialsByUsername(self, username):

        dao = CredentialDAO()
        row = dao.getCredentialsByUsername(username)

        if not row:
            return jsonify(Error = "Credentials Not Found"), 404
        else:
            credentials = self.build_credential_dict(row)
            return jsonify(Credentials = credentials)

# ================ #
#    Accounts      #
# ================ #

    def getAccountCredentials(self, aid):

        daoAcc = AccountDAO()
        dao = CredentialDAO()

        if not daoAcc.getAccountById(aid):
            return jsonify(Error = 'Account Not Found'), 404

        credentials_list = dao.getAccountCredentials(aid)
        results_list = []
        for row in credentials_list:
            result = self.build_credential_dict(row)
            results_list.append(result)
        return jsonify(Credentials = results_list)

    def searchAccountCredentials(self, aid, args):

        daoAcc = AccountDAO()
        dao = CredentialDAO()

        if not daoAcc.getAccountById(aid):
            return jsonify(Error = 'Account Not Found'), 404

        username = args.get('username')
        password = args.get('password')

        credentials_list = []

        if (len(args) == 2) and username and password:
            credentials_list = dao.getAccountCredentialsByUsernamePassword(aid, username, password)
        elif (len(args) == 1) and username:
            credentials_list = dao.getAccountCredentialsByUsername(aid, username)
        elif (len(args) == 1) and password:
            credentials_list = dao.getAccountCredentialsByPassword(aid, password)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in credentials_list:
            result = self.build_credential_dict(row)
            result_list.append(row)
        return jsonify(Credentials = result_list)