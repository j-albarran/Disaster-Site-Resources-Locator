from flask import jsonify

from dao.supplier import SupplierDAO
from dao.bank_account import BankAccountDAO
from dao.address import AddressDAO
from dao.city import CityDAO
from dao.region import RegionDAO
from dao.resource import ResourceDAO
from dao.transaction import TransactionDAO
from dao.order import OrderDAO
from dao.category import CategoryDAO

class SupplierHandler:

# =========================================================================== #
#                                 Builders                                    #
# =========================================================================== #

    def build_supplier_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['afirst'] = row[1]
        result['alast'] = row[2]
        result['email'] = row[3]
        result['phone'] = row[4]
        return result

# =========================================================================== #
#                                 Methods                                     #
# =========================================================================== #

# ================ #
#     Suppliers    #
# ================ #

    def getAllSuppliers(self):
        dao = SupplierDAO()
        suppliers_list = dao.getAllSuppliers()
        result_list = []
        for supplier in suppliers_list:
            result = self.build_supplier_dict(supplier)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def getSupplierById(self, sid):
        dao = SupplierDAO()
        row = dao.getSupplierById(sid)
        if not row:
            return jsonify(Error = "Supplier Not Found"), 404
        else:
            supplier = self.build_supplier_dict(row)
            return jsonify(Supplier = supplier)

    def searchSuppliers(self, args):

        dao = SupplierDAO()

        afirst = args.get('afirst')
        alast = args.get('alast')
        email = args.get('email')
        phone = args.get('phone')

        suppliers_list = []

        if(len(args) == 4) and afirst and alast and email and phone:
            suppliers_list = dao.getSuppliersByAFirstALastEmailPhone(afirst, alast, email, phone)
        elif(len(args) == 3) and afirst and alast and email:
            suppliers_list = dao.getSuppliersByAFirstALastEmail(afirst, alast, email)
        elif(len(args) == 3) and afirst and alast and phone:
            suppliers_list = dao.getSuppliersByAFirstALastPhone(afirst, alast, phone)
        elif(len(args) == 3) and afirst and phone and email:
            suppliers_list = dao.getSuppliersByAFirstPhoneEmail(afirst, phone, email)
        elif(len(args) == 3) and alast and email and phone:
            suppliers_list = dao.getSuppliersByALastEmailPhone(alast, email, phone)
        elif(len(args) == 2) and afirst and alast:
            suppliers_list = dao.getSuppliersByAFirstALast(afirst, alast)
        elif(len(args) == 2) and afirst and email:
            suppliers_list = dao.getSuppliersByAFirstEmail(afirst, email)
        elif(len(args) == 2) and afirst and phone:
            suppliers_list = dao.getSuppliersByAFirstPhone(afirst, phone)
        elif(len(args) == 2) and alast and email:
            suppliers_list = dao.getSuppliersByALastEmail(alast, email)
        elif(len(args) == 2) and alast and phone:
            suppliers_list = dao.getSuppliersByALastPhone(alast, phone)
        elif(len(args) == 2) and email and phone:
            suppliers_list = dao.getSuppliersByEmailPhone(email, phone)
        elif(len(args) == 1) and afirst:
            suppliers_list = dao.getSuppliersByAFirst(afirst)
        elif(len(args) == 1) and alast:
            suppliers_list = dao.getSuppliersByALast(alast)
        elif(len(args) == 1) and email:
            suppliers_list = dao.getSuppliersByEmail(email)
        elif(len(args) == 1) and phone:
            suppliers_list = dao.getSuppliersByPhone(phone)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers = result_list)

