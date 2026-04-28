import streamlit as st

st.title("Sistem Pakar Tanaman Cabai")

st.write("Pilih gejala yang terjadi pada tanaman:")

# Input gejala
daun_menguning = st.checkbox("Daun menguning")
daun_berlubang = st.checkbox("Daun berlubang")
bercak_hitam = st.checkbox("Bercak hitam pada daun")
batang_layu = st.checkbox("Batang layu")
buah_membusuk = st.checkbox("Buah membusuk")
ada_hama = st.checkbox("Terdapat hama")
tanaman_kerdil = st.checkbox("Tanaman kerdil")

# Proses
if st.button("Diagnosa"):
    if daun_menguning and batang_layu:
        st.success("Diagnosa: Layu Fusarium\nSolusi: Gunakan fungisida dan perbaiki drainase tanah")
    
    elif daun_berlubang and ada_hama:
        st.success("Diagnosa: Serangan Ulat\nSolusi: Gunakan pestisida alami")
    
    elif bercak_hitam:
        st.success("Diagnosa: Antraknosa\nSolusi: Semprot fungisida")
    
    elif buah_membusuk:
        st.success("Diagnosa: Busuk Buah\nSolusi: Kurangi kelembapan")
    
    elif tanaman_kerdil and daun_menguning:
        st.success("Diagnosa: Kekurangan Nutrisi\nSolusi: Beri pupuk NPK")
    
    elif daun_menguning and ada_hama:
        st.success("Diagnosa: Kutu Daun\nSolusi: Gunakan insektisida")
    
    else:
        st.warning("Gejala tidak terdeteksi, silakan konsultasi lebih lanjut.")