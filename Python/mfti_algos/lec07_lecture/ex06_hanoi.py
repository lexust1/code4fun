# Ханоский башни при помощи рекурсии, О(n^2).
def hanoi(n, source, target, auxiliary):
    """Hanoi algo."""
    if n > 0:
        # Перекладываем диск с исходной башни на вспомогательную.
        hanoi(n-1, source, auxiliary, target)
        print(f"Перемещение диска {n} с {source} на {target}.")
        # Перекладываем диск с вспомогательное башни на целевую.
        hanoi(n-1, auxiliary, target, source)


def main():
    # A number of disks.
    n = 5
    hanoi(n, "1st tower", "2nd tower", "3rd tower")


if __name__ == "__main__":
    main()