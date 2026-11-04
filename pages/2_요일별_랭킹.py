
import streamlit as st

st.set_page_config(
    page_title="WEBTOON ARCHIVE | 요일별 랭킹",
    page_icon="🏆",
    layout="wide"
)

# ── 디자인 ──
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=DM+Serif+Display&display=swap');

.stApp {
    background: #e9e3d2;
    color: #354637;
    font-family: 'Gowun Batang', serif;
}

.block-container {
    max-width: 1000px;
    padding-top: 2.5rem;
    padding-bottom: 4rem;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.paper-header {
    background: #354637;
    color: #f4eddd;
    text-align: center;
    padding: 45px 20px 38px;
    border: 1px solid #b9a982;
    outline: 3px double #354637;
    outline-offset: 5px;
    margin-bottom: 35px;
}

.eyebrow {
    color: #d8c69e;
    font-size: 11px;
    letter-spacing: 5px;
}

.paper-header h1 {
    color: #f4eddd;
    font-family: 'DM Serif Display', serif;
    font-size: clamp(34px, 5vw, 55px);
    letter-spacing: 3px;
    margin: 17px 0;
}

.paper-header p {
    color: #e3d8bd;
    font-size: 14px;
    margin-bottom: 20px;
}

.edition {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 10px;
    padding: 12px 3px;
    margin: 20px 0 25px;
    border-top: 1px solid #a99b7c;
    border-bottom: 3px double #354637;
    font-size: 11px;
    letter-spacing: 1px;
}

.notice {
    background: #f8f2e5;
    border: 1px solid #c2b496;
    box-shadow: 4px 4px 0 #d5cbb7;
    padding: 20px 23px;
    margin: 25px 0 35px;
    color: #454537;
}

.notice-label {
    color: #a34d3e;
    font-size: 11px;
    font-weight: bold;
    letter-spacing: 3px;
    margin-bottom: 10px;
}

.section-heading {
    font-size: 19px;
    font-weight: bold;
    border-bottom: 2px solid #354637;
    padding-bottom: 10px;
    margin: 35px 0 18px;
}

.day-caption {
    color: #85785f;
    font-size: 12px;
    letter-spacing: 2px;
    margin-bottom: 10px;
}

/* 요일 선택 버튼 */
div[role="radiogroup"] {
    gap: 8px;
}

div[role="radiogroup"] label {
    background: #f8f2e5;
    border: 1px solid #b9aa8a;
    padding: 9px 14px;
    border-radius: 2px;
    transition: 0.2s;
}

div[role="radiogroup"] label:hover {
    background: #dce2d2;
    border-color: #354637;
}

/* 순위 카드 */
.rank-card {
    display: flex;
    align-items: center;
    gap: 20px;
    background: #f8f2e5;
    border: 1px solid #c2b496;
    border-left: 5px solid #7b886d;
    padding: 19px 22px;
    margin: 12px 0;
    box-shadow: 3px 3px 0 #d5cbb7;
}

.rank-card.first {
    background: #f2e7d2;
    border-left-color: #a34d3e;
    padding: 24px 22px;
}

.rank-number {
    min-width: 48px;
    font-family: 'DM Serif Display', serif;
    font-size: 29px;
    color: #354637;
    text-align: center;
}

.first .rank-number {
    color: #a34d3e;
    font-size: 37px;
}

.rank-name {
    font-size: 18px;
    font-weight: bold;
    color: #354637;
}

.first .rank-name {
    font-size: 21px;
}

.rank-subtitle {
    font-size: 10px;
    color: #95866a;
    letter-spacing: 2px;
    margin-top: 5px;
}

.archive-stamp {
    display: inline-block;
    border: 2px solid #a34d3e;
    color: #a34d3e;
    padding: 5px 12px;
    font-size: 10px;
    letter-spacing: 2px;
    transform: rotate(-2deg);
    margin: 5px 0 15px;
}

.footer-note {
    border-top: 1px dashed #a99b7c;
    margin-top: 45px;
    padding-top: 22px;
    text-align: center;
    color: #827963;
    font-size: 11px;
    line-height: 2;
}

hr {
    border-color: #b9aa8a;
}

@media (max-width: 600px) {
    .paper-header {
        padding: 30px 12px;
    }
    .edition {
        font-size: 9px;
    }
    .rank-card {
        padding: 15px 12px;
        gap: 12px;
    }
    .rank-name {
        font-size: 15px;
    }
}
</style>
""", unsafe_allow_html=True)


# ── 요일별 웹툰 목록 ──
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


# ── 신문 머리말 ──
st.markdown("""
<div class="paper-header">
    <div class="eyebrow">THE OLD WEBTOON ARCHIVE · WEEKLY EDITION</div>
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
    <div class="notice-label">▣ WEEKLY BULLETIN / 주간 소식</div>
    <div>요일을 선택해 해당 요일에 연재되는 웹툰 목록을 확인하세요.</div>
    <div>오래된 신문 한 장처럼, 오늘의 취향을 기록합니다.</div>
</div>
""", unsafe_allow_html=True)


# ── 요일 선택 ──
st.markdown(
    '<div class="section-heading">01. 발행 요일 선택 / SELECT A DAY</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="day-caption">▼ 원하는 요일을 선택하세요.</div>',
    unsafe_allow_html=True
)

days = list(ranking_data.keys())

# select_slider 대신 radio 사용
day = st.radio(
    "요일 선택",
    options=days,
    index=0,
    horizontal=True,
    label_visibility="collapsed"
)


# ── 선택한 요일의 순위 ──
st.markdown(
    f'<div class="section-heading">02. {day} 인기 웹툰 TOP 5</div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="archive-stamp">ARCHIVE PICK · {day}</div>',
    unsafe_allow_html=True
)

for i, title in enumerate(ranking_data[day], start=1):

    if i == 1:
        rank_class = "rank-card first"
    else:
        rank_class = "rank-card"

    st.markdown(
        f"""
        <div class="{rank_class}">
            <div class="rank-number">{i:02d}</div>
            <div>
                <div class="rank-name">{title.strip()}</div>
                <div class="rank-subtitle">
                    RANKING NO. {i:02d} · {day.upper()}
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ── 하단 안내 ──
st.markdown("""
<div class="notice">
    <div class="notice-label">※ ARCHIVE NOTICE</div>
    <div>이 페이지는 직접 수집하고 입력한 작품 목록을 요일별로 보여 줍니다.</div>
    <div>실시간 인기 순위가 자동으로 수집되는 기능은 연결되어 있지 않습니다.</div>
</div>

<div class="footer-note">
    THE OLD WEBTOON ARCHIVE · WEEKLY COLLECTION<br>
    오래된 종이, 새로운 이야기 · 기록은 계속됩니다.
</div>
""", unsafe_allow_html=True)
