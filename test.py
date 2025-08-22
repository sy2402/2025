import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="약물 농도-시간 곡선", page_icon="💉", layout="wide")

st.title("💉 약물 농도-시간 시뮬레이터")

# 사용자 입력
dose = st.number_input("투여 용량 (mg)", 10, 1000, 500, 50)
half_life = st.slider("반감기 (시간)", 1, 24, 6)
interval = st.slider("투여 간격 (시간)", 1, 24, 8)
time_end = st.slider("시뮬레이션 시간 (시간)", 12, 72, 48)

# 약물 농도 계산
k = np.log(2) / half_life  # 소실 속도 상수
time = np.linspace(0, time_end, 500)
conc = np.zeros_like(time)

# 반복 투여 모델
for t in np.arange(0, time_end, interval):
    conc += dose * np.exp(-k * (time - t)) * (time >= t)

# 그래프
fig, ax = plt.subplots()
ax.plot(time, conc, label="혈중 약물 농도")
ax.set_xlabel("시간 (hr)")
ax.set_ylabel("농도 (mg/L)")
ax.axhline(y=np.max(conc)/2, color="r", linestyle="--", label="50% 농도")
ax.legend()
st.pyplot(fig)

# 해석 출력
st.metric("최고 농도 (Cmax)", f"{np.max(conc):.1f} mg/L")
st.metric("반감기", f"{half_life} 시간")
