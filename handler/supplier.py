from flask import jsonify

class SupplierHandler:

    def getAllSuppliers(self):
        return 'Viewing all suppliers'

    def getSupplierById(self, sid):
        return 'Looking for a supplier by ID: %d' % (sid)

    def getSuppliersOnThisrname(self, rname):
       return 'Showing suppliers on rname: %s' %(rname)

    def searchSuppliers(self, args):

        firstName = args.get("pname")
        lastName = args.get('plname')
        cname = args.get('cname')
        email = args.get('email')
        username = args.get('username')
        rname = args.get('rname')

        if (len(args) == 6) and firstName and lastName and cname and email and username and rname:
            return 'Looking for and account by pname, plname, cname, emaill, username and rname'

        # ------------------------------------------------------------------------------

        # Without rname
        elif (len(args) == 5) and firstName and lastName and cname and email and username:
            return 'Looking for an account by pname, plname, cname, email and username'

        # Without username
        elif (len(args) == 5) and firstName and lastName and cname and email and rname:
            return 'Looking for an account by pname, plname, cname, email and rname'

        # Without email
        elif (len(args) == 5) and firstName and lastName and cname and username and rname:
            return 'Looking for an account by pname, plname, cname, username and rname'

        # Without cname
        elif (len(args) == 5) and firstName and lastName and cname and email and rname:
            return 'Looking for an account by pname, plname, cname, email and rname'

        # Without lastname
        elif (len(args) == 5) and firstName and cname and email and username and rname:
            return 'Looking for an account by pname, cname, email, username and rname'

        # Without firstname
        elif (len(args) == 5) and lastName and cname and email and username and rname:
            return 'Looking for an account by plname, cname, email, username and rname'
        # ------------------------------------------------------------------------------

        # Without rname and username
        elif (len(args) == 4) and firstName and lastName and cname and email:
            return 'Looking for an account by pname, plname, cname, and email'

        # Without rname and email
        elif (len(args) == 4) and firstName and lastName and cname and username:
            return 'Looking for an account by pname, plname, cname, and username'

        # Without rname and cname
        elif (len(args) == 4) and firstName and lastName and email and username:
            return 'Looking for an account by pname, plname, email, and username'

        # Without rname and lastname
        elif (len(args) == 4) and firstName and cname and email and username:
            return 'Looking for an account by pname, cname, email, and username'

        # Without rname and firstname
        elif (len(args) == 4) and lastName and cname and email and username:
            return 'Looking for an account by plname, cname, email, and username'

        # Without username and email
        elif (len(args) == 4) and firstName and lastName and cname and rname:
            return 'Looking for an account by pname, plname, cname, and rname'

        # Without username and cname
        elif (len(args) == 4) and firstName and lastName and email and rname:
            return 'Looking for an account by pname, plname, email, and rname'

        # firstname, lastname, cname, email, username, rname

        # Without username and lastname
        elif (len(args) == 4) and firstName and cname and email and rname:
            return 'Looking for an account by pname, cname, email, and rname'

        # Without username and firstname
        elif (len(args) == 4) and lastName and cname and email and rname:
            return 'Looking for an account by plame, cname, email, and rname'

        # Without email and cname
        elif (len(args) == 4) and firstName and lastName and username and rname:
            return 'Looking for an account by pname, plname, username, and rname'

        # Without email and lastname
        elif (len(args) == 4) and firstName and cname and username and rname:
            return 'Looking for an account by pname, cname, username, and rname'

        # Without email and firstname
        elif (len(args) == 4) and lastName and cname and username and rname:
            return 'Looking for an account by plname, cname, username, and rname'

        # Without cname and lastname
        elif (len(args) == 4) and firstName and email and username and rname:
            return 'Looking for an account by pname, email, username, and rname'

        # Without cname and firstName
        elif (len(args) == 4) and lastName and email and username and rname:
            return 'Looking for an account by plname, email, username, and rname'

        # Without lastname and firstName
        elif (len(args) == 4) and cname and email and username and rname:
            return 'Looking for an account by cname, email, username, and rname'

        # ------------------------------------------------------------------------------

        # Without email, username and rname
        elif (len(args) == 3) and firstName and lastName and cname:
            return 'Looking for account by pname, plname and cname'

        # Without cname, username and rname
        elif (len(args) == 3) and firstName and lastName and email:
            return 'Looking for account by pname, plname and email'

        # Without lastname, username and rname
        elif (len(args) == 3) and firstName and cname and email:
            return 'Looking for account by pname, cname and email'

        # Without firstname, username and rname
        elif (len(args) == 3) and lastName and cname and email:
            return 'Looking for account by plname, cname and email'

        # Without cname, email and rname
        elif (len(args) == 3) and firstName and lastName and username:
            return 'Looking for account by pname, plname and username'

        # Without lastname, email and rname
        elif (len(args) == 3) and firstName and cname and username:
            return 'Looking for account by pname, cname and username'

        # Without firstname, email and rname
        elif (len(args) == 3) and lastName and cname and username:
            return 'Looking for account by plname, cname and username'

        # Without lastname, cname and rname
        elif (len(args) == 3) and firstName and email and username:
            return 'Looking for account by pname, email and username'

        # Without firstname, cname and rname
        elif (len(args) == 3) and lastName and email and username:
            return 'Looking for account by plname, email and username'

        # Without firstname, lastname and rname
        elif (len(args) == 3) and cname and email and username:
            return 'Looking for account by cname, email and username'

        # Without cname, email and username
        elif (len(args) == 3) and firstName and lastName and rname:
            return 'Looking for account by pname, plname and rname'

        # Without lastname, email and username
        elif (len(args) == 3) and firstName and cname and rname:
            return 'Looking for account by pname, cname and rname'

        # Without firstname, email and username
        elif (len(args) == 3) and lastName and cname and rname:
            return 'Looking for account by plname, cname and rname'

        # Without lastname, cname and username
        elif (len(args) == 3) and firstName and email and rname:
            return 'Looking for account by pname, email and rname'

        # Without firstname, cname and username
        elif (len(args) == 3) and lastName and email and rname:
            return 'Looking for account by plname, email and rname'

        # Without lastname, cname and email
        elif (len(args) == 3) and firstName and username and rname:
            return 'Looking for account by pname, username and rname'

        # Without firstname, cname and email
        elif (len(args) == 3) and lastName and username and rname:
            return 'Looking for account by plname, username and rname'

        # Without firstname, lastname and cname
        elif (len(args) == 3) and email and username and rname:
            return 'Looking for account by email, username and rname'

        # Without firstname, lastname and email
        elif (len(args) == 3) and cname and username and rname:
            return 'Looking for account by cname, username and rname'

        # Without firstname, lastname and username
        elif (len(args) == 3) and cname and email and rname:
            return 'Looking for account by cname, email and rname'

        # ------------------------------------------------------------------------------

        elif (len(args) == 2) and username and rname:
            return 'Looking for suppliers by username and rname'

        elif (len(args) == 2) and email and rname:
            return 'Looking for suppliers by email and rname'

        elif (len(args) == 2) and cname and rname:
            return 'Looking for suppliers by cname and rname'

        elif (len(args) == 2) and lastName and rname:
            return 'Looking for suppliers by plname and rname'

        elif (len(args) == 2) and firstName and rname:
            return 'Looking for suppliers by pname and rname'

        elif (len(args) == 2) and username and rname:
            return 'Looking for suppliers by username and rname'

        elif (len(args) == 2) and email and username:
            return 'Looking for suppliers by email and username'

        elif (len(args) == 2) and cname and username:
            return 'Looking for suppliers by cname and username'

        elif (len(args) == 2) and lastName and username:
            return 'Looking for suppliers by plname and username'

        elif (len(args) == 2) and firstName and username:
            return 'Looking for suppliers by pname and username'

        elif (len(args) == 2) and cname and email:
            return 'Looking for suppliers by cname and email'

        elif (len(args) == 2) and lastName and email:
            return 'Looking for suppliers by plname and email'

        elif (len(args) == 2) and firstName and email:
            return 'Looking for suppliers by pname and email'

        elif (len(args) == 2) and lastName and cname:
            return 'Looking for suppliers by plname and cname'

        elif (len(args) == 2) and firstName and cname:
            return 'Looking for suppliers by pname and cname'

        elif (len(args) == 2) and firstName and lastName:
            return 'Looking for suppliers by pname and plname'

        # ------------------------------------------------------------------------------

        # firstname
        elif (len(args) == 1) and firstName:
            return 'Looking for suppliers by pname'

        # lastname
        elif (len(args) == 1) and lastName:
            return 'Looking for suppliers by plname'

        # cname
        elif (len(args) == 1) and cname:
            return 'Looking for suppliers by cname'

        # email
        elif (len(args) == 1) and email:
            return 'Looking for suppliers by email'

        # username
        elif (len(args) == 1) and username:
            return 'Looking for suppliers by username'

        # rname
        elif (len(args) == 1) and rname:
            return 'Looking for suppliers by rname'
        # ------------------------------------------------------------------------------

        else:
            return 'No suppliers found', 404