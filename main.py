
import streamlit as st
import random

st.set_page_config(
    page_title="WEBTOON ARCHIVE",
    page_icon="📚",
    layout="wide"
)

# ── 웹툰 데이터 ──
webtoon_data = {
    "판타지": [
        "전지적 독자 시점", "화산귀환", "나 혼자만 레벨업",
        "초인의 게임", "철수를 구하시오"
    ],
    "로맨스": [
        "작전명 순정", "시든 꽃에 눈물을", "럭키비치"
    ],
    "액션": [
        "광마회귀", "나노마신", "외모지상주의", "상남자"
    ],
    "스릴러": [
        "44교시 생존수업", "종말이 찾아왔다", "조의 영역"
    ],
    "BL": [
        "물가의 밤", "체크메이트", "남고소년"
    ],
    "드라마": [
        "재벌집 막내아들", "마흔 즈음에", "육아일기"
    ]
}

all_titles = list(dict.fromkeys(
    title
    for titles in webtoon_data.values()
    for title in titles
))

# ── 디자인 ──
st.markdown("""
<style>
.stApp {
    background-color: #e8eddd;
    color: #29432f;
}

[data-testid="stSidebar"] {
    background-color: #d3dfc4;
}

.block-container {
    max-width: 1050px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.poster {
    background-color: #f7f3e4;
    border: 4px double #526b49;
    padding: 40px 25px;
    text-align: center;
    box-shadow: 8px 8px 0 #bdcbae;
    margin-bottom: 35px;
}

.eyebrow {
    letter-spacing: 4px;
    color: #718568;
    font-size: 13px;
}

.main-title {
    font-family: Georgia, serif;
    font-size: clamp(42px, 7vw, 68px);
    font-weight: bold;
    color: #29432f;
    margin: 25px 0 10px;
    line-height: 1.05;
}

.subtitle {
    font-size: 16px;
    color: #687b58;
    letter-spacing: 2px;
}

.stamp {
    display: inline-block;
    margin-top: 25px;
    padding: 8px 15px;
    border: 2px solid #526b49;
    color: #526b49;
    transform: rotate(-3deg);
}

.section-title {
    font-family: Georgia, serif;
    font-size: 23px;
    font-weight: bold;
    border-bottom: 2px solid #526b49;
    padding-bottom: 10px;
    margin: 32px 0 20px;
}

.archive-card {
    background: #f7f3e4;
    border: 1px solid #a4b596;
    padding: 22px;
    min-height: 150px;
    box-shadow: 4px 4px 0 #cbd6bd;
    margin-bottom: 10px;
}

.card-number {
    color: #718568;
    font-size: 12px;
    letter-spacing: 2px;
}

.card-title {
    font-size: 20px;
    font-weight: bold;
    margin: 15px 0;
    color: #29432f;
}

.card-description {
    font-size: 14px;
    line-height: 1.8;
    color: #596b50;
}

.pick-card {
    background: #344a35;
    color: #f7f3e4;
    border: 4px double #a7b895;
    padding: 28px 20px;
    text-align: center;
    margin: 10px 0 20px;
}

.pick-label {
    font-size: 12px;
    letter-spacing: 4px;
    color: #d3dfc4;
}

.pick-title {
    font-family: Georgia, serif;
    font-size: clamp(25px, 4vw, 36px);
    font-weight: bold;
    margin: 16px 0;
    overflow-wrap: anywhere;
}

.pick-note {
    font-size: 13px;
    color: #d3dfc4;
}

.stButton > button {
    background-color: #526b49;
    color: white;
    border-radius: 3px;
    border: 1px solid #29432f;
    min-height: 42px;
    transition: 0.2s;
}

.stButton > button:hover {
    background-color: #718568;
    color: white;
    border-color: #29432f;
}

div[data-baseweb="select"] > div,
div[data-testid="stTextInput"] input {
    background-color: #f7f3e4;
    border-color: #a4b596;
}

.footer {
    border-top: 2px solid #718568;
    text-align: center;
    margin-top: 40px;
    padding-top: 20px;
    color: #718568;
    letter-spacing: 2px;
    font-size: 12px;
}

@media (max-width: 600px) {
    .poster { padding: 28px 14px; }
    .eyebrow { letter-spacing: 2px; }
    .subtitle { letter-spacing: 1px; }
    .archive-card { padding: 16px; }
}
</style>
""", unsafe_allow_html=True)

# ── 메인 포스터 ──
st.markdown("""
<div class="poster">
    <div class="eyebrow">
        THE INDEPENDENT WEBTOON PAPER · VOL. 001
    </div>
    <div class="main-title">
        WEBTOON<br>ARCHIVE
    </div>
    <div class="subtitle">
        웹툰을 수집하고, 발견하고, 기록하다.
    </div>
    <div class="stamp">
        EST. 2026 · WEBTOON CULTURE
    </div>
</div>
""", unsafe_allow_html=True)

# ── 소개 ──
st.markdown("""
<div class="section-title">
    ▣ ARCHIVE GUIDE — 자료실 안내
</div>
<p style="line-height:2;">
장르별 웹툰을 탐색하고, 취향에 맞는 작품을 발견해 보세요.<br>
오래된 잡지와 전단지처럼 이야기를 모아 소개하는 작은 아카이브입니다.
</p>
""", unsafe_allow_html=True)

