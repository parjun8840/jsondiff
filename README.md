# Jsondiff

Jsondiff is a Python module to compare two json files.

## Use Case

(1)  Find the common key, which have different values.

(2) Keys present only in File1.

(3) Keys present only in File2. 


## Usage

```
C:\Users\parjun8840\eclipse-workspace\PythonDev>python jsondiff.py --help
usage: jsondiff.py [-h] [-f1 FILE1_PATH] [-f2 FILE2_PATH]

JSON DIFF

optional arguments:
  -h, --help            show this help message and exit
  -f1 FILE1_PATH, --FILE1_PATH FILE1_PATH
                        First Json File
  -f2 FILE2_PATH, --FILE2_PATH FILE2_PATH
                        Second Json file
C:\Users\parjun8840\eclipse-workspace\PythonDev>

Scenario 1: Both files same content
Input files used: json_dict1 ,json_dict1  have same content
{"test1": "1", "test2" : "2", "test3" : "abcd", "test4" : "xyz", "test5" : "12ab", "test6" : "12ab" }

C:\Users\parjun8840\eclipse-workspace\PythonDev>python jsondiff.py -f1 json_dict1 -f2 json_dict2
INFO: Files exists and non-empty
JSON files are same
C:\Users\parjun8840\eclipse-workspace\PythonDev>

Scenario 2: When one of the file has extra key and other one has different value for the same key.
C:\Users\parjun8840\eclipse-workspace\PythonDev>python jsondiff.py -f1 json_dict1 -f2 json_dict2
INFO: Files exists and non-empty
Key is common with different value: {'test5'}
Key present only in file: json_dict2- {'test6'}
C:\Users\parjun8840\eclipse-workspace\PythonDev>



```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
None