# Quiz
Below script allows you to find most relevent answer to the question provided along with options.

### Setup:
1) Need to create google search custom project for <google-customsearch-id>. https://cse.google.co.in/cse/
2) Create a Custom search api project on google cloud platform for get key <google-cse-project-key>. https://console.cloud.google.com
3) Replace the above vaiable in script and add question and anser options in text variable.
4) Run main.py

# Sample
['Who was the first president of United states?\n', '\n', 'Abraham Lincoln\n', 'Karnataka\n', 'George Washington\n', 'Benjamin Franklin\n', ' ']
2
1
13
1

The above sample, results show Option 3 getting most hits and that is the answer. In most of cases the option with maximum number would be right anwser.
