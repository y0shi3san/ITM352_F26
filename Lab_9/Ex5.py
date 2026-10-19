# Program to remove any scores from a list that are below 50.
 
scores = [60, 45, 30, 85, 10, 90]

passing_scores = []
for score in scores:
    if score >= 50:
        passing_scores.append(score)

scores = passing_scores
print(scores)
