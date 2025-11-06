def average(scores_dict):
 
    all_scores = scores_dict.values()
    
    total_score = sum(all_scores)
    
    num_students = len(all_scores)
    
    if num_students == 0:
        return 0
    
    class_average = total_score / num_students
    
    return class_average

class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}

class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")