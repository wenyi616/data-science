from scipy import spatial
from scipy.spatial.distance import euclidean, pdist, squareform,cosine
from scipy import linalg

from sklearn.metrics.pairwise import cosine_similarity

import numpy as np


#################
# loading data
#################

with open("./data/shows.txt", "r") as fd:
    shows = fd.read().splitlines()

with open("./data/user-shows.txt", "r") as fd:
    user = fd.read().splitlines()

# print(shows)
# print(user)

u = [ [ 0 for i in range(563) ] for j in range(9985) ]
for i in range(len(user)):
    u[i] = user[i].split(" ")
    
u = [[int(j) for j in i]  for i in u]


#################
# user
#################

s = cosine_similarity(u)
similarity = s [499]

u = np.matrix(u) 

r_a = np.dot(similarity,u)
r_a_list = r_a.tolist()[0]
# print(r_list)


# S - the set of the first 100 shows
sample_a = r_a[0,0:100]

ranked_a = np.argsort(-sample_a).tolist()
# print(ranked)

largest_indices = ranked_a[0][:5]
# print(largest_indices)
# [96, 74, 45, 60, 9]


part_a_scores = []
part_a_shows = []

for i in largest_indices:
	part_a_scores.append(r_a_list[i])
	part_a_shows.append(shows[i])

print("\n\n >>> Printing results for question A")

print(part_a_scores)	
print(part_a_shows)

# [908.4800534761259, 861.1759992873294, 827.6012954743575, 784.7819589039735, 757.6011181024219]

# "FOX 28 News at 10pm"
# "Family Guy"
# "2009 NCAA Basketball Tournament"
# "NBC 4 at Eleven"
# "Two and a Half Men"



#################
# iten-item 
#################
Alex = u[499]

uT = u.transpose()
s_b = cosine_similarity(uT)

r_b = np.dot(Alex,s_b)
r_b_list = r_b.tolist()[0]

sample_b = r_b[0,:100]

ranked_b = np.argsort(-sample_b).tolist()

largest_indices_b = ranked_b[0][:5]
# print(largest_indices_b)
# [96, 74, 60, 45, 82]

part_b_scores = []
part_b_shows = []

for i in largest_indices_b:
	part_b_scores.append(r_b_list[i])
	part_b_shows.append(shows[i])

print("\n\n >>> Printing results for question B")
print(part_b_scores)	
print(part_b_shows)
# [31.3647016783424, 30.00114179887777, 29.396797773402543, 29.227001561500487, 28.971277674055557]

# "FOX 28 News at 10pm" 
# "Family Guy"
# "NBC 4 at Eleven"
# "2009 NCAA Basketball Tournament"
# "Access Hollywood"



#################
# Latent hidden model
#################
U, s, Vh = linalg.svd(u)

for i in range(len(s)):
    if i>9:
        s[i]=0

Sigma = np.zeros((u.shape[0], u.shape[1]))
Sigma[:u.shape[1], :u.shape[1]] = np.diag(s)

# R*
R = U.dot(Sigma.dot(Vh))
Alex_c = R[499,:100]

r_c_list = Alex_c.tolist()
# print(r_c_list)

ranking_latent = np.argsort(-Alex_c)[:5]

part_c_scores = []
part_c_shows = []

for i in ranking_latent:
	part_c_scores.append(r_c_list[i])
	part_c_shows.append(shows[i])


print("\n\n >>> Printing results for question C")
# print(ranking_latent)
print(part_c_scores)	
print(part_c_shows)
