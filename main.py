import streamlit as st
import random

st.set_page_config(
    page_title="WEBTOON ARCHIVE",
    page_icon="📚",
    layout="wide"
)

# ── 조사한 웹툰 데이터 및 공식 플랫폼 링크 ──
webtoon_data = {
    "판타지": [
        "별을 품은 소드마스터",
        "종말이 찾아왔다",
        "샤MONEY",
        "생존지상주의",
        "검술 명가의 네크로맨서",
        "대마법사 커리큘럼",
        "집구석 절대자",
        "전지적 독자 시점",
        "하울링",
        "그림으로 승부",
        "엄마를 만나러 가는 길",
        "전자오락수호대",
        "무한의 마법사",
        "블랙 헤이즈",
        "SSS급 죽어야 사는 헌터",
        "천재 궁수의 스트리밍",
        "만렙 플레이어의 100번째 회귀",
        "성자는 개뿔, 현대의학의 힘이다",
        "월스트리트 천재의 시한부 투자법"
    ],
    "로맨스": [
        "백작가의 비밀스런 시녀님",
        "벙커의 낮",
        "세림의 철칙",
        "연상녀 클럽",
        "완벽한 선배의 Hide!",
        "해일주의보",
        "비공식 CC",
        "1인칭 혈육시점",
        "사랑이 끝나면 네가 끝난다",
        "인소의 법칙"
    ],
    "로맨스 판타지": [
        "백작가의 비밀스런 시녀님",
        "죽었는데 왜 집착하세요",
        "사신님과 3년 계약",
        "내 호수에 가둔 인어",
        "엄마가 계약결혼 했다",
        "이번 생은 가주가 되겠습니다"
    ],
    "액션": [
        "사랑은 좀비를 찢고",
        "정글쥬스",
        "싸움배달",
        "레디액션",
        "은퇴한 킬러는 힐링하고 싶다",
        "악마에 입문했습니다! 이루마 군",
        "엔드와 세이브",
        "흡혈귀는 툭하면 죽는다"
    ],
    "스릴러": [
        "44교시 생존수업",
        "쪽팔려 게임",
        "똑 닮은 딸",
        "제물 투표",
        "귀촌리",
        "모닥불 친구들",
        "유령의 노래"
    ],
    "BL": [
        "남고 소년",
        "시맨틱 에러(개정판)"
    ],
    "기타": []
}

