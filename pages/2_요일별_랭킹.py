
import streamlit as st

st.set_page_config(
    page_title="WEBTOON ARCHIVE | 요일별 랭킹",
    page_icon="🏆",
    layout="wide"
)

# ── 웹툰 목록 ──
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
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 1rem;
}

header[data-testid="stHeader"] {
    background: transparent;
}

/* 왼쪽 제목 패널 */
.left-panel {
    background: #354637;
    color: #f4eddd;
    border: 3px double #d8c69e;
    outline: 1px solid #354637;
    outline-offset: 4px;
    padding: 35px 25px;
    min-height: 510px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
    box-sizing: border-box;
}

.left-small {
    color: #e2c36b;
    font-size: 10px;
    letter-spacing: 3px;
    line-height: 2;
}

.left-title {
    font-family: 'DM Serif Display', serif;
    font-size: clamp(30px, 3vw, 43px);
    line-height: 1.2;
    color: #f5edda;
    margin: 28px 0;
    word-break: keep-all;
}

.left-description {
    color: #e2d7bd;
    font-size: 13px;
    line-height: 2;
}

.left-divider {
    border-top: 1px solid #a99b7c;
    margin: 25px 0;
}

.left-caption {
    color: #d8c69e;
    font-size: 10px;
    letter-spacing: 2px;
    line-height: 2;
}

.left-footer {
    color: #e2c36b;
    font-size: 11px;
    margin-top: 35px;
    letter-spacing: 2px;
}

/* 오른쪽 제목 */
.right-title {
    font-family: 'DM Serif Display', serif;
    font-size: 31px;
    color: #354637;
    margin: 0 0 8px 0;
}

.right-subtitle {
    color: #9a8765;
    font-size: 10px;
    letter-spacing: 2px;
    border-bottom: 2px solid #354637;
    padding-bottom: 13px;
    margin-bottom: 15px;
}

/* 요일 선택 */
div[role="radiogroup"] {
    gap: 5px;
    flex-wrap: wrap;
}

div[role="radiogroup"] label {
    background: #f8f2e5;
    border: 1px solid #c2b496;
    border-radius: 2px;
    padding: 7px 10px;
    font-size: 13px;
}

div[role="radiogroup"] label:hover {
    background: #e4e8d9;
}

/* 순위 카드 */
.rank-card {
    display: flex;
    align-items: center;
    gap: 13px;
    min-height: 76px;
    box-sizing: border-box;
    background: #f8f2e5;
    border: 1px solid #c2b496;
    border-left: 4px solid #849176;
    padding: 12px 14px;
    margin-bottom: 10px;
    box-shadow: 3px 3px 0 #d5cbb7;
    transition: all 0.25s ease;
}

.rank-card:hover {
    transform: translateY(-3px);
    box-shadow: 4px 6px 0 #c9bea6;
    background: #fff9eb;
}

.rank-card.first {
    background: #f2e7d2;
    border-left-color: #b18a35;
}

.rank-number {
    font-family: 'DM Serif Display', serif;
    font-size: 27px;
    min-width: 42px;
    text-align: center;
    color: #354637;
}

.first .rank-number {
    color: #a34d3e;
    font-size: 33px;
}

.rank-name {
    color: #354637;
    font-size: 15px;
    font-weight: bold;
    word-break: keep-all;
}

.rank-subtitle {
    color: #a18e6c;
    font-size: 9px;
    letter-spacing: 1px;
    margin-top: 5px;
}

.archive-stamp {
    color: #a34d3e;
    font-size: 10px;
    letter-spacing: 2px;
    margin: 10px 0 15px;
}

.footer-note {
    border-top: 1px dashed #b9aa8a;
    margin-top: 20px;
    padding-top: 15px;
    color: #95866a;
    text-align: center;
    font-size: 10px;
    line-height: 2;
}

/* 반짝이는 별 */
.star {
    position: fixed;
    z-index: 0;
    pointer-events: none;
    color: #e9bd43;
    text-shadow: 0 0 7px #f4d66f, 0 0 15px #e9bd43;
    animation: twinkle 2.5s ease-in-out infinite alternate;
}

