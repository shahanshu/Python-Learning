dict={
    12:23,
    22:45,
    56:45
}
dict2={
    44:56,
    66:45,
    34:66
}
dict.update(dict2)
print(dict)
# dict.pop(12)
del dict[66]

print(dict)