import numpy as np

from src.agent import Agent
from src.constants import setup, round_coord
from src.environment import Environment

if __name__ == '__main__':
    setup_file = open("settings.txt", 'r')
    settings = setup(setup_file)
    setup_file.close()

    x_len = settings[0]
    y_len = settings[1]
    evaporation_coeff = settings[2]
    agents_amount = settings[3]

    agents_list = []
    start = np.random.rand(agents_amount, 3)

    speed = settings[4]
    turn = settings[5]
    detectors_rotate = settings[6]
    detectors_dist = settings[7]

    for line in start:
        agents_list.append(Agent(speed, turn, detectors_rotate, detectors_dist, \
                                 round_coord(x_len * line[0], x_len), round_coord(y_len * line[1], y_len), \
                                 round(int(360 * line[2]))))

    Environment(x_len, y_len, evaporation_coeff, agents_list)
