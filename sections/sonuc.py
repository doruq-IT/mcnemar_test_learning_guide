import streamlit as st
from navigation import next_button

def goster_sonuc():
    # Başlık ve Giriş
    st.title("📈 Sonuç ve Özet")

    # McNemar Testinin Genel Değerlendirmesi
    st.header("🔍 McNemar Testinin Genel Değerlendirmesi")
    st.write("""
    McNemar testi, bağımlı iki ikili veri kümesi arasındaki oranları karşılaştırmak için kullanılan basit ama güçlü bir istatistiksel testtir. Test, özellikle aynı bireylerin farklı zamanlarda veya koşullarda ölçülen sonuçlarını karşılaştırmak için tasarlanmıştır. Bu testin kullanımı şu durumlarda idealdir:
    """)

    st.markdown("""
    - **Eğitim Programları:** Bir eğitim programının öncesi ve sonrası etkilerini değerlendirmek.
    - **Tıbbi Tedaviler:** Bir tedavi öncesi ve sonrası hastaların sağlık durumlarını karşılaştırmak.
    - **Psikolojik Araştırmalar:** Bir terapi öncesi ve sonrası bireylerin durumlarını analiz etmek.
    - **Pazarlama Araştırmaları:** Bir reklam kampanyasının öncesi ve sonrası etkilerini incelemek.
    """)

    st.write("""
    McNemar testi, bağımsız iki grup arasındaki farkları inceleyen chi-kare testinden farklı olarak, bağımlı örneklerle çalışır. Bu özellik, aynı bireyler üzerinde yapılan ölçümlerde daha doğru ve anlamlı sonuçlar elde etmemizi sağlar.
    """)

    # Özet ve Öneriler
    st.header("📚 Özet ve Öneriler")

    st.subheader("Özet")
    st.write("""
    - **Kullanım Alanları:** McNemar testi, ikili sonuçlarla çalışan ve aynı bireylerin farklı zamanlardaki veya koşullardaki sonuçlarını karşılaştıran araştırmalarda kullanılır.
    - **Temelleri:** Test, b ve c hücrelerindeki farkları değerlendirir ve bu farkların anlamlı olup olmadığını belirlemek için chi-kare istatistiği veya binom testi kullanılır.
    - **Yorumlama:** P-değeri kullanılarak sonuçların anlamlılığı değerlendirilir. P-değeri 0.05'ten küçükse, iki durum arasında anlamlı bir fark olduğu kabul edilir.
    - **Güçlü Yönler:** Bağımlı örneklerle çalışırken etkili ve kullanışlıdır, hesaplaması nispeten basittir.
    - **Sınırlamalar:** Yalnızca ikili sonuçlarla çalışabilir ve bağımlı örnekler gerektirir.
    """)

    st.subheader("Öneriler")
    st.markdown("""
    - **Bağımlı Örneklerle Çalışın:** McNemar testi, aynı bireyler üzerinde yapılan ölçümler için tasarlandığından, bağımlı örneklerle çalışmak için idealdir. Farklı zamanlarda veya koşullarda ölçülen aynı bireylerin sonuçlarını analiz etmek için bu testi kullanabilirsiniz.
    - **Küçük Örneklem Boyutlarında Kesin McNemar Testi Kullanın:** Küçük örneklem boyutlarında kesin McNemar testi (binom testi) kullanmak daha doğru sonuçlar verir. Bu, özellikle b ve c hücrelerindeki gözlem sayıları düşük olduğunda önemlidir.
    - **Verileri Görselleştirin:** Sonuçları daha iyi anlamak ve sunmak için verilerinizi grafiklerle görselleştirin. Bar grafikleri veya diğer uygun görselleştirme teknikleri, analizlerinizi daha anlaşılır hale getirir.
    - **Anlamlılık Düzeyini Dikkate Alın:** P-değerini belirlenen anlamlılık düzeyi (genellikle 0.05) ile karşılaştırarak sonuçlarınızı yorumlayın. P-değeri 0.05'ten küçükse, sonuçlarınızın anlamlı olduğunu ve iki durum arasında fark olduğunu kabul edin.
    """)

    st.write("""
    Sonuç olarak, McNemar testi, bağımlı örneklerle çalışan araştırmalar için güçlü bir araçtır. Bu testi doğru şekilde kullanarak, aynı bireyler üzerindeki farklı zamanlarda veya koşullardaki değişiklikleri anlamlı bir şekilde analiz edebilirsiniz.
    """)
    
    next_button("kaynaklar", "McNemar Testinin Matematiksel Temeli'ne Git")