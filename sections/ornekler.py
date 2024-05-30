import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2
from navigation import next_button

def goster_ornekler():
    # Başlık ve Giriş
    st.title("🧪 Uygulamalı Örnekler")

    # Giriş
    st.header("🔍 Farklı Senaryolar ve Örnek Çalışmalar")
    st.write("""
    McNemar testini daha iyi anlamak için farklı senaryolar ve örnek çalışmalar üzerinden gidelim. Bu, testin nasıl çalıştığını ve sonuçların nasıl yorumlandığını görmemizi sağlar.
    """)

    # Senaryo 1: Eğitim Programının Etkisi
    st.header("📘 Senaryo 1: Eğitim Programının Etkisi")
    st.write("""
    Bir grup öğrenci üzerinde bir eğitim programı uyguladığınızı düşünün. Öğrencilerin program öncesi ve sonrası bir sınavdan geçtiklerini varsayalım. Amacımız, bu programın öğrencilerin bilgi seviyelerinde anlamlı bir fark yaratıp yaratmadığını belirlemektir.
    Verilerimiz şöyle olsun:
    """)

    st.write("""
    | Program Sonrası: Anladı | Program Sonrası: Anlamadı |
    |-------------------------|---------------------------|
    | **Program Öncesi: Anladı** | 20 | 10 |
    | **Program Öncesi: Anlamadı** | 5 | 15 |
    """)

    st.subheader("Adım 1: Chi-Kare İstatistiğinin Hesaplanması")
    st.latex(r'''
    \chi^2 = \frac{(b - c)^2}{b + c}
    ''')
    st.write("""
    Bu verilerle hesapladığımızda:
    - **b = 10** (Program öncesi "Anladı", program sonrası "Anlamadı")
    - **c = 5** (Program öncesi "Anlamadı", program sonrası "Anladı")
    """)

    chi_square = (10 - 5) ** 2 / (10 + 5)
    st.write(f"Chi-kare istatistiği: χ² = (10 - 5)² / (10 + 5) = {chi_square:.2f}")

    st.subheader("Adım 2: P-Değerinin Hesaplanması")
    st.write("Chi-kare istatistiği kullanarak p-değerini hesaplıyoruz:")
    st.code("""
from scipy.stats import chi2

# Chi-kare istatistiği
chi_square = 1.67

# P-değerini hesaplama
p_value = chi2.sf(chi_square, 1)
print('p-value:', p_value)
    """, language='python')

    p_value = chi2.sf(chi_square, 1)
    st.write(f"Bu durumda p-değeri: {p_value:.3f} olacaktır. P-değeri 0.05'ten büyük olduğu için, null hipotezi reddetmeyiz. Yani, eğitim programı öğrencilerin bilgi seviyelerinde anlamlı bir fark yaratmamıştır.")

    # Senaryo 2: Tedavi Etkisinin Değerlendirilmesi
    st.header("💊 Senaryo 2: Tedavi Etkisinin Değerlendirilmesi")
    st.write("""
    Bir grup hasta üzerinde yeni bir ilaç tedavisinin etkisini değerlendirdiğinizi düşünün. Hastaların tedavi öncesi ve sonrası sağlık durumlarını "İyileşti/İyileşmedi" olarak kaydediyoruz.
    Verilerimiz şöyle olsun:
    """)

    st.write("""
    | Tedavi Sonrası: İyileşti | Tedavi Sonrası: İyileşmedi |
    |--------------------------|----------------------------|
    | **Tedavi Öncesi: İyileşti** | 30 | 10 |
    | **Tedavi Öncesi: İyileşmedi** | 8 | 12 |
    """)

    st.write("""
    Bu verilerle aynı adımları izleyerek chi-kare istatistiği ve p-değerini hesaplıyoruz. Eğer p-değeri 0.05'ten küçükse, tedavinin etkili olduğunu kabul ederiz.
    """)

    # Sonuçların Görselleştirilmesi ve Analizi
    st.header("📊 Sonuçların Görselleştirilmesi ve Analizi")
    st.write("""
    Sonuçları daha iyi anlamak ve sunmak için görselleştirme çok önemlidir. Matplotlib gibi kütüphaneleri kullanarak verileri grafiklerle gösterebiliriz.
    """)

    st.write("Örneğin, yukarıdaki eğitim programı verilerini bir bar grafiği ile görselleştirelim:")
    st.code("""
import matplotlib.pyplot as plt

# Verileri hazırlama
categories = ['Program Öncesi: Anladı', 'Program Öncesi: Anlamadı']
before = [20, 5]
after = [10, 15]

# Bar grafiği oluşturma
bar_width = 0.35
index = np.arange(len(categories))

fig, ax = plt.subplots()
bar1 = ax.bar(index, before, bar_width, label='Program Sonrası: Anladı')
bar2 = ax.bar(index + bar_width, after, bar_width, label='Program Sonrası: Anlamadı')

# Grafik ayarları
ax.set_xlabel('Durum')
ax.set_ylabel('Öğrenci Sayısı')
ax.set_title('Eğitim Programı Öncesi ve Sonrası Bilgi Seviyeleri')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(categories)
ax.legend()

plt.show()
    """, language='python')

    st.write("Bu grafik, program öncesi ve sonrası öğrencilerin bilgi seviyelerindeki değişiklikleri görsel olarak gösterir.")

    # Bar Grafiği Görselleştirme
    categories = ['Program Öncesi: Anladı', 'Program Öncesi: Anlamadı']
    before = [20, 5]
    after = [10, 15]

    bar_width = 0.35
    index = np.arange(len(categories))

    fig, ax = plt.subplots()
    bar1 = ax.bar(index, before, bar_width, label='Program Sonrası: Anladı')
    bar2 = ax.bar(index + bar_width, after, bar_width, label='Program Sonrası: Anlamadı')

    ax.set_xlabel('Durum')
    ax.set_ylabel('Öğrenci Sayısı')
    ax.set_title('Eğitim Programı Öncesi ve Sonrası Bilgi Seviyeleri')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(categories)
    ax.legend()

    st.pyplot(fig)
    
    next_button("sonuc", "Sonuç ve Özet'e Git")
