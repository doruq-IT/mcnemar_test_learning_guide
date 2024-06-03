import streamlit as st

def goster_testin_yorumu():
    # Başlık ve Giriş
    st.title("📊 McNemar Testinin Yorumlanması")

    # Hipotezlerin Tanımlanması (H0 ve H1)
    st.header("🔍 Hipotezlerin Tanımlanması (H0 ve H1)")
    st.write("""
    McNemar testinde iki hipotez vardır:
    - **Null Hipotezi (H0):** İki zaman veya durum arasında fark yoktur.
    - **Alternatif Hipotez (H1):** İki zaman veya durum arasında fark vardır.
    """)

    st.write("""
    **Örnek:** Eğitim programının etkisini değerlendiriyorsak:
    - **H0:** Program öncesi ve sonrası bilgi seviyeleri arasında fark yoktur.
    - **H1:** Program öncesi ve sonrası bilgi seviyeleri arasında fark vardır.
    """)

    # P-Değeri ve Anlamlılık Düzeyi
    st.header("📉 P-Değeri ve Anlamlılık Düzeyi")
    st.write("""
    P-değeri, test sonucunun rastlantısal olup olmadığını gösterir.
    """)

    st.subheader("Anlamlılık Düzeyi (α):")
    st.markdown("""
    - Genellikle 0.05 olarak belirlenir.
    - P-değeri 0.05'ten küçükse, sonuç anlamlı kabul edilir ve H0 reddedilir.
    """)

    st.write("""
    **Örnek:** 
    - **P-değeri = 0.03**
    - **Anlamlılık düzeyi (α) = 0.05**
    Bu durumda, p-değeri 0.05'ten küçük olduğu için H0 reddedilir.
    """)

    # Sonuçların Yorumlanması ve Karar Verme
    st.header("📝 Sonuçların Yorumlanması ve Karar Verme")
    st.write("""
    1. **P-değerini Anlamlılık Düzeyi ile Karşılaştırma:**
       - **P-değeri < α** ise, H0 reddedilir.
       - **P-değeri ≥ α** ise, H0 reddedilmez.
    """)

    st.write("""
    **Örnek:** P-değeri 0.03 ve α = 0.05 ise:
    """)
    st.latex(r'''
    \text{P-değeri} = 0.03 < \alpha = 0.05
    ''')

    st.write("""
    Bu durumda, H0 reddedilir ve H1 kabul edilir. Bu, eğitim programının öğrencilerin bilgi seviyelerinde anlamlı bir fark yarattığını gösterir.
    """)

    # Özet
    st.header("📚 Özet")
    st.write("""
    McNemar testinin sonuçlarını yorumlarken p-değerine ve anlamlılık düzeyine dikkat ederiz. P-değeri 0.05'ten küçükse, H0 reddedilir ve H1 kabul edilir. Bu, belirli bir tedavi veya müdahalenin etkisini anlamamıza yardımcı olur.
    """)