# ================ #
#     Addresses    #
# ================ #

    def getSuppliersOnThisAddressID(self, addId):

        daoAd = AddressDAO()
        dao = SupplierDAO()

        if not daoAd.getAddressById(addId):
            return jsonify(Error = 'Address Not Found'), 404

        suppliers_list = dao.getSuppliersWithThisAddressID(addId)

        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers = result_list)

    def searchSuppliersOnThisAddressID(self, addId, args):

        daoAd = AddressDAO()
        dao = SupplierDAO()

        if not daoAd.getAddressById(addId):
            return jsonify(Error = 'Address Not Found'), 404

        afirst = args.get('afirst')
        alast = args.get('alast')
        email = args.get('email')
        phone = args.get('phone')

        suppliers_list = []

        if(len(args) == 4) and afirst and alast and email and phone:
            suppliers_list = dao.getSuppliersOnThisAddressIDByAfirstAlastEmailPhone(addId, afirst, alast, email, phone)
        elif(len(args) == 3) and afirst and alast and email:
            suppliers_list = dao.getSuppliersOnThisAddressIDByAfirstAlastEmail(addId, afirst, alast, email)
        elif(len(args) == 3) and afirst and alast and phone:
            suppliers_list = dao.getSuppliersOnThisAddressIDByAfirstAlastPhone(addId, afirst, alast, phone)
        elif(len(args) == 3) and afirst and phone and email:
            suppliers_list = dao.getSuppliersOnThisAddressIDByAfirstPhoneEmail(addId, afirst, phone, email)
        elif(len(args) == 3) and alast and email and phone:
            suppliers_list = dao.getSuppliersOnThisAddressIDByAlastEmailPhone(addId, alast, email, phone)
        elif(len(args) == 2) and afirst and alast:
            suppliers_list = dao.getSuppliersOnThisAddressIDByAfirstAlast(addId, afirst, alast)
        elif(len(args) == 2) and afirst and email:
            suppliers_list = dao.getSuppliersOnThisAddressIDByAfirstEmail(addId, afirst, email)
        elif(len(args) == 2) and afirst and phone:
            suppliers_list = dao.getSuppliersOnThisAddressIDByAfirstPhone(addId, afirst, phone)
        elif(len(args) == 2) and alast and email:
            suppliers_list = dao.getSuppliersOnThisAddressIDByAlastEmail(addId, alast, email)
        elif(len(args) == 2) and alast and phone:
            suppliers_list = dao.getSuppliersOnThisAddressIDByAlastPhone(addId, alast, phone)
        elif(len(args) == 2) and email and phone:
            suppliers_list = dao.getSuppliersOnThisAddressIDByEmailPhone(addId, email, phone)
        elif(len(args) == 1) and afirst:
            suppliers_list = dao.getSuppliersOnThisAddressIDByAfirst(addId, afirst)
        elif(len(args) == 1) and alast:
            suppliers_list = dao.getSuppliersOnThisAddressIDByAlast(addId, alast)
        elif(len(args) == 1) and email:
            suppliers_list = dao.getSuppliersOnThisAddressIDByEmail(addId, email)
        elif(len(args) == 1) and phone:
            suppliers_list = dao.getSuppliersOnThisAddressIDByPhone(addId, phone)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers = result_list)

# ================ #
#     Cities       #
# ================ #

    def getSuppliersOnThisCity(self, cname):

        daoCities = CityDAO()
        dao = SupplierDAO()

        if not daoCities.getCityByName(cname):
            return jsonify(Error="City Not Found"), 404

        suppliers_list = dao.getSuppliersOnThisCity(cname)
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers = result_list)

    def searchSuppliersOnThisCity(self, cname, args):

        daoCities = CityDAO()
        dao = SupplierDAO()

        if not daoCities.getCityByName(cname):
            return jsonify(Error="City Not Found"), 404

        afirst = args.get('afirst')
        alast = args.get('alast')
        email = args.get('email')
        phone = args.get('phone')

        suppliers_list = []

        if(len(args) == 4) and afirst and alast and email and phone:
            suppliers_list = dao.getSuppliersOnThisCityAfirstAlastEmailPhone(cname, afirst, alast, email, phone)
        elif(len(args) == 3) and afirst and alast and email:
            suppliers_list = dao.getSuppliersOnThisCityByAfirstAlastEmail(cname, afirst, alast, email)
        elif(len(args) == 3) and afirst and alast and phone:
            suppliers_list = dao.getSuppliersOnThisCityByAfirstAlastPhone(cname, afirst, alast, phone)
        elif(len(args) == 3) and afirst and phone and email:
            suppliers_list = dao.getSuppliersOnThisCityByAfirstPhoneEmail(cname, afirst, phone, email)
        elif(len(args) == 3) and alast and email and phone:
            suppliers_list = dao.getSuppliersOnThisCityByAlastEmailPhone(cname, alast, email, phone)
        elif(len(args) == 2) and afirst and alast:
            suppliers_list = dao.getSuppliersOnThisCityByAfirstAlast(cname, afirst, alast)
        elif(len(args) == 2) and afirst and email:
            suppliers_list = dao.getSuppliersOnThisCityByAfirstEmail(cname, afirst, email)
        elif(len(args) == 2) and afirst and phone:
            suppliers_list = dao.getSuppliersOnThisCityByAfirstPhone(cname, afirst, phone)
        elif(len(args) == 2) and alast and email:
            suppliers_list = dao.getSuppliersOnThisCityByAlastEmail(cname, alast, email)
        elif(len(args) == 2) and alast and phone:
            suppliers_list = dao.getSuppliersOnThisCityByAlastPhone(cname, alast, phone)
        elif(len(args) == 2) and email and phone:
            suppliers_list = dao.getSuppliersOnThisCityByEmailPhone(cname, email, phone)
        elif(len(args) == 1) and afirst:
            suppliers_list = dao.getSuppliersOnThisCityByAfirst(cname, afirst)
        elif(len(args) == 1) and alast:
            suppliers_list = dao.getSuppliersOnThisCityByAlast(cname, alast)
        elif(len(args) == 1) and email:
            suppliers_list = dao.getSuppliersOnThisCityByEmail(cname, email)
        elif(len(args) == 1) and phone:
            suppliers_list = dao.getSuppliersOnThisCityByPhone(cname, phone)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers = result_list)

