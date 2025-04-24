total = 0
class PointsForPlace:
    points = 0

    @staticmethod
    def get_points_for_place(place):
        points = 0
        if place > 100:
            print('Баллы начисляются только первым 100 участникам.')
        elif place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место.')
        else:
            points = 101 - place
        return points

class PointsForMeters:
    points = 0

    @staticmethod
    def get_points_for_meters(meters):
        points = 0
        if meters < 0:
            print('Количество метров не может быть отрицательным.')
        else:
            points = int(meters * 0.5)
        return points

class TotalPoints(PointsForPlace, PointsForMeters):
    def __init__(self):
        PointsForPlace.__init__(self)
        PointsForMeters.__init__(self)

    def get_points_for_place(self, place):
        v_place = PointsForPlace.get_points_for_place(place)
        global total
        total += v_place
        return v_place

    def get_points_for_meters(self, meters):
        v_meters = PointsForMeters.get_points_for_meters(meters)
        global total
        total += v_meters
        return v_meters

    def get_total_points(self, place, meters):
        v_place = PointsForPlace.get_points_for_place(place)
        v_meters = PointsForMeters.get_points_for_meters(meters)
        global total
        total += v_place
        total += v_meters
        return total



points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))