import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate_pattern(pat, interval=50):
    """
    Animates a 3D pattern (height, width, nFrames).

    Parameters:
      pat: 3D NumPy array representing the pattern.
      interval: Delay between frames in milliseconds.

    Returns:
      ani: The FuncAnimation object.
    """
    # Create a figure and axis.
    fig, ax = plt.subplots()
    # Display the first frame. Set vmin/vmax according to your data range.
    im = ax.imshow(pat[:, :, 0], cmap='gray', vmin=0, vmax=3)
    ax.set_title("Frame 0")

    # Update function that changes the image for each frame.
    def update(frame):
        im.set_data(pat[:, :, frame])
        ax.set_title(f"Frame {frame}")
        return [im]

    # Create the animation.
    ani = animation.FuncAnimation(fig, update, frames=pat.shape[2],
                                  interval=interval, blit=True)
    plt.show()
    return ani
