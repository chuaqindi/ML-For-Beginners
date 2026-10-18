# NLP quiz answers

English quiz IDs 31–40. Answers match the repository question bank; explanations flag historical APIs and simplifications.

## Quiz 31: Intro to NLP: Pre-Lecture Quiz

1. What does NLP stand for in these lessons?  
   **Answer:** natural language processing  
   NLP concerns computational processing of human language.
2. Eliza was an early bot that acted as a computer  
   **Answer:** therapist  
   The lesson uses ELIZA as an early example of a simulated therapeutic conversation.
3. Alan Turing's 'Turing Test' tried to determine if a computer was  
   **Answer:** both of the above  
   The source answer combines its two descriptions of a conversational imitation test; it is not a proof of human-like understanding.

## Quiz 32: Intro to NLP: Post-Lecture Quiz

1. Joseph Weizenbaum invented the bot  
   **Answer:** Eliza  
   The lesson attributes ELIZA to Joseph Weizenbaum.
2. A conversational bot gives output based on  
   **Answer:** Both of these  
   Bots may use rules or learned patterns to select replies.
3. How would you make the bot more effective?  
   **Answer:** By feeding it more data and training it accordingly  
   Useful representative data and evaluation matter; more data alone cannot guarantee better behavior.

## Quiz 33: NLP Tasks: Pre-Lecture Quiz

1. Tokenization  
   **Answer:** Splits text into separate tokens (words)  
   Token boundaries need conventions for punctuation, language, and contractions.
2. Embeddings  
   **Answer:** converts text data numerically so words can cluster  
   Embeddings represent tokens numerically so context-related items can be compared.
3. Parts-of-Speech Tagging  
   **Answer:** takes tokenized words and tags them by their part of speech  
   Tags identify grammatical categories such as noun and verb.

## Quiz 34: NLP Tasks: Post-Lecture Quiz

1. Build a dictionary of how often words reoccur using:  
   **Answer:** Word and Phrase Frequencies  
   A frequency table records repeated words or phrases.
2. N-grams refer to  
   **Answer:** A text can be split into sequences of words of a set length  
   An n-gram is a contiguous sequence of n tokens.
3. Sentiment analysis  
   **Answer:** analyzes a phrase for positivity or negativity  
   Sentiment estimates expressed polarity; it need not recover irony or author intent.

## Quiz 35: NLP and Translation: Pre-Lecture Quiz

1. Naive translation  
   **Answer:** translates words only  
   Word-by-word translation ignores syntax and idiom.
2. A *corpus* of texts refers to  
   **Answer:** A large number of texts  
   A corpus is a body of text used for linguistic work.
3. If a ML model has enough human translations to build a model on, it can  
   **Answer:** improve the accuracy of translations  
   Aligned examples can support learning translation patterns; evaluation remains necessary.

## Quiz 36: NLP and Translation: Post-Lecture Quiz

1. Underlying TextBlob's translation library is:  
   **Answer:** Google Translate  
   This is the historical lesson answer. Current TextBlob removed its translation methods in version 0.18.0.
2. To use `blob.translate` you need:  
   **Answer:** an internet connection  
   This describes the retired service-backed method; it is not a working call in the pinned current package.
3. To determine sentiment, an ML approach would be to:  
   **Answer:** apply NLP techniques to manually generated opinions and scores and look for patterns  
   Labeled opinions and scores provide examples for supervised learning and held-out evaluation.

## Quiz 37: NLP 4: Pre-Lecture Quiz

1. What information can we get from text that was written or spoken by a human?  
   **Answer:** both of the above  
   Text can expose frequency patterns and expressed affect; neither guarantees comprehension.
2. What is sentiment analysis?  
   **Answer:** a method of systematically identifying, extracting, quantifying, and studying affective states and subjective information  
   The source definition concerns systematic analysis of affect and subjectivity.
3. What question could be answered using a dataset of hotel reviews, Python, and sentiment analysis?  
   **Answer:** What are the most frequently used words and phrases in reviews?  
   Word and phrase frequency can be measured directly on the review text.

## Quiz 38: NLP 4: Post-Lecture Quiz

1. What is the essence of NLP?  
   **Answer:** interpreting meaning or sentiment without having to have a human do it  
   This is the lesson phrasing; automatic interpretation is an estimate that still benefits from human validation.
2. What are some things you might look for while cleaning data?  
   **Answer:** both of the above  
   Missing values and inconsistent formats are among the data quality issues to investigate.
3. It is important to understand your data and its foibles before performing operations on it.  
   **Answer:** true  
   Understanding sampling, placeholders, and aggregation prevents misleading analysis.

## Quiz 39: NLP 5: Pre-Lecture Quiz

1. Why is it important to clean data before analyzing it?  
   **Answer:** Both of the above  
   Relevant, consistently represented data makes analysis easier to interpret.
2. What is one example of a strategy for cleaning data?  
   **Answer:** removing columns/rows that aren't useful for answering a specific question  
   Removing irrelevant columns can help, provided the analysis question and audit needs are preserved.
3. It can be useful to categorize data using a Tag column.  
   **Answer:** true  
   Useful tags can encode trip or guest type after validating their format and meaning.

## Quiz 40: NLP 5: Post-Lecture Quiz

1. What is the goal of the dataset?  
   **Answer:** to add sentiment and columns that will help you choose the best hotel  
   The lesson prepares features for choosing hotels, but it does not establish recommender performance.
2. What are stop words?  
   **Answer:** both of the above  
   Common words are often called stopwords. Negators and intensifiers can still be essential to sentiment.
3. To test the sentiment analysis, make sure it matches the reviewer's score for the same review.  
   **Answer:** true  
   This is the expected quiz answer. A rating comparison is a sanity check, not proof of sentiment accuracy or a requirement for perfect agreement.
