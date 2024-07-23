'''NOTE
Given data:

Day      | Season | Fog   | Rain  | Class
-----------------------------------------
Weekday  | Spring | None  | None  | On Time
Weekday  | Winter | None  | Slight| On Time
Weekday  | Winter | None  | None  | On Time
Holiday  | Winter | High  | Slight| Late
Saturday | Summer | Normal| None  | On Time
Weekday  | Autumn | Normal| None  | Very Late
Holiday  | Summer | High  | Slight| On Time
Sunday   | Summer | Normal| None  | On Time
Weekday  | Winter | High  | Heavy | Very Late
Weekday  | Summer | None  | Slight| On Time
Saturday | Spring | High  | Heavy | Cancelled
Weekday  | Summer | High  | Slight| On Time
Weekday  | Winter | Normal| None  | Late
Weekday  | Summer | High  | None  | On Time
Weekday  | Winter | Normal| Heavy | Very Late
Saturday | Autumn | High  | Slight| On Time
Weekday  | Autumn | None  | Heavy | On Time
Holiday  | Spring | Normal| Slight| On Time
Weekday  | Spring | Normal| None  | On Time
Weekday  | Spring | Normal| Heavy | On Time

For "Class = On Time"

Attribute     Value      Count   Likelihood
-------------------------------------------
Day           Weekday    9       9/14 
              Holiday    2       2/14
              Saturday   2       2/14 
              Sunday     1       1/14 

Season        Spring     4       4/14 
              Winter     2       2/14 
              Summer     6       5/14 
              Autumn     2       2/14 

Fog           None       5       5/14 
              High       4       4/14 
              Normal     5       5/14

Rain          None       6       6/14 
              Slight     6       6/14 
              Heavy      2       2/14 

For "Class = Late"

Attribute     Value      Count   Likelihood
-------------------------------------------
Day           Weekday    1       1/2 
              Holiday    1       1/2
              Saturday   0       0/2 
              Sunday     0       0/2

Season        Spring     0       0/2
              Winter     2       2/2 
              Summer     0       0/2 
              Autumn     0       0/2 

Fog           None       0       0/2 
              High       1       1/2
              Normal     1       1/2 

Rain          Slight     1       1/2 
              None       1       1/2 
              Heavy      0       0/2 

For "Class = Very Late"

Attribute     Value      Count   Likelihood
-------------------------------------------
Day           Weekday    3       3/3 
              Holiday    0       0/3
              Saturday   0       0/3
              Sunday     0       0/3

Season        Spring     0       0/3
              Winter     2       2/3 
              Summer     0       0/3 
              Autumn     1       1/3 

Fog           None       0       0/3 
              High       1       1/3
              Normal     2       2/3 

Rain          Slight     0       0/3 
              None       1       1/3 
              Heavy      2       2/3 

For "Class = Cancelled"

Attribute     Value      Count   Likelihood
-------------------------------------------
Day           Weekday    0       0/1
              Holiday    0       0/1
              Saturday   1       1/1 
              Sunday     0       0/1 

Season        Spring     1       1/1
              Winter     0       0/1 
              Summer     0       0/1 
              Autumn     0       0/1

Fog           None       0       0/1
              High       1       1/1
              Normal     0       0/1 

Rain          Slight     0       0/1 
              None       0       0/1 
              Heavy      1       1/1 

Given:
X = (Day=Weekday, Season=Winter, Fog=High, Rain=Heavy)

Using Naive Bayes to calculate:

P(Class = On Time | X) ∝ P(Day=Weekday | Class=On Time) *
                         P(Season=Winter | Class=On Time) *
                         P(Fog=High | Class=On Time) *
                         P(Rain=Heavy | Class=On Time) *
                         P(Class=On Time)

P(Class = On Time | X) ∝ 9/14 * 2/14 * 4/14 * 2/14 * (14/20) = 0.0026

P(Class = Late | X) ∝ P(Day=Weekday | Class=Late) *
                      P(Season=Winter | Class=Late) *
                      P(Fog=High | Class=Late) *
                      P(Rain=Heavy | Class=Late) *
                      P(Class=Late)

P(Class = Late | X) ∝ 1/2 * 2/2 * 1/2 * 0/2 * (2/20) = 0.0

P(Class = Very Late | X) ∝ P(Day=Weekday | Class=Very Late) *
                           P(Season=Winter | Class=Very Late) *
                           P(Fog=High | Class=Very Late) *
                           P(Rain=Heavy | Class=Very Late) *
                           P(Class=Very Late)

P(Class = Very Late | X) ∝ 3/3 * 2/3 * 1/3 * 2/3 * (3/20) = 0.0222

P(Class = Cancelled | X) ∝ P(Day=Weekday | Class=Cancelled) *
                           P(Season=Winter | Class=Cancelled) *
                           P(Fog=High | Class=Cancelled) *
                           P(Rain=Heavy | Class=Cancelled) *
                           P(Class=Cancelled)

P(Class = Cancelled | X) ∝ 0/1 * 0/1 * 1/1 * 1/1 * (1/20) = 0.0


When event X occurs, the label of "Class" will be:
"Class" = "Very Late"
'''
