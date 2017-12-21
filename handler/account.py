from flask import jsonify

accounts = [
    {
        'sid': 1,
        'pname': 'supplier1',
        'plname': 'supplier_lastname1',
        'city': 'Ponce',
        'region': 'sur',
        'address': 'address1',
        'gps': 'gps1',
        'email': 'suplier1@email.com',
        'username': 'supplier_1',
        'password': 'password1'
    },
    {
        'sid': 2,
        'pname': 'supplier2',
        'plname': 'supplier_lastname2',
        'city': 'Mayaguez',
        'region': 'oeste',
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
        'region': 'este',
        'address': 'address3',
        'gps': 'gps3',
        'email': 'suplier3@email.com',
        'username': 'supplier_3',
        'password': 'password3'
    },
{
        'sid': 4,
        'pname': 'needer1',
        'plname': 'needer_lastname1',
        'city': 'Ponce',
        'region': 'sur',
        'address': 'address1',
        'gps': 'gps1',
        'email': 'suplier1@email.com',
        'username': 'needer_1',
        'password': 'password1'
    },
    {
        'sid': 5,
        'pname': 'needer2',
        'plname': 'needer_lastname2',
        'city': 'Mayaguez',
        'region': 'oeste',
        'address': 'address2',
        'gps': 'gps2',
        'email': 'suplier2@email.com',
        'username': 'needer_2',
        'password': 'password2'
    },
    {
        'sid': 6,
        'pname': 'needer3',
        'plname': 'needer_lastname3',
        'city': 'Caguas',
        'region': 'este',
        'address': 'address3',
        'gps': 'gps3',
        'email': 'suplier3@email.com',
        'username': 'needer_3',
        'password': 'password3'
    },
{
        'sid': 7,
        'pname': 'administrator1',
        'plname': 'administrator_lastname1',
        'city': 'Ponce',
        'region': 'sur',
        'address': 'address1',
        'gps': 'gps1',
        'email': 'suplier1@email.com',
        'username': 'administrator_1',
        'password': 'password1'
    },
    {
        'sid': 8,
        'pname': 'administrator2',
        'plname': 'administrator_lastname2',
        'city': 'Mayaguez',
        'region': 'oeste',
        'address': 'address2',
        'gps': 'gps2',
        'email': 'suplier2@email.com',
        'username': 'administrator_2',
        'password': 'password2'
    },
    {
        'sid': 9,
        'pname': 'administrator3',
        'plname': 'administrator_lastname3',
        'city': 'Caguas',
        'region': 'este',
        'address': 'address3',
        'gps': 'gps3',
        'email': 'suplier3@email.com',
        'username': 'administrator_3',
        'password': 'password3'
    }
]


