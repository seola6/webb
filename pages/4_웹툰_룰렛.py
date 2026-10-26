
import time
import random
import streamlit as st

st.set_page_config(
    page_title="WEBTOON ROULETTE",
    page_icon="🎰",
    layout="wide"
)

# ── 웹툰 데이터 ──
webtoon_data = {
    '전체': [
        '별을 품은 소드마스터',
        '종말이 찾아왔다',
        '샤MONEY',
        '생존지상주의',
        '검술 명가의 네크로맨서',
        '대마법사 커리큘럼',
        '집구석 절대자',
        '전지적 독자 시점',
        '하울링',
        '그림으로 승부',
        '엄마를 만나러 가는 길',
        '전자오락수호대',
        '무한의 마법사',
        '블랙 헤이즈',
        'SSS급 죽어야 사는 헌터',
        '도굴왕: 엔드라인',
        '천재 궁수의 스트리밍',
        '만렙 플레이어의 100번째 회귀',
        '성자는 개뿔, 현대의학의 힘이다',
        '월스트리트 천재의 시한부 투자법',
        '백작가의 비밀스런 시녀님',
        '벙커의 낮',
        '세림의 철칙',
        '연상녀 클럽',
        '완벽한 선배의 Hide!',
        '해일주의보',
        '비공식 CC',
        '1인칭 혈육시점',
        '사랑이 끝나면 네가 끝난다',
        '인소의 법칙',
        '남고 소년',
        '시맨틱 에러(개정판)',
        '죽었는데 왜 집착하세요',
        '사신님과 3년 계약',
        '내 호수에 가둔 인어',
        '엄마가 계약결혼 했다',
        '이번 생은 가주가 되겠습니다',
        '사랑은 좀비를 찢고',
        '정글쥬스',
        '싸움배달',
        '레디액션',
        '은퇴한 킬러는 힐링하고 싶다',
        '악마에 입문했습니다! 이루마 군',
        '엔드와 세이브',
        '흡혈귀는 툭하면 죽는다',
        '44교시 생존수업',
        '쪽팔려 게임',
        '똑 닮은 딸',
        '제물 투표',
        '귀촌리',
        '모닥불 친구들',
        '유령의 노래',
    ],
    '판타지': [
        '별을 품은 소드마스터',
        '종말이 찾아왔다',
        '샤MONEY',
        '생존지상주의',
        '검술 명가의 네크로맨서',
        '대마법사 커리큘럼',
        '집구석 절대자',
        '전지적 독자 시점',
        '하울링',
        '그림으로 승부',
        '엄마를 만나러 가는 길',
        '전자오락수호대',
        '무한의 마법사',
        '블랙 헤이즈',
        'SSS급 죽어야 사는 헌터',
        '도굴왕: 엔드라인',
        '천재 궁수의 스트리밍',
        '만렙 플레이어의 100번째 회귀',
        '성자는 개뿔, 현대의학의 힘이다',
        '월스트리트 천재의 시한부 투자법',
    ],
    '로맨스': [
        '백작가의 비밀스런 시녀님',
        '벙커의 낮',
        '세림의 철칙',
        '연상녀 클럽',
        '완벽한 선배의 Hide!',
        '해일주의보',
        '비공식 CC',
        '1인칭 혈육시점',
        '사랑이 끝나면 네가 끝난다',
        '인소의 법칙',
        '남고 소년',
        '시맨틱 에러(개정판)',
    ],
    '로맨스 판타지': [
        '백작가의 비밀스런 시녀님',
        '죽었는데 왜 집착하세요',
        '사신님과 3년 계약',
        '내 호수에 가둔 인어',
        '엄마가 계약결혼 했다',
        '이번 생은 가주가 되겠습니다',
    ],
    '액션': [
        '사랑은 좀비를 찢고',
        '정글쥬스',
        '싸움배달',
        '레디액션',
        '은퇴한 킬러는 힐링하고 싶다',
        '악마에 입문했습니다! 이루마 군',
        '엔드와 세이브',
        '흡혈귀는 툭하면 죽는다',
    ],
    '스릴러': [
        '44교시 생존수업',
        '쪽팔려 게임',
        '똑 닮은 딸',
        '제물 투표',
        '귀촌리',
        '모닥불 친구들',
        '유령의 노래',
    ],
    'BL': [
        '남고 소년',
        '시맨틱 에러(개정판)',
    ]
}

