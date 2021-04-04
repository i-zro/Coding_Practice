def solution(prices):
    n = len(prices)
    answer = [0] * n
    stk = []

    for i in range(n):

        # 스택 비지 않았을 때 스택 마지막 원소부터 비교해서 빼내기
        while stk and prices[stk[-1]] > prices[i]:
            top = stk.pop()
            answer[top] = i - top

        # 처음원소가 들어갔을 때 일단 stk에 그 시간 저장
        stk.append(i)

    while stk:
        top = stk.pop()
        answer[top] = n-1 - top
    return answer