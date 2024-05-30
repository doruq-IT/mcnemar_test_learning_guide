import streamlit as st
from navigation import next_button

def goster_sorular():
    # Başlık ve Giriş
    st.title("❓ Sıkça Sorulan Sorular (SSS)")

    # McNemar Testi ile İlgili Yaygın Sorular ve Yanıtları
    st.header("📋 McNemar Testi ile İlgili Yaygın Sorular ve Yanıtları")

    # Soru 1
    st.subheader("Soru 1: McNemar testi nedir ve ne zaman kullanılır?")
    st.write("""
    Yanıt: McNemar testi, bağımlı iki ikili veri kümesi arasındaki oranları karşılaştırmak için kullanılan bir istatistiksel testtir. Aynı bireylerin farklı zamanlarda veya koşullarda ölçülen sonuçlarını karşılaştırmak için kullanılır. Örneğin, bir tedavi öncesi ve sonrası hastaların sağlık durumlarını veya bir eğitim programı öncesi ve sonrası öğrencilerin bilgi seviyelerini değerlendirmek için uygundur.
    """)

    # Soru 2
    st.subheader("Soru 2: McNemar testi ile chi-kare testi arasındaki fark nedir?")
    st.write("""
    Yanıt: Chi-kare testi, bağımsız iki kategorik veri kümesi arasındaki ilişkiyi test ederken, McNemar testi bağımlı iki ikili veri kümesi arasındaki farkı test eder. McNemar testi, aynı bireylerin iki farklı durumda ölçülen sonuçlarını karşılaştırmak için uygundur. Chi-kare testi ise bağımsız örnekler üzerinde kullanılır.
    """)

    # Soru 3
    st.subheader("Soru 3: McNemar testi nasıl hesaplanır?")
    st.write("""
    Yanıt: McNemar testi, b ve c hücrelerindeki farkları değerlendirir ve şu formülle hesaplanır:
    """)
    st.latex(r'''
    \chi^2 = \frac{(b - c)^2}{b + c}
    ''')
    st.write("""
    Burada, b ve c hücrelerindeki gözlem sayılarıdır. Elde edilen chi-kare istatistiği kullanılarak p-değeri hesaplanır ve bu p-değeri belirli bir anlamlılık düzeyi ile karşılaştırılır.
    """)

    # Soru 4
    st.subheader("Soru 4: P-değeri nedir ve nasıl yorumlanır?")
    st.write("""
    Yanıt: P-değeri, istatistiksel testin sonucunun rastlantısal olup olmadığını belirler. Genellikle 0.05 anlamlılık düzeyi kullanılır. Eğer p-değeri 0.05'ten küçükse, null hipotez (H0) reddedilir ve alternatif hipotez (H1) kabul edilir. Bu, iki durum arasında anlamlı bir fark olduğunu gösterir.
    """)

    # Soru 5
    st.subheader("Soru 5: McNemar testi için hangi tür veriler gereklidir?")
    st.write("""
    Yanıt: McNemar testi, ikili sonuçlarla çalışır. Bu, "Evet/Hayır", "Başarılı/Başarısız" gibi iki olası durumu ifade eden verilerdir. Ayrıca, verilerin bağımlı olması, yani aynı bireylerin farklı zamanlarda veya koşullarda ölçülen sonuçlarını içermesi gerekir.
    """)

    # Soru 6
    st.subheader("Soru 6: Küçük örneklem boyutlarıyla nasıl çalışılır?")
    st.write("""
    Yanıt: Küçük örneklem boyutlarında, McNemar testi için kesin McNemar testi (binom testi) kullanmak daha doğru sonuçlar verir. Bu, özellikle b ve c hücrelerindeki gözlem sayıları düşük olduğunda önemlidir. Binom testi, b ve c hücrelerindeki farkların anlamlı olup olmadığını belirlemek için kullanılır.
    """)

    # Soru 7
    st.subheader("Soru 7: McNemar testi ile ilgili daha fazla bilgi nerede bulabilirim?")
    st.write("""
    Yanıt: McNemar testi ve genel istatistiksel analizler hakkında daha fazla bilgi edinmek için aşağıdaki kaynakları inceleyebilirsiniz:
    - "Practical Statistics for Data Scientists" by Peter Bruce and Andrew Bruce
    - "Statistical Methods for Psychology" by David C. Howell
    - Khan Academy ve Coursera gibi online eğitim platformları
    - İlgili akademik makaleler ve kitaplar
    """)

    # Soru 8
    st.subheader("Soru 8: McNemar testini Python ile nasıl uygulayabilirim?")
    st.write("""
    Yanıt: McNemar testini Python ile uygulamak için numpy ve scipy gibi kütüphaneleri kullanabilirsiniz. Önce verilerinizi 2x2 kontenjans tablosu olarak düzenleyin, ardından chi-kare istatistiği ve p-değerini hesaplayın. Küçük örneklem boyutları için binom testini kullanabilirsiniz. Örnek bir uygulama kodu:
    """)
    st.code("""
import numpy as np
from scipy.stats import binom_test, chi2

# 2x2 kontenjans tablosu
table = np.array([[20, 10], [5, 15]])

# b ve c değerleri
b = table[0, 1]
c = table[1, 0]

# Chi-kare istatistiği
chi_square = (b - c) ** 2 / (b + c)
p_value_chi2 = chi2.sf(chi_square, 1)

# Binom testi
p_value_binom = binom_test([b, c])

print('Chi-square Statistic:', chi_square)
print('p-value (Chi-square):', p_value_chi2)
print('p-value (Binom Test):', p_value_binom)
    """, language='python')

    st.write("""
    Bu sıkça sorulan sorular ve yanıtları, McNemar testi hakkında temel bilgileri ve uygulama detaylarını öğrenmenize yardımcı olacaktır.
    """)
