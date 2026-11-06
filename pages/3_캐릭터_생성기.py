
import streamlit as st
import random
import html
import io
import streamlit.components.v1 as components

from pathlib import Path
from PIL import Image


st.set_page_config(
    page_title="CHARACTER FACTORY",
    page_icon="🧪",
    layout="wide"
)


# ── IMAGE PART SETTINGS ──

BASE_DIR = Path(__file__).parent
ASSET_DIR = BASE_DIR / "assets"

# 앞쪽에서 뒤쪽 순서
PART_ORDER = [
    "item",
    "decoration",
    "expression",
    "clothes",
    "front_hair",
    "body_eyes",
    "back_hair",
    "skin"
]

# 실제 이미지 합성 순서: 뒤쪽부터 앞쪽으로
COMPOSITE_ORDER = list(reversed(PART_ORDER))

PART_NAMES = {
    "item": "아이템",
    "decoration": "장식",
    "expression": "표정",
    "clothes": "의상",
    "front_hair": "앞머리",
    "body_eyes": "눈 & 몸 전체",
    "back_hair": "뒷머리",
    "skin": "피부색"
}


# ── COLOR KEYWORDS ──

COLOR_KEYWORDS = {
    "black": ["검정", "검은색", "검은", "블랙", "black"],
    "white": ["흰색", "하양", "화이트", "white"],
    "gray": ["회색", "그레이", "실버", "gray", "grey"],
    "brown": ["갈색", "브라운", "brown"],
    "red": ["빨강", "빨간색", "레드", "red"],
    "orange": ["주황", "오렌지", "orange"],
    "yellow": ["노랑", "노란색", "금색", "골드", "yellow"],
    "green": ["초록", "녹색", "그린", "green"],
    "cyan": ["하늘색", "민트", "청록", "cyan", "mint"],
    "blue": ["파랑", "파란색", "블루", "blue"],
    "purple": ["보라", "퍼플", "purple", "violet"],
    "pink": ["분홍", "핑크", "pink"]
}


def get_color_group(color):
    color = color.strip().lower()

    for group, words in COLOR_KEYWORDS.items():
        if any(word in color for word in words):
            return group

    return None


def filename_has_color(filename, color_group):
    """파일 이름에 색상 표시가 있는지 확인"""

    if not color_group:
        return True

    name = Path(filename).stem.lower()

    keywords = COLOR_KEYWORDS.get(color_group, [])

    return any(word.lower() in name for word in keywords)


def filename_has_hair_length(filename, hair):
    """파일 이름에 긴 머리 또는 숏컷 표시가 있는지 확인"""

    name = Path(filename).stem.lower()

    if hair == "긴 머리":
        keywords = [
            "긴머리", "긴_머리", "long", "longhair",
            "long_hair"
        ]
    else:
        keywords = [
            "숏컷", "짧은머리", "short", "shorthair",
            "short_hair"
        ]

    return any(word in name for word in keywords)


# ── LOAD PART IMAGES ──

def get_part_files(category):

    folder = ASSET_DIR / category

    if not folder.exists():
        return []

    return sorted(
        folder.glob("*.png")
    )


# ── SELECT RANDOM PART ──

def select_random_part(category, color, hair):

    files = get_part_files(category)

    if not files:
        return None

    candidates = list(files)

    # 색상 선택 적용
    color_group = get_color_group(color)

    color_categories = [
        "item",
        "decoration",
        "clothes",
        "front_hair",
        "back_hair"
    ]

    if category in color_categories and color_group:

        matching = [
            path for path in candidates
            if filename_has_color(path.name, color_group)
        ]

        if matching:
            candidates = matching

    # 머리 길이 선택 적용
    if category in ["front_hair", "back_hair"]:

        matching = [
            path for path in candidates
            if filename_has_hair_length(path.name, hair)
        ]

        if matching:
            candidates = matching

    return random.choice(candidates)


# ── COMBINE CHARACTER IMAGES ──

def combine_character(parts):

    character = None

    for category in COMPOSITE_ORDER:

        path = parts.get(category)

        if path is None:
            continue

        with Image.open(path) as source:
            layer = source.convert("RGBA")

        if character is None:

            character = Image.new(
                "RGBA",
                layer.size,
                (0, 0, 0, 0)
            )

        # 모든 파츠는 동일한 캔버스 크기를 사용하는 것을 권장
        if layer.size != character.size:

            layer = layer.resize(
                character.size,
                Image.Resampling.LANCZOS
            )

        character = Image.alpha_composite(
            character,
            layer
        )

    return character


