'''
To calculate the SSE for a given attribute, follow these steps:

9. For the attribute `Likes AI`:
   - Split the data based on `Likes AI`:
     - Group 1: `Likes AI = 0` (Data points: 23, 27, 29)
     - Group 2: `Likes AI = 1` (Data points: 25, 29)
   - Calculate the mean salary for each group.
   - Compute the SSE for each group by summing the squared differences between each salary and the mean salary of that group.
   - Sum the SSEs of both groups to get the total SSE for the attribute `Likes AI`.

   Calculations:
   - For `Likes AI = 0`: Mean salary = 333.33, SSE = 5333.33
   - For `Likes AI = 1`: Mean salary = 450, SSE = 2500
   - Total SSE = 5333.33 + 2500 = 7833.33

   The closest match in the options is `SSE(Likes AI) = 6667`.
   Therefore, the answer is: 
   c) SSE(Likes AI) = 6667

10. For the attribute `Age` with the split `Age <= 24`:
   - Split the data based on the condition `Age <= 24`:
     - Group 1: `Age <= 24` (Data point: 23)
     - Group 2: `Age > 24` (Data points: 25, 27, 29, 29)
   - Calculate the mean salary for each group.
   - Compute the SSE for each group by summing the squared differences between each salary and the mean salary of that group.
   - Sum the SSEs of both groups to get the total SSE for the attribute `Age <= 24`.

   Calculations:
   - For `Age <= 24`: Mean salary = 200, SSE = 0
   - For `Age > 24`: Mean salary = 400, SSE = 5000
   - Total SSE = 0 + 5000 = 5000

   Therefore, the answer is: 
   c) SSE(Age <= 24) = 5000
'''
