import streamlit as st

st.title("🎈 선준이의 첫번째 앱!")
st.write(
    "안녕하세요! 반갑습니다. 저는 박선준입니다."
)
if st.button("클릭하세요")==1:
    st.write("이 버튼입니다!")

if st.button("클릭")==1:
    st.write("그 버튼이 아닙니다.")

if st.button("클릭해주세요")==1:
    st.write("그 버튼이 아닙니다.")

if st.button("클릭인가요?")==1:
    st.write("그 버튼이 아닙니다.")

if st.button("클릭입니다")==1:
    st.write("그 버튼이 아닙니다.")