# ================ #
#     Regions      #
# ================ #

    def getSuppliersOnThisRegion(self, rname):

        daoReg = RegionDAO()
        dao = SupplierDAO()

        if not daoReg.getRegionByName(rname):
            return jsonify(Error="Region Not Found"), 404

        suppliers_list = dao.getSuppliersOnThisRegion(rname)
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers = result_list)

    def searchSuppliersOnThisRegion(self, rname, args):

        daoReg = RegionDAO()
        dao = SupplierDAO()

        if not daoReg.getRegionByName(rname):
            return jsonify(Error="Region Not Found"), 404

        afirst = args.get('afirst')
        alast = args.get('alast')
        email = args.get('email')
        phone = args.get('phone')

        suppliers_list = []

        if(len(args) == 4) and afirst and alast and email and phone:
            suppliers_list = dao.getSuppliersOnThisRegionAfirstAlastEmailPhone(rname, afirst, alast, email, phone)
        elif(len(args) == 3) and afirst and alast and email:
            suppliers_list = dao.getSuppliersOnThisRegionByAfirstAlastEmail(rname, afirst, alast, email)
        elif(len(args) == 3) and afirst and alast and phone:
            suppliers_list = dao.getSuppliersOnThisRegionByAfirstAlastPhone(rname, afirst, alast, phone)
        elif(len(args) == 3) and afirst and phone and email:
            suppliers_list = dao.getSuppliersOnThisRegionByAfirstPhoneEmail(rname, afirst, phone, email)
        elif(len(args) == 3) and alast and email and phone:
            suppliers_list = dao.getSuppliersOnThisRegionByAlastEmailPhone(rname, alast, email, phone)
        elif(len(args) == 2) and afirst and alast:
            suppliers_list = dao.getSuppliersOnThisRegionByAfirstAlast(rname, afirst, alast)
        elif(len(args) == 2) and afirst and email:
            suppliers_list = dao.getSuppliersOnThisRegionByAfirstEmail(rname, afirst, email)
        elif(len(args) == 2) and afirst and phone:
            suppliers_list = dao.getSuppliersOnThisRegionByAfirstPhone(rname, afirst, phone)
        elif(len(args) == 2) and alast and email:
            suppliers_list = dao.getSuppliersOnThisRegionByAlastEmail(rname, alast, email)
        elif(len(args) == 2) and alast and phone:
            suppliers_list = dao.getSuppliersOnThisRegionByAlastPhone(rname, alast, phone)
        elif(len(args) == 2) and email and phone:
            suppliers_list = dao.getSuppliersOnThisRegionByEmailPhone(rname, email, phone)
        elif(len(args) == 1) and afirst:
            suppliers_list = dao.getSuppliersOnThisRegionByAfirst(rname, afirst)
        elif(len(args) == 1) and alast:
            suppliers_list = dao.getSuppliersOnThisRegionByAlast(rname, alast)
        elif(len(args) == 1) and email:
            suppliers_list = dao.getSuppliersOnThisRegionByEmail(rname, email)
        elif(len(args) == 1) and phone:
            suppliers_list = dao.getSuppliersOnThisRegionByPhone(rname, phone)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers = result_list)

