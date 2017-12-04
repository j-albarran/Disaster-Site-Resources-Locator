import subprocess

routes = []
routes.append("/")
routes.append("/ResourceApp/resources")
routes.append("/ResourceApp/resources/7")
routes.append("/ResourceApp/resources/available")
routes.append("/ResourceApp/resources/needed")
routes.append("/ResourceApp/categories")
routes.append("/ResourceApp/categories/JAY")
routes.append("/ResourceApp/regions")
routes.append("/ResourceApp/regions/JAY")
routes.append("/ResourceApp/supplier/7/resources")
routes.append("/ResourceApp/resource/7/suppliers")
routes.append("/ResourceApp/supply")
routes.append("/ResourceApp/needer/7/resources")
routes.append("/ResourceApp/transactions")
routes.append("/ResourceApp/resource/7/needer/supplier")
routes.append("/ResourceApp/needer/7/resource/supplier")
routes.append("/ResourceApp/supplier/7/resource/needer")
routes.append("/ResourceApp")
routes.append("/ResourceApp/suppliers")
routes.append("/ResourceApp/suppliers/7")
routes.append("/ResourceApp/needers")
routes.append("/ResourceApp/needers/7")
routes.append("/ResourceApp/administrators")
routes.append("/ResourceApp/administrators/7")
routes.append("/ResourceApp/persons/7")
routes.append("/ResourceApp/persons")
routes.append("/ResourceApp/cities")
routes.append("/ResourceApp/cities/JAY")

def test():
    for route in routes:
        print("--------------------------------------------------------------\n")
        print("127.0.0.1:5000" + route + "\n")
        subprocess.call("curl -i 127.0.0.1:5000" + route, shell=True)
        print("\n")

test()