class AccountHandler:
    def getAllAccounts(self):
        return jsonify(Accounts=accounts)

    def getAccountByUniqueId(self, sid):
        result_list = []
        for account in accounts:
            if int(account['sid']) == sid:
                result_list.append(account)
        if not result_list:
            return jsonify(Error="Account Not Found"), 404
        return jsonify(Account=result_list)

    def searchAccounts(self, args):

        firstName = args.get("pname")
        lastName = args.get('plname')
        cname = args.get('cname')
        email = args.get('email')
        username = args.get('username')
        rname = args.get('rname')

        if (len(args) == 6) and firstName and lastName and cname and email and username and rname:
            result_list = []
            for account in accounts:
                if account['pname'] == firstName and account['plname'] == lastName and account['city'] == cname \
                        and account['email'] == email and account['username'] == username \
                        and account['region'] == rname:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # ------------------------------------------------------------------------------

        # Without rname
        elif (len(args) == 5) and firstName and lastName and cname and email and username:
            result_list = []
            for account in accounts:
                if account['pname'] == firstName and account['plname'] == lastName and account['city'] == cname \
                        and account['email'] == email and account['username'] == username:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # Without username
        elif (len(args) == 5) and firstName and lastName and cname and email and rname:
            result_list = []
            for account in accounts:
                if account['pname'] == firstName and account['plname'] == lastName and account['city'] == cname \
                        and account['email'] == email and account['region'] == rname:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # Without email
        elif (len(args) == 5) and firstName and lastName and cname and username and rname:
            result_list = []
            for account in accounts:
                if account['pname'] == firstName and account['plname'] == lastName and account['city'] == cname \
                        and account['username'] == username and account['region'] == rname:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # Without cname
        elif (len(args) == 5) and firstName and lastName and cname and email and rname:
            result_list = []
            for account in accounts:
                if account['pname'] == firstName and account['plname'] == lastName and account['email'] == email \
                        and account['username'] == username and account['region'] == rname:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # Without lastname
        elif (len(args) == 5) and firstName and cname and email and username and rname:
            result_list = []
            for account in accounts:
                if account['pname'] == firstName and account['city'] == cname \
                        and account['email'] == email and account['username'] == username \
                        and account['region'] == rname:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # Without firstname
        elif (len(args) == 5) and lastName and cname and email and username and rname:
            result_list = []
            for account in accounts:
                if account['plname'] == lastName and account['city'] == cname \
                        and account['email'] == email and account['username'] == username \
                        and account['region'] == rname:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)
        # ------------------------------------------------------------------------------

        # Without rname and username
        elif (len(args) == 4) and firstName and lastName and cname and email:
            result_list = []
            for account in accounts:
                if account['pname'] == firstName and account['plname'] == lastName and account['city'] == cname \
                        and account['email'] == email:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # Without rname and email
        elif (len(args) == 4) and firstName and lastName and cname and username:
            result_list = []
            for account in accounts:
                if account['pname'] == firstName and account['plname'] == lastName and account['city'] == cname \
                        and account['username'] == username:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # Without rname and cname
        elif (len(args) == 4) and firstName and lastName and email and username:
            result_list = []
            for account in accounts:
                if account['pname'] == firstName and account['plname'] == lastName \
                        and account['email'] == email and account['username'] == username:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # Without rname and lastname
        elif (len(args) == 4) and firstName and cname and email and username:
            result_list = []
            for account in accounts:
                if account['pname'] == firstName and account['city'] == cname \
                        and account['email'] == email and account['username'] == username:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # Without rname and firstname
        elif (len(args) == 4) and lastName and cname and email and username:
            result_list = []
            for account in accounts:
                if account['plname'] == lastName and account['city'] == cname \
                        and account['email'] == email and account['username'] == username:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # Without username and email
        elif (len(args) == 4) and firstName and lastName and cname and rname:
            result_list = []
            for account in accounts:
                if account['pname'] == firstName and account['plname'] == lastName and account['city'] == cname \
                        and account['region'] == rname:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # Without username and cname
        elif (len(args) == 4) and firstName and lastName and email and rname:
            result_list = []
            for account in accounts:
                if account['pname'] == firstName and account['plname'] == lastName \
                        and account['email'] == email and account['region'] == rname:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # firstname, lastname, cname, email, username, rname

        # Without username and lastname
        elif (len(args) == 4) and firstName and cname and email and rname:
            result_list = []
            for account in accounts:
                if account['pname'] == firstName and account['city'] == cname \
                        and account['email'] == email and account['region'] == rname:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # Without username and firstname
        elif (len(args) == 4) and lastName and cname and email and rname:
            result_list = []
            for account in accounts:
                if account['plname'] == lastName and account['city'] == cname \
                        and account['email'] == email and account['region'] == rname:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # Without email and cname
        elif (len(args) == 4) and firstName and lastName and username and rname:
            result_list = []
            for account in accounts:
                if account['pname'] == firstName and account['plname'] == lastName \
                        and account['username'] == username and account['region'] == rname:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # Without email and lastname
        elif (len(args) == 4) and firstName and cname and username and rname:
            result_list = []
            for account in accounts:
                if account['pname'] == firstName and account['city'] == cname \
                        and account['username'] == username and account['region'] == rname:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # Without email and firstname
        elif (len(args) == 4) and lastName and cname and username and rname:
            result_list = []
            for account in accounts:
                if account['plname'] == lastName and account['city'] == cname \
                        and account['username'] == username and account['region'] == rname:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # Without cname and lastname
        elif (len(args) == 4) and firstName and email and username and rname:
            result_list = []
            for account in accounts:
                if account['pname'] == firstName \
                        and account['email'] == email and account['username'] == username \
                        and account['region'] == rname:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # Without cname and firstName
        elif (len(args) == 4) and lastName and email and username and rname:
            result_list = []
            for account in accounts:
                if account['plname'] == lastName \
                        and account['email'] == email and account['username'] == username \
                        and account['region'] == rname:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # Without lastname and firstName
        elif (len(args) == 4) and cname and email and username and rname:
            result_list = []
            for account in accounts:
                if account['city'] == cname \
                        and account['email'] == email and account['username'] == username \
                        and account['region'] == rname:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # ------------------------------------------------------------------------------

        # Without email, username and rname
        elif (len(args) == 3) and firstName and lastName and cname:
            result_list = []
            for account in accounts:
                if account['pname'] == firstName and account['plname'] == lastName and account['city'] == cname:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # Without cname, username and rname
        elif (len(args) == 3) and firstName and lastName and email:
            result_list = []
            for account in accounts:
                if account['pname'] == firstName and account['plname'] == lastName and account['email'] == email:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # Without lastname, username and rname
        elif (len(args) == 3) and firstName and cname and email:
            result_list = []
            for account in accounts:
                if account['pname'] == firstName and account['city'] == cname and account['email'] == email:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # Without firstname, username and rname
        elif (len(args) == 3) and lastName and cname and email:
            result_list = []
            for account in accounts:
                if account['plname'] == lastName and account['city'] == cname and account['email'] == email:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # Without cname, email and rname
        elif (len(args) == 3) and firstName and lastName and username:
            result_list = []
            for account in accounts:
                if account['pname'] == firstName and account['plname'] == lastName \
                        and account['username'] == username:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # Without lastname, email and rname
        elif (len(args) == 3) and firstName and cname and username:
            result_list = []
            for account in accounts:
                if account['pname'] == firstName and account['city'] == cname and account['username'] == username:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # Without firstname, email and rname
        elif (len(args) == 3) and lastName and cname and username:
            result_list = []
            for account in accounts:
                if account['plname'] == lastName and account['city'] == cname and account['username'] == username:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # Without lastname, cname and rname
        elif (len(args) == 3) and firstName and email and username:
            result_list = []
            for account in accounts:
                if account['pname'] == firstName and account['email'] == email and account['username'] == username:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # Without firstname, cname and rname
        elif (len(args) == 3) and lastName and email and username:
            result_list = []
            for account in accounts:
                if account['plname'] == lastName and account['email'] == email and account['username'] == username:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # Without firstname, lastname and rname
        elif (len(args) == 3) and cname and email and username:
            result_list = []
            for account in accounts:
                if account['city'] == cname and account['username'] == username and account['email'] == email:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # Without cname, email and username
        elif (len(args) == 3) and firstName and lastName and rname:
            result_list = []
            for account in accounts:
                if account['pname'] == firstName and account['plname'] == lastName and account['region'] == rname:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # Without lastname, email and username
        elif (len(args) == 3) and firstName and cname and rname:
            result_list = []
            for account in accounts:
                if account['pname'] == firstName and account['city'] == cname and account['region'] == rname:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # Without firstname, email and username
        elif (len(args) == 3) and lastName and cname and rname:
            result_list = []
            for account in accounts:
                if account['plname'] == lastName and account['city'] == cname and account['region'] == rname:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # Without lastname, cname and username
        elif (len(args) == 3) and firstName and email and rname:
            result_list = []
            for account in accounts:
                if account['pname'] == firstName and account['email'] == email and account['region'] == rname:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # Without firstname, cname and username
        elif (len(args) == 3) and lastName and email and rname:
            result_list = []
            for account in accounts:
                if account['plname'] == lastName and account['email'] == email and account['region'] == rname:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # Without lastname, cname and email
        elif (len(args) == 3) and firstName and username and rname:
            result_list = []
            for account in accounts:
                if account['pname'] == firstName and account['username'] == username and account['region'] == rname:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # Without firstname, cname and email
        elif (len(args) == 3) and lastName and username and rname:
            result_list = []
            for account in accounts:
                if account['plname'] == lastName and account['username'] == username and account['region'] == rname:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # Without firstname, lastname and cname
        elif (len(args) == 3) and email and username and rname:
            result_list = []
            for account in accounts:
                if account['email'] == email and account['username'] == username and account['region'] == rname:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # Without firstname, lastname and email
        elif (len(args) == 3) and cname and username and rname:
            result_list = []
            for account in accounts:
                if account['city'] == cname and account['username'] == username and account['region'] == rname:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # Without firstname, lastname and username
        elif (len(args) == 3) and cname and email and rname:
            result_list = []
            for account in accounts:
                if account['city'] == cname and account['email'] == email and account['region'] == rname:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # ------------------------------------------------------------------------------

        elif (len(args) == 2) and username and rname:
            result_list = []
            for account in accounts:
                if account['username'] == username and account['region'] == rname:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        elif (len(args) == 2) and email and rname:
            result_list = []
            for account in accounts:
                if account['email'] == email and account['region'] == rname:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        elif (len(args) == 2) and cname and rname:
            result_list = []
            for account in accounts:
                if account['city'] == cname and account['region'] == rname:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        elif (len(args) == 2) and lastName and rname:
            result_list = []
            for account in accounts:
                if account['plname'] == lastName and account['region'] == rname:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        elif (len(args) == 2) and firstName and rname:
            result_list = []
            for account in accounts:
                if account['pname'] == firstName and account['region'] == rname:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        elif (len(args) == 2) and username and rname:
            result_list = []
            for account in accounts:
                if account['username'] == username and account['region'] == rname:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        elif (len(args) == 2) and email and username:
            result_list = []
            for account in accounts:
                if account['username'] == username and account['email'] == email:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        elif (len(args) == 2) and cname and username:
            result_list = []
            for account in accounts:
                if account['username'] == username and account['city'] == cname:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        elif (len(args) == 2) and lastName and username:
            result_list = []
            for account in accounts:
                if account['username'] == username and account['plname'] == lastName:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        elif (len(args) == 2) and firstName and username:
            result_list = []
            for account in accounts:
                if account['username'] == username and account['pname'] == firstName:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        elif (len(args) == 2) and cname and email:
            result_list = []
            for account in accounts:
                if account['city'] == cname and account['email'] == email:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        elif (len(args) == 2) and lastName and email:
            result_list = []
            for account in accounts:
                if account['plname'] == lastName and account['email'] == email:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        elif (len(args) == 2) and firstName and email:
            result_list = []
            for account in accounts:
                if account['pname'] == firstName and account['email'] == email:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        elif (len(args) == 2) and lastName and cname:
            result_list = []
            for account in accounts:
                if account['city'] == cname and account['plname'] == lastName:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        elif (len(args) == 2) and firstName and cname:
            result_list = []
            for account in accounts:
                if account['city'] == cname and account['pname'] == firstName:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        elif (len(args) == 2) and firstName and lastName:
            result_list = []
            for account in accounts:
                if account['pname'] == firstName and account['plname'] == lastName:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # ------------------------------------------------------------------------------

        # firstname
        elif (len(args) == 1) and firstName:
            result_list = []
            for account in accounts:
                if account['pname'] == firstName:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # lastname
        elif (len(args) == 1) and lastName:
            result_list = []
            for account in accounts:
                if account['plname'] == lastName:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # cname
        elif (len(args) == 1) and cname:
            result_list = []
            for account in accounts:
                if account['city'] == cname:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # email
        elif (len(args) == 1) and email:
            result_list = []
            for account in accounts:
                if account['email'] == email:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # username
        elif (len(args) == 1) and username:
            result_list = []
            for account in accounts:
                if account['username'] == username:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)

        # rname
        elif (len(args) == 1) and rname:
            result_list = []
            for account in accounts:
                if account['region'] == rname:
                    result_list.append(account)
            if not result_list:
                return jsonify(Error="Accounts Not Found"), 404
            return jsonify(Accounts=result_list)
        # ------------------------------------------------------------------------------

        else:
            return 'No accounts found', 404