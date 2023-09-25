import numpy as np
import math

# Map a value to a new range
def scale_value(value, left_min, left_max, right_min, right_max):
    # x ′ = ( x − x m i n ) / ( x m a x − x m i n )
    # zi = (xi – min(x)) / (max(x) – min(x)) * Q
    left_span = left_max - left_min
    right_span = right_max - right_min
    value_scaled = float(value - left_min) / float(left_span)
    return right_min + (value_scaled * right_span)


def pixel_to_cartesian(coords_dict, mid_w, mid_h):
    for key, value in coords_dict.items():
        # print('~~~', value, key)
        if value[0] <= mid_w and value[1] <= mid_h:
            print('1', value, key)
            x_temp = value[0] - mid_w
            y_temp = mid_h - value[1]

        if value[0] >= mid_w and value[1] <= mid_h:
            print('2', value, key)
            x_temp = value[0] - mid_w
            y_temp = mid_h - value[1]

        if value[0] >= mid_w and value[1] >= mid_h:
            print('3', value, key)
            x_temp = value[0] - mid_w
            y_temp = mid_h - value[1]

        if value[0] <= mid_w and value[1] >= mid_h:
            print('4', value, key)
            x_temp = value[0] - mid_w
            y_temp = mid_h - value[1]

        coords_dict[key][0], coords_dict[key][1] = x_temp, y_temp
    # print('pixel coords', coords_dict)
    return coords_dict

def rotate(coods_dict, angle):
    coord_dict_items = coods_dict.values()
    coords_array = np.array(list(coord_dict_items))
    theta = np.radians(angle)
    new_coord_test = np.array(coords_array)
    mirror = np.array([[math.cos(theta), -math.sin(theta)],
                       [math.sin(theta), math.cos(theta)]]
                      )
    result = mirror.dot(new_coord_test.T).astype(int)

    result = result.T
    rotate_coord_dict = {}
    i = 0
    for value in result:
        rotate_coord_dict[i] = list(value)
        i += 1
    # print('rotated', rotate_coord_dict)
    return rotate_coord_dict

def cartesian_to_pixel(coords_dict, mid_w, mid_h):
    for key, value in coords_dict.items():
        if value[0] <= mid_w and value[1] <= mid_h:
            x_temp = value[0] + mid_w
            y_temp = value[1] - mid_h

        if value[0] >= mid_w and value[1] <= mid_h:
            x_temp = value[0] + mid_w
            y_temp = value[1] - mid_h

        if value[0] >= mid_w and value[1] >= mid_h:
            x_temp = value[0] + mid_w
            y_temp = mid_h + value[1]

        if value[0] <= mid_w and value[1] >= mid_h:
            x_temp = value[0] + mid_w
            y_temp = mid_h + value[1]

        coords_dict[key][0], coords_dict[key][1] = abs(x_temp), abs(y_temp)
    # print('rotated and cartesian', coords_dict)
    return coords_dict