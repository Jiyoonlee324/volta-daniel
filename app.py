import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

st.title("🔋 전기화학 전지 시각화 (화학Ⅱ 화학 전지의 원리)")

# ----------------------------
# 📌 1️⃣ 다니엘 전지 / 볼타 전지 선택 & 시각화
# ----------------------------

cell_type = st.radio("전지 종류를 선택하세요:", ["다니엘 전지", "볼타 전지"])

def draw_cell_diagram(cell_type):
    fig, ax = plt.subplots(figsize=(8,5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis('off')

    if cell_type == "다니엘 전지":
        ax.add_patch(patches.Rectangle((0.5,1), 3,3, color='#d0e7f9', alpha=0.5))
        ax.add_patch(patches.Rectangle((6.5,1), 3,3, color='#d0e7f9', alpha=0.5))
        ax.text(1.7,4.2,"ZnSO₄(aq)", fontsize=10)
        ax.text(7.6,4.2,"CuSO₄(aq)", fontsize=10)

        ax.add_patch(patches.Rectangle((0.9,1),0.3,3, color='gray'))
        ax.add_patch(patches.Rectangle((8.8,1),0.3,3, color='orange'))
        ax.text(0.6,4.5,"Zn electrode(-)", fontsize=10)
        ax.text(8.3,4.5,"Cu electrode(+)", fontsize=10)

        ax.add_patch(patches.Rectangle((4.6,2), 0.8, 1, color='#f0e68c', alpha=0.8))
        ax.text(4.65,3.1, "salt bridge", fontsize=9, color='green')

        ax.arrow(3.5,3.5,2.8,0, head_width=0.2, head_length=0.3, fc='blue', ec='blue', linewidth=2)
        ax.text(5,3.7,"electron flow", fontsize=10, color='blue')

        ax.add_patch(patches.Circle((2,2.5),0.2,color='purple'))
        ax.text(1.8,2.1,"Zn²⁺", fontsize=9)
        ax.add_patch(patches.Circle((8,2.5),0.2,color='pink'))
        ax.text(7.8,2.1,"Cu²⁺", fontsize=9)

        ax.text(1,0.5,"Zn → Zn²⁺ + 2e⁻ (oxidation)", fontsize=10)
        ax.text(6.5,0.5,"Cu²⁺ + 2e⁻ → Cu (reduction)", fontsize=10)
        ax.text(4,4.8,"salt bridge: Na⁺, Cl⁻ transfer", fontsize=10, color='green')

    elif cell_type == "볼타 전지":
        ax.add_patch(patches.Rectangle((0.5,1), 9,3, color='#d0e7f9', alpha=0.5))
        ax.text(4.2,4.2,"dilute H₂SO₄(aq)", fontsize=10)

        ax.add_patch(patches.Rectangle((0.9,1),0.3,3, color='gray'))
        ax.add_patch(patches.Rectangle((8.8,1),0.3,3, color='orange'))
        ax.text(0.6,4.5,"Zn electrode(-)", fontsize=10)
        ax.text(8.3,4.5,"Cu electrode(+)", fontsize=10)

        ax.arrow(3.5,3.5,2.8,0, head_width=0.2, head_length=0.3, fc='blue', ec='blue', linewidth=2)
        ax.text(5,3.7,"electron flow", fontsize=10, color='blue')

        ax.add_patch(patches.Circle((2,2.5),0.2,color='purple'))
        ax.text(1.8,2.1,"Zn²⁺", fontsize=9)
        ax.add_patch(patches.Circle((8,2.5),0.2,color='pink'))
        ax.text(7.8,2.1,"H⁺", fontsize=9)

        ax.add_patch(patches.Circle((8.5,3.3),0.1,color='gray'))
        ax.add_patch(patches.Circle((8.7,3.5),0.1,color='gray'))

        ax.text(1,0.5,"Zn + H⁺ → Zn²⁺ + H₂↑ (oxidation)", fontsize=10)
        ax.text(6.5,0.5,"2H⁺ + 2e⁻ → H₂ (reduction)", fontsize=10)
        ax.text(4,4.8,"reaction in the same solution", fontsize=10, color='green')

    return fig

fig = draw_cell_diagram(cell_type)
st.pyplot(fig)

# ----------------------------
# 📌 2️⃣ 전지 비교 표
# ----------------------------
st.markdown("---")
st.subheader("📌 다니엘 전지 vs 볼타 전지 차이")
st.markdown("""
| 구분 | 다니엘 전지 | 볼타 전지 |
|------|-------------|-----------|
| 전해질 | ZnSO₄, CuSO₄ | 묽은 H₂SO₄ |
| 염다리 | 있음 | 없음 |
| 환원 반응 | Cu²⁺ + 2e⁻ → Cu | 2H⁺ + 2e⁻ → H₂ |
| 생성물 | 고체 Cu 석출 | H₂ 기체 발생 |
| 구조 | 다른 두 수용액 + 염다리 | 같은 수용액에 두 금속판 |
""")

# ----------------------------
# 📌 3️⃣ 전극 선택 → 기전력 계산 → 맞춤형 전지 시각화
# ----------------------------
st.markdown("---")
st.subheader("⚡️ 직접 전극 선택: 기전력 계산 & 전지 구조")

standard_potentials = {
    "Zn": -0.76,
    "Cu": 0.34,
    "Fe": -0.44,
    "Ag": 0.80
}

anode = st.selectbox("산화 전극(음극)", list(standard_potentials.keys()))
cathode = st.selectbox("환원 전극(양극)", list(standard_potentials.keys()))

E_cell = standard_potentials[cathode] - standard_potentials[anode]
st.write(f"✅ 선택한 전지의 표준 기전력: **{E_cell:.2f} V**")

st.write("💡 선택한 전극으로 계산된 기전력은 기본적으로 **염다리가 포함된 갈바니 전지 구조**를 가정합니다.")

def draw_custom_cell(anode, cathode):
    fig, ax = plt.subplots(figsize=(8,5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis('off')

    # 전해질 영역 (좌/우)
    ax.add_patch(patches.Rectangle((0.5,1), 3,3, color='#d0e7f9', alpha=0.5))
    ax.add_patch(patches.Rectangle((6.5,1), 3,3, color='#d0e7f9', alpha=0.5))

    # 염다리
    ax.add_patch(patches.Rectangle((4.6,2), 0.8, 1, color='#f0e68c', alpha=0.8))
    ax.text(4.7,3.1, "salt bridge", fontsize=9, color='green')

    # 전극
    ax.add_patch(patches.Rectangle((0.9,1),0.3,3, color='gray'))
    ax.add_patch(patches.Rectangle((8.8,1),0.3,3, color='orange'))
    ax.text(0.5,4.5,f"{anode} electrode(-)", fontsize=10)
    ax.text(8.3,4.5,f"{cathode} electrode(+)", fontsize=10)

    # 전자 흐름
    ax.arrow(3.5,3.5,2.8,0, head_width=0.2, head_length=0.3, fc='blue', ec='blue', linewidth=2)
    ax.text(5,3.7,"electron flow", fontsize=10, color='blue')

    # 간단한 반응식
    ax.text(1,0.5,f"{anode} → {anode}²⁺ + e⁻", fontsize=10)
    ax.text(6.5,0.5,f"{cathode}²⁺ + e⁻ → {cathode}", fontsize=10)

    return fig

fig2 = draw_custom_cell(anode, cathode)
st.pyplot(fig2)
