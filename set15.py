import sys
r = {
    'X': 10,
    'V': 5,
    'I': 1
}

def change(ch):
    try:
        return r[ch.upper()]
    except KeyError:
        print(f"error: invalid Roman numeral character '{ch}'\n",
              file=sys.stderr)
        sys.exit(1)

def numeral(s):
    result = 0
    lastValue = sys.maxsize
    for ch in s:
        value = change(ch)
        if value > lastValue:
            result += value - 2 * lastValue
        else:
            result += value
        lastValue = value
    return result

def loop():
    while True:
        try:
            userInput = input("Enter a Roman numeral > ").strip()
            if len(userInput) == 0:
                sys.exit(0)
            intValue = numeral(userInput)
            print(f"{userInput} = {intValue}")
        except EOFError:
            print()
            sys.exit(0)

def main():
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            intValue = numeral(arg)
            print(f"{arg} = {intValue}")
    else:
        loop()

if __name__ == "__main__":
    main()
