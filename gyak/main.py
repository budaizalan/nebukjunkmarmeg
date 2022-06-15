import random


def szakasz(hőmérséklet: list[int]) -> int:
    aktuális: int = 0
    maxhossz: int = 0
    for h in hőmérséklet:
        if h < 0:
            aktuális += 1
        else:
            if aktuális >= maxhossz:
                maxhossz = aktuális
            aktuális = 0
    if aktuális > maxhossz:
        maxhossz = aktuális
    return maxhossz


def main() -> None:
    hőmérséklet: list[int] = []
    for _ in range(0, 24):
        hőmérséklet.append(random.randint(-10, 5))
    print(hőmérséklet)
    print(szakasz(hőmérséklet))


if __name__ == "__main__":
    main()
