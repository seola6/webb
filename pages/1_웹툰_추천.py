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

# ── 텍스트 어드벤처 전용 연출 ──
st.markdown("""
<style>
.story-screen {
    background: #171d18;
    color: #d9d4bd;
    border: 2px solid #a33d30;
    outline: 1px dashed #8c8065;
    outline-offset: 5px;
    padding: 25px;
    margin: 16px 0 24px;
    box-shadow: 9px 9px 0 rgba(38, 25, 20, .22);
    font-family: 'Courier New', monospace;
    line-height: 1.9;
}
.story-kicker {
    color: #d46c55;
    font-size: 11px;
    letter-spacing: 3px;
    border-bottom: 1px dashed #726650;
    padding-bottom: 10px;
    margin-bottom: 15px;
}
.story-line {
    color: #e8dfc7;
    font-size: 16px;
    margin: 8px 0;
}
.story-dialogue {
    color: #a9c09a;
    border-left: 3px solid #a33d30;
    padding: 8px 12px;
    margin: 15px 0;
    background: rgba(246, 237, 216, .045);
}
.story-warning {
    color: #d46c55;
    font-weight: bold;
    letter-spacing: 1px;
}
.story-status {
    display: inline-block;
    border: 1px solid #8c8065;
    padding: 4px 8px;
    color: #d9d4bd;
    font-size: 10px;
    letter-spacing: 2px;
    margin: 3px 5px 3px 0;
}
.story-choice-label {
    font-size: 12px;
    letter-spacing: 2px;
    color: #a33d30;
    font-weight: bold;
    margin: 18px 0 8px;
}
.story-result {
    background: #f6edd8;
    color: #26372d;
    border: 3px double #304635;
    padding: 24px;
    margin: 16px 0;
    box-shadow: 7px 7px 0 #c7b99a;
}
.story-result small {
    color: #a33d30;
    letter-spacing: 3px;
    font-weight: bold;
}
.story-result h2 {
    color: #304635;
    font-family: Impact, 'Arial Black', sans-serif;
    font-size: 32px;
    margin: 12px 0;
}
div.stButton > button {
    text-align: left;
    white-space: normal;
    min-height: 48px;
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


# ── 분기형 텍스트 어드벤처 ──
st.markdown("""
<div class="section-title">NIGHT SHIFT / 야간 자료실</div>
<div class="notice">
  <div class="notice-title">긴급 열람 공지 · 03:17</div>
  이 페이지는 추천 서비스가 아닙니다.<br>
  폐쇄된 자료실에서 회수한 기록을 재생합니다. 선택에 따라 기록의 내용과 발견되는 작품이 달라집니다.
</div>
""", unsafe_allow_html=True)

# Each ending is tied to a genre pool from the existing user's webtoon catalog.
# Narrative branches change the eligible genre pool and scene text.
story_paths = {
    "terminal": {
        "title": "꺼진 모니터",
        "scene": "자료실 구석의 모니터가 혼자 켜진다. 화면에는 존재하지 않는 파일 번호가 떠 있다.",
        "dialogue": "모니터: \"기록을 열람하시겠습니까? 이미 한 번 열람하셨습니다.\"",
        "choices": [
            ("파일을 강제로 연다", "force"),
            ("전원을 뽑는다", "unplug"),
        ],
    },
    "force": {
        "title": "파일 강제 열람",
        "scene": "화면에 검은 창이 여러 개 겹친다. 마지막 창 하나만 읽을 수 있다.",
        "dialogue": "알 수 없는 발신자: \"당신은 이야기 속에서 무엇을 찾습니까?\"",
        "choices": [
            ("현실을 벗어난 세계", "fantasy"),
            ("누군가의 감춰진 마음", "romance"),
        ],
    },
    "unplug": {
        "title": "전원 차단",
        "scene": "모니터는 꺼졌지만 프린터가 움직인다. 종이에는 짧은 문장이 찍혀 있다.",
        "dialogue": "인쇄된 문장: \"뒤돌아보지 말 것. 특히 소리가 들려도.\"",
        "choices": [
            ("프린터 속 종이를 읽는다", "thriller"),
            ("자료실 출구를 찾는다", "action"),
        ],
    },
    "fantasy": {
        "title": "분류 오류: 세계",
        "scene": "파일 안에는 지도에도 없는 장소와, 현실에는 존재하지 않는 규칙이 적혀 있다.",
        "dialogue": "기록 담당자: \"이 세계의 규칙을 믿으시겠습니까?\"",
        "choices": [
            ("규칙을 믿고 들어간다", "ending_fantasy"),
            ("규칙을 의심하고 조사한다", "ending_drama"),
        ],
    },
    "romance": {
        "title": "발신인 없는 편지",
        "scene": "오래된 봉투가 열린다. 편지에는 이름이 지워진 채 문장 하나만 남아 있다.",
        "dialogue": "편지: \"끝났다고 생각한 순간부터 시작되는 마음도 있다.\"",
        "choices": [
            ("편지를 보관한다", "ending_romance"),
            ("뒷면의 낙서를 확인한다", "ending_bl"),
        ],
    },
    "thriller": {
        "title": "출력된 경고문",
        "scene": "프린터는 같은 문장을 세 번 출력한다. 세 번째 종이에는 새로운 글자가 나타난다.",
        "dialogue": "경고문: \"이 사건의 기록자는 아직 퇴근하지 않았다.\"",
        "choices": [
            ("사건 기록을 조사한다", "ending_thriller"),
            ("문을 열고 복도로 나간다", "ending_action"),
        ],
    },
    "action": {
        "title": "잠긴 출구",
        "scene": "출구의 자물쇠에는 숫자 대신 오래된 사건 번호가 새겨져 있다.",
        "dialogue": "스피커: \"문을 열려면 물러서지 않는 이야기를 선택하십시오.\"",
        "choices": [
            ("정면으로 돌파한다", "ending_action"),
            ("숨겨진 통로를 찾는다", "ending_fantasy"),
        ],
    },
}

endings = {
    "ending_fantasy": ("판타지", "세계의 바깥", "현실의 규칙을 벗어난 기록이 발견되었습니다."),
    "ending_romance": ("로맨스", "편지의 수신인", "감정과 관계를 기록한 문서가 발견되었습니다."),
    "ending_bl": ("BL", "지워진 이름", "관계의 이면을 기록한 문서가 발견되었습니다."),
    "ending_thriller": ("스릴러", "사건 보고서", "수상한 사건의 기록이 발견되었습니다."),
    "ending_action": ("액션", "잠긴 문 너머", "대결과 돌파의 기록이 발견되었습니다."),
    "ending_drama": ("드라마", "남겨진 기록", "인물의 선택과 성장을 기록한 문서가 발견되었습니다."),
}

if "story_node" not in st.session_state:
    st.session_state.story_node = "terminal"
if "story_history" not in st.session_state:
    st.session_state.story_history = []
if "story_ending_item" not in st.session_state:
    st.session_state.story_ending_item = None
if "story_ending_genre" not in st.session_state:
    st.session_state.story_ending_genre = None

def restart_story():
    st.session_state.story_node = "terminal"
    st.session_state.story_history = []
    st.session_state.story_ending_item = None
    st.session_state.story_ending_genre = None

node = st.session_state.story_node

# Progress strip
st.markdown(
    f'<span class="story-status">SESSION 09</span>'
    f'<span class="story-status">NODE: {node.upper()}</span>'
    f'<span class="story-status">LOGS: {len(st.session_state.story_history):02d}</span>',
    unsafe_allow_html=True
)

if node in story_paths:
    current = story_paths[node]
    st.markdown(f"""
    <div class="story-screen">
      <div class="story-kicker">UNKNOWN SYSTEM / {current["title"].upper()}</div>
      <div class="story-line">▸ {current["scene"]}</div>
      <div class="story-dialogue">{current["dialogue"]}</div>
      <div class="story-warning">[ 입력을 기다리는 중... ]</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="story-choice-label">▼ 다음 행동을 선택하십시오</div>', unsafe_allow_html=True)
    for index, (label, next_node) in enumerate(current["choices"]):
        if st.button(f"▸ {label}", key=f"story_{node}_{index}", use_container_width=True):
            st.session_state.story_history.append({
                "scene": current["title"],
                "choice": label,
            })
            st.session_state.story_node = next_node
            if next_node in endings:
                genre_name, _, _ = endings[next_node]
                candidates = webtoon_data.get(genre_name, [])
                if candidates:
                    st.session_state.story_ending_item = random.choice(candidates)
                    st.session_state.story_ending_genre = genre_name
                else:
                    all_candidates = [
                        (genre, item)
                        for genre, items in webtoon_data.items()
                        for item in items
                    ]
                    selected_genre, selected_item = random.choice(all_candidates)
                    st.session_state.story_ending_item = selected_item
                    st.session_state.story_ending_genre = selected_genre
            st.rerun()

else:
    genre_name, ending_title, ending_text = endings[node]
    item = st.session_state.story_ending_item
    st.markdown(f"""
    <div class="story-screen">
      <div class="story-kicker">END OF FILE / {ending_title.upper()}</div>
      <div class="story-line">{ending_text}</div>
      <div class="story-dialogue">시스템: \"기록을 복구했습니다. 아래 자료는 조사 결과에 따라 분류되었습니다.\"</div>
      <div class="story-warning">[ 열람 가능한 기록이 발견되었습니다 ]</div>
    </div>
    """, unsafe_allow_html=True)

    if item:
        st.markdown(f"""
        <div class="story-result">
          <small>RECOVERED WEBTOON · {st.session_state.story_ending_genre}</small>
          <h2>{item["title"]}</h2>
          <p>{item["description"]}</p>
        </div>
        """, unsafe_allow_html=True)
        link = webtoon_links.get(item["title"])
        if link:
            st.link_button("기록 원본 열람 ↗", link, use_container_width=True)
        else:
            st.info("이 작품의 공식 링크는 아직 등록되지 않았어요.")

    st.markdown('<div class="story-choice-label">조사 기록</div>', unsafe_allow_html=True)
    for entry in st.session_state.story_history:
        st.markdown(f"- **{entry['scene']}** — {entry['choice']}")

    left, right = st.columns(2)
    with left:
        if st.button("같은 결말에서 다른 작품 발견", use_container_width=True):
            candidates = webtoon_data.get(st.session_state.story_ending_genre, [])
            if candidates:
                st.session_state.story_ending_item = random.choice(candidates)
            st.rerun()
    with right:
        if st.button("처음부터 다시 조사", use_container_width=True):
            restart_story()
            st.rerun()

st.markdown(
    '<div class="footer-note">WEBTOON ARCHIVE · UNOFFICIAL PAPER · DO NOT TRUST EVERY FILE</div>',
    unsafe_allow_html=True
)
