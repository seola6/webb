import time
import streamlit as st
import random

st.set_page_config(
    page_title="WEBTOON ROULETTE",
    page_icon="🎰",
    layout="wide"
)

# ── 웹툰 데이터 ──
webtoon_data = {
    "전체": [
        "전지적 독자 시점", "화산귀환", "나 혼자만 레벨업",
        "초인의 게임", "철수를 구하시오", "작전명 순정",
        "물가의 밤", "체크메이트", "남고소년",
        "외모지상주의", "광마회귀", "나노마신",
        "상남자", "재벌집 막내아들", "별을 품은 소드마스터"
    ],
    "판타지": [
        "전지적 독자 시점", "화산귀환", "나 혼자만 레벨업",
        "초인의 게임", "철수를 구하시오"
    ],
    "로맨스": [
        "작전명 순정", "시든 꽃에 눈물을",
        "럭키비치", "황금빛 노을", "로맨스 판타지"
    ],
    "액션": [
        "외모지상주의", "광마회귀", "나노마신",
        "상남자", "절대회귀"
    ],
    "스릴러": [
        "조의 영역", "범죄도시0", "44교시 생존수업",
        "종말이 찾아왔다", "싸이코패스 in 무림"
    ],
    "BL": [
        "물가의 밤", "체크메이트", "남고소년",
        "야화첩", "징크스"
    ],
    "드라마": [
        "재벌집 막내아들", "마흔 즈음에",
        "육아일기", "나의 경험", "시한부 천재가 살아남는 법"
    ]
}

# ── 디자인 ──
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Nanum+Gothic+Coding:wght@400;700&display=swap');

.stApp {
    background:
        radial-gradient(ellipse at top, #30204a 0%, #11101b 48%, #08090e 100%);
    color: #f8f0dc;
}

.block-container {
    max-width: 1000px;
    padding-top: 2rem;
}

h1, h2, h3 {
    font-family: 'Black Han Sans', sans-serif !important;
}

.roulette-banner {
    border: 2px solid #ff4fd8;
    border-radius: 8px;
    padding: 25px 18px;
    text-align: center;
    background: linear-gradient(135deg, #271633, #15192e);
    box-shadow: 0 0 18px #ff4fd844, inset 0 0 18px #6af7ff15;
    margin-bottom: 20px;
}

.roulette-title {
    color: #ff70df;
    font-size: clamp(30px, 5vw, 48px);
    text-shadow: 3px 3px #57234d, 0 0 15px #ff4fd8;
    letter-spacing: 2px;
}

.roulette-subtitle {
    color: #9efaff;
    font-family: 'Nanum Gothic Coding', monospace;
    font-size: 13px;
    letter-spacing: 2px;
}

.ticket {
    background: #f4e7c8;
    color: #251b2c;
    border: 3px dashed #a74787;
    border-radius: 6px;
    padding: 28px 20px;
    text-align: center;
    margin: 15px 0;
    box-shadow: 6px 6px 0 #ff4fd833;
}

.ticket-label {
    font-family: 'Nanum Gothic Coding', monospace;
    font-size: 12px;
    color: #a74787;
    letter-spacing: 3px;
}

.ticket-title {
    font-family: 'Black Han Sans', sans-serif;
    font-size: clamp(25px, 4vw, 38px);
    margin: 14px 0;
    overflow-wrap: anywhere;
}

.ticket-bottom {
    border-top: 1px dashed #a74787;
    padding-top: 12px;
    font-size: 12px;
    color: #59435b;
}

.stButton > button {
    background: linear-gradient(90deg, #ff4fd8, #8d73ff) !important;
    color: white !important;
    border: 1px solid #ffb4ef !important;
    border-radius: 5px !important;
    font-family: 'Black Han Sans', sans-serif !important;
    font-size: 19px !important;
    min-height: 52px;
    box-shadow: 0 0 12px #ff4fd844;
    transition: 0.2s;
}

.stButton > button:hover {
    border-color: #9efaff !important;
    box-shadow: 0 0 22px #ff4fd899;
    transform: translateY(-2px);
}

div[data-baseweb="select"] > div {
    background-color: #201c30;
    border-color: #8d73ff;
    color: #fff;
}

div[data-testid="stMarkdownContainer"] p {
    line-height: 1.7;
}
</style>
""", unsafe_allow_html=True)

# ── 헤더 ──
st.markdown("""
<div class="roulette-banner">
    <div class="roulette-subtitle">★ WEBTOON ARCHIVE · SPECIAL MACHINE ★</div>
    <div class="roulette-title">🎰 WEBTOON ROULETTE</div>
    <div class="roulette-subtitle">오늘 당신이 읽게 될 작품은?</div>
</div>
""", unsafe_allow_html=True)

st.markdown(
    "##### ▣ 오늘의 운명을 뽑아 보세요."
)

st.write(
    "무엇을 읽을지 고민될 때 사용하는 웹툰 추첨기입니다. "
    "장르를 선택하고 버튼을 눌러 보세요!"
)

# ── 장르 선택 ──
genre = st.selectbox(
    "▣ 추첨할 장르",
    list(webtoon_data.keys())
)

st.markdown("---")

# 세션 상태 초기화
if "roulette_result" not in st.session_state:
    st.session_state.roulette_result = None

if "roulette_previous" not in st.session_state:
    st.session_state.roulette_previous = None

# ── 룰렛 버튼 ──
left, center, right = st.columns([1, 2, 1])

with center:
    spin = st.button("🎰  룰렛 돌리기!", use_container_width=True)

if spin:
    candidates = webtoon_data[genre].copy()

    # 같은 장르에서 다시 돌릴 때 직전 결과가 있으면 가능하면 다른 작품 선택
    previous = st.session_state.roulette_previous
    if previous in candidates and len(candidates) > 1:
        candidates.remove(previous)

    result = random.choice(candidates)
    st.session_state.roulette_result = result
    st.session_state.roulette_previous = result

# ── 결과 티켓 ──
if st.session_state.roulette_result:
    result = st.session_state.roulette_result

    st.markdown(f"""
    <div class="ticket">
        <div class="ticket-label">★ YOUR NEXT WEBTOON ★</div>
        <div class="ticket-title">「 {result} 」</div>
        <div class="ticket-bottom">
            SELECTED FROM WEBTOON ARCHIVE · 장르: {genre}
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.success("오늘의 작품이 선정되었습니다! 마음에 들지 않으면 한 번 더 돌려 보세요.")

else:
    st.markdown("""
    <div class="ticket">
        <div class="ticket-label">READY?</div>
        <div class="ticket-title">운명의 버튼을 누르세요!</div>
        <div class="ticket-bottom">
            YOUR NEXT STORY IS WAITING...
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.caption(
    "WEBTOON ARCHIVE © · 작품 목록은 예시 데이터이며, "
    "실시간 인기 순위나 플랫폼 공식 목록이 아닙니다."
)
