# NLP-Test-software
**Overview**

Program: crawlTextFromWeb

![image](https://github.com/thenewcomer/NLP-Test-softeware/blob/master/introductionImages/crawlTextFromWeb.png)

This program is a Scrapy project. Except "getSentences.py", "stopwords.txt", and "usedUrls.txt", other files are created automatically by Scrapy.

Program: cleantext.py, word2vector.py

![image](https://github.com/thenewcomer/NLP-Test-softeware/blob/master/introductionImages/textPrograms.png)

cleantext.py cleans the original text and output clean text. word2vector.py trains the clean text and output a visualized result image.

Folder: introductionImages, resultImages

Folder "introductionImages" contains some images which are used to introduce this project and folder "resultImages" contains some images which are used to show the results.

**Requirements**

Python 2.7 or Python 3.3+

Scrapy

TensorFlow

Here are some useful links:

Scrapy Tutorial: https://doc.scrapy.org/en/1.2/intro/tutorial.html

TensorFlow Tutorial: https://www.tensorflow.org/get_started/get_started

**Run Crawler**

Go to program crawlTextFromWeb's top level directory and run:

```python
scrapy crawl crawlText
```

**Steps and Results** 

1. Crawling data from Wikipedia. When I enter a web page, I save all the body texts to an output file and all URLs to a new URLs list. Scan the new URLs list and delete the URLs which have been used or link to pictures, icons, other languages or other useless pages. Choose an URL to enter and delete it from the new URLs list and add it to the used URLs list. I collect 1063 pages and 200M uncleaned text in total.

2. Cleaning data. I remove all the special characters and check every word to determine whether it is a valid English word. 

   ![image](https://github.com/thenewcomer/NLP-Test-softeware/blob/master/resultImages/originalData.png)

   ![image](https://github.com/thenewcomer/NLP-Test-softeware/blob/master/resultImages/cleanData.png)

3. Tagging the texts and show the results.

   ![image](https://github.com/thenewcomer/NLP-Test-softeware/blob/master/resultImages/tag%20result.png)

4. Saving the clean data to file.

5. Using word2vec to train these texts and visualize the results. 

   ```python
   embedding_size = 50  # Dimension of the embedding vector.
   ```

   ![image](https://github.com/thenewcomer/NLP-Test-softeware/blob/master/resultImages/tsne.png)

  More details:   
   ![image](https://github.com/thenewcomer/NLP-Test-softeware/blob/master/resultImages/word2vec_detail.jpg)

