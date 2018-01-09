from flask import jsonify

from dao.account import AccountDAO
from dao.address import AddressDAO
from dao.city import CityDAO
from dao.region import RegionDAO
from dao.credentials import CredentialDAO

class AccountHandler:

# =========================================================================== #
#                                 Builders                                    #
# =========================================================================== #

    def build_account_dict(self, row):
        result = {}
        result['aid'] = row[0]
        result['afirst'] = row[1]
        result['alast'] = row[2]
        result['email'] = row[3]
        result['phone'] = row[4]
        return result

# =========================================================================== #
#                                 Methods                                     #
# =========================================================================== #

# ================ #
#     Accounts     #
# ================ #

    def getAllAccounts(self):
        dao = AccountDAO()
        accounts_list = dao.getAllAccounts()
        result_list = []
        for account in accounts_list:
            result = self.build_account_dict(account)
            result_list.append(result)
        return jsonify(Accounts=result_list)

    def getAccountById(self, aid):
        dao = AccountDAO()
        row = dao.getAccountById(aid)
        if not row:
            return jsonify(Error = "Account Not Found"), 404
        else:
            account = self.build_account_dict(row)
            return jsonify(Account = account)

    def searchAccounts(self, args):

        dao = AccountDAO()

        afirst = args.get('afirst')
        alast = args.get('alast')
        email = args.get('email')
        phone = args.get('phone')

        accounts_list = []

        if(len(args) == 4) and afirst and alast and email and phone:
            accounts_list = dao.getAccountsByAFirstALastEmailPhone(afirst, alast, email, phone)
        elif(len(args) == 3) and afirst and alast and email:
            accounts_list = dao.getAccountsByAFirstALastEmail(afirst, alast, email)
        elif(len(args) == 3) and afirst and alast and phone:
            accounts_list = dao.getAccountsByAFirstALastPhone(afirst, alast, phone)
        elif(len(args) == 3) and afirst and phone and email:
            accounts_list = dao.getAccountsByAFirstPhoneEmail(afirst, phone, email)
        elif(len(args) == 3) and alast and email and phone:
            accounts_list = dao.getAccountsByALastEmailPhone(alast, email, phone)
        elif(len(args) == 2) and afirst and alast:
            accounts_list = dao.getAccountsByAFirstALast(afirst, alast)
        elif(len(args) == 2) and afirst and email:
            accounts_list = dao.getAccountsByAFirstEmail(afirst, email)
        elif(len(args) == 2) and afirst and phone:
            accounts_list = dao.getAccountsByAFirstPhone(afirst, phone)
        elif(len(args) == 2) and alast and email:
            accounts_list = dao.getAccountsByALastEmail(alast, email)
        elif(len(args) == 2) and alast and phone:
            accounts_list = dao.getAccountsByALastPhone(alast, phone)
        elif(len(args) == 2) and email and phone:
            accounts_list = dao.getAccountsByEmailPhone(email, phone)
        elif(len(args) == 1) and afirst:
            accounts_list = dao.getAccountsByAFirst(afirst)
        elif(len(args) == 1) and alast:
            accounts_list = dao.getAccountsByALast(alast)
        elif(len(args) == 1) and email:
            accounts_list = dao.getAccountsByEmail(email)
        elif(len(args) == 1) and phone:
            accounts_list = dao.getAccountsByPhone(phone)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in accounts_list:
            result = self.build_account_dict(row)
            result_list.append(result)
        return jsonify(Accounts = result_list)

