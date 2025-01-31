import unittest
from Project_3 import *


class Functions_Tester(unittest.TestCase):


  def test_process_text_case(self):
    print('\n\nTest process_text case')
    try:
      text = 'THIS is text that is in MiXeD CASes SOME OF IT is UPPERCASE, some is HArd to EXPlAIN'
      tokens = process_text(text)
      print('Input text was:', text)
      print('Return value was:', tokens)
      result_pred = ['THIS', 'is', 'text', 'that', 'is', 'in', 'MiXeD', 'CASes', 'SOME', 'OF', 'IT', 'is', 'UPPERCASE', 'some', 'is', 'HArd', 'to', 'EXPlAIN']
      print('Expected',result_pred)
      self.assertEqual(tokens, result_pred)
    except BaseException as e:
      print(e)
      print('Testing failed.')


  def test_process_text_punct(self):
    print('\n\nTest process_text remove punctuation')
    try:
      text = 'here is some text!!! with punctu?ation in it, it is all default!'
      tokens = process_text(text)
      print('Input text was:', text)
      print('Return value was:', tokens)
      result_pred = ['here', 'is', 'some', 'text', 'with', 'punctuation', 'in', 'it', 'it', 'is', 'all', 'default']
      print('Expected',result_pred)
      self.assertEqual(tokens, result_pred)
    except BaseException as e:
      print(e)
      print('Testing failed.')
      

  def test_process_text_space_1(self):
    print('\n\nTest process_text space hashtags')
    try:
      text = 'this tweet has a lot of #hashtags#really#close#together and one that is #separate'
      tokens = process_text(text)
      print('Input text was:', text)
      print('Return value was:', tokens)
      result_pred = ['this', 'tweet', 'has', 'a', 'lot', 'of', '#hashtags', '#really', '#close', '#together', 'and', 'one', 'that', 'is', '#separate']
      print('Expected',result_pred)
      self.assertEqual(tokens, result_pred)
    except BaseException as e:
      print(e)
      print('Testing failed.')

  def test_process_text_space_2(self):
    print('\n\nTest process_text space mentions')
    try:
      text = 'this tweet was to @another_user and also @second_user@third_user@fourth_user and this one'
      tokens = process_text(text)
      print('Input text was:',text)
      print('Return value was:', tokens)
      result_pred = ['this', 'tweet', 'was', 'to', '@another_user', 'and', 'also', '@second_user', '@third_user', '@fourth_user', 'and', 'this', 'one']
      print('Expected',result_pred)
      self.assertEqual(tokens, result_pred)
    except BaseException as e:
      print(e)
      print('Testing failed.')
      

  def test_process_text_space_3(self):
    print('\n\nTest process_text space dash')
    try:
      print('THIS MAY NOT WORK CORRECTLY ON ALL OPERATING SYSTEMS. That is ok.')
      text = 'here is a tweet that is open-ended and contains one-time words'
      tokens = process_text(text)
      print('Input text was:', text)
      print('Return value was:', tokens)
      result_pred = ['here', 'is', 'a', 'tweet', 'that', 'is', 'open', 'ended', 'and', 'contains', 'one', 'time', 'words']
      print('Expected',result_pred)
      self.assertEqual(tokens, result_pred)
    except BaseException as e:
      print(e)
      print('Testing failed.')
      
      
  def test_get_features_hashtags(self):
    print('\n\nTest get_features hashtags')
    try:
      text = ['this', 'tweet', 'has', 'a', 'lot', 'of', '#hashtags', '#really', '#close', '#together', 'and', 'one', 'that', 'is', '#separate']
      tokens = get_features(text, '#')
      print('Input was:', text)
      print('Return value was:', tokens)
      result_pred = ['#hashtags', '#really', '#close', '#together', '#separate']
      print('Expected',result_pred)
      self.assertEqual(tokens, result_pred)
    except BaseException as e:
      print(e)
      print('Testing failed.')

  def test_get_features_mentions(self):
    print('\n\nTest get_features mentions')
    try:
      text = ['this', 'tweet', 'was', 'to', '@another_user', 'and', 'also', '@second_user', '@third_user', '@fourth_user', 'and', 'this', 'one']
      tokens = get_features(text, '@')
      print('Input was:', text)
      print('Return value was:', tokens)
      result_pred = ['@another_user', '@second_user', '@third_user', '@fourth_user']
      print('Expected',result_pred)
      self.assertEqual(tokens, result_pred)
    except BaseException as e:
      print(e)
      print('Testing failed.')

  def test_feature_extract_hashtag(self):
    print('\n\nTest feature extract hashtag')
    try:
      file = open('for_testing.txt','r', encoding = 'UTF8')
      text = file.read()
      file.close()
      tokens = feature_extract('for_testing.txt', '#')
      print('Input text from file was:\n', text, sep="")
      print('Return value was:', tokens)
      result_pred = {'#college': 1, '#football': 1, '#fake': 1, '#twitter': 1, '#tweet': 1}
      print('Expected',result_pred)
      self.assertEqual(tokens, result_pred)
    except BaseException as e:
      print(e)
      print('Testing failed.')


  def test_feature_extract_mention(self):
    print('\n\nTest feature extract mention')
    try:
      file = open('for_testing.txt','r', encoding = 'UTF8')
      text = file.read()
      file.close()
      tokens = feature_extract('for_testing.txt', '@')
      print('Input text from file was:\n', text, sep="")
      print('Return value was:', tokens)
      result_pred = {'@fakename': 1, '@auser': 1}
      print('Expected',result_pred)
      self.assertEqual(tokens, result_pred)
    except BaseException as e:
      print(e)
      print('Testing failed.')

if __name__ == '__main__':
  unittest.main()
  