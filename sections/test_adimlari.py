import streamlit as st
import pandas as pd
import scipy.stats as stats
from navigation import next_button

def goster_test_adimlari():
    # Başlık ve Giriş
    st.title("🔬 McNemar Testinin Adımları")

    # Bölüm 1: Veri Toplama ve Hazırlama
    st.header("📊 Veri Toplama ve Hazırlama")
    st.write("""
    McNemar testini uygulamadan önce, veri toplama ve hazırlama aşamalarını tamamlamanız gerekir. Bu aşamada, aynı bireylerin iki farklı durumda veya zamanda elde edilen sonuçlarını toplarız. Veriler genellikle "Evet/Hayır", "Başarılı/Başarısız" gibi ikili sonuçlar şeklinde olur.
    """)

    st.write("""
    **Örnek:** Bir grup öğrenci üzerinde bir eğitim programı uyguluyoruz. Program öncesi ve sonrası öğrencilerin belirli bir konuyu anlayıp anlamadıklarını kaydediyoruz. Bu veriler daha sonra McNemar testi için kullanılacaktır.
    """)

    # Bölüm 2: 2x2 Kontenjans Tablosunun Oluşturulması
    st.header("📋 2x2 Kontenjans Tablosunun Oluşturulması")
    st.write("""
    Verileri topladıktan sonra, bu verileri 2x2 kontenjans tablosu olarak düzenlememiz gerekir. Bu tablo, iki durum arasındaki ilişkiyi gösterir.
    """)

    st.write("""
    **Örnek:** 50 öğrencinin program öncesi ve sonrası bilgilerini aşağıdaki gibi kaydedelim:
    """)

    # Örnek Kontenjans Tablosu
    data = {'Program Sonrası: Anladı': [20, 5], 'Program Sonrası: Anlamadı': [10, 15]}
    df = pd.DataFrame(data, index=['Program Öncesi: Anladı', 'Program Öncesi: Anlamadı'])
    st.table(df)

    st.write("""
    Bu tablo şu şekilde yorumlanır:
    - 20 öğrenci, hem program öncesi hem de program sonrası "Anladı".
    - 10 öğrenci, program öncesi "Anladı", ancak program sonrası "Anlamadı".
    - 5 öğrenci, program öncesi "Anlamadı", ancak program sonrası "Anladı".
    - 15 öğrenci, hem program öncesi hem de program sonrası "Anlamadı".
    """)

    # Bölüm 3: Chi-Kare İstatistiğinin Hesaplanması
    st.header("📐 Chi-Kare İstatistiğinin Hesaplanması")
    st.write("""
    Chi-kare istatistiği, b ve c hücrelerindeki farkın anlamlı olup olmadığını belirlemek için kullanılır. Bu hesaplama şu formülle yapılır:
    """)

    st.latex(r'''
    \chi^2 = \frac{(b - c)^2}{b + c}
    ''')

    st.write("""
    **Örnek:** Tablomuzdaki b ve c değerlerini kullanarak chi-kare istatistiğini hesaplayalım:
    """)

    st.write("""
    - **b = 10** (Program öncesi "Anladı", program sonrası "Anlamadı")
    - **c = 5** (Program öncesi "Anlamadı", program sonrası "Anladı")
    """)

    chi_square = (10 - 5)**2 / (10 + 5)
    st.write(f"Chi-kare istatistiği hesaplama: χ² = (10 - 5)² / (10 + 5) = {chi_square:.2f}")

    st.latex(r'''
    \chi^2 = \frac{(10 - 5)^2}{10 + 5} = \frac{25}{15} \approx 1.67
    ''')

    st.write("Bu istatistik değeri, testin sonucunu değerlendirmek için kullanılır.")

    # Bölüm 4: P-Değerinin Hesaplanması
    st.header("📉 P-Değerinin Hesaplanması")
    st.write("""
    Chi-kare istatistiği hesaplandıktan sonra, bu değeri kullanarak p-değerini hesaplamamız gerekir. P-değeri, elde edilen sonucun rastlantısal olup olmadığını belirlememize yardımcı olur. Genellikle p-değeri 0.05'ten küçükse, sonuç anlamlı kabul edilir.
    """)

    st.write("""
    P-değerini hesaplamak için genellikle bir istatistiksel yazılım veya Python gibi bir programlama dili kullanılır. İşte Python'da nasıl yapılacağına dair bir örnek:
    """)

    st.code("""
import scipy.stats as stats

# Chi-kare istatistiği
chi_square = 1.67

# Serbestlik derecesi (McNemar testi için genellikle 1'dir)
df = 1

# P-değerini hesaplama
p_value = stats.chi2.sf(chi_square, df)
print('p-value:', p_value)
    """, language='python')

    st.write("""
    **Örnek:** Örneğimizde p-değeri şöyle hesaplanır:
    """)

    p_value = stats.chi2.sf(1.67, 1)
    st.write(f"p-değeri: {p_value:.4f}")

    st.write("""
    Eğer p-değeri 0.05'ten küçükse, eğitim programının öğrencilerin bilgi seviyelerinde anlamlı bir değişiklik yaptığı sonucuna varabiliriz.
    """)

    # Sonuç
    st.header("📊 Sonuç")
    st.write("""
    Bu adımlar, McNemar testini uygulamak için gerekli olan temel adımlardır:
    1. Verileri toplamak ve hazırlamak.
    2. 2x2 kontenjans tablosu oluşturmak.
    3. Chi-kare istatistiğini hesaplamak.
    4. P-değerini hesaplamak ve sonuçları yorumlamak.
    """)
    
    next_button("testin_yorumu", "McNemar Testinin Matematiksel Temeli'ne Git")