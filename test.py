import re, subprocess, time
from itertools import combinations

routes = []
accounts = ['aid=1', 'afirst = Alexandra', 'alast = Feliciano', 'email = alexandra.feliciano@hormail.com', 'phone = 123']

def read():
    filepath = 'main.py'
    with open(filepath) as fp:
       line = fp.readline()
       while line:
           if 'app.route' in line:
               route = line.split("'")
               route.pop(0)
               route.pop()
               route = route[0].replace('<string:cname>', 'Bayamon')
               route = route.replace('<int:cid>', '3')
               route = route.replace('<int:cashId>', '3')
               route = route.replace('<int:payId>', '3')
               route = route.replace('<int:oid>', '3')
               route = route.replace('<int:tid>', '3')
               route = route.replace('<int:cashId>', '3')
               route = route.replace('<int:bid>', '3')
               route = route.replace('<string:cat_name>', 'Tools')
               route = route.replace('<int:rrid>', '3')
               route = route.replace('<int:rid>', '13')
               route = route.replace('<int:kid>', '3')
               route = route.replace('<int:rsid>', '3')
               route = route.replace('<int:sid>', '3')
               route = route.replace('<int:aid>', '2')
               route = route.replace("<string:username>", "mQuesada")
               route = route.replace("<int:pid>", "3")
               route = route.replace("<int:addId>", "3")
               route = route.replace("<string:cname>", "Mayaguez")
               route = route.replace("<string:rname>", "Mayaguez")
               routes.append(route)
               com = []


                #Accounts
               for r in range (5, 0, -1):
                   com = ["&".join(a) for a in combinations(accounts, r)]
                   for x in com:
                       route2 = re.sub(r'/accounts$', '/accounts?%s' %(x), route)
                       routes.append(route2)

               # Add other entities below this line...


           line = fp.readline()
       new_routes = remove_duplicates(routes)
       test(new_routes)

def test(new_routes):
    for route in new_routes:
        subprocess.call(['echo', '-e', '--------------------------------------------------------------\n'])
        subprocess.call(['echo', '-e', '127.0.0.1:5000%s\n' %(route)])
        subprocess.call(['curl', '-i', '-s', '127.0.0.1:5000%s' %(route)])
        subprocess.call(['echo', '-e', ''])
        #time.sleep(.2)

def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output

read()
