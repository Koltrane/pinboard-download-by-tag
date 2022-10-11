# Pinboard export bookmarks by tags

after going through a lot of random iterations, the easiest way to do this is to just curl the pinboard API directlly and then parse the xml with xmltodict. 

I tried to make one of the pinboard python libraries work, but it would not give the fully-speced bookmark, just the top level. feh.

This script creates the file `bookmarks.md` which has a date and time stamp that matches when the bookmarks were retrieved.

