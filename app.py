def draw_cell_diagram(cell_type):
    fig, ax = plt.subplots(figsize=(8,5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis('off')

    # 용액 (연파랑 배경)
    ax.add_patch(patches.Rectangle((0.5,1), 3,3, color='#d0e7f9', alpha=0.5))
    ax.add_patch(patches.Rectangle((6.5,1), 3,3, color='#d0e7f9', alpha=0.5))

    # 전극
    ax.add_patch(patches.Rectangle((0.9,1),0.3,3, color='gray')) # Zn
    ax.add_patch(patches.Rectangle((8.8,1),0.3,3, color='orange')) # Cu

    ax.text(0.6,4.2,"Zn 전극(-)", fontsize=10)
    ax.text(8.3,4.2,"Cu 전극(+)", fontsize=10)

    # 전자 흐름
    ax.arrow(3.5,3.5,2.8,0, head_width=0.2, head_length=0.3, fc='blue', ec='blue', linewidth=2)
    ax.text(5,3.7,"전자 흐름", fontsize=10, color='blue')

    if cell_type == "다니엘 전지":
        # 이온
        ax.add_patch(patches.Circle((2,2.5),0.2,color='purple'))
        ax.text(1.8,2.1,"Zn²⁺", fontsize=9)
        ax.add_patch(patches.Circle((8,2.5),0.2,color='pink'))
        ax.text(7.8,2.1,"Cu²⁺", fontsize=9)

        # 염다리 추가 (두 용액 사이에 관 형태로 표현)
        ax.add_patch(patches.Rectangle((4.7,1.8), 0.6, 1.4, color='#f0e68c', alpha=0.7))
        ax.text(4.75,3.3, "염다리", fontsize=9, color='green')

        # 설명
        ax.text(1,0.5,"Zn → Zn²⁺ + 2e⁻ (산화)", fontsize=10)
        ax.text(6.5,0.5,"Cu²⁺ + 2e⁻ → Cu (환원)", fontsize=10)
        ax.text(4,4.6,"염다리: Na⁺, Cl⁻ 이동", fontsize=10, color='green')

    elif cell_type == "볼타 전지":
        # 이온
        ax.add_patch(patches.Circle((2,2.5),0.2,color='purple'))
        ax.text(1.8,2.1,"Zn²⁺", fontsize=9)
        ax.add_patch(patches.Circle((8,2.5),0.2,color='pink'))
        ax.text(7.8,2.1,"H⁺", fontsize=9)

        # 기체 기포
        ax.add_patch(patches.Circle((8.5,3.3),0.1,color='gray'))
        ax.add_patch(patches.Circle((8.7,3.5),0.1,color='gray'))

        # 설명
        ax.text(1,0.5,"Zn + H⁺ → Zn²⁺ + H₂↑ (산화)", fontsize=10)
        ax.text(6.5,0.5,"2H⁺ + 2e⁻ → H₂ (환원)", fontsize=10)
        ax.text(4,4.6,"묽은 H₂SO₄ 내 H⁺", fontsize=10, color='green')

        # 염다리 없음 (따로 그림 없음)

    return fig
