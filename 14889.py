from itertools import combinations #조합할 수 있는 경우를 뽑아줌 cf) 순열(순서 있는 조합)은 permutation

N = int(input()) # 총 모인 사람 몇 명인지 입력 
S = [list(map(int, input().split())) for _ in range(N)] #예제 입력에서 0 1 2 3 입력했듯 S 입력해주는 것, 그걸 for _ in range(N) 번 하겠다. 
members = [i for i in range(N)] # i로 리스트를 채우겠다, 그런데 그 i는 뭐냐면 for i in range(N)이다. 만약 N=4라면 0,1,2,3
possible_team = [] # 빈 리스트 만들어주고

#조합으로 가능한 팀 생성해주기
for team in list(combinations(members, N//2)): #만약 members가 [0,1,2,3]이면 2개씩 해서 나올 수 있는 조합 
    possible_team.append(team) # -> possible_team = [(0,1), (0,2), (0,3), (1,2), (1,3), (2,3)]

min_stat_gap = 10000 #갭이 가장 작은 값을 찾기 위하여 큰 수 아무거나 써준 것 
for i in range(len(possible_team)//2): # 아래 team = possible_team[-1-i]랑 같이 봐야함. 앞에서부터, 뒤에서부터 해주는 것
    #A 팀
    team = possible_team[i] # 만약 i=0 이면 지금 team은 -> (0,1) 인 것
    stat_A = 0 #A팀 능력치 # 아래 코드는 능력치 (문제 속 그림에서 각각의 stat)를 구하기 위한 것
    for j in range(N//2): #만약에 N=4면 -> j는 0,1 
        member = team[j] #멤버는 (0,1)에서 또 [j]번째니까 -> 0으로 '고정' (아래 for문 돈 다음에는 또 1로 '고정')
        for k in team: # -> 결국 (0,0), (0,1)... 다 순서 다르게 해주려고 지금 돌리는 것
            stat_A += S[member][k] #능력치 추가

    """
    설명을 더 하자면, 문제에서 특이한게 '모든 쌍의 능력치 Sij의 합이다. Sij는 Sji와 다를 수도 있으며'라는 점임
    그래서 0,1,2
            0,1,2 있으면 [0][1]하고 [1][0] 값이 다를 수도 있기에 for문 두 번 돌려서 9번([0][0], [1][1],[2][2]는 제외해서 6번) 하는 것
    -> 지금 바로 직전의 코드는 이 stat(능력치)의 값을 구하는 코드를 의미함
    """

            
    #A를 제외한 나머지 팀
    team = possible_team[-i-1]
    stat_B = 0
    for j in range(N//2):
        member = team[j]
        for k in team:
            stat_B += S[member][k]
            
    min_stat_gap = min(min_stat_gap, abs(stat_A - stat_B)) #abs는 절댓값, 위에서 1000은 해줬던 이유. 
    
print(min_stat_gap)