# ── 작품 페이지 링크: 사용자가 제공한 주소만 사용 ──
webtoon_links = {
    '별을 품은 소드마스터': 'https://comic.naver.com/webtoon/list?titleId=816809',
    '종말이 찾아왔다': 'https://comic.naver.com/webtoon/list?titleId=838002',
    '샤MONEY': 'https://comic.naver.com/webtoon/list?titleId=840014',
    '생존지상주의': 'https://comic.naver.com/webtoon/list?titleId=853709',
    '검술 명가의 네크로맨서': 'https://comic.naver.com/webtoon/list?titleId=850499',
    '대마법사 커리큘럼': 'https://comic.naver.com/webtoon/list?titleId=844951',
    '집구석 절대자': 'https://comic.naver.com/webtoon/list?titleId=834351',
    '전지적 독자 시점': 'https://comic.naver.com/webtoon/list?titleId=747269',
    '하울링': 'https://comic.naver.com/webtoon/list?titleId=854794',
    '그림으로 승부': 'https://comic.naver.com/webtoon/list?titleId=853095',
    '엄마를 만나러 가는 길': 'https://comic.naver.com/webtoon/list?titleId=834369',
    '전자오락수호대': 'https://comic.naver.com/webtoon/list?titleId=637931',
    '무한의 마법사': 'https://page.kakao.com/content/60910969/',
    '블랙 헤이즈': 'https://page.kakao.com/content/65986358/',
    'SSS급 죽어야 사는 헌터': 'https://page.kakao.com/content/56243215/',
    '도굴왕: 엔드라인': 'https://page.kakao.com/content/69500409/',
    '천재 궁수의 스트리밍': 'https://page.kakao.com/content/64007563/',
    '만렙 플레이어의 100번째 회귀': 'https://page.kakao.com/content/62916616/',
    '성자는 개뿔, 현대의학의 힘이다': 'https://page.kakao.com/content/59422125/',
    '월스트리트 천재의 시한부 투자법': 'https://comic.naver.com/webtoon/list?titleId=854407',
    '백작가의 비밀스런 시녀님': 'https://comic.naver.com/webtoon/list?titleId=830106',
    '벙커의 낮': 'https://comic.naver.com/webtoon/list?titleId=846643',
    '세림의 철칙': 'https://comic.naver.com/webtoon/list?titleId=852516',
    '연상녀 클럽': 'https://comic.naver.com/webtoon/list?titleId=851476',
    '완벽한 선배의 Hide!': 'https://comic.naver.com/webtoon/list?titleId=849742',
    '해일주의보': 'https://comic.naver.com/webtoon/list?titleId=853833',
    '비공식 CC': 'https://comic.naver.com/webtoon/list?titleId=851431',
    '1인칭 혈육시점': 'https://comic.naver.com/webtoon/list?titleId=850236',
    '사랑이 끝나면 네가 끝난다': 'https://comic.naver.com/webtoon/list?titleId=849864',
    '인소의 법칙': 'https://page.kakao.com/content/52610652/',
    '남고 소년': 'https://www.lezhin.com/ko/comic/highschoolboy',
    '시맨틱 에러(개정판)': 'https://ridibooks.com/books/3392000097?_s=search&_q=%EC%8B%9C%EB%A7%A8%ED%8B%B1+%EC%97%90%EB%9F%AC&_rdt_sid=SearchBookListWithTab&_rdt_idx=2',
    '죽었는데 왜 집착하세요': 'https://comic.naver.com/webtoon/list?titleId=826529',
    '사신님과 3년 계약': 'https://comic.naver.com/webtoon/list?titleId=847850',
    '내 호수에 가둔 인어': 'https://comic.naver.com/webtoon/list?titleId=834391',
    '엄마가 계약결혼 했다': 'https://page.kakao.com/content/59882406/',
    '이번 생은 가주가 되겠습니다': 'https://page.kakao.com/content/56566288/',
    '사랑은 좀비를 찢고': 'https://comic.naver.com/webtoon/list?titleId=854591',
    '정글쥬스': 'https://comic.naver.com/webtoon/list?titleId=762279',
    '싸움배달': 'https://comic.naver.com/webtoon/list?titleId=850079',
    '레디액션': 'https://comic.naver.com/webtoon/list?titleId=855128',
    '은퇴한 킬러는 힐링하고 싶다': 'https://page.kakao.com/content/70268713/',
    '악마에 입문했습니다! 이루마 군': 'https://page.kakao.com/content/52542095/',
    '엔드와 세이브': 'https://page.kakao.com/content/55281534/',
    '흡혈귀는 툭하면 죽는다': 'https://page.kakao.com/content/61388860/',
    '44교시 생존수업': 'https://comic.naver.com/webtoon/list?titleId=836848',
    '쪽팔려 게임': 'https://comic.naver.com/webtoon/list?titleId=847135',
    '똑 닮은 딸': 'https://comic.naver.com/webtoon/list?titleId=774866',
    '제물 투표': 'https\\://comic.naver.com/webtoon/list?titleId=850211',
    '귀촌리': 'https\\://comic.naver.com/webtoon/list?titleId=822573',
    '모닥불 친구들': 'https\\://comic.naver.com/webtoon/list?titleId=837439',
    '유령의 노래': 'https\\://comic.naver.com/webtoon/list?titleId=823239',
}