webtoon_links = {
    "별을 품은 소드마스터": "https://comic.naver.com/webtoon/list?titleId=816809",
    "종말이 찾아왔다": "https://comic.naver.com/webtoon/list?titleId=838002",
    "샤MONEY": "https://comic.naver.com/webtoon/list?titleId=840014",
    "생존지상주의": "https://comic.naver.com/webtoon/list?titleId=853709",
    "검술 명가의 네크로맨서": "https://comic.naver.com/webtoon/list?titleId=850499",
    "대마법사 커리큘럼": "https://comic.naver.com/webtoon/list?titleId=844951",
    "집구석 절대자": "https://comic.naver.com/webtoon/list?titleId=834351",
    "전지적 독자 시점": "https://comic.naver.com/webtoon/list?titleId=747269",
    "하울링": "https://comic.naver.com/webtoon/list?titleId=854794",
    "그림으로 승부": "https://comic.naver.com/webtoon/list?titleId=853095",
    "엄마를 만나러 가는 길": "https://comic.naver.com/webtoon/list?titleId=834369",
    "전자오락수호대": "https://comic.naver.com/webtoon/list?titleId=637931",
    "무한의 마법사": "https://page.kakao.com/content/60910969/",
    "블랙 헤이즈": "https://page.kakao.com/content/65986358/",
    "SSS급 죽어야 사는 헌터": "https://page.kakao.com/content/56243215/",
    "천재 궁수의 스트리밍": "https://page.kakao.com/content/64007563/",
    "만렙 플레이어의 100번째 회귀": "https://page.kakao.com/content/62916616/",
    "성자는 개뿔, 현대의학의 힘이다": "https://page.kakao.com/content/59422125/",
    "월스트리트 천재의 시한부 투자법": "https://comic.naver.com/webtoon/list?titleId=854407",
    "백작가의 비밀스런 시녀님": "https://comic.naver.com/webtoon/list?titleId=830106",
    "벙커의 낮": "https://comic.naver.com/webtoon/list?titleId=846643",
    "세림의 철칙": "https://comic.naver.com/webtoon/list?titleId=852516",
    "연상녀 클럽": "https://comic.naver.com/webtoon/list?titleId=851476",
    "완벽한 선배의 Hide!": "https://comic.naver.com/webtoon/list?titleId=849742",
    "해일주의보": "https://comic.naver.com/webtoon/list?titleId=853833",
    "비공식 CC": "https://comic.naver.com/webtoon/list?titleId=851431",
    "1인칭 혈육시점": "https://comic.naver.com/webtoon/list?titleId=850236",
    "사랑이 끝나면 네가 끝난다": "https://comic.naver.com/webtoon/list?titleId=849864",
    "인소의 법칙": "https://page.kakao.com/content/52610652/",
    "남고 소년": "https://www.lezhin.com/ko/comic/highschoolboy",
    "시맨틱 에러(개정판)": "https://ridibooks.com/books/3392000097?\\_s=search&\\_q=%EC%8B%9C%EB%A7%A8%ED%8B%B1+%EC%97%90%EB%9F%AC&\\_rdt_sid=SearchBookListWithTab&\\_rdt_idx=2",
    "죽었는데 왜 집착하세요": "https://comic.naver.com/webtoon/list?titleId=826529",
    "사신님과 3년 계약": "https://comic.naver.com/webtoon/list?titleId=847850",
    "내 호수에 가둔 인어": "https://comic.naver.com/webtoon/list?titleId=834391",
    "엄마가 계약결혼 했다": "https://page.kakao.com/content/59882406/",
    "이번 생은 가주가 되겠습니다": "https://page.kakao.com/content/56566288/",
    "사랑은 좀비를 찢고": "https://comic.naver.com/webtoon/list?titleId=854591",
    "정글쥬스": "https://comic.naver.com/webtoon/list?titleId=762279",
    "싸움배달": "https://comic.naver.com/webtoon/list?titleId=850079",
    "레디액션": "https://comic.naver.com/webtoon/list?titleId=855128",
    "은퇴한 킬러는 힐링하고 싶다": "https://page.kakao.com/content/70268713/",
    "악마에 입문했습니다! 이루마 군": "https://page.kakao.com/content/52542095/",
    "엔드와 세이브": "https://page.kakao.com/content/55281534/",
    "흡혈귀는 툭하면 죽는다": "https://page.kakao.com/content/61388860/",
    "44교시 생존수업": "https://comic.naver.com/webtoon/list?titleId=836848",
    "쪽팔려 게임": "https://comic.naver.com/webtoon/list?titleId=847135",
    "똑 닮은 딸": "https://comic.naver.com/webtoon/list?titleId=774866",
    "제물 투표": "https://comic.naver.com/webtoon/list?titleId=850211",
    "귀촌리": "https://comic.naver.com/webtoon/list?titleId=822573",
    "모닥불 친구들": "https://comic.naver.com/webtoon/list?titleId=837439",
    "유령의 노래": "https://comic.naver.com/webtoon/list?titleId=823239"
}

all_titles = list(dict.fromkeys(
    title
    for titles in webtoon_data.values()
    for title in titles
))

# ── 저작권 및 출처 안내 ──
# 작품 제목과 장르 정보는 소개·분류 목적으로 기재합니다.
# 웹툰 원작의 이미지·표지·내용을 무단 복제하지 않습니다.
COPYRIGHT_NOTICE = (
    "이 사이트는 웹툰을 소개하고 분류하기 위한 비공식 개인 프로젝트입니다. "
    "웹툰 이미지와 표지는 사용하지 않으며, 작품명과 장르를 텍스트로 소개하고 공식 플랫폼 링크를 제공합니다. "
    "작품의 저작권 및 관련 권리는 각 작품의 작가와 권리자에게 있습니다. "
    "본 사이트는 웹툰 플랫폼과 공식 제휴 관계가 없습니다."
)

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

.copyright {
    background: #f7f3e4;
    border: 1px solid #a4b596;
    border-left: 5px solid #526b49;
    padding: 16px 20px;
    margin-top: 24px;
    color: #596b50;
    font-size: 13px;
    line-height: 1.9;
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

today_url = webtoon_links.get(st.session_state.main_daily_pick)
if today_url:
    st.link_button("공식 플랫폼에서 작품 보기 ↗", today_url, use_container_width=True)

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
    matches = list(dict.fromkeys(matches))

    if matches:
        st.markdown("##### 검색 결과")
        for genre, title in matches:
            url = webtoon_links.get(title)
            if url:
                st.markdown(f"- **[{title}]({url})**　`{genre}`")
            else:
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
    "※ 작품 수는 조사해 등록한 목록 기준입니다. "
    "공식 플랫폼 링크는 작품 페이지로 연결되며, 실시간 순위와는 다를 수 있습니다."
)

# ── 저작권 안내 ──
st.markdown(f"""
<div class="copyright">
    <strong>저작권 및 출처 안내</strong><br>
    {COPYRIGHT_NOTICE}<br>
    작품 감상은 각 작품의 공식 플랫폼을 이용해 주세요.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    WEBTOON ARCHIVE · COLLECT YOUR STORIES
</div>
""", unsafe_allow_html=True)
