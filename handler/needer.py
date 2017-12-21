from flask import jsonify

needers = [
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
    }
]


class NeederHandler:
    def getAllNeeders(self):
        return jsonify(needers=needers)

    def getNeederById(self, sid):
        result_list = []
        for needer in needers:
            if needer['sid'] == sid:
                result_list.append(needer)
        if not result_list:
            return jsonify(Error="needer Not Found"), 404
        return jsonify(needer=result_list)

    def searchNeeders(self, args):

        firstName = args.get("pname")
        lastName = args.get('plname')
        cname = args.get('cname')
        email = args.get('email')
        username = args.get('username')
        rname = args.get('rname')

        if (len(args) == 6) and firstName and lastName and cname and email and username and rname:
            result_list = []
            for needer in needers:
                if needer['pname'] == firstName and needer['plname'] == lastName and needer['city'] == cname \
                        and needer['email'] == email and needer['username'] == username \
                        and needer['region'] == rname:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # ------------------------------------------------------------------------------

        # Without rname
        elif (len(args) == 5) and firstName and lastName and cname and email and username:
            result_list = []
            for needer in needers:
                if needer['pname'] == firstName and needer['plname'] == lastName and needer['city'] == cname \
                        and needer['email'] == email and needer['username'] == username:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # Without username
        elif (len(args) == 5) and firstName and lastName and cname and email and rname:
            result_list = []
            for needer in needers:
                if needer['pname'] == firstName and needer['plname'] == lastName and needer['city'] == cname \
                        and needer['email'] == email and needer['region'] == rname:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # Without email
        elif (len(args) == 5) and firstName and lastName and cname and username and rname:
            result_list = []
            for needer in needers:
                if needer['pname'] == firstName and needer['plname'] == lastName and needer['city'] == cname \
                        and needer['username'] == username and needer['region'] == rname:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # Without cname
        elif (len(args) == 5) and firstName and lastName and cname and email and rname:
            result_list = []
            for needer in needers:
                if needer['pname'] == firstName and needer['plname'] == lastName and needer['email'] == email \
                        and needer['username'] == username and needer['region'] == rname:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # Without lastname
        elif (len(args) == 5) and firstName and cname and email and username and rname:
            result_list = []
            for needer in needers:
                if needer['pname'] == firstName and needer['city'] == cname \
                        and needer['email'] == email and needer['username'] == username \
                        and needer['region'] == rname:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # Without firstname
        elif (len(args) == 5) and lastName and cname and email and username and rname:
            result_list = []
            for needer in needers:
                if needer['plname'] == lastName and needer['city'] == cname \
                        and needer['email'] == email and needer['username'] == username \
                        and needer['region'] == rname:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)
        # ------------------------------------------------------------------------------

        # Without rname and username
        elif (len(args) == 4) and firstName and lastName and cname and email:
            result_list = []
            for needer in needers:
                if needer['pname'] == firstName and needer['plname'] == lastName and needer['city'] == cname \
                        and needer['email'] == email:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # Without rname and email
        elif (len(args) == 4) and firstName and lastName and cname and username:
            result_list = []
            for needer in needers:
                if needer['pname'] == firstName and needer['plname'] == lastName and needer['city'] == cname \
                        and needer['username'] == username:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # Without rname and cname
        elif (len(args) == 4) and firstName and lastName and email and username:
            result_list = []
            for needer in needers:
                if needer['pname'] == firstName and needer['plname'] == lastName \
                        and needer['email'] == email and needer['username'] == username:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # Without rname and lastname
        elif (len(args) == 4) and firstName and cname and email and username:
            result_list = []
            for needer in needers:
                if needer['pname'] == firstName and needer['city'] == cname \
                        and needer['email'] == email and needer['username'] == username:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # Without rname and firstname
        elif (len(args) == 4) and lastName and cname and email and username:
            result_list = []
            for needer in needers:
                if needer['plname'] == lastName and needer['city'] == cname \
                        and needer['email'] == email and needer['username'] == username:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # Without username and email
        elif (len(args) == 4) and firstName and lastName and cname and rname:
            result_list = []
            for needer in needers:
                if needer['pname'] == firstName and needer['plname'] == lastName and needer['city'] == cname \
                        and needer['region'] == rname:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # Without username and cname
        elif (len(args) == 4) and firstName and lastName and email and rname:
            result_list = []
            for needer in needers:
                if needer['pname'] == firstName and needer['plname'] == lastName \
                        and needer['email'] == email and needer['region'] == rname:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # firstname, lastname, cname, email, username, rname

        # Without username and lastname
        elif (len(args) == 4) and firstName and cname and email and rname:
            result_list = []
            for needer in needers:
                if needer['pname'] == firstName and needer['city'] == cname \
                        and needer['email'] == email and needer['region'] == rname:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # Without username and firstname
        elif (len(args) == 4) and lastName and cname and email and rname:
            result_list = []
            for needer in needers:
                if needer['plname'] == lastName and needer['city'] == cname \
                        and needer['email'] == email and needer['region'] == rname:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # Without email and cname
        elif (len(args) == 4) and firstName and lastName and username and rname:
            result_list = []
            for needer in needers:
                if needer['pname'] == firstName and needer['plname'] == lastName \
                        and needer['username'] == username and needer['region'] == rname:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # Without email and lastname
        elif (len(args) == 4) and firstName and cname and username and rname:
            result_list = []
            for needer in needers:
                if needer['pname'] == firstName and needer['city'] == cname \
                        and needer['username'] == username and needer['region'] == rname:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # Without email and firstname
        elif (len(args) == 4) and lastName and cname and username and rname:
            result_list = []
            for needer in needers:
                if needer['plname'] == lastName and needer['city'] == cname \
                        and needer['username'] == username and needer['region'] == rname:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # Without cname and lastname
        elif (len(args) == 4) and firstName and email and username and rname:
            result_list = []
            for needer in needers:
                if needer['pname'] == firstName \
                        and needer['email'] == email and needer['username'] == username \
                        and needer['region'] == rname:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # Without cname and firstName
        elif (len(args) == 4) and lastName and email and username and rname:
            result_list = []
            for needer in needers:
                if needer['plname'] == lastName \
                        and needer['email'] == email and needer['username'] == username \
                        and needer['region'] == rname:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # Without lastname and firstName
        elif (len(args) == 4) and cname and email and username and rname:
            result_list = []
            for needer in needers:
                if needer['city'] == cname \
                        and needer['email'] == email and needer['username'] == username \
                        and needer['region'] == rname:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # ------------------------------------------------------------------------------

        # Without email, username and rname
        elif (len(args) == 3) and firstName and lastName and cname:
            result_list = []
            for needer in needers:
                if needer['pname'] == firstName and needer['plname'] == lastName and needer['city'] == cname:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # Without cname, username and rname
        elif (len(args) == 3) and firstName and lastName and email:
            result_list = []
            for needer in needers:
                if needer['pname'] == firstName and needer['plname'] == lastName and needer['email'] == email:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # Without lastname, username and rname
        elif (len(args) == 3) and firstName and cname and email:
            result_list = []
            for needer in needers:
                if needer['pname'] == firstName and needer['city'] == cname and needer['email'] == email:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # Without firstname, username and rname
        elif (len(args) == 3) and lastName and cname and email:
            result_list = []
            for needer in needers:
                if needer['plname'] == lastName and needer['city'] == cname and needer['email'] == email:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # Without cname, email and rname
        elif (len(args) == 3) and firstName and lastName and username:
            result_list = []
            for needer in needers:
                if needer['pname'] == firstName and needer['plname'] == lastName \
                        and needer['username'] == username:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # Without lastname, email and rname
        elif (len(args) == 3) and firstName and cname and username:
            result_list = []
            for needer in needers:
                if needer['pname'] == firstName and needer['city'] == cname and needer['username'] == username:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # Without firstname, email and rname
        elif (len(args) == 3) and lastName and cname and username:
            result_list = []
            for needer in needers:
                if needer['plname'] == lastName and needer['city'] == cname and needer['username'] == username:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # Without lastname, cname and rname
        elif (len(args) == 3) and firstName and email and username:
            result_list = []
            for needer in needers:
                if needer['pname'] == firstName and needer['email'] == email and needer['username'] == username:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # Without firstname, cname and rname
        elif (len(args) == 3) and lastName and email and username:
            result_list = []
            for needer in needers:
                if needer['plname'] == lastName and needer['email'] == email and needer['username'] == username:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # Without firstname, lastname and rname
        elif (len(args) == 3) and cname and email and username:
            result_list = []
            for needer in needers:
                if needer['city'] == cname and needer['username'] == username and needer['email'] == email:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # Without cname, email and username
        elif (len(args) == 3) and firstName and lastName and rname:
            result_list = []
            for needer in needers:
                if needer['pname'] == firstName and needer['plname'] == lastName and needer['region'] == rname:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # Without lastname, email and username
        elif (len(args) == 3) and firstName and cname and rname:
            result_list = []
            for needer in needers:
                if needer['pname'] == firstName and needer['city'] == cname and needer['region'] == rname:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # Without firstname, email and username
        elif (len(args) == 3) and lastName and cname and rname:
            result_list = []
            for needer in needers:
                if needer['plname'] == lastName and needer['city'] == cname and needer['region'] == rname:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # Without lastname, cname and username
        elif (len(args) == 3) and firstName and email and rname:
            result_list = []
            for needer in needers:
                if needer['pname'] == firstName and needer['email'] == email and needer['region'] == rname:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # Without firstname, cname and username
        elif (len(args) == 3) and lastName and email and rname:
            result_list = []
            for needer in needers:
                if needer['plname'] == lastName and needer['email'] == email and needer['region'] == rname:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # Without lastname, cname and email
        elif (len(args) == 3) and firstName and username and rname:
            result_list = []
            for needer in needers:
                if needer['pname'] == firstName and needer['username'] == username and needer['region'] == rname:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # Without firstname, cname and email
        elif (len(args) == 3) and lastName and username and rname:
            result_list = []
            for needer in needers:
                if needer['plname'] == lastName and needer['username'] == username and needer['region'] == rname:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # Without firstname, lastname and cname
        elif (len(args) == 3) and email and username and rname:
            result_list = []
            for needer in needers:
                if needer['email'] == email and needer['username'] == username and needer['region'] == rname:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # Without firstname, lastname and email
        elif (len(args) == 3) and cname and username and rname:
            result_list = []
            for needer in needers:
                if needer['city'] == cname and needer['username'] == username and needer['region'] == rname:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # Without firstname, lastname and username
        elif (len(args) == 3) and cname and email and rname:
            result_list = []
            for needer in needers:
                if needer['city'] == cname and needer['email'] == email and needer['region'] == rname:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # ------------------------------------------------------------------------------

        elif (len(args) == 2) and username and rname:
            result_list = []
            for needer in needers:
                if needer['username'] == username and needer['region'] == rname:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        elif (len(args) == 2) and email and rname:
            result_list = []
            for needer in needers:
                if needer['email'] == email and needer['region'] == rname:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        elif (len(args) == 2) and cname and rname:
            result_list = []
            for needer in needers:
                if needer['city'] == cname and needer['region'] == rname:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        elif (len(args) == 2) and lastName and rname:
            result_list = []
            for needer in needers:
                if needer['plname'] == lastName and needer['region'] == rname:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        elif (len(args) == 2) and firstName and rname:
            result_list = []
            for needer in needers:
                if needer['pname'] == firstName and needer['region'] == rname:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        elif (len(args) == 2) and username and rname:
            result_list = []
            for needer in needers:
                if needer['username'] == username and needer['region'] == rname:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        elif (len(args) == 2) and email and username:
            result_list = []
            for needer in needers:
                if needer['username'] == username and needer['email'] == email:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        elif (len(args) == 2) and cname and username:
            result_list = []
            for needer in needers:
                if needer['username'] == username and needer['city'] == cname:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        elif (len(args) == 2) and lastName and username:
            result_list = []
            for needer in needers:
                if needer['username'] == username and needer['plname'] == lastName:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        elif (len(args) == 2) and firstName and username:
            result_list = []
            for needer in needers:
                if needer['username'] == username and needer['pname'] == firstName:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        elif (len(args) == 2) and cname and email:
            result_list = []
            for needer in needers:
                if needer['city'] == cname and needer['email'] == email:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        elif (len(args) == 2) and lastName and email:
            result_list = []
            for needer in needers:
                if needer['plname'] == lastName and needer['email'] == email:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        elif (len(args) == 2) and firstName and email:
            result_list = []
            for needer in needers:
                if needer['pname'] == firstName and needer['email'] == email:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        elif (len(args) == 2) and lastName and cname:
            result_list = []
            for needer in needers:
                if needer['city'] == cname and needer['plname'] == lastName:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        elif (len(args) == 2) and firstName and cname:
            result_list = []
            for needer in needers:
                if needer['city'] == cname and needer['pname'] == firstName:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        elif (len(args) == 2) and firstName and lastName:
            result_list = []
            for needer in needers:
                if needer['pname'] == firstName and needer['plname'] == lastName:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # ------------------------------------------------------------------------------

        # firstname
        elif (len(args) == 1) and firstName:
            result_list = []
            for needer in needers:
                if needer['pname'] == firstName:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # lastname
        elif (len(args) == 1) and lastName:
            result_list = []
            for needer in needers:
                if needer['plname'] == lastName:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # cname
        elif (len(args) == 1) and cname:
            result_list = []
            for needer in needers:
                if needer['city'] == cname:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # email
        elif (len(args) == 1) and email:
            result_list = []
            for needer in needers:
                if needer['email'] == email:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # username
        elif (len(args) == 1) and username:
            result_list = []
            for needer in needers:
                if needer['username'] == username:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)

        # rname
        elif (len(args) == 1) and rname:
            result_list = []
            for needer in needers:
                if needer['region'] == rname:
                    result_list.append(needer)
            if not result_list:
                return jsonify(Error="needers Not Found"), 404
            return jsonify(needers=result_list)
        # ------------------------------------------------------------------------------

        else:
            return 'No needers found', 404