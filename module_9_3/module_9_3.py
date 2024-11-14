

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(i)-len(j) for i,j in zip(first, second) if len(i)!=len(j))

second_result=[]
for i in range(0, len(first)):
        if (len(first[i])==len(second[i])):
            second_result.append(True)
        else:
            second_result.append(False)

second_result = (True if len(first[i])==len(second[i]) else False for i in range(0, len(first)))

print(first_result)
print(list(first_result))

print(second_result)
print(list(second_result))
