def main() -> None:
    listaneve: list[fájlnév] = []
    with open('forras.txt', 'r', encoding='utf-8') as file:
        for sor in file.read().splitlines():#[1:]
            listaneve.append(fájlnév(sor))
    print(f'Példák száma: {len(listaneve)}')
    # a for ciklus: Előre meghatározott mennyiségszer fog lefutni
    # lista1: = ['Cucc','dolog','igen','az']

    # while loop: nem meghatározott mennyiségszer





if __name__ == "__main__":
    main()
