import streamlit as st
import random

st.title("🎯 웹툰 추천")

genre = st.selectbox(
    "장르 선택",
    ["판타지", "로맨스", "액션", "드라마", "스릴러"]
)

mood = st.selectbox(
    "분위기 선택",
    ["힐링", "성장", "피폐", "개그"]
)

if st.button("추천 받기"):

    # 여기에 데이터 추가
    webtoon_data = {
        "판타지": [],
        "로맨스": [],
        "액션": [],
        "드라마": [],
        "스릴러": []
    }

    result = webtoon_data.get(genre, [])

    if result:
        webtoon = random.choice(result)

        st.success(webtoon["title"])
        st.write(webtoon["description"])

    else:
        st.warning("데이터를 추가해주세요.")
