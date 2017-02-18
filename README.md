# NLP-Test-softeware
work describtion 

1. Crawl data from wikipedia. When I enter a web page, I save all the body texts to output file and all urls to a new urls list. Scan the list delete the urls which are used or link to pictures, icons, other languages and other useless pages. Choose an url to enter and delete it from new urls list and add it to the used urls list. I collect 1063 pages and 200M uncleaned text in total.

2. Clean data

3. Tag the texts and show the results.

   ![image](https://github.com/thenewcomer/NLP-Test-softeware/blob/master/tag%20result.png)
   
4. Save the clean data to file.

5. Use word2vec to train these texts and visualize the results. 

   embedding_size = 50  # Dimension of the embedding vector.
   ![image](https://github.com/thenewcomer/NLP-Test-softeware/blob/master/tsne.png)

   <figure class="third">
    <img src="https://github.com/thenewcomer/NLP-Test-softeware/blob/master/word2vec01.png">
    <img src="https://github.com/thenewcomer/NLP-Test-softeware/blob/master/word2vec02.png">
   </figure>

