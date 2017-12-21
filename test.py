import subprocess

routes = []
routes.append("/")

# ---------------------------------------------------------------------------- #
#                              Resource routes                                 #
# ---------------------------------------------------------------------------- #
routes.append("/ResourceApp/resources")
routes.append("/ResourceApp/resources/7")
routes.append("/ResourceApp/resources/available")
routes.append("/ResourceApp/resources/needed")
routes.append("/ResourceApp/resources?rname=Diesel&rcategory=Fuel&rqty=3")
routes.append("/ResourceApp/resources?rname=Diesel&rcategory=Fuel")
routes.append("/ResourceApp/resources?rcategory=Fuel&rqty=3")
routes.append("/ResourceApp/resources?rname=Diesel&rqty=3")
routes.append("/ResourceApp/resources?rname=Diesel")
routes.append("/ResourceApp/resources?rcategory=Fuel")
routes.append("/ResourceApp/resources?rqty=3")

# ---------------------------------------------------------------------------- #
#                              Category routes                                 #
# ---------------------------------------------------------------------------- #
routes.append("/ResourceApp/categories")
routes.append("/ResourceApp/categories/JAY")

# ---------------------------------------------------------------------------- #
#                              Region routes                                   #
# ---------------------------------------------------------------------------- #
routes.append("/ResourceApp/regions")
routes.append("/ResourceApp/regions/JAY")

# ---------------------------------------------------------------------------- #
#                              Transaction routes                              #
# ---------------------------------------------------------------------------- #
routes.append("/ResourceApp/supplier/7/resources")
routes.append("/ResourceApp/resource/7/suppliers")
routes.append("/ResourceApp/supply")
routes.append("/ResourceApp/needer/7/resources")
routes.append("/ResourceApp/transactions")
routes.append("/ResourceApp/resource/7/needer/supplier")
routes.append("/ResourceApp/needer/7/resource/supplier")
routes.append("/ResourceApp/supplier/7/resource/needer")

routes.append("/ResourceApp")

# ---------------------------------------------------------------------------- #
#                              Supplier routes                                 #
# ---------------------------------------------------------------------------- #
routes.append("/ResourceApp/supplier")
routes.append("/ResourceApp/supplier/7")
routes.append("/ResourceApp/supplier?pname=YAJ")
routes.append("/ResourceApp/supplier?plname=asa")
routes.append("/ResourceApp/supplier?cname=SanJuan")
routes.append("/ResourceApp/supplier?email=yaj@gmail.com")
routes.append("/ResourceApp/supplier?rname=Metro")
routes.append("/ResourceApp/supplier?pname=YAJ&plname=asa")
routes.append("/ResourceApp/supplier?pname=YAJ&cname=SanJuan")
routes.append("/ResourceApp/supplier?pname=YAJ&email=yaj@gmail.com")
routes.append("/ResourceApp/supplier?pname=YAJ&rname=Metro")
routes.append("/ResourceApp/supplier?plname=asa&cname=SanJuan")
routes.append("/ResourceApp/supplier?plname=asa&email=yaj@gmail.com")
routes.append("/ResourceApp/supplier?plname=asa&rname=Metro")
routes.append("/ResourceApp/supplier?cname=SanJuan&email=yaj@gmail.com")
routes.append("/ResourceApp/supplier?cname=SanJuan&rname=Metro")
routes.append("/ResourceApp/supplier?email=yaj@gmail.com&rname=Metro")
routes.append("/ResourceApp/supplier?pname=YAJ&plname=asa&cname=SanJuan")
routes.append("/ResourceApp/supplier?pname=YAJ&plname=asa&email=yaj@gmail.com")
routes.append("/ResourceApp/supplier?pname=YAJ&plname=asa&rname=Metro")
routes.append("/ResourceApp/supplier?pname=YAJ&cname=SanJuan&email=yaj@gmail.com")
routes.append("/ResourceApp/supplier?pname=YAJ&cname=SanJuan&rname=Metro")
routes.append("/ResourceApp/supplier?pname=YAJ&email=yaj@gmail.com&rname=Metro")
routes.append("/ResourceApp/supplier?plname=asa&cname=SanJuan&email=yaj@gmail.com")
routes.append("/ResourceApp/supplier?plname=asa&cname=SanJuan&rname=Metro")
routes.append("/ResourceApp/supplier?plname=asa&email=yaj@gmail.com&rname=Metro")
routes.append("/ResourceApp/supplier?cname=SanJuan&email=yaj@gmail.com&rname=Metro")
routes.append("/ResourceApp/supplier?pname=YAJ&plname=asa&cname=SanJuan&email=yaj@gmail.com")
routes.append("/ResourceApp/supplier?pname=YAJ&plname=asa&cname=SanJuan&rname=Metro")
routes.append("/ResourceApp/supplier?pname=YAJ&plname=asa&email=yaj@gmail.com&rname=Metro")
routes.append("/ResourceApp/supplier?pname=YAJ&cname=SanJuan&email=yaj@gmail.com&rname=Metro")
routes.append("/ResourceApp/supplier?plname=asa&cname=SanJuan&email=yaj@gmail.com&rname=Metro")
routes.append("/ResourceApp/supplier?pname=YAJ&plname=asa&cname=SanJuan&email=yaj@gmail.com&rname=Metro")

