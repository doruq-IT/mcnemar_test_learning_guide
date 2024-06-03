import streamlit as st

def goster_sonuc():
    # Başlık ve Giriş
    st.title("📈 Sonuç ve Özet")

    # McNemar Testinin Genel Değerlendirmesi
    st.header("🔍 McNemar Testinin Genel Değerlendirmesi")
    st.write("""
    McNemar testi, bağımlı iki ikili veri kümesi arasındaki oranları karşılaştırmak için kullanılan basit ve güçlü bir istatistiksel testtir. Aynı bireylerin farklı zamanlardaki veya koşullardaki sonuçlarını karşılaştırmak için idealdir. Kullanım alanları:
    """)

    st.markdown("""
    - **Eğitim Programları:** Program öncesi ve sonrası etkileri değerlendirmek.
    - **Tıbbi Tedaviler:** Tedavi öncesi ve sonrası sağlık durumlarını karşılaştırmak.
    - **Psikolojik Araştırmalar:** Terapi öncesi ve sonrası durumları analiz etmek.
    - **Pazarlama Araştırmaları:** Reklam kampanyası öncesi ve sonrası etkileri incelemek.
    """)

    st.write("""
    McNemar testi, bağımsız iki grup arasındaki farkları inceleyen chi-kare testinden farklı olarak, aynı bireyler üzerinde yapılan ölçümlerde daha doğru sonuçlar verir.
    """)

    # Özet ve Öneriler
    st.header("📚 Özet ve Öneriler")

    st.subheader("Özet")
    st.write("""
    - **Kullanım Alanları:** İkili sonuçlarla çalışan ve aynı bireylerin farklı zamanlardaki sonuçlarını karşılaştıran araştırmalarda kullanılır.
    - **Temelleri:** b ve c hücrelerindeki farkları değerlendirir ve chi-kare istatistiği veya binom testi ile analiz eder.
    - **Yorumlama:** P-değeri 0.05'ten küçükse, iki durum arasında anlamlı bir fark olduğu kabul edilir.
    - **Güçlü Yönler:** Bağımlı örneklerle çalışırken etkili ve kullanışlıdır, hesaplaması basittir.
    - **Sınırlamalar:** Yalnızca ikili sonuçlarla çalışabilir ve bağımlı örnekler gerektirir.
    """)

    st.subheader("Öneriler")
    st.markdown("""
    - **Bağımlı Örneklerle Çalışın:** Aynı bireyler üzerinde yapılan ölçümler için idealdir.
    - **Küçük Örneklem Boyutlarında Binom Testi Kullanın:** Küçük örneklem boyutlarında daha doğru sonuçlar verir.
    - **Verileri Görselleştirin:** Grafiklerle verilerinizi daha anlaşılır hale getirin.
    - **Anlamlılık Düzeyini Dikkate Alın:** P-değerini 0.05 ile karşılaştırarak yorumlayın.
    """)

    st.write("""
    Sonuç olarak, McNemar testi, bağımlı örneklerle çalışan araştırmalar için güçlü bir araçtır. Doğru şekilde kullanarak, aynı bireyler üzerindeki değişiklikleri anlamlı bir şekilde analiz edebilirsiniz.
    """)

