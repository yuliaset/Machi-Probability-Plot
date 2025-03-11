Win Probability in Riichi Mahjong
This document explains the mathematical deduction of the formulas used to calculate the probability that a player eventually wins by drawing a winning tile from the wall under the following assumptions:

Wall: There are 
𝑅
R tiles remaining.
Winning Tiles: 
𝑛
n copies of the winning tile are still available.
Cycle: A “cycle” (or turn) consists of:
Player's Draw: You draw one tile. You win immediately if you draw one of the 
𝑛
n winning tiles, with probability
𝑛
𝑅
.
R
n
​
 .
Opponents' Draws: If you do not win, three opponents each draw one tile from the remaining 
𝑅
−
1
R−1 tiles. The probability that all three opponents miss (i.e. none of them draws a winning tile) is given by the hypergeometric probability:
(
𝑅
−
1
−
𝑛
3
)
(
𝑅
−
1
3
)
.
( 
3
R−1
​
 )
( 
3
R−1−n
​
 )
​
 .
Thus, the probability that no winning tile is drawn in a given cycle is

𝑄
(
𝑅
,
𝑛
)
=
(
1
−
𝑛
𝑅
)
(
𝑅
−
1
−
𝑛
3
)
(
𝑅
−
1
3
)
.
Q(R,n)=(1− 
R
n
​
 ) 
( 
3
R−1
​
 )
( 
3
R−1−n
​
 )
​
 .
Derivation of the Cumulative Win Probability
If the cycle ends with no winning tile being drawn by anyone, the wall decreases by 4 tiles (1 from your draw and 3 from your opponents' draws). Let the cumulative probability that you win within 
𝑘
k cycles be denoted by 
𝑃
𝑘
(
𝑅
,
𝑛
)
P 
k
​
 (R,n).

Probability of Winning in a Single Cycle
Cycle 
𝑖
i:
At the start of cycle 
𝑖
i, the wall has

𝑅
𝑖
=
𝑅
−
4
𝑖
tiles
,
R 
i
​
 =R−4itiles,
and still 
𝑛
n winning tiles remain.
On cycle 
𝑖
i, your probability of drawing a winning tile is

𝑛
𝑅
𝑖
.
R 
i
​
 
n
​
 .
Survival to Cycle 
𝑖
i:
In order to reach cycle 
𝑖
i, no winning tile must have been drawn in all previous cycles. The probability of “surviving” cycle 
𝑗
j is 
𝑄
(
𝑅
−
4
𝑗
,
𝑛
)
Q(R−4j,n). Hence, the probability of reaching cycle 
𝑖
i is

∏
𝑗
=
0
𝑖
−
1
𝑄
(
𝑅
−
4
𝑗
,
𝑛
)
,
j=0
∏
i−1
​
 Q(R−4j,n),
where by convention an empty product (for 
𝑖
=
0
i=0) is taken as 
1
1.

Cumulative Win Probability
The probability that you win on cycle 
𝑖
i is then

(
∏
𝑗
=
0
𝑖
−
1
𝑄
(
𝑅
−
4
𝑗
,
𝑛
)
)
𝑛
𝑅
−
4
𝑖
.
( 
j=0
∏
i−1
​
 Q(R−4j,n)) 
R−4i
n
​
 .
Summing the contributions over the first 
𝑘
k cycles gives:

𝑃
𝑘
(
𝑅
,
𝑛
)
=
∑
𝑖
=
0
𝑘
−
1
(
∏
𝑗
=
0
𝑖
−
1
𝑄
(
𝑅
−
4
𝑗
,
𝑛
)
)
𝑛
𝑅
−
4
𝑖
,
P 
k
​
 (R,n)= 
i=0
∑
k−1
​
 ( 
j=0
∏
i−1
​
 Q(R−4j,n)) 
R−4i
n
​
 ,
​
 
where

𝑄
(
𝑅
−
4
𝑗
,
𝑛
)
=
(
1
−
𝑛
𝑅
−
4
𝑗
)
(
(
𝑅
−
4
𝑗
)
−
1
−
𝑛
3
)
(
(
𝑅
−
4
𝑗
)
−
1
3
)
.
Q(R−4j,n)=(1− 
R−4j
n
​
 ) 
( 
3
(R−4j)−1
​
 )
( 
3
(R−4j)−1−n
​
 )
​
 .
Example: 
𝑅
=
70
R=70 and 
𝑛
=
8
n=8
Let’s work through the first few cycles:

Cycle 0 (
𝑖
=
0
i=0):
Wall: 
𝑅
0
=
70
R 
0
​
 =70
Player's win probability:
8
70
≈
0.1143.
70
8
​
 ≈0.1143.
Contribution:
Since no previous cycle exists, the contribution is 
0.1143
0.1143.
Cycle 1 (
𝑖
=
1
i=1):
Wall: 
𝑅
1
=
70
−
4
=
66
R 
1
​
 =70−4=66
Player's win probability:
8
66
≈
0.1212.
66
8
​
 ≈0.1212.
Opponents' Draws (Cycle 0):
The probability that no winning tile is drawn in cycle 0 is:
𝑄
(
70
,
8
)
=
(
1
−
8
70
)
(
69
−
8
3
)
(
69
3
)
Q(70,8)=(1− 
70
8
​
 ) 
( 
3
69
​
 )
( 
3
69−8
​
 )
​
 
where
(
61
3
)
≈
35990
,
(
69
3
)
≈
52394.
( 
3
61
​
 )≈35990,( 
3
69
​
 )≈52394.
Thus,
𝑄
(
70
,
8
)
≈
62
70
×
35990
52394
≈
0.8857
×
0.687
≈
0.608.
Q(70,8)≈ 
70
62
​
 × 
52394
35990
​
 ≈0.8857×0.687≈0.608.
Contribution for Cycle 1:
0.608
×
0.1212
≈
0.0737.
0.608×0.1212≈0.0737.
Cycle 2 (
𝑖
=
2
i=2):
Wall: 
𝑅
2
=
70
−
8
=
62
R 
2
​
 =70−8=62
Player's win probability:
8
62
≈
0.1290.
62
8
​
 ≈0.1290.
Cumulative Survival to Cycle 2:
From cycles 0 and 1, survival probability is:
𝑄
(
70
,
8
)
×
𝑄
(
66
,
8
)
(say 
0.608
×
0.587
≈
0.357
)
.
Q(70,8)×Q(66,8)(say 0.608×0.587≈0.357).
Contribution for Cycle 2:
0.357
×
0.1290
≈
0.0461.
0.357×0.1290≈0.0461.
Cumulative Probability
Summing the contributions:

𝑃
3
(
70
,
8
)
≈
0.1143
+
0.0737
+
0.0461
≈
0.2341.
P 
3
​
 (70,8)≈0.1143+0.0737+0.0461≈0.2341.
Continuing in this manner for more cycles (up to the maximum 
𝑘
≈
⌊
70
/
4
⌋
=
17
k≈⌊70/4⌋=17) shows that the cumulative win probability converges to approximately 29.6%.
