from src.constants import round_coord, x_change, y_change, get_line
from random import random

class Agent:
    def __init__(self, speed, angle_turn, angle_detect, dist_detect, start_x, start_y, start_dir):
        self.speed = speed
        self.angle_turn = angle_turn
        self.angle_detect = angle_detect
        self.dist_detect = dist_detect
        self.x_pos = start_x
        self.y_pos = start_y
        self.direction = start_dir

    def update_detectors(self, x_len, y_len):
        self.left_detector_direction = self.direction - self.angle_detect
        self.right_detector_direction = self.direction + self.angle_detect

        self.left_detector_x = round_coord(x_change(self.x_pos, self.left_detector_direction, self.dist_detect), x_len)
        self.left_detector_y = round_coord(y_change(self.y_pos, self.left_detector_direction, self.dist_detect), y_len)
        self.center_detector_x = round_coord(x_change(self.x_pos, self.direction, self.dist_detect), x_len)
        self.center_detector_y = round_coord(y_change(self.y_pos, self.direction, self.dist_detect), y_len)
        self.right_detector_x = round_coord(x_change(self.x_pos, self.right_detector_direction, self.dist_detect), x_len)
        self.right_detector_y = round_coord(y_change(self.y_pos, self.right_detector_direction, self.dist_detect), y_len)

    def wagging(self):
        if random() < 0.3:
            self.direction += (random() - 0.5) * self.angle_turn

    def change_way(self, matrix, x_len, y_len):
        self.update_detectors(x_len, y_len)
        left = matrix[self.left_detector_x, self.left_detector_y]
        center = matrix[self.center_detector_x, self.center_detector_y]
        right = matrix[self.right_detector_x, self.right_detector_y]

        if center >= left and center >= right:
            pass
        elif left >= right:
            self.direction = self.direction - self.angle_turn
        else:
            self.direction = self.direction + self.angle_turn

        self.wagging()

    def make_blob(self, matrix, x, y, value, blob_size, x_len, y_len):
        matrix[x][y] += value

        for dist in range(1, blob_size):
            for x_shift in range(0, dist + 1):
                y_shift = dist - x_shift

                change = value // dist
                matrix[round_coord(x + x_shift, x_len)][round_coord(y + y_shift, y_len)] += change
                matrix[round_coord(x + x_shift, x_len)][round_coord(y - y_shift, y_len)] += change
                matrix[round_coord(x - x_shift, x_len)][round_coord(y + y_shift, y_len)] += change
                matrix[round_coord(x - x_shift, x_len)][round_coord(y - y_shift, y_len)] += change

    def update(self, matrix, x_len, y_len):
        self.change_way(matrix, x_len, y_len)

        x_new = int(round(x_change(self.x_pos, self.direction, self.speed), x_len))
        y_new = int(round(y_change(self.y_pos, self.direction, self.speed), y_len))

        affected_line = get_line(self.x_pos, self.y_pos, x_new, y_new, x_len, y_len)
        for pair in affected_line:
            self.make_blob(matrix, pair[0], pair[1], 60, 13, x_len, y_len)

        self.x_pos = round_coord(x_new, x_len)
        self.y_pos = round_coord(y_new, y_len)
