# random word list
This script can help you generate a list of random english words. 
## method
- [words_alpha.txt](https://github.com/dwyl/english-words) is a collection of 479k english words. 
- [Reservoir Sampling](https://en.wikipedia.org/wiki/Reservoir_sampling) the above file.
## Run
To run the script, please specify the length of the word list that you want. 
```bash
$ ./random_word_list.py 4
```
Result:
```python
['indemoniate', 'miniard', 'syncretize', 'pathologicoanatomic']
```