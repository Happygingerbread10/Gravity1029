import streamlit as st
import random

# MBTI별 추천 직업 데이터
mbti_jobs = {
    "ISTJ": ["👨‍💼 회계사", "👩‍⚖️ 판사", "📊 데이터 분석가"],
    "ISFJ": ["👩‍🏫 교사", "👨‍⚕️ 간호사", "📚 사서"],
    "INFJ": ["🧠 심리상담가", "✍️ 작가", "🎓 교육 컨설턴트"],
    "INTJ": ["🧪 과학자", "📈 전략기획가", "👨‍💻 소프트웨어 엔지니어"],
    "ISTP": ["🛠 정비사", "🚓 경찰관", "🔧 기술자"],
    "ISFP": ["🎨 아티스트", "🎭 배우", "🌿 원예사"],
    "INFP": ["📖 시인", "🎮 게임 디자이너", "🧘 요가 강사"],
    "INTP": ["💻 개발자", "📐 연구원", "🔬 물리학자"],
    "ESTP": ["🕵️‍♂️ 탐정", "💼 마케팅 담당자", "🎬 영화 제작자"],
    "ESFP": ["🎤 가수", "🎉 이벤트 플래너", "📸 포토그래퍼"],
    "ENFP": ["🌍 여행 가이드", "💡 창업가", "🎨 콘텐츠 크리에이터"],
    "ENTP": ["📺 방송인", "🧠 브레인스토머", "🎯 기획자"],
    "ESTJ": ["🏢 관리자", "💼 경영 컨설턴트", "⚖️ 행정 공무원"],
    "ESFJ": ["🍳 요리사", "🏥 병원 코디네이터", "👩‍👧 보육 교사"],
    "ENFJ": ["🗣 강연가", "📚 교육 전문가", "🎭 드라마 연출가"],
    "ENTJ": ["🚀 CEO", "🏛 정치인", "📊 기획 매니저"]
}

# 타이틀 및 소개
st.set_page_config(page_title="🌟 MBTI 직업 추천기 🌟", page_icon="🧭", layout="wide")
st.title("✨ MBTI로 알아보는 나에게 딱 맞는 직업 ✨")
st.markdown("""
<div style='font-size:20px; color:#4B0082;'>
    💫 아래에서 자신의 MBTI를 선택하면, 그에 어울리는 직업을 추천해 드릴게요!<br>
    🌈 이모지로 가득한 화려한 진로 탐험, 지금 시작해요!
</div>
""", unsafe_allow_html=True)

# 사용자 MBTI 선택
selected_mbti = st.selectbox("🔍 MBTI 유형을 선택하세요", list(mbti_jobs.keys()))

# 추천 버튼
if st.button("🎁 나에게 어울리는 직업 보기"):
    jobs = mbti_jobs[selected_mbti]
    st.subheader(f"📌 {selected_mbti} 유형에게 어울리는 직업은...")
    for job in random.sample(jobs, len(jobs)):
        st.success(f"✨ {job}")

# 추가 꾸미기
st.markdown("""
<hr style='border: 3px solid #FFD700;'>
<center>
<h3 style='color:#FF69B4;'>🌟 세상에서 단 하나뿐인, 당신의 가능성을 응원합니다! 🌟</h3>
<p style='color:#6A5ACD;'>더 많은 진로 정보는 선생님께 문의하세요 💌</p>
</center>
""", unsafe_allow_html=True)

st.balloons()
