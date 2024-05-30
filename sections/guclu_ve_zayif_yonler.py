import streamlit as st
from navigation import next_button

def goster_guclu_ve_zayif_yonler():
    # Başlık ve Giriş
    st.title("💪 McNemar Testinin Güçlü ve Zayıf Yönleri")

    # Avantajlar
    st.header("✅ Avantajları")
    st.write("McNemar testinin bazı önemli avantajları vardır. İşte bu avantajları basit bir dille açıklayalım:")

    st.subheader("1. Bağımlı Örnekler İçin Uygunluk")
    st.markdown("""
    - McNemar testi, aynı bireylerin iki farklı durumda veya zamanda ölçülen sonuçlarını karşılaştırmak için idealdir.
    - Bu, aynı grupta yapılan tedavi öncesi ve sonrası değerlendirmeler gibi bağımlı örneklerde kullanışlıdır.
    """)

    st.subheader("2. İkili Sonuçlar İçin Tasarlanmış")
    st.markdown("""
    - McNemar testi, "Evet/Hayır", "Başarılı/Başarısız" gibi ikili sonuçlar için uygundur.
    - İkili sonuçlarla çalışırken, verilerinizi analiz etmek için basit ve etkili bir yöntem sunar.
    """)

    st.subheader("3. Kolay Hesaplama")
    st.markdown("""
    - McNemar testinin matematiksel hesaplamaları nispeten basittir.
    - Özellikle küçük örneklem boyutlarında hesaplamaları manuel olarak yapabilirsiniz.
    """)

    st.subheader("4. Örneklem Büyüklüğüne Duyarlı")
    st.markdown("""
    - McNemar testi, özellikle küçük örneklem boyutlarında kesin sonuçlar verir.
    - Binom testi kullanarak, küçük veri kümelerinde bile doğru sonuçlar elde edebilirsiniz.
    """)

    # Dezavantajlar ve Sınırlamalar
    st.header("⚠️ Dezavantajları ve Sınırlamaları")
    st.write("McNemar testinin bazı dezavantajları ve sınırlamaları da vardır. İşte bu dezavantajları basit bir dille açıklayalım:")

    st.subheader("1. Yalnızca İkili Sonuçlarla Sınırlı")
    st.markdown("""
    - McNemar testi, yalnızca ikili sonuçlarla çalışabilir.
    - Yani, "Evet/Hayır", "Başarılı/Başarısız" gibi iki olası durumun olduğu verilerle sınırlıdır.
    - Daha fazla kategorili verilerle çalışmak için uygun değildir.
    """)

    st.subheader("2. Bağımlı Örnekler Gerektirir")
    st.markdown("""
    - Testin uygulanabilmesi için verilerin bağımlı örnekler olması gerekir.
    - Yani, aynı bireylerin iki farklı durumda veya zamanda ölçülen sonuçlarıyla çalışmanız gerekir.
    - Bağımsız örneklerle çalışmak için uygun değildir.
    """)

    st.subheader("3. Yalnızca 2x2 Tablo Kullanımı")
    st.markdown("""
    - McNemar testi, yalnızca 2x2 kontenjans tablolarıyla çalışır.
    - Daha büyük veya daha karmaşık tablolarla çalışmak için uygun değildir.
    """)

    st.subheader("4. Küçük Örneklem Boyutlarında Hassasiyet")
    st.markdown("""
    - Küçük örneklem boyutlarında testin sonuçları hassas olabilir.
    - Bu durumlarda kesin McNemar testi (binom testi) kullanılması gerekebilir.
    - Büyük örneklem boyutlarında ise chi-kare istatistiği yeterli olabilir.
    """)

    # Özet
    st.header("📚 Özet")
    st.write("""
    Özetle, McNemar testinin bazı güçlü yönleri ve sınırlamaları vardır. Test, bağımlı örneklerle çalışırken ve ikili sonuçlarla uğraşırken oldukça etkili ve kullanışlıdır. Ancak, daha fazla kategorili veriler veya bağımsız örneklerle çalışmak için uygun değildir. Bu avantajlar ve dezavantajlar göz önünde bulundurularak, McNemar testinin ne zaman ve nasıl kullanılacağını belirlemek önemlidir.
    """)
    
    next_button("ornekler", "McNemar Testinin Matematiksel Temeli'ne Git")
