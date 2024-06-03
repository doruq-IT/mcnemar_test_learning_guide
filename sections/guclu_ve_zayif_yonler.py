import streamlit as st

def goster_guclu_ve_zayif_yonler():
    # Başlık ve Giriş
    st.title("💪 McNemar Testinin Güçlü ve Zayıf Yönleri")

    # Avantajlar
    st.header("✅ Avantajları")
    st.write("McNemar testinin bazı önemli avantajları vardır:")

    st.subheader("1. Bağımlı Örnekler İçin Uygunluk")
    st.markdown("""
    - Aynı bireylerin iki farklı zamanda veya durumda ölçülen sonuçlarını karşılaştırmak için idealdir.
    """)

    st.subheader("2. İkili Sonuçlar İçin Tasarlanmış")
    st.markdown("""
    - "Evet/Hayır", "Başarılı/Başarısız" gibi ikili sonuçlar için uygundur.
    """)

    st.subheader("3. Kolay Hesaplama")
    st.markdown("""
    - Matematiksel hesaplamaları basittir ve manuel olarak yapılabilir.
    """)

    st.subheader("4. Küçük Örneklemlerde Doğru Sonuçlar")
    st.markdown("""
    - Küçük örneklem boyutlarında binom testi ile doğru sonuçlar verir.
    """)

    # Dezavantajlar ve Sınırlamalar
    st.header("⚠️ Dezavantajları ve Sınırlamaları")
    st.write("McNemar testinin bazı dezavantajları da vardır:")

    st.subheader("1. Yalnızca İkili Sonuçlarla Sınırlı")
    st.markdown("""
    - Yalnızca ikili sonuçlarla çalışabilir.
    """)

    st.subheader("2. Bağımlı Örnekler Gerektirir")
    st.markdown("""
    - Verilerin bağımlı örnekler olması gerekir.
    """)

    st.subheader("3. Yalnızca 2x2 Tablo Kullanımı")
    st.markdown("""
    - Sadece 2x2 kontenjans tablolarıyla çalışır.
    """)

    st.subheader("4. Küçük Örneklem Boyutlarında Hassasiyet")
    st.markdown("""
    - Küçük örneklem boyutlarında test sonuçları hassas olabilir.
    """)

    # Özet
    st.header("📚 Özet")
    st.write("""
    McNemar testi, bağımlı örneklerle çalışırken ve ikili sonuçlarla uğraşırken etkilidir. Ancak, daha fazla kategorili veriler veya bağımsız örneklerle çalışmak için uygun değildir. Bu avantajlar ve dezavantajlar göz önünde bulundurularak, McNemar testinin ne zaman ve nasıl kullanılacağını belirlemek önemlidir.
    """)
