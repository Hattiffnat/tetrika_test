def appearance(intervals):
    pupil = time_merge(intervals['pupil'])
    tutor = time_merge(intervals['tutor'])

    start_lesson = intervals['lesson'][0]
    end_lesson = intervals['lesson'][1]
    pup_len = len(pupil) - 1
    tut_len = len(tutor) - 1

    time = 0

    pup_ind = 0
    tut_ind = 0
    while pup_ind < pup_len and tut_ind < tut_len:
        start_puple = pupil[pup_ind]
        end_puple = pupil[pup_ind + 1]
        start_tutor = tutor[tut_ind]
        end_tutor = tutor[tut_ind + 1]

        app_start = max(start_puple, start_tutor, start_lesson)
        app_end = min(end_lesson, end_puple, end_tutor)

        if app_start < app_end:
            time += app_end - app_start

        if app_end == end_lesson:
            break

        if app_end == end_tutor:
            tut_ind += 2
        if app_end == end_puple:
            pup_ind += 2

    return time


def sort_intervals(x):
    temp = sorted([(x[i], x[i + 1]) for i in range(0, len(x), 2)], key=lambda y: y[0])
    res = []
    for i in temp:
        res += list(i)

    return res


def time_merge(x):
    arr = sort_intervals(x)
    res = arr[:2]

    for i in range(2, len(arr), 2):
        if res[-1] < arr[i]:
            res.append(arr[i])
            res.append(arr[i+1])
        elif res[-1] >= arr[i]:
            if res[-1] < arr[i+1]:
                res[-1] = arr[i+1]

    return res


tests = [
    {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]


if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