# ================ #
#     Addresses    #
# ================ #

    def getAccountsOnThisAddressID(self, addId):

        daoAdd = AddressDAO()
        dao = AccountDAO()

        if not daoAdd.getAddressById(addId):
            return jsonify(Error = 'Address Not Found'), 404

        accounts_list = dao.getAccountsWithThisAddressID(addId)
        result_list = []
        for row in accounts_list:
            result = self.build_account_dict(row)
            result_list.append(result)
        return jsonify(Accounts = result_list)

    def searchAccountsOnThisAddressID(self, addId, args):

        daoAdd = AddressDAO()
        dao = AccountDAO()

        if not daoAdd.getAddressById(addId):
            return jsonify(Error = 'Address Not Found'), 404

        afirst = args.get('afirst')
        alast = args.get('alast')
        email = args.get('email')
        phone = args.get('phone')

        accounts_list = []

        if(len(args) == 4) and afirst and alast and email and phone:
            accounts_list = dao.getAccountsOnThisAddressIDByAfirstAlastEmailPhone(addId, afirst, alast, email, phone)
        elif(len(args) == 3) and afirst and alast and email:
            accounts_list = dao.getAccountsOnThisAddressIDByAfirstAlastEmail(addId, afirst, alast, email)
        elif(len(args) == 3) and afirst and alast and phone:
            accounts_list = dao.getAccountsOnThisAddressIDByAfirstAlastPhone(addId, afirst, alast, phone)
        elif(len(args) == 3) and afirst and phone and email:
            accounts_list = dao.getAccountsOnThisAddressIDByAfirstPhoneEmail(addId, afirst, phone, email)
        elif(len(args) == 3) and alast and email and phone:
            accounts_list = dao.getAccountsOnThisAddressIDByAlastEmailPhone(addId, alast, email, phone)
        elif(len(args) == 2) and afirst and alast:
            accounts_list = dao.getAccountsOnThisAddressIDByAfirstAlast(addId, afirst, alast)
        elif(len(args) == 2) and afirst and email:
            accounts_list = dao.getAccountsOnThisAddressIDByAfirstEmail(addId, afirst, email)
        elif(len(args) == 2) and afirst and phone:
            accounts_list = dao.getAccountsOnThisAddressIDByAfirstPhone(addId, afirst, phone)
        elif(len(args) == 2) and alast and email:
            accounts_list = dao.getAccountsOnThisAddressIDByAlastEmail(addId, alast, email)
        elif(len(args) == 2) and alast and phone:
            accounts_list = dao.getAccountsOnThisAddressIDByAlastPhone(addId, alast, phone)
        elif(len(args) == 2) and email and phone:
            accounts_list = dao.getAccountsOnThisAddressIDByEmailPhone(addId, email, phone)
        elif(len(args) == 1) and afirst:
            accounts_list = dao.getAccountsOnThisAddressIDByAfirst(addId, afirst)
        elif(len(args) == 1) and alast:
            accounts_list = dao.getAccountsOnThisAddressIDByAlast(addId, alast)
        elif(len(args) == 1) and email:
            accounts_list = dao.getAccountsOnThisAddressIDByEmail(addId, email)
        elif(len(args) == 1) and phone:
            accounts_list = dao.getAccountsOnThisAddressIDByPhone(addId, phone)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in accounts_list:
            result = self.build_account_dict(row)
            result_list.append(result)
        return jsonify(Accounts = result_list)

