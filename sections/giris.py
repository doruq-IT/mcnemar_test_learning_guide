import streamlit as st

def goster_giris():
    # Başlık ve Giriş
    st.title("🔍 McNemar Testi Öğrenme Rehberi")
    st.markdown("""
    ### 💡 Hoş Geldiniz!
    Bu rehber, **McNemar testinin** ne olduğunu, nasıl uygulanacağını ve sonuçların nasıl yorumlanacağını öğrenmek isteyenler için hazırlanmıştır.
    Aşağıdaki menüyü kullanarak rehberdeki konulara göz atabilirsiniz.
    """)
    
    # Bölüm 1: McNemar Testinin Tanımı
    st.header("📊 McNemar Testinin Tanımı")
    st.write("""
    McNemar testi, bağımlı iki ikili veri kümesi arasındaki oranları karşılaştırmak için kullanılan bir istatistiksel testtir. Bu test, özellikle çift-yönlü tablo verilerinde kullanışlıdır ve belirli bir tedavi veya müdahalenin etkisini değerlendirmek amacıyla sıklıkla kullanılır. McNemar testi, örneğin aynı bireylerin iki farklı zaman noktası veya iki farklı koşul altındaki sonuçlarını karşılaştırmak için idealdir.
    """)

    # Görsel veya İllüstrasyon
    st.image("https://www.verywellmind.com/thmb/Wj-Ks0y3OZ9ePxP5KCEc6R0y9G4=/2000x2000/smart/filters:no_upscale()/GettyImages-1256453932-b32a8a4b8b064a9a89ab1640a37843b1.jpg", caption="McNemar Testinin Kullanım Alanları")

    # Bölüm 2: Kullanım Alanları
    st.header("🌐 Kullanım Alanları")
    st.write("""
    McNemar testi, birçok farklı alanda kullanılabilir. İşte birkaç örnek:
    - **Tıp ve Sağlık Araştırmaları**: Hastaların tedaviye verdikleri yanıtların değerlendirilmesi.
    - **Psikoloji ve Eğitim**: Öğrencilerin iki farklı öğrenme yöntemine verdikleri tepkilerin karşılaştırılması.
    - **Sosyal Bilimler**: Sosyal davranış değişikliklerinin iki farklı zaman diliminde incelenmesi.
    - **Pazarlama Araştırmaları**: Tüketici tercih ve alışkanlıklarının iki farklı kampanya arasında karşılaştırılması.
    """)

    # İlginç Gerçekler
    st.header("📌 İlginç Gerçekler")
    st.write("""
    - McNemar testi, özellikle klinik deneylerde sıklıkla kullanılır.
    - İki farklı zaman diliminde aynı grubun verilerini karşılaştırmak için idealdir.
    - Psikoloji ve eğitimde öğrenci performanslarını değerlendirmek için yaygın olarak kullanılır.
    """)

    # Ek Bilgi Butonu
    if st.button('📚 Daha Fazla Bilgi Edinin'):
        st.write("""
        McNemar testi hakkında daha fazla bilgi edinmek için rehberimizin diğer bölümlerine göz atabilirsiniz. Her bölümde testin farklı yönlerini keşfedecek ve nasıl uygulanacağını adım adım öğreneceksiniz.
        """)

# main.py dosyasında gerekli importların ve fonksiyon çağrılarının yapıldığından emin olun
