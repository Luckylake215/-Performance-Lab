import sys

def Task1(n, m):
    path = []
    current = 0
    while True:
        path.append(current + 1)
        current = (current + m - 1) % n
        if current == 0:
            break
    return path

def main():
    if len(sys.argv) != 5:
        print("Введите: python task1.py n1 m1 n2 m2")
        return
    n1, m1, n2, m2 = map(int, sys.argv[1:])
    path1 = Task1(n1, m1)
    path2 = Task1(n2, m2)
    combined_path = path1 + path2
    print(*combined_path, sep="")
if __name__ == "__main__":
    main()
