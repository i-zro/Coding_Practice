from collections import deque

n, k = map(int,input().split())
num_arr = list(input().split())
q = list([["".join(num_arr)]])
print(q)
# ans=-1
# while(q):
#     word,cnt=q.popleft()
#     tempL=list(word)
#     #print(tempL,cnt)
#
#     # 오름차순이면 그만
#     if tempL==sorted(tempL):
#         ans=cnt
#         break
#
#     isFirst=False
#     # i를 뒤집기
#     for i in range(N-K+1):
#         newL = list(tempL)
#         targetL=newL[i:i+K]
#         targetL.reverse()
#         for j in range(K):
#             newL[i+j]=targetL[j]
#         newWord="".join(newL)
#         if newWord not in visitedS:
#             visitedS.add(newWord)
#             q.append([newWord,cnt+1])
#
# print(ans)