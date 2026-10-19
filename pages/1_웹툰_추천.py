import streamlit as st
import random
from pathlib import Path

st.set_page_config(
    page_title="WEBTOON ARCHIVE | 추천 자료실",
    page_icon="📚",
    layout="wide"
)

# ── 빈티지 아카이브 디자인 ──
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&display=swap');

.stApp {
    background-color: #e9e3d2;
    color: #292c20;
    font-family: 'Gowun Batang', serif;
}
.block-container {
    max-width: 1050px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}
.archive-header {
    background: #354637;
    color: #f2ead7;
    padding: 32px 28px;
    border: 3px double #d5c7a4;
    outline: 1px solid #354637;
    outline-offset: 5px;
    text-align: center;
    margin-bottom: 32px;
}
.archive-header .small {
    font-size: 12px;
    letter-spacing: 4px;
    color: #d5c7a4;
}
.archive-header h1 {
    color: #f2ead7;
    font-size: clamp(30px, 5vw, 52px);
    letter-spacing: 3px;
    margin: 12px 0;
}
.archive-header p {
    color: #e1d7bd;
    font-size: 14px;
}
.notice {
    background: #f8f2e4;
    border: 1px solid #8b8066;
    padding: 18px 22px;
    margin: 15px 0 22px 0;
    box-shadow: 4px 4px 0 #d1c7b1;
}
.notice-title {
    font-size: 12px;
    letter-spacing: 3px;
    color: #8c4236;
    font-weight: bold;
}
.section-title {
    border-bottom: 2px solid #354637;
    padding-bottom: 8px;
    margin-top: 24px;
    font-size: 22px;
    font-weight: bold;
}
.poster {
    background: #f8f2e4;
    border: 1px solid #a69a7d;
    padding: 20px;
    box-shadow: 5px 5px 0 #d1c7b1;
    margin: 10px 0;
}
.poster-stamp {
    display: inline-block;
    color: #9b4538;
    border: 2px solid #9b4538;
    padding: 3px 9px;
    font-size: 12px;
    transform: rotate(-3deg);
    letter-spacing: 2px;
}
.result-title {
    font-size: 30px;
    font-weight: bold;
    color: #354637;
    margin: 12px 0;
}
.result-description {
    font-size: 16px;
    line-height: 1.9;
    color: #454537;
}
.footer-note {
    text-align: center;
    color: #716b58;
    font-size: 12px;
    border-top: 1px dashed #a69a7d;
    padding-top: 18px;
    margin-top: 38px;
}
div.stButton > button {
    background: #354637;
    color: #f8f2e4;
    border: 1px solid #354637;
    border-radius: 0;
    padding: 10px 22px;
    font-family: 'Gowun Batang', serif;
}
div.stButton > button:hover {
    background: #52664e;
    color: white;
    border-color: #52664e;
}
div[data-baseweb="select"] > div {
    background: #f8f2e4;
    border-color: #a69a7d;
    border-radius: 0;
}
</style>
""", unsafe_allow_html=True)

# ── 작품 데이터 ──
webtoon_data = {
    "판타지": [
        {"title": "전지적 독자 시점", "description": "소설 속 세계가 현실이 된 후 살아남기 위한 이야기"},
        {"title": "화산귀환", "description": "전설의 검객이 환생해 몰락한 문파를 재건하는 무협 판타지"},
        {"title": "나 혼자만 레벨업", "description": "최약체 헌터가 특별한 능력을 얻어 성장하는 이야기"},
        {"title": "초인의 게임", "description": "초능력자들이 펼치는 생존과 경쟁의 이야기"},
        {"title": "철수를 구하시오", "description": "SF와 판타지 요소가 결합된 독특한 세계관의 작품"}
    ],
    "로맨스": [
        {"title": "작전명 순정", "description": "첫사랑과 우정을 그린 청춘 로맨스"},
        {"title": "세기말 풋사과 보습학원", "description": "1990년대를 배경으로 한 학원 로맨스"},
        {"title": "바른연애 길잡이", "description": "대학생들의 현실적인 연애 이야기를 다룬 작품"},
        {"title": "여신강림", "description": "메이크업으로 자신감을 찾은 여학생의 성장과 사랑 이야기"},
        {"title": "연애혁명", "description": "고등학생들의 사랑과 우정을 그린 학원 로맨스"}
    ],
    "액션": [
        {"title": "참교육", "description": "학교 폭력과 사회 문제를 해결하는 교육관들의 이야기"},
        {"title": "캐슬", "description": "복수를 위해 범죄 조직에 맞서는 남자의 액션 느와르"},
        {"title": "외모지상주의", "description": "두 개의 몸을 가지게 된 주인공의 성장과 격투 이야기"},
        {"title": "격기 3반", "description": "격투기를 중심으로 펼쳐지는 학원 액션물"},
        {"title": "약한영웅", "description": "약해 보이는 학생이 지능과 전략으로 싸워 나가는 이야기"}
    ],
    "스릴러": [
        {"title": "타인은 지옥이다", "description": "수상한 고시원 사람들 사이에서 벌어지는 심리 스릴러"},
        {"title": "스위트홈", "description": "사람들이 괴물로 변하는 세상에서 살아남기 위한 이야기"},
        {"title": "돼지우리", "description": "기억을 잃은 남자가 의문의 섬에서 겪는 사건들"},
        {"title": "방탈출", "description": "목숨을 건 게임과 퍼즐을 풀어나가는 스릴러"},
        {"title": "살인자ㅇ난감", "description": "우연한 살인을 계기로 연쇄 사건에 휘말리는 이야기"}
    ],
    "BL": [
        {"title": "체크메이트", "description": "복수와 집착이 얽힌 관계를 그린 작품"},
        {"title": "물가의 밤", "description": "복잡한 감정선과 관계를 중심으로 한 작품"},
        {"title": "남고 소년", "description": "고등학생들의 일상과 성장을 그린 작품"},
        {"title": "시맨틱 에러", "description": "정반대 성격의 대학생들이 만나 벌어지는 이야기"},
        {"title": "위험한 편의점", "description": "편의점 아르바이트생과 손님의 관계를 그린 작품"}
    ],
    "드라마": [
        {"title": "유미의 세포들", "description": "세포들의 시선으로 그려낸 현실적인 일상과 연애 이야기"},
        {"title": "이번 생도 잘 부탁해", "description": "전생의 기억을 가진 주인공의 사랑과 성장 이야기"},
        {"title": "정년이", "description": "국극 배우를 꿈꾸는 소녀의 성장 이야기"},
        {"title": "중증외상센터 : 골든 아워", "description": "생명을 살리기 위해 노력하는 의료진들의 이야기"},
        {"title": "가비지타임", "description": "농구부 학생들의 성장과 우정을 그린 스포츠 드라마"}
    ]
}

# 이미지 파일은 main.py와 같은 저장소 최상위 폴더에 있음
image_files = {
    "판타지": "별빛 아래 떠 있는 환상의 성채.png",
    "로맨스": "벚꽃빛 강변의 황혼.png",
    "액션": "붉은 달 아래의 종말 전투.png",
    "스릴러": "달빛 아래 유령도시의 성당 폐허.png",
    "BL": "녹빛 폐허 속의 은밀한 입맞춤.png",
    "드라마": "황금빛 노을의 꽃 테라스와 환상도시.png"
}

# 현재 파일(pages 폴더) 기준으로 저장소 최상위 폴더 찾기
root_dir = Path(__file__).resolve().parent.parent

def get_image_path(filename):
    path = root_dir / filename
    if path.exists():
        return str(path)
    return None

# ── 페이지 머리말 ──
st.markdown("""
<div class="archive-header">
    <div class="small">THE OLD WEBTOON ARCHIVE · EST. 2026</div>
    <h1>WEBTOON ARCHIVE</h1>
    <p>오래된 전단지 속에서 발견한, 당신만의 다음 이야기</p>
    <div class="small">NO. 001 — STORY RECOMMENDATION PAPER</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="notice">
    <div class="notice-title">▣ 오늘의 추천 전단 ▣</div>
    <p>취향에 맞는 장르를 고르면 자료실에서 작품 한 편을 꺼내 드립니다.</p>
    <p>종이의 흔적은 오래되어도, 이야기는 아직 끝나지 않았습니다.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">01. 취향 조사표 / READER PROFILE</div>', unsafe_allow_html=True)

