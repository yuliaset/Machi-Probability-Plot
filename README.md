# Win Probability in Riichi Mahjong

This document explains the mathematical deduction of the formulas used to calculate the probability that **you** eventually win by drawing a winning tile in a Riichi Mahjong scenario. The model considers the following:

- **Wall:** There are \( R \) tiles remaining.
- **Winning Tiles:** \( n \) copies of the winning tile are still available.
- **Cycle:** A “cycle” (or turn) consists of:
  - **Your Draw:** You draw one tile.
  - **Opponents' Draws:** Three opponents each draw one tile.

The goal is to compute the cumulative probability that you win (i.e., that you draw the winning tile on your turn) over multiple cycles.

## Mathematical Derivation

### 1. Single Cycle

At the beginning of a cycle:
- There are \( R \) tiles remaining.
- There are \( n \) winning tiles available.

#### Your Draw

The probability that you draw a winning tile is:
\[
\frac{n}{R}.
\]

#### Opponents' Draws

If you **do not** draw a winning tile (with probability \( 1 - \frac{n}{R} \)), the three opponents each draw one tile from the remaining \( R - 1 \) tiles. The probability that **none** of them draws a winning tile is given by the hypergeometric probability:
\[
\frac{\binom{R-1-n}{3}}{\binom{R-1}{3}}.
\]

Thus, the probability that **no winning tile is drawn** in a given cycle is:
\[
Q(R, n) = \left(1 - \frac{n}{R}\right) \frac{\binom{R-1-n}{3}}{\binom{R-1}{3}}.
\]

### 2. Cumulative Win Probability Over \( k \) Cycles

After each cycle, if no winning tile is drawn by anyone, the wall decreases by 4 tiles (1 by you and 3 by the opponents). Denote the state at cycle \( i \) by:
\[
R_i = R - 4i.
\]
At cycle \( i \), the probability that you win on your draw is:
\[
\frac{n}{R_i} = \frac{n}{R - 4i}.
\]

To reach cycle \( i \), no winning tile must have been drawn in all previous cycles. The probability of surviving (i.e., reaching cycle \( i \)) is:
\[
\prod_{j=0}^{i-1} Q(R-4j, n).
\]

Thus, the probability that you win **in cycle \( i \)** is:
\[
\left(\prod_{j=0}^{i-1} Q(R-4j, n)\right) \frac{n}{R-4i}.
\]

Summing the contributions from cycles \( 0 \) to \( k-1 \), the cumulative win probability is:
\[
\boxed{P_k(R,n)=\sum_{i=0}^{k-1}\left(\prod_{j=0}^{i-1} Q(R-4j,n)\right)\frac{n}{R-4i},}
\]
where
\[
Q(R-4j, n)=\left(1-\frac{n}{R-4j}\right)\frac{\binom{(R-4j)-1-n}{3}}{\binom{(R-4j)-1}{3}}.
\]

## Example: \( R = 70 \) and \( n = 8 \)

Let's work through the first few cycles:

### Cycle 0 (\( i = 0 \))
- **Wall:** \( R_0 = 70 \)
- **Player's win probability:**
  \[
  \frac{8}{70} \approx 0.1143.
  \]
- **Contribution:**  
  \( 0.1143 \) (since there are no previous cycles).

### Cycle 1 (\( i = 1 \))
- **Wall:** \( R_1 = 70 - 4 = 66 \)
- **Player's win probability:**
  \[
  \frac{8}{66} \approx 0.1212.
  \]
- **Probability that Cycle 0 passes:**
  \[
  Q(70,8)=\left(1-\frac{8}{70}\right)\frac{\binom{69-8}{3}}{\binom{69}{3}}.
  \]
  Approximating the combinatorial terms:
  - \(\binom{61}{3} \approx 35990\),
  - \(\binom{69}{3} \approx 52394\),
  
  we get:
  \[
  Q(70,8) \approx \frac{62}{70} \times \frac{35990}{52394} \approx 0.8857 \times 0.687 \approx 0.608.
  \]
- **Contribution for Cycle 1:**
  \[
  0.608 \times 0.1212 \approx 0.0737.
  \]

### Cycle 2 (\( i = 2 \))
- **Wall:** \( R_2 = 70 - 8 = 62 \)
- **Player's win probability:**
  \[
  \frac{8}{62} \approx 0.1290.
  \]
- **Cumulative survival probability to Cycle 2:**
  \[
  Q(70,8) \times Q(66,8) \quad (\text{assume } \approx 0.608 \times 0.587 \approx 0.357).
  \]
- **Contribution for Cycle 2:**
  \[
  0.357 \times 0.1290 \approx 0.0461.
  \]

### Cumulative Probability

Summing the contributions from cycles 0, 1, and 2:
\[
P_3(70,8) \approx 0.1143 + 0.0737 + 0.0461 \approx 0.2341.
\]
Continuing this process for up to about 17 cycles (since \(\lfloor 70/4 \rfloor = 17\)) shows that the cumulative win probability converges to approximately **29.6%**.