# ================ #
#   Bank Accounts  #
# ================ #

    def getSupplierOfThisBankAccount(self, bid):

        daoBank = BankAccountDAO()
        dao = SupplierDAO()

        if not daoBank.getBankAccountById(bid):
            return jsonify(Error = 'Bank Account Not Found'), 404

        suppliers_list = dao.getSupplierOfThisBankAccount(bid)
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Supplier = result_list)

    def searchSupplierOfThisBankAccount(self, bid, args):

        daoBank = BankAccountDAO()
        dao = SupplierDAO()

        if not daoBank.getBankAccountById(bid):
            return jsonify(Error = 'Bank Account Not Found'), 404

        afirst = args.get('afirst')
        alast = args.get('alast')
        email = args.get('email')
        phone = args.get('phone')

        suppliers_list = []

        if(len(args) == 4) and afirst and alast and email and phone:
            suppliers_list = dao.getSupplierOfThisBankAccountByAfirstAlastEmailPhone(bid, afirst, alast, email, phone)
        elif(len(args) == 3) and afirst and alast and email:
            suppliers_list = dao.getSupplierOfThisBankAccountByAfirstAlastEmail(bid, afirst, alast, email)
        elif(len(args) == 3) and afirst and alast and phone:
            suppliers_list = dao.getSupplierOfThisBankAccountByAfirstAlastPhone(bid, afirst, alast, phone)
        elif(len(args) == 3) and afirst and phone and email:
            suppliers_list = dao.getSupplierOfThisBankAccountByAfirstPhoneEmail(bid, afirst, phone, email)
        elif(len(args) == 3) and alast and email and phone:
            suppliers_list = dao.getSupplierOfThisBankAccountByAlastEmailPhone(bid, alast, email, phone)
        elif(len(args) == 2) and afirst and alast:
            suppliers_list = dao.getSupplierOfThisBankAccountByAfirstAlast(bid, afirst, alast)
        elif(len(args) == 2) and afirst and email:
            suppliers_list = dao.getSupplierOfThisBankAccountByAfirstEmail(bid, afirst, email)
        elif(len(args) == 2) and afirst and phone:
            suppliers_list = dao.getSupplierOfThisBankAccountByAfirstPhone(bid, afirst, phone)
        elif(len(args) == 2) and alast and email:
            suppliers_list = dao.getSupplierOfThisBankAccountByAlastEmail(bid, alast, email)
        elif(len(args) == 2) and alast and phone:
            suppliers_list = dao.getSupplierOfThisBankAccountByAlastPhone(bid, alast, phone)
        elif(len(args) == 2) and email and phone:
            suppliers_list = dao.getSupplierOfThisBankAccountByEmailPhone(bid, email, phone)
        elif(len(args) == 1) and afirst:
            suppliers_list = dao.getSupplierOfThisBankAccountByAfirst(bid, afirst)
        elif(len(args) == 1) and alast:
            suppliers_list = dao.getSupplierOfThisBankAccountByAlast(bid, alast)
        elif(len(args) == 1) and email:
            suppliers_list = dao.getSupplierOfThisBankAccountByEmail(bid, email)
        elif(len(args) == 1) and phone:
            suppliers_list = dao.getSupplierOfThisBankAccountByPhone(bid, phone)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers = result_list)

# ================ #
#     Resources    #
# ================ #

    def getSuppliersOfThisResource(self, rsid):

        daoRes = ResourceDAO()
        dao = SupplierDAO()

        if not daoRes.getResourceById(rsid):
            return jsonify(Error = 'Resource Not Found'), 404

        suppliers_list = dao.getSuppliersOfThisResource(rsid)

        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Supplier = result_list)

    def searchSuppliersOfThisResource(self, rsid, args):

        daoRes = ResourceDAO()
        dao = SupplierDAO()

        if not daoRes.getResourceById(rsid):
            return jsonify(Error = 'Resource Not Found'), 404

        afirst = args.get('afirst')
        alast = args.get('alast')
        email = args.get('email')
        phone = args.get('phone')

        suppliers_list = []

        if(len(args) == 4) and afirst and alast and email and phone:
            suppliers_list = dao.getSupplierOfThisResourceByAfirstAlastEmailPhone(rsid, afirst, alast, email, phone)
        elif(len(args) == 3) and afirst and alast and email:
            suppliers_list = dao.getSupplierOfThisResourceByAfirstAlastEmail(rsid, afirst, alast, email)
        elif(len(args) == 3) and afirst and alast and phone:
            suppliers_list = dao.getSupplierOfThisResourceByAfirstAlastPhone(rsid, afirst, alast, phone)
        elif(len(args) == 3) and afirst and phone and email:
            suppliers_list = dao.getSupplierOfThisResourceByAfirstPhoneEmail(rsid, afirst, phone, email)
        elif(len(args) == 3) and alast and email and phone:
            suppliers_list = dao.getSupplierOfThisResourceByAlastEmailPhone(rsid, alast, email, phone)
        elif(len(args) == 2) and afirst and alast:
            suppliers_list = dao.getSupplierOfThisResourceByAfirstAlast(rsid, afirst, alast)
        elif(len(args) == 2) and afirst and email:
            suppliers_list = dao.getSupplierOfThisResourceByAfirstEmail(rsid, afirst, email)
        elif(len(args) == 2) and afirst and phone:
            suppliers_list = dao.getSupplierOfThisResourceByAfirstPhone(rsid, afirst, phone)
        elif(len(args) == 2) and alast and email:
            suppliers_list = dao.getSupplierOfThisResourceByAlastEmail(rsid, alast, email)
        elif(len(args) == 2) and alast and phone:
            suppliers_list = dao.getSupplierOfThisResourceByAlastPhone(rsid, alast, phone)
        elif(len(args) == 2) and email and phone:
            suppliers_list = dao.getSupplierOfThisResourceByEmailPhone(rsid, email, phone)
        elif(len(args) == 1) and afirst:
            suppliers_list = dao.getSupplierOfThisResourceByAfirst(rsid, afirst)
        elif(len(args) == 1) and alast:
            suppliers_list = dao.getSupplierOfThisResourceByAlast(rsid, alast)
        elif(len(args) == 1) and email:
            suppliers_list = dao.getSupplierOfThisResourceByEmail(rsid, email)
        elif(len(args) == 1) and phone:
            suppliers_list = dao.getSupplierOfThisResourceByPhone(rsid, phone)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers = result_list)

