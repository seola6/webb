import streamlit as st

st.title("🏆 요일별 웹툰 랭킹")

day = st.selectbox(
    "요일 선택",
    [
        "월요일",
        "화요일",
        "수요일",
        "목요일",
        "금요일",
        "토요일",
        "일요일"
    ]
)

ranking_data = {
    "월요일": [],
    "화요일": [],
    "수요일": [],
    "목요일": [],
    "금요일": [],
    "토요일": [],
    "일요일": []
}

ranking = ranking_data.get(day, [])

if ranking:

    for i, title in enumerate(ranking, start=1):
        st.write(f"{i}위 - {title}")

else:
    st.info("랭킹 데이터를 추가해주세요.")
