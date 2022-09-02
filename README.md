# Active Directory Graph


# İçindekiler
* [Proje Özeti](#proje-özeti)
* [Özgün Değer](#özgün-değer)
* [Amaç ve Hedefler](#amaç-ve-hedefler)
* [Yöntem ve yararlanılan teknolojiler](#yöntem-ve-yararlanılan-teknolojiler)



## Proje Özeti 

  Şirketlerde kullanımı yaygınlaşan Active Directory sistemi getirdiği kolaylıklar yanında gözden kaçan riskleri beraberinde getiriyor. Günümüzde her 39 saniyede bir siber saldırı gerçekleşmektedir. Bunların %94’ü e-mail üzerinden yapılan phishing yöntemi ile yapılmaktadır. Ayrıca 2020 yılı itibariyle fidye yazılımları vakaları %150 artış göstermiştir ve bunlardan en çok etkilenenler işletmeler ve iş kurumlarıdır. Bu kuruluşlar eğer Active Directory üzerine bu saldırılara maruz kalırlarsa tüm sistem tehlikeye girebilmektedir. Oluşan zarar üretimi durdurmaya ve hatta iflasa kadar sürükleyebilmektedir. Projemizin amacı burada devreye girmektedir ve oluşabilecek hasarı en aza indirmeyi amaçlar ve hatta cihazların yetki ve erişimleri üzerinden nasıl bir hasarı oluşabileceğini graph yapısı ile göstermeyi amaçlamaktadır.
  
  
  Active Directory üzerinde yetkilendirme ve erişimleri gösterebilen, olası sızıntılarda erişimi tehlikeye giren kullanıcıları göstererek olası sızıntılara karşı kuruluşların hazır olmasını sağlar. Örneğin A-B-C-D-E cihazları düşünüldüğünde A bilgisayarının yetki ve erişimleri örnek olarak  B - C ve D cihazları olsun bir saldırı planında her zaman daha fazla zarar verebilmek için ana bilgisayar veya yetki ve erişimi daha yüksek olan cihazlar hedeflenmektedir. Böyle bir senaryoda A cihazının elle geçirilmesi durumunda sahip olduğu yetki ve erişimler sayesinde B - C ve D cihazları tehlike altına girmiş olacaktır. Projemiz böyle bir senaryo üzerinde oluşabilecek tehlikeleri göstermeyi ve kullanıcıyı uyarmayı hedefler. Bu sayede sistem yöneticisi oluşabilicek sızıntıları öngörebilir ve hasarı minimuma indirme üzerine yeni bir sistem topolojisi oluşturur.
  
 ## Özgün Değer
 
  Merkezi yönetim sistemleri denince akla ilk gelen Active Directory olmaktadır. Şirketler ve kuruluşlar tarafından sıkça kullanılan active directory getirdiği kolaylıkların yanında her teknolojinin de barındırdığı gibi riskler de bulunmaktadır. Microsoft’un 2021 yılında açıkladığı siber saldırı engelleme oranlarında kimlik istismarı saldırısı türlerinde 25 milyon civarında saldırının engellendiği açıklandı. Bu sayı toplam saldırılar içerisinde büyük bir kısmını oluşturmakta. Bu tarz saldırıların şirket ve kuruluşları iflasa kadar götürdüğü bilinmektedir. Şirketlerin iş modelleri sekteye uğrasa dahil işlerine devam etseler de itibarlarını büyük ölçüde kaybetmektedir. Böyle büyük problemler ekonomik anlamda büyük zararlar oluşturmakta ve engellenemez ise bile kontrol altına daha kısa sürede alınması gerekmektedir. Active Directory üzerinde yapılan saldırı ile yetkisi ele geçirilen bir kullanıcı ile sisteme dahil olup zarar verme ve sistemi sömürme aşamasına geçildi ise bu kullanıcın yetki ve erişimleri olan kulanıcılarında hızlı bir şekilde gözetlenmesi ve gerekirse müdahale edilmesi gerekmektedir. Bu sayede sistemin enfekte olma durumunun büyümesi de engellenmiş olacak ve oluşabilecek daha büyük zararlar ortadan kaldırılmış olacaktır.
 
  Yapılan literatür araştırmasında Active Directory userları üzerinden haritalandırma projelerinden büyük çoğunluğu ücretli ve kaynak kodu kapalı olduğu görülmüştür. Ücretsiz olanlarında kapalı kaynak koda sahip olduğu ile de karşılaşılmıştır. Açık kaynak kodlu proje olarak ise Bloodhound ile karşılaşılmıştır. Karmaşık sayılabilecek bir çalışma mekanizması bulunmaktadır ve powershell scriptleri, javascript, html, css dörtlüsünden oluşmaktadır. Bu projenin özgünlüğü ise mümkün olduğunca karmaşıklığın önüne geçerek python dili ile sisteme direkt bağlantı sağlanarak elde edilen bilgiler dahilinde haritanın oluşturulması hedeflenmektedir.
  
  
## Amaçlar ve Hedefler 
  
  Active Directory sistemlerinde oluşabilecek hasarları minimum düzeye indirmeyi amaçlayan ve meydana gelebilecek olan büyük hasarları erkenden tespit edip, bir grap yapısı ile senaryoları ortaya koyarak ve bu sayede erkenden harekete geçmeyi ve gözden kaçan yerleri görmemizi amaçlayan bir güvenlik aracı olmasıdır.
  
  
## Yöntem ve Kullanılan Teknolojiler 
  
  * Python LDAP modülü :
  * Graph algoritmaları için Python Networkx modülü

![](Proje/graph.png)
