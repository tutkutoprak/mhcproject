import streamlit as st
import joblib
import pandas as pd

st.set_page_config(layout='wide')

def get_model():
    model = joblib.load("files/voting_clf.pkl")
    return model

st.header('❤️ **Miuul :red[Hearthcare] Project**')
tab_home, tab_graf, tab_end, tab_team = st.tabs(['Giriş', 'Grafikler', 'Sonuç', '💕MHCTeam'])

# TAB HOME

column_ent, column_pro = tab_home.columns(2, gap='large')

column_ent.write('Bu proje kalp sağlığını etkileyen unsurların tespitini yapıp bunu makine öğrenmesi kullanarak rahatsızlığa neden olan etkenleri belirleme amacı taşımaktadır. Projenin ışık tutmak istediği ana konu ise kalp sağlığına yönelik bireylerin açık kaynaklardan bilgi alma özgürlüğünün yanında dolaşım hastalıkları uzmanı doktorlarının erken teşhislerine destek olmak ve kalp ameliyatları ile beraber kalp pili üretimi üzerine teknoloji üretimi yapan firmaların bilgi sahibi olmasını da hedeflemektir.')

column_ent.subheader('**Kalp hastalığı nedir? Hangi etkenlere bağlıdır?**')

column_ent.write('Kalp hastalığı, kalpte meydana gelen ve kalbi etkileyen herhangi bir bozukluğu kapsayan bir terimdir. Kalp hastalığı başlığı altında koroner arter hastalığı gibi kan damar hastalıkları, kalp ritmi problemleri (aritmiler) ve bu hastalıkların yanında doğuştan gelen kalp kusurları yer alır.')

column_ent.markdown('* Sağlık Bakanlığı verilerine göre, ülkemizde 2021 yılı içinde olan ölümlerin yüzde 33.4 kadarı dolaşım sistemi hastalıklarından kaynaklandı. Bu da yaklaşık her üç dakikada bir kişinin ölümü anlamına geliyor. Her yıl yaklaşık 300 bin kişi kalp krizi geçirmektedir. Bu yüzden kalp sağlığı ve kalbi etkileyen herhangi bir durum büyük önem arz etmektedir.')

column_ent.subheader('**Dolaşım sistemi hastalıkları kaynaklı ölümlerin %41,8 kadarını iskemik kalp hastalığı oluşturdu**')
column_ent.markdown("[TÜİK](https://data.tuik.gov.tr/Bulten/Index?p=Olum-ve-Olum-Nedeni-Istatistikleri-2021-45715)")
column_ent.image('media/kalprahatsizligiveri.png')
column_ent.write('Dolaşım sistemi hastalıklarından kaynaklı ölümler alt ölüm nedenlerine göre incelendiğinde, ölenlerin %41,8 kadarını iskemik kalp hastalıklarından, %23,3 ise diğer kalp hastalıklarından, %18,9 serebro-vasküler hastalıklardan öldüğü görüldü.')

column_pro.subheader('**Projenin İçeriği**')
column_pro.markdown('Kardiyovasküler hastalıklar (KVH) dünya genelinde 1 numaralı ölüm nedenidir ve her yıl tahminen 17,9 milyon can almaktadır; bu da dünya genelindeki tüm ölümlerin %31 kadarını oluşturmaktadır. Her 5 KVH ölümünden dördü kalp krizi ve felçten kaynaklanmaktadır ve bu ölümlerin üçte biri 70 yaşın altındaki kişilerde erken gerçekleşmektedir. Kalp yetmezliği, KVH durumunun neden olduğu yaygın bir olaydır ve bu veri kümesi, olası bir kalp hastalığını tahmin etmek için kullanılabilecek 11 özellik içerir.')
column_pro.markdown('Kardiyovasküler hastalığı olan veya yüksek kardiyovasküler risk altında olan kişiler (hipertansiyon, diyabet, hiperlipidemi gibi bir veya daha fazla risk faktörünün varlığı veya halihazırda yerleşmiş hastalık nedeniyle) erken teşhis ve yönetime ihtiyaç duyarlar, bu noktada bir makine öğrenimi modeli çok yardımcı olabilir.')
column_pro.markdown("""
    **Öznitelik Bilgileri**

   - Yaş (Age): hastanın yaşı [yıl]
   - Cinsiyet (Sex): hastanın cinsiyeti [E: Erkek, K: Kadın]
   - ChestPainType : göğüs ağrısı tipi [TA: Tipik Angina, ATA: Atipik Angina, NAP: Anginal Olmayan Ağrı, ASY: Asemptomatik]
   - İstirahatBP (RestingBP) : istirahat kan basıncı [mm Hg]
   - Kolesterol (Cholesterol): serum kolesterolü [mm/dl]
   - Açlık kan şekeri (FastingBS): açlık kan şekeri [1: Açlık kan şekeri > 120 mg/dl ise, 0: aksi halde]
   - İstirahat EKG'si (RestingECG): istirahat elektrokardiyogram sonuçları [Normal: Normal: Normal, ST: ST-T dalga anormalliği olan (T dalga inversiyonları ve/veya > 0,05 mV ST yükselmesi veya çökmesi), LVH: Estes kriterlerine göre olası veya kesin sol ventrikül hipertrofisi gösteren]
   - MaxHR : ulaşılan maksimum kalp atış hızı [60 ile 202 arasında sayısal değer]
   - ExerciseAngina : egzersize bağlı anjina [Y: Evet, N: Hayır]
   - Oldpeak: oldpeak = ST [Depresyonda ölçülen sayısal değer]
   - ST_Slope: en yüksek egzersiz ST segmentinin eğimi [Yukarı: yukarı eğimli, Düz: düz, Aşağı: aşağı eğimli]
   - HeartDisease: çıktı sınıfı [1: kalp hastalığı, 0: Normal]
   """)

