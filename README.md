# SecretSanta

This 2020 with the pandemic going on, Christmas and other festivities are going to be a lot different. However, it is not an excuse to give up on traditions.
For this christmas, I wanted my family to continue their tradition of organising a Secret Santa online.

A Secret Santa is a tradition where each participant is given a random secret match to which they have to offer a present. This way, everyone receives one 
single present from one secret santa.

To prevent sending automatic spam emails from third party softwares, I decided to create my own version of a Secret Santa algorithm. This way you can customize your
email as you want, and you can send it from your customized email address. I do not guarantee its security.

The code is supposed to be as modular as you want, so feel free to fork the project and make your own adaptations.

# How to use it

You will need three files:

- The "info.txt" file
- The "participants_list.txt" file
- The "email_template.txt" file

Please avoid using non latin characters (accents, special characters, etc..) or modify the code to support it.

Once you filled up the three files, run main.py (you will need Python3 installed).

# Disclaimer

I did NOT make the algorithm to be recruited for an internshp next summer, so no, it's not perfect. The code isn't clean or clever, nor is it fast. 
The algorithm is really naive and not efficient (it is O(n^2)) but it works. If you want to make a cleverer algorithm, go for it, but don't wait until the 23rd of
december to send the email to everyone :)

Enjoy!
