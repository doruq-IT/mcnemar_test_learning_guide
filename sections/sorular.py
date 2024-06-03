import streamlit as st

def goster_sorular():
    # Başlık ve Giriş
    st.title("❓ Sıkça Sorulan Sorular (SSS)")

    # McNemar Testi ile İlgili Yaygın Sorular ve Yanıtları
    st.header("📋 McNemar Testi ile İlgili Sorular")

    # Soru 1
    st.subheader("McNemar testi nedir ve ne zaman kullanılır?")
    st.write("""
    McNemar testi, aynı bireylerin iki farklı zaman veya koşuldaki ikili sonuçlarını karşılaştırmak için kullanılır. Örneğin, tedavi öncesi ve sonrası sağlık durumu.
    """)

    # Soru 2
    st.subheader("McNemar testi ile chi-kare testi arasındaki fark nedir?")
    st.write("""
    Chi-kare testi bağımsız grupları, McNemar testi ise bağımlı grupları karşılaştırır.
    """)

    # Soru 3
    st.subheader("McNemar testi nasıl hesaplanır?")
    st.write("""
    McNemar testi şu formülle hesaplanır:
    """)
    st.latex(r'''
    \chi^2 = \frac{(b - c)^2}{b + c}
    ''')

    # Soru 4
    st.subheader("P-değeri nedir ve nasıl yorumlanır?")
    st.write("""
    P-değeri, sonuçların rastlantısal olup olmadığını belirler. Genellikle 0.05'ten küçükse, fark anlamlıdır.
    """)

    # Soru 5
    st.subheader("McNemar testi için hangi tür veriler gereklidir?")
    st.write("""
    İkili sonuçlar ("Evet/Hayır") ve bağımlı örnekler gereklidir.
    """)

    # Soru 6
    st.subheader("Küçük örneklem boyutlarıyla nasıl çalışılır?")
    st.write("""
    Küçük örneklemler için kesin McNemar testi (binom testi) kullanılır.
    """)

    # Soru 7
    st.subheader("McNemar testini Python ile nasıl uygulayabilirim?")
    st.write("""
    McNemar testini Python ile uygulamak için numpy ve scipy kütüphanelerini kullanabilirsiniz. Örnek kod:
    """)
    st.code("""
import numpy as np
from scipy.stats import binomtest, chi2

# 2x2 kontenjans tablosu
table = np.array([[20, 10], [5, 15]])

# b ve c değerleri
b = table[0, 1]
c = table[1, 0]

# Chi-kare istatistiği
chi_square = (b - c) ** 2 / (b + c)
p_value_chi2 = chi2.sf(chi_square, 1)

# Binom testi
p_value_binom = binomtest([b, c])

print('Chi-square Statistic:', chi_square)
print('p-value (Chi-square):', p_value_chi2)
print('p-value (Binom Test):', p_value_binom)
    """, language='python')

    st.write("""
    Bu sıkça sorulan sorular ve yanıtları, McNemar testi hakkında temel bilgileri öğrenmenize yardımcı olacaktır.
    """)

