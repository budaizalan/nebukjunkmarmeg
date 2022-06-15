class Ingatlan(object):
    def __init__(self, sor: str):
        m: list[str] = sor.split(' ')
        self.azonosító = int(m[0])
        self.utca = m[1]
        self.házszám = m[2]
        self.kategória = m[3]
        self.terület = int(m[4])


def main() -> None:
    ingatlanok: list[Ingatlan] = []
    with open('utca.txt', 'r', encoding='utf-8') as file:
        for sor in file.read().splitlines()[1:]:
            ingatlanok.append(Ingatlan(sor))
    print(f'Ingatlanok száma: {len(ingatlanok)}')

    tulajdonos: bool = False
    azonosítószám: int = int(input('Tulajdonos azonosító:'))
    for h in ingatlanok:
        if h.azonosító == azonosítószám:
            tulajdonos = True
            break
    print(f'{"Van" if tulajdonos else "Nincs"} ház ezen az azonosító')

    legnagyobb = ingatlanok[0]
    for e in ingatlanok:
        if e.terület > legnagyobb.terület:
            legnagyobb = e
    print(f'\tMax utca: {legnagyobb.utca}\n\tHázszám: {legnagyobb.házszám}')

    with open("akategoria.txt", 'w', encoding='utf-8') as file:
        for h in ingatlanok:
            if h.kategória == 'A':
                file.write(f'\t{h.azonosító}\t{h.utca}\t{h.házszám}\t{h.terület}\n')


if __name__ == "__main__":
    main()