# ================ #
#    Categories    #
# ================ #

    def getSuppliersOfThisCategory(self, cat_name):

        daoCat = CategoryDAO()
        dao = SupplierDAO()

        if not daoCat.getCategoryByName(cat_name):
            return jsonify(Error = 'Category Not Found'), 404

        suppliers_list = dao.getSupplierOfThisCategory(cat_name)

        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Supplier = result_list)

    def searchSuppliersOfThisCategory(self, cat_name, args):

        daoCat = CategoryDAO()
        dao = SupplierDAO()

        if not daoCat.getCategoryByName(cat_name):
            return jsonify(Error = 'Category Not Found'), 404

        afirst = args.get('afirst')
        alast = args.get('alast')
        email = args.get('email')
        phone = args.get('phone')

        suppliers_list = []

        if(len(args) == 4) and afirst and alast and email and phone:
            suppliers_list = dao.getSupplierOfThisCategoryByAfirstAlastEmailPhone(cat_name, afirst, alast, email, phone)
        elif(len(args) == 3) and afirst and alast and email:
            suppliers_list = dao.getSupplierOfThisCategoryByAfirstAlastEmail(cat_name, afirst, alast, email)
        elif(len(args) == 3) and afirst and alast and phone:
            suppliers_list = dao.getSupplierOfThisCategoryByAfirstAlastPhone(cat_name, afirst, alast, phone)
        elif(len(args) == 3) and afirst and phone and email:
            suppliers_list = dao.getSupplierOfThisCategoryByAfirstPhoneEmail(cat_name, afirst, phone, email)
        elif(len(args) == 3) and alast and email and phone:
            suppliers_list = dao.getSupplierOfThisCategoryByAlastEmailPhone(cat_name, alast, email, phone)
        elif(len(args) == 2) and afirst and alast:
            suppliers_list = dao.getSupplierOfThisCategoryByAfirstAlast(cat_name, afirst, alast)
        elif(len(args) == 2) and afirst and email:
            suppliers_list = dao.getSupplierOfThisCategoryByAfirstEmail(cat_name, afirst, email)
        elif(len(args) == 2) and afirst and phone:
            suppliers_list = dao.getSupplierOfThisCategoryByAfirstPhone(cat_name, afirst, phone)
        elif(len(args) == 2) and alast and email:
            suppliers_list = dao.getSupplierOfThisCategoryByAlastEmail(cat_name, alast, email)
        elif(len(args) == 2) and alast and phone:
            suppliers_list = dao.getSupplierOfThisCategoryByAlastPhone(cat_name, alast, phone)
        elif(len(args) == 2) and email and phone:
            suppliers_list = dao.getSupplierOfThisCategoryByEmailPhone(cat_name, email, phone)
        elif(len(args) == 1) and afirst:
            suppliers_list = dao.getSupplierOfThisCategoryByAfirst(cat_name, afirst)
        elif(len(args) == 1) and alast:
            suppliers_list = dao.getSupplierOfThisCategoryByAlast(cat_name, alast)
        elif(len(args) == 1) and email:
            suppliers_list = dao.getSupplierOfThisCategoryByEmail(cat_name, email)
        elif(len(args) == 1) and phone:
            suppliers_list = dao.getSupplierOfThisCategoryByPhone(cat_name, phone)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers = result_list)

