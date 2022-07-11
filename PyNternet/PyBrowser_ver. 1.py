from re import I
import PyNternet as pynet

#Переменные

#Код Codewelcome.off
print(pynet.hello)
site_check=input('')
if site_check in pynet.sites:
    site_f=open(site_check,'r')
    print('Current site is {}'.format(pynet.site))
    site_content=site_f.readlines()
    for site_page in range(len(site_content)):
        print(site_content[site_page])
    site_f.close
else:
    print("Can't find pysite")