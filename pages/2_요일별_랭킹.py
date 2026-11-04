
import streamlit as st

st.set_page_config(
    page_title="WEBTOON ARCHIVE | 요일별 랭킹",
    page_icon="🏆",
    layout="wide"
)

# ─────────────────────────
# CSS 디자인
# ─────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=DM+Serif+Display&display=swap');

.stApp {
    background: #e9e3d2;
    color: #354637;
    font-family: 'Gowun Batang', serif;
}

.block-container {
    max-width: 1150px;
    padding-top: 1rem;
    padding-bottom: 1rem;
}

header[data-testid="stHeader"] {
    background: transparent;
}

/* ── 사이드바 ── */
section[data-testid="stSidebar"] {
    background: #354637;
    border-right: 3px double #c6ad6c;
}

section[data-testid="stSidebar"] > div {
    background: #354637;
}

section[data-testid="stSidebar"] * {
    color: #f4eddd;
}

section[data-testid="stSidebar"] a:hover {
    background: #53664b;
    color: #f2d47b !important;
}

section[data-testid="stSidebar"] a[aria-current="page"] {
    background: #53664b;
    border-left: 3px solid #eacb69;
}

section[data-testid="stSidebar"] hr {
    border-color: #a99b70;
}

section[data-testid="stSidebar"] [data-testid="stSidebarContent"]::before {
    content: "✦ WEBTOON ARCHIVE ✦";
    display: block;
    color: #eacb69;
    text-align: center;
    font-family: 'DM Serif Display', serif;
    font-size: 15px;
    letter-spacing: 2px;
    padding: 18px 5px;
    border-bottom: 1px solid #9c916c;
    margin-bottom: 15px;
}

/* ── 별 배경 ── */
.star-field {
    position: fixed;
    inset: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    pointer-events: none;
    z-index: 9999;
}

.star {
    position: absolute;
    color: #e4b936;
    font-size: 25px;
    opacity: 0;
    text-shadow:
        0 0 5px #f5d66d,
        0 0 12px #eacb69,
        0 0 22px #d9a92e;
    animation: twinkle 3s ease-in-out infinite,
               float-star 9s ease-in-out infinite;
}

.star:nth-child(1)  { left: 5%; top: 15%; animation-delay: 0s; }
.star:nth-child(2)  { left: 15%; top: 70%; animation-delay: 1s; }
.star:nth-child(3)  { left: 25%; top: 30%; animation-delay: 2s; }
.star:nth-child(4)  { left: 35%; top: 85%; animation-delay: .5s; }
.star:nth-child(5)  { left: 45%; top: 12%; animation-delay: 1.5s; }
.star:nth-child(6)  { left: 55%; top: 65%; animation-delay: 2.5s; }
.star:nth-child(7)  { left: 65%; top: 25%; animation-delay: .8s; }
.star:nth-child(8)  { left: 75%; top: 80%; animation-delay: 3s; }
.star:nth-child(9)  { left: 85%; top: 18%; animation-delay: 1.2s; }
.star:nth-child(10) { left: 95%; top: 55%; animation-delay: 2.2s; }
.star:nth-child(11) { left: 12%; top: 42%; animation-delay: 1.8s; }
.star:nth-child(12) { left: 92%; top: 88%; animation-delay: 3.2s; }
.star:nth-child(13) { left: 40%; top: 48%; animation-delay: .7s; }
.star:nth-child(14) { left: 70%; top: 45%; animation-delay: 2.7s; }
.star:nth-child(15) { left: 30%; top: 8%; animation-delay: 1.4s; }
.star:nth-child(16) { left: 60%; top: 90%; animation-delay: 3.5s; }

@keyframes twinkle {
    0%, 100% {
        opacity: .25;
        transform: scale(.7) rotate(0deg);
    }
    50% {
        opacity: 1;
        transform: scale(1.5) rotate(45deg);
    }
}

@keyframes float-star {
    0%, 100% { margin-top: 0; }
    50% { margin-top: -25px; }
}

/* ── 머리말 ── */
.paper-header {
    background: #354637;
    color: #f4eddd;
    text-align: center;
    padding: 20px 15px 17px;
    border: 1px solid #b9a982;
    outline: 3px double #354637;
    outline-offset: 3px;
    margin: 5px 0 17px;
}

