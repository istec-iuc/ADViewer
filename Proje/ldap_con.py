from http import server
from wsgiref import validate
from xmlrpc.client import Server
from ldap3 import Connection, Server, ALL 
from graphnode import * 
from linkedlist import * 
import prompt_toolkit 
from prompt_toolkit.output import ColorDepth




def ldap_init():
    
    try :
        server=Server("ldap://windows-server.hunterhound.local",get_info=ALL)
        user=input("User Bilgisini Giriniz: ")
        password=prompt_toolkit.prompt("PassWord Bilgisini Giriniz: ",is_password=True)
        con=Connection(server,user, password, auto_bind=True)
        print("-----------------------------------------------------------------------")
        print("Bağlantı Adresi : ", con)
        print("-----------------------------------------------------------------------")
        con.search('ou=it_bilgisayarlar,ou=IT_Departmanı,dc=hunterhound,dc=local','(cn=*)')
        bilgisayarlar_it=con.entries
        print("\n",con.entries,"\n")
        print("-----------------------------------------------------------------------")
        con.search('ou=it_kullanıcılar,ou=IT_Departmanı,dc=hunterhound,dc=local','(cn=*)')
        kullanicilar_it=con.entries
        print("\n",con.entries,"\n")
        print("-----------------------------------------------------------------------")
        con.search('ou=arge_bilgisayarlar,ou=AR-GE_Departmanı,dc=hunterhound,dc=local','(cn=*)')
        bilgisayarlar_arge=con.entries
        print("\n",con.entries,"\n")
        print("-----------------------------------------------------------------------")
        con.search('ou=arge_kullanıcılar,ou=AR-GE_Departmanı,dc=hunterhound,dc=local','(cn=*)')
        kullanicilar_arge=con.entries
        print("\n",con.entries,"\n")

        return(bilgisayarlar_it,kullanicilar_it,bilgisayarlar_arge,kullanicilar_arge)

    except:
        print("\n\nYanlış kullanıcı adı veya şifre girdiniz programdan çıkış yapılıyor...")
        exit()    
    

