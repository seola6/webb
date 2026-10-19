import streamlit as st

st.set_page_config(
    page_title="WEBTOON ARCHIVE",
    page_icon="📚",
    layout="wide"
)

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
    padding-top: 3rem;
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
    font-size: 58px;
    font-weight: bold;
    color: #29432f;
    margin: 25px 0 10px;
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
    font-size: 25px;
    font-weight: bold;
    border-bottom: 2px solid #526b49;
    padding-bottom: 10px;
    margin: 30px 0 20px;
}

.archive-card {
    background: #f7f3e4;
    border: 1px solid #a4b596;
    padding: 22px;
    min-height: 150px;
    box-shadow: 4px 4px 0 #cbd6bd;
}

.card-number {
    color: #718568;
    font-size: 12px;
    letter-spacing: 2px;
}

.card-title {
    font-size: 21px;
    font-weight: bold;
    margin: 15px 0;
    color: #29432f;
}

.card-description {
    font-size: 14px;
    line-height: 1.8;
    color: #596b50;
}

.stButton > button {
    background-color: #526b49;
    color: white;
    border-radius: 3px;
    border: 1px solid #29432f;
}

.stButton > button:hover {
    background-color: #718568;
    color: white;
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
</style>
""", unsafe_allow_html=True)

# 메인 포스터
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

# 소개
st.markdown("""
<div class="section-title">
    ▣ ARCHIVE GUIDE — 자료실 안내
</div>
<p style="line-height:2;">
장르별 웹툰을 탐색하고, 취향에 맞는 작품을 발견해 보세요.<br>
다양한 이야기와 작품을 모아 소개하는 작은 아카이브입니다.
</p>
""", unsafe_allow_html=True)

# 기능 카드
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="archive-card">
        <div class="card-number">FILE NO. 001</div>
        <div class="card-title">▣ 웹툰 추천</div>
        <div class="card-description">
            취향에 맞는 작품을 발견하고<br>
            새로운 이야기를 만나 보세요.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="archive-card">
        <div class="card-number">FILE NO. 002</div>
        <div class="card-title">▣ 요일별 랭킹</div>
        <div class="card-description">
            요일별 인기 작품과<br>
            웹툰 순위를 확인해 보세요.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="archive-card">
        <div class="card-number">FILE NO. 003</div>
        <div class="card-title">▣ 장르 아카이브</div>
        <div class="card-description">
            다양한 장르의 작품을<br>
            한곳에서 살펴보세요.
        </div>
    </div>
    """, unsafe_allow_html=True)

# 시스템 정보
st.markdown("""
<div class="section-title">
    ▣ ARCHIVE RECORD
</div>
""", unsafe_allow_html=True)

info1, info2, info3 = st.columns(3)

info1.metric("등록 장르", "06")
info2.metric("등록 작품", "30+")
info3.metric("추천 시스템", "ONLINE")

st.markdown("""
<div class="footer">
    WEBTOON ARCHIVE · COLLECT YOUR STORIES
</div>
""", unsafe_allow_html=True)
