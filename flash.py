import time
import datetime

with open("questions.txt") as file:
    test_list = [x.split(':') for x in file.read().splitlines()] #read returns lines , splitlines() splits lines

correct_count = 0 # correct answer counter 
priority_list = [] # questions that take more than 5 seconds to answer

time_taken = datetime.timedelta(seconds = 5) # used to test if time taken by user for a particular question > 5 seconds

for i,x in test_list:
    print("{}".format(i))
    when_asked = datetime.datetime.now() # time noted at the time of questioning
    askUser = input()
    if askUser != x: # if user answer not equal to 'x'
        continue
    correct_count += 1
    when_told = datetime.datetime.now() # time noted at the time of answering
    intel_time = when_told - when_asked # time taken by user to answer the question
    if intel_time > time_taken:  # test for time taken by user more than 5 seconds
      priority_list.append(i)

print("your score is {} , it took you {} ".format(correct_count,intel_time))
if priority_list: 
  print("some questions seemed as if they took long to be answered ,")
  for questions in priority_list:
    print(questions)

time.sleep(20)

###--------------------->extra stuff below<----------------### 
 #for words in test_list :
  #  if "\n" in words :
   #     refined_word = words.replace("\n","")
    #    questions_list.append(refined_word)
    #else :
     #   questions_list.append(words)

#for i in questions_list :
 #   print("{} ".format(i))
