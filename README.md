#'Archive Of Our Own' Scraper Tool

This tool is built to retrieve the full body of works from any fandom on the fanfiction site 'archiveofourown.org'.

Running it requires some arguments. For example:

`Python3 parser.py "text value" -s -t "dir"`

* "text value" represents the link to all the works in a tag, the tag itself, or a possible tag to search for alternatives, depending on the flags
* "-s" determines if you want to search for possible alternate tags
* "-t" determines if you want to get works based off the tag you put in
* "dir" represents the directory you want the scraped works to go

Only runs using Python 3. Make sure Python 3 is installed on your system, and if Python 3 isn't the default version, run as Python3 in the shell
