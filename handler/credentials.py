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

    def build_credential_attributes(self, username, password):
        result = {}
        result['username'] = username
        result['password'] = password
        return result
# =========================================================================== #
#                                 Methods                                     #
# =========================================================================== #


    # ============ #
    #    Updates   #
    # ============ #

    def addCredentials(self, form):
        if len(form) != 3:
            return jsonify(Error = "Malformed post request"), 400
        else:

            username = form['username']
            password = form['password']
            aid = form['aid']

            if username and password and aid:
                dao = CredentialDAO()
                credential = dao.addCredentials(username, password, aid)
                result = self.build_credential_attributes(credential, password)
                return jsonify(Credentials = result), 201
            else:
                return jsonify(Error = "Unexpected attributes in post request"), 400


    def updateCredentials(self, username, form):
        dao = CredentialDAO()
        if not dao.getCredentialsByUsername(username):
            return jsonify(Error = "Credentials not found"), 404
        else:
            if len(form) != 3:
                return jsonify(Error = "Malformed update request"), 400

            username = form['username']
            password = form['password']
            aid = form['aid']

            if username and password and aid:
                dao.updateCredentials(username, password, aid)
                result = self.build_credential_attributes(username, password)
                return jsonify(Credentials = result), 200
            else:
                return jsonify(Error = "Unexpected attributes in update request"), 400

    def deleteCredentials(self, username):
        dao = CredentialDAO()
        if not dao.getCredentialsByUsername(username):
            return jsonify(Error="Credentials not found"), 404
        else:
            dao.deleteCredentials(username)
            return jsonify(DeleteStatus="OK"), 200

    # ============ #
    #    Gets      #
    # ============ #

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