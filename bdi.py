def ask_question(question, options):
    print(question)
    for key, value in options.items():
        print(f"{key}. {value['text']}")
    while True:
        choice = input("Enter the number of your choice: ")
        if choice in options:
            return options[choice]['score']
        else:
            print("Invalid choice. Please select a valid option.")

def main():
    questions = [
        ("Sadness", {"0": {"text": "I do not feel sad.", "score": 0},
                      "1": {"text": "I feel sad much of the time.", "score": 1},
                      "2": {"text": "I am sad all the time.", "score": 2},
                      "3": {"text": "I am so sad or unhappy that I can't stand it.", "score": 3}}),
        ("Pessimism", {"0": {"text": "I am not discouraged about my future.", "score": 0},
                        "1": {"text": "I feel more discouraged about my future than I used to.", "score": 1},
                        "2": {"text": "I do not expect things to work out for me.", "score": 2},
                        "3": {"text": "I feel my future is hopeless and will only get worse.", "score": 3}}),
        ("Past Failure", {"0": {"text": "I do not feel like a failure.", "score": 0},
                          "1": {"text": "I have failed more than I should have.", "score": 1},
                          "2": {"text": "As I look back, I see a lot of failures.", "score": 2},
                          "3": {"text": "I feel I am a total failure as a person.", "score": 3}}),
        ("Loss of Pleasure", {"0": {"text": "I get as much pleasure as I ever did from the things I enjoy.", "score": 0},
                              "1": {"text": "I don't enjoy things as much as I used to.", "score": 1},
                              "2": {"text": "I get very little pleasure from the things I used to enjoy.", "score": 2},
                              "3": {"text": "I can't get any pleasure from the things I used to enjoy.", "score": 3}}),
        ("Guilty Feelings", {"0": {"text": "I don't feel particularly guilty.", "score": 0},
                             "1": {"text": "I feel guilty over many things I have done or should have done.", "score": 1},
                             "2": {"text": "I feel quite guilty most of the time.", "score": 2},
                             "3": {"text": "I feel guilty all of the time.", "score": 3}}),
        ("Punishment Feelings", {"0": {"text": "I don't feel I am being punished.", "score": 0},
                                 "1": {"text": "I feel I may be punished.", "score": 1},
                                 "2": {"text": "I expect to be punished.", "score": 2},
                                 "3": {"text": "I feel I am being punished.", "score": 3}}),
        ("Self-Dislike", {"0": {"text": "I feel the same about myself as ever.", "score": 0},
                          "1": {"text": "I have lost confidence in myself.", "score": 1},
                          "2": {"text": "I am disappointed in myself.", "score": 2},
                          "3": {"text": "I dislike myself.", "score": 3}}),
        ("Self-Criticalness", {"0": {"text": "I don't criticize or blame myself more than usual.", "score": 0},
                              "1": {"text": "I am more critical of myself than I used to be.", "score": 1},
                              "2": {"text": "I criticize myself for all of my faults.", "score": 2},
                              "3": {"text": "I blame myself for everything bad that happens.", "score": 3}}),
        ("Suicidal Thoughts or Wishes", {"0": {"text": "I don't have any thoughts of killing myself.", "score": 0},
                                         "1": {"text": "I have thoughts of killing myself, but I would not carry them out.", "score": 1},
                                         "2": {"text": "I would like to kill myself.", "score": 2},
                                         "3": {"text": "I would kill myself if I had the chance.", "score": 3}}),
        # Add remaining questions here in the same format up to 21...
    ]

    total_score = 0
    print("\nInstructions: Please select the statement that best describes your feelings in the past two weeks.\n")
    for question, options in questions:
        total_score += ask_question(question, options)
        print("\n")

    print(f"Your total score is: {total_score}")

    if total_score<5:
        print("Minimal depression")

    elif total_score>5 and total_score<=12:
        print("Mild depression")

    elif total_score>12 and total_score<=20:
        print("Moderate depression")

    else:
        print("Severe depression")

if __name__ == "__main__":
    main()
