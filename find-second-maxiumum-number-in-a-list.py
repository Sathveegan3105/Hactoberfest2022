n = int(input())
A = input().split()
runner_up_score = int(min(A))
if n >= 2 and n <= 10:
    if len(A) == n:
        for i in A:
            i = int(i)
            if i >= -100 and i <= 100:
                if i > int(min(A)) and i < int(max(A)):
                    runner_up_score = i
            else:print("Invalid score!")
    else:print("Error in total scores")
else:print("Invalid number of scores")

print(runner_up_score)
                

             
