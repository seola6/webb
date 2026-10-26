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
