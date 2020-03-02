import re


class Solution:
    @staticmethod
    def clean(string: str) -> str:
        vow = 'A, E, I, O, U,Y'.replace(',', '|')
        match = F"{vow.lower()}|{vow}"
        print(match)
        return re.sub(F'[{match}]', '', string)


print(Solution.clean("aemiOytrer"))
