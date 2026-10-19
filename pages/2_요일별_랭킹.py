import streamlit as st

st.set_page_config(
    page_title="WEBTOON ARCHIVE | 요일별 랭킹",
    page_icon="🏆",
    layout="wide"
)

# ── 빈티지 신문 디자인 ──
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
.paper-header {
    background: #354637;
    color: #f2ead7;
    padding: 30px 24px;
    text-align: center;
    border: 3px double #d5c7a4;
    outline: 1px solid #354637;
    outline-offset: 5px;
    margin-bottom: 30px;
}
.paper-header .eyebrow {
    color: #d5c7a4;
    font-size: 12px;
    letter-spacing: 4px;
}
.paper-header h1 {
    color: #f2ead7;
    font-size: clamp(28px, 5vw, 48px);
    letter-spacing: 3px;
    margin: 12px 0;
}
.paper-header p {
    color: #e1d7bd;
    font-size: 14px;
}
.edition {
    display: flex;
    justify-content: space-between;
    gap: 12px;
    flex-wrap: wrap;
    border-top: 1px solid #a69a7d;
    border-bottom: 3px double #354637;
    padding: 9px 2px;
    margin: 18px 0;
    font-size: 12px;
    letter-spacing: 1px;
}
.notice {
    background: #f8f2e4;
    border: 1px solid #a69a7d;
    box-shadow: 4px 4px 0 #d1c7b1;
    padding: 18px 22px;
    margin: 20px 0;
}
.notice-label {
    color: #93483a;
    font-weight: bold;
    font-size: 12px;
    letter-spacing: 3px;
}
.section-heading {
    font-size: 22px;
    font-weight: bold;
    border-bottom: 2px solid #354637;
    padding-bottom: 8px;
    margin: 28px 0 15px;
}
.rank-card {
    display: flex;
    align-items: center;
    gap: 18px;
    background: #f8f2e4;
    border: 1px solid #b7aa8d;
    border-left: 6px solid #65745b;
    padding: 16px 18px;
    margin: 10px 0;
    box-shadow: 3px 3px 0 #d1c7b1;
}
.rank-number {
    min-width: 55px;
    font-size: 25px;
    font-weight: bold;
    color: #354637;
    text-align: center;
}
.rank-medal {
    font-size: 27px;
    min-width: 55px;
    text-align: center;
}
.rank-name {
    font-size: 18px;
    font-weight: bold;
    color: #30392b;
}
.rank-subtitle {
    font-size: 11px;
    letter-spacing: 2px;
    color: #84775e;
    margin-top: 4px;
}
.top-rank {
    border-left-color: #a34d3e;
    background: #f5ead7;
}
.archive-stamp {
    display: inline-block;
    border: 2px solid #93483a;
    color: #93483a;
    padding: 4px 10px;
    font-size: 11px;
    letter-spacing: 2px;
    transform: rotate(-2deg);
    margin-bottom: 10px;
}
.footer-note {
    border-top: 1px dashed #a69a7d;
    margin-top: 36px;
    padding-top: 18px;
    text-align: center;
    color: #716b58;
    font-size: 12px;
}
div.stButton > button {
    background: #354637;
    color: #f8f2e4;
    border: 1px solid #354637;
    border-radius: 0;
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

# ── 요일별 웹툰 목록 ──
ranking_data = {
    "월요일": [
        "신체",
        "참교육",
        "환생천마",
        "시한부 천재가 살아남는 ",
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
    <span>요일별 인기 작품 조사표</span>
    <span>VOL. 2026</span>
</div>
<div class="notice">
    <div class="notice-label">▣ WEEKLY BULLETIN / 주간 소식</div>
    <p>요일을 선택해 해당 요일에 정리된 웹툰 목록을 확인하세요.</p>
    <p>오래된 신문 한 장처럼, 오늘의 취향을 기록합니다.</p>
</div>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="section-heading">01. 발행 요일 선택 / SELECT A DAY</div>',
    unsafe_allow_html=True
)

days = list(ranking_data.keys())
day = st.select_slider(
    "신문을 펼칠 요일",
    options=days,
    value="월요일"
)

st.markdown(
    f'<div class="section-heading">02. {day} 인기 웹툰 TOP 5</div>',
    unsafe_allow_html=True
)
st.markdown(
    f'<div class="archive-stamp">ARCHIVE PICK · {day}</div>',
    unsafe_allow_html=True
)

medals = ["🥇", "🥈", "🥉"]

for i, title in enumerate(ranking_data[day], start=1):
    if i <= 3:
        medal_html = f'<div class="rank-medal">{medals[i-1]}</div>'
        rank_class = "rank-card top-rank"
    else:
        medal_html = f'<div class="rank-number">0{i}</div>'
        rank_class = "rank-card"

    st.markdown(
        f"""
        <div class="{rank_class}">
            {medal_html}
            <div>
                <div class="rank-name">{title.strip()}</div>
                <div class="rank-subtitle">RANKING NO. {i:02d} · {day.upper()}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("""
<div class="notice">
    <div class="notice-label">※ ARCHIVE NOTICE</div>
    <p>이 페이지는 직접 입력한 작품 목록을 요일별로 보여 줍니다.</p>
    <p>실시간 인기 순위가 자동으로 수집되는 기능은 아직 연결되어 있지 않습니다.</p>
</div>
<div class="footer-note">
    WEBTOON ARCHIVE TIMES · WEEKLY COLLECTION<br>
    오래된 종이, 새로운 이야기 · 기록은 계속됩니다.
</div>
""", unsafe_allow_html=True)
