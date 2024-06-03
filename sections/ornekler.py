import streamlit as st
import pandas as pd

def goster_ornekler():
    st.header("📚 Örnekler")
    st.write("""
    McNemar testinin farklı kullanım alanlarına örnekler:
    """)

    # Eğitim Programı Örneği
    st.subheader("Örnek 1: Eğitim Programının Etkisi")
    st.write("""
    Bir eğitim programının öğrenci başarıları üzerindeki etkisini değerlendirmek için program öncesi ve sonrası başarı durumlarını karşılaştırabiliriz.
    """)

    # Örnek tablo
    data_egitim = {'Program Sonrası: Anladı': [20, 5], 'Program Sonrası: Anlamadı': [10, 15]}
    df_egitim = pd.DataFrame(data_egitim, index=['Program Öncesi: Anladı', 'Program Öncesi: Anlamadı'])
    st.table(df_egitim)

    # Tıbbi Tedavi Örneği
    st.subheader("Örnek 2: Tıbbi Tedavinin Etkisi")
    st.write("""
    Bir tıbbi tedavinin hasta sağlık durumları üzerindeki etkisini değerlendirmek için tedavi öncesi ve sonrası sağlık durumlarını karşılaştırabiliriz.
    """)

    # Örnek tablo
    data_tedavi = {'Tedavi Sonrası: İyileşti': [30, 5], 'Tedavi Sonrası: İyileşmedi': [10, 15]}
    df_tedavi = pd.DataFrame(data_tedavi, index=['Tedavi Öncesi: İyileşti', 'Tedavi Öncesi: İyileşmedi'])
    st.table(df_tedavi)

    # Psikolojik Terapi Örneği
    st.subheader("Örnek 3: Psikolojik Terapi")
    st.write("""
    Bir psikolojik terapi programının depresyon üzerindeki etkisini değerlendirmek için terapi öncesi ve sonrası depresyon durumlarını karşılaştırabiliriz.
    """)

    # Örnek tablo
    data_terapi = {'Terapi Sonrası: Depresyon Yok': [25, 5], 'Terapi Sonrası: Depresyon Var': [15, 5]}
    df_terapi = pd.DataFrame(data_terapi, index=['Terapi Öncesi: Depresyon Yok', 'Terapi Öncesi: Depresyon Var'])
    st.table(df_terapi)

    st.write("""
    Bu örnekler, McNemar testinin farklı alanlarda nasıl kullanılabileceğini ve sonuçların nasıl yorumlanabileceğini göstermektedir.
    """)

