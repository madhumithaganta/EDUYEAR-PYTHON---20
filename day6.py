str="a,e,i,o,u"
word='natalia'
for i in word:
    if i in str:
        print(word.index(i))






string='hello my dear chulbuli chokie'
split_string=string.split(' ')
reversed_string=reversed(split_string)
final_string=' '.join(reversed_string)
print(final_string)



a=[1,3,3,5,7,8,8,9]
l=[]
for x in a:
    if x not in l:
        l.append(x)
        print(l)

        
