import streamlit as st

# ----------------------------
# Streamlit 설정
# ----------------------------
st.set_page_config(page_title="투약 계산 & 약물 안전 교육", page_icon="💊", layout="wide")

st.title("💊 투약 계산 & 약물 안전 교육 앱")
st.write("환자 정보를 입력하고 약물 계산 문제를 풀어보세요.")

# ----------------------------
# 환자 정보 입력
# ----------------------------
col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("환자 체중 (kg)", min_value=1.0, max_value=200.0, value=60.0, step=0.5)
with col2:
    age = st.number_input("환자 나이 (세)", min_value=0, max_value=120, value=30, step=1)

# ----------------------------
# 예시 문제 1: 소아 용량 계산
# ----------------------------
st.subheader("📌 문제 1: 체중 기반 소아 용량 계산")
st.write("아세트아미노펜 권장 용량은 10 mg/kg 입니다. 환자에게 필요한 1회 용량은 얼마일까요?")

correct_dose = weight * 10  # mg
user_answer = st.number_input("계산한 용량 (mg)", min_value=0.0, step=0.1)

if st.button("정답 확인 (문제 1)"):
    if abs(user_answer - correct_dose) < 0.1:
        st.success(f"✅ 정답입니다! (정답: {correct_dose:.1f} mg)")
    else:
        st.error(f"❌ 오답입니다. 정답은 {correct_dose:.1f} mg 입니다.")
        st.info("풀이: 체중(kg) × 10 mg = 1회 용량 (mg)")

# ----------------------------
# 예시 문제 2: 수액 주입 속도 계산
# ----------------------------
st.subheader("📌 문제 2: 수액 주입 속도 계산")
st.write("500 mL 수액을 4시간에 주입하려고 합니다. 시간당 몇 mL를 주입해야 할까요?")

correct_rate = 500 / 4  # mL/hr
user_answer2 = st.number_input("계산한 주입 속도 (mL/hr)", min_value=0.0, step=0.1)

if st.button("정답 확인 (문제 2)"):
    if abs(user_answer2 - correct_rate) < 0.1:
        st.success(f"✅ 정답입니다! (정답: {correct_rate:.1f} mL/hr)")
    else:
        st.error(f"❌ 오답입니다. 정답은 {correct_rate:.1f} mL/hr 입니다.")
        st.info("풀이: 총량 ÷ 시간 = 주입 속도 (mL/hr)")

# ----------------------------
# 약물 안전 가이드
# ----------------------------
st.subheader("⚠️ 약물 안전 가이드")
st.markdown("""
- 투약 전 **3원칙**: 환자 확인, 약물 확인, 용량 확인  
- 투약 후 반드시 **부작용** 관찰  
- 계산이 애매할 땐 반드시 **이중 확인** 필요
""")
