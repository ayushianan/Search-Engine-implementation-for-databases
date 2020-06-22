# Search Engine Implementation for database
* Database: MongoDB
* Data structure: Inverted Index
-------------------------------------------
## Dependencies Required
* Python3
* MongoDB
* Qt-Creator 
--------------------------------------------
## File System
1. **Storage.py** : Creates the folder "New Testament" and stores txt files in it.
2. **parsing.py** : Contains methods to clean and store data in the database.
3. **browser.py** : Responsible for designing GUI using PyQt4 modules and Qt-Creator.
4. **querying.py** : Contains methods to rank the documents according to their frequencies.
5. **main.py** : It ranks the documents according to their searched word frequency count with a summarised text detail.
-----------------------------------------------
> ## Inverted Index
> An inverted index is an index data structure storing a mapping from content, such as words or numbers, to its locations in a document or a set of documents. In simple words, it is a hashmap like  data structure that directs you from a word to a document or a web page.
> ## Steps to build an inverted index:
>   * **Fetch the Document**
Removing of Stop Words: Stop words are most occuring and useless words in document like “I”, “the”, “we”, “is”, “an”.
> * **Stemming of Root Word**
Whenever I want to search for “cat”, I want to see a document that has information about it. But the word present in the document is called “cats” or “catty” instead of “cat”. To relate the both words, I’ll chop some part of each and every word I read so that I could get the “root word”. There are standard tools for performing this like “Porter’s Stemmer”.
> * **Record Document IDs**
If word is already present add reference of document to index else create new entry. Add additional information like frequency of word, location of word etc.
Repeat for all documents and sort the words.