# ---------------------------------------------------------------------------- #
#                              Needer routes                                   #
# ---------------------------------------------------------------------------- #
routes.append("/ResourceApp/needer")
routes.append("/ResourceApp/needer/7")
routes.append("/ResourceApp/needer?pname=YAJ")
routes.append("/ResourceApp/needer?plname=asa")
routes.append("/ResourceApp/needer?cname=SanJuan")
routes.append("/ResourceApp/needer?email=yaj@gmail.com")
routes.append("/ResourceApp/needer?rname=Metro")
routes.append("/ResourceApp/needer?pname=YAJ&plname=asa")
routes.append("/ResourceApp/needer?pname=YAJ&cname=SanJuan")
routes.append("/ResourceApp/needer?pname=YAJ&email=yaj@gmail.com")
routes.append("/ResourceApp/needer?pname=YAJ&rname=Metro")
routes.append("/ResourceApp/needer?plname=asa&cname=SanJuan")
routes.append("/ResourceApp/needer?plname=asa&email=yaj@gmail.com")
routes.append("/ResourceApp/needer?plname=asa&rname=Metro")
routes.append("/ResourceApp/needer?cname=SanJuan&email=yaj@gmail.com")
routes.append("/ResourceApp/needer?cname=SanJuan&rname=Metro")
routes.append("/ResourceApp/needer?email=yaj@gmail.com&rname=Metro")
routes.append("/ResourceApp/needer?pname=YAJ&plname=asa&cname=SanJuan")
routes.append("/ResourceApp/needer?pname=YAJ&plname=asa&email=yaj@gmail.com")
routes.append("/ResourceApp/needer?pname=YAJ&plname=asa&rname=Metro")
routes.append("/ResourceApp/needer?pname=YAJ&cname=SanJuan&email=yaj@gmail.com")
routes.append("/ResourceApp/needer?pname=YAJ&cname=SanJuan&rname=Metro")
routes.append("/ResourceApp/needer?pname=YAJ&email=yaj@gmail.com&rname=Metro")
routes.append("/ResourceApp/needer?plname=asa&cname=SanJuan&email=yaj@gmail.com")
routes.append("/ResourceApp/needer?plname=asa&cname=SanJuan&rname=Metro")
routes.append("/ResourceApp/needer?plname=asa&email=yaj@gmail.com&rname=Metro")
routes.append("/ResourceApp/needer?cname=SanJuan&email=yaj@gmail.com&rname=Metro")
routes.append("/ResourceApp/needer?pname=YAJ&plname=asa&cname=SanJuan&email=yaj@gmail.com")
routes.append("/ResourceApp/needer?pname=YAJ&plname=asa&cname=SanJuan&rname=Metro")
routes.append("/ResourceApp/needer?pname=YAJ&plname=asa&email=yaj@gmail.com&rname=Metro")
routes.append("/ResourceApp/needer?pname=YAJ&cname=SanJuan&email=yaj@gmail.com&rname=Metro")
routes.append("/ResourceApp/needer?plname=asa&cname=SanJuan&email=yaj@gmail.com&rname=Metro")
routes.append("/ResourceApp/needer?pname=YAJ&plname=asa&cname=SanJuan&email=yaj@gmail.com&rname=Metro")

