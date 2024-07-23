'''NOTE:
Given data:

Day |Outlook    |Temperature    |Humidity   |Wind       |PlayTennis

D1  |Sunny      |Hot            |High       |Weak       |No
D2  |Sunny      |Hot            |High       |Strong     |No
D3  |Overcast   |Hot            |High       |Weak       |Yes
D4  |Rain       |Mild           |High       |Weak       |Yes
D5  |Rain       |Cool           |Normal     |Weak       |Yes
D6  |Rain       |Cool           |Normal     |Strong     |No
D7  |Overcast   |Cool           |Normal     |Strong     |Yes
D8  |Overcast   |Mild           |High       |Weak       |No
D9  |Sunny      |Cool           |Normal     |Weak       |Yes
D10 |Rain       |Mild           |Normal     |Weak       |Yes


Given input:
X = (Outlook=Sunny, Temperature=Cool, Humidity=High, Wind=Strong)

_________________________________________________________________________________________________

For "Play Tennis = Yes"

Attribute     Value    Count   Likelihood
-----------------------------------------
Outlook       Sunny    1       1/6
              Overcast 2       2/6
              Rain     3       3/6 

Temperature   Hot      1       1/6 
              Mild     2       2/6 
              Cool     3       3/6 

Humidity      High     2       2/6 
              Normal   4       4/6 

Wind          Weak     5       5/6 
              Strong   1       1/6

_________________________________________________________________________________________________

For "Play Tennis = No"

Attribute     Value    Count   Likelihood
-----------------------------------------
Outlook       Sunny    2       2/4 
              Overcast 1       1/4 
              Rain     1       1/4 

Temperature   Hot      2       2/4 
              Mild     1       1/4 
              Cool     1       1/4 

Humidity      High     3       3/4 
              Normal   1       1/4 

Wind          Weak     2       2/4
              Strong   2       2/4 

_________________________________________________________________________________________________

Using Naive Bayes to calculate:  X = (Outlook=Sunny, Temperature=Cool, Humidity=High, Wind=Strong)

P(Play Tennis = Yes | X) ∝ P(Outlook=Sunny | Play Tennis=Yes) *
                           P(Temperature=Cool | Play Tennis=Yes) *
                           P(Humidity=High | Play Tennis=Yes) *
                           P(Wind=Strong | Play Tennis=Yes) *
                           P(Play Tennis=Yes)

P(Play Tennis = Yes | X) ∝ 1/6 * 3/6 * 2/6 * 1/6 * 6/10 = 0.0028

P(Play Tennis = No | X) ∝ P(Outlook=Sunny | Play Tennis=No) *
                          P(Temperature=Cool | Play Tennis=No) *
                          P(Humidity=High | Play Tennis=No) *
                          P(Wind=Strong | Play Tennis=No) *
                          P(Play Tennis=No)

P(Play Tennis = No | X) ∝ 2/4 * 1/4 * 3/4 * 2/4 * 4/10 = 0.01875


When event X occurs, the label of "Class" will be:
"Class" = "No"
'''
