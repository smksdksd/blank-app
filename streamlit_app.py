import streamlit as st
import time

# 세션 상태에 초기화된 값 저장
if "initialized" not in st.session_state:
    st.session_state.initialized = False

def mainpage():
    # 버튼이 클릭되었을 때 UI를 숨기고 상태 변경
    if st.button("클릭하세요"):
        st.write("잘하셨습니다!")
        st.session_state.initialized = True  # 상태를 True로 바꾸어 UI 숨김
        st.experimental_rerun()  # 페이지 새로고침

    # UI가 사라지도록 설정
    if st.session_state.initialized:
        st.empty()  # UI를 비우는 역할
        st.write("모든 UI가 사라졌습니다.")
    else:
        # 초기 UI 구성
        st.title("🎈 선준이의 천번째 앺!")
        st.header("안녕하세요! 저는 박선준임니다.")
        st.write("버튼을 클릭해주세요!")
        
        # 여기에 다른 버튼들 추가 가능
        if st.button("클릭"):
            st.write("그 버튼 아닌데!")

        if st.button("클릭해주세요"):
            st.code("""
import streamlit as st
st.title('ㅋㅋ 그거 아닌데데')
""", language="python")

        if st.button("클릭인가요?"):
            st.link_button("혹시 이건가?", "https://www.google.com")

        if st.button("클릭입니다"):
            tab1, tab2 = st.tabs(["탭 1", "탭 2"])  # 2개의 탭 생성

            with tab1:
                st.write("이거")  # 첫 번째 탭에 표시할 내용
            with tab2:
                st.write("아닌데.")  # 두 번째 탭에 표시할 내용

        # 성별 선택
        gender = st.radio("성별을 선택하세요", ["남성", "여성", "기타"])
        if gender == "기타":
            st.write("그런 성별은 없습니다.")
        elif gender == "여성":
            st.write("선택한 성별:", gender)
        elif gender == "남성":
            st.write("선택한 성별:", gender)

mainpage()
