# создать список студентов отлженно

lst = [
        'Fedya Petrov',
        'Vasya Holodov',
        'Gosha Pupkin',
        'Stas Bubkin',
        ]

gen = (stud for stud in lst)

print(next(gen))
print(next(gen))

#exit(0)

for s in (gen):
    print('======')
    print(s)
