import numpy as np

def compute_xdist2(xgain, duration=0.2):
    '''
    Tue 18 Feb 2025
    v0.0.1
    Seongyeon Kim

    It's for moving pattern
    Shift calculation

    :param xgain: frames/sec
    :param duration: stimulus duration
    :return: how much distance to move (you can apply this value in your code)
    '''
    dt = 0.0001
    t = np.arange(0, duration+dt, dt) - 0.0025
    vel = 1.0/(1+np.exp(-(t-0.022)*105)) - 1.0/(1+np.exp(-(t-0.082)*51.5))
    vel = vel - vel[0]
    vel[vel < 0] = 0
    if np.max(vel)-np.min(vel) != 0:
        vel = (vel - np.min(vel))/(np.max(vel)-np.min(vel))
    xpos = np.cumsum(vel)
    if np.max(xpos) != 0:
        xpos = xpos / np.max(xpos)
    if len(xpos) > 800:
        xpos = xpos[100:-700]
    num_interp = int(round(duration*xgain + 1))
    xdist = np.interp(np.linspace(0, len(xpos)-1, num_interp),
                      np.arange(len(xpos)), xpos)
    xdist = (xdist - xdist[0])/(xdist[-1]-xdist[0] + 1e-9)
    diffs = np.diff(xdist)
    if len(diffs) > 0 and np.max(diffs)!=0:
        xdist = xdist/np.max(diffs)
    xdist = xdist/xdist[-1]*round(xdist[-1])
    xdist2 = xdist * 2
    return xdist2


def generate_looming(pat, stim_onset_idx, nFrames, loom_frames, center_x, center_y, r_interp_array, arenaheight, arenawidth, bright=False, maxPixelIntensity=15):
    '''
    Tue 18 Feb 2025
    v0.0.1
    Seongyeon Kim

    Basic code for generating looming patterns

    :param pat: your new pattern data
    :param stim_onset_idx: stimulus onset index
    :param nFrames: total number of frames
    :param loom_frames: stimulus frames
    :param center_x: looming centre x
    :param center_y: looming centre y
    :param r_interp_array: to control looming size
    :param arenaheight: height of the arena
    :param arenawidth: width of the arena
    :param bright:
    :param maxPixelIntensity:
    :return:
    '''
    for i in range(0, stim_onset_idx):
        pat[:, :, i] = pat[:, :, 64]
    # Looming period: draw circle
    for i in range(stim_onset_idx, stim_onset_idx + loom_frames):
        loom_idx = i - stim_onset_idx
        for j in range(arenaheight):
            for k in range(arenawidth):
                r_pixel = np.sqrt((k+1 - center_x)**2 + (j+1 - center_y)**2)
                if r_pixel <= r_interp_array[loom_idx]:
                    pat[j, k, i] = maxPixelIntensity if bright else 0
    # Hold final looming frame
    final_frame = stim_onset_idx + loom_frames - 1
    for i in range(stim_onset_idx + loom_frames, nFrames):
        pat[:, :, i] = pat[:, :, final_frame]
    return pat
