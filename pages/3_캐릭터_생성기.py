
import streamlit as st
import random
import html

st.set_page_config(
    page_title="CHARACTER FACTORY",
    page_icon="🎮",
    layout="wide"
)

# ── ARCADE / FLYER STYLE ──
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=Gowun+Batang:wght@400;700&display=swap');

.stApp{
    background:#17130f;
    color:#f4ead2;
    font-family:'Gowun Batang',serif;
}

/* 전체 폭 */
.block-container{
    max-width:1000px;
    padding-top:2rem;
    padding-bottom:3rem;
}

/* 길드 간판 */
.guild-header{
    background:linear-gradient(180deg,#4d3319,#2b1d0f);
    border:4px solid #c79b49;
    box-shadow:0 0 25px rgba(199,155,73,.3), inset 0 0 20px rgba(255,230,170,.08);
    padding:32px;
    text-align:center;
    margin-bottom:28px;
}

.guild-mini{
    color:#d8c18a;
    letter-spacing:3px;
    font-size:12px;
}

.guild-title{
    font-family:'Cinzel',serif;
    color:#f7d36c;
    font-size:clamp(30px,5vw,52px);
    text-shadow:0 0 8px rgba(255,220,120,.35);
    margin:16px 0;
}

.guild-sub{
    color:#e9d7b0;
}

/* 양피지 */
.parchment{
    background:#efe2bf;
    color:#2a1a10;
    border:3px solid #b88b3f;
    box-shadow:6px 6px 0 #46301a;
    padding:20px;
    margin:18px 0;
}

.quest-tag{
    display:inline-block;
    background:#8f2e25;
    color:#fff6dd;
    padding:6px 10px;
    font-size:12px;
    letter-spacing:2px;
    transform:rotate(-2deg);
}

/* 제목 */
.section-label{
    font-family:'Cinzel',serif;
    color:#f3c86b;
    font-size:18px;
    border-bottom:2px solid #8b6a34;
    padding-bottom:8px;
    margin:30px 0 18px;
}

/* 입력창 */
div[data-baseweb="select"]>div,
.stTextInput input{
    background:#2b2219;
    color:white;
    border:1px solid #c79b49;
}

/* 버튼 */
.stButton>button{
    background:linear-gradient(180deg,#c79b49,#8d5d1f);
    color:#24170d;
    border:2px solid #f6dd9c;
    font-weight:bold;
    border-radius:4px;
    min-height:48px;
}

.stButton>button:hover{
    background:linear-gradient(180deg,#e2bb61,#a46b22);
}

/* 장비 보관함 */
.wardrobe{
    background:linear-gradient(180deg,#3a2818,#24170d);
    border:3px solid #7b5226;
    box-shadow:6px 6px 0 #120d09;
    padding:18px;
}

/* 슬라임 말풍선 */
.slime{
    background:#24452f;
    border-left:5px solid #66ff88;
    padding:14px;
    margin-top:14px;
    color:#d7ffe1;
}

/* 결과 카드 */
.result-card{
    background:linear-gradient(180deg,#342414,#1d140d);
    border:3px solid #d6ab59;
    box-shadow:0 0 18px rgba(214,171,89,.2);
    padding:24px;
    margin-top:16px;
}

.result-banner{
    display:inline-block;
    background:#8f2e25;
    color:#fff5dd;
    padding:6px 12px;
    letter-spacing:2px;
}

.character-name{
    font-family:'Cinzel',serif;
    color:#ffd774;
    font-size:34px;
    margin:14px 0;
}

.character-job{
    color:#bde3ff;
    font-size:18px;
}

.stat-line{
    border-top:1px dashed #8a6c44;
    padding:10px 0;
}

.stat-label{
    color:#d9b86f;
    font-weight:bold;
}

.footer-note{
    text-align:center;
    color:#b59b72;
    margin-top:34px;
    font-size:12px;
}
</style>
""",unsafe_allow_html=True)

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
        취향에 맞는 조건을 선택하고 새로운 캐릭터를 생성하세요.<br>
        성별과 이름, 직업은 랜덤! 결과는 오직 운명에 맡기세요.
    </p>
    <p>★ LIMITED EDITION · CHARACTER DATA CENTER ★</p>
</div>
""", unsafe_allow_html=True)

# ── CHARACTER DATA ──
names = [
    "유하진", "강민", "서윤", "하린", "도현",
    "윤시온", "백이안", "차유현", "한서우", "정이든",
    "서해온", "강이현", "문시율", "류하온", "진유안"
]

jobs_by_genre = {
    "판타지": ["마법사", "기사", "마왕의 후계자", "연금술사", "용병"],
    "로맨스": ["대학생", "작가", "아이돌 연습생", "카페 직원", "배우"],
    "액션": ["헌터", "격투가", "경찰", "정보원", "용병"],
    "스릴러": ["탐정", "기자", "형사", "연구원", "목격자"]
}

# ── PLAYER CUSTOMIZATION ──
st.markdown(
    '<div class="section-label">01 / PLAYER CUSTOMIZATION</div>',
    unsafe_allow_html=True
)

left, right = st.columns(2)

with left:
    color = st.text_input(
        "▣ 좋아하는 색",
        placeholder="예: 네온 핑크, 검정, 하늘색",
        key="character_color"
    )

    hair = st.selectbox(
        "▣ 선호하는 머리 길이",
        ["긴 머리", "숏컷"],
        key="character_hair"
    )

with right:
    genre = st.selectbox(
        "▣ 세계관 / 장르",
        ["판타지", "로맨스", "액션", "스릴러"],
        key="character_genre"
    )

    st.markdown("""
    <div class="result-card">
        <div class="result-banner">SYSTEM MESSAGE</div>
        <p>캐릭터 생성 대기 중...</p>
        <p style="color:#00f5ff">STATUS : READY</p>
        <p style="color:#c4ff38">MODE : RANDOM</p>
    </div>
    """, unsafe_allow_html=True)

# ── CHARACTER GENERATOR ──
def generate_character(color, hair, genre):
    return {
        "name": random.choice(names),
        "gender": random.choice(["남성", "여성"]),
        "job": random.choice(jobs_by_genre[genre]),
        "hair": hair,
        "genre": genre,
        "color": color.strip() if color.strip() else "미지정",
        "rarity": random.choices(
            ["COMMON", "RARE", "EPIC", "LEGENDARY"],
            weights=[55, 27, 14, 4],
            k=1
        )[0]
    }

# ── GENERATE ──
if st.button(
    "▶ START GAME / 캐릭터 생성!",
    use_container_width=True
):
    st.session_state["character_result"] = generate_character(
        color, hair, genre
    )

# 이전 버전의 캐릭터 데이터도 안전하게 처리
result = st.session_state.get("character_result")

if result and not all(
    key in result
    for key in ["name", "gender", "job", "hair", "genre", "color", "rarity"]
):
    del st.session_state["character_result"]
    result = None

# ── RESULT ──
if result:
    st.markdown(
        '<div class="section-label">02 / CHARACTER DATA UNLOCKED</div>',
        unsafe_allow_html=True
    )

    st.markdown(f"""
    <div class="result-card">
        <div class="result-banner">★ PLAYER DATA : UNLOCKED ★</div>
        <div class="character-name">{html.escape(str(result["name"]))}</div>
        <div class="character-job">▶ 직업 : {html.escape(str(result["job"]))}</div>
        <div class="stat-line">
            <span class="stat-label">GENDER //</span>
            {html.escape(str(result["gender"]))}
        </div>
        <div class="stat-line">
            <span class="stat-label">HAIR STYLE //</span>
            {html.escape(str(result["hair"]))}
        </div>
        <div class="stat-line">
            <span class="stat-label">WORLD //</span>
            {html.escape(str(result["genre"]))}
        </div>
        <div class="stat-line">
            <span class="stat-label">COLOR CODE //</span>
            {html.escape(str(result["color"]))}
        </div>
        <div class="stat-line">
            <span class="stat-label">RARITY //</span>
            {html.escape(str(result["rarity"]))}
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="flyer">
        <span class="flyer-tag">CHARACTER FILE</span>
        <h3>DATA SAVED!</h3>
        <p>새로운 이야기가 시작되었습니다. 다음 캐릭터도 생성해 보세요!</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "↻ RANDOMIZE! / 다시 뽑기",
        use_container_width=True
    ):
        st.session_state["character_result"] = generate_character(
            color, hair, genre
        )
        st.rerun()

st.markdown("""
<div class="flying-note">
    ★ GAME OVER? NO WAY! ★<br>
    CHARACTER FACTORY · EST. 199X<br>
    THANK YOU FOR PLAYING!
</div>
""", unsafe_allow_html=True)