# ── 페이지 바로가기 ──
st.markdown("""
<div class="section-title">
    ▣ ARCHIVE INDEX — 자료실 목차
</div>
""", unsafe_allow_html=True)

pages = [
    {
        "number": "FILE NO. 001",
        "title": "▣ 웹툰 추천",
        "description": "취향에 맞는 작품을 발견하고<br>새로운 이야기를 만나 보세요.",
        "path": "pages/1_웹툰_추천.py",
        "button": "추천 페이지 열기"
    },
    {
        "number": "FILE NO. 002",
        "title": "▣ 요일별 랭킹",
        "description": "요일별로 정리된 작품 목록을<br>신문처럼 살펴보세요.",
        "path": "pages/2_요일별_랭킹.py",
        "button": "랭킹 페이지 열기"
    },
    {
        "number": "FILE NO. 003",
        "title": "▣ 캐릭터 생성기",
        "description": "나만의 취향을 담아<br>캐릭터를 만들어 보세요.",
        "path": "pages/3_캐릭터_생성기.py",
        "button": "생성기 열기"
    },
    {
        "number": "FILE NO. 004",
        "title": "▣ 웹툰 룰렛",
        "description": "무엇을 읽을지 모르겠다면<br>운명에 맡겨 보세요.",
        "path": "pages/4_웹툰_룰렛.py",
        "button": "룰렛 돌리러 가기"
    }
]

for start in range(0, len(pages), 2):
    cols = st.columns(2)

    for col, page in zip(cols, pages[start:start + 2]):
        with col:
            st.markdown(f"""
            <div class="archive-card">
                <div class="card-number">{page['number']}</div>
                <div class="card-title">{page['title']}</div>
                <div class="card-description">
                    {page['description']}
                </div>
            </div>
            """, unsafe_allow_html=True)

            if st.button(
                page["button"],
                key=f"nav_{page['number']}",
                use_container_width=True
            ):
                st.switch_page(page["path"])

# ── 오늘의 웹툰 ──
st.markdown("""
<div class="section-title">
    ▣ TODAY'S PICK — 오늘의 작품
</div>
""", unsafe_allow_html=True)

if "main_daily_pick" not in st.session_state:
    st.session_state.main_daily_pick = random.choice(all_titles)

if "main_daily_genre" not in st.session_state:
    st.session_state.main_daily_genre = next(
        genre for genre, titles in webtoon_data.items()
        if st.session_state.main_daily_pick in titles
    )

st.markdown(f"""
<div class="pick-card">
    <div class="pick-label">A STORY SELECTED FOR YOU</div>
    <div class="pick-title">「 {st.session_state.main_daily_pick} 」</div>
    <div class="pick-note">
        GENRE: {st.session_state.main_daily_genre}
        &nbsp; · &nbsp; 오늘의 아카이브 추천
    </div>
</div>
""", unsafe_allow_html=True)

if st.button("↻ 다른 작품 추천받기", use_container_width=True):
    candidates = [
        title for title in all_titles
        if title != st.session_state.main_daily_pick
    ]
    st.session_state.main_daily_pick = random.choice(candidates)
    st.session_state.main_daily_genre = next(
        genre for genre, titles in webtoon_data.items()
        if st.session_state.main_daily_pick in titles
    )
    st.rerun()

# ── 작품 검색 ──
st.markdown("""
<div class="section-title">
    ▣ ARCHIVE SEARCH — 작품 검색
</div>
""", unsafe_allow_html=True)

query = st.text_input(
    "찾고 싶은 작품 이름",
    placeholder="작품명을 입력하세요. 예: 화산귀환"
)

if query.strip():
    matches = [
        (genre, title)
        for genre, titles in webtoon_data.items()
        for title in titles
        if query.strip().lower() in title.lower()
    ]

    # 동일한 작품이 여러 장르에 걸쳐 표시되면 첫 결과만 남김
    matches = list(dict.fromkeys(matches))

    if matches:
        st.markdown("##### 검색 결과")
        for genre, title in matches:
            st.markdown(f"- **{title}**　`{genre}`")
    else:
        st.info("등록된 목록에서 찾지 못했어요. 다른 검색어를 입력해 보세요.")

# ── 아카이브 기록 ──
st.markdown("""
<div class="section-title">
    ▣ ARCHIVE RECORD — 자료실 기록
</div>
""", unsafe_allow_html=True)

info1, info2, info3 = st.columns(3)

info1.metric("등록 장르", f"{len(webtoon_data):02d}")
info2.metric("등록 작품", f"{len(all_titles)}종")
info3.metric("추천 시스템", "ONLINE")

st.caption(
    "※ 작품 수는 메인 페이지에 등록된 예시 데이터 기준입니다. "
    "실시간 플랫폼 순위와는 다를 수 있습니다."
)

st.markdown("""
<div class="footer">
    WEBTOON ARCHIVE · COLLECT YOUR STORIES
</div>
""", unsafe_allow_html=True)
