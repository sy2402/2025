import streamlit as st

# ------------------------
# 초기 설정
# ------------------------
st.set_page_config(page_title="응급상황 대응 훈련", page_icon="🚑", layout="centered")

st.title("🚨 응급상황 대응 훈련 시뮬레이터")
st.write("임상에서 자주 발생하는 응급 케이스에 대해 올바른 대응을 훈련해보세요.")

# ------------------------
# 시나리오 데이터
# ------------------------
scenarios = {
    "심정지 환자": {
        "intro": "병실에서 환자가 갑자기 의식을 잃고 반응이 없습니다.",
        "steps": [
            ("환자 반응 확인", True),
            ("주변에 도움 요청", True),
            ("호흡 및 맥박 확인", True),
            ("심폐소생술(CPR) 시작", True),
            ("산소 공급 먼저", False),
            ("혈압 측정", False),
        ],
    },
    "기도폐쇄 환자": {
        "intro": "환자가 식사 중 갑자기 기침하며 숨을 못 쉽니다.",
        "steps": [
            ("환자에게 기침 유도", True),
            ("하임리히법 시행", True),
            ("산소 공급 먼저", False),
            ("의식 확인 및 CPR 준비", True),
            ("혈압 측정", False),
        ],
    },
}

# ------------------------
# 선택한 시나리오 불러오기
# ------------------------
scenario = st.selectbox("시나리오 선택", list(scenarios.keys()))
st.subheader(f"📝 상황: {scenario}")
st.info(scenarios[scenario]["intro"])

# ------------------------
# 진행 상황 저장 (세션)
# ------------------------
if "progress" not in st.session_state:
    st.session_state.progress = []
if "score" not in st.session_state:
    st.session_state.score = 0

# ------------------------
# 버튼으로 단계 진행
# ------------------------
for step, correct in scenarios[scenario]["steps"]:
    if step not in st.session_state.progress:
        if st.button(step):
            st.session_state.progress.append(step)
            if correct:
                st.session_state.score += 1
                st.success(f"✅ 올바른 선택: {step}")
            else:
                st.error(f"❌ 잘못된 선택: {step}")
        break

# ------------------------
# 결과 출력
# ------------------------
if len(st.session_state.progress) == len(scenarios[scenario]["steps"]):
    st.subheader("📊 결과 요약")
    st.write(f"점수: {st.session_state.score} / {len(scenarios[scenario]['steps'])}")
    if st.session_state.score >= len(scenarios[scenario]["steps"]) - 1:
        st.success("🎉 훌륭합니다! 응급 상황 대응을 잘 수행했습니다.")
    else:
        st.warning("더 연습이 필요합니다. 올바른 우선순위를 다시 학습하세요.")

    if st.button("🔄 다시 시작"):
        st.session_state.progress = []
        st.session_state.score = 0