left, right = st.columns(2)

with left:
    genre = st.selectbox("▣ 장르를 선택하세요", list(webtoon_data.keys()))

with right:
    mood = st.selectbox(
        "▣ 오늘 읽고 싶은 분위기",
        ["상관없음", "힐링", "성장", "피폐", "개그"]
    )

st.caption("※ 분위기는 취향 기록용 선택지이며, 현재 추천은 선택한 장르 안에서 무작위로 이루어집니다.")

if st.button("✦ 자료실에서 작품 한 편 찾기 ✦", use_container_width=True):
    st.session_state["recommended_webtoon"] = {
        "genre": genre,
        "mood": mood,
        "webtoon": random.choice(webtoon_data[genre])
    }

# ── 추천 결과 유지 및 표시 ──
result = st.session_state.get("recommended_webtoon")

if result:
    st.markdown('<div class="section-title">02. 발굴된 작품 / ARCHIVE FIND</div>', unsafe_allow_html=True)

    result_genre = result["genre"]
    webtoon = result["webtoon"]
    image_path = get_image_path(image_files[result_genre])

    image_col, text_col = st.columns([1, 1.3], gap="large")

    with image_col:
        if image_path:
            st.image(image_path, use_container_width=True)
        else:
            st.warning("이미지를 찾지 못했어요. 저장소 최상위의 이미지 파일 이름을 확인해 주세요.")

    with text_col:
        st.markdown('<div class="poster">', unsafe_allow_html=True)
        st.markdown('<span class="poster-stamp">ARCHIVE PICK</span>', unsafe_allow_html=True)
        st.markdown(f'<div class="result-title">{webtoon["title"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="result-description">{webtoon["description"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<p>분류 번호: WT-{list(webtoon_data.keys()).index(result_genre) + 1:02d}</p>', unsafe_allow_html=True)
        st.markdown(f'<p>선택한 분위기: {result["mood"]}</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    if st.button("↻ 다른 작품 다시 뽑기", use_container_width=True):
        st.session_state["recommended_webtoon"] = {
            "genre": result_genre,
            "mood": result["mood"],
            "webtoon": random.choice(webtoon_data[result_genre])
        }
        st.rerun()

st.markdown("""
<div class="footer-note">
    WEBTOON ARCHIVE · PAPER COLLECTION SERIES<br>
    오래된 종이, 새로운 이야기 · 자료실 기록은 계속됩니다.
</div>
""", unsafe_allow_html=True)
