# Wiki Scrape

A standalone Python file that utilizes requests and BeautifulSoup to get and sort all referenced Wikipedia links on a given Wikipedia article. It was built as a quick prototype to explore the possibility of developing the "Rabbit Hole" platform

### Usage

When prompted enter the name of the starting Wikipedia article. The program will then prompt you to choose one of the articles found on that page to visit (after listing all of the referenced articles). After entering the next article all of the articles found on that page and the process continues. 

The program also keeps track of your thread which is the chain of articles you have visited. 

A possible use case of this program would be while taking part in a "Wikipedia Game." In this game the player is prompted with a starting Wikipedia article and tasked with arriving on the destination article using only clinking links, no searching allowed.
