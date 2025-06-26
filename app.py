import streamlit as st
import qrcode
from datetime import datetime

st.title("QR Code Generator")

# Initialize session state
if 'clear_input' not in st.session_state:
    st.session_state.clear_input = False
if 'qr_generated' not in st.session_state:
    st.session_state.qr_generated = False

# ใช้ key ที่แตกต่างกันเมื่อต้องการ clear
input_key = "input_data_cleared" if st.session_state.clear_input else "input_data"
data = st.text_input("Enter data for QR code:", key=input_key)

# ปุ่มสำหรับสร้าง QR code
if st.button("Generate QR Code"):
    if data:
        img = qrcode.make(data)
        img_path = f"qrcodeimg/qrcode_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        img.save(img_path)

        # แสดง QR code ที่สร้างขึ้น
        st.image(img_path, caption="Generated QR Code", width=300)
        st.success("QR Code generated successfully!")

        # ทำเครื่องหมายว่าต้องการ clear input
        st.session_state.clear_input = True
        st.session_state.qr_generated = True
    else:
        st.error("Please enter some data to generate a QR code.")

# รีเซ็ต clear flag หลังจาก rerun
if st.session_state.clear_input:
    st.session_state.clear_input = False
