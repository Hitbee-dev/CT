''' 경수가 내주는 숙제
< 모든 변수는 객체일 것 >

1. N X N 격자가 주어짐
2. 몬스터, 유저 1 개체씩 랜덤 위치에 겹치지 않게 존재 (hp, def, atk)등은 내가 알아서 Custom
3. 각 몬스터, 유저는 (x, y)좌표 및 방향(동, 서, 남, 북)을 가짐
    - 유저는 치명타 확률이 존재함(재밌는 거 있으면 더 추가 해보기)
4. 프로그램 선택지 입력 받음
    - while 돌면서 아래 선택지가 주어짐
        1) 유저 추가(랜덤 위치)
        2) 모든 객체 이동 (각 객체가 바라보는 방향으로 한 칸씩 이동, 벽이면 90도나 180도로 이동)
            - 만약 이동 위치에 적 만날시 공격 (한대 때리고 밀려나든, 뒤질때까지 싸우든 알아서)
            - hp <= 0이 되면 전장 강제 이탈
5. 유저가 다 뒤지거나 몬스터가 다 뒤지면 게임 끝, <누구의 승리인지 보여주고 끝>
'''