# ── 디자인 ──
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Nanum+Gothic+Coding:wght@400;700&display=swap');

.stApp {
    background: radial-gradient(
        ellipse at top, #30204a 0%, #11101b 48%, #08090e 100%
    );
    color: #f8f0dc;
}

.block-container {
    max-width: 1000px;
    padding-top: 2rem;
}

h1, h2, h3 {
    font-family: 'Black Han Sans', sans-serif !important;
}

.roulette-banner {
    border: 2px solid #ff4fd8;
    border-radius: 8px;
    padding: 25px 18px;
    text-align: center;
    background: linear-gradient(135deg, #271633, #15192e);
    box-shadow: 0 0 18px #ff4fd844, inset 0 0 18px #6af7ff15;
    margin-bottom: 20px;
}

.roulette-title {
    color: #ff70df;
    font-size: clamp(30px, 5vw, 48px);
    text-shadow: 3px 3px #57234d, 0 0 15px #ff4fd8;
    letter-spacing: 2px;
}

.roulette-subtitle {
    color: #9efaff;
    font-family: 'Nanum Gothic Coding', monospace;
    font-size: 13px;
    letter-spacing: 2px;
}

.roulette-screen {
    position: relative;
    overflow: hidden;
    background: linear-gradient(135deg, #25152f, #111827);
    border: 3px solid #ff4fd8;
    border-radius: 12px;
    padding: 38px 12px;
    text-align: center;
    box-shadow: 0 0 22px #ff4fd855;
    margin: 18px 0;
}

.roulette-status {
    color: #9efaff;
    font-family: 'Nanum Gothic Coding', monospace;
    font-size: 12px;
    letter-spacing: 3px;
    line-height: 1.8;
}

.roulette-name {
    position: relative;
    z-index: 2;
    color: #fff0fb;
    font-size: clamp(25px, 5vw, 40px);
    font-weight: bold;
    margin: 24px 0;
    overflow-wrap: anywhere;
    text-shadow: 0 0 14px #ff4fd8;
}

.roulette-deco {
    color: #ffcf5c;
    font-size: 25px;
    letter-spacing: 8px;
}

/* 당첨 화면 팡! */
.jackpot-screen {
    animation: jackpot-pop 0.65s cubic-bezier(.18,.89,.32,1.35) both;
    border-color: #ffe17a;
    box-shadow:
        0 0 15px #ff4fd8,
        0 0 35px #ffcf5c,
        inset 0 0 30px #ff4fd833;
}

.jackpot-screen .roulette-name {
    animation: title-glow 1s ease-in-out infinite alternate;
}

/* 중앙에서 퍼지는 빛 */
.burst-light {
    position: absolute;
    left: 50%;
    top: 48%;
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: #fff8c9;
    box-shadow:
        0 0 18px 8px #ff4fd8,
        0 0 35px 15px #9efaff;
    pointer-events: none;
    animation: light-burst 0.8s ease-out forwards;
}

/* 터지는 색종이 */
.confetti {
    position: absolute;
    left: 50%;
    top: 48%;
    width: 9px;
    height: 15px;
    border-radius: 2px;
    pointer-events: none;
    animation: confetti-burst 1s ease-out forwards;
}

.confetti:nth-child(2) { --x: -130px; --y: -85px; background: #9efaff; }
.confetti:nth-child(3) { --x: 125px; --y: -90px; background: #ffcf5c; }
.confetti:nth-child(4) { --x: -155px; --y: 20px; background: #b9ff9e; }
.confetti:nth-child(5) { --x: 150px; --y: 25px; background: #ff70df; }
.confetti:nth-child(6) { --x: -85px; --y: 100px; background: #ffcf5c; }
.confetti:nth-child(7) { --x: 90px; --y: 100px; background: #9efaff; }
.confetti:nth-child(8) { --x: 0px; --y: -125px; background: #ffffff; }
.confetti:nth-child(9) { --x: 0px; --y: 120px; background: #ff70df; }

@keyframes jackpot-pop {
    0% {
        transform: scale(0.55);
        opacity: 0;
    }
    65% {
        transform: scale(1.07);
        opacity: 1;
    }
    100% {
        transform: scale(1);
        opacity: 1;
    }
}

@keyframes light-burst {
    0% {
        transform: translate(-50%, -50%) scale(0);
        opacity: 1;
    }
    45% {
        transform: translate(-50%, -50%) scale(5);
        opacity: .8;
    }
    100% {
        transform: translate(-50%, -50%) scale(9);
        opacity: 0;
    }
}

@keyframes confetti-burst {
    0% {
        transform: translate(-50%, -50%) rotate(0deg) scale(0);
        opacity: 1;
    }
    100% {
        transform: translate(
            calc(-50% + var(--x)),
            calc(-50% + var(--y))
        ) rotate(540deg) scale(1);
        opacity: 0;
    }
}

@keyframes title-glow {
    from {
        text-shadow: 0 0 8px #ff4fd8;
    }
    to {
        text-shadow: 0 0 24px #ff4fd8, 0 0 38px #9efaff;
    }
}

/* 결과 티켓 */
.ticket {
    background: #f4e7c8;
    color: #251b2c;
    border: 3px dashed #a74787;
    border-radius: 6px;
    padding: 28px 20px;
    text-align: center;
    margin: 15px 0;
    box-shadow: 6px 6px 0 #ff4fd833;
}

.ticket-label {
    font-family: 'Nanum Gothic Coding', monospace;
    font-size: 12px;
    color: #a74787;
    letter-spacing: 3px;
}

.ticket-title {
    font-family: 'Black Han Sans', sans-serif;
    font-size: clamp(25px, 4vw, 38px);
    margin: 14px 0;
    overflow-wrap: anywhere;
}

.ticket-bottom {
    border-top: 1px dashed #a74787;
    padding-top: 12px;
    font-size: 12px;
    color: #59435b;
}

.stButton > button {
    background: linear-gradient(90deg, #ff4fd8, #8d73ff) !important;
    color: white !important;
    border: 1px solid #ffb4ef !important;
    border-radius: 5px !important;
    font-family: 'Black Han Sans', sans-serif !important;
    font-size: 19px !important;
    min-height: 52px;
    box-shadow: 0 0 12px #ff4fd844;
    transition: 0.2s;
}

.stButton > button:hover {
    border-color: #9efaff !important;
    box-shadow: 0 0 22px #ff4fd899;
    transform: translateY(-2px);
}

div[data-baseweb="select"] > div {
    background-color: #201c30;
    border-color: #8d73ff;
    color: #fff;
}

div[data-testid="stMarkdownContainer"] p {
    line-height: 1.7;
}
</style>
""", unsafe_allow_html=True)

# ── 헤더 ──
st.markdown("""
<div class="roulette-banner">
    <div class="roulette-subtitle">
        ★ WEBTOON ARCHIVE · SPECIAL MACHINE ★
    </div>
    <div class="roulette-title">🎰 WEBTOON ROULETTE</div>
    <div class="roulette-subtitle">오늘 당신이 읽게 될 작품은?</div>
</div>
""", unsafe_allow_html=True)

st.markdown("##### ▣ 오늘의 운명을 뽑아 보세요.")

st.write(
    "무엇을 읽을지 고민될 때 사용하는 웹툰 추첨기입니다. "
    "장르를 선택하고 버튼을 눌러 보세요!"
)

# ── 장르 선택 ──
genre = st.selectbox(
    "▣ 추첨할 장르",
    list(webtoon_data.keys())
)

# ── 세션 상태 초기화 ──
if "roulette_result" not in st.session_state:
    st.session_state.roulette_result = None

if "roulette_previous" not in st.session_state:
    st.session_state.roulette_previous = None

if "roulette_genre" not in st.session_state:
    st.session_state.roulette_genre = genre

# 장르 변경 시 결과 초기화
if st.session_state.roulette_genre != genre:
    st.session_state.roulette_result = None
    st.session_state.roulette_previous = None
    st.session_state.roulette_genre = genre

st.markdown("---")

# ── 룰렛 화면 ──
roulette_display = st.empty()
status_display = st.empty()

if st.button("🎰  룰렛 돌리기!", use_container_width=True):
    candidates = webtoon_data[genre].copy()
    previous = st.session_state.roulette_previous

    # 직전 당첨작은 가능한 한 제외
    if previous in candidates and len(candidates) > 1:
        candidates.remove(previous)

    # 당첨작은 한 번만 결정하고 session_state에 저장
    result = random.choice(candidates)
    others = [title for title in webtoon_data[genre] if title != result]

    roulette_display.markdown("""
    <div class="roulette-screen">
        <div class="roulette-status">★ ARCHIVE MACHINE ★</div>
        <div class="roulette-deco">✦ ✧ ✦</div>
        <div class="roulette-name">READY...</div>
        <div class="roulette-status">DRAWING YOUR NEXT STORY</div>
    </div>
    """, unsafe_allow_html=True)
    time.sleep(0.25)

    delays = [0.06, 0.07, 0.08, 0.09, 0.10, 0.12, 0.14, 0.17, 0.20, 0.24, 0.29, 0.35, 0.42, 0.50]
    for delay in delays:
        title = random.choice(others) if others else result
        roulette_display.markdown(f"""
        <div class="roulette-screen">
            <div class="roulette-status">★ SPINNING ★</div>
            <div class="roulette-deco">✦ ✧ ✦</div>
            <div class="roulette-name">「 {title} 」</div>
            <div class="roulette-status">SEARCHING THE ARCHIVE...</div>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(delay)

    st.session_state.roulette_result = result
    st.session_state.roulette_previous = result
    st.session_state.roulette_genre = genre

    jackpot_html = f"""
    <div class="roulette-screen jackpot-screen">
        <div class="burst-light"></div>
        <div class="confetti"></div><div class="confetti"></div>
        <div class="confetti"></div><div class="confetti"></div>
        <div class="confetti"></div><div class="confetti"></div>
        <div class="confetti"></div><div class="confetti"></div>
        <div class="roulette-status">★ JACKPOT ★</div>
        <div class="roulette-deco">✦ ✨ ✦</div>
        <div class="roulette-name">「 {result} 」</div>
        <div class="roulette-status">YOUR NEXT WEBTOON HAS BEEN SELECTED!</div>
    </div>
    """
    roulette_display.markdown(jackpot_html, unsafe_allow_html=True)
    status_display.success("🎉 팡! 당첨! 오늘의 웹툰이 결정됐어!")

elif st.session_state.roulette_result:
    result = st.session_state.roulette_result
    result_genre = st.session_state.get("roulette_genre", genre)
    roulette_display.markdown(f"""
    <div class="roulette-screen jackpot-screen">
        <div class="roulette-status">★ YOUR NEXT WEBTOON ★</div>
        <div class="roulette-deco">✦ ✨ ✦</div>
        <div class="roulette-name">「 {result} 」</div>
        <div class="roulette-status">장르: {result_genre}</div>
    </div>
    """, unsafe_allow_html=True)
else:
    roulette_display.markdown("""
    <div class="roulette-screen">
        <div class="roulette-status">★ READY ★</div>
        <div class="roulette-deco">✦ ✧ ✦</div>
        <div class="roulette-name">운명의 버튼을 누르세요!</div>
        <div class="roulette-status">YOUR NEXT STORY IS WAITING</div>
    </div>
    """, unsafe_allow_html=True)

# ── 결과 티켓: 위쪽 룰렛과 같은 저장 결과를 사용 ──
if st.session_state.roulette_result:
    result = st.session_state.roulette_result
    result_genre = st.session_state.get("roulette_genre", genre)
    st.markdown(f"""
    <div class="ticket">
        <div class="ticket-label">★ YOUR NEXT WEBTOON ★</div>
        <div class="ticket-title">「 {result} 」</div>
        <div class="ticket-bottom">
            SELECTED FROM WEBTOON ARCHIVE · 장르: {result_genre}
        </div>
    </div>
    """, unsafe_allow_html=True)
    result_link = webtoon_links.get(result)
    if result_link:
        st.link_button("📖 작품 보러 가기 ↗", result_link, use_container_width=True)
    else:
        st.info("이 작품의 바로가기 주소는 아직 등록되지 않았어요. 작품 제목으로 검색해 주세요.")

    st.success("오늘의 작품이 선정되었습니다! 마음에 들지 않으면 한 번 더 돌려 보세요.")
else:
    st.markdown("""
    <div class="ticket">
        <div class="ticket-label">READY?</div>
        <div class="ticket-title">운명의 버튼을 누르세요!</div>
        <div class="ticket-bottom">YOUR NEXT STORY IS WAITING...</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.caption(
    "WEBTOON ARCHIVE © · 작품 링크는 사용자가 제공한 목록을 바탕으로 구성했습니다. "
    "실시간 인기 순위나 플랫폼 공식 목록이 아닙니다."
)
