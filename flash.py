#!/usr/bin/env python3

import time
import datetime


class flash_cards(object):
  def __init__(self, qfile='questions.txt'):
    self.correct_count = 0 # correct answer counter 
    self.priority_list = [] # questions that take more than 5 seconds to answer
    self.time_taken = datetime.timedelta(seconds = 5)
    self.intel_time = 100
    with open(qfile) as file:
      self.test_list = [x.split(':') for x in file.read().splitlines()] #read returns lines , splitlines() splits lines
    print(self.test_list)
  def game(self):
    for i,x in self.test_list:
      print("{}".format(i))
      when_asked = datetime.datetime.now()
      askUser = input()
      if askUser != x:
        continue
      self.correct_count += 1
      when_told = datetime.datetime.now()
      self.intel_time = when_told - when_asked
      if self.intel_time > time_taken: 
        self.priority_list.append(i)


if __name__ == '__main__':
  fc = flash_cards()
  fc.game()
  print("your score is {} , it took you {} ".format(fc.correct_count, fc.intel_time))
  if fc.priority_list: 
    print("some questions seemed as if they took long to be answered ,")
    for questions in fc.priority_list:
      print(questions)

  time.sleep(20)

