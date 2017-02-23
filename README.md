# NLP-Test-softeware
**Overview**

Program: crawlTextFromWeb

![image](https://github.com/thenewcomer/NLP-Test-softeware/blob/master/introductionImages/crawlTextFromWeb.png)

This program is a Scrapy project. Except "getSentences.py", "stopwords.txt", and "usedUrls.txt", other files are created automatically by Scrapy.

Program: cleantext.py, word2vector.py

![image](https://github.com/thenewcomer/NLP-Test-softeware/blob/master/introductionImages/textPrograms.png)

cleantext.py clean the original text and output clean text. word2vector.py train the clean text and output a visualized result image.

Folder: introductionImages, resultImages

some Images which are used to introduce this project or show the results.

**Requirements**

Python 2.7 or Python 3.3+

Scrapy

TensorFlow

Here are some useful links:

Scrapy guide: https://doc.scrapy.org/en/1.2/intro/install.html

TensorFlow Tutorial: https://www.tensorflow.org/get_started/get_started

**Work describtion** 

1. Crawl data from wikipedia. When I enter a web page, I save all the body texts to output file and all urls to a new urls list. Scan the new urls list and delete the urls which have been used or link to pictures, icons, other languages or other useless pages. Choose an url to enter and delete it from the new urls list and add it to the used urls list. I collect 1063 pages and 200M uncleaned text in total.

2. Clean data. I remove all the special characters and check every word to determine whether it is a valid english word. 

   ![image](https://github.com/thenewcomer/NLP-Test-softeware/blob/master/resultImages/originalData.png)

   ![image](https://github.com/thenewcomer/NLP-Test-softeware/blob/master/resultImages/cleanData.png)

3. Tag the texts and show the results.

   ![image](https://github.com/thenewcomer/NLP-Test-softeware/blob/master/resultImages/tag%20result.png)

4. Save the clean data to file.

5. Use word2vec to train these texts and visualize the results. 

   embedding_size = 50  # Dimension of the embedding vector.
   ![image](https://github.com/thenewcomer/NLP-Test-softeware/blob/master/resultImages/tsne.png)

  More details:   
   ![image](https://github.com/thenewcomer/NLP-Test-softeware/blob/master/resultImages/word2vec_detail.jpg)

