###########################################################
# Author >>> Falzy                                        #
# Telegram >>> https://t.me/balestra / https://t.me/op_v0 #
# Website >>> https://blackdata.altervista.org            #
###########################################################


import os
import time
import datetime
#import openai
import poe
import json
import re
import requests
import nltk
import io
import ftplib
import warnings
import google_trans_new as gtn

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

async def get_answer(question,POE_TOKEN,POE_BOT_NAME): 
    prompt = question

    tokens = nltk.word_tokenize(question)
    pos_tags = nltk.pos_tag(tokens)

    is_request = any(tag in ["WP", "WRB", "WDT", "WP$", "MD"] for word, tag in pos_tags)

    max_tokens = 500
    token = POE_TOKEN
    client = poe.Client(token)
    message = prompt
    for chunk in client.send_message(POE_BOT_NAME, message):
      pass
    answer = chunk["text"]
    
    if not is_request and answer.lower() != "yes" and answer.lower() != "no":
        answer = f"{answer}"

    return answer
    
async def clear(POE_TOKEN,POE_BOT_NAME):
    token = POE_TOKEN
    client = poe.Client(token)
    client.purge_conversation(POE_BOT_NAME)
