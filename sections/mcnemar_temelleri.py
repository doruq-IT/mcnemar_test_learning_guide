import streamlit as st

def goster_temeller():
    st.header("📊 McNemar Testinin Temelleri")
    st.write("""
    McNemar testi, bağımlı iki ikili veri kümesi arasındaki oranları karşılaştırmak için kullanılır. Özellikle aynı bireylerin farklı zamanlardaki veya koşullardaki sonuçlarını analiz etmek için idealdir.
    - **Bağımlı Örnekler:** Aynı grup, farklı zaman veya koşullarda test edilir.
                            Bir grup hastanın tedavi öncesi ve tedavi sonrası sağlık durumlarını karşılaştırmak.
    - **Eşleştirilmiş Veriler:** Aynı bireylerin iki farklı ölçümdeki sonuçları karşılaştırılır.
                                 Aynı öğrencilerin iki farklı sınavdaki başarı durumlarını karşılaştırmak.
    """)
