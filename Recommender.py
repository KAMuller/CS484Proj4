
trainFile = open('C:/Users/kalex/PycharmProjects/CS484Proj4/Train.dat', 'r')
trainList = []
for line in trainFile:
    splitLine = line.split(' ')
    trainList.append(splitLine)
print(trainList[1])
actorFile = open('C:/Users/kalex/PycharmProjects/CS484Proj4/movie_actors.dat', 'r')
actorList = []
for line in actorFile:
    actSplitLine = line.split(' ')
    actorList.append(actSplitLine)
print(actorList[1])
dirFile = open('C:/Users/kalex/PycharmProjects/CS484Proj4/movie_directors.dat', 'r')
dirList = []
for line in dirFile:
    dirSplitLine = line.split(' ')
    dirList.append(dirSplitLine)
print(dirList[1])
genresList = []
with open('C:/Users/kalex/PycharmProjects/CS484Proj4/movie_genres.dat', 'r') as genFile:
    for line in genFile:
        genSplitLine = line.split(' ')
        genresList.append(genSplitLine)
print(genresList[1])
mTagsList = []
with open('C:/Users/kalex/PycharmProjects/CS484Proj4/movie_tags.dat', 'r') as mTagsFile:
    for line in mTagsFile:
        mTagsSplitLine = line.split(' ')
        mTagsList.append(mTagsSplitLine)
print(mTagsList[1])
tagsList = []
with open('C:/Users/kalex/PycharmProjects/CS484Proj4/tags.dat', 'r') as tagsFile:
    for line in tagsFile:
        tagsSplitLine = line.split(' ')
        tagsList.append(tagsSplitLine)
print(tagsList[1])
useTList = []
with open('C:/Users/kalex/PycharmProjects/CS484Proj4/user_taggedmovies.dat', 'r') as useTFile:
    for line in useTFile:
        useTSplitLine = line.split(' ')
        useTList.append(useTSplitLine)
print(useTList[1])
testList = []
with open('C:/Users/kalex/PycharmProjects/CS484Proj4/test.dat', 'r') as testFile:
    for line in testFile:
        testSplitLine = line.split(' ')
        testList.append(testSplitLine)
print(testList[1])
