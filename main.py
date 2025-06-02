import streamlit as st
import random

# MBTI별 추천 직업 리스트와 이미지
mbti_jobs = {
    "INTJ": [
        ("🔬 과학자", "https://cdn.pixabay.com/photo/2016/11/18/13/47/laboratory-1834220_1280.jpg"),
        ("👩‍💻 데이터 사이언티스트", "https://cdn.pixabay.com/photo/2019/04/04/11/57/artificial-intelligence-4098952_1280.jpg"),
        ("📈 전략 컨설턴트", "https://cdn.pixabay.com/photo/2018/03/11/09/33/analytics-3214287_1280.jpg")
    ],
    "INTP": [
        ("💡 발명가", "https://cdn.pixabay.com/photo/2015/05/31/10/55/light-bulb-791825_1280.jpg"),
        ("📊 연구원", "https://cdn.pixabay.com/photo/2016/03/27/21/56/analysis-1280537_1280.jpg"),
        ("👨‍🔬 이론 물리학자", "https://cdn.pixabay.com/photo/2017/07/12/18/04/physics-2493764_1280.jpg")
    ],
    # (다른 MBTI들도 같은 형식으로 추가)
    # 예시로 ENFP 한 개만 더 추가
    "ENFP": [
        ("🌍 여행가", "https://cdn.pixabay.com/photo/2017/01/20/00/30/backpack-1997620_1280.jpg"),
        ("🎬 영화 감독", "https://cdn.pixabay.com/photo/2016/11/29/05/08/camera-1867184_1280.jpg"),
        ("🧑‍🎨 창작자", "https://cdn.pixabay.com/photo/2016/11/19/14/00/artist-1837302_1280.jpg")
    ]
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
    job, image_url = random.choice(mbti_jobs[mbti])
    st.image(image_url, use_column_width=True)
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
