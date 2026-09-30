import streamlit as st
import random

st.title("🎯 웹툰 추천")

webtoon_data = {
    "판타지": [
        {
            "title": "전지적 독자 시점",
            "description": "소설 속 세계가 현실이 된 후 살아남기 위한 이야기"
        },
        {
            "title": "화산귀환",
            "description": "전설의 검객이 환생해 몰락한 문파를 재건하는 무협 판타지"
        },
        {
            "title": "나 혼자만 레벨업",
            "description": "최약체 헌터가 특별한 능력을 얻어 성장하는 이야기"
        },
        {
            "title": "초인의 게임",
            "description": "초능력자들이 펼치는 생존과 경쟁의 이야기"
        },
        {
            "title": "철수를 구하시오",
            "description": "SF와 판타지 요소가 결합된 독특한 세계관의 작품"
        }
    ],

    "로맨스": [
        {
            "title": "작전명 순정",
            "description": "첫사랑과 우정을 그린 청춘 로맨스"
        },
        {
            "title": "세기말 풋사과 보습학원",
            "description": "1990년대를 배경으로 한 학원 로맨스"
        },
        {
            "title": "바른연애 길잡이",
            "description": "대학생들의 현실적인 연애 이야기를 다룬 작품"
        },
        {
            "title": "여신강림",
            "description": "메이크업으로 자신감을 찾은 여학생의 성장과 사랑 이야기"
        },
        {
            "title": "연애혁명",
            "description": "고등학생들의 사랑과 우정을 그린 학원 로맨스"
        }
    ],

    "액션": [
        {
            "title": "참교육",
            "description": "학교 폭력과 사회 문제를 해결하는 교육관들의 이야기"
        },
        {
            "title": "캐슬",
            "description": "복수를 위해 범죄 조직에 맞서는 남자의 액션 느와르"
        },
        {
            "title": "외모지상주의",
            "description": "두 개의 몸을 가지게 된 주인공의 성장과 격투 이야기"
        },
        {
            "title": "격기 3반",
            "description": "격투기를 중심으로 펼쳐지는 학원 액션물"
        },
        {
            "title": "약한영웅",
            "description": "약해 보이는 학생이 지능과 전략으로 싸워 나가는 이야기"
        }
    ],

    "스릴러": [
        {
            "title": "타인은 지옥이다",
            "description": "수상한 고시원 사람들 사이에서 벌어지는 심리 스릴러"
        },
        {
            "title": "스위트홈",
            "description": "사람들이 괴물로 변하는 세상에서 살아남기 위한 이야기"
        },
        {
            "title": "돼지우리",
            "description": "기억을 잃은 남자가 의문의 섬에서 겪는 사건들"
        },
        {
            "title": "방탈출",
            "description": "목숨을 건 게임과 퍼즐을 풀어나가는 스릴러"
        },
        {
            "title": "살인자ㅇ난감",
            "description": "우연한 살인을 계기로 연쇄 사건에 휘말리는 이야기"
        }
    ],

    "BL": [
        {
            "title": "체크메이트",
            "description": "복수와 집착이 얽힌 관계를 그린 작품"
        },
        {
            "title": "물가의 밤",
            "description": "복잡한 감정선과 관계를 중심으로 한 작품"
        },
        {
            "title": "남고 소년",
            "description": "고등학생들의 일상과 성장을 그린 작품"
        },
        {
            "title": "시맨틱 에러",
            "description": "정반대 성격의 대학생들이 만나 벌어지는 이야기"
        },
        {
            "title": "위험한 편의점",
            "description": "편의점 아르바이트생과 손님의 관계를 그린 작품"
        }
    ],

    "드라마": [
        {
            "title": "유미의 세포들",
            "description": "세포들의 시선으로 그려낸 현실적인 일상과 연애 이야기"
        },
        {
            "title": "이번 생도 잘 부탁해",
            "description": "전생의 기억을 가진 주인공의 사랑과 성장 이야기"
        },
        {
            "title": "정년이",
            "description": "국극 배우를 꿈꾸는 소녀의 성장 이야기"
        },
        {
            "title": "중증외상센터 : 골든 아워",
            "description": "생명을 살리기 위해 노력하는 의료진들의 이야기"
        },
        {
            "title": "가비지타임",
            "description": "농구부 학생들의 성장과 우정을 그린 스포츠 드라마"
        }
    ]
}

genre = st.selectbox(
    "장르 선택",
    list(webtoon_data.keys())
)

mood = st.selectbox(
    "분위기 선택",
    ["힐링", "성장", "피폐", "개그"]
)

if st.button("추천 받기"):
    webtoon = random.choice(webtoon_data[genre])

    st.success(f"📚 추천 웹툰: {webtoon['title']}")
    st.write(webtoon["description"])
