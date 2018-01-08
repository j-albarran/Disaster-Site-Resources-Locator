import re, subprocess, time

routes = []

def read():
    filepath = 'main.py'
    with open(filepath) as fp:
       line = fp.readline()
       cnt = 1
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
           line = fp.readline()
           cnt += 1

def test():
    for route in routes:
        subprocess.call(['echo', '-e', '--------------------------------------------------------------\n'])
        subprocess.call(['echo', '-e', '127.0.0.1:5000%s\n' %(route)])
        subprocess.call(['curl', '-i', '-s', '127.0.0.1:5000%s' %(route)])
        subprocess.call(['echo', '-e', ''])
        #time.sleep(.2)

read()
test()
