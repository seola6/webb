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
.stApp { background:#e8eddd; color:#29432f; }
[data-testid="stSidebar"] { background:#d3dfc4; }
.block-container { max-width:1100px; padding-top:2rem; padding-bottom:3rem; }
.poster {
    background:#f7f3e4; border:4px double #526b49; padding:38px 24px;
    text-align:center; box-shadow:8px 8px 0 #bdcbae; margin-bottom:30px;
}
.eyebrow { letter-spacing:4px; color:#718568; font-size:12px; }
.main-title {
    font-family:Georgia,serif; font-size:clamp(40px,7vw,66px);
    font-weight:bold; color:#29432f; margin:20px 0 10px; line-height:1.05;
}
.subtitle { font-size:15px; color:#687b58; letter-spacing:2px; }
.stamp { display:inline-block; margin-top:22px; padding:7px 13px;
    border:2px solid #526b49; color:#526b49; transform:rotate(-3deg); }
.section-title {
    font-family:Georgia,serif; font-size:22px; font-weight:bold;
    border-bottom:2px solid #526b49; padding-bottom:9px; margin:30px 0 16px;
}
.index-card {
    background:#f7f3e4; border:1px solid #a4b596; padding:17px 18px;
    min-height:105px; box-shadow:4px 4px 0 #cbd6bd; margin-bottom:10px;
}
.index-number { color:#718568; font-size:11px; letter-spacing:2px; }
.index-title { font-size:18px; font-weight:bold; margin:9px 0; color:#29432f; }
.index-desc { font-size:13px; line-height:1.7; color:#596b50; }
.catalog-box {
    background:#f7f3e4; border:1px solid #a4b596; padding:12px 16px;
    margin:6px 0; line-height:1.8;
}
.catalog-count { color:#718568; font-size:12px; letter-spacing:1px; }
.copyright {
    background:#f7f3e4; border:1px solid #a4b596; border-left:5px solid #526b49;
    padding:15px 18px; margin-top:25px; color:#596b50; font-size:13px; line-height:1.9;
}
.stButton > button {
    background:#526b49; color:white; border-radius:3px; border:1px solid #29432f;
    min-height:40px;
}
.stButton > button:hover { background:#718568; color:white; border-color:#29432f; }
div[data-baseweb="select"] > div, div[data-testid="stTextInput"] input {
    background:#f7f3e4; border-color:#a4b596;
}
.footer {
    border-top:2px solid #718568; text-align:center; margin-top:38px; padding-top:18px;
    color:#718568; letter-spacing:2px; font-size:11px;
}
@media(max-width:600px) {
    .poster { padding:26px 12px; }
    .eyebrow { letter-spacing:2px; }
    .subtitle { letter-spacing:1px; }
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="poster">
  <div class="eyebrow">THE INDEPENDENT WEBTOON PAPER · VOL. 001</div>
  <div class="main-title">WEBTOON<br>ARCHIVE</div>
  <div class="subtitle">작품을 모으고, 분류하고, 기록하다.</div>
  <div class="stamp">EST. 2026 · WEBTOON CATALOG</div>
</div>
""", unsafe_allow_html=True)

# 개요 지표
unique_genre_count = len(webtoon_data)
unique_title_count = len(all_titles)
st.markdown('<div class="section-title">▣ ARCHIVE OVERVIEW — 아카이브 개요</div>', unsafe_allow_html=True)
m1, m2, m3 = st.columns(3)
m1.metric("분류 장르", f"{unique_genre_count}개")
m2.metric("수록 작품", f"{unique_title_count}종")
m3.metric("작품 이미지", "미사용")

st.markdown(
    "이곳은 추천 결과를 보여주는 메인 화면이 아니라, 조사한 웹툰을 한눈에 찾아보는 작품 목록입니다. "
    "아래 목차에서 장르를 살펴보거나 작품명을 검색할 수 있습니다."
)

# 목차 및 다른 기능 안내
st.markdown('<div class="section-title">▣ ARCHIVE INDEX — 사이트 목차</div>', unsafe_allow_html=True)
index_items = [
    ("01", "작품 도감", "장르별 웹툰 목록과 공식 작품 링크를 확인합니다.", "아래 작품 목록"),
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
              <div class="index-number">FILE NO. {num}</div>
              <div class="index-title">{title}</div>
              <div class="index-desc">{desc}</div>
            </div>
            """, unsafe_allow_html=True)
            if target.startswith("pages/"):
                if st.button(f"{title} 페이지 열기 ↗", key=f"index_{num}", use_container_width=True):
                    st.switch_page(target)
            else:
                st.button("작품 목록 보기 ↓", key=f"index_{num}", use_container_width=True,
                          on_click=lambda: st.session_state.update({"main_catalog_focus": True}))

st.markdown('<div class="section-title">▣ CATALOG SEARCH — 작품 검색</div>', unsafe_allow_html=True)
query = st.text_input("작품명 검색", placeholder="예: 전지적 독자 시점, 정글쥬스")
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
    st.markdown('<div class="section-title">▣ SEARCH RESULTS — 검색 결과</div>', unsafe_allow_html=True)
    if matches:
        for genre, title in matches:
            url = webtoon_links.get(title)
            link_text = f"[{title}]({url})" if url else title
            st.markdown(f"- {link_text}　`{genre}`")
    else:
        st.info("검색 결과가 없습니다. 다른 검색어를 입력해 보세요.")

st.markdown('<div class="section-title">▣ COMPLETE CATALOG — 전체 작품 목록</div>', unsafe_allow_html=True)
st.caption("장르 이름을 펼치면 해당 분류에 등록된 작품을 볼 수 있습니다. 작품명 링크를 누르면 공식 플랫폼으로 이동합니다.")

for genre, titles in webtoon_data.items():
    with st.expander(f"{genre}　·　{len(titles)}개 분류 항목", expanded=(selected_genre == genre or selected_genre == "전체 장르")):
        # 중복 분류 작품은 장르별 목록에는 그대로 표시하고, 전체 작품 수는 중복 제거 기준으로 계산합니다.
        for title in titles:
            url = webtoon_links.get(title)
            if url:
                st.markdown(f"- [{title}]({url})")
            else:
                st.markdown(f"- {title}")

st.markdown('<div class="section-title">▣ COPYRIGHT & SOURCE — 저작권 및 출처</div>', unsafe_allow_html=True)
st.markdown(f'<div class="copyright"><strong>저작권 안내</strong><br>{COPYRIGHT_NOTICE}<br>작품 감상은 각 작품의 공식 플랫폼을 이용해 주세요.</div>', unsafe_allow_html=True)

st.markdown("""
<div class="footer">
  WEBTOON ARCHIVE · COLLECT YOUR STORIES
</div>
""", unsafe_allow_html=True)
