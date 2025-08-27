import streamlit as st

st.set_page_config(page_title="건강 자가진단 시뮬레이터", page_icon="🩺")

st.title("🩺 건강 자가진단 시뮬레이터")
st.markdown("간단한 문진을 통해 증상의 응급도를 확인해보세요.")

# 증상 선택
symptom = st.selectbox("증상을 선택하세요:", [
    "복통", "두통", "기침", "호흡곤란", "발열", "어지러움", "메스꺼움/구토"
])

# 복통 문진
if symptom == "복통":
    st.subheader("📍 복통 문진")
    area = st.radio("통증 위치는 어디인가요?", ["상복부", "하복부", "전체", "잘 모르겠음"])
    intensity = st.slider("통증 강도 (0 = 없음, 10 = 매우 심함)", 0, 10)
    additional = st.checkbox("구토/설사/혈변 등의 증상이 동반되나요?")
    
    if intensity >= 7 and additional:
        st.error("🚨 응급실 방문이 필요할 수 있습니다. 즉시 병원에 방문하세요.")
    elif intensity <= 3 and not additional:
        st.success("✅ 자가조치가 가능합니다. 수분 섭취와 휴식을 취하세요.")
    else:
        st.warning("⚠️ 외래 진료를 권장합니다.")

# 두통 문진
elif symptom == "두통":
    st.subheader("🧠 두통 문진")
    intensity = st.slider("두통 강도 (0 = 없음, 10 = 매우 심함)", 0, 10)
    sudden = st.checkbox("갑작스럽고 번개처럼 시작된 두통인가요?")
    fever = st.checkbox("발열 또는 목 경직이 동반되나요?")
    
    if sudden or (intensity >= 8 and fever):
        st.error("🚨 뇌출혈/수막염 가능성. 즉시 응급실 방문이 필요합니다.")
    elif intensity <= 3:
        st.success("✅ 자가조치가 가능합니다. 수면과 스트레스 완화가 도움이 됩니다.")
    else:
        st.warning("⚠️ 외래 진료를 권장합니다.")

# 기침 문진
elif symptom == "기침":
    st.subheader("😷 기침 문진")
    duration = st.radio("기침이 지속된 기간은?", ["3일 미만", "3일 이상", "2주 이상"])
    fever = st.checkbox("발열이 동반되나요?")
    breathing = st.checkbox("호흡곤란이나 흉통이 있나요?")
    
    if breathing:
        st.error("🚨 폐렴 또는 천식 가능성. 즉시 병원 방문이 필요합니다.")
    elif duration == "2주 이상":
        st.warning("⚠️ 만성 기침은 결핵 등 원인 가능성이 있습니다. 외래 진료 권장.")
    elif duration == "3일 미만" and not fever:
        st.success("✅ 자가조치가 가능합니다. 충분한 수분과 휴식을 취하세요.")
    else:
        st.warning("⚠️ 외래 진료를 권장합니다.")

# 호흡곤란 문진
elif symptom == "호흡곤란":
    st.subheader("💨 호흡곤란 문진")
    sudden = st.checkbox("갑작스럽게 발생했나요?")
    chest_pain = st.checkbox("가슴 통증이 함께 있나요?")
    chronic = st.checkbox("기저 질환(천식, COPD 등)이 있나요?")
    
    if sudden and chest_pain:
        st.error("🚨 심근경색 또는 폐색전증 가능성. 즉시 응급실로 가세요.")
    elif chronic:
        st.warning("⚠️ 만성질환자일 경우 상태 악화 가능성. 병원 방문 필요.")
    else:
        st.success("✅ 경미한 호흡곤란일 수 있습니다. 상황을 지켜보며 휴식을 취하세요.")

# 발열 문진
elif symptom == "발열":
    st.subheader("🌡️ 발열 문진")
    temperature = st.slider("체온을 선택하세요 (°C)", 35.0, 42.0, step=0.1)
    duration = st.radio("발열이 지속된 기간은?", ["1일 이하", "2~3일", "3일 이상"])
    infant = st.checkbox("소아/영유아인가요?")
    
    if temperature >= 39.0 and duration == "3일 이상":
        st.error("🚨 고열 지속 시 세균성 감염 가능성. 병원 진료가 꼭 필요합니다.")
    elif infant and temperature >= 38.0:
        st.warning("⚠️ 영유아의 발열은 주의가 필요합니다. 소아청소년과 진료 권장.")
    elif temperature <= 37.5:
        st.success("✅ 정상 범위의 체온입니다. 경과 관찰을 권장합니다.")
    else:
        st.warning("⚠️ 외래 진료를 고려하세요.")

# 어지러움 문진
elif symptom == "어지러움":
    st.subheader("🌀 어지러움 문진")
    standing = st.checkbox("일어설 때 더 심해지나요?")
    nausea = st.checkbox("메스꺼움이 동반되나요?")
    trauma = st.checkbox("최근 머리를 다친 적이 있나요?")
    
    if trauma:
        st.error("🚨 외상 후 어지러움은 뇌손상 가능성. 즉시 병원 방문 필요.")
    elif standing and nausea:
        st.warning("⚠️ 저혈압 또는 전정기관 이상 가능성. 외래 진료 권장.")
    else:
        st.success("✅ 일시적인 현기증일 수 있습니다. 수분 섭취 및 휴식을 취하세요.")

# 메스꺼움/구토 문진
elif symptom == "메스꺼움/구토":
    st.subheader("🤢 메스꺼움/구토 문진")
    frequency = st.radio("구토 빈도는?", ["1~2회", "3회 이상", "지속적인 구토"])
    hydration = st.checkbox("수분 섭취가 어려운 상태인가요?")
    blood = st.checkbox("토사물에 피가 섞여 있나요?")
    
    if blood or (frequency == "지속적인 구토" and hydration):
        st.error("🚨 탈수 또는 위장 출혈 가능성. 즉시 병원 방문 필요.")
    elif frequency == "1~2회" and not hydration:
        st.success("✅ 일시적인 위장장애일 수 있습니다. 경과 관찰을 권장합니다.")
    else:
        st.warning("⚠️ 증상이 지속된다면 외래 진료를 받으세요.")

# 공통 안내
st.markdown("---")
st.info("❗ 이 앱은 참고용 자가진단 도구이며, 정확한 의학적 판단은 전문의의 진료를 통해 확인하시기 바랍니다.")
