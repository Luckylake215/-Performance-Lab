import sys
def task1(n, m):
    path = []
    current_position = 0
    while True:
        path.append((current_position % n) + 1)
        current_position += m
        if current_position % n == 0:
            break
    return path

def main():
    if len(sys.argv) != 5:
        print("Неверное количество!")
        return
    n1 = int(sys.argv[1])
    m1 = int(sys.argv[2])
    n2 = int(sys.argv[3])
    m2 = int(sys.argv[4])
    path1 = task1(n1, m1)
    path2 = task1(n2, m2)
    result = path1 + path2
    print(''.join(map(str, result)))
if __name__ == "__main__":
    main()