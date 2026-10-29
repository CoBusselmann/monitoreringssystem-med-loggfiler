import sys

sequence = sys.argv[1:]

def get_user_input(prompt=""):
    if sequence:
        answer = sequence.pop(0)
        print(f"{prompt} {answer}")
        return answer
    return input(prompt)