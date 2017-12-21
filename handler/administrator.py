from flask import jsonify

administrators = [
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


class AdministratorHandler:
    def getAllAdministrators(self):
        return jsonify(Administrators=administrators)

    def getAdministratorById(self, sid):
        result_list = []
        for administrator in administrators:
            if administrator['sid'] == sid:
                result_list.append(administrator)
        if not result_list:
            return jsonify(Error="Administrator Not Found"), 404
        return jsonify(Administrator=result_list)

    def searchAdministrators(self, args):

        firstName = args.get("pname")
        lastName = args.get('plname')
        cname = args.get('cname')
        email = args.get('email')
        username = args.get('username')
        rname = args.get('rname')

        if (len(args) == 6) and firstName and lastName and cname and email and username and rname:
            result_list = []
            for administrator in administrators:
                if administrator['pname'] == firstName and administrator['plname'] == lastName and administrator['city'] == cname \
                        and administrator['email'] == email and administrator['username'] == username \
                        and administrator['region'] == rname:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # ------------------------------------------------------------------------------

        # Without rname
        elif (len(args) == 5) and firstName and lastName and cname and email and username:
            result_list = []
            for administrator in administrators:
                if administrator['pname'] == firstName and administrator['plname'] == lastName and administrator['city'] == cname \
                        and administrator['email'] == email and administrator['username'] == username:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # Without username
        elif (len(args) == 5) and firstName and lastName and cname and email and rname:
            result_list = []
            for administrator in administrators:
                if administrator['pname'] == firstName and administrator['plname'] == lastName and administrator['city'] == cname \
                        and administrator['email'] == email and administrator['region'] == rname:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # Without email
        elif (len(args) == 5) and firstName and lastName and cname and username and rname:
            result_list = []
            for administrator in administrators:
                if administrator['pname'] == firstName and administrator['plname'] == lastName and administrator['city'] == cname \
                        and administrator['username'] == username and administrator['region'] == rname:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # Without cname
        elif (len(args) == 5) and firstName and lastName and cname and email and rname:
            result_list = []
            for administrator in administrators:
                if administrator['pname'] == firstName and administrator['plname'] == lastName and administrator['email'] == email \
                        and administrator['username'] == username and administrator['region'] == rname:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # Without lastname
        elif (len(args) == 5) and firstName and cname and email and username and rname:
            result_list = []
            for administrator in administrators:
                if administrator['pname'] == firstName and administrator['city'] == cname \
                        and administrator['email'] == email and administrator['username'] == username \
                        and administrator['region'] == rname:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # Without firstname
        elif (len(args) == 5) and lastName and cname and email and username and rname:
            result_list = []
            for administrator in administrators:
                if administrator['plname'] == lastName and administrator['city'] == cname \
                        and administrator['email'] == email and administrator['username'] == username \
                        and administrator['region'] == rname:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)
        # ------------------------------------------------------------------------------

        # Without rname and username
        elif (len(args) == 4) and firstName and lastName and cname and email:
            result_list = []
            for administrator in administrators:
                if administrator['pname'] == firstName and administrator['plname'] == lastName and administrator['city'] == cname \
                        and administrator['email'] == email:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # Without rname and email
        elif (len(args) == 4) and firstName and lastName and cname and username:
            result_list = []
            for administrator in administrators:
                if administrator['pname'] == firstName and administrator['plname'] == lastName and administrator['city'] == cname \
                        and administrator['username'] == username:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # Without rname and cname
        elif (len(args) == 4) and firstName and lastName and email and username:
            result_list = []
            for administrator in administrators:
                if administrator['pname'] == firstName and administrator['plname'] == lastName \
                        and administrator['email'] == email and administrator['username'] == username:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # Without rname and lastname
        elif (len(args) == 4) and firstName and cname and email and username:
            result_list = []
            for administrator in administrators:
                if administrator['pname'] == firstName and administrator['city'] == cname \
                        and administrator['email'] == email and administrator['username'] == username:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # Without rname and firstname
        elif (len(args) == 4) and lastName and cname and email and username:
            result_list = []
            for administrator in administrators:
                if administrator['plname'] == lastName and administrator['city'] == cname \
                        and administrator['email'] == email and administrator['username'] == username:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # Without username and email
        elif (len(args) == 4) and firstName and lastName and cname and rname:
            result_list = []
            for administrator in administrators:
                if administrator['pname'] == firstName and administrator['plname'] == lastName and administrator['city'] == cname \
                        and administrator['region'] == rname:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # Without username and cname
        elif (len(args) == 4) and firstName and lastName and email and rname:
            result_list = []
            for administrator in administrators:
                if administrator['pname'] == firstName and administrator['plname'] == lastName \
                        and administrator['email'] == email and administrator['region'] == rname:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # firstname, lastname, cname, email, username, rname

        # Without username and lastname
        elif (len(args) == 4) and firstName and cname and email and rname:
            result_list = []
            for administrator in administrators:
                if administrator['pname'] == firstName and administrator['city'] == cname \
                        and administrator['email'] == email and administrator['region'] == rname:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # Without username and firstname
        elif (len(args) == 4) and lastName and cname and email and rname:
            result_list = []
            for administrator in administrators:
                if administrator['plname'] == lastName and administrator['city'] == cname \
                        and administrator['email'] == email and administrator['region'] == rname:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # Without email and cname
        elif (len(args) == 4) and firstName and lastName and username and rname:
            result_list = []
            for administrator in administrators:
                if administrator['pname'] == firstName and administrator['plname'] == lastName \
                        and administrator['username'] == username and administrator['region'] == rname:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # Without email and lastname
        elif (len(args) == 4) and firstName and cname and username and rname:
            result_list = []
            for administrator in administrators:
                if administrator['pname'] == firstName and administrator['city'] == cname \
                        and administrator['username'] == username and administrator['region'] == rname:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # Without email and firstname
        elif (len(args) == 4) and lastName and cname and username and rname:
            result_list = []
            for administrator in administrators:
                if administrator['plname'] == lastName and administrator['city'] == cname \
                        and administrator['username'] == username and administrator['region'] == rname:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # Without cname and lastname
        elif (len(args) == 4) and firstName and email and username and rname:
            result_list = []
            for administrator in administrators:
                if administrator['pname'] == firstName \
                        and administrator['email'] == email and administrator['username'] == username \
                        and administrator['region'] == rname:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # Without cname and firstName
        elif (len(args) == 4) and lastName and email and username and rname:
            result_list = []
            for administrator in administrators:
                if administrator['plname'] == lastName \
                        and administrator['email'] == email and administrator['username'] == username \
                        and administrator['region'] == rname:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # Without lastname and firstName
        elif (len(args) == 4) and cname and email and username and rname:
            result_list = []
            for administrator in administrators:
                if administrator['city'] == cname \
                        and administrator['email'] == email and administrator['username'] == username \
                        and administrator['region'] == rname:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # ------------------------------------------------------------------------------

        # Without email, username and rname
        elif (len(args) == 3) and firstName and lastName and cname:
            result_list = []
            for administrator in administrators:
                if administrator['pname'] == firstName and administrator['plname'] == lastName and administrator['city'] == cname:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # Without cname, username and rname
        elif (len(args) == 3) and firstName and lastName and email:
            result_list = []
            for administrator in administrators:
                if administrator['pname'] == firstName and administrator['plname'] == lastName and administrator['email'] == email:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # Without lastname, username and rname
        elif (len(args) == 3) and firstName and cname and email:
            result_list = []
            for administrator in administrators:
                if administrator['pname'] == firstName and administrator['city'] == cname and administrator['email'] == email:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # Without firstname, username and rname
        elif (len(args) == 3) and lastName and cname and email:
            result_list = []
            for administrator in administrators:
                if administrator['plname'] == lastName and administrator['city'] == cname and administrator['email'] == email:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # Without cname, email and rname
        elif (len(args) == 3) and firstName and lastName and username:
            result_list = []
            for administrator in administrators:
                if administrator['pname'] == firstName and administrator['plname'] == lastName \
                        and administrator['username'] == username:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # Without lastname, email and rname
        elif (len(args) == 3) and firstName and cname and username:
            result_list = []
            for administrator in administrators:
                if administrator['pname'] == firstName and administrator['city'] == cname and administrator['username'] == username:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # Without firstname, email and rname
        elif (len(args) == 3) and lastName and cname and username:
            result_list = []
            for administrator in administrators:
                if administrator['plname'] == lastName and administrator['city'] == cname and administrator['username'] == username:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # Without lastname, cname and rname
        elif (len(args) == 3) and firstName and email and username:
            result_list = []
            for administrator in administrators:
                if administrator['pname'] == firstName and administrator['email'] == email and administrator['username'] == username:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # Without firstname, cname and rname
        elif (len(args) == 3) and lastName and email and username:
            result_list = []
            for administrator in administrators:
                if administrator['plname'] == lastName and administrator['email'] == email and administrator['username'] == username:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # Without firstname, lastname and rname
        elif (len(args) == 3) and cname and email and username:
            result_list = []
            for administrator in administrators:
                if administrator['city'] == cname and administrator['username'] == username and administrator['email'] == email:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # Without cname, email and username
        elif (len(args) == 3) and firstName and lastName and rname:
            result_list = []
            for administrator in administrators:
                if administrator['pname'] == firstName and administrator['plname'] == lastName and administrator['region'] == rname:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # Without lastname, email and username
        elif (len(args) == 3) and firstName and cname and rname:
            result_list = []
            for administrator in administrators:
                if administrator['pname'] == firstName and administrator['city'] == cname and administrator['region'] == rname:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # Without firstname, email and username
        elif (len(args) == 3) and lastName and cname and rname:
            result_list = []
            for administrator in administrators:
                if administrator['plname'] == lastName and administrator['city'] == cname and administrator['region'] == rname:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # Without lastname, cname and username
        elif (len(args) == 3) and firstName and email and rname:
            result_list = []
            for administrator in administrators:
                if administrator['pname'] == firstName and administrator['email'] == email and administrator['region'] == rname:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # Without firstname, cname and username
        elif (len(args) == 3) and lastName and email and rname:
            result_list = []
            for administrator in administrators:
                if administrator['plname'] == lastName and administrator['email'] == email and administrator['region'] == rname:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # Without lastname, cname and email
        elif (len(args) == 3) and firstName and username and rname:
            result_list = []
            for administrator in administrators:
                if administrator['pname'] == firstName and administrator['username'] == username and administrator['region'] == rname:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # Without firstname, cname and email
        elif (len(args) == 3) and lastName and username and rname:
            result_list = []
            for administrator in administrators:
                if administrator['plname'] == lastName and administrator['username'] == username and administrator['region'] == rname:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # Without firstname, lastname and cname
        elif (len(args) == 3) and email and username and rname:
            result_list = []
            for administrator in administrators:
                if administrator['email'] == email and administrator['username'] == username and administrator['region'] == rname:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # Without firstname, lastname and email
        elif (len(args) == 3) and cname and username and rname:
            result_list = []
            for administrator in administrators:
                if administrator['city'] == cname and administrator['username'] == username and administrator['region'] == rname:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # Without firstname, lastname and username
        elif (len(args) == 3) and cname and email and rname:
            result_list = []
            for administrator in administrators:
                if administrator['city'] == cname and administrator['email'] == email and administrator['region'] == rname:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # ------------------------------------------------------------------------------

        elif (len(args) == 2) and username and rname:
            result_list = []
            for administrator in administrators:
                if administrator['username'] == username and administrator['region'] == rname:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        elif (len(args) == 2) and email and rname:
            result_list = []
            for administrator in administrators:
                if administrator['email'] == email and administrator['region'] == rname:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        elif (len(args) == 2) and cname and rname:
            result_list = []
            for administrator in administrators:
                if administrator['city'] == cname and administrator['region'] == rname:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        elif (len(args) == 2) and lastName and rname:
            result_list = []
            for administrator in administrators:
                if administrator['plname'] == lastName and administrator['region'] == rname:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        elif (len(args) == 2) and firstName and rname:
            result_list = []
            for administrator in administrators:
                if administrator['pname'] == firstName and administrator['region'] == rname:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        elif (len(args) == 2) and username and rname:
            result_list = []
            for administrator in administrators:
                if administrator['username'] == username and administrator['region'] == rname:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        elif (len(args) == 2) and email and username:
            result_list = []
            for administrator in administrators:
                if administrator['username'] == username and administrator['email'] == email:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        elif (len(args) == 2) and cname and username:
            result_list = []
            for administrator in administrators:
                if administrator['username'] == username and administrator['city'] == cname:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        elif (len(args) == 2) and lastName and username:
            result_list = []
            for administrator in administrators:
                if administrator['username'] == username and administrator['plname'] == lastName:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        elif (len(args) == 2) and firstName and username:
            result_list = []
            for administrator in administrators:
                if administrator['username'] == username and administrator['pname'] == firstName:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        elif (len(args) == 2) and cname and email:
            result_list = []
            for administrator in administrators:
                if administrator['city'] == cname and administrator['email'] == email:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        elif (len(args) == 2) and lastName and email:
            result_list = []
            for administrator in administrators:
                if administrator['plname'] == lastName and administrator['email'] == email:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        elif (len(args) == 2) and firstName and email:
            result_list = []
            for administrator in administrators:
                if administrator['pname'] == firstName and administrator['email'] == email:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        elif (len(args) == 2) and lastName and cname:
            result_list = []
            for administrator in administrators:
                if administrator['city'] == cname and administrator['plname'] == lastName:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        elif (len(args) == 2) and firstName and cname:
            result_list = []
            for administrator in administrators:
                if administrator['city'] == cname and administrator['pname'] == firstName:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        elif (len(args) == 2) and firstName and lastName:
            result_list = []
            for administrator in administrators:
                if administrator['pname'] == firstName and administrator['plname'] == lastName:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # ------------------------------------------------------------------------------

        # firstname
        elif (len(args) == 1) and firstName:
            result_list = []
            for administrator in administrators:
                if administrator['pname'] == firstName:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # lastname
        elif (len(args) == 1) and lastName:
            result_list = []
            for administrator in administrators:
                if administrator['plname'] == lastName:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # cname
        elif (len(args) == 1) and cname:
            result_list = []
            for administrator in administrators:
                if administrator['city'] == cname:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # email
        elif (len(args) == 1) and email:
            result_list = []
            for administrator in administrators:
                if administrator['email'] == email:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # username
        elif (len(args) == 1) and username:
            result_list = []
            for administrator in administrators:
                if administrator['username'] == username:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)

        # rname
        elif (len(args) == 1) and rname:
            result_list = []
            for administrator in administrators:
                if administrator['region'] == rname:
                    result_list.append(administrator)
            if not result_list:
                return jsonify(Error="Administrators Not Found"), 404
            return jsonify(Administrators=result_list)
        # ------------------------------------------------------------------------------

        else:
            return 'No administrators found', 404