# ================ #
#   Transactions   #
# ================ #

    def getSupplierOfThisTransaction(self, tid):

        daoTrans = TransactionDAO()
        dao = SupplierDAO()

        if not daoTrans.getTransactionById(tid):
            return jsonify(Error = 'Transaction Not Found'), 404

        suppliers_list = dao.getSupplierOfThisTransaction(tid)

        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Supplier = result_list)

    def searchSupplierOfThisTransaction(self, tid, args):

        daoTrans = TransactionDAO()
        dao = SupplierDAO()

        if not daoTrans.getTransactionById(tid):
            return jsonify(Error = 'Transaction Not Found'), 404

        afirst = args.get('afirst')
        alast = args.get('alast')
        email = args.get('email')
        phone = args.get('phone')

        suppliers_list = []

        if(len(args) == 4) and afirst and alast and email and phone:
            suppliers_list = dao.getSupplierOfThisTransactionByAfirstAlastEmailPhone(tid, afirst, alast, email, phone)
        elif(len(args) == 3) and afirst and alast and email:
            suppliers_list = dao.getSupplierOfThisTransactionByAfirstAlastEmail(tid, afirst, alast, email)
        elif(len(args) == 3) and afirst and alast and phone:
            suppliers_list = dao.getSupplierOfThisTransactionByAfirstAlastPhone(tid, afirst, alast, phone)
        elif(len(args) == 3) and afirst and phone and email:
            suppliers_list = dao.getSupplierOfThisTransactionByAfirstPhoneEmail(tid, afirst, phone, email)
        elif(len(args) == 3) and alast and email and phone:
            suppliers_list = dao.getSupplierOfThisTransactionByAlastEmailPhone(tid, alast, email, phone)
        elif(len(args) == 2) and afirst and alast:
            suppliers_list = dao.getSupplierOfThisTransactionByAfirstAlast(tid, afirst, alast)
        elif(len(args) == 2) and afirst and email:
            suppliers_list = dao.getSupplierOfThisTransactionByAfirstEmail(tid, afirst, email)
        elif(len(args) == 2) and afirst and phone:
            suppliers_list = dao.getSupplierOfThisTransactionByAfirstPhone(tid, afirst, phone)
        elif(len(args) == 2) and alast and email:
            suppliers_list = dao.getSupplierOfThisTransactionByAlastEmail(tid, alast, email)
        elif(len(args) == 2) and alast and phone:
            suppliers_list = dao.getSupplierOfThisTransactionByAlastPhone(tid, alast, phone)
        elif(len(args) == 2) and email and phone:
            suppliers_list = dao.getSupplierOfThisTransactionByEmailPhone(tid, email, phone)
        elif(len(args) == 1) and afirst:
            suppliers_list = dao.getSupplierOfThisTransactionByAfirst(tid, afirst)
        elif(len(args) == 1) and alast:
            suppliers_list = dao.getSupplierOfThisTransactionByAlast(tid, alast)
        elif(len(args) == 1) and email:
            suppliers_list = dao.getSupplierOfThisTransactionByEmail(tid, email)
        elif(len(args) == 1) and phone:
            suppliers_list = dao.getSupplierOfThisTransactionByPhone(tid, phone)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers = result_list)

# ================ #
#   Orders Info    #
# ================ #

    def getSuppliersOfThisOrderInfo(self, oid):

        daoOI = OrderDAO()
        dao = SupplierDAO()

        if not daoOI.getOrderById(oid):
            return jsonify(Error = 'Order Info Not Found'), 404

        suppliers_list = dao.getSupplierOfThisOrderInfo(oid)

        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Supplier = result_list)

    def searchSuppliersOfThisOrderInfo(self, oid, args):

        daoOI = OrderDAO()
        dao = SupplierDAO()

        if not daoOI.getOrderById(oid):
            return jsonify(Error = 'Order Info Not Found'), 404

        afirst = args.get('afirst')
        alast = args.get('alast')
        email = args.get('email')
        phone = args.get('phone')

        suppliers_list = []

        if(len(args) == 4) and afirst and alast and email and phone:
            suppliers_list = dao.getSupplierOfThisOrderInfoByAfirstAlastEmailPhone(oid, afirst, alast, email, phone)
        elif(len(args) == 3) and afirst and alast and email:
            suppliers_list = dao.getSupplierOfThisOrderInfoByAfirstAlastEmail(oid, afirst, alast, email)
        elif(len(args) == 3) and afirst and alast and phone:
            suppliers_list = dao.getSupplierOfThisOrderInfoByAfirstAlastPhone(oid, afirst, alast, phone)
        elif(len(args) == 3) and afirst and phone and email:
            suppliers_list = dao.getSupplierOfThisOrderInfoByAfirstPhoneEmail(oid, afirst, phone, email)
        elif(len(args) == 3) and alast and email and phone:
            suppliers_list = dao.getSupplierOfThisOrderInfoByAlastEmailPhone(oid, alast, email, phone)
        elif(len(args) == 2) and afirst and alast:
            suppliers_list = dao.getSupplierOfThisOrderInfoByAfirstAlast(oid, afirst, alast)
        elif(len(args) == 2) and afirst and email:
            suppliers_list = dao.getSupplierOfThisOrderInfoByAfirstEmail(oid, afirst, email)
        elif(len(args) == 2) and afirst and phone:
            suppliers_list = dao.getSupplierOfThisOrderInfoByAfirstPhone(oid, afirst, phone)
        elif(len(args) == 2) and alast and email:
            suppliers_list = dao.getSupplierOfThisOrderInfoByAlastEmail(oid, alast, email)
        elif(len(args) == 2) and alast and phone:
            suppliers_list = dao.getSupplierOfThisOrderInfoByAlastPhone(oid, alast, phone)
        elif(len(args) == 2) and email and phone:
            suppliers_list = dao.getSupplierOfThisOrderInfoByEmailPhone(oid, email, phone)
        elif(len(args) == 1) and afirst:
            suppliers_list = dao.getSupplierOfThisOrderInfoByAfirst(oid, afirst)
        elif(len(args) == 1) and alast:
            suppliers_list = dao.getSupplierOfThisOrderInfoByAlast(oid, alast)
        elif(len(args) == 1) and email:
            suppliers_list = dao.getSupplierOfThisOrderInfoByEmail(oid, email)
        elif(len(args) == 1) and phone:
            suppliers_list = dao.getSupplierOfThisOrderInfoByPhone(oid, phone)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers = result_list)

