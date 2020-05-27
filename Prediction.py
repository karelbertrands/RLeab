from scipy.stats import norm
import numpy as np
from stable_baselines import ACKTR, A2C, PPO2, ACER

def NewPotential(current_window, algorithm='PPO'):

    # Determine the pretrained agent
    if algorithm == 'A2C':
        model = A2C.load("pretrained_A2C")
    elif algorithm == 'PPO':
        model = PPO2.load("pretrained_PPO")
    elif algorithm == 'ACKTR':
        model = ACKTR.load("pretrained_ACKTR")
    elif algorithm == 'ACER':
        model = ACER.load("pretrained_ACER")
    else:
        raise ValueError("%s is not a valid algorithm." % algorithm)

    if len(current_window) != model.observation_space.shape[0]:
        raise ValueError("%s is does not match the model's window size." % len(current_window))

    action, _states = model.predict(current_window, deterministic=False)

    voltages = np.linspace(0, 1, num=model.action_space.n)
    if action >= 0 and action <= model.action_space.n - 1:
        voltage = voltages[action]
    else:
        raise ValueError("Received invalid action={} which is not part of the action space".format(action))

    return voltage