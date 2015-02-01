import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

def bartender_ans():
    """Asks some questions and returns a dictionary of booleans
    relies on global questions and ingredients"""
    
    answers = {
        "strong": False,
        "salty": False,
        "bitter": False,
        "sweet": False,
        "fruity": False
    }

    for question in questions:
            try:
                answerstr = raw_input(questions[question]+' ')
                answerstr = answerstr.strip().upper()
                answers[question] = (len(answerstr)==3 and 'YES' in answerstr) or (len(answerstr)==1 and answerstr[0] == 'Y')
            except:
                print "Don't understand, will take that as a no"
    
    return answers

def make_drink(drink_prefs):
    """Given a dictionary of answers, returns a drink list, relies on global ingredients"""
    drink = []
    for pref in drink_prefs:
        if drink_prefs[pref]:
            drink.append(random.choice(ingredients[pref]))
    return drink

if __name__ == "__main__":
    
    answers = bartender_ans()
    print "Your drink contains this list of ingredients"
    print make_drink(answers)
     