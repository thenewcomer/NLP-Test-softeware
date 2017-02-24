import scrapy
from scrapy.linkextractors import LinkExtractor

#Import these libraries to handle these errors: DNSLookupError, HttpError, TimeoutError
from twisted.internet.error import DNSLookupError
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import TimeoutError

#Start page: the home page of Wikipedia
url = 'https://en.wikipedia.org/wiki/Main_Page/'

#Many of wiki's URLs are incomplete, like:"/wiki/Epsilon_Eridani", so I should add a head to make it valid
urlHead = 'https://en.wikipedia.org'

#Count how many pages have been crawled
pageCount = 0

#When 10000 pages have been crawled, stop obtain more pages
totalPagesCrawl = 10000

#The list that saves all the new URLs
allNewUrls = []

#The used URLs should not be used again, so I should save these URLs to a file and check every new URL whether it has been used
usedFileName = "usedUrls.txt"

#The list that saves all the used URLs, I will check the used URLs many times, so read them from memory is faster than read them from file
usedUrls = []

#Many URLs link to images or icons, I should ignore these URLs.
#These URLs usually contain some particular words like "png", "icon", "pdf", "php" and so on.
#I will read the stop words from "stopWordFile" to list "stopWords".
#In this way I can modify stop words without change my code.
stopWordFile = "stopwords.txt"
stopWords = []

#The name of the file which will save the results
filename = "textfile.txt"


class getSentences(scrapy.Spider):
    handle_httpstatus_list = [404, 401, 403, 500, 502, 503, 504] #If these error codes are returned, I will handle these errors by myself
    name = "crawlText"
    global stopWords
    stopfile = open(stopWordFile)
    for line in stopfile:
        stopWords.append(line) #Load stop words from file to list "stopWords"
    print("-----------------", stopWords)
    def start_requests(self):
            global usedUrls
            #Config the request
            request = scrapy.Request(url=url, callback=self.parse, dont_filter=True, errback=self.errback_httpbin)
            #Config the cookies and headers, in this way our requests will look like the requests which are sent by browsers
            #So we can avoid being banned by Wikipedia
            request.cookies['over18'] = 1
            request.headers['User-Agent'] = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
            #Load usedUrls from file to list "usedUrls"
            with open(usedFileName) as usedfile:
                usedUrls = usedfile.readlines()
                usedUrls = [x.strip() for x in usedUrls]
            #Send request: will visit the home page of Wikipedia
            yield request

    #The callback function of request
    def parse(self, response):
            global pageCount
            global allNewUrls
            global usedUrls
            hasAttributeError = False #Indicate whether there are any AttributeErrors
            if response.status == 200: # If status == 200 means the response is OK
                pageCount = pageCount + 1 #This page is valid, the pageCount should +1
                print("page number is : ", pageCount)
                '''
                    get text of this page and save it to file
                    '''
                #The variable "response" may not have the attribute xpath,
                #In this case it may trigger an attributeError. I will set the indicator "hasAttributeError" to true
                try:
                    text = response.xpath('//body//text()').extract()
                except AttributeError:
                    hasAttributeError = True
                    print("Have AttributeError = ", hasAttributeError)
                #If the indicator hasAttributeError == true, then I will abandon this web page and continue crawling next url
                #If the indicator hasAttributeError == false, then I will add the texts of this page to the file "textfile.txt"
                if not hasAttributeError:
                    with open(filename, 'a') as textfile:
                        for i in range(0,len(text)):
                            textfile.write(text[i].encode('utf-8'))
                        textfile.write("\n".encode('utf-8'))
                    '''
                        get all the URLs of this page and delete the used ones
                        use these new URLs to craw
                    '''
                    validUrl = True
                    if pageCount < totalPagesCrawl:
                        urls = response.xpath('//*//@href').extract()
                        for i in range(0, len(urls)):
                            #If "http" not in this url, which means this url is incomplete, I should add a head to this url
                            if "http" not in urls[i]:
                                urls[i] = urlHead + urls[i]
                        #Remove the used URLs, the URLs in list newUrls havn't been used but may invalid
                        newUrls = list(set(urls) - set(usedUrls))
                        #If one url contain any stop words, then it is invalid and will be ignored
                        for i in range(0, len(newUrls)):
                            for j in range(0, len(stopWords)):
                                if stopWords[j].strip() in newUrls[i]:
                                        validUrl = False
                            if validUrl:
                                allNewUrls.append(newUrls[i])
                    #If all new URLs have been crawled, save the used URLs to file
                    if len(allNewUrls) <= 0:
                        with open(usedFileName, 'wb') as saveusedfile:
                            for i_used in range(0, len(usedUrls)):
                                saveusedfile.write((usedUrls[i_used] + "\n").encode('utf-8'))
            #If there are some new and valid URLs need to be crawled
            if len(allNewUrls) > 0:
                print("here is nextUrl ------------", allNewUrls[0])
                nextUrl = allNewUrls[0]
                del allNewUrls[0] #delete this url from the list newUrls
                usedUrls.append(nextUrl) #add this url to the list usedUrls
                #Config request
                #dont_filter=True               means don't help me filt URLs I will do it myselfe
                #errback=self.errback_httpbin   means if there is any error occurs, the callback function errback_httpbin will handle it
                #                               if I don't do this, the program will be interrupted automatically when any error occurs
                request = scrapy.Request(url=nextUrl, callback=self.parse, dont_filter=True, errback=self.errback_httpbin)
                #Send request
                yield request
    #The error callback function
    #In this program we will ignore these error pages and just start crawling next page
    def errback_httpbin(self, failure):
            if failure.check(HttpError): #HttpError, skip this page, continue
                    print("HttpError")
            elif failure.check(DNSLookupError): #DNSLookupError, skip this page, continue
                    request = failure.request
                    self.logger.info('DNSLookupError on %s', request.url)
            elif failure.check(TimeoutError): #TimeoutError, skip this page, continue
                    print("TimeoutError")
            #If the list "allNewUrls" is not emputy, crawl next page
            if len(allNewUrls) > 0:
                    nextUrl = allNewUrls[0]
                    del allNewUrls[0]
                    request = scrapy.Request(url=nextUrl, callback=self.parse, dont_filter=True, errback=self.errback_httpbin)
                    yield request







