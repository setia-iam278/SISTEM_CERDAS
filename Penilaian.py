import streamlit as st
import pandas as pd

# =========================
# DATA SEMENTARA (DATABASE)
# =========================
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Nama", "Nilai", "Grade", "Keterangan"])

# =========================
# LOGIN SEDERHANA
# =========================
def login():
    st.title("Login Sistem")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "123":
            st.session_state.login = True
            st.success("Login berhasil!")
        else:
            st.error("Username atau password salah!")

# =========================
# RULE-BASED SYSTEM
# =========================
def hitung_grade(nilai):
    if nilai >= 85:
        return "A", "Sangat Baik"
    elif nilai >= 75:
        return "B", "Baik"
    elif nilai >= 65:
        return "C", "Cukup"
    elif nilai >= 50:
        return "D", "Kurang"
    else:
        return "E", "Sangat Kurang"

# =========================
# CRUD DATA
# =========================
def dashboard():
    st.title("Dashboard Penilaian Mahasiswa")

    menu = st.sidebar.selectbox("Menu", ["Tambah Data", "Lihat Data", "Hapus Data"])

    # ➕ CREATE
    if menu == "Tambah Data":
        st.subheader("Input Nilai Mahasiswa")

        nama = st.text_input("Nama Mahasiswa")
        nilai = st.number_input("Nilai", 0, 100)

        if st.button("Simpan"):
            grade, ket = hitung_grade(nilai)

            data_baru = {
                "Nama": nama,
                "Nilai": nilai,
                "Grade": grade,
                "Keterangan": ket
            }

            st.session_state.data = pd.concat(
                [st.session_state.data, pd.DataFrame([data_baru])],
                ignore_index=True
            )

            st.success("Data berhasil disimpan!")

    # 📄 READ
    elif menu == "Lihat Data":
        st.subheader("Data Mahasiswa")
        st.dataframe(st.session_state.data)

    # ❌ DELETE
    elif menu == "Hapus Data":
        st.subheader("Hapus Data")

        nama = st.selectbox("Pilih Nama", st.session_state.data["Nama"].unique())

        if st.button("Hapus"):
            st.session_state.data = st.session_state.data[
                st.session_state.data["Nama"] != nama
            ]
            st.success("Data berhasil dihapus!")

# =========================
# MAIN APP
# =========================
if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    login()
else:
    dashboard()