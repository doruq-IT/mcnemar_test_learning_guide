import streamlit as st
import pandas as pd

def goster_giris():
    # Bölüm 1: McNemar Testinin Tanımı
    st.header("📊 McNemar Testinin Tanımı")
    st.write("""
    McNemar testi, bağımlı iki ikili veri kümesi arasındaki oranların karşılaştırılması için kullanılan bir istatistiksel testtir. Bu test, özellikle çift-yönlü tablo verilerinde kullanışlıdır ve belirli bir tedavi veya müdahalenin etkisini değerlendirmek amacıyla sıklıkla kullanılır. McNemar testi, örneğin aynı bireylerin iki farklı zaman noktası veya iki farklı koşul altındaki sonuçlarını karşılaştırmak için idealdir.
    
    Örneğin, bir grup öğrencinin bir eğitim programı öncesi ve sonrası bilgi seviyelerini karşılaştırmak istiyorsunuz. Bu durumda, McNemar testi, eğitim programının bilgi seviyesinde anlamlı bir değişiklik yaratıp yaratmadığını belirlemek için kullanılabilir.
    
    Bu test, bağımsız iki grubu karşılaştırmak için değil, aynı grup üzerinde yapılan iki farklı ölçümü karşılaştırmak için tasarlanmıştır. Testin uygulanması için bir 2x2 kontenjans tablosu kullanılır ve bu tablo şu şekilde görünebilir:
    """)

    # Örnek Kontenjans Tablosu
    st.subheader("Örnek 2x2 Kontenjans Tablosu")
    data = {'Koşul B: Evet': ['a', 'c'], 'Koşul B: Hayır': ['b', 'd']}
    df = pd.DataFrame(data, index=['Koşul A: Evet', 'Koşul A: Hayır'])
    st.table(df)

    st.write("""
    Bu tablodaki hücreler şu şekilde tanımlanır:
    - **a**: Her iki koşulda da "Evet" olan gözlemler.
    - **b**: İlk koşulda "Evet" ve ikinci koşulda "Hayır" olan gözlemler.
    - **c**: İlk koşulda "Hayır" ve ikinci koşulda "Evet" olan gözlemler.
    - **d**: Her iki koşulda da "Hayır" olan gözlemler.
    
    McNemar testi, özellikle **b** ve **c** hücrelerindeki değişikliklere odaklanır ve şu formülle hesaplanır:
    """)

    # McNemar Testi Formülü
    st.latex(r'''
    \chi^2 = \frac{(b - c)^2}{b + c}
    ''')
    
    st.write("""
    Bu formül, iki koşul arasındaki farkın istatistiksel olarak anlamlı olup olmadığını belirlemek için kullanılır.
    """)
    
    if st.button('📚 Daha Fazla Bilgi Edinin'):
        st.write("""
        McNemar testi hakkında daha fazla bilgi edinmek için rehberimizin diğer bölümlerine göz atabilirsiniz. Her bölümde testin farklı yönlerini keşfedecek ve nasıl uygulanacağını adım adım öğreneceksiniz.
        """)
