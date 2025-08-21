import streamlit as st

st.set_page_config(page_title="🌈 MBTI 진료 교육 웹앱", layout="wide")

# --- 헤더 ---
st.markdown(
    """
    <h1 style='text-align: center; color: #ff66b2;'>
    🧑‍⚕️✨ MBTI 기반 진료 커뮤니케이션 교육 ✨🧑‍⚕️
    </h1>
    <h3 style='text-align: center; color: #666;'>
    🌸 환자의 성향에 따라 달라지는 맞춤형 진료 가이드 🌸
    </h3>
    """,
    unsafe_allow_html=True
)

st.divider()

# --- MBTI 선택 ---
st.markdown("### 🌟 Step 1. 당신의 MBTI를 선택하세요 🌟")
mbti = st.selectbox(
    "👇 MBTI를 골라주세요!",
    ["INTJ","INTP","ENTJ","ENTP",
     "INFJ","INFP","ENFJ","ENFP",
     "ISTJ","ISFJ","ESTJ","ESFJ",
     "ISTP","ISFP","ESTP","ESFP"]
)

st.success(f"🎉 선택된 MBTI: **{mbti}** 💖")

# --- 가이드 ---
st.markdown("### 💡 Step 2. 환자 진료 가이드 💡")

guides = {
    "INTJ": "📚 논리적이고 체계적인 설명이 효과적이에요.",
    "ENFP": "🎨 공감을 잘하지만 산만할 수 있어 ✨핵심을 반복✨해 주세요.",
    "ISTJ": "🗂️ 구체적이고 사실 기반 설명이 중요합니다.",
    "INFP": "💞 감정적 공감과 따뜻한 분위기가 효과적이에요.",
    "ESTP": "⚡ 즉흥적이고 실용적인 대화를 선호합니다.",
    "ESFJ": "🤝 관계 중심, 친근하게 다가가는 것이 좋아요.",
    # ... 나머지도 추가 가능
}

if mbti in guides:
    st.markdown(
        f"""
        <div style="padding:20px; background-color:#ffe6f2; border-radius:15px; 
        border: 2px solid #ff99cc; font-size:18px;">
        🌟 <b>{mbti}</b> 환자 진료 팁 <br><br>
        {guides[mbti]}
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

# --- 퀴즈 ---
st.markdown("### 📝 Step 3. 교육용 퀴즈 📝")

quiz_answer = st.radio(
    "❓ ISTJ 환자의 특징은 무엇일까요?",
    [
        "😭 감정적인 공감을 많이 원한다",
        "🗂️ 체계적이고 구체적인 설명을 선호한다",
        "🎭 즉흥적인 상담을 좋아한다"
    ]
)

if quiz_answer:
    if "체계적" in quiz_answer:
        st.balloons()
        st.success("✅ 정답이에요! 🎉 ISTJ는 구체적이고 사실적인 설명을 선호합니다.")
    else:
        st.error("❌ 아쉽습니다! 다시 시도해 보세요 💪")

# --- 푸터 ---
st.markdown(
    """
    <hr>
    <p style='text-align: center; color: gray;'>
    ✨ MBTI 기반 환자 교육 플랫폼 ✨ <br>
    🧑‍⚕️ Designed for Medical Training 💊
    </p>
    """,
    unsafe_allow_html=True
)
