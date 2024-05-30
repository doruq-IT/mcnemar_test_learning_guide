import streamlit as st
from navigation import next_button

def goster_testin_yorumu():
    # Başlık ve Giriş
    st.title("📊 McNemar Testinin Yorumlanması")

    # Hipotezlerin Tanımlanması (H0 ve H1)
    st.header("🔍 Hipotezlerin Tanımlanması (H0 ve H1)")
    st.write("""
    Herhangi bir istatistiksel testte olduğu gibi, McNemar testinde de iki hipotez tanımlanır: null hipotezi (H0) ve alternatif hipotez (H1).
    """)

    st.subheader("Null Hipotezi (H0):")
    st.markdown("""
    - İki durum veya zaman noktası arasında anlamlı bir fark olmadığını belirtir.
    - Örneğin, tedavinin veya müdahalenin etkisinin olmadığını varsayar.
    """)

    st.subheader("Alternatif Hipotez (H1):")
    st.markdown("""
    - İki durum veya zaman noktası arasında anlamlı bir fark olduğunu belirtir.
    - Örneğin, tedavinin veya müdahalenin etkili olduğunu varsayar.
    """)

    st.write("""
    **Örnek:** Bir eğitim programının etkisini değerlendiriyorsak:
    - **H0:** Eğitim programı öncesi ve sonrası bilgi seviyeleri arasında anlamlı bir fark yoktur.
    - **H1:** Eğitim programı öncesi ve sonrası bilgi seviyeleri arasında anlamlı bir fark vardır.
    """)

    # P-Değeri ve Anlamlılık Düzeyi
    st.header("📉 P-Değeri ve Anlamlılık Düzeyi")
    st.write("""
    P-değeri, istatistiksel testin sonucunun rastlantısal olup olmadığını belirlememize yardımcı olur. P-değeri, null hipotezin doğru olması durumunda gözlemlenen sonuçların ortaya çıkma olasılığını ifade eder.
    """)

    st.subheader("Anlamlılık Düzeyi (α):")
    st.markdown("""
    - Genellikle %5 (0.05) olarak belirlenir.
    - Yanlışlıkla null hipotezi reddetme olasılığını ifade eder.
    - P-değeri 0.05'ten küçükse, sonuç anlamlı kabul edilir ve null hipotez reddedilir.
    """)

    st.write("""
    **Örnek:** Bir p-değerimiz olduğunu varsayalım:
    - **P-değeri = 0.03**
    - **Anlamlılık düzeyi (α) = 0.05**
    Bu durumda, p-değeri 0.05'ten küçük olduğu için sonuç anlamlıdır ve null hipotezi reddederiz.
    """)

    # Sonuçların Yorumlanması ve Karar Verme
    st.header("📝 Sonuçların Yorumlanması ve Karar Verme")
    st.write("""
    Sonuçları yorumlarken, p-değerini ve belirlenen anlamlılık düzeyini dikkate alırız. İşte adımlar:
    """)

    st.subheader("1. P-değerini Anlamlılık Düzeyi ile Karşılaştırma:")
    st.markdown("""
    - **P-değeri < α** ise, null hipotezi reddederiz.
    - **P-değeri ≥ α** ise, null hipotezi reddetmeyiz.
    """)

    st.subheader("2. Karar Verme:")
    st.markdown("""
    - Null hipotezi reddediyorsak, bu iki durum veya zaman noktası arasında anlamlı bir fark olduğunu gösterir.
    - Null hipotezi reddetmiyorsak, bu iki durum veya zaman noktası arasında anlamlı bir fark olmadığını gösterir.
    """)

    st.write("""
    **Örnek:** Eğitim programı ile ilgili örneğimizi ele alalım. Diyelim ki, McNemar testi sonucunda p-değeri 0.03 çıktı. Anlamlılık düzeyimiz 0.05 olduğuna göre:
    """)

    st.latex(r'''
    \text{P-değeri} = 0.03 < \alpha = 0.05
    ''')

    st.write("""
    Bu durumda, null hipotezi (H0) reddederiz ve alternatif hipotezi (H1) kabul ederiz. Bu, eğitim programının öğrencilerin bilgi seviyelerinde anlamlı bir fark yarattığını gösterir.
    """)

    # Özet
    st.header("📚 Özet")
    st.write("""
    Özetle, McNemar testinin sonuçlarını yorumlarken p-değerine ve belirlenen anlamlılık düzeyine dikkat ederiz. P-değeri küçükse (genellikle 0.05'ten küçükse), null hipotezi reddederiz ve alternatif hipotezi kabul ederiz. Bu süreç, belirli bir tedavi veya müdahalenin etkisini anlamamıza yardımcı olur.
    """)
    
    next_button("matematiksel_temel", "McNemar Testinin Matematiksel Temeli'ne Git")