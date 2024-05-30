import streamlit as st
import pandas as pd
import math
from navigation import next_button

def goster_matematiksel_temel():
    # Başlık ve Giriş
    st.title("🔍 McNemar Testinin Matematiksel Temeli")

    # Chi-Kare Testi ve McNemar Testi Arasındaki İlişki
    st.header("📊 Chi-Kare Testi ve McNemar Testi Arasındaki İlişki")
    st.write("""
    Chi-kare testi ve McNemar testi, her ikisi de kategorik verileri analiz etmek için kullanılan istatistiksel testlerdir, ancak farklı amaçlara hizmet ederler.
    """)

    st.subheader("Chi-Kare Testi:")
    st.markdown("""
    - İki bağımsız kategorik veri kümesi arasındaki ilişkiyi test eder.
    - Örneğin, iki farklı grubun belirli bir ürünü tercih edip etmediğini test etmek için kullanılır.
    """)

    st.subheader("McNemar Testi:")
    st.markdown("""
    - Bağımlı iki ikili veri kümesi arasındaki oranları karşılaştırmak için kullanılır.
    - Aynı bireylerin iki farklı zamanda veya koşulda ölçülen sonuçlarını karşılaştırır.
    """)

    st.write("Özetle, chi-kare testi bağımsız örnekler için kullanılırken, McNemar testi bağımlı örnekler için kullanılır.")

    # Chi-Kare İstatistiğinin Hesaplanması
    st.header("📐 Chi-Kare İstatistiğinin Hesaplanması")
    st.write("""
    McNemar testinde, chi-kare istatistiği özel bir formülle hesaplanır. Bu formül, b ve c hücrelerindeki farkların anlamlı olup olmadığını belirlemek için kullanılır.
    """)

    st.latex(r'''
    \chi^2 = \frac{(b - c)^2}{b + c}
    ''')

    st.write("""
    Burada:
    - **b**: İlk koşulda "Evet", ikinci koşulda "Hayır" olan gözlemlerin sayısı.
    - **c**: İlk koşulda "Hayır", ikinci koşulda "Evet" olan gözlemlerin sayısı.
    Bu formül, b ve c hücrelerindeki değişiklikleri değerlendirir. Eğer b ve c hücrelerindeki değerler arasında büyük bir fark varsa, bu testin sonucu anlamlı olabilir.
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
    McNemar testi, özellikle küçük örneklem boyutlarında (örneğin, b + c < 25) kesin test olarak da yapılabilir. Bu durumda binom testi kullanılır. Binom testi, b ve c hücrelerindeki farkların anlamlı olup olmadığını belirlemek için binom dağılımını kullanır.
    """)

    st.subheader("Örnek: Binom Testi ile Kesin McNemar Testi")
    st.write("""
    Kesin McNemar testinde, b ve c değerleri kullanılarak binom testi yapılır. Örneğin:
    - **b = 10** ve **c = 5** ise, binom testi şu şekilde yapılır:
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
    Bu test, küçük örneklem boyutlarında daha doğru sonuçlar verir. Özetle, McNemar testi için chi-kare istatistiği ve kesin McNemar testi (binom testi) iki farklı yöntemdir. Chi-kare istatistiği, daha büyük örneklem boyutları için uygundur, ancak küçük örneklem boyutlarında kesin McNemar testi daha doğrudur.
    """)
