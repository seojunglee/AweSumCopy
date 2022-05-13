import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import time
import torch
from transformers import T5ForConditionalGeneration,T5Tokenizer
import random
import spacy
import zipfile
import os
import json
import requests
from collections import OrderedDict
import string

import nltk
import numpy 
from nltk import FreqDist
#nltk.download('brown')
#nltk.download('stopwords')
#nltk.download('popular')
from nltk.corpus import stopwords
from nltk.corpus import brown
from nltk.tokenize import sent_tokenize


import time

def beam_search_decoding (inp_ids,attn_mask,model,tokenizer):
    beam_output = model.generate(input_ids=inp_ids,attention_mask=attn_mask,max_length=256,num_beams=10,num_return_sequences=3,no_repeat_ngram_size=2,early_stopping=True)
    Questions = [tokenizer.decode(out, skip_special_tokens=True, clean_up_tokenization_spaces=True) for out in beam_output]
    return [Question.strip().capitalize() for Question in Questions]

class BoolQGen:
       
    def __init__(self):
        self.tokenizer = T5Tokenizer.from_pretrained('t5-base')
        model = T5ForConditionalGeneration.from_pretrained('ramsrigouthamg/t5_boolean_questions')
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model.to(device)
        # model.eval()
        self.device = device
        self.model = model
        self.set_seed(42)
        
    def set_seed(self,seed):
        numpy.random.seed(seed)
        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)

    def random_choice(self):
        a = random.choice([0,1])
        return bool(a)
    

    def predict_boolq(self,payload):
        start = time.time()
        inp = {
            "input_text": payload,
            "max_questions": 6
        }

        text = inp['input_text']
        num= inp['max_questions']
        sentences = sent_tokenize(text)
        joiner = " "
        modified_text = joiner.join(sentences)
        answer = self.random_choice()
        form = "truefalse: %s passage: %s </s>" % (modified_text, answer)

        encoding = self.tokenizer.encode_plus(form, return_tensors="pt")
        input_ids, attention_masks = encoding["input_ids"].to(self.device), encoding["attention_mask"].to(self.device)

        output = beam_search_decoding (input_ids, attention_masks,self.model,self.tokenizer)
        if torch.device=='cuda':
            torch.cuda.empty_cache()
        
        final= {}
        final['Text']= text
        final['Count']= num
        final['Boolean Questions']= output
            
        return final