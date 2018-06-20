"""
Complete the solution so that it strips all text that follows any of a set of comment markers passed in.
Any whitespace at the end of the line should also be stripped out.

Given an input string of:
apples, pears # and bananas
grapes
bananas !apples

apples, pears
grapes
bananas

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
"""

def solution(string, markers):

    lines = string.splitlines()

    for index_of_line, line in enumerate(lines):
        temp_string = ''
        for letter in line:
            if letter in markers:
                lines[index_of_line] = temp_string.rstrip()
                # string_whitespace
                break
            temp_string += letter

    return '\n'.join(lines)


print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
