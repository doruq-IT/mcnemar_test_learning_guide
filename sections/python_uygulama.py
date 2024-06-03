import streamlit as st
import numpy as np
import pandas as pd
from scipy.stats import binomtest, chi2

def goster_python_uygulama():
    st.header("🐍 Python ile McNemar Testi Uygulama")
    st.write("""
    McNemar testini Python'da nasıl uygulayacağınızı görelim. Bu test, özellikle aynı grubun iki farklı zamanda veya koşulda ölçülen ikili sonuçlarını karşılaştırmak için kullanılır.
    """)

    # 2x2 kontenjans tablosu verileri
    st.subheader("Örnek 2x2 Kontenjans Tablosu")
    table = np.array([[20, 10], [5, 15]])
    df = pd.DataFrame(table, columns=["Koşul B: Evet", "Koşul B: Hayır"], index=["Koşul A: Evet", "Koşul A: Hayır"])
    st.table(df)

    b = table[0, 1]  # 10
    c = table[1, 0]  # 5

    # Chi-kare istatistiği hesaplama
    st.write("Chi-kare istatistiği hesaplama adımları:")
    st.write(f"b = {b}")
    st.write(f"c = {c}")
    st.write(f"(b - c) = ({b} - {c}) = {b - c}")
    st.write(f"(b - c)^2 = ({b - c})^2 = {(b - c) ** 2}")
    st.write(f"b + c = {b} + {c} = {b + c}")
    chi_square = (b - c) ** 2 / (b + c)
    st.write(f"Chi-square İstatistiği = ({b - c})^2 / ({b + c}) = {(b - c) ** 2} / {b + c} = {chi_square:.2f}")

    # P-değerini hesaplama (Chi-kare dağılımı kullanarak)
    p_value_chi2 = chi2.sf(chi_square, 1)
    st.write(f"P-değeri (Chi-square): {p_value_chi2:.2f}")

    # Binom testi ile kesin McNemar testi
    st.write("Binom Testi hesaplama adımları:")
    st.write(f"b = {b}, c = {c}")
    st.write(f"n = b + c = {b} + {c} = {b + c}")
    p_value_binom = binomtest(b, n=b+c, p=0.5, alternative='two-sided').pvalue
    st.write(f"P-değeri (Binom Testi): {p_value_binom:.2f}")