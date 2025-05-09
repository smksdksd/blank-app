import streamlit as st

# 초기값 설정
if "count" not in st.session_state:
    st.session_state.count = 0

st.write(f"카운트: {st.session_state.count}")

# 버튼으로 값 증가
if st.button("+1"):
    st.session_state.count += 1

# 초기화 버튼
if st.button("초기화"):
    for key in st.session_state.keys():
        del st.session_state[key]
    st.experimental_rerun()  # 페이지 전체 새로고침
