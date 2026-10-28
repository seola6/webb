import streamlit as st

st.set_page_config(
    page_title="WEBTOON ARCHIVE",
    page_icon="📚",
    layout="wide"
)

# 조사한 웹툰 목록과 공식 플랫폼 링크
webtoon_data = {
    "판타지": [
        "별을 품은 소드마스터", "종말이 찾아왔다", "샤MONEY",
        "생존지상주의", "검술 명가의 네크로맨서", "대마법사 커리큘럼",
        "집구석 절대자", "전지적 독자 시점", "하울링", "그림으로 승부",
        "엄마를 만나러 가는 길", "전자오락수호대", "무한의 마법사",
        "블랙 헤이즈", "SSS급 죽어야 사는 헌터", "천재 궁수의 스트리밍",
        "만렙 플레이어의 100번째 회귀", "성자는 개뿔, 현대의학의 힘이다",
        "월스트리트 천재의 시한부 투자법"
    ],
    "로맨스": [
        "백작가의 비밀스런 시녀님", "벙커의 낮", "세림의 철칙",
        "연상녀 클럽", "완벽한 선배의 Hide!", "해일주의보",
        "비공식 CC", "1인칭 혈육시점", "사랑이 끝나면 네가 끝난다",
        "인소의 법칙"
    ],
    "로맨스 판타지": [
        "백작가의 비밀스런 시녀님", "죽었는데 왜 집착하세요",
        "사신님과 3년 계약", "내 호수에 가둔 인어",
        "엄마가 계약결혼 했다", "이번 생은 가주가 되겠습니다"
    ],
    "액션": [
        "사랑은 좀비를 찢고", "정글쥬스", "싸움배달", "레디액션",
        "은퇴한 킬러는 힐링하고 싶다", "악마에 입문했습니다! 이루마 군",
        "엔드와 세이브", "흡혈귀는 툭하면 죽는다"
    ],
    "스릴러": [
        "44교시 생존수업", "쪽팔려 게임", "똑 닮은 딸", "제물 투표",
        "귀촌리", "모닥불 친구들", "유령의 노래"
    ],
    "BL": [
        "남고 소년", "시맨틱 에러(개정판)"
    ]
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
    "시맨틱 에러(개정판)": "https://ridibooks.com/books/3392000097?_s=search&_q=%EC%8B%9C%EB%A7%A8%ED%8B%B1+%EC%97%90%EB%9F%AC&_rdt_sid=SearchBookListWithTab&_rdt_idx=2",
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
    title for titles in webtoon_data.values() for title in titles
))
COPYRIGHT_NOTICE = (
    "이 사이트는 웹툰을 소개하고 분류하기 위한 비공식 개인 프로젝트입니다. "
    "웹툰 이미지와 표지는 사용하지 않으며, 작품명과 장르를 텍스트로 소개하고 공식 플랫폼 링크를 제공합니다. "
    "작품의 저작권 및 관련 권리는 각 작품의 작가와 권리자에게 있습니다. "
    "본 사이트는 웹툰 플랫폼과 공식 제휴 관계가 없습니다."
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Do+Hyeon&display=swap');

:root {
    --yellow: #fff000;
    --red: #ff1717;
    --blue: #123bff;
    --black: #080808;
    --white: #ffffff;
}

.stApp {
    background: var(--yellow);
    color: var(--black);
    font-family: 'Do Hyeon', sans-serif;
}

[data-testid="stHeader"] {
    background: var(--yellow);
}

[data-testid="stSidebar"] {
    background: var(--red);
    border-right: 5px solid var(--black);
}

[data-testid="stSidebar"] * {
    color: var(--white) !important;
}

.block-container {
    max-width: 1450px;
    padding: 1rem 1.5rem 3rem;
}

h1, h2, h3, p, label {
    color: var(--black);
}

h1, h2, h3 {
    font-family: 'Black Han Sans', sans-serif;
}

hr {
    border: 0;
    border-top: 3px solid var(--black);
}

.stButton > button,
.stLinkButton > a {
    background: var(--red);
    color: var(--white) !important;
    border: 3px solid var(--black);
    border-radius: 0;
    font-family: 'Do Hyeon', sans-serif;
    font-size: 18px;
    box-shadow: 4px 4px 0 var(--black);
    transition: .12s;
}

.stButton > button:hover,
.stLinkButton > a:hover {
    background: var(--blue);
    color: var(--white) !important;
    border-color: var(--black);
    transform: translate(2px, 2px);
    box-shadow: 2px 2px 0 var(--black);
}

div[data-baseweb="select"] > div,
div[data-testid="stTextInput"] input {
    background: var(--white);
    color: var(--black);
    border: 3px solid var(--black);
    border-radius: 0;
}

div[data-testid="stMetric"] {
    background: var(--white);
    border: 3px solid var(--black);
    border-radius: 0;
    box-shadow: 5px 5px 0 var(--red);
}

div[data-testid="stMetricLabel"],
div[data-testid="stMetricValue"] {
    color: var(--black);
}

[data-testid="stExpander"] {
    background: var(--white);
    border: 3px solid var(--black);
    border-radius: 0;
    box-shadow: 4px 4px 0 var(--red);
    margin-bottom: 12px;
}

[data-testid="stExpander"] summary {
    font-family: 'Black Han Sans', sans-serif;
    font-size: 20px;
}

a {
    color: var(--blue) !important;
    font-weight: bold;
}

.poster {
    display: grid;
    grid-template-columns: 105px minmax(0, 1fr) 150px;
    gap: 15px;
    align-items: stretch;
    background: var(--yellow);
    border: 5px solid var(--black);
    padding: 15px;
    margin: 10px 0 25px;
    box-shadow: 8px 8px 0 var(--black);
}

.poster-logo {
    display: flex;
    align-items: center;
    justify-content: center;
    align-self: start;
    width: 100px;
    height: 100px;
    background: var(--red);
    color: var(--white);
    border: 3px solid var(--black);
    border-radius: 50%;
    font-family: 'Black Han Sans', sans-serif;
    font-size: 44px;
    writing-mode: vertical-rl;
    transform: rotate(-5deg);
}

.poster-main {
    min-width: 0;
}

.poster-small {
    font-size: 15px;
    font-weight: bold;
    line-height: 1.6;
}

.main-title {
    font-family: 'Black Han Sans', sans-serif;
    font-size: clamp(35px, 6vw, 82px);
    color: var(--red);
    line-height: 1;
    letter-spacing: -2px;
    text-shadow: 3px 3px 0 var(--black);
    margin: 8px 0 14px;
    overflow-wrap: anywhere;
}

.poster-subtitle {
    color: var(--blue);
    font-family: 'Black Han Sans', sans-serif;
    font-size: clamp(18px, 2.8vw, 35px);
    line-height: 1.4;
    overflow-wrap: anywhere;
}

.poster-side {
    background: var(--red);
    border: 3px solid var(--black);
    color: var(--white);
    padding: 10px 7px;
    text-align: center;
    font-family: 'Black Han Sans', sans-serif;
    font-size: 19px;
    line-height: 1.65;
    overflow-wrap: anywhere;
}

.poster-side * {
    color: var(--white) !important;
}

.section-title {
    background: var(--red);
    color: var(--white);
    border: 3px solid var(--black);
    padding: 8px 12px;
    margin: 28px 0 15px;
    box-shadow: 4px 4px 0 var(--black);
    font-family: 'Black Han Sans', sans-serif;
    font-size: 23px;
}

.section-title small {
    float: right;
    font-size: 12px;
    padding-top: 8px;
}

.paper-box,
.index-card,
.copyright {
    background: var(--white);
    border: 3px solid var(--black);
    border-radius: 0;
    padding: 15px;
    margin-bottom: 12px;
    box-shadow: 5px 5px 0 var(--black);
}

.red-label {
    display: inline-block;
    background: var(--red);
    color: var(--white);
    border: 2px solid var(--black);
    padding: 4px 8px;
    font-size: 14px;
}

.index-number,
.catalog-count {
    color: var(--red);
    font-weight: bold;
}

.index-title {
    font-family: 'Black Han Sans', sans-serif;
    font-size: 25px;
    margin: 8px 0;
}

.index-desc,
.small-note {
    font-size: 15px;
    line-height: 1.7;
}

.footer {
    text-align: center;
    border-top: 4px solid var(--black);
    margin-top: 35px;
    padding-top: 15px;
    font-size: 14px;
    font-weight: bold;
}

@media (max-width: 700px) {
    .block-container {
        padding: .6rem .7rem 2rem;
    }

    .poster {
        grid-template-columns: 1fr;
    }

    .poster-logo {
        width: 75px;
        height: 75px;
        font-size: 32px;
    }

    .poster-side {
        font-size: 17px;
    }

    .section-title {
        font-size: 20px;
    }
}
</style>
""", unsafe_allow_html=True)

# 왼쪽 신문 제호
with st.sidebar:
    st.markdown("""
    <div style="font-family:'Black Han Sans',sans-serif;font-size:30px;line-height:.95;
    color:#e8dfc9;border:2px solid #b9aa8d;padding:15px 10px;transform:rotate(-1deg);">
    WEBTOON<br>ARCHIVE
    </div>
    <p style="font-size:12px;line-height:1.8;color:#c7b99c!important;margin-top:16px;">
    웹툰을 수집하고,<br>발견하고, 기록하다.<br>
    <span style="color:#c85a4b!important;">VOL. 001 · 2026</span></p>
    <hr>
    """, unsafe_allow_html=True)
    st.markdown("### ☰ 목차")
    st.markdown("- **01** 작품 도감")
    st.markdown("- **02** 웹툰 추천")
    st.markdown("- **03** 요일별 랭킹")
    st.markdown("- **04** 캐릭터 생성기")
    st.markdown("- **05** 웹툰 룰렛")
    st.markdown("---")
    st.caption("COLLECT YOUR STORIES")

st.markdown("""
<div class="topline"><span>지금도 누군가의 마음을 두드리는, 그 이야기들</span><span>THE INDEPENDENT WEBTOON PAPER</span></div>
<div class="poster">
  <div class="poster-side">
    <div class="poster-kicker">웹툰 기록 보관소</div>
    <div style="font-size:25px;font-weight:800;line-height:1.25;margin:12px 0;">오늘의 이야기,<br>오래도록 기록하다.</div>
    <div style="font-size:12px;color:#c9bea4;">장르별 작품 수집 · 공식 플랫폼 안내</div>
  </div>
  <div>
    <div class="main-title">WEBTOON<br>ARCHIVE<span style="color:#343a32;">✳</span></div>
    <div class="poster-sub">THE INDEPENDENT WEBTOON PAPER · VOL. 001</div>
    <div class="poster-stamp">READ · COLLECT · REMEMBER</div>
  </div>
  <div class="poster-note">
    <b>당신의 다음 이야기는<br>여기서 시작됩니다.</b>
    <p style="margin:9px 0 0;">취향에 맞는 장르를 찾고<br>새로운 작품을 발견해 보세요.</p>
    <div style="font:11px 'Special Elite',monospace;color:#8d3029;margin-top:8px;">EST. 2026 ★</div>
  </div>
</div>
""", unsafe_allow_html=True)

# 아카이브 요약
unique_genre_count = len(webtoon_data)
unique_title_count = len(all_titles)
st.markdown('<div class="section-title">아카이브 현황 <small>ARCHIVE OVERVIEW</small></div>', unsafe_allow_html=True)
m1, m2, m3 = st.columns(3)
m1.metric("수집 장르", f"{unique_genre_count}개")
m2.metric("수록 작품", f"{unique_title_count}종")
m3.metric("작품 이미지", "미사용")

# 오늘의 작품 및 바로가기
st.markdown('<div class="section-title">오늘의 웹툰 <small>TODAY’S PICK</small></div>', unsafe_allow_html=True)
left, right = st.columns([1.55, 1])
with left:
    st.markdown("""
    <div class="paper-box">
      <span class="red-label">EDITOR'S PICK</span>
      <h3 style="margin:3px 0 8px;font-size:25px;">전지적 독자 시점</h3>
      <div class="small-note">판타지 · 네이버웹툰</div>
      <hr>
      <p style="font-size:13px;line-height:1.9;">
      세상이 멸망한 후, 유일하게 결말을 알고 있는 독자.<br>
      그는 다시 시작된 이야기 속에서 자신만의 길을 찾아갑니다.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("공식 페이지 바로가기 ↗", webtoon_links["전지적 독자 시점"], use_container_width=True)
with right:
    st.markdown('<div class="paper-box"><span class="red-label">QUICK ACCESS</span>', unsafe_allow_html=True)
    st.markdown("**바로가기**")
    st.markdown("- 작품 검색 및 장르별 목록")
    st.markdown("- 공식 플랫폼에서 작품 감상")
    st.markdown("- 아래 목차에서 장르별 작품 펼쳐보기")
    st.markdown("</div>", unsafe_allow_html=True)

# 목차
st.markdown('<div class="section-title">사이트 목차 <small>ARCHIVE INDEX</small></div>', unsafe_allow_html=True)
index_items = [
    ("01", "작품 도감", "장르별 웹툰 목록과 공식 작품 링크를 확인합니다.", "catalog"),
    ("02", "웹툰 추천", "장르와 분위기를 기준으로 작품을 찾아봅니다.", "pages/1_웹툰_추천.py"),
    ("03", "요일별 랭킹", "요일별로 정리된 웹툰 순위를 살펴봅니다.", "pages/2_요일별_랭킹.py"),
    ("04", "캐릭터 생성기", "캐릭터 아이디어를 만들어 봅니다.", "pages/3_캐릭터_생성기.py"),
    ("05", "웹툰 룰렛", "무작위로 작품 하나를 뽑아 봅니다.", "pages/4_웹툰_룰렛.py")
]
for start in range(0, len(index_items), 2):
    cols = st.columns(2)
    for col, item in zip(cols, index_items[start:start + 2]):
        num, title, desc, target = item
        with col:
            st.markdown(f"""
            <div class="index-card">
              <div class="index-number">FILE NO. {num} / WEBTOON ARCHIVE</div>
              <div class="index-title">{title}</div>
              <div class="index-desc">{desc}</div>
            </div>
            """, unsafe_allow_html=True)
            if target.startswith("pages/"):
                if st.button(f"{title} 페이지 열기 ↗", key=f"index_{num}", use_container_width=True):
                    st.switch_page(target)
            else:
                if st.button("작품 목록 보기 ↓", key=f"index_{num}", use_container_width=True):
                    st.session_state["main_catalog_focus"] = True

# 작품 검색
st.markdown('<div class="section-title">작품 검색 <small>CATALOG SEARCH</small></div>', unsafe_allow_html=True)
search_col, genre_col = st.columns([1.4, 1])
with search_col:
    query = st.text_input("작품명 검색", placeholder="예: 전지적 독자 시점, 정글쥬스")
with genre_col:
    selected_genre = st.selectbox("장르별 목차", ["전체 장르"] + list(webtoon_data.keys()))

if query.strip():
    matches = []
    for genre, titles in webtoon_data.items():
        if selected_genre != "전체 장르" and genre != selected_genre:
            continue
        for title in titles:
            if query.strip().casefold() in title.casefold():
                matches.append((genre, title))
    matches = list(dict.fromkeys(matches))
    st.markdown('<div class="section-title">검색 결과 <small>SEARCH RESULTS</small></div>', unsafe_allow_html=True)
    if matches:
        for genre, title in matches:
            url = webtoon_links.get(title)
            link_text = f"[{title}]({url})" if url else title
            st.markdown(f"- {link_text}　`{genre}`")
    else:
        st.info("검색 결과가 없습니다. 다른 검색어를 입력해 보세요.")

# 장르별 작품 목록
st.markdown('<div class="section-title">장르별 작품 목록 <small>COMPLETE CATALOG</small></div>', unsafe_allow_html=True)
st.caption("장르 이름을 펼치면 등록된 작품을 볼 수 있습니다. 작품명 링크를 누르면 공식 플랫폼으로 이동합니다.")
for genre, titles in webtoon_data.items():
    should_expand = selected_genre == genre or selected_genre == "전체 장르"
    with st.expander(f"{genre}　·　{len(titles)}개 분류 항목", expanded=should_expand):
        st.markdown(f'<div class="catalog-count">CATEGORY FILE / {genre.upper()} / {len(titles)} TITLES</div>', unsafe_allow_html=True)
        for title in titles:
            url = webtoon_links.get(title)
            if url:
                st.markdown(f"- [{title}]({url})")
            else:
                st.markdown(f"- {title}")

st.markdown('<div class="section-title">저작권 및 출처 <small>COPYRIGHT & SOURCE</small></div>', unsafe_allow_html=True)
st.markdown(
    f'<div class="copyright"><strong>저작권 안내</strong><br>{COPYRIGHT_NOTICE}'
    '<br>작품 감상은 각 작품의 공식 플랫폼을 이용해 주세요.</div>',
    unsafe_allow_html=True
)
st.markdown("""
<div class="footer">
  WEBTOON ARCHIVE · COLLECT YOUR STORIES · VOL. 001
</div>
""", unsafe_allow_html=True)
