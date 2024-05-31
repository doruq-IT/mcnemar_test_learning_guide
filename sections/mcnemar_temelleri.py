import streamlit as st
import pandas as pd

def goster_temeller():
    # Başlık ve Giriş
    st.title("📘 McNemar Testinin Temelleri")

    # Bölüm 1: Bağımlı Örnekler ve Eşleştirilmiş Veriler
    st.header("🔍 Bağımlı Örnekler ve Eşleştirilmiş Veriler")
    st.write("""
    McNemar testi, bağımlı örnekler ve eşleştirilmiş verilerle çalışır. Bağımlı örnekler, aynı grubun iki farklı zamanda veya iki farklı koşul altında test edilmesi anlamına gelir. Eşleştirilmiş veriler ise, aynı bireylerin iki farklı ölçümdeki sonuçlarını karşılaştırmak için kullanılır.
    """)

    st.subheader("Bağımlı Örnekler:")
    st.markdown("""
    - Bir grubun belirli bir tedavi öncesi ve sonrası durumu.
    - Aynı bireylerin farklı zamanlarda test edilmesi.
    """)

    st.subheader("Eşleştirilmiş Veriler:")
    st.markdown("""
    - İki farklı testin aynı bireyler üzerindeki sonuçları.
    - Aynı bireylerin iki farklı koşul altındaki davranışları.
    """)

    st.write("""
    **Örnek:** Bir eğitim programının etkisini değerlendirdiğimizi düşünelim. Öğrencilerin program öncesi ve sonrası bilgilerini "Anladı/Anlamadı" olarak kaydediyoruz.
    """)

    # Eğitim Programı Kontenjans Tablosu
    st.subheader("Eğitim Programı Kontenjans Tablosu:")
    data2 = {'Program Sonrası: Anladı': [20, 5], 'Program Sonrası: Anlamadı': [10, 15]}
    df2 = pd.DataFrame(data2, index=['Program Öncesi: Anladı', 'Program Öncesi: Anlamadı'])
    st.table(df2)

    st.write("""
    Bu tablo, öğrencilerin eğitim programı öncesi ve sonrası bilgilerini karşılaştırmak için kullanılır.
    """)

    # Bölüm 3: Örnek Durumlar (Örnekler ve Senaryolar)
    st.header("📚 Örnek Durumlar (Örnekler ve Senaryolar)")

    # Örnek 1: Tıp ve Sağlık Araştırmaları
    st.subheader("Örnek 1: Tıp ve Sağlık Araştırmaları")
    st.write("""
    Bir grup hastanın yeni bir ilaç tedavisi öncesi ve sonrası sağlık durumunu değerlendiriyoruz. Hastaların tedavi öncesi ve sonrası "İyileşti/İyileşmedi" olarak kaydedilen durumları McNemar testi ile analiz edilebilir.
    """)

    # Tıp ve Sağlık Araştırmaları Kontenjans Tablosu
    st.subheader("Tedavi Öncesi ve Sonrası Kontenjans Tablosu:")
    data3 = {'Tedavi Sonrası: İyileşti': [40, 5], 'Tedavi Sonrası: İyileşmedi': [10, 45]}
    df3 = pd.DataFrame(data3, index=['Tedavi Öncesi: İyileşti', 'Tedavi Öncesi: İyileşmedi'])
    st.table(df3)

    # Örnek 2: Psikoloji ve Eğitim
    st.subheader("Örnek 2: Psikoloji ve Eğitim")
    st.write("""
    Bir terapi programının depresyon üzerindeki etkisini ölçmek için katılımcıların program öncesi ve sonrası depresyon seviyelerini değerlendiriyoruz. Katılımcıların depresyon seviyeleri "Depresyon Yok/Depresyon Var" olarak kaydedilir.
    """)

    # Psikoloji ve Eğitim Kontenjans Tablosu
    st.subheader("Terapi Öncesi ve Sonrası Kontenjans Tablosu:")
    data4 = {'Program Sonrası: Depresyon Yok': [30, 5], 'Program Sonrası: Depresyon Var': [10, 15]}
    df4 = pd.DataFrame(data4, index=['Program Öncesi: Depresyon Yok', 'Program Öncesi: Depresyon Var'])
    st.table(df4)

    # Örnek 3: Sosyal Bilimler
    st.subheader("Örnek 3: Sosyal Bilimler")
    st.write("""
    Bir farkındalık kampanyasının etkisini ölçmek için insanların kampanya öncesi ve sonrası belirli bir konu hakkındaki görüşlerini değerlendiriyoruz. Görüşler "Bilinçli/Bilinçsiz" olarak kaydedilir.
    """)

    # Sosyal Bilimler Kontenjans Tablosu
    st.subheader("Kampanya Öncesi ve Sonrası Kontenjans Tablosu:")
    data5 = {'Kampanya Sonrası: Bilinçli': [25, 10], 'Kampanya Sonrası: Bilinçsiz': [15, 50]}
    df5 = pd.DataFrame(data5, index=['Kampanya Öncesi: Bilinçli', 'Kampanya Öncesi: Bilinçsiz'])
    st.table(df5)

    st.write("""
    Bu örnekler, McNemar testinin farklı alanlarda nasıl kullanılabileceğini ve sonuçların nasıl yorumlanabileceğini göstermektedir. Bu test, özellikle bağımlı örnekler ve eşleştirilmiş verilerle çalışırken ikili sonuçları karşılaştırmak için çok uygundur.
    """)
