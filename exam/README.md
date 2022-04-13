# README
## To run
 - type python3 exam4.py

## index
  ### Exam.py
   - this generates 4 points based on the given constraints
  ### Exam2.py
   - this generates the distance between the 6 pairs of points and returns it
   - the distances are res1, res2 ...  res6
   - it also generates the initial potential energy of the system
   - we dont use the armstrong value in this case as it causes an overflow error
  ### Exam3.py
   - this uses steepest descent method to find the minimum potential energy for different learning rates and momentums
   - the values are listed 
   - it doesnt plot since we would require to plot potential energy against the six values of the pairwise distances
   - we use the six pairwise distances as 6 parameters to the function, in each iteration, delta_w is the distance by which we bring the points closer to or further away from each other, i.e. the value by which we change these 6 pair wise distances.
   - the plot is of U(x) vs steps for different values of momenta (each row) and learning rates (each column)

  ### Exam4.py
   - this uses steepest descent method to find the minimum potential energy for different learning rates and momentums
   - it uses the co ordinates to compute the gradient unlike exam3 which used pairwise distances
   - hessian matrix is also provided
   - we use the six pairwise distances as 6 parameters to the function, in each iteration, delta_w is the distance by which we bring the points closer to or further away from each other, i.e. the value by which we change these 6 pair wise distances.
   - the plot is of U(x) vs steps for different values of momenta (each row) and learning rates (each column)