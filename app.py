import streamlit as st

st.set_page_config(page_title="채유니의 수학교실", page_icon="👋")
st.title("채유니의 수학교실👋")
st.write("안녕하세요. 반갑습니다 !! ")

name = st.text_input("이름을 알려주세용!!!!!!!!!!")
if name:
    st.success(f"사랑해 "+name)