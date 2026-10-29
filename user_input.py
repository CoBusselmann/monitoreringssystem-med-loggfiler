import sys
#Lista med alla argument som i kommandotolken
sequence = sys.argv[1:]
#input funktion som kollar om det finns argument, samt skriver ut argument. annars returnerar den input från användaren.
def get_user_input(prompt=""):
    if sequence:
        answer = sequence.pop(0)
        print(f"{prompt} {answer}")
        return answer
    return input(prompt)