# ================ #
#     Cities       #
# ================ #

    def getAccountsOnThisCity(self, cname):

        dao = AccountDAO()
        daoCities = CityDAO()

        if not daoCities.getCityByName(cname):
            return jsonify(Error="City Not Found"), 404

        accounts_list = dao.getAccountsOnThisCity(cname)

        result_list = []
        for row in accounts_list:
            result = self.build_account_dict(row)
            result_list.append(result)
        return jsonify(Accounts = result_list)

    def searchAccountsOnThisCity(self, cname, args):

        dao = AccountDAO()
        daoCities = CityDAO()

        if not daoCities.getCityByName(cname):
            return jsonify(Error="City Not Found"), 404

        afirst = args.get('afirst')
        alast = args.get('alast')
        email = args.get('email')
        phone = args.get('phone')

        accounts_list = []

        if(len(args) == 4) and afirst and alast and email and phone:
            accounts_list = dao.getAccountsOnThisCityAfirstAlastEmailPhone(cname, afirst, alast, email, phone)
        elif(len(args) == 3) and afirst and alast and email:
            accounts_list = dao.getAccountsOnThisCityByAfirstAlastEmail(cname, afirst, alast, email)
        elif(len(args) == 3) and afirst and alast and phone:
            accounts_list = dao.getAccountsOnThisCityByAfirstAlastPhone(cname, afirst, alast, phone)
        elif(len(args) == 3) and afirst and phone and email:
            accounts_list = dao.getAccountsOnThisCityByAfirstPhoneEmail(cname, afirst, phone, email)
        elif(len(args) == 3) and alast and email and phone:
            accounts_list = dao.getAccountsOnThisCityByAlastEmailPhone(cname, alast, email, phone)
        elif(len(args) == 2) and afirst and alast:
            accounts_list = dao.getAccountsOnThisCityByAfirstAlast(cname, afirst, alast)
        elif(len(args) == 2) and afirst and email:
            accounts_list = dao.getAccountsOnThisCityByAfirstEmail(cname, afirst, email)
        elif(len(args) == 2) and afirst and phone:
            accounts_list = dao.getAccountsOnThisCityByAfirstPhone(cname, afirst, phone)
        elif(len(args) == 2) and alast and email:
            accounts_list = dao.getAccountsOnThisCityByAlastEmail(cname, alast, email)
        elif(len(args) == 2) and alast and phone:
            accounts_list = dao.getAccountsOnThisCityByAlastPhone(cname, alast, phone)
        elif(len(args) == 2) and email and phone:
            accounts_list = dao.getAccountsOnThisCityByEmailPhone(cname, email, phone)
        elif(len(args) == 1) and afirst:
            accounts_list = dao.getAccountsOnThisCityByAfirst(cname, afirst)
        elif(len(args) == 1) and alast:
            accounts_list = dao.getAccountsOnThisCityByAlast(cname, alast)
        elif(len(args) == 1) and email:
            accounts_list = dao.getAccountsOnThisCityByEmail(cname, email)
        elif(len(args) == 1) and phone:
            accounts_list = dao.getAccountsOnThisCityByPhone(cname, phone)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in accounts_list:
            result = self.build_account_dict(row)
            result_list.append(result)
        return jsonify(Accounts = result_list)

