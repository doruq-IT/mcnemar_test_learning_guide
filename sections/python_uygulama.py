import streamlit as st
import numpy as np
from scipy.stats import binomtest, chi2

def goster_python_uygulama():
    st.header("🐍 Python ile McNemar Testi Uygulama")
    st.write("""
    McNemar testini Python'da nasıl uygulayacağınızı görelim:
    """)

    # 2x2 kontenjans tablosu verileri
    table = np.array([[20, 10], [5, 15]])
    b = table[0, 1]
    c = table[1, 0]

    # Chi-kare istatistiği hesaplama
    chi_square = (b - c) ** 2 / (b + c)
    st.write(f"Chi-square Statistic: {chi_square:.2f}")

    # P-değerini hesaplama (Chi-kare dağılımı kullanarak)
    p_value_chi2 = chi2.sf(chi_square, 1)
    st.write(f"P-değeri (Chi-square): {p_value_chi2:.2f}")

    # Binom testi ile kesin McNemar testi
    p_value_binom = binomtest(b, n=b+c, p=0.5, alternative='two-sided').pvalue
    st.write(f"P-değeri (Binom Testi): {p_value_binom:.2f}")
