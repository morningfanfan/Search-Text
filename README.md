###Before you run:
The result of the program is based on the following prerequisites:

* Character '\n' semantically doesn't equal to '&nbsp;<space> ', which means the algorithm would ignore the case if the searching string needs to be concatenated from multi-lines.
* Only a simple rule is applied to divide sentences(by finding '.', '!', '?' or '&nbsp;<space>  &nbsp;<space> ' to define a start and '!', '.', '?' to define an end). This cannot work well under the circumstance when a name entity contains '.', for example, Washington D.C. in the _king-i.txt_ text file.
*  When changing the value of ngram in the code, a trade-off can be made between  the running speed and the memory space, by having higher speed with more memory space or having lower speed with less memory space.

###Usage:

Run the test cases for testing the work of our algorithm under three different circumstances:

~~~
cd ./Search-Text

python3 tests/test_algorithm.py

~~~


Run it locally:
	
~~~~
cd ./Search-Text

pip3 install -r requirements.txt

python3 src/app.py
	
~~~~

Run by built an image from the Dockerfile(for deployment):
	
~~~~

cd ./Search-Text

docker build -t flask-search-app:latest .

docker run -it flask-search-app
	
~~~~

By default, the application would be running at **localhost:8080**. To search a string, simplely add the string to the URL. For example, search string 'dream' by **localhost:8080/dream**.
