# Remove duplciate chareaters from a given string keeping only the first occurences mainitaining the order. For example if th einput is bananas the output would be 'bans'

def remove_duplicates_from_string(input: str):
    counts = set()
    new_string = ""
    for i in input:
        if not i in counts:
            counts.add(i)
            new_string += i
    return new_string


remove_duplicates_from_string('bananas')