.star.one { top: 17%; left: 31%; font-size: 25px; }
.star.two { top: 35%; left: 91%; font-size: 20px; animation-delay: .8s; }
.star.three { top: 72%; left: 43%; font-size: 17px; animation-delay: 1.3s; }
.star.four { top: 82%; left: 88%; font-size: 24px; animation-delay: .4s; }
.star.five { top: 52%; left: 72%; font-size: 13px; animation-delay: 1.7s; }
.star.six { top: 12%; left: 80%; font-size: 15px; animation-delay: 1s; }

@keyframes twinkle {
    from {
        opacity: .25;
        transform: scale(.7) rotate(0deg);
    }
    to {
        opacity: 1;
        transform: scale(1.25) rotate(35deg);
    }
}

/* 사이드바 */
section[data-testid="stSidebar"] {
    background: #354637;
}

section[data-testid="stSidebar"] * {
    color: #f4eddd;
}

@media (max-width: 750px) {
    .left-panel {
        min-height: 250px;
        padding: 25px 15px;
    }
    .left-title {
        font-size: 30px;
        margin: 15px 0;
    }
}
</style>

<div class="star one">✦</div>
<div class="star two">✧</div>
<div class="star three">✦</div>
<div class="star four">✧</div>
<div class="star five">✦</div>
<div class="star six">✧</div>
""", unsafe_allow_html=True)


# ── 화면 구성 ──
left, right = st.columns([0.85, 1.9], gap="large")

with left:
    st.markdown("""
    <div class="left-panel">
        <div class="left-small">✦ THE OLD WEBTOON ARCHIVE ✦</div>

        <div class="left-title">
            WEEKLY<br>RANKING
        </div>

        <div class="left-description">
            한 주의 이야기,<br>
            일곱 장의 기록
        </div>

        <div class="left-divider"></div>

        <div class="left-caption">
            ✦ WEEKLY EDITION ✦
        </div>

        <div class="left-description">
            요일을 선택하고<br>
            오늘의 웹툰을 확인하세요.
        </div>

        <div class="left-divider"></div>

        <div class="left-caption">
            WEBTOON ARCHIVE TIMES<br>
            POPULAR WEBTOON CATALOGUE<br>
            VOL. 2026
        </div>

        <div class="left-footer">
            ✦ EST. 2026 ✦
        </div>
    </div>
    """, unsafe_allow_html=True)


with right:
    st.markdown("""
    <div class="right-title">오늘의 웹툰 기록</div>
    <div class="right-subtitle">
        ✦ ARCHIVE PICK · WEEKLY COLLECTION ✦
    </div>
    """, unsafe_allow_html=True)

    days = list(ranking_data.keys())

    day = st.radio(
        "요일 선택",
        options=days,
        index=0,
        horizontal=True,
        label_visibility="collapsed"
    )

    st.markdown(
        f'<div class="right-title" style="font-size:25px; margin-top:18px;">'
        f'{day} · TOP 5</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="archive-stamp">✦ ARCHIVE PICK · {day} · WEEKLY COLLECTION ✦</div>',
        unsafe_allow_html=True
    )

    # 순위 카드 2열 배치
    col1, col2 = st.columns(2, gap="medium")

    for i, title in enumerate(ranking_data[day], start=1):
        rank_class = "rank-card first" if i == 1 else "rank-card"

        card_html = f"""
        <div class="{rank_class}">
            <div class="rank-number">{i:02d}</div>
            <div>
                <div class="rank-name">{title}</div>
                <div class="rank-subtitle">RANKING NO. {i:02d}</div>
            </div>
        </div>
        """

        if i % 2 == 1:
            with col1:
                st.markdown(card_html, unsafe_allow_html=True)
        else:
            with col2:
                st.markdown(card_html, unsafe_allow_html=True)

    st.markdown("""
    <div class="footer-note">
        ✦ THE OLD WEBTOON ARCHIVE ✦<br>
        직접 수집한 작품 목록 · 실시간 순위가 아닙니다.<br>
        오래된 종이, 새로운 이야기
    </div>
    """, unsafe_allow_html=True)
