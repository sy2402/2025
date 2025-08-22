import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="산소포화도 & 호흡 생리 시뮬레이터", page_icon="🫁", layout="wide")

st.title("🫁 산소포화도 & 호흡 생리 시뮬레이터")

# 사용자 입력
altitude = st.slider("고도 (m)", 0, 8000, 0, 500)  # 해수면~에베레스트
resp_rate = st.slider("호흡수 (회/분)", 8, 40, 16)

# 단순 모델: 고도가 올라갈수록 산소분압 감소
pO2_sea = 100  # mmHg
pO2 = pO2_sea * np.exp(-altitude / 7000)

# 산소포화도 (Sigmoid 근사)
def oxyhemoglobin_curve(pO2, resp_rate):
    sat = 100 / (1 + np.exp(-(pO2 - 60) / 5))
    sat = sat + (resp_rate - 16) * 0.3  # 과호흡 → 산소포화도 상승 보정
    return np.clip(sat, 50, 100)

# 그래프 그리기
x = np.linspace(20, 100, 200)
y = 100 / (1 + np.exp(-(x - 60) / 5))
fig, ax = plt.subplots()
ax.plot(x, y, label="O₂ 해리곡선")
ax.axvline(pO2, color='r', linestyle="--", label=f"현재 pO₂ ≈ {pO2:.1f} mmHg")
ax.set_xlabel("동맥 산소분압 (mmHg)")
ax.set_ylabel("산소포화도 (%)")
ax.legend()
st.pyplot(fig)

# 현재 상태 출력
st.metric("현재 산소포화도", f"{oxyhemoglobin_curve(pO2, resp_rate):.1f} %")
