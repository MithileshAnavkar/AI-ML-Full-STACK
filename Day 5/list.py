scores = [45, 67, 89, 32, 76]
scores.append(95)
scores[0] = 50
scores.pop(3)
for score in scores:
    print(score)
print("Total Length:" , len(scores))