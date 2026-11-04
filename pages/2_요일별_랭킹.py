
import streamlit as st
import textwrap

st.set_page_config(
    page_title="WEBTOON ARCHIVE | 요일별 랭킹",
    page_icon="🏆",
    layout="wide"
)

# ── 웹툰 데이터 ──
ranking_data = {
    "월요일": ["신체", "참교육", "환생천마", "시한부 천재가 살아남는", "절대검"],
    "화요일": ["44교시 생존수업", "절대회귀", "괴력 난신", "오! 나의 교주님", "회귀한 용병은 다 계획이 있다"],
    "수요일": ["화산귀환", "별을 품은 소드마스터", "종말이 찾아왔다", "싸이코패스 in 무림", "조의 영역: 여의도"],
    "목요일": ["나노마신", "나의 경험", "마흔 즈음에", "육아일기", "재벌집 막내아들"],
    "금요일": ["광마회귀", "오! 나의 교주님", "외모지상주의", "나 혼자 만렙 뉴비", "상남자"],
    "토요일": ["절대군림", "호랑이형님", "마도전생기", "시든 꽃에 눈물을", "만취남녀"],
    "일요일": ["육아일", "범죄도시0", "럭키비치", "권왕환생", "태존비록"]
}

# ── CSS 디자인 ──
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=DM+Serif+Display&display=swap');

.stApp {
    background: #e9e3d2;
    color: #354637;
    font-family: 'Gowun Batang', serif;
}

.block-container {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 1rem;
}

header[data-testid="stHeader"] {
    background: transparent;
}

/* 왼쪽 표지 */
.left-panel {
    background: #354637;
    color: #f4eddd;
    border: 3px double #d8c69e;
    outline: 1px solid #354637;
    padding: 35px 24px;
    min-height: 440px;
    box-shadow: 5px 5px 0 #cfc4ac;
    text-align: center;
}

.left-eyebrow {
    color: #e8c96d;
    font-size: 10px;
    letter-spacing: 3px;
}

.left-title {
    font-family: 'DM Serif Display', serif;
    color: #f4eddd;
    font-size: clamp(28px, 3vw, 43px);
    line-height: 1.15;
    margin: 35px 0 18px;
}

.left-description {
    color: #e3d8bd;
    font-size: 13px;
    line-height: 2;
}

.left-divider {
    border-top: 1px solid #8e987b;
    margin: 25px 0;
}

.left-caption {
    color: #e8c96d;
    font-size: 10px;
    letter-spacing: 2px;
    margin-bottom: 10px;
}

.left-footer {
    color: #c9bd9e;
    font-size: 10px;
    line-height: 2;
    margin-top: 28px;
}

/* 오른쪽 순위 제목 */
.right-heading {
    font-family: 'DM Serif Display', serif;
    font-size: clamp(24px, 3vw, 34px);
    color: #354637;
    border-bottom: 2px solid #354637;
    padding-bottom: 12px;
    margin: 5px 0 12px;
}

.right-subtitle {
    color: #95866a;
    font-size: 10px;
    letter-spacing: 2px;
    margin-bottom: 20px;
}

/* 순위 카드 */
.rank-card {
    display: flex;
    align-items: center;
    gap: 13px;
    min-height: 78px;
    padding: 15px;
    margin-bottom: 13px;
    background: #f8f2e5;
    border: 1px solid #c2b496;
    border-left: 5px solid #7b886d;
    box-shadow: 3px 3px 0 #d5cbb7;
    transition: all .25s ease;
}

.rank-card:hover {
    transform: translateY(-3px);
    box-shadow: 4px 6px 0 #c8bda5;
}

.rank-card.first {
    background: #f2e7d2;
    border-left-color: #b18a35;
}

.rank-number {
    min-width: 40px;
    font-family: 'DM Serif Display', serif;
    font-size: 30px;
    text-align: center;
    color: #354637;
}

.first .rank-number {
    color: #a34d3e;
    font-size: 36px;
}

.rank-name {
    font-size: 14px;
    font-weight: bold;
    color: #354637;
    word-break: keep-all;
    line-height: 1.5;
}

.rank-subtitle {
    color: #95866a;
    font-size: 9px;
    letter-spacing: 1px;
    margin-top: 5px;
}

/* 요일 선택 */
div[role="radiogroup"] {
    gap: 5px;
}

div[role="radiogroup"] label {
    background: #f8f2e5;
    border: 1px solid #b9aa8a;
    padding: 8px 10px;
    border-radius: 2px;
    font-size: 12px;
}

