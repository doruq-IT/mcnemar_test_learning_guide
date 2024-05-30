import streamlit as st
import numpy as np
from scipy.stats import binomtest, chi2
from navigation import next_button

def goster_python_uygulama():
    # Başlık ve Giriş
    st.title("💻 McNemar Testinin Python ile Uygulanması")

    # Gerekli Kütüphanelerin Kurulumu ve İmport Edilmesi
    st.header("🔧 Gerekli Kütüphanelerin Kurulumu ve İmport Edilmesi")
    st.write("""
    Python'da McNemar testi yapabilmek için bazı kütüphaneleri kurmamız ve import etmemiz gerekecek. Ancak, bu bölümde kütüphane kullanmadan nasıl yapacağımızı göstereceğiz. Yine de, veri manipülasyonu için numpy ve istatistiksel hesaplamalar için scipy kütüphanelerine ihtiyaç duyabiliriz. Bu kütüphaneleri kurmak için aşağıdaki komutları kullanabilirsiniz:
    """)
    st.code("pip install numpy scipy", language='bash')

    st.write("Daha sonra bu kütüphaneleri import edelim:")
    st.code("""
import numpy as np
from scipy.stats import binomtest
    """, language='python')

    # Kontenjans Tablosunun Oluşturulması
    st.header("📊 Kontenjans Tablosunun Oluşturulması")
    st.write("""
    İlk olarak, verilerimizi 2x2 kontenjans tablosu olarak düzenlememiz gerekiyor. Örneğin, bir eğitim programının öncesi ve sonrası sonuçlarını karşılaştıralım. Aşağıdaki verileri kullanacağız:
    """)

    st.write("""
    | Program Sonrası: Anladı | Program Sonrası: Anlamadı |
    |-------------------------|---------------------------|
    | **Program Öncesi: Anladı** | 20 | 10 |
    | **Program Öncesi: Anlamadı** | 5 | 15 |
    """)

    st.write("Bu tabloyu Python'da oluşturmak için:")
    st.code("""
# 2x2 kontenjans tablosu verileri
table = np.array([[20, 10],
                  [5, 15]])
    """, language='python')

    # Chi-Kare İstatistiği ile McNemar Testi
    st.header("📐 Chi-Kare İstatistiği ile McNemar Testi")
    st.write("""
    Şimdi, McNemar testi için chi-kare istatistiğini manuel olarak hesaplayalım. Chi-kare istatistiği şu formülle hesaplanır:
    """)
    st.latex(r'''
    \chi^2 = \frac{(b - c)^2}{b + c}
    ''')

    st.write("""
    Burada:
    - **b**: İlk koşulda "Evet", ikinci koşulda "Hayır" olan gözlemlerin sayısı.
    - **c**: İlk koşulda "Hayır", ikinci koşulda "Evet" olan gözlemlerin sayısı.
    Python'da bu hesaplamayı şöyle yapabiliriz:
    """)
    st.code("""
# b ve c değerlerini tablodan alalım
b = table[0, 1]
c = table[1, 0]

# Chi-kare istatistiğini hesaplayalım
chi_square = (b - c) ** 2 / (b + c)
print('Chi-square Statistic:', chi_square)
    """, language='python')

    # Kesin McNemar Testi (Binom Testi)
    st.header("🔬 Kesin McNemar Testi (Binom Testi)")
    st.write("""
    Küçük örneklem boyutlarında kesin McNemar testi (binom testi) daha doğru sonuçlar verir. Binom testi, b ve c hücrelerindeki farkların anlamlı olup olmadığını belirlemek için kullanılır.
    Python'da binom testi yapmak için:
    """)
    st.code("""
# b ve c değerleri
b = table[0, 1]
c = table[1, 0]

# Binom testi
p_value = binomtest([b, c])
print('p-value:', p_value)
    """, language='python')

    # Örnek Kod ve Uygulama
    st.header("📝 Örnek Kod ve Uygulama")
    st.write("Son olarak, yukarıdaki adımları birleştirerek McNemar testinin tam uygulamasını gösterelim:")
    st.code("""
import numpy as np
from scipy.stats import binomtest, chi2

# 2x2 kontenjans tablosu verileri
table = np.array([[20, 10],
                  [5, 15]])

# b ve c değerlerini tablodan alalım
b = table[0, 1]
c = table[1, 0]

# Chi-kare istatistiğini hesaplayalım
chi_square = (b - c) ** 2 / (b + c)
print('Chi-square Statistic:', chi_square)

# P-değerini hesaplayalım (Chi-kare dağılımı kullanarak)
p_value_chi2 = chi2.sf(chi_square, 1)
print('p-value (Chi-square):', p_value_chi2)

# Binom testi ile kesin McNemar testi
p_value_binom = binomtest([b, c])
print('p-value (Binom Test):', p_value_binom)
    """, language='python')

    st.write("""
    Bu kod, McNemar testini manuel olarak hesaplamak ve sonuçları yorumlamak için gerekli tüm adımları içerir. Yukarıdaki örnekte, chi-kare istatistiği ve p-değerlerini hesapladık. Sonuçları, belirlenen anlamlılık düzeyi (genellikle 0.05) ile karşılaştırarak yorumlayabiliriz. Eğer p-değeri 0.05'ten küçükse, null hipotezi reddederiz ve alternatif hipotezi kabul ederiz. Bu, iki durum arasında anlamlı bir fark olduğunu gösterir.
    """)
