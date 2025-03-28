import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def roll_die():
    return random.randint(1, 6)

dice_faces = {
    1: [(0.5, 0.5)],
    2: [(0.2, 0.8), (0.8, 0.2)],
    3: [(0.2, 0.8), (0.5, 0.5), (0.8, 0.2)],
    4: [(0.2, 0.2), (0.8, 0.2), (0.2, 0.8), (0.8, 0.8)],
    5: [(0.2, 0.2), (0.8, 0.2), (0.5, 0.5), (0.2, 0.8), (0.8, 0.8)],
    6: [(0.2, 0.2), (0.8, 0.2), (0.2, 0.5), (0.8, 0.5), (0.2, 0.8), (0.8, 0.8)]
}

def update(frame):
    plt.clf()
    face = roll_die()
    plt.gca().set_xlim(0, 1)
    plt.gca().set_ylim(0, 1)
    plt.gca().set_xticks([])
    plt.gca().set_yticks([])
    plt.gca().set_frame_on(True)
    
    # Draw dice outline
    plt.gca().add_patch(plt.Rectangle((0.1, 0.1), 0.8, 0.8, fill=False, linewidth=2))
    
    # Draw dice pips
    for (x, y) in dice_faces[face]:
        plt.plot(x, y, 'ko', markersize=20)
    
    # Display rolled number
    plt.text(0.5, -0.2, f"Rolled: {face}", fontsize=15, ha='center', va='center')
    
fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=30, interval=1000)
plt.show()
