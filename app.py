import streamlit as st
import time

st.set_page_config(page_title="เกมลับ", page_icon="👻")
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    </style>
    """, unsafe_allow_html=True)

st.title("มาวัดใจกันหน่อย?")
st.write("ลองกดปุ่มด้านล่างดูสิ... ถ้ากล้าพอ")

if st.button("กดตรงนี้"):
    with st.spinner('กำลังโหลดข้อมูลลับ...'):
        time.sleep(3)
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJ4eG14bHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/12u87AYOFp8yWk/giphy.gif")
    st.subheader("555555555 ตกใจเหรอ?")
    st.balloons()