import sys
from pyspark import SparkContext, SparkConf
 
conf = SparkConf()
sc = SparkContext(conf=conf)

# inputFile = sc.textFile("./wiki.txt")
inputFile = sc.textFile(sys.argv[1])

# MAP: we map each bigram to a tuple ((word_1,word_2), 1), 1 being the number of occurrences of bigram
bigrams = inputFile.map(lambda line : line.strip().split(" "))\
    .flatMap(lambda line: [((line[i],line[i+1]),1) for i in range (0, len(line)-1)])
words = inputFile.flatMap(lambda line: line.strip().split(" ")).map(lambda word: (word, 1.0))

# REDUCE: 
wordCounts = words.reduceByKey(lambda a,b:a +b)
bigramsCounts = bigrams.reduceByKey(lambda a, b: a + b).map(lambda x : (x[0][0], (x[0][1],x[1])))

bigramsFreq = wordCounts.join(bigramsCounts).map(lambda x :((x[0],x[1][1][0]),x[1][1][1]/x[1][0]))

# bigramsCounts.coalesce(1, shuffle=True).saveAsTextFile(sys.argv[2])
# bigramsFreq.coalesce(1, shuffle=True).saveAsTextFile(sys.argv[3])
bigramsCounts.saveAsTextFile("./counts-5")
bigramsFreq.saveAsTextFile("./freq-5")

sc.stop()
