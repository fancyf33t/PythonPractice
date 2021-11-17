favorite_languages = {
    'jen': 'python',
    'keitron': 'python',
    'ethan': 'c',
}
poll_takers = ['kate', 'jordan', 'patrick', 'valencia', 'keitron']

for name in poll_takers:
    if name in favorite_languages.keys():
        print(f"Dude, {name.title()}... You already took the survey.")
    else:
        print(f"{name.title()}, you should take the survey.")
#fucking one and done. let's go

#Step1: there is a dictionary set to determine the favorite_languages with key:value pairs of users and favorite languages for programming
#Step2: there is a list of poll_takers who have yet to choose a favorite language
#Step3: run a for loop checking the names in the poll_takers list
#Step4: run an if-statement testing if there are any names in the dictionary favorite_languages
#Step5: default an else statement if the names are not available