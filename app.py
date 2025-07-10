import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 표준 전극전위 데이터 (예시)
standard_potentials = {
    "Zn": -0.76,
    "Cu": 0.34,
    "Fe": -0.44,
    "Ag": 0.80
}

st.title("🔋 산화/환원 전극 선택 → 기전력 계산 + 전지 시각화")

# 산화 전극, 환원 전극 선택
anode = st.selectbox("산화 전극(음극)을 선택하세요", options=standard_potentials.keys())
cathode = st.selectbox("환원 전극(양극)을 선택하세요", options=standard_potentials.keys())

# 기전력 계산
E_cell = standard_potentials[cathode] - standard_potentials[anode]
st.write(f"✅ 선택한 전지의 표준 기전력: **{E_cell:.2f} V**")

# 시각화 함수
def draw_custom_cell(anode, cathode):
    fig, ax = plt.subplots(figsize=(8,5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis('off')

    # 전극과 전해질 영역
    ax.add_patch(patches.Rectangle((0.5,1), 3,3, color='#d0e7f9', alpha=0.5))
    ax.add_patch(patches.Rectangle((6.5,1), 3,3, color='#d0e7f9', alpha=0.5))

    # 전극
    ax.add_patch(patches.Rectangle((0.9,1),0.3,3, color='gray'))
    ax.add_patch(patches.Rectangle((8.8,1),0.3,3, color='orange'))

    # 전극 라벨
    ax.text(0.6,4.2,f"{anode} 전극(-, 산화)", fontsize=10)
    ax.text(8.0,4.2,f"{cathode} 전극(+, 환원)", fontsize=10)

    # 전자 흐름
    ax.arrow(3.5,3.5,2.8,0, head_width=0.2, head_length=0.3, fc='blue', ec='blue', linewidth=2)
    ax.text(5,3.7,"전자 흐름", fontsize=10, color='blue')

    # 간단한 반응식 예시
    ax.text(0.7,0.5,f"{anode} → {anode}²⁺ + 2e⁻", fontsize=10)
    ax.text(6.7,0.5,f"{cathode}²⁺ + 2e⁻ → {cathode}", fontsize=10)

    return fig

# 시각화 출력
fig = draw_custom_cell(anode, cathode)
st.pyplot(fig)
