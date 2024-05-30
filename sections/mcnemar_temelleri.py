# sections/mcnemar_temelleri.py
import streamlit as st

def goster_temeller():
    st.subheader("Bağımlı Örnekler ve Eşleştirilmiş Veriler")
    st.write("""
    McNemar testi, bağımlı örnekler ve eşleştirilmiş verilerle çalışır. Bağımlı örnekler, aynı grubun iki farklı zamanda veya iki farklı koşul altında test edilmesi anlamına gelir.
    """)
    st.subheader("İkili Sonuçlar ve 2x2 Kontenjans Tablosu")
    st.write("""
    McNemar testi, ikili sonuçlarla çalışır. İkili sonuçlar, iki olası durumu ifade eder: "Evet/Hayır", "Başarılı/Başarısız", "Anladı/Anlamadı" gibi. Bu sonuçlar, 2x2 kontenjans tablosunda gösterilir.
    """)
