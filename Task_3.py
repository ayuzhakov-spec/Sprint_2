class PointsForPlace:
    @staticmethod
    def get_points_for_place(place):
        points = 0
        if place == 1:
            points = 100
        elif place == 2:
            points = 90
        return points

class PointsForMeters:
    @staticmethod
    def get_points_for_meters(meters):
        points = 0
        if meters < 0:
            print('Количество метров не может быть отрицательным')
        else:
            points = meters * 0.5
        return points

class TotalPoints(PointsForPlace, PointsForMeters):
    # Добавляем метод, который все суммирует
    def get_total(self, place, meters):
        points_place = self.get_points_for_place(place) 
        points_meters = self.get_points_for_meters(meters)
        return points_place + points_meters



points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_total_points(100, 10)) 