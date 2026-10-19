import streamlit as st
import random

st.set_page_config(
    page_title="CHARACTER FACTORY",
    page_icon="🎮",
    layout="wide"
)

# ── ARCADE / FLYER STYLE ──
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Gowun+Dodum&display=swap');

.stApp {
    background-color: #101014;
    color: #f7f5ee;
    font-family: 'Gowun Dodum', sans-serif;
}
.block-container {
    max-width: 1000px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}
.arcade-header {
    background: #181820;
    border: 3px solid #ff3eaa;
    box-shadow: 6px 6px 0 #00f5ff;
    padding: 28px 20px;
    text-align: center;
    margin: 8px 0 30px;
    position: relative;
}
.arcade-mini {
    color: #c4ff38;
    font-size: 11px;
    letter-spacing: 3px;
    line-height: 2;
}
.arcade-title {
    font-family: 'Press Start 2P', monospace;
    color: #ff3eaa;
    font-size: clamp(19px, 4vw, 35px);
    line-height: 1.8;
    text-shadow: 3px 3px #00f5ff;
    margin: 14px 0;
    overflow-wrap: anywhere;
}
.arcade-subtitle {
    color: #f7f5ee;
    font-size: 14px;
    letter-spacing: 2px;
}
.flyer {
    background: #f8f0d9;
    color: #151515;
    padding: 18px;
    border: 3px dashed #ff3eaa;
    box-shadow: 5px 5px 0 #c4ff38;
    transform: rotate(-0.5deg);
    margin: 15px 0 25px;
}
.flyer-tag {
    display: inline-block;
    background: #ff3eaa;
    color: #101014;
    padding: 5px 9px;
    font-weight: bold;
    font-size: 12px;
    transform: rotate(-2deg);
}
.flyer h3 {
    font-family: 'Press Start 2P', monospace;
    font-size: 15px;
    line-height: 1.9;
    margin: 13px 0;
}
.flyer p {
    font-size: 14px;
    line-height: 1.8;
}
.section-label {
    color: #00f5ff;
    font-family: 'Press Start 2P', monospace;
    font-size: 12px;
    line-height: 2;
    border-bottom: 2px dashed #ff3eaa;
    padding-bottom: 10px;
    margin: 28px 0 18px;
}
.stTextInput label, .stSelectbox label {
    color: #c4ff38 !important;
    font-weight: bold;
}
div[data-baseweb="select"] > div {
    background: #202027;
    color: white;
    border: 1px solid #00f5ff;
    border-radius: 0;
}
.stTextInput input {
    background: #202027;
    color: #ffffff;
    border: 1px solid #00f5ff;
    border-radius: 0;
}
div.stButton > button {
    background: #ff3eaa;
    color: #101014;
    border: 2px solid #f7f5ee;
    border-radius: 0;
    font-weight: 900;
    min-height: 48px;
    box-shadow: 4px 4px 0 #00f5ff;
    transition: 0.1s;
}
div.stButton > button:hover {
    background: #c4ff38;
    color: #101014;
    border-color: #ffffff;
    box-shadow: 2px 2px 0 #ff3eaa;
}
.result-card {
    background: #191920;
    border: 2px solid #00f5ff;
    box-shadow: 6px 6px 0 #ff3eaa;
    padding: 22px;
    margin: 10px 0 25px;
}
.result-banner {
    color: #101014;
    background: #c4ff38;
    padding: 8px 12px;
    font-family: 'Press Start 2P', monospace;
    font-size: 11px;
    line-height: 1.9;
    display: inline-block;
    margin-bottom: 16px;
}
.character-name {
    color: #ff3eaa;
    font-size: 30px;
    font-weight: bold;
    overflow-wrap: anywhere;
}
.character-job {
    color: #00f5ff;
    font-size: 17px;
    margin: 10px 0;
}
.stat-line {
    border-top: 1px dashed #5b5b6a;
    padding: 10px 0;
    color: #f7f5ee;
}
.stat-label {
    color: #c4ff38;
    font-weight: bold;
}
.flying-note {
    color: #ff3eaa;
    font-family: 'Press Start 2P', monospace;
    font-size: 10px;
    line-height: 2.2;
    text-align: center;
    border: 1px dashed #ff3eaa;
    padding: 12px;
    margin-top: 28px;
}
div[data-testid="stCaptionContainer"] {
    color: #aaa8b8;
}
</style>
""", unsafe_allow_html=True)

# ── HEADER ──
st.markdown("""
<div class="arcade-header">
    <div class="arcade-mini">★ INSERT COIN · PLAYER 001 · INSERT COIN ★</div>
    <div class="arcade-title">CHARACTER<br>FACTORY</div>
    <div class="arcade-subtitle">YOUR TASTE, YOUR CHARACTER.</div>
    <div class="arcade-mini">NO RULES! JUST CREATE!</div>
