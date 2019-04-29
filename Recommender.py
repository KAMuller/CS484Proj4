# Kalman Muller and Jonathan Barker
# CS484 Assignment 4
import os
import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
# load all information from files to list for use in the program
trainList = []
with open('Train.dat', 'r') as trainFile:
    for line in trainFile:
        splitLine = line.split(' ')
        trainList.append(splitLine)
        trainList[-1][-1] = trainList[-1][-1].replace('\n', '')
    trainList = trainList[1:-1]
actorList = []
with open('movie_actors.dat', 'r') as actorFile:
    for line in actorFile:
        actSplitLine = line.split('\t')
        actorList.append(actSplitLine)
        actorList[-1][-1] = actorList[-1][-1].replace('\n', '')
    actorList = actorList[1:-1]
dirList = []
with open('movie_directors.dat', 'r') as dirFile:
    for line in dirFile:
        dirSplitLine = line.split('\t')
        dirList.append(dirSplitLine)
        dirList[-1][-1] = dirList[-1][-1].replace('\n', '')
    dirList = dirList[1:-1]
genresList = []
with open('movie_genres.dat', 'r') as genFile:
    for line in genFile:
        genSplitLine = line.split('\t')
        genresList.append(genSplitLine)
        genresList[-1][-1] = genresList[-1][-1].replace('\n', '')
    genresList = genresList[1:-1]
mTagsList = []
with open('movie_tags.dat', 'r') as mTagsFile:
    for line in mTagsFile:
        mTagsSplitLine = line.split('\t')
        mTagsList.append(mTagsSplitLine)
        mTagsList[-1][-1] = mTagsList[-1][-1].replace('\n', '')
    mTagsList = mTagsList[1:-1]
tagsList = []
with open('tags.dat', 'r') as tagsFile:
    for line in tagsFile:
        tagsSplitLine = line.split('\t')
        tagsList.append(tagsSplitLine)
        tagsList[-1][-1] = tagsList[-1][-1].replace('\n', '')
    tagsList = tagsList[1:-1]
testList = []
with open('test.dat', 'r') as testFile:
    for line in testFile:
        testSplitLine = line.split(' ')
        testList.append(testSplitLine)
        testList[-1][-1] = testList[-1][-1].replace('\n', '')
    testList = testList[1:-1]


# used to get the string for the tag id value
def getTagString(tagID):
    for i in tagsList:
        if tagID == i[0]:
            return i[1]
    return ''


# used to check if a movie vector currently exist for the specified id
def mVectExists(movVects, mID):
    for x in movVects:
        if mID == x[0]:
            return True
    return False


# used to check if a profile exist for the specified user id
def uexists(profiles, uid):
    for x in profiles:
        if uid == x[0]:
            return True
    return False


# used to get the index for the specified user id in the profiles list
def getuidindex(profiles, uid):
    for index,val in enumerate(profiles):
        if uid == val[0]:
            return index
    return -1

# loops though the movie tags data list
# creates profiles if it encounters a new user id
# adds the tag string to the string for the profile
# repeatedly adds the tag based on its weight value
movList = []
fullMovList = []
movID = 0
movInd = -1
string = ''
firstCheck = False
print("Vectorizing")
for prog,x in enumerate(mTagsList):
    if movID != x[0]:
        if firstCheck:
            fullMovList.append(string)
            string = ''
        movInd += 1
        movID = x[0]
        movie = [x[0]]
        movVect = movInd
        movie.append(movVect)
        movList.append(movie)
        firstCheck = True
    tag = getTagString(x[1])
    string += " " + tag
    a = int(x[2])
    while a > 1:
        string += " " + tag
        a = a - 1
    progPerc = str(prog/(len(mTagsList)))
    progPerc = progPerc[0:4]
    sys.stdout.write("\r%s%s" % ('1/4 %', progPerc))
    sys.stdout.flush()
fullMovList.append(string)

# loops though the movie director data list
# creates profiles if it encounters a new user id
# adds the director id string to the string for the profile
movID = 0
string = ''
firstCheck = False
for prog, line in enumerate(dirList):
    if movID != line[0]:
        if not mVectExists(movList, line[0]):
            movInd = len(fullMovList)
            movID = line[0]
            movie = [line[0]]
            movVect = movInd
            movie.append(movVect)
            movList.append(movie)
            fullMovList.append(string)
        for x in movList:
            if x[0] == line[0]:
                movInd = x[1]
                break
    fullMovList[movInd] += " " + line[1]
    progPerc = str(prog / (len(dirList)))
    progPerc = progPerc[0:4]
    sys.stdout.write("\r%s%s" % ('2/4 %', progPerc))
    sys.stdout.flush()

