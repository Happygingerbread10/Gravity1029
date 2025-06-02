import streamlit as st
import random

# MBTI별 추천 직업 리스트
mbti_jobs = {
    "INTJ": ["🔬 과학자", "👩‍💻 데이터 사이언티스트", "📈 전략 컨설턴트"],
    "INTP": ["💡 발명가", "📊 연구원", "👨‍🔬 이론 물리학자"],
    "ENTJ": ["💼 CEO", "🧠 경영 컨설턴트", "🏛️ 정치가"],
    "ENTP": ["🎤 방송인", "🎭 기획자", "🚀 창업가"],
    "INFJ": ["🧘 상담가", "📚 작가", "🧑‍🏫 교육자"],
    "INFP": ["🎨 예술가", "📝 시인", "🌱 사회 운동가"],
    "ENFJ": ["👩‍🏫 교사", "🎤 연설가", "🤝 리더"],
    "ENFP": ["🌍 여행가", "🎬 영화 감독", "🧑‍🎨 창작자"],
    "ISTJ": ["📋 행정가", "👨‍⚖️ 판사", "🛡️ 군인"],
    "ISFJ": ["👩‍⚕️ 간호사", "👨‍🏫 교사", "🏥 사회복지사"],
    "ESTJ": ["👮 경찰", "🏢 관리자", "📦 운영 책임자"],
    "ESFJ": ["💐 이벤트 플래너", "🧑‍🍳 요리사", "🛍️ 마케터"],
    "ISTP": ["🔧 엔지니어", "🕵️ 탐정", "🧭 파일럿"],
    "ISFP": ["🎶 음악가", "🎨 디자이너", "🪴 플로리스트"],
    "ESTP": ["🏎️ 레이서", "🕺 퍼포머", "💼 세일즈맨"],
    "ESFP": ["🎤 가수", "📸 인플루언서", "🎉 파티 플래너"]
}

st.set_page_config(
    page_title="🌟 MBTI로 찾는 나만의 직업 🌟",
    page_icon="✨",
    layout="centered"
)

st.markdown("""
    <h1 style='text-align: center; color: #ff69b4;'>🌈 MBTI로 알아보는 인생 직업 찾기! 💼✨</h1>
    <p style='text-align: center;'>당신의 MBTI를 선택하면 찰떡같이 어울리는 직업을 추천해드려요! 🚀🎯</p>
    <hr>
""", unsafe_allow_html=True)

# 사용자 MBTI 입력 받기
mbti = st.selectbox("🔍 당신의 MBTI를 선택하세요!", list(mbti_jobs.keys()))

if mbti:
    st.markdown(f"## 🎉 {mbti} 유형에게 추천하는 직업은?! 🎯")
    job = random.choice(mbti_jobs[mbti])
    st.markdown(f"### 👉 {job}")
    st.balloons()
    st.markdown("""
    <hr>
    <p style='text-align: center; font-size: 18px;'>모든 MBTI 유형은 고유하고 멋져요! 🌟<br>당신의 꿈을 응원합니다! 💖</p>
    """, unsafe_allow_html=True)

# 사이드바 꾸미기
st.sidebar.title("💫 메뉴")
st.sidebar.info("이 앱은 진로 교육을 돕기 위해 제작되었습니다. 🎓")
st.sidebar.success("MBTI 기반 직업 추천 ✨")
st.sidebar.warning("모든 추천은 참고용이에요! 💡")
