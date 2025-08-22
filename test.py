import streamlit as st

# ----------------------------
# 기본 데이터 (간단 예시)
# ----------------------------
nursing_diagnoses = {
    "호흡곤란": {
        "진단": "비효율적 호흡양상",
        "중재": [
            "호흡곤란 정도 사정 (SpO₂, 호흡수)",
            "산소 공급 유지",
            "호흡 패턴 교육 (심호흡, 기침법)",
        ],
        "목표": "환자는 24시간 이내 호흡곤란이 완화되고 SpO₂가 95% 이상 유지된다.",
    },
    "통증": {
        "진단": "급성 통증",
        "중재": [
            "통증 사정 (0~10 척도)",
            "처방된 진통제 투여",
            "이완요법 및 편안한 체위 제공",
        ],
        "목표": "환자는 1시간 이내 통증 점수가 3점 이하로 감소한다.",
    },
    "불안": {
        "진단": "불안",
        "중재": [
            "불안의 원인 파악 및 경청",
            "심호흡, 명상 등 이완요법 제공",
            "정서적 지지 및 정보 제공",
        ],
        "목표": "환자는 30분 이내 불안 정도를 감소되었다고 보고한다.",
    },
}

# ----------------------------
# Streamlit UI
# ----------------------------
st.set_page_config(page_title="간호과정 도우미", page_icon="🩺", layout="wide")

st.title("🩺 간호 진단 & 간호과정 도우미")
st.write("환자 정보를 입력하면 적절한 간호진단과 중재를 추천합니다.")

# 사용자 입력
col1, col2 = st.columns(2)
with col1:
    symptom = st.selectbox("주요 증상 선택", ["호흡곤란", "통증", "불안"])
with col2:
    severity = st.slider("증상 정도 (0~10)", 0, 10, 5)

# 결과 출력
if st.button("간호과정 생성하기"):
    data = nursing_diagnoses.get(symptom)
    if data:
        st.subheader("✅ 간호진단")
        st.write(f"**{data['진단']}**")

        st.subheader("📝 간호중재")
        for i, intervention in enumerate(data['중재'], start=1):
            st.write(f"{i}. {intervention}")

        st.subheader("🎯 간호목표")
        st.write(data['목표'])

        # 간단한 평가
        if severity > 5:
            st.warning("⚠️ 증상 정도가 심각하므로 즉각적인 중재가 필요합니다.")
        else:
            st.success("😊 현재 증상은 비교적 안정적입니다.")

        # PDF/Word 생성 기능 확장 가능
    else:
        st.error("데이터베이스에 해당 증상이 없습니다.")

