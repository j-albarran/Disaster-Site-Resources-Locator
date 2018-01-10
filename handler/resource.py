from flask import jsonify
from dao.resource import ResourceDAO
from dao.city import CityDAO
from dao.region import RegionDAO
from dao.supplier import SupplierDAO
from dao.keyword import KeywordDAO
from dao.category import CategoryDAO
from dao.transaction import TransactionDAO
from dao.order import OrderDAO

class ResourceHandler:

    def build_resource_dict(self, row):
        result = {}
        result['rsid'] = row[0]
        result['rsname'] = row[1]
        result['rdescription'] = row[2]
        result['r_changed_date'] = row[3]
        result['rqty'] = row[4]
        result['rprice'] = row[5]
        result['r_supply_date'] = row[6]
        return result

    def build_resource_attributes(self, rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date):
        result = {}
        result['rsid'] = rsid
        result['rsname'] = rsname
        result['rdescription'] = rdescription
        result['r_changed_date'] = r_changed_date
        result['rqty'] = rqty
        result['rprice'] = rprice
        result['r_supply_date'] = r_supply_date
        return result

    def getAllResources(self):
        dao = ResourceDAO()
        resource_list = dao.getAllResources()
        result_list = []
        for row in resource_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error = "Resources Not Found"), 404
        else:
            return jsonify(Resources = result_list)

    def searchResources(self, args):
        rsname = args.get('rsname')
        r_changed_date = args.get('r_changed_date')
        rqty = args.get('rqty')
        rprice = args.get('rprice')
        r_supply_date = args.get('r_supply_date')
        dao = ResourceDAO()
        resource_list = []
        if (len(args) == 5) and rsname and r_changed_date and rqty and rprice and r_supply_date:
            resource_list = dao.getResourceByNameChangedDateQtyPriceSupplyDate(rsname, r_changed_date, rqty, rprice, r_supply_date)
        elif (len(args) == 4) and rsname and r_changed_date and rqty and rprice:
            resource_list = dao.getResourceByNameChangedDateQtyPrice(rsname, r_changed_date, rqty, rprice)
        elif (len(args) == 4) and rsname and r_changed_date and rqty and r_supply_date:
            resource_list = dao.getResourceByNameChangedDateQtySupplyDate(rsname, r_changed_date, rqty, r_supply_date)
        elif (len(args) == 4) and rsname and r_changed_date and rprice and r_supply_date:
            resource_list = dao.getResourceByNameChangedDatePriceSupplyDate(rsname, r_changed_date, rprice, r_supply_date)
        elif (len(args) == 4) and rsname and rqty and rprice and r_supply_date:
            resource_list = dao.getResourceByNameQtyPriceSupplyDate(rsname, rqty, rprice, r_supply_date)
        elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
            resource_list = dao.getResourceByChangedDateQtyPriceSupplyDate(r_changed_date, rqty, rprice, r_supply_date)
        elif (len(args) == 3) and rsname and r_changed_date and rqty:
            resource_list = dao.getResourceByNameChangedDateQty(rsname, r_changed_date, rqty)
        elif (len(args) == 3) and rsname and r_changed_date and rprice:
            resource_list = dao.getResourceByNameChangedDatePrice(rsname, r_changed_date, rprice)
        elif (len(args) == 3) and rsname and r_changed_date and r_supply_date:
            resource_list = dao.getResourceByNameChangedDateSupplyDate(rsname, r_changed_date, r_supply_date)
        elif (len(args) == 3) and rsname and rqty and rprice:
            resource_list = dao.getResourceByNameQtyPrice(rsname, rqty, rprice)
        elif (len(args) == 3) and rsname and rqty and r_supply_date:
            resource_list = dao.getResourceByNameQtySupplyDate(rsname, rqty, r_supply_date)
        elif (len(args) == 3) and rsname and rprice and r_supply_date:
            resource_list = dao.getResourceByNamePriceSupplyDate(rsname, rprice, r_supply_date)
        elif (len(args) == 3) and r_changed_date and rqty and rprice:
            resource_list = dao.getResourceByChangedDateQtyPrice(r_changed_date, rqty, rprice)
        elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
            resource_list = dao.getResourceByChangedDateQtySupplyDate(r_changed_date, rqty, r_supply_date)
        elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
            resource_list = dao.getResourceByChangedDatePriceSupplyDate(r_changed_date, rprice, r_supply_date)
        elif (len(args) == 3) and rqty and rprice and r_supply_date:
            resource_list = dao.getResourceByQtyPriceSupplyDate(rqty, rprice, r_supply_date)
        elif (len(args) == 2) and rsname and r_changed_date:
            resource_list = dao.getResourceByNameChangedDate(rsname, r_changed_date)
        elif (len(args) == 2) and rsname and rqty:
            resource_list = dao.getResourceByNameQty(rsname, rqty)
        elif (len(args) == 2) and rsname and rprice:
            resource_list = dao.getResourceByNamePrice(rsname, rprice)
        elif (len(args) == 2) and rsname and r_supply_date:
            resource_list = dao.getResourceByNameSupplyDate(rsname, r_supply_date)
        elif (len(args) == 2) and r_changed_date and rqty:
            resource_list = dao.getResourceByChangedDateQty(r_changed_date, rqty)
        elif (len(args) == 2) and r_changed_date and rprice:
            resource_list = dao.getResourceByChangedDatePrice(r_changed_date, rprice)
        elif (len(args) == 2) and r_changed_date and r_supply_date:
            resource_list = dao.getResourceByChangedDateSupplyDate(r_changed_date, r_supply_date)
        elif (len(args) == 2) and rqty and rprice:
            resource_list = dao.getResourceByQtyPrice(rqty, rprice)
        elif (len(args) == 2) and rqty and r_supply_date:
            resource_list = dao.getResourceByQtySupplyDate(rqty, r_supply_date)
        elif (len(args) == 2) and rprice and r_supply_date:
            resource_list = dao.getResourceByPriceSupplyDate(rprice, r_supply_date)
        elif (len(args) == 1) and rsname:
            resource_list = dao.getResourceByName(rsname)
        elif (len(args) == 1) and r_changed_date:
            resource_list = dao.getResourceByChangedDate(r_changed_date)
        elif (len(args) == 1) and rqty:
            resource_list = dao.getResourceByQty(rqty)
        elif (len(args) == 1) and rprice:
            resource_list = dao.getResourceByPrice(rprice)
        elif (len(args) == 1) and r_supply_date:
            resource_list = dao.getResourceBySupplyDate(r_supply_date)
        else:
            return jsonify(Error = "Malformed Query String"), 400
        result_list = []
        for row in resource_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error = "Resource Not Found"), 404
        else:
            return jsonify(Resources = result_list)

    def getResourceById(self, rsid):
        dao = ResourceDAO()
        resource = dao.getResourceById(rsid)
        if not resource:
            return jsonify(Error = "Resource Not Found"), 404
        else:
            result = self.build_resource_dict(resource)
            return jsonify(Resource = result)

    def getAvailabilityOfResourcesById(self, rsid):
        dao = ResourceDAO()
        resource = dao.getResourceById(rsid)
        if not resource:
            return jsonify(Error = "Resource Not Found"), 404
        else:
            resource = dao.getAvailabilityOfResourcesById(rsid)
            result = {}
            result['rsid'] = resource[0]
            result['rsname'] = resource[1]
            result['available'] = resource[2]
            return jsonify(Resource = result)

    def getAvailabilityOfResources(self):
        dao = ResourceDAO()
        resource_list = dao.getAvailabilityOfResources()
        result_list = []
        for resource in resource_list:
            result = {}
            result['rsid'] = resource[0]
            result['rsname'] = resource[1]
            result['available'] = resource[2]
            result_list.append(result)
        if not result_list:
            return jsonify(Error = "Resources Not Found"), 404
        else:
            return jsonify(Resources = result_list)

    def insertResource(self, form):
        if len(form) != 6:
            return jsonify(Error = "Malformed Post Request"), 400
        else:
            rsname = form['rsname']
            rdescription = form['rdescription']
            r_changed_date = form['r_changed_date']
            rqty = form['rqty']
            rprice = form['rprice']
            r_supply_date = form['r_supply_date']
            if rsname and rdescription and r_changed_date and rqty and rprice and r_supply_date:
                dao = ResourceDAO()
                rsid = dao.insert(rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date)
                result = self.build_resource_attributes(rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date)
                return jsonify(Resource = result), 201
            else:
                return jsonify(Error = "Unexpected attributes in post request"), 400

    def updateResource(self, rsid, form):
        dao = ResourceDAO()
        if not dao.getResourceById(rsid):
            return jsonify(Error = "Resource Not Found"), 404
        else:
            if len(form) != 6:
                return jsonify(Error = "Malformed Update Request"), 400
            else:
                rsname = form['rsname']
                rdescription = form['rdescription']
                r_changed_date = form['r_changed_date']
                rqty = form['rqty']
                rprice = form['rprice']
                r_supply_date = form['r_supply_date']
                if rsname and rdescription and r_changed_date and rqty and rprice and r_supply_date:
                    dao.update(rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date)
                    result = self.build_resource_attributes(rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date)
                    return jsonify(Resource = result), 201
                else:
                    return jsonify(Error = "Unexpected attributes in post request"), 400

    def deleteResource(self, rsid):
        dao = ResourceDAO()
        if not dao.getResourceById(rsid):
            return jsonify(Error = "Resource Not Found"), 404
        else:
            dao.delete(rsid)
            return jsonify(DeleteStatus = "OK"), 200

    def getResourcesByCityName(self, cname):
        if not CityDAO().getCityByName(cname):
            return jsonify(Error = "City Not Found"), 404
        else:
            resource_list = ResourceDAO().getResourcesByCityName(cname)
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resources Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def searchResourcesByCityName(self, cname, args):
        if not CityDAO().getCityByName(cname):
            return jsonify(Error = "City Not Found"), 404
        else:
            rsname = args.get('rsname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rsname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityNameByNameChangedDateQtyPriceSupplyDate(cname, rsname, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByCityNameByNameChangedDateQtyPrice(cname, rsname, r_changed_date, rqty, rprice)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityNameByNameChangedDateQtySupplyDate(cname, rsname, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityNameByNameChangedDatePriceSupplyDate(cname, rsname, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityNameByNameQtyPriceSupplyDate(cname, rsname, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityNameByChangedDateQtyPriceSupplyDate(cname, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 3) and rsname and r_changed_date and rqty:
                resource_list = dao.getResourcesByCityNameByNameChangedDateQty(cname, rsname, r_changed_date, rqty)
            elif (len(args) == 3) and rsname and r_changed_date and rprice:
                resource_list = dao.getResourcesByCityNameByNameChangedDatePrice(cname, rsname, r_changed_date, rprice)
            elif (len(args) == 3) and rsname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByCityNameByNameChangedDateSupplyDate(cname, rsname, r_changed_date, r_supply_date)
            elif (len(args) == 3) and rsname and rqty and rprice:
                resource_list = dao.getResourcesByCityNameByNameQtyPrice(cname, rsname, rqty, rprice)
            elif (len(args) == 3) and rsname and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityNameByNameQtySupplyDate(cname, rsname, rqty, r_supply_date)
            elif (len(args) == 3) and rsname and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityNameByNamePriceSupplyDate(cname, rsname, rprice, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByCityNameByChangedDateQtyPrice(cname, r_changed_date, rqty, rprice)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityNameByChangedDateQtySupplyDate(cname, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityNameByChangedDatePriceSupplyDate(cname, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityNameByQtyPriceSupplyDate(cname, rqty, rprice, r_supply_date)
            elif (len(args) == 2) and rsname and r_changed_date:
                resource_list = dao.getResourcesByCityNameByNameChangedDate(cname, rsname, r_changed_date)
            elif (len(args) == 2) and rsname and rqty:
                resource_list = dao.getResourcesByCityNameByNameQty(cname, rsname, rqty)
            elif (len(args) == 2) and rsname and rprice:
                resource_list = dao.getResourcesByCityNameByNamePrice(cname, rsname, rprice)
            elif (len(args) == 2) and rsname and r_supply_date:
                resource_list = dao.getResourcesByCityNameByNameSupplyDate(cname, rsname, r_supply_date)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByCityNameByChangedDateQty(cname, r_changed_date, rqty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByCityNameByChangedDatePrice(cname, r_changed_date, rprice)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByCityNameByChangedDateSupplyDate(cname, r_changed_date, r_supply_date)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByCityNameByQtyPrice(cname, rqty, rprice)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityNameByQtySupplyDate(cname, rqty, r_supply_date)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityNameByPriceSupplyDate(cname, rprice, r_supply_date)
            elif (len(args) == 1) and rsname:
                resource_list = dao.getResourcesByCityNameByName(cname, rsname)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByCityNameByChangedDate(cname, r_changed_date)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByCityNameByQty(cname, rqty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByCityNameByPrice(cname, rprice)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByCityNameBySupplyDate(cname, r_supply_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resource Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def getResourcesByRegionName(self, rname):
        if not RegionDAO().getRegionByName(rname):
            return jsonify(Error = "Region Not Found"), 404
        else:
            resource_list = ResourceDAO().getResourcesByRegionName(rname)
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resources Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def searchResourcesByRegionName(self, rname, args):
        if not RegionDAO().getRegionByName(rname):
            return jsonify(Error = "Region Not Found"), 404
        else:
            rsname = args.get('rsname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rsname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionNameByNameChangedDateQtyPriceSupplyDate(rname, rsname, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByRegionNameByNameChangedDateQtyPrice(rname, rsname, r_changed_date, rqty, rprice)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionNameByNameChangedDateQtySupplyDate(rname, rsname, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionNameByNameChangedDatePriceSupplyDate(rname, rsname, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionNameByNameQtyPriceSupplyDate(rname, rsname, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionNameByChangedDateQtyPriceSupplyDate(rname, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 3) and rsname and r_changed_date and rqty:
                resource_list = dao.getResourcesByRegionNameByNameChangedDateQty(rname, rsname, r_changed_date, rqty)
            elif (len(args) == 3) and rsname and r_changed_date and rprice:
                resource_list = dao.getResourcesByRegionNameByNameChangedDatePrice(rname, rsname, r_changed_date, rprice)
            elif (len(args) == 3) and rsname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByRegionNameByNameChangedDateSupplyDate(rname, rsname, r_changed_date, r_supply_date)
            elif (len(args) == 3) and rsname and rqty and rprice:
                resource_list = dao.getResourcesByRegionNameByNameQtyPrice(rname, rsname, rqty, rprice)
            elif (len(args) == 3) and rsname and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionNameByNameQtySupplyDate(rname, rsname, rqty, r_supply_date)
            elif (len(args) == 3) and rsname and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionNameByNamePriceSupplyDate(rname, rsname, rprice, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByRegionNameByChangedDateQtyPrice(rname, r_changed_date, rqty, rprice)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionNameByChangedDateQtySupplyDate(rname, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionNameByChangedDatePriceSupplyDate(rname, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionNameByQtyPriceSupplyDate(rname, rqty, rprice, r_supply_date)
            elif (len(args) == 2) and rsname and r_changed_date:
                resource_list = dao.getResourcesByRegionNameByNameChangedDate(rname, rsname, r_changed_date)
            elif (len(args) == 2) and rsname and rqty:
                resource_list = dao.getResourcesByRegionNameByNameQty(rname, rsname, rqty)
            elif (len(args) == 2) and rsname and rprice:
                resource_list = dao.getResourcesByRegionNameByNamePrice(rname, rsname, rprice)
            elif (len(args) == 2) and rsname and r_supply_date:
                resource_list = dao.getResourcesByRegionNameByNameSupplyDate(rname, rsname, r_supply_date)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByRegionNameByChangedDateQty(rname, r_changed_date, rqty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByRegionNameByChangedDatePrice(rname, r_changed_date, rprice)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByRegionNameByChangedDateSupplyDate(rname, r_changed_date, r_supply_date)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByRegionNameByQtyPrice(rname, rqty, rprice)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionNameByQtySupplyDate(rname, rqty, r_supply_date)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionNameByPriceSupplyDate(rname, rprice, r_supply_date)
            elif (len(args) == 1) and rsname:
                resource_list = dao.getResourcesByRegionNameByName(rname, rsname)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByRegionNameByChangedDate(rname, r_changed_date)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByRegionNameByQty(rname, rqty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByRegionNameByPrice(rname, rprice)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByRegionNameBySupplyDate(rname, r_supply_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resource Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def getResourcesBySupplierId(self, sid):
        if not SupplierDAO().getSupplierById(sid):
            return jsonify(Error = "Supplier Not Found"), 404
        else:
            resource_list = ResourceDAO().getResourcesBySupplierId(sid)
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resources Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def searchResourcesBySupplierId(self, sid, args):
        if not SupplierDAO().getSupplierById(sid):
            return jsonify(Error = "Supplier Not Found"), 404
        else:
            rsname = args.get('rsname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rsname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierIdByNameChangedDateQtyPriceSupplyDate(sid, rsname, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesBySupplierIdByNameChangedDateQtyPrice(sid, rsname, r_changed_date, rqty, rprice)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierIdByNameChangedDateQtySupplyDate(sid, rsname, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierIdByNameChangedDatePriceSupplyDate(sid, rsname, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierIdByNameQtyPriceSupplyDate(sid, rsname, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierIdByChangedDateQtyPriceSupplyDate(sid, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 3) and rsname and r_changed_date and rqty:
                resource_list = dao.getResourcesBySupplierIdByNameChangedDateQty(sid, rsname, r_changed_date, rqty)
            elif (len(args) == 3) and rsname and r_changed_date and rprice:
                resource_list = dao.getResourcesBySupplierIdByNameChangedDatePrice(sid, rsname, r_changed_date, rprice)
            elif (len(args) == 3) and rsname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesBySupplierIdByNameChangedDateSupplyDate(sid, rsname, r_changed_date, r_supply_date)
            elif (len(args) == 3) and rsname and rqty and rprice:
                resource_list = dao.getResourcesBySupplierIdByNameQtyPrice(sid, rsname, rqty, rprice)
            elif (len(args) == 3) and rsname and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierIdByNameQtySupplyDate(sid, rsname, rqty, r_supply_date)
            elif (len(args) == 3) and rsname and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierIdByNamePriceSupplyDate(sid, rsname, rprice, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesBySupplierIdByChangedDateQtyPrice(sid, r_changed_date, rqty, rprice)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierIdByChangedDateQtySupplyDate(sid, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierIdByChangedDatePriceSupplyDate(sid, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierIdByQtyPriceSupplyDate(sid, rqty, rprice, r_supply_date)
            elif (len(args) == 2) and rsname and r_changed_date:
                resource_list = dao.getResourcesBySupplierIdByNameChangedDate(sid, rsname, r_changed_date)
            elif (len(args) == 2) and rsname and rqty:
                resource_list = dao.getResourcesBySupplierIdByNameQty(sid, rsname, rqty)
            elif (len(args) == 2) and rsname and rprice:
                resource_list = dao.getResourcesBySupplierIdByNamePrice(sid, rsname, rprice)
            elif (len(args) == 2) and rsname and r_supply_date:
                resource_list = dao.getResourcesBySupplierIdByNameSupplyDate(sid, rsname, r_supply_date)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesBySupplierIdByChangedDateQty(sid, r_changed_date, rqty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesBySupplierIdByChangedDatePrice(sid, r_changed_date, rprice)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesBySupplierIdByChangedDateSupplyDate(sid, r_changed_date, r_supply_date)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesBySupplierIdByQtyPrice(sid, rqty, rprice)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierIdByQtySupplyDate(sid, rqty, r_supply_date)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierIdByPriceSupplyDate(sid, rprice, r_supply_date)
            elif (len(args) == 1) and rsname:
                resource_list = dao.getResourcesBySupplierIdByName(sid, rsname)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesBySupplierIdByChangedDate(sid, r_changed_date)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesBySupplierIdByQty(sid, rqty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesBySupplierIdByPrice(sid, rprice)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesBySupplierIdBySupplyDate(sid, r_supply_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resource Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def getResourcesByKeywordId(self, kid):
        if not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        else:
            resource_list = ResourceDAO().getResourcesByKeywordId(kid)
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resources Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def searchResourcesByKeywordId(self, kid, args):
        if not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        else:
            rsname = args.get('rsname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rsname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordIdByNameChangedDateQtyPriceSupplyDate(kid, rsname, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByKeywordIdByNameChangedDateQtyPrice(kid, rsname, r_changed_date, rqty, rprice)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByKeywordIdByNameChangedDateQtySupplyDate(kid, rsname, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordIdByNameChangedDatePriceSupplyDate(kid, rsname, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordIdByNameQtyPriceSupplyDate(kid, rsname, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordIdByChangedDateQtyPriceSupplyDate(kid, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 3) and rsname and r_changed_date and rqty:
                resource_list = dao.getResourcesByKeywordIdByNameChangedDateQty(kid, rsname, r_changed_date, rqty)
            elif (len(args) == 3) and rsname and r_changed_date and rprice:
                resource_list = dao.getResourcesByKeywordIdByNameChangedDatePrice(kid, rsname, r_changed_date, rprice)
            elif (len(args) == 3) and rsname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByKeywordIdByNameChangedDateSupplyDate(kid, rsname, r_changed_date, r_supply_date)
            elif (len(args) == 3) and rsname and rqty and rprice:
                resource_list = dao.getResourcesByKeywordIdByNameQtyPrice(kid, rsname, rqty, rprice)
            elif (len(args) == 3) and rsname and rqty and r_supply_date:
                resource_list = dao.getResourcesByKeywordIdByNameQtySupplyDate(kid, rsname, rqty, r_supply_date)
            elif (len(args) == 3) and rsname and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordIdByNamePriceSupplyDate(kid, rsname, rprice, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByKeywordIdByChangedDateQtyPrice(kid, r_changed_date, rqty, rprice)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByKeywordIdByChangedDateQtySupplyDate(kid, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordIdByChangedDatePriceSupplyDate(kid, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordIdByQtyPriceSupplyDate(kid, rqty, rprice, r_supply_date)
            elif (len(args) == 2) and rsname and r_changed_date:
                resource_list = dao.getResourcesByKeywordIdByNameChangedDate(kid, rsname, r_changed_date)
            elif (len(args) == 2) and rsname and rqty:
                resource_list = dao.getResourcesByKeywordIdByNameQty(kid, rsname, rqty)
            elif (len(args) == 2) and rsname and rprice:
                resource_list = dao.getResourcesByKeywordIdByNamePrice(kid, rsname, rprice)
            elif (len(args) == 2) and rsname and r_supply_date:
                resource_list = dao.getResourcesByKeywordIdByNameSupplyDate(kid, rsname, r_supply_date)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByKeywordIdByChangedDateQty(kid, r_changed_date, rqty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByKeywordIdByChangedDatePrice(kid, r_changed_date, rprice)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByKeywordIdByChangedDateSupplyDate(kid, r_changed_date, r_supply_date)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByKeywordIdByQtyPrice(kid, rqty, rprice)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByKeywordIdByQtySupplyDate(kid, rqty, r_supply_date)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordIdByPriceSupplyDate(kid, rprice, r_supply_date)
            elif (len(args) == 1) and rsname:
                resource_list = dao.getResourcesByKeywordIdByName(kid, rsname)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByKeywordIdByChangedDate(kid, r_changed_date)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByKeywordIdByQty(kid, rqty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByKeywordIdByPrice(kid, rprice)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByKeywordIdBySupplyDate(kid, r_supply_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resource Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def getResourcesByCategoryName(self, cat_name):
        if not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            resource_list = ResourceDAO().getResourcesByCategoryName(cat_name)
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resources Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def searchResourcesByCategoryName(self, cat_name, args):
        if not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            rsname = args.get('rsname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rsname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCategoryNameByNameChangedDateQtyPriceSupplyDate(cat_name, rsname, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByCategoryNameByNameChangedDateQtyPrice(cat_name, rsname, r_changed_date, rqty, rprice)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByCategoryNameByNameChangedDateQtySupplyDate(cat_name, rsname, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByCategoryNameByNameChangedDatePriceSupplyDate(cat_name, rsname, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCategoryNameByNameQtyPriceSupplyDate(cat_name, rsname, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCategoryNameByChangedDateQtyPriceSupplyDate(cat_name, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 3) and rsname and r_changed_date and rqty:
                resource_list = dao.getResourcesByCategoryNameByNameChangedDateQty(cat_name, rsname, r_changed_date, rqty)
            elif (len(args) == 3) and rsname and r_changed_date and rprice:
                resource_list = dao.getResourcesByCategoryNameByNameChangedDatePrice(cat_name, rsname, r_changed_date, rprice)
            elif (len(args) == 3) and rsname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByCategoryNameByNameChangedDateSupplyDate(cat_name, rsname, r_changed_date, r_supply_date)
            elif (len(args) == 3) and rsname and rqty and rprice:
                resource_list = dao.getResourcesByCategoryNameByNameQtyPrice(cat_name, rsname, rqty, rprice)
            elif (len(args) == 3) and rsname and rqty and r_supply_date:
                resource_list = dao.getResourcesByCategoryNameByNameQtySupplyDate(cat_name, rsname, rqty, r_supply_date)
            elif (len(args) == 3) and rsname and rprice and r_supply_date:
                resource_list = dao.getResourcesByCategoryNameByNamePriceSupplyDate(cat_name, rsname, rprice, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByCategoryNameByChangedDateQtyPrice(cat_name, r_changed_date, rqty, rprice)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByCategoryNameByChangedDateQtySupplyDate(cat_name, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByCategoryNameByChangedDatePriceSupplyDate(cat_name, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCategoryNameByQtyPriceSupplyDate(cat_name, rqty, rprice, r_supply_date)
            elif (len(args) == 2) and rsname and r_changed_date:
                resource_list = dao.getResourcesByCategoryNameByNameChangedDate(cat_name, rsname, r_changed_date)
            elif (len(args) == 2) and rsname and rqty:
                resource_list = dao.getResourcesByCategoryNameByNameQty(cat_name, rsname, rqty)
            elif (len(args) == 2) and rsname and rprice:
                resource_list = dao.getResourcesByCategoryNameByNamePrice(cat_name, rsname, rprice)
            elif (len(args) == 2) and rsname and r_supply_date:
                resource_list = dao.getResourcesByCategoryNameByNameSupplyDate(cat_name, rsname, r_supply_date)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByCategoryNameByChangedDateQty(cat_name, r_changed_date, rqty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByCategoryNameByChangedDatePrice(cat_name, r_changed_date, rprice)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByCategoryNameByChangedDateSupplyDate(cat_name, r_changed_date, r_supply_date)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByCategoryNameByQtyPrice(cat_name, rqty, rprice)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByCategoryNameByQtySupplyDate(cat_name, rqty, r_supply_date)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByCategoryNameByPriceSupplyDate(cat_name, rprice, r_supply_date)
            elif (len(args) == 1) and rsname:
                resource_list = dao.getResourcesByCategoryNameByName(cat_name, rsname)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByCategoryNameByChangedDate(cat_name, r_changed_date)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByCategoryNameByQty(cat_name, rqty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByCategoryNameByPrice(cat_name, rprice)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByCategoryNameBySupplyDate(cat_name, r_supply_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resource Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def getResourcesByTransactionId(self, tid):
        if not TransactionDAO().getTransactionById(tid):
            return jsonify(Error = "Transaction Not Found"), 404
        else:
            resource_list = ResourceDAO().getResourcesByTransactionId(tid)
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resources Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def searchResourcesByTransactionId(self, tid, args):
        if not TransactionDAO().getTransactionById(tid):
            return jsonify(Error = "Transaction Not Found"), 404
        else:
            rsname = args.get('rsname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rsname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByTransactionIdByNameChangedDateQtyPriceSupplyDate(tid, rsname, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByTransactionIdByNameChangedDateQtyPrice(tid, rsname, r_changed_date, rqty, rprice)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByTransactionIdByNameChangedDateQtySupplyDate(tid, rsname, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByTransactionIdByNameChangedDatePriceSupplyDate(tid, rsname, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByTransactionIdByNameQtyPriceSupplyDate(tid, rsname, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByTransactionIdByChangedDateQtyPriceSupplyDate(tid, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 3) and rsname and r_changed_date and rqty:
                resource_list = dao.getResourcesByTransactionIdByNameChangedDateQty(tid, rsname, r_changed_date, rqty)
            elif (len(args) == 3) and rsname and r_changed_date and rprice:
                resource_list = dao.getResourcesByTransactionIdByNameChangedDatePrice(tid, rsname, r_changed_date, rprice)
            elif (len(args) == 3) and rsname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByTransactionIdByNameChangedDateSupplyDate(tid, rsname, r_changed_date, r_supply_date)
            elif (len(args) == 3) and rsname and rqty and rprice:
                resource_list = dao.getResourcesByTransactionIdByNameQtyPrice(tid, rsname, rqty, rprice)
            elif (len(args) == 3) and rsname and rqty and r_supply_date:
                resource_list = dao.getResourcesByTransactionIdByNameQtySupplyDate(tid, rsname, rqty, r_supply_date)
            elif (len(args) == 3) and rsname and rprice and r_supply_date:
                resource_list = dao.getResourcesByTransactionIdByNamePriceSupplyDate(tid, rsname, rprice, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByTransactionIdByChangedDateQtyPrice(tid, r_changed_date, rqty, rprice)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByTransactionIdByChangedDateQtySupplyDate(tid, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByTransactionIdByChangedDatePriceSupplyDate(tid, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByTransactionIdByQtyPriceSupplyDate(tid, rqty, rprice, r_supply_date)
            elif (len(args) == 2) and rsname and r_changed_date:
                resource_list = dao.getResourcesByTransactionIdByNameChangedDate(tid, rsname, r_changed_date)
            elif (len(args) == 2) and rsname and rqty:
                resource_list = dao.getResourcesByTransactionIdByNameQty(tid, rsname, rqty)
            elif (len(args) == 2) and rsname and rprice:
                resource_list = dao.getResourcesByTransactionIdByNamePrice(tid, rsname, rprice)
            elif (len(args) == 2) and rsname and r_supply_date:
                resource_list = dao.getResourcesByTransactionIdByNameSupplyDate(tid, rsname, r_supply_date)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByTransactionIdByChangedDateQty(tid, r_changed_date, rqty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByTransactionIdByChangedDatePrice(tid, r_changed_date, rprice)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByTransactionIdByChangedDateSupplyDate(tid, r_changed_date, r_supply_date)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByTransactionIdByQtyPrice(tid, rqty, rprice)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByTransactionIdByQtySupplyDate(tid, rqty, r_supply_date)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByTransactionIdByPriceSupplyDate(tid, rprice, r_supply_date)
            elif (len(args) == 1) and rsname:
                resource_list = dao.getResourcesByTransactionIdByName(tid, rsname)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByTransactionIdByChangedDate(tid, r_changed_date)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByTransactionIdByQty(tid, rqty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByTransactionIdByPrice(tid, rprice)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByTransactionIdBySupplyDate(tid, r_supply_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resource Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def getResourcesByOrderId(self, oid):
        if not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Order Not Found"), 404
        else:
            resource_list = ResourceDAO().getResourcesByOrderId(oid)
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resources Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def searchResourcesByOrderId(self, oid, args):
        if not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Order Not Found"), 404
        else:
            rsname = args.get('rsname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rsname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByOrderIdByNameChangedDateQtyPriceSupplyDate(oid, rsname, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByOrderIdByNameChangedDateQtyPrice(oid, rsname, r_changed_date, rqty, rprice)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByOrderIdByNameChangedDateQtySupplyDate(oid, rsname, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByOrderIdByNameChangedDatePriceSupplyDate(oid, rsname, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByOrderIdByNameQtyPriceSupplyDate(oid, rsname, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByOrderIdByChangedDateQtyPriceSupplyDate(oid, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 3) and rsname and r_changed_date and rqty:
                resource_list = dao.getResourcesByOrderIdByNameChangedDateQty(oid, rsname, r_changed_date, rqty)
            elif (len(args) == 3) and rsname and r_changed_date and rprice:
                resource_list = dao.getResourcesByOrderIdByNameChangedDatePrice(oid, rsname, r_changed_date, rprice)
            elif (len(args) == 3) and rsname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByOrderIdByNameChangedDateSupplyDate(oid, rsname, r_changed_date, r_supply_date)
            elif (len(args) == 3) and rsname and rqty and rprice:
                resource_list = dao.getResourcesByOrderIdByNameQtyPrice(oid, rsname, rqty, rprice)
            elif (len(args) == 3) and rsname and rqty and r_supply_date:
                resource_list = dao.getResourcesByOrderIdByNameQtySupplyDate(oid, rsname, rqty, r_supply_date)
            elif (len(args) == 3) and rsname and rprice and r_supply_date:
                resource_list = dao.getResourcesByOrderIdByNamePriceSupplyDate(oid, rsname, rprice, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByOrderIdByChangedDateQtyPrice(oid, r_changed_date, rqty, rprice)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByOrderIdByChangedDateQtySupplyDate(oid, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByOrderIdByChangedDatePriceSupplyDate(oid, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByOrderIdByQtyPriceSupplyDate(oid, rqty, rprice, r_supply_date)
            elif (len(args) == 2) and rsname and r_changed_date:
                resource_list = dao.getResourcesByOrderIdByNameChangedDate(oid, rsname, r_changed_date)
            elif (len(args) == 2) and rsname and rqty:
                resource_list = dao.getResourcesByOrderIdByNameQty(oid, rsname, rqty)
            elif (len(args) == 2) and rsname and rprice:
                resource_list = dao.getResourcesByOrderIdByNamePrice(oid, rsname, rprice)
            elif (len(args) == 2) and rsname and r_supply_date:
                resource_list = dao.getResourcesByOrderIdByNameSupplyDate(oid, rsname, r_supply_date)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByOrderIdByChangedDateQty(oid, r_changed_date, rqty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByOrderIdByChangedDatePrice(oid, r_changed_date, rprice)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByOrderIdByChangedDateSupplyDate(oid, r_changed_date, r_supply_date)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByOrderIdByQtyPrice(oid, rqty, rprice)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByOrderIdByQtySupplyDate(oid, rqty, r_supply_date)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByOrderIdByPriceSupplyDate(oid, rprice, r_supply_date)
            elif (len(args) == 1) and rsname:
                resource_list = dao.getResourcesByOrderIdByName(oid, rsname)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByOrderIdByChangedDate(oid, r_changed_date)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByOrderIdByQty(oid, rqty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByOrderIdByPrice(oid, rprice)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByOrderIdBySupplyDate(oid, r_supply_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resource Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def getResourcesByCityKeyword(self, cname, kid):
        if not CityDAO().getCityByName(cname) and not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "City and Keyword Not Found"), 404
        elif not CityDAO().getCityByName(cname):
            return jsonify(Error = "City Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        else:
            resource_list = ResourceDAO().getResourcesByCityKeyword(cname, kid)
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resources Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def searchResourcesByCityKeyword(self, cname, kid, args):
        if not CityDAO().getCityByName(cname) and not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "City and Keyword Not Found"), 404
        elif not CityDAO().getCityByName(cname):
            return jsonify(Error = "City Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        else:
            rsname = args.get('rsname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rsname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordByNameChangedDateQtyPriceSupplyDate(cname, kid, rsname, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByCityKeywordByNameChangedDateQtyPrice(cname, kid, rsname, r_changed_date, rqty, rprice)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordByNameChangedDateQtySupplyDate(cname, kid, rsname, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordByNameChangedDatePriceSupplyDate(cname, kid, rsname, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordByNameQtyPriceSupplyDate(cname, kid, rsname, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordByChangedDateQtyPriceSupplyDate(cname, kid, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 3) and rsname and r_changed_date and rqty:
                resource_list = dao.getResourcesByCityKeywordByNameChangedDateQty(cname, kid, rsname, r_changed_date, rqty)
            elif (len(args) == 3) and rsname and r_changed_date and rprice:
                resource_list = dao.getResourcesByCityKeywordByNameChangedDatePrice(cname, kid, rsname, r_changed_date, rprice)
            elif (len(args) == 3) and rsname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordByNameChangedDateSupplyDate(cname, kid, rsname, r_changed_date, r_supply_date)
            elif (len(args) == 3) and rsname and rqty and rprice:
                resource_list = dao.getResourcesByCityKeywordByNameQtyPrice(cname, kid, rsname, rqty, rprice)
            elif (len(args) == 3) and rsname and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordByNameQtySupplyDate(cname, kid, rsname, rqty, r_supply_date)
            elif (len(args) == 3) and rsname and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordByNamePriceSupplyDate(cname, kid, rsname, rprice, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByCityKeywordByChangedDateQtyPrice(cname, kid, r_changed_date, rqty, rprice)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordByChangedDateQtySupplyDate(cname, kid, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordByChangedDatePriceSupplyDate(cname, kid, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordByQtyPriceSupplyDate(cname, kid, rqty, rprice, r_supply_date)
            elif (len(args) == 2) and rsname and r_changed_date:
                resource_list = dao.getResourcesByCityKeywordByNameChangedDate(cname, kid, rsname, r_changed_date)
            elif (len(args) == 2) and rsname and rqty:
                resource_list = dao.getResourcesByCityKeywordByNameQty(cname, kid, rsname, rqty)
            elif (len(args) == 2) and rsname and rprice:
                resource_list = dao.getResourcesByCityKeywordByNamePrice(cname, kid, rsname, rprice)
            elif (len(args) == 2) and rsname and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordByNameSupplyDate(cname, kid, rsname, r_supply_date)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByCityKeywordByChangedDateQty(cname, kid, r_changed_date, rqty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByCityKeywordByChangedDatePrice(cname, kid, r_changed_date, rprice)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordByChangedDateSupplyDate(cname, kid, r_changed_date, r_supply_date)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByCityKeywordByQtyPrice(cname, kid, rqty, rprice)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordByQtySupplyDate(cname, kid, rqty, r_supply_date)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordByPriceSupplyDate(cname, kid, rprice, r_supply_date)
            elif (len(args) == 1) and rsname:
                resource_list = dao.getResourcesByCityKeywordByName(cname, kid, rsname)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByCityKeywordByChangedDate(cname, kid, r_changed_date)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByCityKeywordByQty(cname, kid, rqty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByCityKeywordByPrice(cname, kid, rprice)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordBySupplyDate(cname, kid, r_supply_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resource Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def getResourcesByCityCategory(self, cname, cat_name):
        if not CityDAO().getCityByName(cname) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "City and Category Not Found"), 404
        elif not CityDAO().getCityByName(cname):
            return jsonify(Error = "City Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            resource_list = ResourceDAO().getResourcesByCityCategory(cname, cat_name)
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resources Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def searchResourcesByCityCategory(self, cname, cat_name, args):
        if not CityDAO().getCityByName(cname) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "City and Category Not Found"), 404
        elif not CityDAO().getCityByName(cname):
            return jsonify(Error = "City Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            rsname = args.get('rsname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rsname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryByNameChangedDateQtyPriceSupplyDate(cname, cat_name, rsname, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByCityCategoryByNameChangedDateQtyPrice(cname, cat_name, rsname, r_changed_date, rqty, rprice)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryByNameChangedDateQtySupplyDate(cname, cat_name, rsname, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryByNameChangedDatePriceSupplyDate(cname, cat_name, rsname, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryByNameQtyPriceSupplyDate(cname, cat_name, rsname, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryByChangedDateQtyPriceSupplyDate(cname, cat_name, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 3) and rsname and r_changed_date and rqty:
                resource_list = dao.getResourcesByCityCategoryByNameChangedDateQty(cname, cat_name, rsname, r_changed_date, rqty)
            elif (len(args) == 3) and rsname and r_changed_date and rprice:
                resource_list = dao.getResourcesByCityCategoryByNameChangedDatePrice(cname, cat_name, rsname, r_changed_date, rprice)
            elif (len(args) == 3) and rsname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryByNameChangedDateSupplyDate(cname, cat_name, rsname, r_changed_date, r_supply_date)
            elif (len(args) == 3) and rsname and rqty and rprice:
                resource_list = dao.getResourcesByCityCategoryByNameQtyPrice(cname, cat_name, rsname, rqty, rprice)
            elif (len(args) == 3) and rsname and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryByNameQtySupplyDate(cname, cat_name, rsname, rqty, r_supply_date)
            elif (len(args) == 3) and rsname and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryByNamePriceSupplyDate(cname, cat_name, rsname, rprice, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByCityCategoryByChangedDateQtyPrice(cname, cat_name, r_changed_date, rqty, rprice)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryByChangedDateQtySupplyDate(cname, cat_name, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryByChangedDatePriceSupplyDate(cname, cat_name, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryByQtyPriceSupplyDate(cname, cat_name, rqty, rprice, r_supply_date)
            elif (len(args) == 2) and rsname and r_changed_date:
                resource_list = dao.getResourcesByCityCategoryByNameChangedDate(cname, cat_name, rsname, r_changed_date)
            elif (len(args) == 2) and rsname and rqty:
                resource_list = dao.getResourcesByCityCategoryByNameQty(cname, cat_name, rsname, rqty)
            elif (len(args) == 2) and rsname and rprice:
                resource_list = dao.getResourcesByCityCategoryByNamePrice(cname, cat_name, rsname, rprice)
            elif (len(args) == 2) and rsname and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryByNameSupplyDate(cname, cat_name, rsname, r_supply_date)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByCityCategoryByChangedDateQty(cname, cat_name, r_changed_date, rqty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByCityCategoryByChangedDatePrice(cname, cat_name, r_changed_date, rprice)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryByChangedDateSupplyDate(cname, cat_name, r_changed_date, r_supply_date)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByCityCategoryByQtyPrice(cname, cat_name, rqty, rprice)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryByQtySupplyDate(cname, cat_name, rqty, r_supply_date)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryByPriceSupplyDate(cname, cat_name, rprice, r_supply_date)
            elif (len(args) == 1) and rsname:
                resource_list = dao.getResourcesByCityCategoryByName(cname, cat_name, rsname)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByCityCategoryByChangedDate(cname, cat_name, r_changed_date)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByCityCategoryByQty(cname, cat_name, rqty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByCityCategoryByPrice(cname, cat_name, rprice)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryBySupplyDate(cname, cat_name, r_supply_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resource Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def getResourcesByRegionKeyword(self, rname, kid):
        if not RegionDAO().getRegionByName(rname) and not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Region and Keyword Not Found"), 404
        elif not RegionDAO().getRegionByName(rname):
            return jsonify(Error = "Region Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        else:
            resource_list = ResourceDAO().getResourcesByRegionKeyword(rname, kid)
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resources Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def searchResourcesByRegionKeyword(self, rname, kid, args):
        if not RegionDAO().getRegionByName(rname) and not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Region and Keyword Not Found"), 404
        elif not RegionDAO().getRegionByName(rname):
            return jsonify(Error = "Region Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        else:
            rsname = args.get('rsname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rsname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordByNameChangedDateQtyPriceSupplyDate(rname, kid, rsname, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByRegionKeywordByNameChangedDateQtyPrice(rname, kid, rsname, r_changed_date, rqty, rprice)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordByNameChangedDateQtySupplyDate(rname, kid, rsname, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordByNameChangedDatePriceSupplyDate(rname, kid, rsname, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordByNameQtyPriceSupplyDate(rname, kid, rsname, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordByChangedDateQtyPriceSupplyDate(rname, kid, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 3) and rsname and r_changed_date and rqty:
                resource_list = dao.getResourcesByRegionKeywordByNameChangedDateQty(rname, kid, rsname, r_changed_date, rqty)
            elif (len(args) == 3) and rsname and r_changed_date and rprice:
                resource_list = dao.getResourcesByRegionKeywordByNameChangedDatePrice(rname, kid, rsname, r_changed_date, rprice)
            elif (len(args) == 3) and rsname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordByNameChangedDateSupplyDate(rname, kid, rsname, r_changed_date, r_supply_date)
            elif (len(args) == 3) and rsname and rqty and rprice:
                resource_list = dao.getResourcesByRegionKeywordByNameQtyPrice(rname, kid, rsname, rqty, rprice)
            elif (len(args) == 3) and rsname and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordByNameQtySupplyDate(rname, kid, rsname, rqty, r_supply_date)
            elif (len(args) == 3) and rsname and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordByNamePriceSupplyDate(rname, kid, rsname, rprice, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByRegionKeywordByChangedDateQtyPrice(rname, kid, r_changed_date, rqty, rprice)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordByChangedDateQtySupplyDate(rname, kid, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordByChangedDatePriceSupplyDate(rname, kid, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordByQtyPriceSupplyDate(rname, kid, rqty, rprice, r_supply_date)
            elif (len(args) == 2) and rsname and r_changed_date:
                resource_list = dao.getResourcesByRegionKeywordByNameChangedDate(rname, kid, rsname, r_changed_date)
            elif (len(args) == 2) and rsname and rqty:
                resource_list = dao.getResourcesByRegionKeywordByNameQty(rname, kid, rsname, rqty)
            elif (len(args) == 2) and rsname and rprice:
                resource_list = dao.getResourcesByRegionKeywordByNamePrice(rname, kid, rsname, rprice)
            elif (len(args) == 2) and rsname and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordByNameSupplyDate(rname, kid, rsname, r_supply_date)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByRegionKeywordByChangedDateQty(rname, kid, r_changed_date, rqty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByRegionKeywordByChangedDatePrice(rname, kid, r_changed_date, rprice)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordByChangedDateSupplyDate(rname, kid, r_changed_date, r_supply_date)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByRegionKeywordByQtyPrice(rname, kid, rqty, rprice)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordByQtySupplyDate(rname, kid, rqty, r_supply_date)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordByPriceSupplyDate(rname, kid, rprice, r_supply_date)
            elif (len(args) == 1) and rsname:
                resource_list = dao.getResourcesByRegionKeywordByName(rname, kid, rsname)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByRegionKeywordByChangedDate(rname, kid, r_changed_date)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByRegionKeywordByQty(rname, kid, rqty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByRegionKeywordByPrice(rname, kid, rprice)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordBySupplyDate(rname, kid, r_supply_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resource Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def getResourcesByRegionCategory(self, rname, cat_name):
        if not RegionDAO().getRegionByName(rname) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Region and Category Not Found"), 404
        elif not RegionDAO().getRegionByName(rname):
            return jsonify(Error = "Region Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            resource_list = ResourceDAO().getResourcesByRegionCategory(rname, cat_name)
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resources Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def searchResourcesByRegionCategory(self, rname, cat_name, args):
        if not RegionDAO().getRegionByName(rname) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Region and Category Not Found"), 404
        elif not RegionDAO().getRegionByName(rname):
            return jsonify(Error = "Region Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            rsname = args.get('rsname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rsname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryByNameChangedDateQtyPriceSupplyDate(rname, cat_name, rsname, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByRegionCategoryByNameChangedDateQtyPrice(rname, cat_name, rsname, r_changed_date, rqty, rprice)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryByNameChangedDateQtySupplyDate(rname, cat_name, rsname, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryByNameChangedDatePriceSupplyDate(rname, cat_name, rsname, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryByNameQtyPriceSupplyDate(rname, cat_name, rsname, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryByChangedDateQtyPriceSupplyDate(rname, cat_name, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 3) and rsname and r_changed_date and rqty:
                resource_list = dao.getResourcesByRegionCategoryByNameChangedDateQty(rname, cat_name, rsname, r_changed_date, rqty)
            elif (len(args) == 3) and rsname and r_changed_date and rprice:
                resource_list = dao.getResourcesByRegionCategoryByNameChangedDatePrice(rname, cat_name, rsname, r_changed_date, rprice)
            elif (len(args) == 3) and rsname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryByNameChangedDateSupplyDate(rname, cat_name, rsname, r_changed_date, r_supply_date)
            elif (len(args) == 3) and rsname and rqty and rprice:
                resource_list = dao.getResourcesByRegionCategoryByNameQtyPrice(rname, cat_name, rsname, rqty, rprice)
            elif (len(args) == 3) and rsname and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryByNameQtySupplyDate(rname, cat_name, rsname, rqty, r_supply_date)
            elif (len(args) == 3) and rsname and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryByNamePriceSupplyDate(rname, cat_name, rsname, rprice, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByRegionCategoryByChangedDateQtyPrice(rname, cat_name, r_changed_date, rqty, rprice)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryByChangedDateQtySupplyDate(rname, cat_name, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryByChangedDatePriceSupplyDate(rname, cat_name, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryByQtyPriceSupplyDate(rname, cat_name, rqty, rprice, r_supply_date)
            elif (len(args) == 2) and rsname and r_changed_date:
                resource_list = dao.getResourcesByRegionCategoryByNameChangedDate(rname, cat_name, rsname, r_changed_date)
            elif (len(args) == 2) and rsname and rqty:
                resource_list = dao.getResourcesByRegionCategoryByNameQty(rname, cat_name, rsname, rqty)
            elif (len(args) == 2) and rsname and rprice:
                resource_list = dao.getResourcesByRegionCategoryByNamePrice(rname, cat_name, rsname, rprice)
            elif (len(args) == 2) and rsname and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryByNameSupplyDate(rname, cat_name, rsname, r_supply_date)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByRegionCategoryByChangedDateQty(rname, cat_name, r_changed_date, rqty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByRegionCategoryByChangedDatePrice(rname, cat_name, r_changed_date, rprice)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryByChangedDateSupplyDate(rname, cat_name, r_changed_date, r_supply_date)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByRegionCategoryByQtyPrice(rname, cat_name, rqty, rprice)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryByQtySupplyDate(rname, cat_name, rqty, r_supply_date)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryByPriceSupplyDate(rname, cat_name, rprice, r_supply_date)
            elif (len(args) == 1) and rsname:
                resource_list = dao.getResourcesByRegionCategoryByName(rname, cat_name, rsname)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByRegionCategoryByChangedDate(rname, cat_name, r_changed_date)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByRegionCategoryByQty(rname, cat_name, rqty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByRegionCategoryByPrice(rname, cat_name, rprice)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryBySupplyDate(rname, cat_name, r_supply_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resource Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def getResourcesBySupplierKeyword(self, sid, kid):
        if not SupplierDAO().getSupplierById(sid) and not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Supplier and Keyword Not Found"), 404
        elif not SupplierDAO().getSupplierById(sid):
            return jsonify(Error = "Supplier Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        else:
            resource_list = ResourceDAO().getResourcesBySupplierKeyword(sid, kid)
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resources Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def searchResourcesBySupplierKeyword(self, sid, kid, args):
        if not SupplierDAO().getSupplierById(sid) and not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Supplier and Keyword Not Found"), 404
        elif not SupplierDAO().getSupplierById(sid):
            return jsonify(Error = "Supplier Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        else:
            rsname = args.get('rsname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rsname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordByNameChangedDateQtyPriceSupplyDate(sid, kid, rsname, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesBySupplierKeywordByNameChangedDateQtyPrice(sid, kid, rsname, r_changed_date, rqty, rprice)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordByNameChangedDateQtySupplyDate(sid, kid, rsname, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordByNameChangedDatePriceSupplyDate(sid, kid, rsname, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordByNameQtyPriceSupplyDate(sid, kid, rsname, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordByChangedDateQtyPriceSupplyDate(sid, kid, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 3) and rsname and r_changed_date and rqty:
                resource_list = dao.getResourcesBySupplierKeywordByNameChangedDateQty(sid, kid, rsname, r_changed_date, rqty)
            elif (len(args) == 3) and rsname and r_changed_date and rprice:
                resource_list = dao.getResourcesBySupplierKeywordByNameChangedDatePrice(sid, kid, rsname, r_changed_date, rprice)
            elif (len(args) == 3) and rsname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordByNameChangedDateSupplyDate(sid, kid, rsname, r_changed_date, r_supply_date)
            elif (len(args) == 3) and rsname and rqty and rprice:
                resource_list = dao.getResourcesBySupplierKeywordByNameQtyPrice(sid, kid, rsname, rqty, rprice)
            elif (len(args) == 3) and rsname and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordByNameQtySupplyDate(sid, kid, rsname, rqty, r_supply_date)
            elif (len(args) == 3) and rsname and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordByNamePriceSupplyDate(sid, kid, rsname, rprice, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesBySupplierKeywordByChangedDateQtyPrice(sid, kid, r_changed_date, rqty, rprice)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordByChangedDateQtySupplyDate(sid, kid, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordByChangedDatePriceSupplyDate(sid, kid, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordByQtyPriceSupplyDate(sid, kid, rqty, rprice, r_supply_date)
            elif (len(args) == 2) and rsname and r_changed_date:
                resource_list = dao.getResourcesBySupplierKeywordByNameChangedDate(sid, kid, rsname, r_changed_date)
            elif (len(args) == 2) and rsname and rqty:
                resource_list = dao.getResourcesBySupplierKeywordByNameQty(sid, kid, rsname, rqty)
            elif (len(args) == 2) and rsname and rprice:
                resource_list = dao.getResourcesBySupplierKeywordByNamePrice(sid, kid, rsname, rprice)
            elif (len(args) == 2) and rsname and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordByNameSupplyDate(sid, kid, rsname, r_supply_date)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesBySupplierKeywordByChangedDateQty(sid, kid, r_changed_date, rqty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesBySupplierKeywordByChangedDatePrice(sid, kid, r_changed_date, rprice)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordByChangedDateSupplyDate(sid, kid, r_changed_date, r_supply_date)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesBySupplierKeywordByQtyPrice(sid, kid, rqty, rprice)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordByQtySupplyDate(sid, kid, rqty, r_supply_date)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordByPriceSupplyDate(sid, kid, rprice, r_supply_date)
            elif (len(args) == 1) and rsname:
                resource_list = dao.getResourcesBySupplierKeywordByName(sid, kid, rsname)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesBySupplierKeywordByChangedDate(sid, kid, r_changed_date)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesBySupplierKeywordByQty(sid, kid, rqty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesBySupplierKeywordByPrice(sid, kid, rprice)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordBySupplyDate(sid, kid, r_supply_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resource Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def getResourcesBySupplierCategory(self, sid, cat_name):
        if not SupplierDAO().getSupplierById(sid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Supplier and Category Not Found"), 404
        elif not SupplierDAO().getSupplierById(sid):
            return jsonify(Error = "Supplier Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            resource_list = ResourceDAO().getResourcesBySupplierCategory(sid, cat_name)
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resources Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def searchResourcesBySupplierCategory(self, sid, cat_name, args):
        if not SupplierDAO().getSupplierById(sid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Supplier and Category Not Found"), 404
        elif not SupplierDAO().getSupplierById(sid):
            return jsonify(Error = "Supplier Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            rsname = args.get('rsname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rsname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryByNameChangedDateQtyPriceSupplyDate(sid, cat_name, rsname, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesBySupplierCategoryByNameChangedDateQtyPrice(sid, cat_name, rsname, r_changed_date, rqty, rprice)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryByNameChangedDateQtySupplyDate(sid, cat_name, rsname, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryByNameChangedDatePriceSupplyDate(sid, cat_name, rsname, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryByNameQtyPriceSupplyDate(sid, cat_name, rsname, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryByChangedDateQtyPriceSupplyDate(sid, cat_name, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 3) and rsname and r_changed_date and rqty:
                resource_list = dao.getResourcesBySupplierCategoryByNameChangedDateQty(sid, cat_name, rsname, r_changed_date, rqty)
            elif (len(args) == 3) and rsname and r_changed_date and rprice:
                resource_list = dao.getResourcesBySupplierCategoryByNameChangedDatePrice(sid, cat_name, rsname, r_changed_date, rprice)
            elif (len(args) == 3) and rsname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryByNameChangedDateSupplyDate(sid, cat_name, rsname, r_changed_date, r_supply_date)
            elif (len(args) == 3) and rsname and rqty and rprice:
                resource_list = dao.getResourcesBySupplierCategoryByNameQtyPrice(sid, cat_name, rsname, rqty, rprice)
            elif (len(args) == 3) and rsname and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryByNameQtySupplyDate(sid, cat_name, rsname, rqty, r_supply_date)
            elif (len(args) == 3) and rsname and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryByNamePriceSupplyDate(sid, cat_name, rsname, rprice, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesBySupplierCategoryByChangedDateQtyPrice(sid, cat_name, r_changed_date, rqty, rprice)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryByChangedDateQtySupplyDate(sid, cat_name, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryByChangedDatePriceSupplyDate(sid, cat_name, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryByQtyPriceSupplyDate(sid, cat_name, rqty, rprice, r_supply_date)
            elif (len(args) == 2) and rsname and r_changed_date:
                resource_list = dao.getResourcesBySupplierCategoryByNameChangedDate(sid, cat_name, rsname, r_changed_date)
            elif (len(args) == 2) and rsname and rqty:
                resource_list = dao.getResourcesBySupplierCategoryByNameQty(sid, cat_name, rsname, rqty)
            elif (len(args) == 2) and rsname and rprice:
                resource_list = dao.getResourcesBySupplierCategoryByNamePrice(sid, cat_name, rsname, rprice)
            elif (len(args) == 2) and rsname and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryByNameSupplyDate(sid, cat_name, rsname, r_supply_date)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesBySupplierCategoryByChangedDateQty(sid, cat_name, r_changed_date, rqty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesBySupplierCategoryByChangedDatePrice(sid, cat_name, r_changed_date, rprice)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryByChangedDateSupplyDate(sid, cat_name, r_changed_date, r_supply_date)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesBySupplierCategoryByQtyPrice(sid, cat_name, rqty, rprice)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryByQtySupplyDate(sid, cat_name, rqty, r_supply_date)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryByPriceSupplyDate(sid, cat_name, rprice, r_supply_date)
            elif (len(args) == 1) and rsname:
                resource_list = dao.getResourcesBySupplierCategoryByName(sid, cat_name, rsname)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesBySupplierCategoryByChangedDate(sid, cat_name, r_changed_date)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesBySupplierCategoryByQty(sid, cat_name, rqty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesBySupplierCategoryByPrice(sid, cat_name, rprice)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryBySupplyDate(sid, cat_name, r_supply_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resource Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def getResourcesBySupplierOrder(self, sid, oid):
        if not SupplierDAO().getSupplierById(sid) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Supplier and Order Not Found"), 404
        elif not SupplierDAO().getSupplierById(sid):
            return jsonify(Error = "Supplier Not Found"), 404
        elif not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Order Not Found"), 404
        else:
            resource_list = ResourceDAO().getResourcesBySupplierOrder(sid, oid)
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resources Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def searchResourcesBySupplierOrder(self, sid, oid, args):
        if not SupplierDAO().getSupplierById(sid) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Supplier and Order Not Found"), 404
        elif not SupplierDAO().getSupplierById(sid):
            return jsonify(Error = "Supplier Not Found"), 404
        elif not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Order Not Found"), 404
        else:
            rsname = args.get('rsname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rsname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierOrderByNameChangedDateQtyPriceSupplyDate(sid, oid, rsname, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesBySupplierOrderByNameChangedDateQtyPrice(sid, oid, rsname, r_changed_date, rqty, rprice)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierOrderByNameChangedDateQtySupplyDate(sid, oid, rsname, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierOrderByNameChangedDatePriceSupplyDate(sid, oid, rsname, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierOrderByNameQtyPriceSupplyDate(sid, oid, rsname, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierOrderByChangedDateQtyPriceSupplyDate(sid, oid, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 3) and rsname and r_changed_date and rqty:
                resource_list = dao.getResourcesBySupplierOrderByNameChangedDateQty(sid, oid, rsname, r_changed_date, rqty)
            elif (len(args) == 3) and rsname and r_changed_date and rprice:
                resource_list = dao.getResourcesBySupplierOrderByNameChangedDatePrice(sid, oid, rsname, r_changed_date, rprice)
            elif (len(args) == 3) and rsname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesBySupplierOrderByNameChangedDateSupplyDate(sid, oid, rsname, r_changed_date, r_supply_date)
            elif (len(args) == 3) and rsname and rqty and rprice:
                resource_list = dao.getResourcesBySupplierOrderByNameQtyPrice(sid, oid, rsname, rqty, rprice)
            elif (len(args) == 3) and rsname and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierOrderByNameQtySupplyDate(sid, oid, rsname, rqty, r_supply_date)
            elif (len(args) == 3) and rsname and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierOrderByNamePriceSupplyDate(sid, oid, rsname, rprice, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesBySupplierOrderByChangedDateQtyPrice(sid, oid, r_changed_date, rqty, rprice)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierOrderByChangedDateQtySupplyDate(sid, oid, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierOrderByChangedDatePriceSupplyDate(sid, oid, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierOrderByQtyPriceSupplyDate(sid, oid, rqty, rprice, r_supply_date)
            elif (len(args) == 2) and rsname and r_changed_date:
                resource_list = dao.getResourcesBySupplierOrderByNameChangedDate(sid, oid, rsname, r_changed_date)
            elif (len(args) == 2) and rsname and rqty:
                resource_list = dao.getResourcesBySupplierOrderByNameQty(sid, oid, rsname, rqty)
            elif (len(args) == 2) and rsname and rprice:
                resource_list = dao.getResourcesBySupplierOrderByNamePrice(sid, oid, rsname, rprice)
            elif (len(args) == 2) and rsname and r_supply_date:
                resource_list = dao.getResourcesBySupplierOrderByNameSupplyDate(sid, oid, rsname, r_supply_date)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesBySupplierOrderByChangedDateQty(sid, oid, r_changed_date, rqty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesBySupplierOrderByChangedDatePrice(sid, oid, r_changed_date, rprice)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesBySupplierOrderByChangedDateSupplyDate(sid, oid, r_changed_date, r_supply_date)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesBySupplierOrderByQtyPrice(sid, oid, rqty, rprice)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierOrderByQtySupplyDate(sid, oid, rqty, r_supply_date)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierOrderByPriceSupplyDate(sid, oid, rprice, r_supply_date)
            elif (len(args) == 1) and rsname:
                resource_list = dao.getResourcesBySupplierOrderByName(sid, oid, rsname)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesBySupplierOrderByChangedDate(sid, oid, r_changed_date)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesBySupplierOrderByQty(sid, oid, rqty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesBySupplierOrderByPrice(sid, oid, rprice)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesBySupplierOrderBySupplyDate(sid, oid, r_supply_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resource Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def getResourcesByKeywordCategory(self, kid, cat_name):
        if not KeywordDAO().getKeywordById(kid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Keyword and Category Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            resource_list = ResourceDAO().getResourcesByKeywordCategory(kid, cat_name)
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resources Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def searchResourcesByKeywordCategory(self, kid, cat_name, args):
        if not KeywordDAO().getKeywordById(kid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Keyword and Category Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            rsname = args.get('rsname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rsname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryByNameChangedDateQtyPriceSupplyDate(kid, cat_name, rsname, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByKeywordCategoryByNameChangedDateQtyPrice(kid, cat_name, rsname, r_changed_date, rqty, rprice)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryByNameChangedDateQtySupplyDate(kid, cat_name, rsname, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryByNameChangedDatePriceSupplyDate(kid, cat_name, rsname, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryByNameQtyPriceSupplyDate(kid, cat_name, rsname, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryByChangedDateQtyPriceSupplyDate(kid, cat_name, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 3) and rsname and r_changed_date and rqty:
                resource_list = dao.getResourcesByKeywordCategoryByNameChangedDateQty(kid, cat_name, rsname, r_changed_date, rqty)
            elif (len(args) == 3) and rsname and r_changed_date and rprice:
                resource_list = dao.getResourcesByKeywordCategoryByNameChangedDatePrice(kid, cat_name, rsname, r_changed_date, rprice)
            elif (len(args) == 3) and rsname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryByNameChangedDateSupplyDate(kid, cat_name, rsname, r_changed_date, r_supply_date)
            elif (len(args) == 3) and rsname and rqty and rprice:
                resource_list = dao.getResourcesByKeywordCategoryByNameQtyPrice(kid, cat_name, rsname, rqty, rprice)
            elif (len(args) == 3) and rsname and rqty and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryByNameQtySupplyDate(kid, cat_name, rsname, rqty, r_supply_date)
            elif (len(args) == 3) and rsname and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryByNamePriceSupplyDate(kid, cat_name, rsname, rprice, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByKeywordCategoryByChangedDateQtyPrice(kid, cat_name, r_changed_date, rqty, rprice)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryByChangedDateQtySupplyDate(kid, cat_name, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryByChangedDatePriceSupplyDate(kid, cat_name, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryByQtyPriceSupplyDate(kid, cat_name, rqty, rprice, r_supply_date)
            elif (len(args) == 2) and rsname and r_changed_date:
                resource_list = dao.getResourcesByKeywordCategoryByNameChangedDate(kid, cat_name, rsname, r_changed_date)
            elif (len(args) == 2) and rsname and rqty:
                resource_list = dao.getResourcesByKeywordCategoryByNameQty(kid, cat_name, rsname, rqty)
            elif (len(args) == 2) and rsname and rprice:
                resource_list = dao.getResourcesByKeywordCategoryByNamePrice(kid, cat_name, rsname, rprice)
            elif (len(args) == 2) and rsname and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryByNameSupplyDate(kid, cat_name, rsname, r_supply_date)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByKeywordCategoryByChangedDateQty(kid, cat_name, r_changed_date, rqty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByKeywordCategoryByChangedDatePrice(kid, cat_name, r_changed_date, rprice)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryByChangedDateSupplyDate(kid, cat_name, r_changed_date, r_supply_date)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByKeywordCategoryByQtyPrice(kid, cat_name, rqty, rprice)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryByQtySupplyDate(kid, cat_name, rqty, r_supply_date)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryByPriceSupplyDate(kid, cat_name, rprice, r_supply_date)
            elif (len(args) == 1) and rsname:
                resource_list = dao.getResourcesByKeywordCategoryByName(kid, cat_name, rsname)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByKeywordCategoryByChangedDate(kid, cat_name, r_changed_date)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByKeywordCategoryByQty(kid, cat_name, rqty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByKeywordCategoryByPrice(kid, cat_name, rprice)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryBySupplyDate(kid, cat_name, r_supply_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resource Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def getResourcesByKeywordOrder(self, kid, oid):
        if not KeywordDAO().getKeywordById(kid) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Keyword and Order Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        elif not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Order Not Found"), 404
        else:
            resource_list = ResourceDAO().getResourcesByKeywordOrder(kid, oid)
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resources Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def searchResourcesByKeywordOrder(self, kid, oid, args):
        if not KeywordDAO().getKeywordById(kid) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Keyword and Order Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        elif not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Order Not Found"), 404
        else:
            rsname = args.get('rsname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rsname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordOrderByNameChangedDateQtyPriceSupplyDate(kid, oid, rsname, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByKeywordOrderByNameChangedDateQtyPrice(kid, oid, rsname, r_changed_date, rqty, rprice)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByKeywordOrderByNameChangedDateQtySupplyDate(kid, oid, rsname, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordOrderByNameChangedDatePriceSupplyDate(kid, oid, rsname, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordOrderByNameQtyPriceSupplyDate(kid, oid, rsname, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordOrderByChangedDateQtyPriceSupplyDate(kid, oid, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 3) and rsname and r_changed_date and rqty:
                resource_list = dao.getResourcesByKeywordOrderByNameChangedDateQty(kid, oid, rsname, r_changed_date, rqty)
            elif (len(args) == 3) and rsname and r_changed_date and rprice:
                resource_list = dao.getResourcesByKeywordOrderByNameChangedDatePrice(kid, oid, rsname, r_changed_date, rprice)
            elif (len(args) == 3) and rsname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByKeywordOrderByNameChangedDateSupplyDate(kid, oid, rsname, r_changed_date, r_supply_date)
            elif (len(args) == 3) and rsname and rqty and rprice:
                resource_list = dao.getResourcesByKeywordOrderByNameQtyPrice(kid, oid, rsname, rqty, rprice)
            elif (len(args) == 3) and rsname and rqty and r_supply_date:
                resource_list = dao.getResourcesByKeywordOrderByNameQtySupplyDate(kid, oid, rsname, rqty, r_supply_date)
            elif (len(args) == 3) and rsname and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordOrderByNamePriceSupplyDate(kid, oid, rsname, rprice, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByKeywordOrderByChangedDateQtyPrice(kid, oid, r_changed_date, rqty, rprice)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByKeywordOrderByChangedDateQtySupplyDate(kid, oid, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordOrderByChangedDatePriceSupplyDate(kid, oid, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordOrderByQtyPriceSupplyDate(kid, oid, rqty, rprice, r_supply_date)
            elif (len(args) == 2) and rsname and r_changed_date:
                resource_list = dao.getResourcesByKeywordOrderByNameChangedDate(kid, oid, rsname, r_changed_date)
            elif (len(args) == 2) and rsname and rqty:
                resource_list = dao.getResourcesByKeywordOrderByNameQty(kid, oid, rsname, rqty)
            elif (len(args) == 2) and rsname and rprice:
                resource_list = dao.getResourcesByKeywordOrderByNamePrice(kid, oid, rsname, rprice)
            elif (len(args) == 2) and rsname and r_supply_date:
                resource_list = dao.getResourcesByKeywordOrderByNameSupplyDate(kid, oid, rsname, r_supply_date)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByKeywordOrderByChangedDateQty(kid, oid, r_changed_date, rqty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByKeywordOrderByChangedDatePrice(kid, oid, r_changed_date, rprice)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByKeywordOrderByChangedDateSupplyDate(kid, oid, r_changed_date, r_supply_date)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByKeywordOrderByQtyPrice(kid, oid, rqty, rprice)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByKeywordOrderByQtySupplyDate(kid, oid, rqty, r_supply_date)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordOrderByPriceSupplyDate(kid, oid, rprice, r_supply_date)
            elif (len(args) == 1) and rsname:
                resource_list = dao.getResourcesByKeywordOrderByName(kid, oid, rsname)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByKeywordOrderByChangedDate(kid, oid, r_changed_date)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByKeywordOrderByQty(kid, oid, rqty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByKeywordOrderByPrice(kid, oid, rprice)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByKeywordOrderBySupplyDate(kid, oid, r_supply_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resource Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def getResourcesByCategoryOrder(self, cat_name, oid):
        if not CategoryDAO().getCategoryByName(cat_name) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Category and Order Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        elif not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Order Not Found"), 404
        else:
            resource_list = ResourceDAO().getResourcesByCategoryOrder(cat_name, oid)
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resources Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def searchResourcesByCategoryOrder(self, cat_name, oid, args):
        if not CategoryDAO().getCategoryByName(cat_name) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Category and Order Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        elif not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Order Not Found"), 404
        else:
            rsname = args.get('rsname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rsname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCategoryOrderByNameChangedDateQtyPriceSupplyDate(cat_name, oid, rsname, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByCategoryOrderByNameChangedDateQtyPrice(cat_name, oid, rsname, r_changed_date, rqty, rprice)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByCategoryOrderByNameChangedDateQtySupplyDate(cat_name, oid, rsname, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByCategoryOrderByNameChangedDatePriceSupplyDate(cat_name, oid, rsname, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCategoryOrderByNameQtyPriceSupplyDate(cat_name, oid, rsname, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCategoryOrderByChangedDateQtyPriceSupplyDate(cat_name, oid, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 3) and rsname and r_changed_date and rqty:
                resource_list = dao.getResourcesByCategoryOrderByNameChangedDateQty(cat_name, oid, rsname, r_changed_date, rqty)
            elif (len(args) == 3) and rsname and r_changed_date and rprice:
                resource_list = dao.getResourcesByCategoryOrderByNameChangedDatePrice(cat_name, oid, rsname, r_changed_date, rprice)
            elif (len(args) == 3) and rsname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByCategoryOrderByNameChangedDateSupplyDate(cat_name, oid, rsname, r_changed_date, r_supply_date)
            elif (len(args) == 3) and rsname and rqty and rprice:
                resource_list = dao.getResourcesByCategoryOrderByNameQtyPrice(cat_name, oid, rsname, rqty, rprice)
            elif (len(args) == 3) and rsname and rqty and r_supply_date:
                resource_list = dao.getResourcesByCategoryOrderByNameQtySupplyDate(cat_name, oid, rsname, rqty, r_supply_date)
            elif (len(args) == 3) and rsname and rprice and r_supply_date:
                resource_list = dao.getResourcesByCategoryOrderByNamePriceSupplyDate(cat_name, oid, rsname, rprice, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByCategoryOrderByChangedDateQtyPrice(cat_name, oid, r_changed_date, rqty, rprice)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByCategoryOrderByChangedDateQtySupplyDate(cat_name, oid, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByCategoryOrderByChangedDatePriceSupplyDate(cat_name, oid, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCategoryOrderByQtyPriceSupplyDate(cat_name, oid, rqty, rprice, r_supply_date)
            elif (len(args) == 2) and rsname and r_changed_date:
                resource_list = dao.getResourcesByCategoryOrderByNameChangedDate(cat_name, oid, rsname, r_changed_date)
            elif (len(args) == 2) and rsname and rqty:
                resource_list = dao.getResourcesByCategoryOrderByNameQty(cat_name, oid, rsname, rqty)
            elif (len(args) == 2) and rsname and rprice:
                resource_list = dao.getResourcesByCategoryOrderByNamePrice(cat_name, oid, rsname, rprice)
            elif (len(args) == 2) and rsname and r_supply_date:
                resource_list = dao.getResourcesByCategoryOrderByNameSupplyDate(cat_name, oid, rsname, r_supply_date)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByCategoryOrderByChangedDateQty(cat_name, oid, r_changed_date, rqty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByCategoryOrderByChangedDatePrice(cat_name, oid, r_changed_date, rprice)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByCategoryOrderByChangedDateSupplyDate(cat_name, oid, r_changed_date, r_supply_date)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByCategoryOrderByQtyPrice(cat_name, oid, rqty, rprice)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByCategoryOrderByQtySupplyDate(cat_name, oid, rqty, r_supply_date)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByCategoryOrderByPriceSupplyDate(cat_name, oid, rprice, r_supply_date)
            elif (len(args) == 1) and rsname:
                resource_list = dao.getResourcesByCategoryOrderByName(cat_name, oid, rsname)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByCategoryOrderByChangedDate(cat_name, oid, r_changed_date)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByCategoryOrderByQty(cat_name, oid, rqty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByCategoryOrderByPrice(cat_name, oid, rprice)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByCategoryOrderBySupplyDate(cat_name, oid, r_supply_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resource Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def getResourcesByTransactionOrder(self, tid, oid):
        if not TransactionDAO().getTransactionById(tid) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Transaction and Order Not Found"), 404
        elif not TransactionDAO().getTransactionById(tid):
            return jsonify(Error = "Transaction Not Found"), 404
        elif not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Order Not Found"), 404
        else:
            resource_list = ResourceDAO().getResourcesByTransactionOrder(tid, oid)
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resources Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def searchResourcesByTransactionOrder(self, tid, oid, args):
        if not TransactionDAO().getTransactionById(tid) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Transaction and Order Not Found"), 404
        elif not TransactionDAO().getTransactionById(tid):
            return jsonify(Error = "Transaction Not Found"), 404
        elif not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Order Not Found"), 404
        else:
            rsname = args.get('rsname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rsname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByTransactionOrderByNameChangedDateQtyPriceSupplyDate(tid, oid, rsname, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByTransactionOrderByNameChangedDateQtyPrice(tid, oid, rsname, r_changed_date, rqty, rprice)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByTransactionOrderByNameChangedDateQtySupplyDate(tid, oid, rsname, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByTransactionOrderByNameChangedDatePriceSupplyDate(tid, oid, rsname, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByTransactionOrderByNameQtyPriceSupplyDate(tid, oid, rsname, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByTransactionOrderByChangedDateQtyPriceSupplyDate(tid, oid, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 3) and rsname and r_changed_date and rqty:
                resource_list = dao.getResourcesByTransactionOrderByNameChangedDateQty(tid, oid, rsname, r_changed_date, rqty)
            elif (len(args) == 3) and rsname and r_changed_date and rprice:
                resource_list = dao.getResourcesByTransactionOrderByNameChangedDatePrice(tid, oid, rsname, r_changed_date, rprice)
            elif (len(args) == 3) and rsname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByTransactionOrderByNameChangedDateSupplyDate(tid, oid, rsname, r_changed_date, r_supply_date)
            elif (len(args) == 3) and rsname and rqty and rprice:
                resource_list = dao.getResourcesByTransactionOrderByNameQtyPrice(tid, oid, rsname, rqty, rprice)
            elif (len(args) == 3) and rsname and rqty and r_supply_date:
                resource_list = dao.getResourcesByTransactionOrderByNameQtySupplyDate(tid, oid, rsname, rqty, r_supply_date)
            elif (len(args) == 3) and rsname and rprice and r_supply_date:
                resource_list = dao.getResourcesByTransactionOrderByNamePriceSupplyDate(tid, oid, rsname, rprice, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByTransactionOrderByChangedDateQtyPrice(tid, oid, r_changed_date, rqty, rprice)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByTransactionOrderByChangedDateQtySupplyDate(tid, oid, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByTransactionOrderByChangedDatePriceSupplyDate(tid, oid, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByTransactionOrderByQtyPriceSupplyDate(tid, oid, rqty, rprice, r_supply_date)
            elif (len(args) == 2) and rsname and r_changed_date:
                resource_list = dao.getResourcesByTransactionOrderByNameChangedDate(tid, oid, rsname, r_changed_date)
            elif (len(args) == 2) and rsname and rqty:
                resource_list = dao.getResourcesByTransactionOrderByNameQty(tid, oid, rsname, rqty)
            elif (len(args) == 2) and rsname and rprice:
                resource_list = dao.getResourcesByTransactionOrderByNamePrice(tid, oid, rsname, rprice)
            elif (len(args) == 2) and rsname and r_supply_date:
                resource_list = dao.getResourcesByTransactionOrderByNameSupplyDate(tid, oid, rsname, r_supply_date)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByTransactionOrderByChangedDateQty(tid, oid, r_changed_date, rqty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByTransactionOrderByChangedDatePrice(tid, oid, r_changed_date, rprice)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByTransactionOrderByChangedDateSupplyDate(tid, oid, r_changed_date, r_supply_date)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByTransactionOrderByQtyPrice(tid, oid, rqty, rprice)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByTransactionOrderByQtySupplyDate(tid, oid, rqty, r_supply_date)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByTransactionOrderByPriceSupplyDate(tid, oid, rprice, r_supply_date)
            elif (len(args) == 1) and rsname:
                resource_list = dao.getResourcesByTransactionOrderByName(tid, oid, rsname)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByTransactionOrderByChangedDate(tid, oid, r_changed_date)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByTransactionOrderByQty(tid, oid, rqty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByTransactionOrderByPrice(tid, oid, rprice)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByTransactionOrderBySupplyDate(tid, oid, r_supply_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resource Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def getResourcesByCityKeywordCategory(self, cname, kid, cat_name):
        if not CityDAO().getCityByName(cname) and not KeywordDAO().getKeywordById(kid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "City, Keyword, and Category Not Found"), 404
        elif not CityDAO().getCityByName(cname) and not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "City and Keyword Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Keyword and Category Not Found"), 404
        elif not CityDAO().getCityByName(cname):
            return jsonify(Error = "City Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            resource_list = ResourceDAO().getResourcesByCityKeywordCategory(cname, kid, cat_name)
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resources Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def searchResourcesByCityKeywordCategory(self, cname, kid, cat_name, args):
        if not CityDAO().getCityByName(cname) and not KeywordDAO().getKeywordById(kid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "City, Keyword, and Category Not Found"), 404
        elif not CityDAO().getCityByName(cname) and not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "City and Keyword Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Keyword and Category Not Found"), 404
        elif not CityDAO().getCityByName(cname):
            return jsonify(Error = "City Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            rsname = args.get('rsname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rsname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordCategoryByNameChangedDateQtyPriceSupplyDate(cname, kid, cat_name, rsname, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByCityKeywordCategoryByNameChangedDateQtyPrice(cname, kid, cat_name, rsname, r_changed_date, rqty, rprice)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordCategoryByNameChangedDateQtySupplyDate(cname, kid, cat_name, rsname, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordCategoryByNameChangedDatePriceSupplyDate(cname, kid, cat_name, rsname, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordCategoryByNameQtyPriceSupplyDate(cname, kid, cat_name, rsname, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordCategoryByChangedDateQtyPriceSupplyDate(cname, kid, cat_name, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 3) and rsname and r_changed_date and rqty:
                resource_list = dao.getResourcesByCityKeywordCategoryByNameChangedDateQty(cname, kid, cat_name, rsname, r_changed_date, rqty)
            elif (len(args) == 3) and rsname and r_changed_date and rprice:
                resource_list = dao.getResourcesByCityKeywordCategoryByNameChangedDatePrice(cname, kid, cat_name, rsname, r_changed_date, rprice)
            elif (len(args) == 3) and rsname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordCategoryByNameChangedDateSupplyDate(cname, kid, cat_name, rsname, r_changed_date, r_supply_date)
            elif (len(args) == 3) and rsname and rqty and rprice:
                resource_list = dao.getResourcesByCityKeywordCategoryByNameQtyPrice(cname, kid, cat_name, rsname, rqty, rprice)
            elif (len(args) == 3) and rsname and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordCategoryByNameQtySupplyDate(cname, kid, cat_name, rsname, rqty, r_supply_date)
            elif (len(args) == 3) and rsname and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordCategoryByNamePriceSupplyDate(cname, kid, cat_name, rsname, rprice, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByCityKeywordCategoryByChangedDateQtyPrice(cname, kid, cat_name, r_changed_date, rqty, rprice)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordCategoryByChangedDateQtySupplyDate(cname, kid, cat_name, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordCategoryByChangedDatePriceSupplyDate(cname, kid, cat_name, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordCategoryByQtyPriceSupplyDate(cname, kid, cat_name, rqty, rprice, r_supply_date)
            elif (len(args) == 2) and rsname and r_changed_date:
                resource_list = dao.getResourcesByCityKeywordCategoryByNameChangedDate(cname, kid, cat_name, rsname, r_changed_date)
            elif (len(args) == 2) and rsname and rqty:
                resource_list = dao.getResourcesByCityKeywordCategoryByNameQty(cname, kid, cat_name, rsname, rqty)
            elif (len(args) == 2) and rsname and rprice:
                resource_list = dao.getResourcesByCityKeywordCategoryByNamePrice(cname, kid, cat_name, rsname, rprice)
            elif (len(args) == 2) and rsname and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordCategoryByNameSupplyDate(cname, kid, cat_name, rsname, r_supply_date)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByCityKeywordCategoryByChangedDateQty(cname, kid, cat_name, r_changed_date, rqty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByCityKeywordCategoryByChangedDatePrice(cname, kid, cat_name, r_changed_date, rprice)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordCategoryByChangedDateSupplyDate(cname, kid, cat_name, r_changed_date, r_supply_date)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByCityKeywordCategoryByQtyPrice(cname, kid, cat_name, rqty, rprice)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordCategoryByQtySupplyDate(cname, kid, cat_name, rqty, r_supply_date)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordCategoryByPriceSupplyDate(cname, kid, cat_name, rprice, r_supply_date)
            elif (len(args) == 1) and rsname:
                resource_list = dao.getResourcesByCityKeywordCategoryByName(cname, kid, cat_name, rsname)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByCityKeywordCategoryByChangedDate(cname, kid, cat_name, r_changed_date)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByCityKeywordCategoryByQty(cname, kid, cat_name, rqty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByCityKeywordCategoryByPrice(cname, kid, cat_name, rprice)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordCategoryBySupplyDate(cname, kid, cat_name, r_supply_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resource Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def getResourcesByCityKeywordOrder(self, cname, kid, oid):
        if not CityDAO().getCityByName(cname) and not KeywordDAO().getKeywordById(kid) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "City, Keyword, and Order Not Found"), 404
        elif not CityDAO().getCityByName(cname) and not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "City and Keyword Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Keyword and Order Not Found"), 404
        elif not CityDAO().getCityByName(cname):
            return jsonify(Error = "City Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        elif not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Order Not Found"), 404
        else:
            resource_list = ResourceDAO().getResourcesByCityKeywordOrder(cname, kid, oid)
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resources Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def searchResourcesByCityKeywordOrder(self, cname, kid, oid, args):
        if not CityDAO().getCityByName(cname) and not KeywordDAO().getKeywordById(kid) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "City, Keyword, and Order Not Found"), 404
        elif not CityDAO().getCityByName(cname) and not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "City and Keyword Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Keyword and Order Not Found"), 404
        elif not CityDAO().getCityByName(cname):
            return jsonify(Error = "City Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        elif not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Order Not Found"), 404
        else:
            rsname = args.get('rsname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rsname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordOrderByNameChangedDateQtyPriceSupplyDate(cname, kid, oid, rsname, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByCityKeywordOrderByNameChangedDateQtyPrice(cname, kid, oid, rsname, r_changed_date, rqty, rprice)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordOrderByNameChangedDateQtySupplyDate(cname, kid, oid, rsname, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordOrderByNameChangedDatePriceSupplyDate(cname, kid, oid, rsname, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordOrderByNameQtyPriceSupplyDate(cname, kid, oid, rsname, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordOrderByChangedDateQtyPriceSupplyDate(cname, kid, oid, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 3) and rsname and r_changed_date and rqty:
                resource_list = dao.getResourcesByCityKeywordOrderByNameChangedDateQty(cname, kid, oid, rsname, r_changed_date, rqty)
            elif (len(args) == 3) and rsname and r_changed_date and rprice:
                resource_list = dao.getResourcesByCityKeywordOrderByNameChangedDatePrice(cname, kid, oid, rsname, r_changed_date, rprice)
            elif (len(args) == 3) and rsname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordOrderByNameChangedDateSupplyDate(cname, kid, oid, rsname, r_changed_date, r_supply_date)
            elif (len(args) == 3) and rsname and rqty and rprice:
                resource_list = dao.getResourcesByCityKeywordOrderByNameQtyPrice(cname, kid, oid, rsname, rqty, rprice)
            elif (len(args) == 3) and rsname and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordOrderByNameQtySupplyDate(cname, kid, oid, rsname, rqty, r_supply_date)
            elif (len(args) == 3) and rsname and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordOrderByNamePriceSupplyDate(cname, kid, oid, rsname, rprice, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByCityKeywordOrderByChangedDateQtyPrice(cname, kid, oid, r_changed_date, rqty, rprice)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordOrderByChangedDateQtySupplyDate(cname, kid, oid, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordOrderByChangedDatePriceSupplyDate(cname, kid, oid, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordOrderByQtyPriceSupplyDate(cname, kid, oid, rqty, rprice, r_supply_date)
            elif (len(args) == 2) and rsname and r_changed_date:
                resource_list = dao.getResourcesByCityKeywordOrderByNameChangedDate(cname, kid, oid, rsname, r_changed_date)
            elif (len(args) == 2) and rsname and rqty:
                resource_list = dao.getResourcesByCityKeywordOrderByNameQty(cname, kid, oid, rsname, rqty)
            elif (len(args) == 2) and rsname and rprice:
                resource_list = dao.getResourcesByCityKeywordOrderByNamePrice(cname, kid, oid, rsname, rprice)
            elif (len(args) == 2) and rsname and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordOrderByNameSupplyDate(cname, kid, oid, rsname, r_supply_date)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByCityKeywordOrderByChangedDateQty(cname, kid, oid, r_changed_date, rqty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByCityKeywordOrderByChangedDatePrice(cname, kid, oid, r_changed_date, rprice)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordOrderByChangedDateSupplyDate(cname, kid, oid, r_changed_date, r_supply_date)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByCityKeywordOrderByQtyPrice(cname, kid, oid, rqty, rprice)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordOrderByQtySupplyDate(cname, kid, oid, rqty, r_supply_date)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordOrderByPriceSupplyDate(cname, kid, oid, rprice, r_supply_date)
            elif (len(args) == 1) and rsname:
                resource_list = dao.getResourcesByCityKeywordOrderByName(cname, kid, oid, rsname)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByCityKeywordOrderByChangedDate(cname, kid, oid, r_changed_date)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByCityKeywordOrderByQty(cname, kid, oid, rqty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByCityKeywordOrderByPrice(cname, kid, oid, rprice)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordOrderBySupplyDate(cname, kid, oid, r_supply_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resource Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def getResourcesByCityCategoryOrder(self, cname, cat_name, oid):
        if not CityDAO().getCityByName(cname) and not CategoryDAO().getCategoryByName(cat_name) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "City, Category, and Order Not Found"), 404
        elif not CityDAO().getCityByName(cname) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "City and Category Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Category and Order Not Found"), 404
        elif not CityDAO().getCityByName(cname):
            return jsonify(Error = "City Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        elif not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Order Not Found"), 404
        else:
            resource_list = ResourceDAO().getResourcesByCityCategoryOrder(cname, cat_name, oid)
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resources Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def searchResourcesByCityCategoryOrder(self, cname, cat_name, oid, args):
        if not CityDAO().getCityByName(cname) and not CategoryDAO().getCategoryByName(cat_name) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "City, Category, and Order Not Found"), 404
        elif not CityDAO().getCityByName(cname) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "City and Category Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Category and Order Not Found"), 404
        elif not CityDAO().getCityByName(cname):
            return jsonify(Error = "City Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        elif not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Order Not Found"), 404
        else:
            rsname = args.get('rsname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rsname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryOrderByNameChangedDateQtyPriceSupplyDate(cname, cat_name, oid, rsname, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByCityCategoryOrderByNameChangedDateQtyPrice(cname, cat_name, oid, rsname, r_changed_date, rqty, rprice)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryOrderByNameChangedDateQtySupplyDate(cname, cat_name, oid, rsname, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryOrderByNameChangedDatePriceSupplyDate(cname, cat_name, oid, rsname, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryOrderByNameQtyPriceSupplyDate(cname, cat_name, oid, rsname, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryOrderByChangedDateQtyPriceSupplyDate(cname, cat_name, oid, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 3) and rsname and r_changed_date and rqty:
                resource_list = dao.getResourcesByCityCategoryOrderByNameChangedDateQty(cname, cat_name, oid, rsname, r_changed_date, rqty)
            elif (len(args) == 3) and rsname and r_changed_date and rprice:
                resource_list = dao.getResourcesByCityCategoryOrderByNameChangedDatePrice(cname, cat_name, oid, rsname, r_changed_date, rprice)
            elif (len(args) == 3) and rsname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryOrderByNameChangedDateSupplyDate(cname, cat_name, oid, rsname, r_changed_date, r_supply_date)
            elif (len(args) == 3) and rsname and rqty and rprice:
                resource_list = dao.getResourcesByCityCategoryOrderByNameQtyPrice(cname, cat_name, oid, rsname, rqty, rprice)
            elif (len(args) == 3) and rsname and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryOrderByNameQtySupplyDate(cname, cat_name, oid, rsname, rqty, r_supply_date)
            elif (len(args) == 3) and rsname and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryOrderByNamePriceSupplyDate(cname, cat_name, oid, rsname, rprice, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByCityCategoryOrderByChangedDateQtyPrice(cname, cat_name, oid, r_changed_date, rqty, rprice)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryOrderByChangedDateQtySupplyDate(cname, cat_name, oid, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryOrderByChangedDatePriceSupplyDate(cname, cat_name, oid, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryOrderByQtyPriceSupplyDate(cname, cat_name, oid, rqty, rprice, r_supply_date)
            elif (len(args) == 2) and rsname and r_changed_date:
                resource_list = dao.getResourcesByCityCategoryOrderByNameChangedDate(cname, cat_name, oid, rsname, r_changed_date)
            elif (len(args) == 2) and rsname and rqty:
                resource_list = dao.getResourcesByCityCategoryOrderByNameQty(cname, cat_name, oid, rsname, rqty)
            elif (len(args) == 2) and rsname and rprice:
                resource_list = dao.getResourcesByCityCategoryOrderByNamePrice(cname, cat_name, oid, rsname, rprice)
            elif (len(args) == 2) and rsname and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryOrderByNameSupplyDate(cname, cat_name, oid, rsname, r_supply_date)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByCityCategoryOrderByChangedDateQty(cname, cat_name, oid, r_changed_date, rqty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByCityCategoryOrderByChangedDatePrice(cname, cat_name, oid, r_changed_date, rprice)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryOrderByChangedDateSupplyDate(cname, cat_name, oid, r_changed_date, r_supply_date)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByCityCategoryOrderByQtyPrice(cname, cat_name, oid, rqty, rprice)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryOrderByQtySupplyDate(cname, cat_name, oid, rqty, r_supply_date)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryOrderByPriceSupplyDate(cname, cat_name, oid, rprice, r_supply_date)
            elif (len(args) == 1) and rsname:
                resource_list = dao.getResourcesByCityCategoryOrderByName(cname, cat_name, oid, rsname)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByCityCategoryOrderByChangedDate(cname, cat_name, oid, r_changed_date)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByCityCategoryOrderByQty(cname, cat_name, oid, rqty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByCityCategoryOrderByPrice(cname, cat_name, oid, rprice)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryOrderBySupplyDate(cname, cat_name, oid, r_supply_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resource Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def getResourcesByRegionKeywordCategory(self, rname, kid, cat_name):
        if not RegionDAO().getRegionByName(rname) and not KeywordDAO().getKeywordById(kid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Region, Keyword, and Category Not Found"), 404
        elif not RegionDAO().getRegionByName(rname) and not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Region and Keyword Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Keyword and Category Not Found"), 404
        elif not RegionDAO().getRegionByName(rname):
            return jsonify(Error = "Region Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            resource_list = ResourceDAO().getResourcesByRegionKeywordCategory(rname, kid, cat_name)
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resources Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def searchResourcesByRegionKeywordCategory(self, rname, kid, cat_name, args):
        if not RegionDAO().getRegionByName(rname) and not KeywordDAO().getKeywordById(kid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Region, Keyword, and Category Not Found"), 404
        elif not RegionDAO().getRegionByName(rname) and not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Region and Keyword Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Keyword and Category Not Found"), 404
        elif not RegionDAO().getRegionByName(rname):
            return jsonify(Error = "Region Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            rsname = args.get('rsname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rsname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordCategoryByNameChangedDateQtyPriceSupplyDate(rname, kid, cat_name, rsname, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByRegionKeywordCategoryByNameChangedDateQtyPrice(rname, kid, cat_name, rsname, r_changed_date, rqty, rprice)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordCategoryByNameChangedDateQtySupplyDate(rname, kid, cat_name, rsname, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordCategoryByNameChangedDatePriceSupplyDate(rname, kid, cat_name, rsname, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordCategoryByNameQtyPriceSupplyDate(rname, kid, cat_name, rsname, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordCategoryByChangedDateQtyPriceSupplyDate(rname, kid, cat_name, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 3) and rsname and r_changed_date and rqty:
                resource_list = dao.getResourcesByRegionKeywordCategoryByNameChangedDateQty(rname, kid, cat_name, rsname, r_changed_date, rqty)
            elif (len(args) == 3) and rsname and r_changed_date and rprice:
                resource_list = dao.getResourcesByRegionKeywordCategoryByNameChangedDatePrice(rname, kid, cat_name, rsname, r_changed_date, rprice)
            elif (len(args) == 3) and rsname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordCategoryByNameChangedDateSupplyDate(rname, kid, cat_name, rsname, r_changed_date, r_supply_date)
            elif (len(args) == 3) and rsname and rqty and rprice:
                resource_list = dao.getResourcesByRegionKeywordCategoryByNameQtyPrice(rname, kid, cat_name, rsname, rqty, rprice)
            elif (len(args) == 3) and rsname and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordCategoryByNameQtySupplyDate(rname, kid, cat_name, rsname, rqty, r_supply_date)
            elif (len(args) == 3) and rsname and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordCategoryByNamePriceSupplyDate(rname, kid, cat_name, rsname, rprice, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByRegionKeywordCategoryByChangedDateQtyPrice(rname, kid, cat_name, r_changed_date, rqty, rprice)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordCategoryByChangedDateQtySupplyDate(rname, kid, cat_name, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordCategoryByChangedDatePriceSupplyDate(rname, kid, cat_name, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordCategoryByQtyPriceSupplyDate(rname, kid, cat_name, rqty, rprice, r_supply_date)
            elif (len(args) == 2) and rsname and r_changed_date:
                resource_list = dao.getResourcesByRegionKeywordCategoryByNameChangedDate(rname, kid, cat_name, rsname, r_changed_date)
            elif (len(args) == 2) and rsname and rqty:
                resource_list = dao.getResourcesByRegionKeywordCategoryByNameQty(rname, kid, cat_name, rsname, rqty)
            elif (len(args) == 2) and rsname and rprice:
                resource_list = dao.getResourcesByRegionKeywordCategoryByNamePrice(rname, kid, cat_name, rsname, rprice)
            elif (len(args) == 2) and rsname and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordCategoryByNameSupplyDate(rname, kid, cat_name, rsname, r_supply_date)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByRegionKeywordCategoryByChangedDateQty(rname, kid, cat_name, r_changed_date, rqty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByRegionKeywordCategoryByChangedDatePrice(rname, kid, cat_name, r_changed_date, rprice)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordCategoryByChangedDateSupplyDate(rname, kid, cat_name, r_changed_date, r_supply_date)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByRegionKeywordCategoryByQtyPrice(rname, kid, cat_name, rqty, rprice)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordCategoryByQtySupplyDate(rname, kid, cat_name, rqty, r_supply_date)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordCategoryByPriceSupplyDate(rname, kid, cat_name, rprice, r_supply_date)
            elif (len(args) == 1) and rsname:
                resource_list = dao.getResourcesByRegionKeywordCategoryByName(rname, kid, cat_name, rsname)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByRegionKeywordCategoryByChangedDate(rname, kid, cat_name, r_changed_date)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByRegionKeywordCategoryByQty(rname, kid, cat_name, rqty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByRegionKeywordCategoryByPrice(rname, kid, cat_name, rprice)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordCategoryBySupplyDate(rname, kid, cat_name, r_supply_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resource Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def getResourcesByRegionKeywordOrder(self, rname, kid, oid):
        if not RegionDAO().getRegionByName(rname) and not KeywordDAO().getKeywordById(kid) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Region, Keyword, and Order Not Found"), 404
        elif not RegionDAO().getRegionByName(rname) and not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Region and Keyword Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Keyword and Order Not Found"), 404
        elif not RegionDAO().getRegionByName(rname):
            return jsonify(Error = "Region Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        elif not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Order Not Found"), 404
        else:
            resource_list = ResourceDAO().getResourcesByRegionKeywordOrder(rname, kid, oid)
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resources Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def searchResourcesByRegionKeywordOrder(self, rname, kid, oid, args):
        if not RegionDAO().getRegionByName(rname) and not KeywordDAO().getKeywordById(kid) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Region, Keyword, and Order Not Found"), 404
        elif not RegionDAO().getRegionByName(rname) and not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Region and Keyword Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Keyword and Order Not Found"), 404
        elif not RegionDAO().getRegionByName(rname):
            return jsonify(Error = "Region Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        elif not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Order Not Found"), 404
        else:
            rsname = args.get('rsname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rsname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordOrderByNameChangedDateQtyPriceSupplyDate(rname, kid, oid, rsname, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByRegionKeywordOrderByNameChangedDateQtyPrice(rname, kid, oid, rsname, r_changed_date, rqty, rprice)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordOrderByNameChangedDateQtySupplyDate(rname, kid, oid, rsname, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordOrderByNameChangedDatePriceSupplyDate(rname, kid, oid, rsname, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordOrderByNameQtyPriceSupplyDate(rname, kid, oid, rsname, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordOrderByChangedDateQtyPriceSupplyDate(rname, kid, oid, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 3) and rsname and r_changed_date and rqty:
                resource_list = dao.getResourcesByRegionKeywordOrderByNameChangedDateQty(rname, kid, oid, rsname, r_changed_date, rqty)
            elif (len(args) == 3) and rsname and r_changed_date and rprice:
                resource_list = dao.getResourcesByRegionKeywordOrderByNameChangedDatePrice(rname, kid, oid, rsname, r_changed_date, rprice)
            elif (len(args) == 3) and rsname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordOrderByNameChangedDateSupplyDate(rname, kid, oid, rsname, r_changed_date, r_supply_date)
            elif (len(args) == 3) and rsname and rqty and rprice:
                resource_list = dao.getResourcesByRegionKeywordOrderByNameQtyPrice(rname, kid, oid, rsname, rqty, rprice)
            elif (len(args) == 3) and rsname and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordOrderByNameQtySupplyDate(rname, kid, oid, rsname, rqty, r_supply_date)
            elif (len(args) == 3) and rsname and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordOrderByNamePriceSupplyDate(rname, kid, oid, rsname, rprice, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByRegionKeywordOrderByChangedDateQtyPrice(rname, kid, oid, r_changed_date, rqty, rprice)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordOrderByChangedDateQtySupplyDate(rname, kid, oid, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordOrderByChangedDatePriceSupplyDate(rname, kid, oid, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordOrderByQtyPriceSupplyDate(rname, kid, oid, rqty, rprice, r_supply_date)
            elif (len(args) == 2) and rsname and r_changed_date:
                resource_list = dao.getResourcesByRegionKeywordOrderByNameChangedDate(rname, kid, oid, rsname, r_changed_date)
            elif (len(args) == 2) and rsname and rqty:
                resource_list = dao.getResourcesByRegionKeywordOrderByNameQty(rname, kid, oid, rsname, rqty)
            elif (len(args) == 2) and rsname and rprice:
                resource_list = dao.getResourcesByRegionKeywordOrderByNamePrice(rname, kid, oid, rsname, rprice)
            elif (len(args) == 2) and rsname and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordOrderByNameSupplyDate(rname, kid, oid, rsname, r_supply_date)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByRegionKeywordOrderByChangedDateQty(rname, kid, oid, r_changed_date, rqty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByRegionKeywordOrderByChangedDatePrice(rname, kid, oid, r_changed_date, rprice)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordOrderByChangedDateSupplyDate(rname, kid, oid, r_changed_date, r_supply_date)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByRegionKeywordOrderByQtyPrice(rname, kid, oid, rqty, rprice)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordOrderByQtySupplyDate(rname, kid, oid, rqty, r_supply_date)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordOrderByPriceSupplyDate(rname, kid, oid, rprice, r_supply_date)
            elif (len(args) == 1) and rsname:
                resource_list = dao.getResourcesByRegionKeywordOrderByName(rname, kid, oid, rsname)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByRegionKeywordOrderByChangedDate(rname, kid, oid, r_changed_date)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByRegionKeywordOrderByQty(rname, kid, oid, rqty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByRegionKeywordOrderByPrice(rname, kid, oid, rprice)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordOrderBySupplyDate(rname, kid, oid, r_supply_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resource Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def getResourcesByRegionCategoryOrder(self, rname, cat_name, oid):
        if not RegionDAO().getRegionByName(rname) and not CategoryDAO().getCategoryByName(cat_name) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Region, Category, and Order Not Found"), 404
        elif not RegionDAO().getRegionByName(rname) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Region and Category Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Category and Order Not Found"), 404
        elif not RegionDAO().getRegionByName(rname):
            return jsonify(Error = "Region Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        elif not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Order Not Found"), 404
        else:
            resource_list = ResourceDAO().getResourcesByRegionCategoryOrder(rname, cat_name, oid)
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resources Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def searchResourcesByRegionCategoryOrder(self, rname, cat_name, oid, args):
        if not RegionDAO().getRegionByName(rname) and not CategoryDAO().getCategoryByName(cat_name) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Region, Category, and Order Not Found"), 404
        elif not RegionDAO().getRegionByName(rname) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Region and Category Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Category and Order Not Found"), 404
        elif not RegionDAO().getRegionByName(rname):
            return jsonify(Error = "Region Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        elif not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Order Not Found"), 404
        else:
            rsname = args.get('rsname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rsname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryOrderByNameChangedDateQtyPriceSupplyDate(rname, cat_name, oid, rsname, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByRegionCategoryOrderByNameChangedDateQtyPrice(rname, cat_name, oid, rsname, r_changed_date, rqty, rprice)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryOrderByNameChangedDateQtySupplyDate(rname, cat_name, oid, rsname, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryOrderByNameChangedDatePriceSupplyDate(rname, cat_name, oid, rsname, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryOrderByNameQtyPriceSupplyDate(rname, cat_name, oid, rsname, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryOrderByChangedDateQtyPriceSupplyDate(rname, cat_name, oid, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 3) and rsname and r_changed_date and rqty:
                resource_list = dao.getResourcesByRegionCategoryOrderByNameChangedDateQty(rname, cat_name, oid, rsname, r_changed_date, rqty)
            elif (len(args) == 3) and rsname and r_changed_date and rprice:
                resource_list = dao.getResourcesByRegionCategoryOrderByNameChangedDatePrice(rname, cat_name, oid, rsname, r_changed_date, rprice)
            elif (len(args) == 3) and rsname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryOrderByNameChangedDateSupplyDate(rname, cat_name, oid, rsname, r_changed_date, r_supply_date)
            elif (len(args) == 3) and rsname and rqty and rprice:
                resource_list = dao.getResourcesByRegionCategoryOrderByNameQtyPrice(rname, cat_name, oid, rsname, rqty, rprice)
            elif (len(args) == 3) and rsname and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryOrderByNameQtySupplyDate(rname, cat_name, oid, rsname, rqty, r_supply_date)
            elif (len(args) == 3) and rsname and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryOrderByNamePriceSupplyDate(rname, cat_name, oid, rsname, rprice, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByRegionCategoryOrderByChangedDateQtyPrice(rname, cat_name, oid, r_changed_date, rqty, rprice)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryOrderByChangedDateQtySupplyDate(rname, cat_name, oid, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryOrderByChangedDatePriceSupplyDate(rname, cat_name, oid, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryOrderByQtyPriceSupplyDate(rname, cat_name, oid, rqty, rprice, r_supply_date)
            elif (len(args) == 2) and rsname and r_changed_date:
                resource_list = dao.getResourcesByRegionCategoryOrderByNameChangedDate(rname, cat_name, oid, rsname, r_changed_date)
            elif (len(args) == 2) and rsname and rqty:
                resource_list = dao.getResourcesByRegionCategoryOrderByNameQty(rname, cat_name, oid, rsname, rqty)
            elif (len(args) == 2) and rsname and rprice:
                resource_list = dao.getResourcesByRegionCategoryOrderByNamePrice(rname, cat_name, oid, rsname, rprice)
            elif (len(args) == 2) and rsname and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryOrderByNameSupplyDate(rname, cat_name, oid, rsname, r_supply_date)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByRegionCategoryOrderByChangedDateQty(rname, cat_name, oid, r_changed_date, rqty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByRegionCategoryOrderByChangedDatePrice(rname, cat_name, oid, r_changed_date, rprice)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryOrderByChangedDateSupplyDate(rname, cat_name, oid, r_changed_date, r_supply_date)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByRegionCategoryOrderByQtyPrice(rname, cat_name, oid, rqty, rprice)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryOrderByQtySupplyDate(rname, cat_name, oid, rqty, r_supply_date)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryOrderByPriceSupplyDate(rname, cat_name, oid, rprice, r_supply_date)
            elif (len(args) == 1) and rsname:
                resource_list = dao.getResourcesByRegionCategoryOrderByName(rname, cat_name, oid, rsname)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByRegionCategoryOrderByChangedDate(rname, cat_name, oid, r_changed_date)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByRegionCategoryOrderByQty(rname, cat_name, oid, rqty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByRegionCategoryOrderByPrice(rname, cat_name, oid, rprice)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryOrderBySupplyDate(rname, cat_name, oid, r_supply_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resource Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def getResourcesBySupplierKeywordCategory(self, sid, kid, cat_name):
        if not SupplierDAO().getSupplierById(sid) and not KeywordDAO().getKeywordById(kid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Supplier, Keyword, and Category Not Found"), 404
        elif not SupplierDAO().getSupplierById(sid) and not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Supplier and Keyword Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Keyword and Category Not Found"), 404
        elif not SupplierDAO().getSupplierById(sid):
            return jsonify(Error = "Supplier Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            resource_list = ResourceDAO().getResourcesBySupplierKeywordCategory(sid, kid, cat_name)
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resources Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def searchResourcesBySupplierKeywordCategory(self, sid, kid, cat_name, args):
        if not SupplierDAO().getSupplierById(sid) and not KeywordDAO().getKeywordById(kid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Supplier, Keyword, and Category Not Found"), 404
        elif not SupplierDAO().getSupplierById(sid) and not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Supplier and Keyword Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Keyword and Category Not Found"), 404
        elif not SupplierDAO().getSupplierById(sid):
            return jsonify(Error = "Supplier Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            rsname = args.get('rsname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rsname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByNameChangedDateQtyPriceSupplyDate(sid, kid, cat_name, rsname, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByNameChangedDateQtyPrice(sid, kid, cat_name, rsname, r_changed_date, rqty, rprice)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByNameChangedDateQtySupplyDate(sid, kid, cat_name, rsname, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByNameChangedDatePriceSupplyDate(sid, kid, cat_name, rsname, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByNameQtyPriceSupplyDate(sid, kid, cat_name, rsname, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByChangedDateQtyPriceSupplyDate(sid, kid, cat_name, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 3) and rsname and r_changed_date and rqty:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByNameChangedDateQty(sid, kid, cat_name, rsname, r_changed_date, rqty)
            elif (len(args) == 3) and rsname and r_changed_date and rprice:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByNameChangedDatePrice(sid, kid, cat_name, rsname, r_changed_date, rprice)
            elif (len(args) == 3) and rsname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByNameChangedDateSupplyDate(sid, kid, cat_name, rsname, r_changed_date, r_supply_date)
            elif (len(args) == 3) and rsname and rqty and rprice:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByNameQtyPrice(sid, kid, cat_name, rsname, rqty, rprice)
            elif (len(args) == 3) and rsname and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByNameQtySupplyDate(sid, kid, cat_name, rsname, rqty, r_supply_date)
            elif (len(args) == 3) and rsname and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByNamePriceSupplyDate(sid, kid, cat_name, rsname, rprice, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByChangedDateQtyPrice(sid, kid, cat_name, r_changed_date, rqty, rprice)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByChangedDateQtySupplyDate(sid, kid, cat_name, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByChangedDatePriceSupplyDate(sid, kid, cat_name, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByQtyPriceSupplyDate(sid, kid, cat_name, rqty, rprice, r_supply_date)
            elif (len(args) == 2) and rsname and r_changed_date:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByNameChangedDate(sid, kid, cat_name, rsname, r_changed_date)
            elif (len(args) == 2) and rsname and rqty:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByNameQty(sid, kid, cat_name, rsname, rqty)
            elif (len(args) == 2) and rsname and rprice:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByNamePrice(sid, kid, cat_name, rsname, rprice)
            elif (len(args) == 2) and rsname and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByNameSupplyDate(sid, kid, cat_name, rsname, r_supply_date)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByChangedDateQty(sid, kid, cat_name, r_changed_date, rqty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByChangedDatePrice(sid, kid, cat_name, r_changed_date, rprice)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByChangedDateSupplyDate(sid, kid, cat_name, r_changed_date, r_supply_date)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByQtyPrice(sid, kid, cat_name, rqty, rprice)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByQtySupplyDate(sid, kid, cat_name, rqty, r_supply_date)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByPriceSupplyDate(sid, kid, cat_name, rprice, r_supply_date)
            elif (len(args) == 1) and rsname:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByName(sid, kid, cat_name, rsname)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByChangedDate(sid, kid, cat_name, r_changed_date)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByQty(sid, kid, cat_name, rqty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByPrice(sid, kid, cat_name, rprice)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordCategoryBySupplyDate(sid, kid, cat_name, r_supply_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resource Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def getResourcesBySupplierKeywordOrder(self, sid, kid, oid):
        if not SupplierDAO().getSupplierById(sid) and not KeywordDAO().getKeywordById(kid) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Supplier, Keyword, and Order Not Found"), 404
        elif not SupplierDAO().getSupplierById(sid) and not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Supplier and Keyword Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Keyword and Order Not Found"), 404
        elif not SupplierDAO().getSupplierById(sid):
            return jsonify(Error = "Supplier Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        elif not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Order Not Found"), 404
        else:
            resource_list = ResourceDAO().getResourcesBySupplierKeywordOrder(sid, kid, oid)
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resources Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def searchResourcesBySupplierKeywordOrder(self, sid, kid, oid, args):
        if not SupplierDAO().getSupplierById(sid) and not KeywordDAO().getKeywordById(kid) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Supplier, Keyword, and Order Not Found"), 404
        elif not SupplierDAO().getSupplierById(sid) and not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Supplier and Keyword Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Keyword and Order Not Found"), 404
        elif not SupplierDAO().getSupplierById(sid):
            return jsonify(Error = "Supplier Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        elif not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Order Not Found"), 404
        else:
            rsname = args.get('rsname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rsname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordOrderByNameChangedDateQtyPriceSupplyDate(sid, kid, oid, rsname, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesBySupplierKeywordOrderByNameChangedDateQtyPrice(sid, kid, oid, rsname, r_changed_date, rqty, rprice)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordOrderByNameChangedDateQtySupplyDate(sid, kid, oid, rsname, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordOrderByNameChangedDatePriceSupplyDate(sid, kid, oid, rsname, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordOrderByNameQtyPriceSupplyDate(sid, kid, oid, rsname, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordOrderByChangedDateQtyPriceSupplyDate(sid, kid, oid, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 3) and rsname and r_changed_date and rqty:
                resource_list = dao.getResourcesBySupplierKeywordOrderByNameChangedDateQty(sid, kid, oid, rsname, r_changed_date, rqty)
            elif (len(args) == 3) and rsname and r_changed_date and rprice:
                resource_list = dao.getResourcesBySupplierKeywordOrderByNameChangedDatePrice(sid, kid, oid, rsname, r_changed_date, rprice)
            elif (len(args) == 3) and rsname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordOrderByNameChangedDateSupplyDate(sid, kid, oid, rsname, r_changed_date, r_supply_date)
            elif (len(args) == 3) and rsname and rqty and rprice:
                resource_list = dao.getResourcesBySupplierKeywordOrderByNameQtyPrice(sid, kid, oid, rsname, rqty, rprice)
            elif (len(args) == 3) and rsname and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordOrderByNameQtySupplyDate(sid, kid, oid, rsname, rqty, r_supply_date)
            elif (len(args) == 3) and rsname and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordOrderByNamePriceSupplyDate(sid, kid, oid, rsname, rprice, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesBySupplierKeywordOrderByChangedDateQtyPrice(sid, kid, oid, r_changed_date, rqty, rprice)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordOrderByChangedDateQtySupplyDate(sid, kid, oid, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordOrderByChangedDatePriceSupplyDate(sid, kid, oid, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordOrderByQtyPriceSupplyDate(sid, kid, oid, rqty, rprice, r_supply_date)
            elif (len(args) == 2) and rsname and r_changed_date:
                resource_list = dao.getResourcesBySupplierKeywordOrderByNameChangedDate(sid, kid, oid, rsname, r_changed_date)
            elif (len(args) == 2) and rsname and rqty:
                resource_list = dao.getResourcesBySupplierKeywordOrderByNameQty(sid, kid, oid, rsname, rqty)
            elif (len(args) == 2) and rsname and rprice:
                resource_list = dao.getResourcesBySupplierKeywordOrderByNamePrice(sid, kid, oid, rsname, rprice)
            elif (len(args) == 2) and rsname and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordOrderByNameSupplyDate(sid, kid, oid, rsname, r_supply_date)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesBySupplierKeywordOrderByChangedDateQty(sid, kid, oid, r_changed_date, rqty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesBySupplierKeywordOrderByChangedDatePrice(sid, kid, oid, r_changed_date, rprice)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordOrderByChangedDateSupplyDate(sid, kid, oid, r_changed_date, r_supply_date)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesBySupplierKeywordOrderByQtyPrice(sid, kid, oid, rqty, rprice)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordOrderByQtySupplyDate(sid, kid, oid, rqty, r_supply_date)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordOrderByPriceSupplyDate(sid, kid, oid, rprice, r_supply_date)
            elif (len(args) == 1) and rsname:
                resource_list = dao.getResourcesBySupplierKeywordOrderByName(sid, kid, oid, rsname)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesBySupplierKeywordOrderByChangedDate(sid, kid, oid, r_changed_date)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesBySupplierKeywordOrderByQty(sid, kid, oid, rqty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesBySupplierKeywordOrderByPrice(sid, kid, oid, rprice)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordOrderBySupplyDate(sid, kid, oid, r_supply_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resource Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def getResourcesBySupplierCategoryOrder(self, sid, cat_name, oid):
        if not SupplierDAO().getSupplierById(sid) and not CategoryDAO().getCategoryByName(cat_name) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Supplier, Category, and Order Not Found"), 404
        elif not SupplierDAO().getSupplierById(sid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Supplier and Category Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Category and Order Not Found"), 404
        elif not SupplierDAO().getSupplierById(sid):
            return jsonify(Error = "Supplier Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        elif not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Order Not Found"), 404
        else:
            resource_list = ResourceDAO().getResourcesBySupplierCategoryOrder(sid, cat_name, oid)
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resources Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def searchResourcesBySupplierCategoryOrder(self, sid, cat_name, oid, args):
        if not SupplierDAO().getSupplierById(sid) and not CategoryDAO().getCategoryByName(cat_name) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Supplier, Category, and Order Not Found"), 404
        elif not SupplierDAO().getSupplierById(sid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Supplier and Category Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Category and Order Not Found"), 404
        elif not SupplierDAO().getSupplierById(sid):
            return jsonify(Error = "Supplier Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        elif not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Order Not Found"), 404
        else:
            rsname = args.get('rsname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rsname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryOrderByNameChangedDateQtyPriceSupplyDate(sid, cat_name, oid, rsname, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesBySupplierCategoryOrderByNameChangedDateQtyPrice(sid, cat_name, oid, rsname, r_changed_date, rqty, rprice)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryOrderByNameChangedDateQtySupplyDate(sid, cat_name, oid, rsname, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryOrderByNameChangedDatePriceSupplyDate(sid, cat_name, oid, rsname, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryOrderByNameQtyPriceSupplyDate(sid, cat_name, oid, rsname, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryOrderByChangedDateQtyPriceSupplyDate(sid, cat_name, oid, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 3) and rsname and r_changed_date and rqty:
                resource_list = dao.getResourcesBySupplierCategoryOrderByNameChangedDateQty(sid, cat_name, oid, rsname, r_changed_date, rqty)
            elif (len(args) == 3) and rsname and r_changed_date and rprice:
                resource_list = dao.getResourcesBySupplierCategoryOrderByNameChangedDatePrice(sid, cat_name, oid, rsname, r_changed_date, rprice)
            elif (len(args) == 3) and rsname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryOrderByNameChangedDateSupplyDate(sid, cat_name, oid, rsname, r_changed_date, r_supply_date)
            elif (len(args) == 3) and rsname and rqty and rprice:
                resource_list = dao.getResourcesBySupplierCategoryOrderByNameQtyPrice(sid, cat_name, oid, rsname, rqty, rprice)
            elif (len(args) == 3) and rsname and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryOrderByNameQtySupplyDate(sid, cat_name, oid, rsname, rqty, r_supply_date)
            elif (len(args) == 3) and rsname and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryOrderByNamePriceSupplyDate(sid, cat_name, oid, rsname, rprice, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesBySupplierCategoryOrderByChangedDateQtyPrice(sid, cat_name, oid, r_changed_date, rqty, rprice)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryOrderByChangedDateQtySupplyDate(sid, cat_name, oid, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryOrderByChangedDatePriceSupplyDate(sid, cat_name, oid, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryOrderByQtyPriceSupplyDate(sid, cat_name, oid, rqty, rprice, r_supply_date)
            elif (len(args) == 2) and rsname and r_changed_date:
                resource_list = dao.getResourcesBySupplierCategoryOrderByNameChangedDate(sid, cat_name, oid, rsname, r_changed_date)
            elif (len(args) == 2) and rsname and rqty:
                resource_list = dao.getResourcesBySupplierCategoryOrderByNameQty(sid, cat_name, oid, rsname, rqty)
            elif (len(args) == 2) and rsname and rprice:
                resource_list = dao.getResourcesBySupplierCategoryOrderByNamePrice(sid, cat_name, oid, rsname, rprice)
            elif (len(args) == 2) and rsname and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryOrderByNameSupplyDate(sid, cat_name, oid, rsname, r_supply_date)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesBySupplierCategoryOrderByChangedDateQty(sid, cat_name, oid, r_changed_date, rqty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesBySupplierCategoryOrderByChangedDatePrice(sid, cat_name, oid, r_changed_date, rprice)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryOrderByChangedDateSupplyDate(sid, cat_name, oid, r_changed_date, r_supply_date)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesBySupplierCategoryOrderByQtyPrice(sid, cat_name, oid, rqty, rprice)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryOrderByQtySupplyDate(sid, cat_name, oid, rqty, r_supply_date)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryOrderByPriceSupplyDate(sid, cat_name, oid, rprice, r_supply_date)
            elif (len(args) == 1) and rsname:
                resource_list = dao.getResourcesBySupplierCategoryOrderByName(sid, cat_name, oid, rsname)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesBySupplierCategoryOrderByChangedDate(sid, cat_name, oid, r_changed_date)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesBySupplierCategoryOrderByQty(sid, cat_name, oid, rqty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesBySupplierCategoryOrderByPrice(sid, cat_name, oid, rprice)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryOrderBySupplyDate(sid, cat_name, oid, r_supply_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resource Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def getResourcesByKeywordCategoryOrder(self, kid, cat_name, oid):
        if not KeywordDAO().getKeywordById(kid) and not CategoryDAO().getCategoryByName(cat_name) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Keyword, Category, and Order Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Keyword and Category Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Category and Order Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        elif not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Order Not Found"), 404
        else:
            resource_list = ResourceDAO().getResourcesByKeywordCategoryOrder(kid, cat_name, oid)
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resources Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def searchResourcesByKeywordCategoryOrder(self, kid, cat_name, oid, args):
        if not KeywordDAO().getKeywordById(kid) and not CategoryDAO().getCategoryByName(cat_name) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Keyword, Category, and Order Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Keyword and Category Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Category and Order Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        elif not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Order Not Found"), 404
        else:
            rsname = args.get('rsname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rsname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryOrderByNameChangedDateQtyPriceSupplyDate(kid, cat_name, oid, rsname, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByKeywordCategoryOrderByNameChangedDateQtyPrice(kid, cat_name, oid, rsname, r_changed_date, rqty, rprice)
            elif (len(args) == 4) and rsname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryOrderByNameChangedDateQtySupplyDate(kid, cat_name, oid, rsname, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 4) and rsname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryOrderByNameChangedDatePriceSupplyDate(kid, cat_name, oid, rsname, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 4) and rsname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryOrderByNameQtyPriceSupplyDate(kid, cat_name, oid, rsname, rqty, rprice, r_supply_date)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryOrderByChangedDateQtyPriceSupplyDate(kid, cat_name, oid, r_changed_date, rqty, rprice, r_supply_date)
            elif (len(args) == 3) and rsname and r_changed_date and rqty:
                resource_list = dao.getResourcesByKeywordCategoryOrderByNameChangedDateQty(kid, cat_name, oid, rsname, r_changed_date, rqty)
            elif (len(args) == 3) and rsname and r_changed_date and rprice:
                resource_list = dao.getResourcesByKeywordCategoryOrderByNameChangedDatePrice(kid, cat_name, oid, rsname, r_changed_date, rprice)
            elif (len(args) == 3) and rsname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryOrderByNameChangedDateSupplyDate(kid, cat_name, oid, rsname, r_changed_date, r_supply_date)
            elif (len(args) == 3) and rsname and rqty and rprice:
                resource_list = dao.getResourcesByKeywordCategoryOrderByNameQtyPrice(kid, cat_name, oid, rsname, rqty, rprice)
            elif (len(args) == 3) and rsname and rqty and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryOrderByNameQtySupplyDate(kid, cat_name, oid, rsname, rqty, r_supply_date)
            elif (len(args) == 3) and rsname and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryOrderByNamePriceSupplyDate(kid, cat_name, oid, rsname, rprice, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByKeywordCategoryOrderByChangedDateQtyPrice(kid, cat_name, oid, r_changed_date, rqty, rprice)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryOrderByChangedDateQtySupplyDate(kid, cat_name, oid, r_changed_date, rqty, r_supply_date)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryOrderByChangedDatePriceSupplyDate(kid, cat_name, oid, r_changed_date, rprice, r_supply_date)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryOrderByQtyPriceSupplyDate(kid, cat_name, oid, rqty, rprice, r_supply_date)
            elif (len(args) == 2) and rsname and r_changed_date:
                resource_list = dao.getResourcesByKeywordCategoryOrderByNameChangedDate(kid, cat_name, oid, rsname, r_changed_date)
            elif (len(args) == 2) and rsname and rqty:
                resource_list = dao.getResourcesByKeywordCategoryOrderByNameQty(kid, cat_name, oid, rsname, rqty)
            elif (len(args) == 2) and rsname and rprice:
                resource_list = dao.getResourcesByKeywordCategoryOrderByNamePrice(kid, cat_name, oid, rsname, rprice)
            elif (len(args) == 2) and rsname and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryOrderByNameSupplyDate(kid, cat_name, oid, rsname, r_supply_date)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByKeywordCategoryOrderByChangedDateQty(kid, cat_name, oid, r_changed_date, rqty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByKeywordCategoryOrderByChangedDatePrice(kid, cat_name, oid, r_changed_date, rprice)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryOrderByChangedDateSupplyDate(kid, cat_name, oid, r_changed_date, r_supply_date)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByKeywordCategoryOrderByQtyPrice(kid, cat_name, oid, rqty, rprice)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryOrderByQtySupplyDate(kid, cat_name, oid, rqty, r_supply_date)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryOrderByPriceSupplyDate(kid, cat_name, oid, rprice, r_supply_date)
            elif (len(args) == 1) and rsname:
                resource_list = dao.getResourcesByKeywordCategoryOrderByName(kid, cat_name, oid, rsname)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByKeywordCategoryOrderByChangedDate(kid, cat_name, oid, r_changed_date)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByKeywordCategoryOrderByQty(kid, cat_name, oid, rqty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByKeywordCategoryOrderByPrice(kid, cat_name, oid, rprice)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryOrderBySupplyDate(kid, cat_name, oid, r_supply_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resource Not Found"), 404
            else:
                return jsonify(Resources = result_list)
