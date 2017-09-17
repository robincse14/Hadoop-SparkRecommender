from dataset_movielens_movienames import dataset_movie_name

from SingleNode import *

from pyspark import SparkContext 
def fun(x):
	k=predict('75',str(x))
	return (x,k)

def recommend(user):
    MatchDictionary(user)
    
    MovieRdd=sc.textFile('MovieID')

    MovieRdd2=MovieRdd.filter(lambda x:x not in TrainData[user])

    PredictedRating=MovieRdd.map(fun)
    L=PredictedRating.collect()
    
    L=sorted(L,key=itemgetter(1))

    L.reverse()
    ans=[]
    for i in range(0,10):
        ans.append(list(dataset_movie_name[L[i][0]])[0][1:])
    
    return ans

recommend('75')