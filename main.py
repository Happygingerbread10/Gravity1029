import streamlit as st
import random

# MBTI별 추천 직업 리스트와 이미지 URL
mbti_jobs = {
    "INTJ": [
        ("🔬 과학자", "https://cdn.pixabay.com/photo/2016/11/18/13/47/laboratory-1834220_1280.jpg"),
        ("👩‍💻 데이터 사이언티스트", "https://cdn.pixabay.com/photo/2019/04/04/11/57/artificial-intelligence-4098952_1280.jpg"),
        ("📈 전략 컨설턴트", "https://cdn.pixabay.com/photo/2018/03/11/09/33/analytics-3214287_1280.jpg")
    ],
    "ENFP": [
        ("🌍 여행가", "https://cdn.pixabay.com/photo/2017/01/20/00/30/backpack-1997620_1280.jpg"),
        ("🎬 영화 감독", "https://cdn.pixabay.com/photo/2016/11/29/05/08/camera-1867184_1280.jpg"),
        ("🧑‍🎨 창작자", "https://cdn.pixabay.com/photo/2016/11/19/14/00/artist-1837302_1280.jpg")
    ],
    "ISFJ": [
        ("👩‍⚕️ 간호사", "https://cdn.pixabay.com/photo/2016/03/31/19/56/medical-1291052_1280.jpg"),
        ("🏥 사회복지사", "https://cdn.pixabay.com/photo/2017/08/06/04/00/wheelchair-2588794_1280.jpg"),
        ("👨‍🏫 교사", "https://cdn.pixabay.com/photo/2016/02/19/11/19/school-1209821_1280.jpg")
    ]
}

# 페이지 설정
st.set_page_config(page_title="💖 MBTI 직업 추천기 💖", page_icon="🎯", layout="centered")

# 화려한 헤더
st.markdown("""
    <div style='text-align: center;'>
        <h1 style='color: #FF69B4;'>🌟 MBTI로 알아보는 인생 직업 찾기! 🌟</h1>
        <p style='font-size: 18px;'>당신의 성격에 딱 맞는 직업은? 🎨💼✨<br>MBTI를 골라보세요! 👇</p>
    </div>
    <hr style='border-top: 3px solid #f0f0f0;'>
""", unsafe_allow_html=True)

# MBTI 선택 박스
mbti = st.selectbox("🎭 MBTI 유형을 선택하세요!", list(mbti_jobs.keys()))

# 추천 직업 표시
if mbti:
    job, image_url = random.choice(mbti_jobs[mbti])
    st.markdown(f"<h2 style='color:#00BFFF;'>🎯 추천 직업: {job}</h2>", unsafe_allow_html=True)
    st.image(image_url, caption=job, use_column_width=True)
    st.balloons()
    st.success("✨ 당신에게 어울리는 직업이에요! 꿈을 향해 출발~ 🚀")

# 화려한 푸터
st.markdown("""
    <hr style='border-top: 2px dashed #f0c0ff;'>
    <div style='text-align: center; font-size: 16px; color: #888888;'>
        이 앱은 교육용 목적으로 제작되었습니다. 💡<br>
        모든 추천은 참고용이니 스스로를 믿고 탐색하세요! 🌈<br><br>
        Made with ❤️ by ChatGPT
    </div>
""", unsafe_allow_html=True)

# 사이드바 꾸미기
st.sidebar.title("📚 메뉴")
st.sidebar.info("MBTI 기반 직업 추천 앱에 오신 걸 환영합니다! 🎉")
st.sidebar.success("MBTI + 이모지 + 이미지 = 인생직업찾기")
st.sidebar.warning("🔎 직업 추천은 참고용입니다!")
