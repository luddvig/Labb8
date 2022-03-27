from LinkedQFile import LinkedQ


class Syntaxfel(Exception):
    """Klass för fel"""
    pass


def readMolecule(q):
    """Läser molekyl. Max 2 bokstäver, första stor. Molekylnummer minst 2. Ex He2 korrekt."""
    readCap(q)              # Läser första tecknet, kollar om stor bokstav
    if not q.isEmpty():
        readSmall(q)        # Läser andra tecknet, kollar om liten bokstav
    if not q.isEmpty():
        readNum(q)          # Läser molekylnummer


def readCap(q):
    """Läser bokstav, dequeue om stor, annars raise Syntaxfel."""
    letter = q.peek()
    if letter.isupper():
        q.dequeue()
        return
    raise Syntaxfel("Saknad stor bokstav vid radslutet" + " " + str(q))


def readSmall(q):
    """Läser bokstav, dequeue om liten."""
    letter = q.peek()
    if letter.islower():
        q.dequeue()
        return


def readNum(q):
    """Läser nummer för molekyluppsättning av atom, måste vara större än 1, ex H2."""
    num = q.peek()
    if num.isnumeric():             # Kollar om siffra
        num = q.dequeue()
        if num == "0":
            raise Syntaxfel("För litet tal vid radslutet" + " " + str(q))
        if num == "1" and q.isEmpty():
            raise Syntaxfel("För litet tal vid radslutet" + " " + str(q))
        return


def checkMoleculeSyntax(molecule):
    """Kontrollerar om angiven molekyl följer syntax."""
    q = storeMolecule(molecule)
    try:
        readMolecule(q)
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as error:                      # Fångar fel i syntax
        return str(error)                           # Skriver ut  fel


def storeMolecule(molecule):
    """Hjälpfuntion för att lägga in molekylnamn i kö."""
    q = LinkedQ()
    variables = [i for i in molecule]
    for var in variables:
        q.enqueue(var)
    return q


def main():
    while True:
        uinput = input()
        if uinput == "#":
            break
        print(checkMoleculeSyntax(uinput))


if __name__ == "__main__":
    main()