.eyebrow {
    color: #e4c66b;
    font-size: 9px;
    letter-spacing: 4px;
}

.paper-header h1 {
    color: #f4eddd;
    font-family: 'DM Serif Display', serif;
    font-size: clamp(30px, 4vw, 43px);
    letter-spacing: 3px;
    margin: 7px 0;
}

.paper-header p {
    color: #e3d8bd;
    font-size: 12px;
    margin: 5px 0;
}

/* 발행 정보 */
.edition {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 8px;
    padding: 7px 2px;
    margin: 10px 0 13px;
    border-top: 1px solid #a99b7c;
    border-bottom: 3px double #354637;
    font-size: 10px;
    letter-spacing: 1px;
}

/* 안내문 */
.notice {
    background: #f8f2e5;
    border: 1px solid #c2b496;
    box-shadow: 3px 3px 0 #d5cbb7;
    padding: 10px 15px;
    margin: 12px 0 18px;
    color: #454537;
    font-size: 12px;
}

.notice-label {
    color: #a34d3e;
    font-size: 10px;
    font-weight: bold;
    letter-spacing: 2px;
    margin-bottom: 3px;
}

/* 소제목 */
.section-heading {
    font-size: 16px;
    font-weight: bold;
    border-bottom: 2px solid #354637;
    padding-bottom: 6px;
    margin: 15px 0 10px;
}

.day-caption {
    color: #85785f;
    font-size: 10px;
    letter-spacing: 1px;
    margin-bottom: 5px;
}

/* 요일 선택 */
div[role="radiogroup"] {
    gap: 5px;
}

div[role="radiogroup"] label {
    background: #f8f2e5;
    border: 1px solid #b9aa8a;
    padding: 5px 9px;
    border-radius: 2px;
    transition: .2s;
}

div[role="radiogroup"] label:hover {
    background: #e7d9b6;
    border-color: #b28d3d;
}

div[role="radiogroup"] label:has(input:checked) {
    background: #354637;
    border-color: #d7ad42;
}

div[role="radiogroup"] label:has(input:checked) p {
    color: #f2d47b;
}

/* ── 순위 카드 ── */
.rank-card {
    display: flex;
    align-items: center;
    gap: 13px;
    min-height: 65px;
    background: #f8f2e5;
    border: 1px solid #c2b496;
    border-left: 4px solid #7b886d;
    padding: 10px 14px;
    margin: 5px 0;
    box-shadow: 2px 2px 0 #d5cbb7;
    transition: .2s;
}

.rank-card:hover {
    transform: translateY(-3px);
    box-shadow: 4px 4px 0 #c6b68e;
}

.rank-card.first {
    background: #f2e7d2;
    border-left-color: #b28d3d;
}

.rank-number {
    min-width: 35px;
    font-family: 'DM Serif Display', serif;
    font-size: 25px;
    color: #354637;
    text-align: center;
}

.first .rank-number {
    color: #a34d3e;
    font-size: 31px;
}

.rank-name {
    font-size: 15px;
    font-weight: bold;
    color: #354637;
}

.first .rank-name {
    font-size: 17px;
}

.rank-subtitle {
    font-size: 9px;
    color: #95866a;
    letter-spacing: 1px;
    margin-top: 3px;
}

/* 순위 표시 */
.archive-stamp {
    display: inline-block;
    border: 1px solid #a34d3e;
    color: #a34d3e;
    padding: 3px 9px;
    font-size: 9px;
    letter-spacing: 2px;
    transform: rotate(-2deg);
    margin: 2px 0 8px;
}

/* 하단 */
.footer-note {
    border-top: 1px dashed #a99b7c;
    margin-top: 15px;
    padding-top: 8px;
    text-align: center;
    color: #827963;
    font-size: 9px;
    line-height: 1.5;
}

