from math import sin, cos, radians

def setup(setup_file):
    settings = []

    for i in range(2):
        setup_file.readline()
        setup_file.readline()
        for j in range(4):
            line = setup_file.readline()
            settings.append(int((line.split())[-1]))
        setup_file.readline()

    return settings

def x_change(cur_x, angle, dist):
    return cur_x + dist * sin(radians(angle))

def y_change(cur_y, angle, dist):
    return cur_y + dist * cos(radians(angle))

def round_coord(coord, limit):
    coord = round(coord)
    if (coord < 0):
        coord += 5 * limit
    coord %= limit
    return coord

def get_line(x_old, y_old, x_new, y_new, x_len, y_len):
    swapped = 0

    if x_new < x_old:
        x_new, x_old = x_old, x_new
        swapped += 1
    if y_new < y_old:
        y_new, y_old = y_old, y_new
        swapped += 1

    delta_x = x_new - x_old
    delta_y = y_new - y_old

    reversed = False
    if delta_x < delta_y:
        reversed = True
        delta_x, delta_y = delta_y, delta_x
        x_new, y_new = y_new, x_new
        x_old, y_old = y_old, x_old
        x_len, y_len = y_len, x_len

    answer = []

    for x in range(x_old, x_new + 1):
        answer.append([round_coord(x, x_len), round_coord(y_old + ((x - x_old) / delta_x) * delta_y, y_len)])

    if reversed:
        for pair in answer:
            pair[0], pair[1] = pair[1], pair[0]

    if swapped == 1:
        for i in range(0, len(answer) // 2 + 1):
            answer[i][1], answer[len(answer) - i - 1][1] = answer[len(answer) - i - 1][1], answer[i][1]

    return answer