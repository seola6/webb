import streamlit as st
import random

st.title("🎨 취향 기반 캐릭터 생성기")

color = st.text_input("좋아하는 색")

personality = st.selectbox(
    "성격",
    [
        "조용함",
        "활발함",
        "냉정함",
        "다정함",
        "엉뚱함"
    ]
)

genre = st.selectbox(
    "좋아하는 장르",
    [
        "판타지",
        "로맨스",
        "액션",
        "스릴러"
    ]
)

if st.button("생성하기"):

    names = [
        "유하진",
        "강민",
        "서윤",
        "하린",
        "도현"
    ]

    jobs = [
        "마법사",
        "기사",
        "학생",
        "헌터",
        "연구원"
    ]

    st.subheader("✨ 생성 결과")

    st.write(f"이름 : {random.choice(names)}")
    st.write(f"직업 : {random.choice(jobs)}")
    st.write(f"성격 : {personality}")

    st.write(
        f"{color} 이미지를 가진 "
        f"{genre} 장르의 캐릭터입니다."
    )
