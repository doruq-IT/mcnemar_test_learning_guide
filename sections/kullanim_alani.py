import streamlit as st
import pandas as pd
from navigation import next_button

def goster_kullanim_alani():
    # Başlık ve Giriş
    st.title("📌 McNemar Testinin Kullanım Alanları")
    st.write("""
    McNemar testi, birçok farklı alanda kullanılabilir. İşte birkaç örnek:
    """)

    # Bölüm 1: Tıp ve Sağlık Araştırmaları
    st.header("🏥 Tıp ve Sağlık Araştırmaları")
    st.write("""
    Bir tedavinin veya müdahalenin etkisini değerlendirmek için kullanılır. Örneğin, bir ilacın etkinliğini belirlemek için hastaların tedavi öncesi ve sonrası durumları (iyileşenler ve iyileşmeyenler) karşılaştırılabilir.
    """)

    # Tıp ve Sağlık Araştırmaları Tablosu
    st.subheader("Örnek: Bir ilacın etkinliğini değerlendirme")
    st.write("""
    Bir ilacın etkinliğini değerlendirmek için 100 hasta üzerinde yapılan bir çalışmada, ilacın kullanımından önce ve sonra hastaların durumları şu şekilde kaydedilebilir:
    """)
    data1 = {'Tedavi Sonrası: İyileşti': [40, 5], 'Tedavi Sonrası: İyileşmedi': [10, 45]}
    df1 = pd.DataFrame(data1, index=['Tedavi Öncesi: İyileşti', 'Tedavi Öncesi: İyileşmedi'])
    st.table(df1)
    st.write("Bu tabloyu kullanarak, ilacın etkinliğini McNemar testi ile değerlendirebilirsiniz.")

    # Bölüm 2: Psikoloji ve Eğitim
    st.header("📘 Psikoloji ve Eğitim")
    st.write("""
    Bir eğitim veya terapi programının etkisini değerlendirmek için kullanılır. Örneğin, bir terapi programının depresyon seviyeleri üzerindeki etkisini ölçmek için katılımcıların program öncesi ve sonrası durumları karşılaştırılabilir.
    """)

    # Psikoloji ve Eğitim Tablosu
    st.subheader("Örnek: Bir terapi programının depresyon üzerindeki etkisini değerlendirme")
    st.write("""
    Bir terapi programının depresyon üzerindeki etkisini değerlendirmek için, program öncesi ve sonrası katılımcıların depresyon seviyeleri şu şekilde kaydedilebilir:
    """)
    data2 = {'Program Sonrası: Depresyon Yok': [30, 5], 'Program Sonrası: Depresyon Var': [10, 15]}
    df2 = pd.DataFrame(data2, index=['Program Öncesi: Depresyon Yok', 'Program Öncesi: Depresyon Var'])
    st.table(df2)
    st.write("Bu tabloyu kullanarak, programın depresyon üzerindeki etkisini McNemar testi ile değerlendirebilirsiniz.")

    # Bölüm 3: Sosyal Bilimler
    st.header("🌐 Sosyal Bilimler")
    st.write("""
    Sosyal araştırmalarda, bir müdahalenin veya kampanyanın etkisini değerlendirmek için kullanılır. Örneğin, bir farkındalık kampanyasının etkisini ölçmek için insanların kampanya öncesi ve sonrası görüşleri karşılaştırılabilir.
    """)

    # Sosyal Bilimler Tablosu
    st.subheader("Örnek: Bir farkındalık kampanyasının etkisini değerlendirme")
    st.write("""
    Bir farkındalık kampanyasının etkisini değerlendirmek için, kampanya öncesi ve sonrası insanların bir konu hakkındaki görüşleri şu şekilde kaydedilebilir:
    """)
    data3 = {'Kampanya Sonrası: Bilinçli': [25, 10], 'Kampanya Sonrası: Bilinçsiz': [15, 50]}
    df3 = pd.DataFrame(data3, index=['Kampanya Öncesi: Bilinçli', 'Kampanya Öncesi: Bilinçsiz'])
    st.table(df3)
    st.write("Bu tabloyu kullanarak, kampanyanın etkisini McNemar testi ile değerlendirebilirsiniz.")

    # Bölüm 4: Pazarlama Araştırmaları
    st.header("📊 Pazarlama Araştırmaları")
    st.write("""
    Bir reklam kampanyasının veya ürün değişikliğinin tüketici algısı üzerindeki etkisini değerlendirmek için kullanılır. Örneğin, bir ürünün yeni ambalaj tasarımının tüketici algısı üzerindeki etkisini ölçmek için, tüketicilerin yeni ve eski ambalaj hakkındaki görüşleri karşılaştırılabilir.
    """)

    # Pazarlama Araştırmaları Tablosu
    st.subheader("Örnek: Bir ürünün yeni ambalaj tasarımının etkisini değerlendirme")
    st.write("""
    Bir ürünün yeni ambalaj tasarımının etkisini değerlendirmek için, tüketicilerin eski ve yeni ambalaj hakkındaki görüşleri şu şekilde kaydedilebilir:
    """)
    data4 = {'Yeni Ambalaj: Beğendi': [40, 10], 'Yeni Ambalaj: Beğenmedi': [20, 30]}
    df4 = pd.DataFrame(data4, index=['Eski Ambalaj: Beğendi', 'Eski Ambalaj: Beğenmedi'])
    st.table(df4)
    st.write("Bu tabloyu kullanarak, yeni ambalajın tüketici algısı üzerindeki etkisini McNemar testi ile değerlendirebilirsiniz.")