# loops though the movie actors data list
# creates profiles if it encounters a new user id
# adds the actor id string to the string for the profile
# repeatedly adds the actor id based on its ranking value
rank_hold = 0
movID = 0
string = ''
firstCheck = False
for prog, line in enumerate(actorList):
    if movID != line[0]:
        if not mVectExists(movList, line[0]):
            movInd = len(fullMovList)
            movID = line[0]
            movie = [line[0]]
            movVect = movInd
            movie.append(movVect)
            movList.append(movie)
            fullMovList.append(string)
        for x in movList:
            if x[0] == line[0]:
                movInd = x[1]
                break
    rank_hold = int(line[3])
    if rank_hold > 5:
        continue
    string = ''
    while rank_hold <= 5:
        string += line[1] + " "
        rank_hold += 1
    fullMovList[movInd] += " " + string
    progPerc = str(prog / (len(actorList)))
    progPerc = progPerc[0:4]
    sys.stdout.write("\r%s%s" % ('3/4 %', progPerc))
    sys.stdout.flush()

# loops though the movie genres data list
# creates profiles if it encounters a new user id
# adds the genre string to the string for the profile
movID = 0
string = ''
firstCheck = False
for prog, line in enumerate(genresList):
    if movID != line[0]:
        if not mVectExists(movList, line[0]):
            movInd = len(fullMovList)
            movID = line[0]
            movie = [line[0]]
            movVect = movInd
            movie.append(movVect)
            movList.append(movie)
            fullMovList.append(string)
        for x in movList:
            if x[0] == line[0]:
                movInd = x[1]
                break
    fullMovList[movInd] += " " + line[1]
    progPerc = str(prog / (len(genresList)))
    progPerc = progPerc[0:4]
    sys.stdout.write("\r%s%s" % ('4/4 %', progPerc))
    sys.stdout.flush()

# converts the strings for each movie to vectors using the sklearn TF-IDFVectorizer function
vectorizer = TfidfVectorizer(max_features=400)
vector = vectorizer.fit_transform(fullMovList)
vector = vector.toarray()
print('\rDone')


# gets the movie vector for the associated movie id
def getVector(mID):
    for i in movList:
        if i[0] == mID:
            return vector[i[1]]
    return np.array([9, 9])

# generates the user taste profiles using the information from the train data list
# each element in userProfiles stores the user id, the list of movie vectors for that user,
# and the scores given by the user for each movie
userProfiles = []
print("Creating User Taste Profiles")
curUser = 0
index = 0
for prog, line in enumerate(trainList):
    if curUser != line[0]:
        curUser = line[0]
        profile = [line[0]]
        proMovies = []
        proMovieScores = []
        profile.append(proMovies)
        profile.append(proMovieScores)
        userProfiles.append(profile)
        index = getuidindex(userProfiles, line[0])
    vect = getVector(line[1])
    if not np.array_equal(vect, np.array([9, 9])):
        userProfiles[index][1].append(getVector(line[1]))
        userProfiles[index][2].append(line[2])
    progPerc = str(prog/(len(trainList)))
    progPerc = progPerc[0:4]
    sys.stdout.write("\r%s%s" % ('%', progPerc))
    sys.stdout.flush()
print("\rDone")

# for each line in test list
# calculates the similarity of the specified movie to those in the users taste profile
# predicts the users score for the movie based on a weighted average of the k most similar movies
k = 15
print("Recommending Scores")
outputScores = []
fistCheck = False
current_user = 0
testMovVect = []
indexCheck = []
for prog, line in enumerate(testList):
    index = getuidindex(userProfiles, line[0])
    testMovVect = getVector(line[1]).reshape(1, -1)
    similarities = cosine_similarity(userProfiles[index][1], testMovVect)
    sortO = (-similarities).argsort(axis=0)[:k]
    weightTot = 0
    weightSum = 0
    for a in range(len(sortO)):
        x = int(sortO[a])
        weightTot += float(similarities[x])
        weightSum += float(similarities[x]) * float(userProfiles[index][2][x])
    progPerc = str(prog / (len(testList)))
    progPerc = progPerc[0:4]
    sys.stdout.write("\r%s%s" % ('%', progPerc))
    sys.stdout.flush()
    if weightTot == 0:
        indexCheck.append(line[1])
        outputScores.append(np.round(2.5, decimals=1))
    else:
        indexCheck.append(line[1])
        outputScores.append(np.round(weightSum/weightTot, decimals=1))
print("\rDone")
# outputs scores to the file
try:
    os.remove("output.dat")
except OSError:
    pass
output = open("output.dat", "w", encoding="utf8")
for x in outputScores:
    output.write(str(x))
    output.write('\n')
    output.flush()
output.close()
