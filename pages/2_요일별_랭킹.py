import streamlit as st
import random

st.set_page_config(
    page_title="WEBTOON ARCHIVE | 요일별 랭킹",
    page_icon="🏆",
    layout="wide"
)

# ── 요일별 웹툰 목록 ──
ranking_data = {
    "월요일": ["신체", "참교육", "환생천마", "시한부 천재가 살아남는", "절대검"],
    "화요일": ["44교시 생존수업", "절대회귀", "괴력 난신", "오! 나의 교주님", "회귀한 용병은 다 계획이 있다"],
    "수요일": ["화산귀환", "별을 품은 소드마스터", "종말이 찾아왔다", "싸이코패스 in 무림", "조의 영역: 여의도"],
    "목요일": ["나노마신", "나의 경험", "마흔 즈음에", "육아일기", "재벌집 막내아들"],
    "금요일": ["광마회귀", "오! 나의 교주님", "외모지상주의", "나 혼자 만렙 뉴비", "상남자"],
    "토요일": ["절대군림", "호랑이형님", "마도전생기", "시든 꽃에 눈물을", "만취남녀"],
    "일요일": ["육아일", "범죄도시0", "럭키비치", "권왕환생", "태존비록"]
}

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
    max-width: 1350px;
    padding-top: 2rem;
    padding-bottom: 1rem;
}

header[data-testid="stHeader"] {
    background: transparent;
}

/* 왼쪽 영역 */
.left-panel {
    background: #354637;
    color: #f4eddd;
    padding: 35px 25px;
    border: 3px double #d8c69e;
    outline: 1px solid #354637;
    height: 100%;
    min-height: 520px;
    position: relative;
}

.left-eyebrow {
    color: #e4c66d;
    font-size: 10px;
    letter-spacing: 3px;
    text-align: center;
}

.left-title {
    font-family: 'DM Serif Display', serif;
    font-size: clamp(28px, 3vw, 44px);
    line-height: 1.15;
    text-align: center;
    margin: 30px 0 15px;
    color: #f4eddd;
}

.left-description {
    color: #dfd2b4;
    font-size: 13px;
    text-align: center;
    line-height: 2;
}

.left-divider {
    border-top: 1px solid #9c9b72;
    margin: 25px 0;
}

.left-caption {
    color: #e4c66d;
    font-size: 11px;
    letter-spacing: 2px;
    margin-bottom: 12px;
}

.left-footer {
    color: #c9bd9e;
    font-size: 10px;
    text-align: center;
    margin-top: 35px;
    line-height: 2;
}

/* 오른쪽 제목 */
.right-heading {
    font-family: 'DM Serif Display', serif;
    font-size: 29px;
    color: #354637;
    border-bottom: 2px solid #354637;
    padding-bottom: 12px;
    margin-bottom: 15px;
}

.right-subtitle {
    color: #8b7d60;
    font-size: 11px;
    letter-spacing: 2px;
    margin-bottom: 20px;
}

/* 순위 카드 */
.rank-card {
    background: #f8f2e5;
    border: 1px solid #c2b496;
    border-left: 5px solid #7b886d;
    box-shadow: 3px 3px 0 #d5cbb7;
    padding: 19px 15px;
    min-height: 78px;
    display: flex;
    align-items: center;
    gap: 13px;
    margin-bottom: 12px;
    transition: 0.25s;
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
    font-family: 'DM Serif Display', serif;
    font-size: 30px;
    color: #354637;
    min-width: 38px;
    text-align: center;
}

.first .rank-number {
    color: #a34d3e;
    font-size: 35px;
}

.rank-name {
    color: #354637;
    font-size: 15px;
    font-weight: bold;
    word-break: keep-all;
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
}

div[role="radiogroup"] label:hover {
    background: #e4e8d9;
}

/* 별 장식 */
.star {
    position: fixed;
    color: #e9bd39;
    font-size: 23px;
    pointer-events: none;
    z-index: 999;
    text-shadow: 0 0 7px #f5d66d, 0 0 15px #e9bd39;
    animation: twinkle 2.5s ease-in-out infinite alternate;
}

.star.s1 { top: 17%; left: 31%; animation-delay: 0s; }
.star.s2 { top: 33%; left: 92%; animation-delay: .7s; }
.star.s3 { top: 65%; left: 29%; animation-delay: 1.2s; }
.star.s4 { top: 83%; left: 94%; animation-delay: .4s; }
.star.s5 { top: 48%; left: 70%; animation-delay: 1.6s; }
.star.s6 { top: 8%; left: 76%; animation-delay: .9s; }
.star.s7 { top: 75%; left: 54%; animation-delay: 2s; }

@keyframes twinkle {
    0% {
        opacity: .25;
        transform: scale(.65) rotate(0deg);
    }
    100% {
        opacity: 1;
        transform: scale(1.3) rotate(45deg);
    }
}

@media (max-width: 750px) {
    .left-panel {
        min-height: auto;
        padding: 25px 15px;
    }
}
</style>

<div class="star s1">✦</div>
<div class="star s2">✧</div>
<div class="star s3">✦</div>
<div class="star s4">✧</div>
<div class="star s5">✦</div>
<div class="star s6">✧</div>
<div class="star s7">✦</div>
""", unsafe_allow_html=True)


# ── 화면 좌우 분할 ──
left, right = st.columns([0.85, 1.7], gap="large")

with left:
    st.markdown("""
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

        <div class="left-caption">✦ WEEKLY EDITION</div>
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
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        '<div class="left-caption">✦ SELECT A DAY</div>',
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
        f'<div class="right-heading">{day.upper()} · TOP 5</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="right-subtitle">✦ ARCHIVE PICK · {day} · WEEKLY COLLECTION ✦</div>',
        unsafe_allow_html=True
    )

    # 순위 카드 2열 배치
    col1, col2 = st.columns(2, gap="medium")

    for i, title in enumerate(ranking_data[day], start=1):
        target = col1 if i % 2 == 1 else col2

        with target:
            rank_class = "rank-card first" if i == 1 else "rank-card"

            st.markdown(
                f"""
                <div class="{rank_class}">
                    <div class="rank-number">{i:02d}</div>
                    <div>
                        <div class="rank-name">{title}</div>
                        <div class="rank-subtitle">
                            RANKING NO. {i:02d}
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("""
    <div style="
        border-top: 1px dashed #b9aa8a;
        margin-top: 25px;
        padding-top: 15px;
        text-align: center;
        color: #887b60;
        font-size: 10px;
        letter-spacing: 1px;
        line-height: 2;
    ">
        ✦ THE OLD WEBTOON ARCHIVE ✦<br>
        직접 수집한 작품 목록 · 실시간 순위가 아닙니다.
    </div>
    """, unsafe_allow_html=True)
