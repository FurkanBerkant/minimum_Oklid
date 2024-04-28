from math import sqrt

points = [(1, 2), (3, 4), (5, 6), (7, 8)]
distances = []


def euclidean_distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))


def calculating_distances(point):
    for i in range(len(point) - 1):
        x1, y1 = point[i]
        x2, y2 = point[i + 1]
        distances.insert(i, euclidean_distance(x1, y1, x2, y2))


def minimum_distance(distance):
    return min(distance)


if __name__ == '__main__':
    calculating_distances(points)
    print(minimum_distance(distances))
