import pandas as pd
import matplotlib.pyplot as plt
import random
import seaborn as sns

#filename='user_data.csv'
positive = list(pd.read_csv("positive_words.txt", header=0).iloc[:,0].values)
negative = list(pd.read_csv("negative_words.txt", header=0).iloc[:,0].values)

positive_responses=["Great!","Cool!","Sounds great!","Ohhhhh:)"]
negative_responses=["Too bad.","Womp, womp.","Sorry to hear that."]
neutral_responses=["hmmmm","I see"]
#question=["Are you a student?","What's your age?","How are you feeling today?","What's your favorite color?"]
user_responses = pd.DataFrame(columns=["Name", "Mood","Question_1", "Question_2", "Question_3"])
escape = ["bye","quit","end"]
i=1

print("I need to collect data from at least three users. So I will then repeat the conversation until you want to stop.")
while True:
    name = input("Hi user{}, what is your name? (Type 'bye' or 'quit' to quit)".format(i))
    if name.lower() in escape:
        print('Bye, {}!'.format(name))
        break
    print("Nice to meet you, {}. How are you today? (Type 'bye' or 'quit' to quit)".format(name))

    positive_num=0#number of positive words the user input
    negative_num=0
    neutral_num=0
    response=input()
    mood=None

    if response.lower() in escape:
        print('Bye, {}!'.format(name))
        break

    words=response.split()
    for word in words:
        if word.lower() in positive:
            positive_num+=1
        elif word.lower() in negative:
            negative_num+=1
        else:
            neutral_num+=1
    
    if positive_num>negative_num:
        mood="positive"
        question2=input(random.choice(positive_responses)+" Do you have something excitiong planned today?")
        question3=input("Nice! Where to?")
        print("Sounds great. I enjoyed chating with you. Bye!")
    elif positive_num<negative_num:
        mood="negative"
        question2=input(random.choice(negative_responses)+" What's wrong?")
        question3=input("Can you tell me more about what's going on?")
        print("Come on, it will get better. Bye!")
    else:
        mood="neutral"
        question2=input(random.choice(neutral_responses)+" What do you like to do in your free time?")
        question3=input("Have you been to any interesting places recently?")
        print("I enjoyed chating with you. Have a nice day. Bye!")
    
    new_responses=pd.DataFrame({
        "Name":[name],
         "Mood":[mood],
         "Question_1":[response], 
         "Question_2":[question2], 
         "Question_3":[question3]}
    )
    user_responses=pd.concat([user_responses,new_responses], ignore_index=True)
    i+=1

print("Thanks for your responses. I've made a note of it.")
#user_responses.to_csv(filename,index=False)
#user_responses=pd.read_csv(filename)

sns.set_theme()
sns.countplot(x='Mood', data=user_responses)
plt.title("Counts of user mood")
plt.xlabel("User mood")
plt.ylabel("Count")
plt.show()

