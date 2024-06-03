import streamlit as st
import pandas as pd
import math

def goster_matematiksel_temel():
    # Başlık ve Giriş
    st.title("🔍 McNemar Testinin Matematiksel Temeli")

    # Chi-Kare Testi ve McNemar Testi Arasındaki İlişki
    st.header("📊 Chi-Kare Testi ve McNemar Testi Arasındaki İlişki")
    st.write("""
    Chi-kare testi ve McNemar testi, kategorik verileri analiz etmek için kullanılır. Ancak, Chi-kare testi bağımsız gruplar arasındaki farkları incelerken, McNemar testi aynı grubun farklı zamanlardaki sonuçlarını karşılaştırır.
    """)

    st.subheader("Chi-Kare Testi:")
    st.markdown("""
    - İki bağımsız veri kümesi arasındaki ilişkiyi test eder.
    - Örneğin, iki farklı grubun belirli bir ürünü tercih edip etmediğini test eder.
    """)

    st.subheader("McNemar Testi:")
    st.markdown("""
    - Aynı grubun iki farklı zaman veya koşulda ölçülen sonuçlarını karşılaştırır.
    """)

    # Chi-Kare İstatistiğinin Hesaplanması
    st.header("📐 Chi-Kare İstatistiğinin Hesaplanması")
    st.write("""
    McNemar testinde, chi-kare istatistiği şu formülle hesaplanır:
    """)

    st.latex(r'''
    \chi^2 = \frac{(b - c)^2}{b + c}
    ''')

    st.write("""
    Burada:
    - **b**: İlk koşulda "Evet", ikinci koşulda "Hayır" olan gözlemler.
    - **c**: İlk koşulda "Hayır", ikinci koşulda "Evet" olan gözlemler.
    """)

    # Örnek Tablo ve Hesaplama
    st.subheader("Örnek: Bir eğitim programının etkisini değerlendirme")
    data = {'Program Sonrası: Anladı': [20, 5], 'Program Sonrası: Anlamadı': [10, 15]}
    df = pd.DataFrame(data, index=['Program Öncesi: Anladı', 'Program Öncesi: Anlamadı'])
    st.table(df)

    st.write("""
    Bu tabloda:
    - **b = 10** (Program öncesi "Anladı", program sonrası "Anlamadı")
    - **c = 5** (Program öncesi "Anlamadı", program sonrası "Anladı")
    """)

    chi_square = (10 - 5)**2 / (10 + 5)
    st.write(f"Chi-kare istatistiği hesaplama: χ² = (10 - 5)² / (10 + 5) = {chi_square:.2f}")

    st.latex(r'''
    \chi^2 = \frac{(10 - 5)^2}{10 + 5} = \frac{25}{15} \approx 1.67
    ''')

    st.write("Bu chi-kare istatistiği, p-değerini hesaplamak için kullanılır.")

    # Kesin McNemar Testi ve Binom Testi
    st.header("🎯 Kesin McNemar Testi ve Binom Testi")
    st.write("""
    Küçük örneklem boyutlarında McNemar testi binom testi olarak yapılabilir. Bu yöntem, daha doğru sonuçlar verir.
    """)

    st.subheader("Örnek: Binom Testi ile Kesin McNemar Testi")
    st.write("""
    Binom testi, b ve c hücrelerindeki farkların anlamlı olup olmadığını belirlemek için kullanılır. Örneğin:
    """)

    st.code("""
from scipy.stats import binom_test

# b ve c değerleri
b = 10
c = 5

# Binom testi
p_value = binom_test([b, c])
print('p-value:', p_value)
    """, language='python')

    st.write("""
    Bu test, küçük örneklem boyutlarında daha doğru sonuçlar verir.
    """)
