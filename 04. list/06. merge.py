lang1 = ["C","C++","JAVA"]
lang2 = ["Python", "Go", "C#"]

langs = lang1+lang2
print(langs)


"""
C#에서 합치는 것 처럼
expected: c c++ java p go c#
real: ['C', 'C++', 'JAVA', 'Python', 'Go', 'C#']

"""
