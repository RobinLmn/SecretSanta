# SecretSanta

With the 2020 pandemic, Christmas and other festivities had to adapt to an online format. To support that, I decided to translate our long lasting traditon of Secret Santa online.

A Secret Santa is a tradition where each participant is given a random secret match to which they have to offer a present. This way, everyone receives a present from a secret santa.

To prevent sending automatic spam emails from third party softwares, I decided to create my own version of a Secret Santa algorithm. This way, the email sent is customizable and can be sent from your own email address. 

The code is supposed to be as modular as you want, so feel free to fork the project and make your own adaptations.

# How to use it

You will need two files:

- The "participants.json" file

Each participant is a json object with three fields, the name, the email adress, and the list of other participants names that participants cannot get assigned. For example, if participant A got participant B last year, and participant A really doesn't like participant A, the list of forbidden matches for participant A will be ```["ParticipantB", "ParticpantC"]```.

- The "email_template.txt" file

It is the content of the email that will automatically be sent. You can use the variables below to customize the email for each participant:

```$(PERSON_NAME)``` is the name of the email receiver.

```$(PERSON_ASSIGNEE)``` is the name of the match of the email receiver.

Once you filled up the two files, you will have to edit the email, password, subject and server fields in main.py. Then, run the file.

# Disclaimer

The algorithm is not perfect; it is really naive and not efficient (it is O(n^2)). If the family continues to grow, I will probably have to opimize it...

Enjoy!
