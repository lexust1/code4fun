# Упражнение №2
# Вывести на экран все элементы множества A, которых нет в множестве B.

A = set('bqlpzlkwehrlulsdhfliuywemrlkjhsdlfjhlzxcovt')
B = set('zmxcvnboaiyerjhbziuxdytvasenbriutsdvinjhgik')
# for x in A:
#     ...


def main():
    print("Элементы A, которых нет в B:", A.difference(B))
    print(f"f in B: {'f' in B}")
    print(f"z in B: {'z' in B}")
    for el in A.difference(B):
        print(f"{el} in B: {el in B}")


if __name__ == "__main__":
    main()
