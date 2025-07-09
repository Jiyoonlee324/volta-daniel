import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

st.title("🔋 전기화학 전지 시각화 (직접 제작 다이어그램)")

# 전지 선택
cell_type = st.radio("전지 종류를 선택하세요:", ["다니엘 전지", "볼타 전지"])

def draw_cell_diagram(cell_type):
    fig, ax = plt.subplots(figsize=(8,5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis('off')

    if cell_type == "다니엘 전지":
        # 왼쪽: ZnSO₄ 수용액, 오른쪽: CuSO₄ 수용액
        ax.add_patch(patches.Rectangle((0.5,1), 3,3, color='#d0e7f9', alpha=0.5))
        ax.add_patch(patches.Rectangle((6.5,1), 3,3, color='#d0e7f9', alpha=0.5))

        # 용액 이름
        ax.text(1.7,4.2,"ZnSO₄ 수용액", fontsize=10)
        ax.text(7.6,4.2,"CuSO₄ 수용액", fontsize=10)

        # 전극
        ax.add_patch(patches.Rectangle((0.9,1),0.3,3, color='gray'))   # Zn 전극(-)
        ax.add_patch(patches.Rectangle((8.8,1),0.3,3, color='orange')) # Cu 전극(+)

        ax.text(0.6,4.5,"Zn 전극(-)", fontsize=10)
        ax.text(8.3,4.5,"Cu 전극(+)", fontsize=10)

        # 염다리
        ax.add_patch(patches.Rectangle((4.6,2), 0.8, 1, color='#f0e68c', alpha=0.8))
        ax.text(4.65,3.1, "염다리", fontsize=9, color='green')

        # 전자 흐름
        ax.arrow(3.5,3.5,2.8,0, head_width=0.2, head_length=0.3, fc='blue', ec='blue', linewidth=2)
        ax.text(5,3.7,"전자 흐름", fontsize=10, color='blue')

        # 이온
        ax.add_patch(patches.Circle((2,2.5),0.2,color='purple'))
        ax.text(1.8,2.1,"Zn²⁺", fontsize=9)
        ax.add_patch(patches.Circle((8,2.5),0.2,color='pink'))
        ax.text(7.8,2.1,"Cu²⁺", fontsize=9)

        # 설명
        ax.text(1,0.5,"Zn → Zn²⁺ + 2e⁻ (산화)", fontsize=10)
        ax.text(6.5,0.5,"Cu²⁺ + 2e⁻ → Cu (환원)", fontsize=10)
        ax.text(4,4.8,"염다리: Na⁺, Cl⁻ 이동", fontsize=10, color='green')

    elif cell_type == "볼타 전지":
        # 하나의 큰 수용액 (묽은 H₂SO₄)
        ax.add_patch(patches.Rectangle((0.5,1), 9,3, color='#d0e7f9', alpha=0.5))

        # 용액 이름
        ax.text(4.2,4.2,"묽은 H₂SO₄ 수용액", fontsize=10)

        # 전극
        ax.add_patch(patches.Rectangle((0.9,1),0.3,3, color='gray'))   # Zn 전극(-)
        ax.add_patch(patches.Rectangle((8.8,1),0.3,3, color='orange')) # Cu 전극(+)

        ax.text(0.6,4.5,"Zn 전극(-)", fontsize=10)
        ax.text(8.3,4.5,"Cu 전극(+)", fontsize=10)

        # 전자 흐름
        ax.arrow(3.5,3.5,2.8,0, head_width=0.2, head_length=0.3, fc='blue', ec='blue', linewidth=2)
        ax.text(5,3.7,"전자 흐름", fontsize=10, color='blue')

        # 이온
        ax.add_patch(patches.Circle((2,2.5),0.2,color='purple'))
        ax.text(1.8,2.1,"Zn²⁺", fontsize=9)
        ax.add_patch(patches.Circle((8,2.5),0.2,color='pink'))
        ax.text(7.8,2.1,"H⁺", fontsize=9)

        # 기체 기포 (H₂ 발생)
        ax.add_patch(patches.Circle((8.5,3.3),0.1,color='gray'))
        ax.add_patch(patches.Circle((8.7,3.5),0.1,color='gray'))

        # 설명
        ax.text(1,0.5,"Zn + H⁺ → Zn²⁺ + H₂↑ (산화)", fontsize=10)
        ax.text(6.5,0.5,"2H⁺ + 2e⁻ → H₂ (환원)", fontsize=10)
        ax.text(4,4.8,"같은 수용액에서 반응", fontsize=10, color='green')

    return fig

# 출력
fig = draw_cell_diagram(cell_type)
st.pyplot(fig)

# 구분선
st.markdown("---")

# 📌 전지 비교 표
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
