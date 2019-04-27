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
        mTagsSplitLine = line.split(' ')
        mTagsList.append(mTagsSplitLine)
        mTagsList[-1][-1] = mTagsList[-1][-1].replace('\n', '')
# print(mTagsList[1])

tagsList = []
with open('tags.dat', 'r') as tagsFile:
    for line in tagsFile:
        tagsSplitLine = line.split(' ')
        tagsList.append(tagsSplitLine)
        tagsList[-1][-1] = tagsList[-1][-1].replace('\n', '')
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


# placeholder vector
trainList = trainList[1:-1]
print(trainList[0][0])
movieVect = [1, 1, 1, 1, 1, 1, 1, 1, 1]
userProfiles = []
for line in trainList:
    if not uexists(userProfiles, line[0]):
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
print(userProfiles[0][0])
print(userProfiles[0][1])
print(len(userProfiles[0][1]))
print(userProfiles[0][2])
print(len(userProfiles[0][2]))

k = 10
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


