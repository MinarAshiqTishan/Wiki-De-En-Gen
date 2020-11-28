# Wiki-De-En-Gen
 
### Description
----------------------------------------------------------

Generate  German word list from Wiki with English meaning as a CSV

- download wiki page with wikipedia-api as text    
- read the text , generate the unique german words list
- translate the words with dictcc API
- generate csv with pandas
    -- delimiter:  ';' 
   
### Usage
----------------------------------------------------------

Give the following arguments to generate.py. Put no space after parameter.

-    --i=input filename or wiki title e.g. sometext.txt or Apfel
-    --o=outfile filename e.g. somecsv.csv
-    --d=delimiter character e.g. ;
-    --n=no of translations e.g. 1\n',
-    --s=source of de 'wiki' or 'local' file

sample call: 

          python.exe generate.py --i=Apfel --o=Apfel.csv --d=; --n=1 --s=wiki
      
or from dist:
          
          generate.exe --i=Apfel --o=Apfel.csv --d=; --n=1 --s=wiki

### Installation
----------------------------------------------------------
- if downloaded to a local folder, run pip :
        
        pip install ./folder_name_of_Wiki-De-En-Gen
