from flask import jsonify
suppliers = [
        {
            'sid':1,
            'pname':'supplier1',
            'plname':'supplier_lastname1',
            'city':'Ponce',
            'region':'sur',
            'address':'address1',
            'gps':'gps1',
            'email':'suplier1@email.com',
            'username':'supplier_1',
            'password':'password1'
        },
        {
            'sid': 2,
            'pname': 'supplier2',
            'plname': 'supplier_lastname2',
            'city': 'Mayaguez',
            'region':'oeste',
            'address': 'address2',
            'gps': 'gps2',
            'email': 'suplier2@email.com',
            'username': 'supplier_2',
            'password': 'password2'
        },
        {
            'sid': 3,
            'pname': 'supplier3',
            'plname': 'supplier_lastname3',
            'city': 'Caguas',
            'region':'este',
            'address': 'address3',
            'gps': 'gps3',
            'email': 'suplier3@email.com',
            'username': 'supplier_3',
            'password': 'password3'
        }
    ]
class SupplierHandler:


    def getAllSuppliers(self):
        return jsonify(Suppliers=suppliers)

    def getSupplierById(self, sid):
        result_list = []
        for supplier in suppliers:
            if supplier['sid'] == sid:
                result_list.append(supplier)
        if not result_list:
            return jsonify(Error="Supplier Not Found"), 404
        return jsonify(Supplier=result_list)

    def searchSuppliers(self, args):

        firstName = args.get("pname")
        lastName = args.get('plname')
        cname = args.get('cname')
        email = args.get('email')
        username = args.get('username')
        rname = args.get('rname')

        if (len(args) == 6) and firstName and lastName and cname and email and username and rname:
            result_list = []
            for supplier in suppliers:
                if supplier['pname'] == firstName and supplier['plname'] == lastName and supplier['city'] == cname\
                        and supplier['email'] == email and supplier['username'] == username\
                        and supplier['region'] == rname:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # ------------------------------------------------------------------------------

        # Without rname
        elif (len(args) == 5) and firstName and lastName and cname and email and username:
            result_list = []
            for supplier in suppliers:
                if supplier['pname'] == firstName and supplier['plname'] == lastName and supplier['city'] == cname \
                        and supplier['email'] == email and supplier['username'] == username:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # Without username
        elif (len(args) == 5) and firstName and lastName and cname and email and rname:
            result_list = []
            for supplier in suppliers:
                if supplier['pname'] == firstName and supplier['plname'] == lastName and supplier['city'] == cname \
                        and supplier['email'] == email and supplier['region'] == rname:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # Without email
        elif (len(args) == 5) and firstName and lastName and cname and username and rname:
            result_list = []
            for supplier in suppliers:
                if supplier['pname'] == firstName and supplier['plname'] == lastName and supplier['city'] == cname \
                        and supplier['username'] == username and supplier['region'] == rname:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # Without cname
        elif (len(args) == 5) and firstName and lastName and cname and email and rname:
            result_list = []
            for supplier in suppliers:
                if supplier['pname'] == firstName and supplier['plname'] == lastName and supplier['email'] == email \
                        and supplier['username'] == username and supplier['region'] == rname:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # Without lastname
        elif (len(args) == 5) and firstName and cname and email and username and rname:
            result_list = []
            for supplier in suppliers:
                if supplier['pname'] == firstName and supplier['city'] == cname \
                        and supplier['email'] == email and supplier['username'] == username \
                        and supplier['region'] == rname:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # Without firstname
        elif (len(args) == 5) and lastName and cname and email and username and rname:
            result_list = []
            for supplier in suppliers:
                if supplier['plname'] == lastName and supplier['city'] == cname \
                        and supplier['email'] == email and supplier['username'] == username \
                        and supplier['region'] == rname:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)
        # ------------------------------------------------------------------------------

        # Without rname and username
        elif (len(args) == 4) and firstName and lastName and cname and email:
            result_list = []
            for supplier in suppliers:
                if supplier['pname'] == firstName and supplier['plname'] == lastName and supplier['city'] == cname \
                        and supplier['email'] == email:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # Without rname and email
        elif (len(args) == 4) and firstName and lastName and cname and username:
            result_list = []
            for supplier in suppliers:
                if supplier['pname'] == firstName and supplier['plname'] == lastName and supplier['city'] == cname \
                        and supplier['username'] == username:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # Without rname and cname
        elif (len(args) == 4) and firstName and lastName and email and username:
            result_list = []
            for supplier in suppliers:
                if supplier['pname'] == firstName and supplier['plname'] == lastName \
                        and supplier['email'] == email and supplier['username'] == username:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # Without rname and lastname
        elif (len(args) == 4) and firstName and cname and email and username:
            result_list = []
            for supplier in suppliers:
                if supplier['pname'] == firstName and supplier['city'] == cname \
                        and supplier['email'] == email and supplier['username'] == username:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # Without rname and firstname
        elif (len(args) == 4) and lastName and cname and email and username:
            result_list = []
            for supplier in suppliers:
                if supplier['plname'] == lastName and supplier['city'] == cname \
                        and supplier['email'] == email and supplier['username'] == username:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # Without username and email
        elif (len(args) == 4) and firstName and lastName and cname and rname:
            result_list = []
            for supplier in suppliers:
                if supplier['pname'] == firstName and supplier['plname'] == lastName and supplier['city'] == cname \
                        and supplier['region'] == rname:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # Without username and cname
        elif (len(args) == 4) and firstName and lastName and email and rname:
            result_list = []
            for supplier in suppliers:
                if supplier['pname'] == firstName and supplier['plname'] == lastName \
                        and supplier['email'] == email and supplier['region'] == rname:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # firstname, lastname, cname, email, username, rname

        # Without username and lastname
        elif (len(args) == 4) and firstName and cname and email and rname:
            result_list = []
            for supplier in suppliers:
                if supplier['pname'] == firstName and supplier['city'] == cname \
                        and supplier['email'] == email and supplier['region'] == rname:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # Without username and firstname
        elif (len(args) == 4) and lastName and cname and email and rname:
            result_list = []
            for supplier in suppliers:
                if supplier['plname'] == lastName and supplier['city'] == cname \
                        and supplier['email'] == email and supplier['region'] == rname:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # Without email and cname
        elif (len(args) == 4) and firstName and lastName and username and rname:
            result_list = []
            for supplier in suppliers:
                if supplier['pname'] == firstName and supplier['plname'] == lastName \
                        and supplier['username'] == username and supplier['region'] == rname:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # Without email and lastname
        elif (len(args) == 4) and firstName and cname and username and rname:
            result_list = []
            for supplier in suppliers:
                if supplier['pname'] == firstName and supplier['city'] == cname \
                        and supplier['username'] == username and supplier['region'] == rname:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # Without email and firstname
        elif (len(args) == 4) and lastName and cname and username and rname:
            result_list = []
            for supplier in suppliers:
                if supplier['plname'] == lastName and supplier['city'] == cname \
                        and supplier['username'] == username and supplier['region'] == rname:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # Without cname and lastname
        elif (len(args) == 4) and firstName and email and username and rname:
            result_list = []
            for supplier in suppliers:
                if supplier['pname'] == firstName \
                        and supplier['email'] == email and supplier['username'] == username \
                        and supplier['region'] == rname:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # Without cname and firstName
        elif (len(args) == 4) and lastName and email and username and rname:
            result_list = []
            for supplier in suppliers:
                if supplier['plname'] == lastName \
                        and supplier['email'] == email and supplier['username'] == username \
                        and supplier['region'] == rname:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # Without lastname and firstName
        elif (len(args) == 4) and cname and email and username and rname:
            result_list = []
            for supplier in suppliers:
                if supplier['city'] == cname \
                        and supplier['email'] == email and supplier['username'] == username \
                        and supplier['region'] == rname:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # ------------------------------------------------------------------------------

        # Without email, username and rname
        elif (len(args) == 3) and firstName and lastName and cname:
            result_list = []
            for supplier in suppliers:
                if supplier['pname'] == firstName and supplier['plname'] == lastName and supplier['city'] == cname:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # Without cname, username and rname
        elif (len(args) == 3) and firstName and lastName and email:
            result_list = []
            for supplier in suppliers:
                if supplier['pname'] == firstName and supplier['plname'] == lastName and supplier['email'] == email:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # Without lastname, username and rname
        elif (len(args) == 3) and firstName and cname and email:
            result_list = []
            for supplier in suppliers:
                if supplier['pname'] == firstName and supplier['city'] == cname and supplier['email'] == email:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # Without firstname, username and rname
        elif (len(args) == 3) and lastName and cname and email:
            result_list = []
            for supplier in suppliers:
                if supplier['plname'] == lastName and supplier['city'] == cname and supplier['email'] == email:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # Without cname, email and rname
        elif (len(args) == 3) and firstName and lastName and username:
            result_list = []
            for supplier in suppliers:
                if supplier['pname'] == firstName and supplier['plname'] == lastName\
                        and supplier['username'] == username:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # Without lastname, email and rname
        elif (len(args) == 3) and firstName and cname and username:
            result_list = []
            for supplier in suppliers:
                if supplier['pname'] == firstName and supplier['city'] == cname and supplier['username'] == username:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # Without firstname, email and rname
        elif (len(args) == 3) and lastName and cname and username:
            result_list = []
            for supplier in suppliers:
                if supplier['plname'] == lastName and supplier['city'] == cname and supplier['username'] == username:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # Without lastname, cname and rname
        elif (len(args) == 3) and firstName and email and username:
            result_list = []
            for supplier in suppliers:
                if supplier['pname'] == firstName and supplier['email'] == email and supplier['username'] == username:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # Without firstname, cname and rname
        elif (len(args) == 3) and lastName and email and username:
            result_list = []
            for supplier in suppliers:
                if supplier['plname'] == lastName and supplier['email'] == email and supplier['username'] == username:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # Without firstname, lastname and rname
        elif (len(args) == 3) and cname and email and username:
            result_list = []
            for supplier in suppliers:
                if supplier['city'] == cname and supplier['username'] == username and supplier['email'] == email:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # Without cname, email and username
        elif (len(args) == 3) and firstName and lastName and rname:
            result_list = []
            for supplier in suppliers:
                if supplier['pname'] == firstName and supplier['plname'] == lastName and supplier['region'] == rname:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # Without lastname, email and username
        elif (len(args) == 3) and firstName and cname and rname:
            result_list = []
            for supplier in suppliers:
                if supplier['pname'] == firstName and supplier['city'] == cname and supplier['region'] == rname:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # Without firstname, email and username
        elif (len(args) == 3) and lastName and cname and rname:
            result_list = []
            for supplier in suppliers:
                if supplier['plname'] == lastName and supplier['city'] == cname and supplier['region'] == rname:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # Without lastname, cname and username
        elif (len(args) == 3) and firstName and email and rname:
            result_list = []
            for supplier in suppliers:
                if supplier['pname'] == firstName and supplier['email'] == email and supplier['region'] == rname:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # Without firstname, cname and username
        elif (len(args) == 3) and lastName and email and rname:
            result_list = []
            for supplier in suppliers:
                if supplier['plname'] == lastName and supplier['email'] == email and supplier['region'] == rname:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # Without lastname, cname and email
        elif (len(args) == 3) and firstName and username and rname:
            result_list = []
            for supplier in suppliers:
                if supplier['pname'] == firstName and supplier['username'] == username and supplier['region'] == rname:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # Without firstname, cname and email
        elif (len(args) == 3) and lastName and username and rname:
            result_list = []
            for supplier in suppliers:
                if supplier['plname'] == lastName and supplier['username'] == username and supplier['region'] == rname:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # Without firstname, lastname and cname
        elif (len(args) == 3) and email and username and rname:
            result_list = []
            for supplier in suppliers:
                if supplier['email'] == email and supplier['username'] == username and supplier['region'] == rname:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # Without firstname, lastname and email
        elif (len(args) == 3) and cname and username and rname:
            result_list = []
            for supplier in suppliers:
                if supplier['city'] == cname and supplier['username'] == username and supplier['region'] == rname:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # Without firstname, lastname and username
        elif (len(args) == 3) and cname and email and rname:
            result_list = []
            for supplier in suppliers:
                if supplier['city'] == cname and supplier['email'] == email and supplier['region'] == rname:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # ------------------------------------------------------------------------------

        elif (len(args) == 2) and username and rname:
            result_list = []
            for supplier in suppliers:
                if supplier['username'] == username and supplier['region'] == rname:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        elif (len(args) == 2) and email and rname:
            result_list = []
            for supplier in suppliers:
                if supplier['email'] == email and supplier['region'] == rname:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        elif (len(args) == 2) and cname and rname:
            result_list = []
            for supplier in suppliers:
                if supplier['city'] == cname and supplier['region'] == rname:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        elif (len(args) == 2) and lastName and rname:
            result_list = []
            for supplier in suppliers:
                if supplier['plname'] == lastName and supplier['region'] == rname:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        elif (len(args) == 2) and firstName and rname:
            result_list = []
            for supplier in suppliers:
                if supplier['pname'] == firstName and supplier['region'] == rname:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        elif (len(args) == 2) and username and rname:
            result_list = []
            for supplier in suppliers:
                if supplier['username'] == username and supplier['region'] == rname:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        elif (len(args) == 2) and email and username:
            result_list = []
            for supplier in suppliers:
                if supplier['username'] == username and supplier['email'] == email:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        elif (len(args) == 2) and cname and username:
            result_list = []
            for supplier in suppliers:
                if supplier['username'] == username and supplier['city'] == cname:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        elif (len(args) == 2) and lastName and username:
            result_list = []
            for supplier in suppliers:
                if supplier['username'] == username and supplier['plname'] == lastName:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        elif (len(args) == 2) and firstName and username:
            result_list = []
            for supplier in suppliers:
                if supplier['username'] == username and supplier['pname'] == firstName:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        elif (len(args) == 2) and cname and email:
            result_list = []
            for supplier in suppliers:
                if supplier['city'] == cname and supplier['email'] == email:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        elif (len(args) == 2) and lastName and email:
            result_list = []
            for supplier in suppliers:
                if supplier['plname'] == lastName and supplier['email'] == email:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        elif (len(args) == 2) and firstName and email:
            result_list = []
            for supplier in suppliers:
                if supplier['pname'] == firstName and supplier['email'] == email:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        elif (len(args) == 2) and lastName and cname:
            result_list = []
            for supplier in suppliers:
                if supplier['city'] == cname and supplier['plname'] == lastName:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        elif (len(args) == 2) and firstName and cname:
            result_list = []
            for supplier in suppliers:
                if supplier['city'] == cname and supplier['pname'] == firstName:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        elif (len(args) == 2) and firstName and lastName:
            result_list = []
            for supplier in suppliers:
                if supplier['pname'] == firstName and supplier['plname'] == lastName:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # ------------------------------------------------------------------------------

        # firstname
        elif (len(args) == 1) and firstName:
            result_list = []
            for supplier in suppliers:
                if supplier['pname'] == firstName:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # lastname
        elif (len(args) == 1) and lastName:
            result_list = []
            for supplier in suppliers:
                if supplier['plname'] == lastName:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # cname
        elif (len(args) == 1) and cname:
            result_list = []
            for supplier in suppliers:
                if supplier['city'] == cname:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # email
        elif (len(args) == 1) and email:
            result_list = []
            for supplier in suppliers:
                if supplier['email'] == email:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # username
        elif (len(args) == 1) and username:
            result_list = []
            for supplier in suppliers:
                if supplier['username'] == username:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)

        # rname
        elif (len(args) == 1) and rname:
            result_list = []
            for supplier in suppliers:
                if supplier['region'] == rname:
                    result_list.append(supplier)
            if not result_list:
                return jsonify(Error="Suppliers Not Found"), 404
            return jsonify(Suppliers=result_list)
        # ------------------------------------------------------------------------------

        else:
            return 'No suppliers found', 404