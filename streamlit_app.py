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

# 여러 옵션 중 하나 선택
gender = st.radio("성별을 선택하세요", ["남성", "여성", "기타"])
if gender == "기타":
    st.write("그런 성별은 없습니다.")
else:
    st.write("선택한 성별:", gender)

