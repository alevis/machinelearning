import csv
import math
################################################################################################
def loadCsv(filename):
	lines = csv.reader(open(filename,"rb"))
	dataset = list(lines)
	for i in range(len(dataset)):
		dataset[i] = [float(x) for x in dataset[i]]
	return dataset
# Test 1
# filename = 'pima-indians-diabetes.data.csv'
# dataset = loadCsv(filename)
# print('Loaded data file {0} with {1} rows').format(filename,len(dataset))

# Function to split the dataset
import random
def splitDataset(dataset, splitRatio):
	trainSize = int(len(dataset) * splitRatio)
	trainSet = []
	copy = list(dataset)
	while len(trainSet) < trainSize:
		index = random.randrange(len(copy))
		trainSet.append(copy.pop(index))
	return [trainSet, copy]
# dataset = [[1],[2],[3],[4],[5]]
# splitRatio = 0.67
# train, test = splitDataset(dataset,splitRatio)
# print('Split {0} rows into train with {1} and test with {2}').format(len(dataset),train,test)

# Seperate the training dataset instances by class value so we can calculate
# statistics for each class.
def separateByClass(dataset):
        separated = {}
        for i in range(len(dataset)):
                vector = dataset[i]
                if(vector[-1] not in separated):
                        separated[vector[-1]] = []
                separated[vector[-1]].append(vector)
        return separated

# Testing the separateByClass function
# dataset = [[1,20,1],[2,21,0],[3,22,1]]
# separated = separateByClass(dataset)
# print('Seperated instances: {0}').format(separated)

# Calculating the mean
def mean(numbers):
        return sum(numbers)/float(len(numbers))

def stdev(numbers):
        avg = mean(numbers)
        variance = sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
        return math.sqrt(variance)
# testing stdev()
# numbers = [1,2,3,4,5]
# print("Summary of {0}: mean={1}, stdev={2}").format(numbers,mean(numbers),stdev(numbers))

# Summarize Dataset
def summarize(dataset):
        summaries = [(mean(attribute),stdev(attribute)) for attribute in zip(*dataset)]
        del summaries[-1]
        return summaries

# Testing Summarize
# dataset = [[1,20,0],[2,21,1],[3,22,0]]
# summary = summarize(dataset)
# print('Attribute summaries: {0}').format(summary)


# Summarizing attributes by class
def summarizeByClass(dataset):
        separated = separateByClass(dataset)
        summaries = {}
        for classValue, instances in separated.iteritems():
                summaries[classValue] = summarize(instances)
                return summaries

# Testing
# dataset = [[1,20,1],[2,21,0],[3,22,1],[4,22,0]]
# summary = summarizeByClass(dataset)
# print('Summary by class value: {0}').format(summary)

# Make a Prediction
# Calculating the probability that a given data instance belongs to each class, then
# Selecting the class with the largest probability as the prediction
def calculateProbability(x,mean,stdev):
        exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
        return (1/(stdev*math.sqrt(2*math.pi)))*exponent

# Calculating class probabilities
# Combine the probabilities of all the attribute values for a data instance and come up with
# A probability of the entire data instance belonging to the class
def calculateClassProbabilities(summaries,inputVector):
        probabilities={}
        for classValue,classSummaries in summaries.iteritems():
                probabilities[classValue] = 1
                for i in range(len(classSummaries)):
                        mean, stdev = classSummaries[i]
                        x = inputVector[i]
                        probabilities[classValue] *= calculateProbability(x, mean, stdev)
        return probabilities
# Make a Prediction
def predict(summaries, inputVector):
        probabilities = calculateClassProbabilities(summaries, inputVector)
        bestLabel, bestProb = None, -1
        for classValue, probability in probabilities.iteritems():
                if bestLabel is None or probability > bestProb:
                        bestProb = probability
                        bestLabel = classValue
        return bestLabel

# Getting predictions
def getPredictions(summaries,testSet):
        predictions = []
        for i in range(len(testSet)):
                result = predict(summaries,testSet[i])
                predictions .append(result)
        return predictions

# Getting accuracy
def getAccuracy(testSet,predictions):
        correct = 0
        for x in range(len(testSet)):
                if testSet[x][-1] == predictions[x]:
                        correct += 1
        return (correct/float(len(testSet)))*100.0


# Main function,  putting it all together
def main():
        filename = 'pima-indians-diabetes.data.csv'
        splitRatio = 0.67
        dataset = loadCsv(filename)
        trainingSet, testSet = splitDataset(dataset, splitRatio)
        print('Split {0} rows into train = {1} and test = {2} rows').format(len(dataset), len(trainingSet), len(testSet))
        # pprepare model
        summaries = summarizeByClass(trainingSet)
        # test model
        predictions = getPredictions(summaries, testSet)
        accuracy = getAccuracy(testSet,predictions)
        print('Accuracy: {0}%').format(accuracy)
main()
