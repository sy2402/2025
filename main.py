import streamlit as st

st.set_page_config(page_title="MBTI 진료 교육", layout="wide")

st.title("🧑‍⚕️ MBTI 기반 진료 교육 웹앱")

# 1. MBTI 입력
mbti = st.selectbox(
    "당신의 MBTI를 선택하세요:",
    ["INTJ","INTP","ENTJ","ENTP",
     "INFJ","INFP","ENFJ","ENFP",
     "ISTJ","ISFJ","ESTJ","ESFJ",
     "ISTP","ISFP","ESTP","ESFP"]
)

st.write(f"당신이 선택한 MBTI: **{mbti}**")

# 2. MBTI별 환자 커뮤니케이션 가이드
guides = {
    "INTJ": "논리적이고 체계적으로 설명하면 효과적입니다.",
    "ENFP": "공감을 잘하지만 주제가 산만해질 수 있어 핵심을 반복해 주세요.",
    "ISTJ": "구체적이고 사실 기반으로 설명하는 것이 중요합니다.",
    # ... 나머지도 채워넣기
}

if mbti in guides:
    st.subheader("💡 진료 커뮤니케이션 가이드")
    st.info(guides[mbti])

# 3. 간단한 퀴즈
st.subheader("📝 교육용 퀴즈")
quiz_answer = st.radio(
    "ISTJ 환자의 특징은 무엇일까요?",
    ["감정적인 공감을 많이 원한다", "체계적이고 구체적인 설명을 선호한다", "즉흥적인 상담을 좋아한다"]
)

if quiz_answer:
    if quiz_answer == "체계적이고 구체적인 설명을 선호한다":
        st.success("✅ 정답입니다! ISTJ는 구체적이고 사실적인 설명을 선호합니다.")
    else:
        st.error("❌ 다시 생각해 보세요!")
