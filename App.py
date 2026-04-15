import streamlit as st

# Judul
st.title("Sistem Rekomendasi Tanaman")

st.write("Pilih kondisi rumah Anda, dan dapatkan rekomendasi tanaman yang cocok!")

# Input user
cahaya = st.selectbox(
    "Kondisi Cahaya Rumah:",
    ["Terang", "Sedang", "Minim"]
)

perawatan = st.selectbox(
    "Waktu Perawatan:",
    ["Sering", "Jarang"]
)

tujuan = st.selectbox(
    "Tujuan:",
    ["Hiasan", "Kesehatan (Penyaring Udara)"]
)

# Tombol
if st.button("Dapatkan Rekomendasi"):

    # Logika IF-ELSE
    if cahaya == "Terang":
        if perawatan == "Sering":
            if tujuan == "Hiasan":
                hasil = "Tanaman: Monstera atau Bougenville"
            else:
                hasil = "Tanaman: Lidah Mertua (Sansevieria)"
        else:
            hasil = "Tanaman: Kaktus atau Sukulen"

    elif cahaya == "Sedang":
        if perawatan == "Sering":
            hasil = "Tanaman: Peace Lily atau Calathea"
        else:
            hasil = "Tanaman: Sirih Gading"

    else:  # Minim cahaya
        if perawatan == "Sering":
            hasil = "Tanaman: Pakis"
        else:
            hasil = "Tanaman: ZZ Plant (Zamioculcas)"

    # Output
    st.success(hasil)
