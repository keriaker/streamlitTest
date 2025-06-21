import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="MBTI 직업 추천 💼✨",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 스타일
st.markdown(
    """
    <style>
    .title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        color: #5A189A;
        margin-bottom: 20px;
    }
    .job-card {
        background-color: #f8f0fc;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        margin: 10px 0;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 헤더
st.markdown('<div class="title">🌟 나에게 어울리는 직업은? 🌟</div>', unsafe_allow_html=True)
st.subheader("📌 MBTI를 선택하면, 나에게 꼭 맞는 직업을 추천해드려요!")

# MBTI 직업 추천 매핑
mbti_jobs = {
    "INTJ": {"title": "전략 기획가 🧠📊", "desc": "복잡한 문제 해결과 분석에 강한 INTJ는 기획, 분석 분야에 최적화!"},
    "INFP": {"title": "작가 ✍️📚", "desc": "상상력과 감성이 풍부한 INFP는 예술가적 기질이 뛰어나요!"},
    "ENTP": {"title": "스타트업 창업가 🚀🔥", "desc": "새로운 아이디어가 넘치는 ENTP는 창업이나 혁신적인 역할에 찰떡!"},
    "ESFJ": {"title": "간호사 💉💖", "desc": "타인을 돕고 싶은 마음이 큰 ESFJ는 보건의료 분야와 잘 맞아요!"},
    "ISTP": {"title": "엔지니어 🛠️🧰", "desc": "실용적이고 문제 해결력이 뛰어난 ISTP는  기술 분야에서 활약해요!"}
}
