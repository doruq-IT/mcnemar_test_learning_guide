import streamlit as st
from navigation import next_button

def goster_kaynaklar():
    # Başlık ve Giriş
    st.title("📚 Ek Kaynaklar ve İleri Okumalar")

    # İlgili Kitaplar, Makaleler ve Web Kaynakları
    st.header("📖 İlgili Kitaplar, Makaleler ve Web Kaynakları")
    st.write("""
    McNemar testi ve genel istatistiksel analizler hakkında daha fazla bilgi edinmek isteyenler için aşağıdaki kaynaklar faydalı olabilir. Bu kaynaklar, hem temel kavramları anlamak hem de ileri düzeyde bilgi edinmek için kullanılabilir.
    """)

    st.subheader("Kitaplar")
    st.markdown("""
    1. **"Practical Statistics for Data Scientists" by Peter Bruce and Andrew Bruce**
        - Bu kitap, veri bilimciler için istatistiksel yöntemleri pratik bir şekilde açıklar. McNemar testi ve diğer önemli istatistiksel testler hakkında anlaşılır ve uygulamalı bilgiler sunar.
    2. **"Statistical Methods for Psychology" by David C. Howell**
        - Bu kitap, psikoloji öğrencileri ve araştırmacılar için temel ve ileri düzeyde istatistiksel yöntemleri kapsar. McNemar testi gibi ikili verilerle çalışan testler hakkında detaylı bilgi verir.
    """)

    st.subheader("Makaleler")
    st.markdown("""
    1. **Lachenbruch, P. A. (1992). On the sample size for studies based on McNemar's test, *Statistics in Medicine*, 11, 1521–1527**
        - Bu makale, McNemar testi için örneklem büyüklüğünü belirlemenin önemini ve yöntemlerini tartışır. Küçük örneklem boyutlarıyla çalışırken dikkat edilmesi gereken noktaları açıklar.
    2. **Armitage, P. & Berry, G. (1994). Statistical Methods in Medical Research, 3rd Ed. Blackwell Science, Oxford pp. 127–128**
        - Bu kitap, tıbbi araştırmalarda kullanılan istatistiksel yöntemleri kapsar ve McNemar testi hakkında detaylı bilgi sağlar. Tıbbi araştırmalar yapanlar için özellikle faydalıdır.
    """)

    # İleri Seviye İstatistiksel Testler ve Analizler
    st.header("📊 İleri Seviye İstatistiksel Testler ve Analizler")
    st.write("""
    McNemar testi temel bir istatistiksel testtir, ancak daha ileri düzeyde analizler yapmak isteyenler için başka yöntemler de vardır. İşte bazı ileri seviye istatistiksel testler ve analizler:
    """)

    st.subheader("1. Cochran's Q Test")
    st.write("""
    - Birden fazla bağımlı ikili veri kümesi arasındaki farkları analiz etmek için kullanılır. McNemar testinin genişletilmiş bir versiyonu olarak düşünülebilir.
    """)

    st.subheader("2. Logistic Regression")
    st.write("""
    - İkili sonuçları tahmin etmek için kullanılan bir regresyon modelidir. Bağımlı değişkenin ikili olduğu durumlarda (örneğin, "Evet/Hayır") kullanılır.
    """)

    st.subheader("3. Generalized Estimating Equations (GEE)")
    st.write("""
    - Tekrarlanan ölçümler veya bağımlı veri setleri ile çalışırken kullanılan bir yöntemdir. İkili ve sürekli veriler için uygundur.
    """)

    st.subheader("4. Mixed-Effects Models")
    st.write("""
    - Hem sabit hem de rastgele etkileri modellemek için kullanılır. Bu, veri hiyerarşileri veya grup içi korelasyonları olan durumlar için uygundur.
    """)

    st.subheader("5. Survival Analysis")
    st.write("""
    - Olayların zamanını analiz etmek için kullanılır. Özellikle tıbbi araştırmalarda, hastaların hayatta kalma sürelerini analiz etmek için kullanılır.
    """)

    st.subheader("Önerilen Okuma")
    st.markdown("""
    - **"Applied Logistic Regression" by David W. Hosmer, Stanley Lemeshow, and Rodney X. Sturdivant**
        - Bu kitap, lojistik regresyon analizi hakkında derinlemesine bilgi sağlar ve ikili sonuçları analiz etmek için yaygın olarak kullanılır.
    - **"The Analysis of Longitudinal Data" by Peter J. Diggle, Patrick Heagerty, Kung-Yee Liang, and Scott L. Zeger**
        - Tekrarlanan ölçümler ve bağımlı verilerle çalışmak için gerekli olan ileri seviye yöntemleri açıklar.
    - **"Survival Analysis: A Self-Learning Text" by David G. Kleinbaum and Mitchel Klein**
        - Olay zamanlarını ve hayatta kalma analizlerini anlamak için kapsamlı bir rehber sunar.
    """)

    st.write("""
    Bu kaynaklar, McNemar testi ve diğer ileri düzey istatistiksel testler hakkında daha fazla bilgi edinmek isteyenler için mükemmel başlangıç noktalarıdır. Bu kaynakları inceleyerek, istatistiksel analiz becerilerinizi geliştirebilir ve daha karmaşık veri analizlerini gerçekleştirebilirsiniz.
    """)
    
    next_button("sorular", "Sık Sorulan Sorular(SSS)'a Git")
