# Keyphrase Extraction Algorithm

基于 Topic PageRank实现的关键词抽取算法（TextRank， TPR， Salience Rank， Single TPR）

Keyphrase Extraction Algorithm based on Topic PageRank

## Dependencies
  - nltk 3.6.1
  - matplotlib 3.3.4
  - networkx 2.5
  - numpy 1.20.1

## Files
  - runner.py: executes the main function  
  - ranks.py: implementation of various key phrase extraction algorithms
  - tagger.py: POS tagging infrastructure 
  - utils.py: various utilities functions 
  - process.py: infrastructure for dataset processing 

## DataSet

### English

  - data: contains the two standard datasets Inspec (Hulth. 2003. Improved automatic keyword extraction given more linguistic knowledge) and 500N (Marujo et al. 2013. Supervised topical key phrase extraction of news stories using crowdsourcing, light filtering and co-reference normalization). 
  - lda: The TPR and DR algorithms rely on two LDA output files (which can be obtained with any standard LDA implementation). 
    - Each line of lda-topicsXvocab*.txt contains the topic distribution over the vocabulary for each document (documents are sorted alphabetically by filename). 
    - Each line of lda-docxXtopics*.txt contains the proportion of each topic for each document (documents are sorted alphabetically by filename).
  - results: the results for the two datasets are output here after executing runner.py

## Usage
```
python runner.py 
```

## Todo

- [ ] 添加LDA
- [ ] 增加中文关键词提取部分



## Reference

  - Text Rank: Mihalcea and Tarau. 2004. Textrank: Bringing order into texts.
  - TPR: Liu et al. 2010. Automatic keyphrase extraction via topic decomposition.
  - Single TPR: Sterckx et al. 2015. Topical word importance for fast keyphrase extraction.
  - Salience Rank: Nedelina et al . 2017.Salience Rank: Efficient Keyphrase Extraction with Topic Modeling.
  - https://github.com/zhengfeitian/saliencerank
