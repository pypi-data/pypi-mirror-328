from transformers import AutoTokenizer
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
This is a library to calculate fertility and parity scores, as well as provide visualizations. 
The default model is `meta-llama/Llama-3.2-1B-Instruct`. 

Functions/Classes
-----------------
    - `fertilize`
    - `paritize`
    - `TokenMetrics`

Works Cited
-----------
Parity calculation from https://arxiv.org/abs/2305.15425 (page 3). 

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def fertilize(text, tokenizer=AutoTokenizer.from_pretrained('meta-llama/Llama-3.2-1B-Instruct')): 
    """ 
    Get the fertility score and tokens for a given text. 

    Parameters
    ----------
        - text (str): text for tokenization
        - tokenizer (tokenizer): model/tokenizer 
          (optional, defaults to `meta-llama/Llama-3.2-1B-Instruct`)

    Returns
    -------
        - parity (float): parity score
        - tokenized (list): list of tokens 
    """ 
    tokens = tokenizer.tokenize(text) 
    num_words = len(text.split())

    score = len(tokens) / num_words if num_words > 0 else float('inf')  
    return score, tokens


def paritize(sA, sB, tokenizer=AutoTokenizer.from_pretrained('meta-llama/Llama-3.2-1B-Instruct')): 
    """ 
    Calculate parity score for a text and its translation. 
    "Premium" is the actual score, "parity" is when the score is ~1.    

    Parameters
    ----------
        - sA (string): sentence in language A    
        - sB (string): translation of `sA` in language B
        - tokenizer (tokenizer): model/tokenizer 
          (optional, defaults to `meta-llama/Llama-3.2-1B-Instruct`)

    Returns
    -------
    parity (float): parity score for A relative to B (if this is ~1, it achieves parity)

    """
    sA_tokens = tokenizer.tokenize(sA)
    sB_tokens = tokenizer.tokenize(sB)
    length_sA_tokens = len(sA_tokens)
    length_sB_tokens = len(sB_tokens)

    parity = length_sA_tokens / length_sB_tokens if length_sB_tokens>0 else float('inf')
    return parity 


class TokenMetrics:
    """Get token metrics and visualizations for a dataset."""

    def __init__(self, 
                 data, 
                 tokenizer=AutoTokenizer.from_pretrained('meta-llama/Llama-3.2-1B-Instruct')):
        """ 
        Initialize the `TokenMetrics` class.

        Parameters
        ----------
            - data (pd.DataFrame): Dataset of texts for tokenization
                                   Must contain only `language`, `text`, and `translation` columns,   
                                   where all columns are string-type. 
            - tokenizer (tokenizer): model/tokenizer 
                                     (optional, defaults to `meta-llama/Llama-3.2-1B-Instruct`) 

        Returns
        -------
        None. Initilizes the class.        
        """
        data = data.fillna("")
        self.data=data
        self.tokenizer=tokenizer
        self.fertilities=None
        self.parities=None
    
    def help_fertilize(self, text): 
        """ 
        Get the fertility score and tokens for a given text. Serves as helper function 
        for `fertilize`.

        Parameters
        ----------
            - text (str): text for tokenization
            - tokenizer (tokenizer): model/tokenizer 
              (optional, defaults to `meta-llama/Llama-3.2-1B-Instruct`)

        Returns
        -------
            - score (float): fertility score
            - tokenized (list): list of tokens 
        """ 
        tokens = self.tokenizer.tokenize(text) 
        num_words = len(text.split())

        score = len(tokens) / num_words if num_words > 0 else float('inf') 
        return score, tokens

    def fertilize(self, text_col, language_col): 
        """ 
        Get fertility scores and tokens for a dataset of texts in different languages. 
        
        Returns
        -------
        scored (pd.DataFrame): DataFrame with `language`, `corpus`, `fertility`, and `tokens` columns
        
        """

        languages = list(self.data[language_col].unique())
        language2text = {} # {'language1':'text1', 'language2', 'text2', etc.}
        language2score = {} # {'language1':'score1', 'language2', 'score2', etc.}
        tokens = {} # {'language1':'tokens1', 'language2', 'tokens2', etc.}

        for language in languages:
            text = self.data[self.data[language_col] == language][text_col]
            
            corpus = " ".join(text)

            fertility_score, tokenized = self.help_fertilize(corpus)

            language2text[language] = corpus
            language2score[language] = fertility_score
            tokens[language] = tokenized

        scored = pd.DataFrame({'language': pd.Series(languages),
                               'corpus': pd.Series(language2text.values()),
                               'fertility': pd.Series(language2score.values()),
                               'tokens': pd.Series(tokens.values())}) 
        self.fertilities = scored       
        return scored 
    
    def visualize_fertilities(self, figsize=(10, 6), color='purple'): 
        """ 
        Make a bar plot visualizing fertilities by corpus/language. 

        Parameters
        ----------
            - figsize (tuple): Size of figure, default is (10, 6)
            - color (string): Color of bars

        Returns
        -------
        None. Plots fertilities by corpus/language.

        """
        font_size = figsize[0] * 1.5 # Scale font size to `figsize` input
        data_sorted = self.fertilities.sort_values(by='fertility')

        plt.figure(figsize=figsize)
        plt.grid(axis='y', alpha=0.7, zorder=0)
        plt.bar(data_sorted['language'], data_sorted['fertility'], color=color, zorder=2)

        plt.xlabel('Language', fontsize=font_size)
        plt.ylabel('Fertility Score', fontsize=font_size)
        plt.title('Fertility Scores by Language', fontsize=font_size)

        plt.xticks(fontsize=font_size)
        plt.xticks(rotation=90, fontsize=font_size)
        plt.yticks(fontsize=font_size)

        plt.tight_layout()
        plt.show()

    def help_paritize(self, row, text_col1, text_col2): 
        """ 
        Get the parity score for a given text. Serves as helper function 
        for `paritize`.

        Parameters
        ----------
            - text (str): text for tokenization
            - tokenizer (tokenizer): model/tokenizer 
              (optional, defaults to `meta-llama/Llama-3.2-1B-Instruct`)

        Returns
        -------
            - score (float): parity score
        """ 
        sA_tokens = self.tokenizer.tokenize(row[text_col1])
        sB_tokens = self.tokenizer.tokenize(row[text_col2])
        return len(sA_tokens) / len(sB_tokens) if len(sB_tokens) > 0 else float('inf')

    def paritize(self, text_col1, text_col2): 
        """ 
        Get parity scores and tokens for a dataset of texts in different languages. 
        
        Returns
        -------
        scored (pd.DataFrame): DataFrame with `text`, `text2`, `parity`, and `model` columns
        
        """
        # def compute_parity(row):
        #     sA_tokens = self.tokenizer.tokenize(row['text'])
        #     sB_tokens = self.tokenizer.tokenize(row['text2'])
        #     return len(sA_tokens) / len(sB_tokens) if len(sB_tokens) > 0 else float('inf')

        scored = self.data[[text_col1, text_col2]].copy()
        scored['parity'] = scored.apply(lambda row: self.help_paritize(row, text_col1, text_col2), axis=1)
        self.parities = scored 

        return scored    

