# match FIPS code with county name
import re
# input: FIPS code

def fips_match(stringA, stringB):
    # Splitting the strings at "|"
    leftA, rightA = stringA.lower().split("|")
    leftB, rightB = stringB.lower().split("|")

    # Check exact match on the left
    if leftA != leftB:
        return False

    # Check if rightB matches the first 2 to 3 words of rightA
    match_pattern = r'^(' + re.escape(rightB) + r')(\s+\w+){0,2}'
    return bool(re.match(match_pattern, rightA))


# Example usage
stringA = "AK | ALEUTIANS EAST BOROUGH"
stringB = "AK | Aleutians East"
print(fips_match(stringA, stringB)) 


# output: county name