column_pro.markdown("""
    **Kaynak**

     Bu veri seti, halihazırda bağımsız olarak mevcut olan ancak daha önce birleştirilmemiş farklı veri setlerinin bir araya getirilmesiyle oluşturulmuştur. Bu veri setinde, 5 kalp veri seti 11 ortak özellik üzerinden birleştirilmiştir ve bu da onu araştırma amacıyla şimdiye kadar mevcut olan en büyük kalp hastalığı veri seti haline getirmektedir. Küratörlüğü için kullanılan beş veri kümesi şunlardır:. 
   - Cleveland: 303 gözlem
   - Macaristan: 294 gözlem
   - İsviçre: 123 gözlem
   - Long Beach VA: 200 gözlem
   - Stalog (Kalp) Veri Seti: 270 gözlem
   - Nihai veri seti: 918 gözlem
   """)

column_pro.write('Kullanılan her veri kümesi, aşağıdaki bağlantıda UCI Makine Öğrenimi Deposundan kalp hastalığı veri kümeleri dizini altında bulunabilir: (https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/)')

# TAB GRAF

tab_graf.subheader('**Veri Setinin Grafiklerle İfade Edilen Hali**')
tab_graf.image(['media/age.jpeg', 'media/sex.jpeg',  'media/maxhr.jpeg', 'media/heartdisease.jpeg', 'media/chestpaintype.jpeg', 'media/restingecg.jpeg', 'media/st_slope.jpeg'])

# TAB END

column_tav, column_cik = tab_end.columns(2, gap='large')

column_tav.subheader('**Çıkarımlar**')
column_tav.markdown("""
- RestingBP: Kalp hastalığı olanlarda ve olmayanlarda da ortalaması birbirine çok yakın olduğu halde Resting BP ile ilintili yeni değişkenler veya değişkenin kendisi modelin en önemli değişkenidir.
- Kolestrelün genel ortalaması hastalık olanlarda daha düşükken Resting BP ile ilintili değerlendirilme yapıldığında bizim ikinci en önemli değişkenimiz oluyor.
- Kolestrol kalp hastalığında tahmin edildiği gibi yine en önemli değişkenimiz.
- Hastalık görünen kişilerde Age (Yaş) oranı tahmin edildiği üzere daha yüksek ve kolestrol ile yeni değişken oluşturulduğunda en önemli değişkenler sıralamasında ilk beşte.
- MaxHR, kalp hastası olanlarda daha düşükken bu değişken RestingBP ile birlikte değerlendirildiğinde bizim en önemli değişkenimiz haline geliyor.""")

column_cik.subheader('**Tavsiyeler**')
column_cik.markdown("""
- RestingBP'yi dengede tutmak için sağlıklı ve dengeli beslenmek, sodyum ile beraber işlenmiş gıdalardan uzak durmak, azaltılmış alkol ve kafein tüketimi, stres yönetiminin yanında düzenli kan basıncı kontrolü konularına dikkat etmek gerekiyor.
- Kolestrol için ise tuz tüketiminin azaltılması, yine sağlıklı beslenmek, alkol ve sigarada azaltmaya gitmek ve ideal kiloyu korumak gerekiyor.""")
column_cik.subheader('**Voting pipeline oluşturulduktan sonra başarı metrikleri**')
column_cik.image(['media/acc.png'])

model = get_model()

df=pd.read_csv('files/heart.csv')
column_tav.write(df)


# TAB TEAM

column_vht, column_names = tab_team.columns(2, gap='large')

column_vht.image('media/vht.jpeg')
column_names.title('- Yasemin Derya Dilli')
column_names.write('<img src="https://cdn1.iconfinder.com/data/icons/logotypes/32/circle-linkedin-512.png" alt="Linkedin" width="25">', unsafe_allow_html=True)
column_names.markdown("[buraya tıklayın](https://www.linkedin.com/in/yaseminderyadilli/)")
column_names.title('- Mustafa Berk Kuşdemir')
column_names.write('<img src="https://cdn1.iconfinder.com/data/icons/logotypes/32/circle-linkedin-512.png" alt="Linkedin" width="25">', unsafe_allow_html=True)
column_names.markdown("[buraya tıklayın](https://www.linkedin.com/in/mbkusdemir/)")
column_names.title('- Fatih Külcü')
column_names.write('<img src="https://cdn1.iconfinder.com/data/icons/logotypes/32/circle-linkedin-512.png" alt="Linkedin" width="25">', unsafe_allow_html=True)
column_names.markdown("[buraya tıklayın](https://www.linkedin.com/in/fatih-k%C3%BClc%C3%BC-b4b80717a/)")
column_names.title('- Tutku Toprak')
column_names.write('<img src="https://cdn1.iconfinder.com/data/icons/logotypes/32/circle-linkedin-512.png" alt="Linkedin" width="25">', unsafe_allow_html=True)
column_names.markdown("[buraya tıklayın](https://www.linkedin.com/in/tutku-toprak/)")




