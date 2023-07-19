l=5
r=555
answer = []
for i in range(l, r+1):
    if all(num in ['0', '5'] for num in str(i)):
        answer.append(i)
            
if len(answer) == 0:
    answer.append(-1)
    
for i in answer:
    print(i)