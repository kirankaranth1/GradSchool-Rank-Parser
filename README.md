# GradSchool-Rank-Parser  
  
This parser logs information about US universities offering Computer Science Graduate courses according to their ratings in a csv. 
Data is parsed from http://grad-schools.usnews.rankingsandreviews.com/best-graduate-schools/top-science-schools/computer-science-rankings  

#Usage

1) Set URL in the url variable in parser.py  
2) Number of pages to parse are hardcoded in the parser script as of now (Line 12). Currently this is set to 6.

#Notes

The data is parsed from webpage based on xpath location. Column number 4 is not parsed as its xpath does not exist on each page in the us news website  
