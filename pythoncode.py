import math

# Öklid mesafesi hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Kullanıcıdan noktaları alma
points = []
n = int(input("Kaç tane nokta gireceksiniz? "))

for _ in range(n):
    x, y = map(float, input("Bir nokta girin (x, y): ").split(","))
    points.append((x, y))

# Mesafelerin saklanacağı liste
distances = []

# Tüm nokta çiftlerini karşılaştırarak mesafeleri hesapla
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        point1 = points[i]
        point2 = points[j]
        distance = euclideanDistance(point1, point2)
        distances.append((point1, point2, distance))

# Eğer mesafeler listesi boşsa, minimum mesafe bulunamaz
if not distances:
    print("Yeterli nokta yok, mesafe hesaplanamadı.")
else:
    # Minimum mesafeyi bul
    min_distance = min(distances, key=lambda x: x[2])
    point1, point2, distance = min_distance
    print(f"Minimum mesafe {point1} ile {point2} arasındadır ve mesafe: {distance:.2f}")