/* 작은 화면 */
@media (max-width: 600px) {
    .paper-header {
        padding: 18px 8px;
    }

    .edition {
        font-size: 8px;
    }

    .rank-name {
        font-size: 13px;
    }

    .rank-card {
        padding: 8px;
        gap: 8px;
    }
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────
# 별 출력
# ─────────────────────────
st.markdown("""
<div class="star-field">
    <span class="star">✦</span>
    <span class="star">✧</span>
    <span class="star">✦</span>
    <span class="star">✧</span>
    <span class="star">✦</span>
    <span class="star">✧</span>
    <span class="star">✦</span>
    <span class="star">✧</span>
    <span class="star">✦</span>
    <span class="star">✧</span>
    <span class="star">✦</span>
    <span class="star">✧</span>
    <span class="star">✦</span>
    <span class="star">✧</span>
    <span class="star">✦</span>
    <span class="star">✧</span>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────
# 웹툰 목록
# ─────────────────────────
ranking_data = {
    "월요일": [
        "신체",
        "참교육",
        "환생천마",
        "시한부 천재가 살아남는",
        "절대검"
    ],
    "화요일": [
        "44교시 생존수업",
        "절대회귀",
        "괴력 난신",
        "오! 나의 교주님",
        "회귀한 용병은 다 계획이 있다"
    ],
    "수요일": [
        "화산귀환",
        "별을 품은 소드마스터",
        "종말이 찾아왔다",
        "싸이코패스 in 무림",
        "조의 영역: 여의도"
    ],
    "목요일": [
        "나노마신",
        "나의 경험",
        "마흔 즈음에",
        "육아일기",
        "재벌집 막내아들"
    ],
    "금요일": [
        "광마회귀",
        "오! 나의 교주님",
        "외모지상주의",
        "나 혼자 만렙 뉴비",
        "상남자"
    ],
    "토요일": [
        "절대군림",
        "호랑이형님",
        "마도전생기",
        "시든 꽃에 눈물을",
        "만취남녀"
    ],
    "일요일": [
        "육아일",
        "범죄도시0",
        "럭키비치",
        "권왕환생",
        "태존비록"
    ]
}


# ─────────────────────────
# 머리말
# ─────────────────────────
st.markdown("""
<div class="paper-header">
    <div class="eyebrow">✦ THE OLD WEBTOON ARCHIVE · WEEKLY EDITION ✦</div>
    <h1>WEEKLY RANKING</h1>
    <p>한 주의 이야기, 일곱 장의 기록</p>
    <div class="eyebrow">POPULAR WEBTOON CATALOGUE · NO. 002</div>
</div>

<div class="edition">
    <span>WEBTOON ARCHIVE TIMES</span>
    <span>요일별 작품 조사표</span>
    <span>VOL. 2026</span>
</div>

<div class="notice">
    <span class="notice-label">✦ WEEKLY BULLETIN</span>
    &nbsp; 요일을 선택해 해당 요일의 웹툰 목록을 확인하세요.
</div>
""", unsafe_allow_html=True)


# ─────────────────────────
# 요일 선택
# ─────────────────────────
st.markdown(
    '<div class="section-heading">01. 발행 요일 선택 / SELECT A DAY</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="day-caption">✧ 원하는 요일을 선택하세요.</div>',
    unsafe_allow_html=True
)

days = list(ranking_data.keys())

day = st.radio(
    "요일 선택",
    options=days,
    index=0,
    horizontal=True,
    label_visibility="collapsed"
)


# ─────────────────────────
# 순위 표시
# ─────────────────────────
st.markdown(
    f'<div class="section-heading">02. {day} 인기 웹툰 TOP 5</div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="archive-stamp">✦ ARCHIVE PICK · {day} ✦</div>',
    unsafe_allow_html=True
)

# 두 열로 나눠 세로 공간 절약
left_col, right_col = st.columns(2, gap="medium")

for i, title in enumerate(ranking_data[day], start=1):

    rank_class = "rank-card first" if i == 1 else "rank-card"

    card_html = f"""
    <div class="{rank_class}">
        <div class="rank-number">{i:02d}</div>
        <div>
            <div class="rank-name">{title.strip()}</div>
            <div class="rank-subtitle">
                RANKING NO. {i:02d} · {day.upper()}
            </div>
        </div>
    </div>
    """

    if i % 2 == 1:
        with left_col:
            st.markdown(card_html, unsafe_allow_html=True)
    else:
        with right_col:
            st.markdown(card_html, unsafe_allow_html=True)


# ─────────────────────────
# 하단
# ─────────────────────────
st.markdown("""
<div class="footer-note">
    ✦ THE OLD WEBTOON ARCHIVE · WEEKLY COLLECTION ✦<br>
    직접 수집한 작품 목록 · 오래된 종이, 새로운 이야기
</div>
""", unsafe_allow_html=True)
