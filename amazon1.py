def popularNFeatures(numFeatures, topFeatures, possibleFeatures,
                     numFeatureRequests, featureRequests):
    # WRITE YOUR CODE HERE
    frequency = dict()

    for fea in possibleFeatures:
        frequency[fea] = 0

    for fea in possibleFeatures:
        for req in featureRequests:
           if fea in req:
               frequency[fea] += 1

    sortedresult = sorted(frequency.items(), key=lambda x:x[1], reverse=True)[:topFeatures]
    print(sortedresult[0][0])
    resultlist = []
    for i in range(0, topFeatures):
        resultlist.append(sortedresult[i][0])

    print(resultlist)




if __name__ == "__main__":
    possibleFeatures = ["a", "b","c","e","d"]
    featureRequests = ["sghfssdfa", "fsfdsfsdb","yertera","sdfsa"]
    popularNFeatures(5, 2, possibleFeatures,4, featureRequests)