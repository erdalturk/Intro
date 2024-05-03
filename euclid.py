points = [(3,5), (8,9), (5,4), (1,2), (7,4), (6,8)]
def euclideanDistance(point1, point2):
    x1,y1 = point1
    x2,y2 = point2
    return ((x2-x1)**2) + ((y2-y1)**2)

distances = []

for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

print("Tüm mesafeler: ", (distances))
minDistance = min(distances)
print("En kısa mesafe: ", minDistance)