</div>

<div class="flyer">
    <span class="flyer-tag">긴급 전단 / SPECIAL ISSUE</span>
    <h3>▶ 나만의 캐릭터를 만들어라!</h3>
    <p>
        당신의 취향을 입력하면 새로운 캐릭터가 출현합니다.<br>
        이름도 직업도 랜덤! 결과는 오직 운명에 맡기세요.
    </p>
    <p>★ LIMITED EDITION · CHARACTER DATA CENTER ★</p>
</div>
""", unsafe_allow_html=True)

# ── CHARACTER OPTIONS ──
names = ["유하진", "강민", "서윤", "하린", "도현"]
jobs = ["마법사", "기사", "학생", "헌터", "연구원"]

st.markdown(
    '<div class="section-label">01 / PLAYER CUSTOMIZATION</div>',
    unsafe_allow_html=True
)

left, right = st.columns(2)

with left:
    color = st.text_input(
        "▣ 좋아하는 색",
        placeholder="예: 네온 핑크, 검정, 하늘색"
    )

    personality = st.selectbox(
        "▣ 캐릭터 성격",
        ["조용함", "활발함", "냉정함", "다정함", "엉뚱함"]
    )

with right:
    genre = st.selectbox(
        "▣ 세계관 / 장르",
        ["판타지", "로맨스", "액션", "스릴러"]
    )

    st.markdown("""
    <div class="result-card">
        <div class="result-banner">SYSTEM MESSAGE</div>
        <p>캐릭터 생성 대기 중...</p>
        <p style="color:#00f5ff">STATUS : READY</p>
        <p style="color:#c4ff38">MODE : RANDOM</p>
    </div>
    """, unsafe_allow_html=True)

# ── GENERATE ──
if st.button("▶ START GAME / 캐릭터 생성!", use_container_width=True):
    st.session_state["character_result"] = {
        "name": random.choice(names),
        "job": random.choice(jobs),
        "personality": personality,
        "genre": genre,
        "color": color.strip() if color.strip() else "미지정"
    }

result = st.session_state.get("character_result")

# ── RESULT ──
if result:
    st.markdown(
        '<div class="section-label">02 / CHARACTER DATA UNLOCKED</div>',
        unsafe_allow_html=True
    )

    st.markdown(f"""
    <div class="result-card">
        <div class="result-banner">★ PLAYER DATA : UNLOCKED ★</div>
        <div class="character-name">{result["name"]}</div>
        <div class="character-job">▶ 직업 : {result["job"]}</div>
        <div class="stat-line"><span class="stat-label">PERSONALITY //</span> {result["personality"]}</div>
        <div class="stat-line"><span class="stat-label">WORLD //</span> {result["genre"]}</div>
        <div class="stat-line"><span class="stat-label">COLOR CODE //</span> {result["color"]}</div>
        <div class="stat-line"><span class="stat-label">RARITY //</span> UNKNOWN ???</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="flyer"><span class="flyer-tag">CHARACTER FILE</span>'
        '<h3>DATA SAVED!</h3>'
        '<p>새로운 이야기가 시작되었습니다. 다음 캐릭터도 생성해 보세요!</p></div>',
        unsafe_allow_html=True
    )

    if st.button("↻ RANDOMIZE! / 다시 뽑기", use_container_width=True):
        st.session_state["character_result"] = {
            "name": random.choice(names),
            "job": random.choice(jobs),
            "personality": personality,
            "genre": genre,
            "color": color.strip() if color.strip() else "미지정"
        }
        st.rerun()

st.markdown("""
<div class="flying-note">
    ★ GAME OVER? NO WAY! ★<br>
    CHARACTER FACTORY · EST. 199X<br>
    THANK YOU FOR PLAYING!
</div>
""", unsafe_allow_html=True)
