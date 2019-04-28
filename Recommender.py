import os
import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

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
# print(actorList[1])

dirList = []
with open('movie_directors.dat', 'r') as dirFile:
    for line in dirFile:
        dirSplitLine = line.split('\t')
        dirList.append(dirSplitLine)
        dirList[-1][-1] = dirList[-1][-1].replace('\n', '')
    dirList = dirList[1:-1]
# print(dirList[1])

genresList = []
with open('movie_genres.dat', 'r') as genFile:
    for line in genFile:
        genSplitLine = line.split('\t')
        genresList.append(genSplitLine)
        genresList[-1][-1] = genresList[-1][-1].replace('\n', '')
    genresList = genresList[1:-1]
# print(genresList[1])

mTagsList = []
with open('movie_tags.dat', 'r') as mTagsFile:
    for line in mTagsFile:
        mTagsSplitLine = line.split('\t')
        mTagsList.append(mTagsSplitLine)
        mTagsList[-1][-1] = mTagsList[-1][-1].replace('\n', '')
    mTagsList = mTagsList[1:-1]
# print(mTagsList[1])

tagsList = []
with open('tags.dat', 'r') as tagsFile:
    for line in tagsFile:
        tagsSplitLine = line.split('\t')
        tagsList.append(tagsSplitLine)
        tagsList[-1][-1] = tagsList[-1][-1].replace('\n', '')
    tagsList = tagsList[1:-1]
# print(tagsList[1])

useTList = []
with open('user_taggedmovies.dat', 'r') as useTFile:
    for line in useTFile:
        useTSplitLine = line.split(' ')
        useTList.append(useTSplitLine)
        useTList[-1][-1] = useTList[-1][-1].replace('\n', '')
# print(useTList[1])

testList = []
with open('test.dat', 'r') as testFile:
    for line in testFile:
        testSplitLine = line.split(' ')
        testList.append(testSplitLine)
        testList[-1][-1] = testList[-1][-1].replace('\n', '')
    testList = testList[1:-1]
# print(testList[1])
def getTagString(tagID):
    for i in tagsList:
        if tagID == i[0]:
            return i[1]
    return ''


def mVectExists(movVects, mID):
    for x in movVects:
        if mID == x[0]:
            return True
    return False


def uexists(profiles, uid):
    for x in profiles:
        if uid == x[0]:
            return True
    return False


def getuidindex(profiles, uid):
    for index,val in enumerate(profiles):
        if uid == val[0]:
            return index
    return -1

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
            # movList[movInd - 1][1] = len(fullMovList) - 1
        movInd += 1
        movID = x[0]
        movie = [x[0]]
        movVect = movInd
        movie.append(movVect)
        movList.append(movie)
        firstCheck = True
#     get tag FROM X[1] AND tagsList
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
##################################################
# getting actors
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


# print('\rDone')
# print("The first full movie list is now: ", fullMovList[0])

vectorizer = TfidfVectorizer(max_features=400)
vector = vectorizer.fit_transform(fullMovList)
vector = vector.toarray()
print('\rDone')
# print(fullMovList[0])
# for x in vector:
#     print(len(x))
#     print(x)
# print(vector[0])
# placeholder vector
def getVector(mID):
    for i in movList:
        if i[0] == mID:
            return vector[i[1]]
    return np.array([9, 9])


# for x in testList:
#     vect = getVector(x[1])
#     print(vect.shape)
#
# for x in trainList:
#     vect = getVector(x[1])
#     print(vect.shape)

# def checkMiss(mid, mList):
#     for el in mList:
#         if mid == el:
#             return False
#     return True
#
# missingMovies = []
# for x in testList:
#     vect = getVector(x[1])
#     if np.array_equal(vect, np.array([9, 9])):
#         if checkMiss(x[1], missingMovies):
#             missingMovies.append(x[1])
# print("test ", len(missingMovies))
# print(missingMovies)
#
# tmissingMovies = []
# for x in trainList:
#     vect = getVector(x[1])
#     if np.array_equal(vect, np.array([9, 9])):
#         if checkMiss(x[1], tmissingMovies):
#             tmissingMovies.append(x[1])
# print("train ", len(tmissingMovies))
# print(tmissingMovies)
userProfiles = []
print("Creating User Taste Profiles")
curUser = 0
index = 0
for prog, line in enumerate(trainList):
    if curUser != line[0]:
    # if not uexists(userProfiles, line[0]):
        curUser = line[0]
        profile = [line[0]]
        proMovies = []
        proMovieScores = []
        profile.append(proMovies)
        profile.append(proMovieScores)
        userProfiles.append(profile)
        index = getuidindex(userProfiles, line[0])
    # get movie vector from id here, store vector in movieVect
    vect = getVector(line[1])
    if not np.array_equal(vect, np.array([9, 9])):
        userProfiles[index][1].append(getVector(line[1]))
        userProfiles[index][2].append(line[2])
    # else:
        # print("no tags for ", line[1])
    progPerc = str(prog/(len(trainList)))
    progPerc = progPerc[0:4]
    sys.stdout.write("\r%s%s" % ('%', progPerc))
    sys.stdout.flush()
print("\rDone")
# print("There are: ", len(userProfiles), "User Profiles")
# movMin = 99999
# movMax = 0
# for x in userProfiles:
#     if len(x[1]) < movMin:
#         movMin = len(x[1])
#     if len(x[1]) > movMin:
#         movMax = len(x[1])
# print(movMin)
# print(movMax)
# print("The first user is: ", userProfiles[0][0])
# print("The movie vectors for profile 0 are: ", userProfiles[0][1], "Length: ", len(userProfiles[0][1]))
# print("The movie scores for profile 0 are: ", userProfiles[0][2], "Length: ", len(userProfiles[0][2]))
# exit()
k = 15
print("Recommending Scores")
outputScores = []
# testList = the data from test.dat
fistCheck = False
current_user = 0
testMovVect = []
for prog, line in enumerate(testList):
    index = getuidindex(userProfiles, line[0])
    # get movie vector and store to variable testMovVect
    testMovVect = getVector(line[1]).reshape(1, -1)
    # print(index)
    # print(len(testMovVect))
    # print(len(userProfiles[index][1]))
    # print(userProfiles[index][1])
    similarities = cosine_similarity(userProfiles[index][1], testMovVect)
    # print(similarities)
    sortO = (-similarities).argsort(axis=0)[:k]
    # print("sortO is: ", sortO)
    # print(len(sortO))
    weightTot = 0
    weightSum = 0
    for a in range(len(sortO)):
        x = int(sortO[a])
        # print("similarities[0][x] is: ", similarities[x])
        # print("user profiles is: ", userProfiles[index][x])
        weightTot += float(similarities[x])
        # print(weightTot)
        weightSum += float(similarities[x]) * float(userProfiles[index][2][x])
        # print(weightSum)
    progPerc = str(prog / (len(testList)))
    progPerc = progPerc[0:4]
    sys.stdout.write("\r%s%s" % ('%', progPerc))
    sys.stdout.flush()
    if weightTot == 0:
        outputScores.append(np.round(2.5, decimals=1))
    else:
        outputScores.append(np.round(weightSum/weightTot, decimals=1))
print("\rDone")
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
