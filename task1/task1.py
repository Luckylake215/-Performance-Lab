def task1(n, m):
    result = []
    ptr = 0
    
    while True:
        result.append(str(ptr + 1))
        ptr = (ptr + m - 1) % n
        if ptr == 0:
            break
    
    return ''.join(result)

def main():
    try:
        print("Массив 1:")
        n1 = int(input("n = "))
        m1 = int(input("m = "))
        print("\nМассив 2:")
        n2 = int(input("n = "))
        m2 = int(input("m = "))
        path1 = task1(n1, m1)
        path2 = task1(n2, m2)
        combined_path = path1 + path2
        print(f"\nРезультат:")
        print(f"Путь для массива 1 (n={n1}, m={m1}): {path1}")
        print(f"Путь для массива 2 (n={n2}, m={m2}): {path2}")
        print(f"вывод в консоль: {combined_path}")
        
    except ValueError as e:
        print("Ошибка")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()