# ============================================ #
#   Suppliers of This Resource on This City    #
# ============================================ #

    def getSupplierOfThisResourceOnThisCity(self, cname, rsid):

        daoRes = ResourceDAO()
        daoCity = CityDAO()
        dao = SupplierDAO()

        if not daoCity.getCityByName(cname):
            return jsonify(Error = 'City Not Found'), 404

        if not daoRes.getResourceById(rsid):
            return jsonify(Error = 'Resource Not Found'), 404

        suppliers_list = dao.getSupplierOfThisResourceOnThisCity(cname, rsid)

        result_list = []

        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Supplier = result_list)

    def searchSupplierOfThisResourceOnThisCity(self,cname, rsid, args):

        daoRes = ResourceDAO()
        daoCity = CityDAO()
        dao = SupplierDAO()

        if not daoCity.getCityByName(cname):
            return jsonify(Error = 'City Not Found'), 404

        if not daoRes.getResourceById(rsid):
            return jsonify(Error = 'Resource Not Found'), 404

        afirst = args.get('afirst')
        alast = args.get('alast')
        email = args.get('email')
        phone = args.get('phone')

        suppliers_list = []

        if(len(args) == 4) and afirst and alast and email and phone:
            suppliers_list = dao.getSupplierOfThisResourceOnThisCityByAfirstAlastEmailPhone(cname, rsid, afirst, alast, email, phone)
        elif(len(args) == 3) and afirst and alast and email:
            suppliers_list = dao.getSupplierOfThisResourceOnThisCityByAfirstAlastEmail(cname, rsid, afirst, alast, email)
        elif(len(args) == 3) and afirst and alast and phone:
            suppliers_list = dao.getSupplierOfThisResourceOnThisCityByAfirstAlastPhone(cname, rsid, afirst, alast, phone)
        elif(len(args) == 3) and afirst and phone and email:
            suppliers_list = dao.getSupplierOfThisResourceOnThisCityByAfirstPhoneEmail(cname, rsid, afirst, phone, email)
        elif(len(args) == 3) and alast and email and phone:
            suppliers_list = dao.getSupplierOfThisResourceOnThisCityByAlastEmailPhone(cname, rsid, alast, email, phone)
        elif(len(args) == 2) and afirst and alast:
            suppliers_list = dao.getSupplierOfThisResourceOnThisCityByAfirstAlast(cname, rsid, afirst, alast)
        elif(len(args) == 2) and afirst and email:
            suppliers_list = dao.getSupplierOfThisResourceOnThisCityByAfirstEmail(cname, rsid, afirst, email)
        elif(len(args) == 2) and afirst and phone:
            suppliers_list = dao.getSupplierOfThisResourceOnThisCityByAfirstPhone(cname, rsid, afirst, phone)
        elif(len(args) == 2) and alast and email:
            suppliers_list = dao.getSupplierOfThisResourceOnThisCityByAlastEmail(cname, rsid, alast, email)
        elif(len(args) == 2) and alast and phone:
            suppliers_list = dao.getSupplierOfThisResourceOnThisCityByAlastPhone(cname, rsid, alast, phone)
        elif(len(args) == 2) and email and phone:
            suppliers_list = dao.getSupplierOfThisResourceOnThisCityByEmailPhone(cname, rsid, email, phone)
        elif(len(args) == 1) and afirst:
            suppliers_list = dao.getSupplierOfThisResourceOnThisCityByAfirst(cname, rsid, afirst)
        elif(len(args) == 1) and alast:
            suppliers_list = dao.getSupplierOfThisResourceOnThisCityByAlast(cname, rsid, alast)
        elif(len(args) == 1) and email:
            suppliers_list = dao.getSupplierOfThisResourceOnThisCityByEmail(cname, rsid, email)
        elif(len(args) == 1) and phone:
            suppliers_list = dao.getSupplierOfThisResourceOnThisCityByPhone(cname, rsid, phone)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers = result_list)

