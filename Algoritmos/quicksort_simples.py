def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


print(
    quick_sort(
        [
            391,
            290,
            796,
            685,
            548,
            396,
            603,
            801,
            816,
            642,
            960,
            86,
            488,
            28,
            179,
            941,
            438,
            686,
            452,
            182,
            767,
            376,
            322,
            619,
            849,
            730,
            516,
            289,
            390,
            331,
            740,
            942,
            550,
            727,
            551,
            55,
            789,
            51,
            862,
            104,
            791,
            959,
            425,
            224,
            221,
            413,
            319,
            314,
            892,
            356,
            307,
            288,
            874,
            141,
            357,
            721,
            972,
            249,
            120,
            183,
            920,
            858,
            425,
            280,
            390,
            31,
            277,
            360,
            391,
            426,
            661,
            312,
            182,
            966,
            501,
            145,
            659,
            466,
            429,
            377,
            675,
            53,
            643,
            260,
            440,
            12,
            269,
            226,
            224,
            816,
            613,
            713,
            661,
            335,
            586,
            458,
            525,
            624,
            484,
            708,
        ]
    )
)
