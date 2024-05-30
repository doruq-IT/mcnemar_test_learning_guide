# sections/giris.py
import streamlit as st

def goster_giris():
    st.subheader("McNemar Testinin Tanımı")
    st.write("""
    McNemar testi, bağımlı iki ikili veri kümesi arasındaki oranları karşılaştırmak için kullanılan bir istatistiksel testtir. Bu test, özellikle çift-yönlü tablo verilerinde kullanışlıdır ve belirli bir tedavi veya müdahalenin etkisini değerlendirmek amacıyla sıklıkla kullanılır. McNemar testi, örneğin aynı bireylerin iki farklı zaman noktası veya iki farklı koşul altındaki sonuçlarını karşılaştırmak için idealdir.
    """)
    st.subheader("Kullanım Alanları")
    st.write("""
    McNemar testi, birçok farklı alanda kullanılabilir. İşte birkaç örnek:
    - **Tıp ve Sağlık Araştırmaları**
    - **Psikoloji ve Eğitim**
    - **Sosyal Bilimler**
    - **Pazarlama Araştırmaları**
    """)