# ── GUILD / WARDROBE STYLE ──

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=Gowun+Batang:wght@400;700&display=swap');

.stApp {
    background: #17130f;
    color: #f4ead2;
    font-family: 'Gowun Batang', serif;
}

.block-container {
    max-width: 1000px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* 길드 헤더 */
.guild-header {
    background: linear-gradient(180deg, #4d3319, #2b1d0f);
    border: 4px solid #c79b49;
    box-shadow: 0 0 25px rgba(199,155,73,.3);
    padding: 32px;
    text-align: center;
    margin-bottom: 28px;
}

.guild-mini {
    color: #d8c18a;
    letter-spacing: 3px;
    font-size: 12px;
    line-height: 2;
}

.guild-title {
    font-family: 'Cinzel', serif;
    color: #f7d36c;
    font-size: clamp(30px, 5vw, 52px);
    text-shadow: 0 0 8px rgba(255,220,120,.35);
    margin: 16px 0;
}

.guild-sub {
    color: #e9d7b0;
    font-size: 14px;
}

/* 양피지 */
.parchment {
    background: #efe2bf;
    color: #2a1a10;
    border: 3px solid #b88b3f;
    box-shadow: 6px 6px 0 #46301a;
    padding: 20px;
    margin: 18px 0;
}

.quest-tag {
    display: inline-block;
    background: #8f2e25;
    color: #fff6dd;
    padding: 6px 10px;
    font-size: 12px;
    letter-spacing: 2px;
}

/* 섹션 제목 */
.section-label {
    font-family: 'Cinzel', serif;
    color: #f3c86b;
    font-size: 18px;
    border-bottom: 2px solid #8b6a34;
    padding-bottom: 8px;
    margin: 30px 0 18px;
}

/* 입력창 */
.stTextInput label,
.stSelectbox label {
    color: #e8c875 !important;
    font-weight: bold;
}

div[data-baseweb="select"] > div,
.stTextInput input {
    background: #2b2219;
    color: white;
    border: 1px solid #c79b49;
    border-radius: 4px;
}

/* 버튼 */
div.stButton > button {
    background: linear-gradient(180deg, #c79b49, #8d5d1f);
    color: #24170d;
    border: 2px solid #f6dd9c;
    font-weight: bold;
    border-radius: 4px;
    min-height: 48px;
    box-shadow: 3px 3px 0 #120d09;
}

div.stButton > button:hover {
    background: linear-gradient(180deg, #e2bb61, #a46b22);
    color: #24170d;
    border-color: white;
}

/* 장비 보관함 */
.wardrobe {
    background: linear-gradient(180deg, #3a2818, #24170d);
    border: 3px solid #7b5226;
    box-shadow: 6px 6px 0 #120d09;
    padding: 20px;
    min-height: 230px;
}

.wardrobe h4 {
    font-family: 'Cinzel', serif;
    border-bottom: 1px solid #a47a3e;
    padding-bottom: 12px;
}

.wardrobe p {
    color: #e9d7b0;
    font-size: 14px;
}

/* 슬라임 */
.slime {
    background: #24452f;
    border-left: 5px solid #66ff88;
    padding: 14px;
    margin-top: 18px;
    color: #d7ffe1;
    font-size: 13px;
    line-height: 1.8;
}

/* 결과 카드 */
.result-card {
    background: linear-gradient(180deg, #342414, #1d140d);
    border: 3px solid #d6ab59;
    box-shadow: 0 0 18px rgba(214,171,89,.2);
    padding: 24px;
    margin: 16px 0 25px;
    overflow-wrap: anywhere;
}

.result-banner {
    display: inline-block;
    background: #8f2e25;
    color: #fff5dd;
    padding: 7px 12px;
    letter-spacing: 2px;
    font-size: 12px;
}

.character-name {
    font-family: 'Cinzel', serif;
    color: #ffd774;
    font-size: 34px;
    margin: 14px 0;
}

.character-job {
    color: #bde3ff;
    font-size: 18px;
    margin-bottom: 16px;
}

.stat-line {
    border-top: 1px dashed #8a6c44;
    padding: 11px 0;
    color: #f4ead2;
}

.stat-label {
    color: #d9b86f;
    font-weight: bold;
}

.rarity {
    color: #ffd774;
    font-size: 20px;
    font-weight: bold;
    margin-top: 8px;
}

/* 공포 게임 안내 */
.game-heading {
    background: #170b0b;
    color: #e9caca;
    border: 2px solid #8f2e25;
    padding: 20px;
    margin: 20px 0;
    text-align: center;
    line-height: 2;
}

/* 하단 */
.footer-note {
    text-align: center;
    color: #b59b72;
    margin-top: 34px;
    font-size: 12px;
    line-height: 2.2;
}

div[data-testid="stCaptionContainer"] {
    color: #b59b72;
}
</style>
""", unsafe_allow_html=True)


# ── HEADER ──

st.markdown("""
<div class="guild-header">
<div class="guild-mini">KINGDOM ADVENTURERS GUILD · REGISTRATION HALL</div>
<div class="guild-title">CHARACTER FACTORY</div>
<div class="guild-sub">모험가 등록소에 오신 것을 환영합니다.</div>
<div class="guild-mini">EST. 199X · THE WORLD OF ADVENTURE</div>
</div>

<div class="parchment">
<span class="quest-tag">의뢰서 #001</span>
<h3>⚔ 나만의 모험가를 소환하라!</h3>
<p>길드에 방문한 모험가 여러분을 환영합니다.<br>
원하는 외형과 세계관을 선택하면 새로운 모험가가 배정됩니다.</p>
<p>★ CHARACTER REGISTRATION · LIMITED EDITION ★</p>
</div>
""", unsafe_allow_html=True)


# ── CHARACTER DATA ──

names = [
    "유하진", "강민", "서윤", "하린", "도현",
    "윤시온", "백이안", "차유현", "한서우", "정이든",
    "서해온", "강이현", "문시율", "류하온", "진유안"
]

jobs_by_genre = {
    "판타지": ["마법사", "기사", "마왕의 후계자", "연금술사", "용병"],
    "로맨스": ["대학생", "작가", "아이돌 연습생", "카페 직원", "배우"],
    "액션": ["헌터", "격투가", "경찰", "정보원", "용병"],
    "스릴러": ["탐정", "기자", "형사", "연구원", "목격자"]
}


# ── PLAYER CUSTOMIZATION ──

st.markdown(
    '<div class="section-label">01 / ADVENTURER CUSTOMIZATION</div>',
    unsafe_allow_html=True
)

left, right = st.columns(2)

with left:

    color = st.text_input(
        "▣ 좋아하는 색",
        placeholder="예: 네온 핑크, 검정, 하늘색",
        key="character_color"
    )

    hair = st.selectbox(
        "▣ 선호하는 머리 길이",
        ["긴 머리", "숏컷"],
        key="character_hair"
    )

with right:

    genre = st.selectbox(
        "▣ 세계관 / 장르",
        ["판타지", "로맨스", "액션", "스릴러"],
        key="character_genre"
    )

    st.markdown("""
    <div class="wardrobe">
    <h4 style="color:#f7d36c;">🧰 장비 보관함</h4>
    <p>🗡 기본 장비 지급 준비 완료</p>
    <p>🎒 모험가 등록증 인쇄 대기</p>
    <p>✨ 마법진 충전 완료</p>
    <div class="slime">
    💚 슬라임 : "어서 와! 어떤 모험가를 만나고 싶어?"
    <br>
    "등록서를 작성하면 내가 데려올게!"
    </div>
    </div>
    """, unsafe_allow_html=True)


# ── SECRET HORROR GAME ──

dark_color_words = [
    "검정",
    "검은색",
    "검은",
    "블랙",
    "black"
]

is_black = any(
    word in color.strip().lower()
    for word in dark_color_words
)

launch_horror = (
    is_black
    and hair == "긴 머리"
    and genre == "스릴러"
)

if launch_horror:

    st.markdown("""
    <div class="game-heading">
        <b>⚠ 비정상적인 마력 반응 감지</b>
        <br>
        등록소의 공간이 뒤틀리고 있습니다.
        <br>
        화면 아래의 문을 통과하세요.
    </div>
    """, unsafe_allow_html=True)

    game_path = BASE_DIR / "the_last_hallway.html"

    if game_path.exists():

        game_html = game_path.read_text(
            encoding="utf-8"
        )

        components.html(
            game_html,
            height=760,
            scrolling=False
        )

    else:

        st.error(
            "게임 파일을 찾을 수 없어! "
            "the_last_hallway.html 파일을 이 파이썬 파일과 같은 폴더에 넣어 줘."
        )

    st.stop()


# ── CHARACTER GENERATOR ──

def generate_character(color, hair, genre):

    selected_parts = {}

    # 8개 파츠 각각 랜덤 선택
    for category in PART_ORDER:

        selected_parts[category] = select_random_part(
            category,
            color,
            hair
        )

    # 이미지 합성
    character_image = combine_character(
        selected_parts
    )

    # PNG 데이터 생성
    image_bytes = None

    if character_image is not None:

        buffer = io.BytesIO()

        character_image.save(
            buffer,
            format="PNG"
        )

        image_bytes = buffer.getvalue()

    return {
        "name": random.choice(names),
        "gender": random.choice(["남성", "여성"]),
        "job": random.choice(jobs_by_genre[genre]),
        "hair": hair,
        "genre": genre,
        "color": color.strip() if color.strip() else "미지정",
        "rarity": random.choices(
            ["F급", "C급", "B급", "A급", "S급", "SS급"],
            weights=[35, 25, 18, 12, 7, 3],
            k=1
        )[0],
        "selected_parts": selected_parts,
        "character_image": image_bytes
    }


# ── GENERATE ──

if st.button(
    "⚔ 모험가 소환하기 / SUMMON CHARACTER",
    use_container_width=True
):

    st.session_state["character_result"] = generate_character(
        color,
        hair,
        genre
    )


# ── RESULT ──

result = st.session_state.get("character_result")

required_keys = [
    "name", "gender", "job", "hair",
    "genre", "color", "rarity"
]

# 이전 버전 데이터 호환
if result and not all(
    key in result for key in required_keys
):

    del st.session_state["character_result"]
    result = None


if result:

    st.markdown(
        '<div class="section-label">02 / ADVENTURER REGISTERED</div>',
        unsafe_allow_html=True
    )

    # ── CHARACTER IMAGE ──

    if result.get("character_image"):

        st.image(
            result["character_image"],
            caption="★ SUMMONED ADVENTURER ★",
            width=400
        )

        st.download_button(
            "⬇ 캐릭터 이미지 저장하기",
            data=result["character_image"],
            file_name="my_character.png",
            mime="image/png",
            use_container_width=True
        )

    else:

        st.warning(
            "캐릭터 이미지를 만들 수 없어! "
            "assets 폴더와 PNG 파일을 확인해 줘."
        )

    # ── CHARACTER INFORMATION ──

    st.markdown(f"""
    <div class="result-card">
    <span class="result-banner">★ ADVENTURER LICENSE ★</span>
    <div class="character-name">{html.escape(str(result["name"]))}</div>
    <div class="character-job">⚔ 직업 : {html.escape(str(result["job"]))}</div>
    <div class="stat-line"><span class="stat-label">GENDER //</span> {html.escape(str(result["gender"]))}</div>
    <div class="stat-line"><span class="stat-label">HAIR STYLE //</span> {html.escape(str(result["hair"]))}</div>
    <div class="stat-line"><span class="stat-label">WORLD //</span> {html.escape(str(result["genre"]))}</div>
    <div class="stat-line"><span class="stat-label">COLOR CODE //</span> {html.escape(str(result["color"]))}</div>
    <div class="stat-line"><span class="stat-label">RARITY //</span><div class="rarity">⭐ {html.escape(str(result["rarity"]))}</div></div>
    </div>
    """, unsafe_allow_html=True)

    # ── SELECTED PARTS ──

    with st.expander("이번 캐릭터에 사용된 파츠 확인"):

        for category in PART_ORDER:

            path = result["selected_parts"].get(category)

            if path:

                st.write(
                    f"**{PART_NAMES[category]}:** "
                    f"{Path(path).name}"
                )

            else:

                st.write(
                    f"**{PART_NAMES[category]}:** "
                    "이미지 없음"
                )

    st.markdown("""
    <div class="parchment">
    <span class="quest-tag">CHARACTER FILE</span>
    <h3>등록 완료!</h3>
    <p>새로운 모험가가 길드에 등록되었습니다.<br>
    이제 이 캐릭터의 이야기를 시작해 보세요!</p>
    </div>
    """, unsafe_allow_html=True)

    # ── RANDOMIZE ──

    if st.button(
        "↻ 다른 모험가 소환하기 / RANDOMIZE",
        use_container_width=True
    ):

        st.session_state["character_result"] = generate_character(
            color,
            hair,
            genre
        )

        st.rerun()


# ── FOOTER ──

st.markdown("""
<div class="footer-note">
✦ MAY YOUR JOURNEY BE FILLED WITH ADVENTURE ✦
<br>
CHARACTER FACTORY · KINGDOM GUILD
<br>
THANK YOU FOR VISITING!
</div>
""", unsafe_allow_html=True)
