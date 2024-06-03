import streamlit as st
import pandas as pd

def goster_ornekler():
    st.header("📚 Örnekler")
    st.write("""
    McNemar testinin farklı kullanım alanlarına örnekler:
    - **Eğitim Programı:** Program öncesi ve sonrası öğrenci başarılarını karşılaştırmak.
    - **Tıbbi Tedavi:** Tedavi öncesi ve sonrası hasta sağlık durumlarını değerlendirmek.
    """)

    # Örnek tablo
    data = {'Program Sonrası: Anladı': [20, 5], 'Program Sonrası: Anlamadı': [10, 15]}
    df = pd.DataFrame(data, index=['Program Öncesi: Anladı', 'Program Öncesi: Anlamadı'])
    st.table(df)
