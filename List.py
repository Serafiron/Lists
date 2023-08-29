# a standard list and how it's printed
txt = ["a", "b", "c"]
print(txt)
print()

# a list without the brackets, with a standard separator
txt2 = ["One", "Two", "Three"]
print(*txt2)
print("\n")

# a list where the separator describes a continuum, or just looks cool
txt3 = ["Concept", "Planning", "Implementation", "Review", "Release"]
print("Five Stages Of An Agile Development Cycle")
print(*txt3, sep=" --> ")