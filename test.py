import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# ----------------------------
# 데이터 예시 (간단 설명)
# ----------------------------
body_systems = {
    "호흡기계": {
        "설명": "폐와 기도를 포함하며, 산소를 들여보내고 이산화탄소를 배출하는 역할을 합니다.",
        "질환": "폐렴 시 폐포에 염증이 생겨 가스교환이 저하됩니다.",
        "퀴즈": {
            "질문": "폐에서 산소와 이산화탄소가 교환되는 부위는 어디일까요?",
            "보기": ["기관", "폐포", "기관지"],
            "정답": "폐포",
        },
    },
    "순환기계": {
        "설명": "심장과 혈관으로 구성되며, 산소와 영양분을 온몸에 전달합니다.",
        "질환": "심부전 시 심박출량이 감소하여 전신에 혈액 공급이 저하됩니다.",
        "퀴즈": {
            "질문": "심박출량(Cardiac Output)의 공식은?",
            "보기": ["심박수 × 1회 박출량", "혈압 ÷ 맥박수", "호흡수 × 폐활량"],
            "정답": "심박수 × 1회 박출량",
        },
    },
    "신경계": {
        "설명": "뇌와 척수, 신경으로 이루어져 신체 기능을 조절하고 감각을 전달합니다.",
        "질환": "뇌졸중 시 특정 부위의 신경 손상으로 운동/감각 기능이 저하됩니다.",
        "퀴즈": {
            "질문": "말초신경계는 크게 몇 가지로 구분되나요?",
            "보기": ["2가지 (체성, 자율)", "3가지 (운동, 감각, 자율)", "1가지 (자율)",],
            "정답": "2가지 (체성, 자율)",
        },
    },
}

# ----------------------------
# Streamlit UI
# ----------------------------
st.set_page_config(page_title="간호학 해부·생리학 시각화", page_icon="🧬", layout="wide")

st.title("🧬 간호학 해부·생리학 시각화 앱")
st.write("인체 시스템을 선택하면 설명, 질환 사례, 퀴즈를 제공합니다.")

# 선택
system = st.selectbox("인체 시스템 선택", list(body_systems.keys()))
data = body_systems[system]

# 정보 출력
st.subheader(f"🔎 {system} 설명")
st.info(data["설명"])

st.subheader("⚠️ 관련 질환")
st.warning(data["질환"])

# 간단 그래프 (예: 활력징후 변화 시뮬레이션)
if system == "호흡기계":
    x = np.linspace(0, 10, 100)
    y = np.sin(x)  # 정상 호흡 곡선
    plt.plot(x, y)
    plt.title("호흡 파형 예시")
    st.pyplot(plt)
    plt.clf()

elif system == "순환기계":
    hr = np.random.normal(75, 5, 100)  # 심박수 데이터
    plt.plot(hr)
    plt.title("심박수 변화 (bpm)")
    st.pyplot(plt)
    plt.clf()

# 퀴즈
quiz = data["퀴즈"]
st.subheader("📝 퀴즈")
st.write(quiz["질문"])
choice = st.radio("보기", quiz["보기"])

if st.button("정답 확인"):
    if choice == quiz["정답"]:
        st.success("✅ 정답입니다!")
    else:
        st.error(f"❌ 오답입니다. 정답은 {quiz['정답']} 입니다.")
