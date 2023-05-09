import streamlit as st
st.set_page_config(page_title="blablabla",page_icon=":microscope:")




menu = ["Debit Air Sungai","Volume","Artikel"]
choice = st.sidebar.selectbox("Tentukan Pilihan",menu)

if choice == "Volume":
    st.title("PERHITUNGAN AIR PERMUKAAN")
    st.title("Menghitung volume")

    panjang = st.number_input("Masukkan panjang (m): ", min_value=0.0, step=0.1)
    lebar = st.number_input("Masukkan lebar (m): ", min_value=0.0, step=0.1)
    kedalaman = st.number_input("Masukkan kedalaman (m): ", min_value=0.0, step=0.1)

    if st.button("calculate"):
        volume = panjang * lebar * kedalaman
        st.write(f"Hasil Volume adalah {volume} m³")

elif choice == "Debit Air Sungai":
    st.title("PERHITUNGAN AIR PERMUKAAN")
    st.title("Menghitung Debit Air Sungai")

    volume = st.number_input("Masukkan volume (m³): ", min_value=0.0, step=0.1)
    waktu = st.number_input("Masukkan waktu (detik): ", min_value=0.0, step=0.1)

    if st.button("calculate"):
        debit = volume / waktu
        st.write(f"Hasil Debit adalah {debit} M³/detik")
        
elif choice == "Artikel":
    st.title("TEKNIK PENGAMBILAN SAMPEL AIR PERMUKAAN")
    
    st.subheader("Pengertian Air Permukaan – Karakteristik, Kualitas, Debit, Pengolahan, Pengukuran, Contoh")
    st.write("Air permukaan merupakan air yang terkumpul di atas tanah atau di mata air, sungai danau, lahan basah atau laut. Air permukaan berhubungan dengan air bawah tanah atau air atmosfer. Air permukaan dapat dibedakan menjadi dua jenis yaitu: Perairan Darat dan Perairan Laut.")
    st.write("Perairan Darat adalah air permukaan yang berada di atas daratan, misalnya seperti rawa-rawa, danau, sungai, dan lain sebagainya.")
    st.write("Perairan Laut adalah air permukaan yang berada di lautan luas.")
    st.write("Air permukaan dapat dibedakan menjadi dua jenis yaitu:")
    
    st.subheader("Perairan Darat")
    st.write("Perairan darat adalah air permukaan yang berada di atas daratan, misalnya seperti rawa-rawa, danau, sungai, dan lain sebagainya.")
    
    st.subheader("Perairan Laut")
    st.write("Perairan laut adalah air permukaan yang berada di lautan luas. Contohnya seperti air laut yang berada di laut.")
    
    st.subheader("Menghitung Debit Air Permukaan")
    st.write("Debit adalah jumlah aliran air (volume) yang mengalir melalui suatu penampang dalam waktu tertentu, umumnya dinyatakan dalam satuan volume/waktu yaitu (m3/detik)."
    
             


