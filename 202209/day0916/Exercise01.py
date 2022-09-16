# -*- coding:utf-8 -*-
def is_safe(leading_point, with_the_ball, seconds_left):
    score = leading_point - 1
    if with_the_ball:
        score += 0.5
    else:
        score -= 0.5
        if score <= 0:
            score = 0
    score = score ** 2
    if score > seconds_left:
        return True
    return False


print(is_safe(13, False, 240))


