import sys

def read_ellipse_data(file_path):
    try:
        with open(file_path, "r") as file:
            center = file.readline().strip().split()
            axes = file.readline().strip().split()
            if len(center) != 2 or len(axes) != 2:
                raise ValueError(
                    "Файл с эллипсом должен содержать две строки: координаты центра и полуоси"
                )
            cx, cy = map(float, center)
            a, b = map(float, axes)
            for value in [cx, cy, a, b]:
                if abs(value) > 1e38 or (abs(value) < 1e-38 and value != 0):
                    raise ValueError(
                        f"Число {value} выходит за допустимый диапазон.")
            if a <= 0 or b <= 0:
                raise ValueError("Полуоси a и b должны быть положительными числами.")
            return cx, cy, a, b
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)

def read_points_data(file_path):
    try:
        points = []
        with open(file_path, "r") as file:
            for line in file:
                data = line.strip().split()
                if len(data) != 2:
                    raise ValueError(
                        "Каждая строка файла с точками должна содержать 2 числа"
                    )
                x, y = map(float, data)
                if (abs(x) > 1e38 or (abs(x) < 1e-38 and x != 0) or 
                    abs(y) > 1e38 or (abs(y) < 1e-38 and y != 0)):
                    raise ValueError(
                        f"Координаты ({x}, {y}) выходят за допустимый диапазон"
                    )
                points.append((x, y))
        if (len(points) < 1) or (len(points) >= 100):
            raise ValueError("Количество точек должно быть от 1 до 100.")
        return points
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)

def point_position_relative_to_ellipse(cx, cy, a, b, x, y):
    value = ((x - cx) ** 2) / (a**2) + ((y - cy) ** 2) / (b**2)
    if abs(value - 1) < 1e-10:
        return 0
    elif value < 1:
        return 1
    else:
        return 2

def main():
    if len(sys.argv) != 3:
        print("Использование: python script.py <файл_эллипса> <файл_точек>")
        sys.exit(1)
    
    ellipse_file = sys.argv[1]
    points_file = sys.argv[2]
    
    cx, cy, a, b = read_ellipse_data(ellipse_file)
    points = read_points_data(points_file)
    
    results = []
    for x, y in points:
        position = point_position_relative_to_ellipse(cx, cy, a, b, x, y)
        results.append(position)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()