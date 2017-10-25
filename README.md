# Hadoop-SparkRecommender
Real time movie recommender system which recommends movies in real time(computationally efficient)

This approach is extension of the Already implemented Recommender system. The computation performed to recommend items to each user are large and hence the system cannot be used practically in real life in the single processor.

Idea is to parallize the recommendation given to various users at the single time. 

RESULTS - Computation speed was doubled when using 2 processors(4 core each) ,almost tripled when using 3 processors (4 core each).
It was observed han the computation speed was not linearly dependent on number of processors due to overhead each processor take to communicate with one another. After certain number of processors , computation speed achieves saturation value which can be predicted graphically.

The recommender system is built using Personality Diaganosis approach which can be found in other repository. 