# ---------------------------------------------------------------------------- #
#                            Administrator routes                              #
# ---------------------------------------------------------------------------- #
routes.append("/ResourceApp/administrator")
routes.append("/ResourceApp/administrator/7")
routes.append("/ResourceApp/administrator?pname=YAJ")
routes.append("/ResourceApp/administrator?plname=asa")
routes.append("/ResourceApp/administrator?cname=SanJuan")
routes.append("/ResourceApp/administrator?email=yaj@gmail.com")
routes.append("/ResourceApp/administrator?rname=Metro")
routes.append("/ResourceApp/administrator?pname=YAJ&plname=asa")
routes.append("/ResourceApp/administrator?pname=YAJ&cname=SanJuan")
routes.append("/ResourceApp/administrator?pname=YAJ&email=yaj@gmail.com")
routes.append("/ResourceApp/administrator?pname=YAJ&rname=Metro")
routes.append("/ResourceApp/administrator?plname=asa&cname=SanJuan")
routes.append("/ResourceApp/administrator?plname=asa&email=yaj@gmail.com")
routes.append("/ResourceApp/administrator?plname=asa&rname=Metro")
routes.append("/ResourceApp/administrator?cname=SanJuan&email=yaj@gmail.com")
routes.append("/ResourceApp/administrator?cname=SanJuan&rname=Metro")
routes.append("/ResourceApp/administrator?email=yaj@gmail.com&rname=Metro")
routes.append("/ResourceApp/administrator?pname=YAJ&plname=asa&cname=SanJuan")
routes.append("/ResourceApp/administrator?pname=YAJ&plname=asa&email=yaj@gmail.com")
routes.append("/ResourceApp/administrator?pname=YAJ&plname=asa&rname=Metro")
routes.append("/ResourceApp/administrator?pname=YAJ&cname=SanJuan&email=yaj@gmail.com")
routes.append("/ResourceApp/administrator?pname=YAJ&cname=SanJuan&rname=Metro")
routes.append("/ResourceApp/administrator?pname=YAJ&email=yaj@gmail.com&rname=Metro")
routes.append("/ResourceApp/administrator?plname=asa&cname=SanJuan&email=yaj@gmail.com")
routes.append("/ResourceApp/administrator?plname=asa&cname=SanJuan&rname=Metro")
routes.append("/ResourceApp/administrator?plname=asa&email=yaj@gmail.com&rname=Metro")
routes.append("/ResourceApp/administrator?cname=SanJuan&email=yaj@gmail.com&rname=Metro")
routes.append("/ResourceApp/administrator?pname=YAJ&plname=asa&cname=SanJuan&email=yaj@gmail.com")
routes.append("/ResourceApp/administrator?pname=YAJ&plname=asa&cname=SanJuan&rname=Metro")
routes.append("/ResourceApp/administrator?pname=YAJ&plname=asa&email=yaj@gmail.com&rname=Metro")
routes.append("/ResourceApp/administrator?pname=YAJ&cname=SanJuan&email=yaj@gmail.com&rname=Metro")
routes.append("/ResourceApp/administrator?plname=asa&cname=SanJuan&email=yaj@gmail.com&rname=Metro")
routes.append("/ResourceApp/administrator?pname=YAJ&plname=asa&cname=SanJuan&email=yaj@gmail.com&rname=Metro")

