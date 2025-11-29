import sys
import statistics


def calc_steps(nums: list[int]):
    median_num = statistics.median(nums)

    total_steps = sum(abs(num - median_num) for num in nums)

    if total_steps > 20:
        return (
            "20 ходов недостаточно для приведения всех элементов массива к одному числу"
        )

    return int(total_steps)


def main():
    """Скрипт для приведения всех элементов массива к одному числу, число определяется
    ближайшим числом к среднему данные для массива находятся в: "data4.txt" """
    if len(sys.argv) != 2:
        print("Напишите: python task4.py <путь к файлу>")
        return

    try:
        with open(sys.argv[1], "r") as f:
            array = list(map(int, f.read().split()))
        print(calc_steps(array))
    except FileNotFoundError:
        print(f"Файл {sys.argv[1]} не найден.")
    except ValueError:
        print("Файл содержит некорректные данные (требуются целые числа).")


if __name__ == "__main__":
    main()