# ============================================ #
#   Suppliers of This Resource on This Region  #
# ============================================ #

    def getSupplierOfThisResourceOnThisRegion(self, rname, rsid):

        daoRes = ResourceDAO()
        daoRegion = RegionDAO()
        dao = SupplierDAO()

        if not daoRegion.getRegionByName(rname):
            return jsonify(Error = 'Region Not Found'), 404

        if not daoRes.getResourceById(rsid):
            return jsonify(Error = 'Resource Not Found'), 404

        suppliers_list = dao.getSupplierOfThisResourceOnThisRegion(rname, rsid)

        result_list = []

        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Supplier = result_list)

    def searchSupplierOfThisResourceOnThisRegion(self,rname, rsid, args):

        daoRes = ResourceDAO()
        daoRegion = RegionDAO()
        dao = SupplierDAO()

        if not daoRegion.getRegionByName(rname):
            return jsonify(Error = 'Region Not Found'), 404

        if not daoRes.getResourceById(rsid):
            return jsonify(Error = 'Resource Not Found'), 404

        afirst = args.get('afirst')
        alast = args.get('alast')
        email = args.get('email')
        phone = args.get('phone')

        suppliers_list = []

        if(len(args) == 4) and afirst and alast and email and phone:
            suppliers_list = dao.getSupplierOfThisResourceOnThisRegionByAfirstAlastEmailPhone(rname, rsid, afirst, alast, email, phone)
        elif(len(args) == 3) and afirst and alast and email:
            suppliers_list = dao.getSupplierOfThisResourceOnThisRegionByAfirstAlastEmail(rname, rsid, afirst, alast, email)
        elif(len(args) == 3) and afirst and alast and phone:
            suppliers_list = dao.getSupplierOfThisResourceOnThisRegionByAfirstAlastPhone(rname, rsid, afirst, alast, phone)
        elif(len(args) == 3) and afirst and phone and email:
            suppliers_list = dao.getSupplierOfThisResourceOnThisRegionByAfirstPhoneEmail(rname, rsid, afirst, phone, email)
        elif(len(args) == 3) and alast and email and phone:
            suppliers_list = dao.getSupplierOfThisResourceOnThisRegionByAlastEmailPhone(rname, rsid, alast, email, phone)
        elif(len(args) == 2) and afirst and alast:
            suppliers_list = dao.getSupplierOfThisResourceOnThisRegionByAfirstAlast(rname, rsid, afirst, alast)
        elif(len(args) == 2) and afirst and email:
            suppliers_list = dao.getSupplierOfThisResourceOnThisRegionByAfirstEmail(rname, rsid, afirst, email)
        elif(len(args) == 2) and afirst and phone:
            suppliers_list = dao.getSupplierOfThisResourceOnThisRegionByAfirstPhone(rname, rsid, afirst, phone)
        elif(len(args) == 2) and alast and email:
            suppliers_list = dao.getSupplierOfThisResourceOnThisRegionByAlastEmail(rname, rsid, alast, email)
        elif(len(args) == 2) and alast and phone:
            suppliers_list = dao.getSupplierOfThisResourceOnThisRegionByAlastPhone(rname, rsid, alast, phone)
        elif(len(args) == 2) and email and phone:
            suppliers_list = dao.getSupplierOfThisResourceOnThisRegionByEmailPhone(rname, rsid, email, phone)
        elif(len(args) == 1) and afirst:
            suppliers_list = dao.getSupplierOfThisResourceOnThisRegionByAfirst(rname, rsid, afirst)
        elif(len(args) == 1) and alast:
            suppliers_list = dao.getSupplierOfThisResourceOnThisRegionByAlast(rname, rsid, alast)
        elif(len(args) == 1) and email:
            suppliers_list = dao.getSupplierOfThisResourceOnThisRegionByEmail(rname, rsid, email)
        elif(len(args) == 1) and phone:
            suppliers_list = dao.getSupplierOfThisResourceOnThisRegionByPhone(rname, rsid, phone)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers = result_list)