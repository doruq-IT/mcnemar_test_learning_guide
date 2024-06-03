import streamlit as st
from sections import giris, mcnemar_temelleri, matematiksel_temel, test_adimlari, testin_yorumu, python_uygulama, guclu_ve_zayif_yonler, ornekler, sonuc, sorular

# Sayfa Başlığı
st.title("McNemar Testi Öğrenme Rehberi")
st.write("""
Bu rehber, McNemar testinin ne olduğunu, nasıl uygulanacağını ve sonuçların nasıl yorumlanacağını öğrenmek isteyenler için hazırlanmıştır.
Soldaki menüyü kullanarak rehberdeki konulara göz atabilirsiniz.
""")

# Menü
menu = ["Giriş", "McNemar Testinin Temelleri", "McNemar Testinin Matematiksel Temeli", 
        "McNemar Testinin Güçlü ve Zayıf Yönleri", "McNemar Testinin Adımları", 
        "Uygulamalı Örnekler", "McNemar Testinin Yorumlanması", 
        "McNemar Testinin Python ile Uygulanması", "Sıkça Sorulan Sorular (SSS)",
         "Sonuç ve Özet"]

choice = st.sidebar.selectbox("Bölümler", menu)

if choice == "Giriş":
    giris.goster_giris()
elif choice == "McNemar Testinin Temelleri":
    mcnemar_temelleri.goster_temeller()
elif choice == "McNemar Testinin Matematiksel Temeli":
    matematiksel_temel.goster_matematiksel_temel()
elif choice == "McNemar Testinin Adımları":
    test_adimlari.goster_test_adimlari()
elif choice == "McNemar Testinin Yorumlanması":
    testin_yorumu.goster_testin_yorumu()
elif choice == "McNemar Testinin Python ile Uygulanması":
    python_uygulama.goster_python_uygulama()
elif choice == "McNemar Testinin Güçlü ve Zayıf Yönleri":
    guclu_ve_zayif_yonler.goster_guclu_ve_zayif_yonler()
elif choice == "Uygulamalı Örnekler":
    ornekler.goster_ornekler()
elif choice == "Sonuç ve Özet":
    sonuc.goster_sonuc()
elif choice == "Sıkça Sorulan Sorular (SSS)":
    sorular.goster_sorular()
