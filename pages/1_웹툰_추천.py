import streamlit as st
import random

st.set_page_config(
    page_title="WEBTOON ARCHIVE | 추천 자료실",
    page_icon="📚",
    layout="wide"
)

# ── 낡은 찌라시 / 전단지 디자인 ──
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&display=swap');

:root {
    --paper: #e7dcc0;
    --cream: #f6edd8;
    --ink: #26372d;
    --green: #304635;
    --red: #a33d30;
    --muted: #786d58;
    --line: #9d8d6d;
}

.stApp {
    background-color: var(--paper);
    background-image:
        radial-gradient(#75694d 0.55px, transparent 0.7px),
        repeating-linear-gradient(
            0deg,
            rgba(65, 51, 31, 0.025) 0px,
            rgba(65, 51, 31, 0.025) 1px,
            transparent 1px,
            transparent 4px
        );
    background-size: 6px 6px, auto;
    color: var(--ink);
    font-family: 'Gowun Batang', serif;
}

.block-container {
    max-width: 1120px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* 왼쪽 사이드바 */
[data-testid="stSidebar"] {
    background-color: var(--green);
    border-right: 5px solid var(--red);
}
[data-testid="stSidebar"] > div:first-child {
    background: transparent;
}
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
    color: var(--cream);
}
[data-testid="stSidebar"] a {
    color: var(--cream) !important;
    border-radius: 0 !important;
    border-bottom: 1px dashed rgba(246, 237, 216, 0.3);
    padding: 10px 8px !important;
    margin: 3px 0 !important;
}
[data-testid="stSidebar"] a:hover {
    background: rgba(246, 237, 216, 0.12) !important;
}
[data-testid="stSidebar"] [aria-current="page"] {
    background: var(--red) !important;
    color: var(--cream) !important;
}

/* 상단 찌라시 헤드라인 */
.archive-header {
    position: relative;
    background: var(--green);
    color: var(--cream);
    padding: 38px 25px 32px;
    border: 3px double var(--cream);
    outline: 2px solid var(--ink);
    outline-offset: 4px;
    text-align: center;
    margin: 8px 0 32px;
    box-shadow: 9px 9px 0 rgba(38, 55, 45, 0.22);
    transform: rotate(-0.2deg);
}
.archive-header .small {
    font-size: 11px;
    letter-spacing: 4px;
    color: #dfcba1;
    font-weight: bold;
}
.archive-header h1 {
    color: var(--cream);
    font-family: Impact, 'Arial Black', sans-serif;
    font-size: clamp(30px, 5vw, 57px);
    font-weight: 1000;
    letter-spacing: 1px;
    line-height: 1.1;
    margin: 20px 0;
    text-shadow: 3px 3px 0 rgba(0, 0, 0, 0.2);
}
.archive-header p {
    color: #e6d7b8;
    font-size: 14px;
    font-weight: bold;
}

/* 공지 전단 */
.notice {
    background: var(--cream);
    border: 2px solid var(--ink);
    padding: 18px 22px;
    margin: 18px 0 25px;
    box-shadow: 5px 5px 0 #c7b99a;
    position: relative;
}
.notice-title {
    display: inline-block;
    font-family: Georgia, serif;
    font-size: 12px;
    letter-spacing: 3px;
    color: var(--red);
    font-weight: bold;
    border-bottom: 2px solid var(--red);
    padding-bottom: 4px;
    margin-bottom: 8px;
}

/* 섹션 제목 */
.section-title {
    background: var(--green);
    color: var(--cream);
    border-left: 8px solid var(--red);
    padding: 9px 13px;
    margin: 30px 0 16px;
    font-family: Impact, 'Arial Black', sans-serif;
    font-size: 21px;
    letter-spacing: 1px;
    box-shadow: 4px 4px 0 #c7b99a;
}

/* 추천 작품 종이 */
.poster {
    background: var(--cream);
    border: 2px solid var(--ink);
    outline: 1px dashed var(--line);
    outline-offset: -7px;
    padding: 24px;
    box-shadow: 7px 7px 0 #c7b99a;
    margin: 12px 0 17px;
    position: relative;
    transform: rotate(-0.15deg);
}
.poster-stamp {
    display: inline-block;
    color: var(--red);
    border: 3px solid var(--red);
    padding: 5px 10px;
    font-family: Georgia, serif;
    font-size: 11px;
    font-weight: bold;
    transform: rotate(-4deg);
    letter-spacing: 2px;
}
.result-title {
    font-family: Impact, 'Arial Black', sans-serif;
    font-size: clamp(27px, 4vw, 38px);
    font-weight: 900;
    color: var(--green);
    margin: 18px 0 12px;
    border-bottom: 2px solid var(--ink);
    padding-bottom: 12px;
}
.result-description {
    font-size: 15px;
    line-height: 2;
    color: #454537;
}

/* 버튼 */
div.stButton > button,
div.stLinkButton > a {
    background: var(--red);
    color: var(--cream);
    border: 2px solid var(--ink);
    border-radius: 0;
    padding: 10px 18px;
    font-family: 'Gowun Batang', serif;
    font-weight: bold;
    box-shadow: 4px 4px 0 var(--ink);
    transition: 0.12s ease;
}
div.stButton > button:hover,
div.stLinkButton > a:hover {
    background: var(--green);
    color: white;
    border-color: var(--ink);
    transform: translate(2px, 2px);
    box-shadow: 2px 2px 0 var(--ink);
}

/* 선택창 */
div[data-baseweb="select"] > div,
div[data-testid="stTextInput"] input {
    background: var(--cream);
    border: 2px solid var(--ink);
    border-radius: 0;
}

/* 하단 안내 */
.footer-note {
    text-align: center;
    color: var(--muted);
    font-family: Georgia, serif;
    font-size: 11px;
    font-weight: bold;
    letter-spacing: 2px;
    border-top: 3px double var(--ink);
    border-bottom: 1px solid var(--ink);
    padding: 15px 5px;
    margin-top: 40px;
}

@media (max-width: 600px) {
    .archive-header { padding: 28px 14px; }
    .archive-header .small { letter-spacing: 1px; }
    .poster { padding: 20px 15px; }
}
</style>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
<div style="
    background:#26372d;
    color:#f6edd8;
    border:2px dashed #e7dcc0;
    padding:18px 8px;
    text-align:center;
    margin:8px 0 24px;
    transform:rotate(-1deg);
">
    <div style="font-size:10px;letter-spacing:3px;">
        THE UNOFFICIAL PAPER
    </div>
    <div style="
        font-family:Impact,Georgia,serif;
        font-size:26px;
        font-weight:900;
        line-height:1.1;
        color:#e5b5a4;
        margin:12px 0;
    ">
        WEBTOON<br>ARCHIVE
    </div>
    <div style="font-size:10px;letter-spacing:2px;">
        VOL. 001 · EST. 2026
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="archive-header">
  <div class="small">WEBTOON ARCHIVE · UNOFFICIAL PAPER NO. 01</div>
  <h1>WEBTOON<br>RECOMMENDATION</h1>
  <p>오늘의 취향을 찾아드립니다 · 작품 자료실 제1호</p>
</div>
<div class="notice">
  <div class="notice-title">ARCHIVE NOTE</div>
  장르와 기분을 선택하면 작품 하나를 추천해 줍니다. 작품 제목 아래 버튼을 눌러 작품 페이지로 이동할 수 있어요.
</div>
""", unsafe_allow_html=True)

webtoon_data = {
    "판타지": [
        {"title": "전지적 독자 시점", "description": "소설 속 세계가 현실이 된 후 살아남기 위한 이야기"},
        {"title": "화산귀환", "description": "전설의 검객이 환생해 몰락한 문파를 재건하는 무협 판타지"},
        {"title": "나 혼자만 레벨업", "description": "최약체 헌터가 특별한 능력을 얻어 성장하는 이야기"},
        {"title": "초인의 게임", "description": "초능력자들이 펼치는 생존과 경쟁의 이야기"},
        {"title": "철수를 구하시오", "description": "SF와 판타지 요소가 결합된 독특한 세계관의 작품"}
    ],
    "로맨스": [
        {"title": "작전명 순정", "description": "첫사랑과 우정을 그린 청춘 로맨스"},
        {"title": "세기말 풋사과 보습학원", "description": "1990년대를 배경으로 한 학원 로맨스"},
        {"title": "바른연애 길잡이", "description": "대학생들의 현실적인 연애 이야기를 다룬 작품"},
        {"title": "여신강림", "description": "메이크업으로 자신감을 찾은 여학생의 성장과 사랑 이야기"},
        {"title": "연애혁명", "description": "고등학생들의 사랑과 우정을 그린 학원 로맨스"}
    ],
    "액션": [
        {"title": "참교육", "description": "학교 문제에 맞서는 교육관들의 이야기"},
        {"title": "캐슬", "description": "복수를 위해 범죄 조직에 맞서는 남자의 액션 느와르"},
        {"title": "외모지상주의", "description": "두 개의 몸을 가지게 된 주인공의 성장과 격투 이야기"},
        {"title": "격기 3반", "description": "격투기를 중심으로 펼쳐지는 학원 액션물"},
        {"title": "약한영웅", "description": "주인공이 지능과 전략으로 싸워 나가는 이야기"}
    ],
    "스릴러": [
        {"title": "타인은 지옥이다", "description": "수상한 고시원 사람들 사이에서 벌어지는 심리 스릴러"},
        {"title": "스위트홈", "description": "사람들이 괴물로 변하는 세상에서 살아남기 위한 이야기"},
        {"title": "돼지우리", "description": "기억을 잃은 남자가 의문의 섬에서 겪는 사건들"},
        {"title": "방탈출", "description": "목숨을 건 게임과 퍼즐을 풀어나가는 스릴러"},
        {"title": "살인자ㅇ난감", "description": "우연한 살인을 계기로 연쇄 사건에 휘말리는 이야기"}
    ],
    "BL": [
        {"title": "체크메이트", "description": "복수와 집착이 얽힌 관계를 그린 작품"},
        {"title": "물가의 밤", "description": "복잡한 감정선과 관계를 중심으로 한 작품"},
        {"title": "남고 소년", "description": "고등학생들의 일상과 성장을 그린 작품"},
        {"title": "시맨틱 에러(개정판)", "description": "정반대 성격의 대학생들이 만나 벌어지는 이야기"},
        {"title": "위험한 편의점", "description": "편의점 아르바이트생과 손님의 관계를 그린 작품"}
    ],
    "드라마": [
        {"title": "유미의 세포들", "description": "세포들의 시선으로 그려낸 현실적인 일상과 연애 이야기"},
        {"title": "이번 생도 잘 부탁해", "description": "전생의 기억을 가진 주인공의 사랑과 성장 이야기"},
        {"title": "정년이", "description": "국극 배우를 꿈꾸는 소녀의 성장 이야기"},
        {"title": "중증외상센터 : 골든 아워", "description": "생명을 살리기 위해 노력하는 의료진들의 이야기"},
        {"title": "가비지타임", "description": "농구부 학생들의 성장과 우정을 그린 스포츠 드라마"}
    ]
}

webtoon_links = {
    "전지적 독자 시점": "https://comic.naver.com/webtoon/list?titleId=747269",
    "화산귀환": "https://comic.naver.com/webtoon/list?titleId=769209",
    "나 혼자만 레벨업": "https://page.kakao.com/content/50866481",
    "초인의 게임": "https://comic.naver.com/webtoon/list?titleId=795658",
    "철수를 구하시오": "https://ridibooks.com/books/4851000001",
    "작전명 순정": "https://comic.naver.com/webtoon/list?titleId=793275",
    "세기말 풋사과 보습학원": "https://comic.naver.com/webtoon/list?titleId=761722",
    "바른연애 길잡이": "https://comic.naver.com/webtoon/list?titleId=703852",
    "여신강림": "https://comic.naver.com/webtoon/list?titleId=703846",
    "연애혁명": "https://comic.naver.com/webtoon/list?titleId=570503",
    "참교육": "https://comic.naver.com/webtoon/list?titleId=758037",
    "캐슬": "https://comic.naver.com/webtoon/list?titleId=733074",
    "외모지상주의": "https://comic.naver.com/webtoon/list?titleId=650305",
    "격기 3반": "https://comic.naver.com/webtoon/list?titleId=701535",
    "약한영웅": "https://comic.naver.com/webtoon/list?titleId=710751",
    "타인은 지옥이다": "https://comic.naver.com/webtoon/list?titleId=721433",
    "스위트홈": "https://comic.naver.com/webtoon/list?titleId=708378",
    "돼지우리": "https://comic.naver.com/webtoon/list?titleId=732955",
    "방탈출": "https://comic.naver.com/webtoon/list?titleId=737628",
    "살인자ㅇ난감": "https://comic.naver.com/webtoon/list?titleId=701081",
    "유미의 세포들": "https://comic.naver.com/webtoon/list?titleId=709731",
    "중증외상센터 : 골든 아워": "https://comic.naver.com/webtoon/list?titleId=738174",
    "가비지타임": "https://comic.naver.com/webtoon/list?titleId=701545",
    "남고 소년": "https://www.lezhin.com/ko/comic/highschoolboy",
    "시맨틱 에러(개정판)": "https://ridibooks.com/books/3392000097"
}


st.markdown('<div class="section-title">01 / 작품 찾기</div>', unsafe_allow_html=True)
left, right = st.columns(2)
with left:
    genre = st.selectbox("장르 선택", list(webtoon_data.keys()))
with right:
    mood = st.selectbox("오늘의 기분", ["상관없음", "힐링", "성장", "피폐", "개그", "긴장감"])

if "recommended_webtoon" not in st.session_state:
    st.session_state.recommended_webtoon = None

if st.button("✦ 추천 받기", use_container_width=True):
    st.session_state.recommended_webtoon = random.choice(webtoon_data[genre])

if st.session_state.recommended_webtoon:
    item = st.session_state.recommended_webtoon
    st.markdown('<div class="section-title">02 / 오늘의 추천 작품</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="poster">
      <span class="poster-stamp">ARCHIVE PICK</span>
      <div class="result-title">{item["title"]}</div>
      <div class="result-description">{item["description"]}</div>
    </div>
    """, unsafe_allow_html=True)
    link = webtoon_links.get(item["title"])
    if link:
        st.link_button("작품 페이지 바로가기 ↗", link, use_container_width=True)
    else:
        st.info("이 작품의 링크는 아직 등록되지 않았어요.")
    if st.button("다른 작품 추천받기", use_container_width=True):
        st.session_state.recommended_webtoon = random.choice(webtoon_data[genre])
        st.rerun()

st.markdown('<div class="footer-note">WEBTOON ARCHIVE · 개인 취향 탐색용 자료실</div>', unsafe_allow_html=True)
