#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Code for processing the datasets, writing the extracted keyphrases 
to files and getting the final accuracy statistics. 
'''

import os, io
from ranks import saliencerank, textrank, tpr, singletpr
from utils import *
import numpy as np

"""Outputs the keyphrases in sepatare text files."""


def writeFiles(keyphrases, fileName, fileDir):
    keyphraseFile = io.open(fileDir + "/" + fileName + ".txt", 'wb')
    keyphraseFile.write('; '.join(keyphrases).encode())
    keyphraseFile.close()


"""Switch for running the different algorithms"""


def algorithm_switch(argument, topics, pt, txt, article_ID, alpha=0.1):
    if argument == 0:
        return textrank(txt)
    elif argument == 1:
        return tpr(topics, pt, txt, article_ID)
    elif argument == 2:
        return saliencerank(topics, pt, txt, article_ID, alpha)
    elif argument == 3:
        return singletpr(topics, pt, txt, article_ID)


"""Process the Inspec (Hulth2003) dataset
    The keyphrases for each document are written to files. """


def process_hulth(lda_file, docsXtopics_file, output_dir, flag):
    directory = "data/inspec/all"
    articles = os.listdir(directory)

    text_articles = []
    for article in articles:
        if article.endswith(".abstr"):
            text_articles.append(article)
    text_articles.sort()

    pt = load_docsXtopics_from_file(docsXtopics_file)
    pt = np.array(pt, dtype='float64')
    topics = parse_weights_from_file(lda_file)

    for article_ID in range(len(text_articles)):
        articleFile = io.open(directory + "/" + text_articles[article_ID], 'rb')
        text = articleFile.read()
        text = text.strip(b'\t\n\r')
        text = text.split(b'\r\n')
        article = text[1].decode()
        phrases = algorithm_switch(flag, topics, pt, article, article_ID)
        phrases_topk = []
        for k, _ in phrases:
            phrases_topk.append(k)
        writeFiles(phrases_topk, text_articles[article_ID], output_dir)
        print("article ID:", article_ID, "\t phrases topk:" + ';'.join(phrases_topk))


"""Process the 500N dataset
    The keyphrases for each document are written to files. """


def process_500N(lda_file, docsXtopics_file, output_dir, flag):
    directory = "data/500N/all"

    articles = os.listdir(directory)

    text_articles = []
    for article in articles:
        if article.endswith(".txt"):
            text_articles.append(article)
    text_articles.sort()

    pt = load_docsXtopics_from_file(docsXtopics_file)
    pt = np.array(pt, dtype='float64')
    topics = parse_weights_from_file(lda_file)

    for article_ID in range(len(text_articles)):
        articleFile = io.open(directory + "/" + text_articles[article_ID], 'rb')
        text = articleFile.read()
        text = text.split(b'\n')
        article = text[1].decode()
        phrases = algorithm_switch(flag, topics, pt, article, article_ID)
        phrases_topk = []
        for k, _ in phrases:
            phrases_topk.append(k)
        writeFiles(phrases_topk, text_articles[article_ID][:-4], output_dir)
        print("article ID:", article_ID, "\t phrases topk:" + ';'.join(phrases_topk))

'''Runs a single algorithm on both Inspec (Hulth2003) and 500N datasets and outputs stats. '''


def process_datasets(algorithm, data_set="inspec"):
    if data_set == "inspec":
        output_dir = "results/inspec"
        lda_file = "lda/lda-topicsXvocab-500-Hulth2003.txt"
        docXtopics_file = "lda/lda-docxXtopics-500-Hulth2003.txt"
        gold_standard_directory = "data/inspec/all/"
        process_hulth(lda_file, docXtopics_file, output_dir, algorithm)
    elif data_set == "500N":
        output_dir = "results/500N"
        lda_file = "lda/lda-topicsXvocab-500-500N.txt"
        docXtopics_file = "lda/lda-docxXtopics-500-500N.txt"
        gold_standard_directory = "data/500N/all/"
        process_500N(lda_file, docXtopics_file, output_dir, algorithm)
    else:
        print("data_set must be inspec or 500N")
