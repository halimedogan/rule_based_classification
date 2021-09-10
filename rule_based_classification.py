### HELLOOO FIRST PROJECT ###
# Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama #
### GOREV-1 ###
#persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.
import pandas as pd
df = pd.read_csv(r"C:\Users\ASUS.HALIMEASUS\Desktop\hafta_2\persona.csv")
def check_df(dataframe, head=5):
    print("##################### Shape #####################")
    print(dataframe.shape)

    print("##################### Types #####################")
    print(dataframe.dtypes)

    print("##################### Head #####################")
    print(dataframe.head(head))

    print("##################### Tail #####################")
    print(dataframe.tail(head))

    print("##################### NA #####################")
    print(dataframe.isnull().sum())

    print("##################### Info #####################")
    print(dataframe.info())

    print("##################### Quantiles #####################")
    print(dataframe.quantile([0, 0.05, 0.50, 0.95, 0.99, 1]).T)

check_df(df)

#Kaç unique SOURCE vardır? Frekansları nedir?
df.SOURCE.nunique()
df.SOURCE.value_counts()
#Kaç unique PRICE vardır?
df.PRICE.nunique()
#Hangi PRICE'dan kaçar tane satış gerçekleşmiş?
df.groupby('PRICE').agg({'PRICE': 'count'})
#Hangi ülkeden kaçar tane satış olmuş?
df.groupby('COUNTRY').agg({'PRICE': 'count'})
#Ülkelere göre satışlardan toplam ne kadar kazanılmış?
df.groupby('COUNTRY').agg({'PRICE': 'sum'})
#SOURCE türlerine göre göre satış sayıları nedir?
df.groupby('SOURCE').agg({'PRICE': 'count'})
#Ülkelere göre PRICE ortalamaları nedir?
df.groupby('COUNTRY').agg({'PRICE': 'mean'})
#SOURCE'lara göre PRICE ortalamaları nedir?
df.groupby('SOURCE').agg({'PRICE': 'mean'})
#COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?
df.groupby(['COUNTRY', 'SOURCE']).agg({'PRICE': 'mean'})

### GOREV-2 ###
#COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?
df.groupby(['COUNTRY', 'SOURCE']).agg({'PRICE': 'mean'})

### GOREV-3 ###
#Çıktıyı PRICE’a göre sıralayınız.
agg_df = df.groupby(['COUNTRY', 'SOURCE', 'SEX', 'AGE']).agg({'PRICE': 'mean'}).sort_values('PRICE', ascending=False)

### GOREV-4 ###
#Index’te yer alan isimleri değişken ismine çeviriniz.
agg_df.reset_index(inplace=True)
### GOREV-5 ###
#age değişkenini kategorik değişkene çeviriniz ve agg_df’e ekleyiniz.
agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"], bins=[0, 18, 23, 30, 40, 66], labels=["0_18", "19_23", "24_30", "31_40", "41_66"])
agg_df.head()
### GOREV-6 ###
#Yeni seviye tabanlı müşterileri (persona) tanımlayınız.
agg_df["customers_level_based"] = [str(row[0]).upper() + "_" + str(row[1]).upper() + "_" + str(row[2]).upper() + "_" + str(row[5]).upper()for row in agg_df.values]
agg_df = agg_df.loc[:,["customers_level_based", "PRICE"]]
agg_df = agg_df.groupby("customers_level_based").agg({"PRICE":"mean"})
agg_df.head()
### GOREV-7 ###
#Yeni müşterileri (personaları) segmentlere ayırınız.
agg_df['SEGMENT'] = pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])
agg_df.groupby("SEGMENT").agg({"PRICE": ["mean", "min", "max", "sum"]})
c_segment = agg_df.loc[(agg_df["SEGMENT"] == "C"),  "SEGMENT"]
c_segment.value_counts()
### GOREV-8 ###
#Yeni gelen müşterileri segmentlerine göre sınıflandırınız ve ne kadar gelir getirebileceğini tahmin ediniz.agg_df[agg_df["customers_level_based"] == new_user2]
new_user = 'tur_android_female_25_40'
new_user_2 = 'fra_ios_female_25_40'
#33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?
agg_df[agg_df["customers_level_based"] == new_user1]
agg_df.loc[agg_df["customers_level_based"] == new_user, ["PRICE","SEGMENT"]]
agg_df.loc[agg_df["customers_level_based"] == new_user, ["PRICE","SEGMENT"]].agg({"PRICE":"mean"})
#35 yaşında IOS kullanan bir Fransız kadını hangi segmente ve ortalama ne kadar gelir kazandırması beklenir?
agg_df[agg_df["customers_level_based"] == new_user2]
agg_df.loc[agg_df["customers_level_based"] == new_user_2, ["PRICE","SEGMENT"]]
agg_df.loc[agg_df["customers_level_based"] == new_user_2, ["PRICE","SEGMENT"]].agg({"PRICE":"mean"})