# ================ #
#     Regions      #
# ================ #

    def getAccountsOnThisRegion(self, rname):

        daoReg = RegionDAO()
        dao = AccountDAO()

        if not daoReg.getRegionByName(rname):
            return jsonify(Error="Region Not Found"), 404

        accounts_list = dao.getAccountsOnThisRegion(rname)

        result_list = []
        for row in accounts_list:
            result = self.build_account_dict(row)
            result_list.append(result)
        return jsonify(Accounts = result_list)

    def searchAccountsOnThisRegion(self, rname, args):

        daoReg = RegionDAO()
        dao = AccountDAO()

        if not daoReg.getRegionByName(rname):
            return jsonify(Error="Region Not Found"), 404

        afirst = args.get('afirst')
        alast = args.get('alast')
        email = args.get('email')
        phone = args.get('phone')

        accounts_list = []

        if(len(args) == 4) and afirst and alast and email and phone:
            accounts_list = dao.getAccountsOnThisRegionAfirstAlastEmailPhone(rname, afirst, alast, email, phone)
        elif(len(args) == 3) and afirst and alast and email:
            accounts_list = dao.getAccountsOnThisRegionByAfirstAlastEmail(rname, afirst, alast, email)
        elif(len(args) == 3) and afirst and alast and phone:
            accounts_list = dao.getAccountsOnThisRegionByAfirstAlastPhone(rname, afirst, alast, phone)
        elif(len(args) == 3) and afirst and phone and email:
            accounts_list = dao.getAccountsOnThisRegionByAfirstPhoneEmail(rname, afirst, phone, email)
        elif(len(args) == 3) and alast and email and phone:
            accounts_list = dao.getAccountsOnThisRegionByAlastEmailPhone(rname, alast, email, phone)
        elif(len(args) == 2) and afirst and alast:
            accounts_list = dao.getAccountsOnThisRegionByAfirstAlast(rname, afirst, alast)
        elif(len(args) == 2) and afirst and email:
            accounts_list = dao.getAccountsOnThisRegionByAfirstEmail(rname, afirst, email)
        elif(len(args) == 2) and afirst and phone:
            accounts_list = dao.getAccountsOnThisRegionByAfirstPhone(rname, afirst, phone)
        elif(len(args) == 2) and alast and email:
            accounts_list = dao.getAccountsOnThisRegionByAlastEmail(rname, alast, email)
        elif(len(args) == 2) and alast and phone:
            accounts_list = dao.getAccountsOnThisRegionByAlastPhone(rname, alast, phone)
        elif(len(args) == 2) and email and phone:
            accounts_list = dao.getAccountsOnThisRegionByEmailPhone(rname, email, phone)
        elif(len(args) == 1) and afirst:
            accounts_list = dao.getAccountsOnThisRegionByAfirst(rname, afirst)
        elif(len(args) == 1) and alast:
            accounts_list = dao.getAccountsOnThisRegionByAlast(rname, alast)
        elif(len(args) == 1) and email:
            accounts_list = dao.getAccountsOnThisRegionByEmail(rname, email)
        elif(len(args) == 1) and phone:
            accounts_list = dao.getAccountsOnThisRegionByPhone(rname, phone)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in accounts_list:
            result = self.build_account_dict(row)
            result_list.append(result)
        return jsonify(Accounts = result_list)

    # ================ #
    #   Credentials    #
    # ================ #

    def getAccountWithThisUsername(self, username):

        daoCred = CredentialDAO()
        dao = AccountDAO()

        if not daoCred.getCredentialsByUsername(username):
            return jsonify(Error = 'Credentials Not Found'), 404

        accounts_list = dao.getAccountWithThisUsername(username)

        result_list = []
        for row in accounts_list:
            result = self.build_account_dict(row)
            result_list.append(result)
        return jsonify(Accounts = result_list)

    def searchAccountWithThisUsername(self, username, args):

        daoCred = CredentialDAO()
        dao = AccountDAO()

        if not daoCred.getCredentialsByUsername(username):
            return jsonify(Error = 'Credentials Not Found'), 404

        afirst = args.get('afirst')
        alast = args.get('alast')
        email = args.get('email')
        phone = args.get('phone')

        accounts_list = []

        if(len(args) == 4) and afirst and alast and email and phone:
            accounts_list = dao.getAccountsWithThisUsernameByAfirstAlastEmailPhone(username, afirst, alast, email, phone)
        elif(len(args) == 3) and afirst and alast and email:
            accounts_list = dao.getAccountsWithThisUsernameByAfirstAlastEmail(username, afirst, alast, email)
        elif(len(args) == 3) and afirst and alast and phone:
            accounts_list = dao.getAccountsWithThisUsernameByAfirstAlastPhone(username, afirst, alast, phone)
        elif(len(args) == 3) and afirst and phone and email:
            accounts_list = dao.getAccountsWithThisUsernameByAfirstPhoneEmail(username, afirst, phone, email)
        elif(len(args) == 3) and alast and email and phone:
            accounts_list = dao.getAccountsWithThisUsernameByAlastEmailPhone(username, alast, email, phone)
        elif(len(args) == 2) and afirst and alast:
            accounts_list = dao.getAccountsWithThisUsernameByAfirstAlast(username, afirst, alast)
        elif(len(args) == 2) and afirst and email:
            accounts_list = dao.getAccountsWithThisUsernameByAfirstEmail(username, afirst, email)
        elif(len(args) == 2) and afirst and phone:
            accounts_list = dao.getAccountsWithThisUsernameByAfirstPhone(username, afirst, phone)
        elif(len(args) == 2) and alast and email:
            accounts_list = dao.getAccountsWithThisUsernameByAlastEmail(username, alast, email)
        elif(len(args) == 2) and alast and phone:
            accounts_list = dao.getAccountsWithThisUsernameByAlastPhone(username, alast, phone)
        elif(len(args) == 2) and email and phone:
            accounts_list = dao.getAccountsWithThisUsernameByEmailPhone(username, email, phone)
        elif(len(args) == 1) and afirst:
            accounts_list = dao.getAccountsWithThisUsernameByAfirst(username, afirst)
        elif(len(args) == 1) and alast:
            accounts_list = dao.getAccountsWithThisUsernameByAlast(username, alast)
        elif(len(args) == 1) and email:
            accounts_list = dao.getAccountsWithThisUsernameByEmail(username, email)
        elif(len(args) == 1) and phone:
            accounts_list = dao.getAccountsWithThisUsernameByPhone(username, phone)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in accounts_list:
            result = self.build_account_dict(row)
            result_list.append(result)
        return jsonify(Accounts = result_list)