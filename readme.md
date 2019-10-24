## Requirements
* Requires Python3+


## Install
1. Install dependencies locally
    * Inside of the project folder:
        * `pip install --target python_modules  -r requirements.txt`
    * Move up one directory and run the program `python3 <yourfoldername> amd64`

## Run
* The config file has adjustable parameters with sane defaults.

## Project Summary
* This was an interesting project, that tested multiple facets of development:
 file system usage, parsing files, http requests, some light algorithms,
 dealing with non trivial data sets. 
 
* I viewed this as basically a hot caching problem. 
 Finding the top elements from a set of millions of data points.
 The hot cache keeps track of the top elements and their quantities and 
 when a element with a bigger quantity is found it boots the smallest element 
 out of the hot cache.

* I spent probably around 4 hours working on this.

## Testing
* This has not been unit or integration tested.
* Grepping the file with a regex for the program, however, outputs the exact same counts as the python program.
    * `grep -i '.*fonts/texlive-fonts-extra.*' /tmp/Contents-amd64.txt | wc -l`

## Potential performance Improvements
* Multiprocessing on the file parsing.   
* Check for a local file and ask to use that, if present. 