div[role="radiogroup"] label:hover {
    background: #e4e8d9;
}

/* 반짝이는 별 */
.star {
    position: fixed;
    z-index: 999;
    pointer-events: none;
    color: #f0c642;
    font-size: 25px;
    text-shadow: 0 0 5px #f0c642, 0 0 15px #e8c35a;
    animation: sparkle 2s ease-in-out infinite alternate;
}

.star1 { top: 15%; left: 32%; animation-delay: 0s; }
.star2 { top: 32%; left: 94%; animation-delay: .5s; }
.star3 { top: 68%; left: 30%; animation-delay: 1s; }
.star4 { top: 82%; left: 90%; animation-delay: .3s; }
.star5 { top: 48%; left: 72%; animation-delay: 1.4s; }
.star6 { top: 10%; left: 77%; animation-delay: .8s; }
.star7 { top: 75%; left: 57%; animation-delay: 1.7s; }

@keyframes sparkle {
    0% {
        opacity: .2;
        transform: scale(.6) rotate(0deg);
    }
    100% {
        opacity: 1;
        transform: scale(1.35) rotate(45deg);
    }
}

.footer-note {
    border-top: 1px dashed #b9aa8a;
    margin-top: 25px;
    padding-top: 15px;
    text-align: center;
    color: #95866a;
    font-size: 10px;
    line-height: 2;
}

@media (max-width: 750px) {
    .left-panel {
        min-height: auto;
    }
}
</style>
""", unsafe_allow_html=True)

# ── 별 장식 ──
st.markdown("""
<div class="star star1">✦</div>
<div class="star star2">✧</div>
<div class="star star3">✦</div>
<div class="star star4">✧</div>
<div class="star star5">✦</div>
<div class="star star6">✧</div>
<div class="star star7">✦</div>
""", unsafe_allow_html=True)


# ── 좌우 화면 ──
left, right = st.columns([0.85, 1.8], gap="large")

with left:

    # textwrap.dedent로 HTML 들여쓰기 문제 방지
    left_html = textwrap.dedent("""
    <div class="left-panel">
        <div class="left-eyebrow">✦ THE OLD WEBTOON ARCHIVE ✦</div>

        <div class="left-title">
            WEEKLY<br>RANKING
        </div>

        <div class="left-description">
            한 주의 이야기,<br>
            일곱 장의 기록
        </div>

        <div class="left-divider"></div>

        <div class="left-caption">✦ WEEKLY EDITION ✦</div>

        <div class="left-description">
            요일을 선택하고<br>
            오늘의 웹툰을 확인하세요.
        </div>

        <div class="left-divider"></div>

        <div class="left-caption">ARCHIVE INFORMATION</div>

        <div class="left-description">
            WEBTOON ARCHIVE TIMES<br>
            POPULAR WEBTOON CATALOGUE<br>
            VOL. 2026
        </div>

        <div class="left-footer">
            오래된 종이, 새로운 이야기<br>
            ✦ EST. 2026 ✦
        </div>
    </div>
    """)

    st.markdown(left_html, unsafe_allow_html=True)

    st.markdown(
        '<div class="left-caption" style="margin-top:25px;">✦ SELECT A DAY</div>',
        unsafe_allow_html=True
    )

    day = st.radio(
        "요일 선택",
        options=list(ranking_data.keys()),
        index=0,
        label_visibility="collapsed"
    )


with right:

    st.markdown(
        f'<div class="right-heading">{day} · TOP 5</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="right-subtitle">✦ ARCHIVE PICK · {day} · WEEKLY COLLECTION ✦</div>',
        unsafe_allow_html=True
    )

    # 2열 순위 카드
    col1, col2 = st.columns(2, gap="medium")

    for i, title in enumerate(ranking_data[day], start=1):

        target = col1 if i % 2 == 1 else col2

        with target:
            rank_class = "rank-card first" if i == 1 else "rank-card"

            card_html = textwrap.dedent(f"""
            <div class="{rank_class}">
                <div class="rank-number">{i:02d}</div>
                <div>
                    <div class="rank-name">{title}</div>
                    <div class="rank-subtitle">RANKING NO. {i:02d}</div>
                </div>
            </div>
            """)

            st.markdown(card_html, unsafe_allow_html=True)

    st.markdown("""
    <div class="footer-note">
        ✦ THE OLD WEBTOON ARCHIVE ✦<br>
        직접 수집한 작품 목록 · 실시간 순위가 아닙니다.
    </div>
    """, unsafe_allow_html=True)
