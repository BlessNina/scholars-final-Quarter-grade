def 
get_adjectival_equivalent(grade):
    if 96 <= grade <= 100:
        return "EXCELLENT"
    elif 90 <= grade < 96:
        return "VERY GOOD"
    elif 84 <= grade < 90:
        return "VERY GOOD"
    elif 78 <= grade < 84:
        return "GOOD"
    elif 72 <= grade < 78:
        return "GOOD"
    elif 66 <= grade < 72:
        return "SATISFACTORY"
    elif 60 <= grade < 66:
        return "SATISFACTORY"
    elif 55 <= grade < 60:
        return "FAIR"
    elif 50 <= grade < 55:
        return "FAIR"
    elif 40 <= grade < 50:
        return "FAILED ON CONDITION"
    else:
        return "FAILED"

90 = float(input("Enter Tentative Grade for Q1: "))
92 = float(input("Enter Tentative Grade for Q2: "))
88 = float(input("Enter Tentative Grade for Q3: "))
94 = float(input("Enter Tentative Grade for Q4: "))

Q1 = t1
Q2 = (Q1 + 2 * t2) / 3
Q3 = (Q2 + 2 * t3) / 3
Q4 = (Q3 + 2 * t4) / 3
