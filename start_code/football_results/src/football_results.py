

def get_result(final_score):
    if final_score["home_score"] > final_score["away_score"]:
        return "Home win"
    elif final_score["home_score"] < final_score["away_score"]:
        return "Away win"
    else: 
        return "Draw"

def get_results(final_scores):
    final_scores = [get_result[0], get_result[1], get_result[2]]
    return final_scores