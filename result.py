Name = input('Name: ')
Class = '9th'
print (Class) 
phy= int(input('Physics Marks: '))
chem = int(input('Chemistry Marks:'))
math = int(input('Mathematics Marks:'))
eng = int(input('English Marks:'))
sindhi = int(input('Sindhi Marks:'))
def add(phy,chem,math,eng,sindhi):
    return phy+chem+math+eng+sindhi
total = (add(phy,chem,math,eng,sindhi))
print('Total Matks', '=' ,total)
percent = float((total/500)*100)
print('Percentage', '=' , percent,' % ')
if percent >=80 and percent <100:
    print('Grade = A+')
elif percent  >=70 and percent <80:
    print('Grade = A')
elif percent  >=60 and percent <70:
    print('Grade = B')
elif percent >=50 and percent <60:
    print('Grade = C')
elif percent >=40 and percent <50:
    print('Grade = D')
elif percent <40:
    print('Fail!')
else:
    print('\aSomething is wrong!')                     