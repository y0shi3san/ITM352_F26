#
# Kaili Takara
# September 25, 2026

emotions = ('suprised', 'sad', 'fear', 'happy', 'anxious')

#is_it_true = emotions[len(emotions)-1] == "happy" and len(emotions) > 3

if emotions[len(emotions) - 1] == "happy" and len(emotions) > 3:
    is_it_true = True
else:
    is_it_true = False

print(is_it_true)
# print(emotions[3] == "happy" and len(emotions) > 3)
