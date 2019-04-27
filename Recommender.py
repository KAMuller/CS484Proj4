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


actorList = []
with open('movie_actors.dat', 'r') as actorFile:
    for line in actorFile:
        actSplitLine = line.split(' ')
        actorList.append(actSplitLine)
        actorList[-1][-1] = actorList[-1][-1].replace('\n', '')
# print(actorList[1])

dirList = []
with open('movie_directors.dat', 'r') as dirFile:
    for line in dirFile:
        dirSplitLine = line.split(' ')
        dirList.append(dirSplitLine)
        dirList[-1][-1] = dirList[-1][-1].replace('\n', '')
# print(dirList[1])

genresList = []
with open('movie_genres.dat', 'r') as genFile:
    for line in genFile:
        genSplitLine = line.split(' ')
        genresList.append(genSplitLine)
        genresList[-1][-1] = genresList[-1][-1].replace('\n', '')
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
# print(testList[1])
def getTagString(tagID):
    for i in tagsList:
        if tagID == i[0]:
            return i[1]
    return ''

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

    sys.stdout.write("\r%s%s" % ('%', progPerc))
    sys.stdout.flush()
fullMovList.append(string)

print(movList)
print("Index 0 of FullMoveList: ", fullMovList[0:2])
vectorizer = TfidfVectorizer()
vector = vectorizer.fit_transform(fullMovList)

print("the vector is", vector[movList[0][1]])
print("The length of moveList: ", len(movList))
print("Vector is: ", np.shape(vector))
exit()
# placeholder vector
trainList = trainList[1:-1]
print(trainList[0][0])
movieVect = [1, 1, 1, 1, 1, 1, 1, 1, 1]
userProfiles = []
print("Creating User Taste Profiles")
curUser = 0
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
    userProfiles[index][1].append(movieVect)
    userProfiles[index][2].append(line[2])
    progPerc = str(prog/(len(trainList)))
    progPerc = progPerc[0:4]
    sys.stdout.write("\r%s%s" % ('%', progPerc))
    sys.stdout.flush()
print("\rDone")
print(len(userProfiles))
movMin = 99999
movMax = 0
for x in userProfiles:
    if len(x[1]) < movMin:
        movMin = len(x[1])
    if len(x[1]) > movMin:
        movMax = len(x[1])
print(movMin)
print(movMax)


exit()
k = 15
outputScores = []
for line in testList:
    index = getuidindex(userProfiles, line[0])
    # get movie vector and store to variable testMovVect
    testMovVect = []
    similarities = cosine_similarity(userProfiles[index], testMovVect)
    sortO = (-similarities).argsort(axis=1)[:, :k]
    weightTot = 0
    weightSum = 0
    for x in sortO:
        weightTot += similarities[x]
        weightSum = similarities[x] * userProfiles[index][2][x]
    outputScores.append(weightSum/weightTot)


