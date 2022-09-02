from random import seed
from parsing import *
from branch import *



def main():
    bilgisayarlar_it,kullanicilar_it,bilgisayarlar_arge,kullanicilar_arge=ldap_init()

    lst_con = [str(st) for st in bilgisayarlar_arge]
    lst_con = parse(lst_con)

    lst_con_2 = [str(st) for st in bilgisayarlar_it]
    lst_con_2= parse(lst_con_2)

    lst_con_3 = [str(st) for st in kullanicilar_it]
    lst_con_3= parse(lst_con_3)

    lst_con_4 = [str(st) for st in kullanicilar_arge]
    lst_con_4= parse(lst_con_4)


    lst = [
        node(lst_con[0], part='root',img="root"),
        node(lst_con[1], part='body',parent=lst_con[0], img="server"),
        node(lst_con[2], part='body',parent=lst_con[1], img="server"),
        node(lst_con[3], part='body',parent=lst_con[2] ,img="pc"),
        node(lst_con[4], part='branch',parent= lst_con[2], img="pc"),
        node(lst_con[5], part='branch',parent=lst_con[2], img="pc"),
        node(lst_con[6], part='branch', parent=lst_con[2],img="pc"),
        node(lst_con[7], part='branch',parent=lst_con[2], img="pc"),
    ]

    lst_2 = [
        node(lst_con_2[0], part='root',img="root"),
        node(lst_con_2[1], part='body',parent=lst_con_2[0], img="server"),
        node(lst_con_2[2], part='body',parent=lst_con_2[1], img="server"),
        node(lst_con_2[3], part='body',parent=lst_con_2[2] ,img="pc"),
        node(lst_con_2[4], part='branch',parent= lst_con_2[2], img="pc"),
        node(lst_con_2[5], part='branch',parent=lst_con_2[2], img="pc"),
        node(lst_con_2[6], part='branch', parent=lst_con_2[2],img="pc"),
        node(lst_con_2[7], part='branch',parent=lst_con_2[2], img="pc"),
    ]

    lst_3 = [
        node(lst_con_3[0], part='root',img="root"),
        node(lst_con_3[1], part='body',parent=lst_con_3[0], img="server"),
        node(lst_con_3[2], part='body',parent=lst_con_3[1], img="server"),
        node(lst_con_3[3], part='body',parent=lst_con_3[2] ,img="user"),
        node(lst_con_3[4], part='branch',parent= lst_con_3[2], img="user"),
    ]
   
    lst_4 = [
        node(lst_con_4[0], part='root',img="root"),
        node(lst_con_4[1], part='body',parent=lst_con_4[0], img="server"),
        node(lst_con_4[2], part='body',parent=lst_con_4[1], img="server"),
        node(lst_con_4[3], part='body',parent=lst_con_4[2] ,img="user"),
        node(lst_con_4[4], part='branch',parent= lst_con_4[2], img="user"),
        node(lst_con_4[5], part='branch',parent= lst_con_4[2], img="user"),
        node(lst_con_4[6], part='branch',parent= lst_con_4[2], img="user"),
        node(lst_con_4[7], part='branch',parent= lst_con_4[2], img="user"),

        
    ]
    

    _graph = myGraph(lst + lst_2+lst_3+lst_4,seed=42,figsize=(10,10))


if __name__ == "__main__":
    main()