# sections/python_uygulama.py
import streamlit as st
import numpy as np
from scipy.stats import chi2, binomtest

def goster_python_uygulama():
    st.subheader("Gerekli Kütüphanelerin Kurulumu ve İmport Edilmesi")
    st.write("""
    Bu uygulamada numpy ve scipy kütüphanelerine ihtiyacımız var. Kurulum için:
    ```bash
    pip install numpy scipy
    ```
    """)

    st.subheader("Kontenjans Tablosunun Oluşturulması")
    st.write("""
    Verilerimizi 2x2 kontenjans tablosu olarak düzenleyelim:
    ```python
    table = np.array([[20, 10], [5, 15]])
    ```
    """)

    st.subheader("Chi-Kare İstatistiği ile McNemar Testi")
    st.write("""
    Chi-kare istatistiğini hesaplayalım:
    ```python
    b = table[0, 1]
    c = table[1, 0]
    chi_square = (b - c) ** 2 / (b + c)
    print('Chi-square Statistic:', chi_square)
    ```
    """)

    st.subheader("Kesin McNemar Testi (Binom Testi)")
    st.write("""
    Binom testi ile p-değerini hesaplayalım:
    ```python
    p_value = binomtest([b, c], alternative='two-sided').pvalue
    print('p-value:', p_value)
    ```
    """)