# ---------------------------------------------------------------------------- #
#                              Account routes                                  #
# ---------------------------------------------------------------------------- #
routes.append("/ResourceApp/account/7")
routes.append("/ResourceApp/account")
routes.append("/ResourceApp/account?pname=YAJ")
routes.append("/ResourceApp/account?plname=asa")
routes.append("/ResourceApp/account?cname=SanJuan")
routes.append("/ResourceApp/account?email=yaj@gmail.com")
routes.append("/ResourceApp/account?rname=Metro")
routes.append("/ResourceApp/account?pname=YAJ&plname=asa")
routes.append("/ResourceApp/account?pname=YAJ&cname=SanJuan")
routes.append("/ResourceApp/account?pname=YAJ&email=yaj@gmail.com")
routes.append("/ResourceApp/account?pname=YAJ&rname=Metro")
routes.append("/ResourceApp/account?plname=asa&cname=SanJuan")
routes.append("/ResourceApp/account?plname=asa&email=yaj@gmail.com")
routes.append("/ResourceApp/account?plname=asa&rname=Metro")
routes.append("/ResourceApp/account?cname=SanJuan&email=yaj@gmail.com")
routes.append("/ResourceApp/account?cname=SanJuan&rname=Metro")
routes.append("/ResourceApp/account?email=yaj@gmail.com&rname=Metro")
routes.append("/ResourceApp/account?pname=YAJ&plname=asa&cname=SanJuan")
routes.append("/ResourceApp/account?pname=YAJ&plname=asa&email=yaj@gmail.com")
routes.append("/ResourceApp/account?pname=YAJ&plname=asa&rname=Metro")
routes.append("/ResourceApp/account?pname=YAJ&cname=SanJuan&email=yaj@gmail.com")
routes.append("/ResourceApp/account?pname=YAJ&cname=SanJuan&rname=Metro")
routes.append("/ResourceApp/account?pname=YAJ&email=yaj@gmail.com&rname=Metro")
routes.append("/ResourceApp/account?plname=asa&cname=SanJuan&email=yaj@gmail.com")
routes.append("/ResourceApp/account?plname=asa&cname=SanJuan&rname=Metro")
routes.append("/ResourceApp/account?plname=asa&email=yaj@gmail.com&rname=Metro")
routes.append("/ResourceApp/account?cname=SanJuan&email=yaj@gmail.com&rname=Metro")
routes.append("/ResourceApp/account?pname=YAJ&plname=asa&cname=SanJuan&email=yaj@gmail.com")
routes.append("/ResourceApp/account?pname=YAJ&plname=asa&cname=SanJuan&rname=Metro")
routes.append("/ResourceApp/account?pname=YAJ&plname=asa&email=yaj@gmail.com&rname=Metro")
routes.append("/ResourceApp/account?pname=YAJ&cname=SanJuan&email=yaj@gmail.com&rname=Metro")
routes.append("/ResourceApp/account?plname=asa&cname=SanJuan&email=yaj@gmail.com&rname=Metro")
routes.append("/ResourceApp/account?pname=YAJ&plname=asa&cname=SanJuan&email=yaj@gmail.com&rname=Metro")


# ---------------------------------------------------------------------------- #
#                              City routes                                     #
# ---------------------------------------------------------------------------- #
routes.append("/ResourceApp/city")
routes.append("/ResourceApp/city/JAY")

# ---------------------------------------------------------------------------- #
#                              Request routes                                  #
# ---------------------------------------------------------------------------- #
routes.append("/ResourceApp/request?qty=12&request_date=12-1-2017")
routes.append("/ResourceApp/request?request_date=12-1-2017")
routes.append("/ResourceApp/request?qty=12")
routes.append("/ResourceApp/request/needer?city=SJ")
routes.append("/ResourceApp/request/needer/city/region/San Juan")

# ---------------------------------------------------------------------------- #
#                              Supply routes                                   #
# ---------------------------------------------------------------------------- #
routes.append("/ResourceApp/supply?qty=12&supply_date=12-1-2017")
routes.append("/ResourceApp/supply?supply_date=12-1-2017")
routes.append("/ResourceApp/supply?qty=12")
routes.append("/ResourceApp/supply/supplier?city=SJ")
routes.append("/ResourceApp/supply/supplier/city/region/San Juan")

# ---------------------------------------------------------------------------- #
#                              Transactions routes                             #
# ---------------------------------------------------------------------------- #
routes.append("/ResourceApp/transactions?price=15&quantity=13&purchase_date=12-1-2017")
routes.append("/ResourceApp/transactions?price=15&purchase_date=12-1-2017")
routes.append("/ResourceApp/transactions?price=15&quantity=13")
routes.append("/ResourceApp/transactions?quantity=13&purchase_date=12-1-2017")
routes.append("/ResourceApp/transactions?price=15")
routes.append("/ResourceApp/transactions?quantity=13")
routes.append("/ResourceApp/transactions?purchase_date=12-1-2017")
routes.append("/ResourceApp/transactions?cat=Agua")

def test():
    for route in routes:
        subprocess.call(['echo', '-e', '--------------------------------------------------------------\n'])
        subprocess.call(['echo', '-e', '127.0.0.1:5000%s\n' %(route)])
        subprocess.call(['curl', '-i', '-s', '127.0.0.1:5000%s' %(route)])
        subprocess.call(['echo', '-e', ''])

test()
