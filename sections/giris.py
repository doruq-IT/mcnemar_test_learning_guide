import streamlit as st
import pandas as pd

def goster_giris():
    # Bölüm 1: McNemar Testinin Tanımı
    st.header("📊 McNemar Testinin Tanımı")
    st.write("""
    McNemar testi, aynı grup içindeki iki farklı durum veya zamandaki ikili sonuçları karşılaştıran bir istatistiksel testtir. Özellikle aynı bireylerin farklı zaman noktalarındaki sonuçlarını değerlendirmek için idealdir.
    
    Örneğin, bir eğitim programının öğrencilerin bilgi seviyesinde değişiklik yaratıp yaratmadığını anlamak için kullanılabilir.
    
    Test, bağımsız iki grubu karşılaştırmak için değil, aynı grup üzerinde yapılan iki farklı ölçümü karşılaştırmak için tasarlanmıştır. 2x2 kontenjans tablosu kullanılarak uygulanır:
    """)

    # Örnek Kontenjans Tablosu
    st.subheader("Örnek 2x2 Kontenjans Tablosu (pd.crosstab(data['column1'], data['column2']))")
    data = {'Koşul B: Evet': ['a', 'c'], 'Koşul B: Hayır': ['b', 'd']}
    df = pd.DataFrame(data, index=['Koşul A: Evet', 'Koşul A: Hayır'])
    st.table(df)

    st.write("""
    - **a**: Her iki koşulda da "Evet" olan gözlemler.
    - **b**: İlk koşulda "Evet", ikinci koşulda "Hayır" olan gözlemler.
    - **c**: İlk koşulda "Hayır", ikinci koşulda "Evet" olan gözlemler.
    - **d**: Her iki koşulda da "Hayır" olan gözlemler.
    
    McNemar testi, **b** ve **c** hücrelerindeki değişikliklere odaklanır ve şu formülle hesaplanır:
    """)

    # McNemar Testi Formülü
    st.latex(r'''
    \chi^2 = \frac{(b - c)^2}{b + c}
    ''')
    
    st.write("""
    Bu formül, iki koşul arasındaki farkın anlamlı olup olmadığını belirlemek için kullanılır.
    """)
    
    if st.button('📚 Daha Fazla Bilgi Edinin'):
        st.write("""
        McNemar testi hakkında daha fazla bilgi edinmek için rehberimizin diğer bölümlerine göz atabilirsiniz. Her bölümde testin farklı yönlerini keşfedecek ve nasıl uygulanacağını adım adım öğreneceksiniz.
        """)
