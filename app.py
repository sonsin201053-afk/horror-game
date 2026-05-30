import streamlit as st

st.stitle("ยินดีต้อนรับสู่เว็ปปัญญาอ่อน")

username = st.test.input("กรอกชื่อก่อนนนนนน")

if st.button("งั้นมาเริ่มกันเลย"):
    if username:
        st.write(f"สวัสดีค้าบบ {username} เซอร์ไพร์อยู่ข้างหน้า")
        st.ballons()
    else:
        st.error("รีบไปไหนกรอกชื่อก่อนเฮ้ย")    