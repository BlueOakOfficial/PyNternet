#Импорты Imports


#Переменные Values
hello='Welcome and thank you for joining our project we feeling you love it. Now just type urls we have for that time like welcome.off. Ver 0.0.1'
site='welcome.off'
sites=['welcome.off','pynder.off']
site_finder=0
site_list=0
#Код Code
f=open('sites.g','r')
for site_list in f:
    sites.append(site_list)

site_check=len(sites)

for site_view in sites:
     if site_view == len(sites):
        print(site_view)