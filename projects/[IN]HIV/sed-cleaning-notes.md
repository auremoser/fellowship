##HIV@30
####Cleaning Process Notes
Rename extension = select all files, change extension from .docx to .txt

Remove initial numerals:
for i in *DN*.txt; do mv $i ${i/*DN/DN}; done

Reorder date:
echo 01DN021288.txt | perl -pe 's/(..)(..)(....)(..)/$4$3$1$2

or try 
echo 01DN310888.txt | sed 's/\(....\)\(..\)\(..\)\(..\)/\4\3\2\1/'

to reorder date in a directory

echo *DN.txt | perl -pe 's/(..)(..)(....)(..)/$4$3$1$2

Tried to setup overview account
aurelia@ushahidi.com

###HIV@30
#####FILE CLEANING IN TERMINAL
Here's a quick worflow for converting documents from the Overview export format:
Like this: 
01DN021388.docx
To this:
YYMMDD##DN.txt
This will make it easier to process them as a batch with Chambua.
######CONVERT EXTENSION  

`textutil -convert txt /Users/aurelia/Desktop/rename-test/*.docx`

In the folder where you store your files (on windows/mac) you can look in Finder at the files, navigate in the menu to View > Arrange by (or Sort by on windows) > Application (or Date Created) this will group all of the .txt files so that you can save them to another directory.[^1]

[^1]: Revised to use [Pandoc](http://johnmacfarlane.net/pandoc/), a python library that does document conversion

######RESTRUCTURE FILE NAMES

In this case, I am reading into a directory (paty/to/files) and piping it to a sed script which will rename them according to a set structure.
To test the script in terminal:
`ls ~/Desktop/rename-batch | sed 's/\(....\)\(..\)\(..\)\(..\)/\4\3\2\1/'`
To execute the tested script once satisfied with the results:
`ls *.txt | sed -e 's/\(....\)\(..\)\(..\)\(..\)/mv \1\2\3\4.txt \4\3\2\1/' | sh`

######ELIMINATE HYPHENS IN TEXT BODY

Edit files in place (-i) replace '-' with space (//) globally (g) in all .txt files.

`sed -i s/-//g' .txt`

`ls *.txt | sed -i 's/-//g'| sh` 

`for file in *.txt; do sed -i '' 's/-/ /g' $file; done`[^2]

[^2] Using a new method for a few reasons: First, on mac, sed errors out with the sed: 1: "...": invalid command code. I think it's expecting an extension or something, so we just pass it an empty string ''.

Second, it wanted a file name to write to, the only way I could make it work was by using a for loop instead of an ls and piping the output. We do the for loop and get a handle to the filename; do for file in *.txt, we are storing the name in the variable file, and then we can reference it by appending the $ sign, $file.


######BATCH PROCESSING - CHAMBUA
I can then write a script to go over all directories and autopull tags)
I did a sample version of this with a sample_text.txt document and it worked (extracted entities and person/institution and place in JSON and printed them in terminal).   

![Chambua](https://raw.githubusercontent.com/auremoser/images/master/chambua.png)

`curl -H "Content-Type:application/json" -X POST -d @sample_data.txt http://chambua.ushahidi.com/v1/tags`

{"people": ["Mombesa", "P.Mueka", "Achola", Mueke]....

I will work with EK at Ushahidi this next week to incorporate medical vocabulary from Freebase into Chambua, to get an idea for entities.

######NOTE ON SPELL CHECK
I'm not sure it's that devastating, once the "-" error is fixed I think we can probably weed most of the posts that we'll pull dynamically on a manual basis. Even after doing the '-' sed script, I realized that not many of the 1980s documents were "-"ated.

####HIV@30 4/14/14
#####COMPONENTS
3 in one timeline: media coverage, scientific, factoid

Semantic Analysis

Infographics - prefab (media, scientific, factoid)

Multimedia piece

----------------
#####Data Cleaning Process
* extract/scrape article
* check name (02DN081588.docx)
* spell check document
* rewrite if just a line, put in "problem file" otherwise
* upload scraped/clean files to dropbox (https://www.dropbox.com/sh/jit3zscakt0cg3e/l-a9zaUUgz)
* spend a maximum of 15 minutes > problem folder
* try to make sure that you have at least **2-3 documents** that are legible per year
* if feeling particularly adventurous, use Aggrey's Convert to TXT program to clean up files by column
* Aurelia will process the files from there

NEXT TIME
* we'll discuss the amount of "problem files" per decade
* we'll discuss the chambua readings 
* we'll discuss a way to analyze subjective sentiment (good, bad freighted articles) over each period


-------------------
##1980s (4/22/14)
###Documentation

`cd Desktop/HIV_30/1980s-corrected/`  

//check writability
`ls -l`

//make writeable  

`chmod 777 ~/Desktop/HIV_30/1980s-corrected`

//change file name
test  
`ls ~/Desktop/HIV_30/1980s-corrected | sed 's/\(....\)\(..\)\(..\)\(..\)/\4\3\2\1/'`  

* Lookout for things that terminate in -SA.txt or -1.txt we will need to manually reformat them
* Lookout for extras of the same date to make sure they are not duplicates (marked as "DUPE" in my directory)

(mkdir SA mv all files that are wonky into that, correct them, run sed script | sh again)


//delete hyphens  
`for file in *.txt; do sed -i '' 's/-/ /g' $file; done`  

* Wrap text in {"text":""}
* Run Chambua in terminal to extract people, institution, place entities

###Results
Results by file (two per year):
#####1981
`@81070814DN.txt`  

 {"people":["r. Curran"],"organizations":["Kaposi","LSI"],"places":[{"name":"California","latitude":37.25022,"longitude":-119.75126,"place_type":"Adm"},{"name":"US","latitude":39.76,"longitude":-98.5,"place_type":"Country"},{"name":"New York","latitude":43.00035,"longitude":-75.4999,"place_type":"Adm"}]}

#####1983
`@83080906DN.txt`  

{"people":["Mr Roger Barilliet.secretary","Piet J.Hspn","Juhan Likola","Mr Frank Schnabel"],"organizations":["Shl","World Health OrganisationGeneva","International Red Çrosa","Bayer","Montreal.based World Federation","Revlon","United","French Government"],"places":[{"name":"France","latitude":46.0,"longitude":2.0,"place_type":"Country"},{"name":"America","latitude":39.76,"longitude":-98.5,"place_type":"Country"},{"name":"US","latitude":39.76,"longitude":-98.5,"place_type":"Country"},{"name":"Associa","latitude":34.7666,"longitude":137.3833,"place_type":"Hotel"},{"name":"Paris","latitude":48.85339,"longitude":2.34864,"place_type":"Adm"},{"name":"Europe","latitude":43.5333,"longitude":3.9833,"place_type":"Hotel"}]}  
  
`83121206DN.txt`  
{"people":["Walter Dowclle.who","Brunet"],"organizations":["Ufl","Centrefor Disease Control","Tel Aviv Medical","Western Africa","Upper CongoBasin","United Stan"],"places":[{"name":"United States","latitude":39.76,"longitude":-98.5,"place_type":"Country"},{"name":"North America","latitude":35.50069,"longitude":-80.00032,"place_type":"Adm"},{"name":"Mali","latitude":17.0,"longitude":-4.0,"place_type":"Country"},{"name":"Americas","latitude":16.51667,"longitude":-90.64389,"place_type":"City"},{"name":"Gabon","latitude":-1.0,"longitude":11.75,"place_type":"Country"},{"name":"Europe","latitude":43.5333,"longitude":3.9833,"place_type":"Hotel"},{"name":"Israel","latitude":31.5,"longitude":34.75,"place_type":"Country"},{"name":"Haiti","latitude":19.0,"longitude":-70.66667,"place_type":"Country"},{"name":"San Francisco","latitude":37.77668,"longitude":-122.42031,"place_type":"GisFeature"},{"name":"New York","latitude":43.00035,"longitude":-75.4999,"place_type":"Adm"},{"name":"Canada","latitude":60.0,"longitude":-96.0,"place_type":"Country"},{"name":"Africa","latitude":-30.0,"longitude":26.0,"place_type":"Country"},{"name":"Australia","latitude":-25.0,"longitude":135.0,"place_type":"Country"},{"name":"Japan","latitude":35.68536,"longitude":139.7531,"place_type":"Country"}]}

#####1985
`@85073102DN.txt`  
{"people":["Rock Hudson"],"organizations":["specialAir France Boeing"],"places":[{"name":"Paris","latitude":48.85339,"longitude":2.34864,"place_type":"Adm"},{"name":"LosAngeles","latitude":1.80128,"longitude":-75.39373,"place_type":"GisFeature"}]}  

`85103102DN.txt`  
{"people":["Robin Weiss","Anne Bayley"],"organizations":["Institute ofCancer Research","UniversityHospital"],"places":[{"name":"Zambia","latitude":-15.0,"longitude":30.0,"place_type":"Country"},{"name":"Lusaka","latitude":-15.40669,"longitude":28.28713,"place_type":"City"}]}

#####1986
`@86050407SN.txt`  
{"people":["DrRuhakana Rugunda","Andrew Kakimpe"],"organizations":["Nyakibaje MissionHospital"],"places":[{"name":"Mulago","latitude":0.35,"longitude":32.58333,"place_type":"CitySubdivision"},{"name":"Tanzania","latitude":-6.0,"longitude":35.0,"place_type":"Country"},{"name":"Zaire","latitude":0.0,"longitude":25.0,"place_type":"Country"},{"name":"Rakai","latitude":-0.61556,"longitude":31.5175,"place_type":"City"},{"name":"Uganda","latitude":2.0,"longitude":33.0,"place_type":"Country"},{"name":"Kampala","latitude":0.31628,"longitude":32.58219,"place_type":"City"},{"name":"Rwanda","latitude":-2.0,"longitude":30.0,"place_type":"Country"},{"name":"Masaka","latitude":-0.33379,"longitude":31.73409,"place_type":"City"}]}
  
`86100220DN.txt`  
{"people":["M. Owili","Siongok","Owilj","Dr. T. K. ampSwngok"],"organizations":["Humanlmmunodeticiency Virus"],"places":[{"name":"Europe","latitude":43.5333,"longitude":3.9833,"place_type":"Hotel"}]}

#####1987
`87020517DN.txt`  
{"people":["N. N. Àgata"],"organizations":["Kenya Medical Research","Univer"],"places":[{"name":"Nairobi","latitude":-1.28333,"longitude":36.81667,"place_type":"City"}]}

`87030508DN.txt`  
{"people":["Mann","DrJonathan Mann"],"organizations":["Aida","DrMann","WorldHealth Organisation"]}

#####1988
`88020405DN.txt`  
{"people":["Maitha","G.M. Maitha"],"organizations":["Ninth Kemri•Ketri Annualedical Scientific Conference","Kenya Trypanosomiasis Research Institute","theKenya Medical Research"],"places":[{"name":"Kenya","latitude":1.0,"longitude":38.0,"place_type":"Country"},{"name":"Ndola","latitude":-12.95867,"longitude":28.63659,"place_type":"City"}]}  
  
`88020512DN.txt`  
{"people":["William Cameron","Datta","Cameron","Mr E. Itotia","Mrs Anne M. Pertet ofKemri"],"organizations":["University ofNairobi","Upjohncompany","University of Nairobi"],"places":[{"name":"Nairobi","latitude":-1.28333,"longitude":36.81667,"place_type":"City"},{"name":"Nyeri District","latitude":3.76667,"longitude":31.85,"place_type":"Mountain"},{"name":"Pumwani","latitude":-1.2,"longitude":39.98333,"place_type":"City"},{"name":"Kemri","latitude":28.81667,"longitude":79.21667,"place_type":"City"}]}

#####1989
`89013007DN.txt`  
{} Empty array :(  

`89022214DN.txt`  
{"organizations":["oNational Committee","Dutch Government","Dutch Educa.tiol Television","Rutgers Stiehting","NCAB","DutchFamilý Planning Association","Rutgers Stlchting","FPA","Rutgers Stichttng"],"places":[{"name":"West Germany","latitude":51.28333,"longitude":12.36667,"place_type":"CitySubdivision"},{"name":"Netherlands","latitude":-5.0,"longitude":120.0,"place_type":"Country"}]}  
  
`89030404DN.txt`  
{"people":["Kinuthia"],"organizations":["KenyaMedical Women Association Scientific Conference","Immuno","Kenyatta International Conference Centie","University of Nairobi Dr. Dorothy Kinuthia","Coast","College ofHealth Sciences"],"places":[{"name":"Nairobi","latitude":-1.28333,"longitude":36.81667,"place_type":"City"},{"name":"Kenya","latitude":1.0,"longitude":38.0,"place_type":"Country"}]}


####Observations
* places go from global to local (international > Nairobi)
* people become increasingly local doctors in the news, as opposed to international institutions like the CDC and other "foreign" doctors
* In 1988 for example, we see mention of more Kenyan institutions (Kenya Trypanosomiasis Research Institute, University of Nairobi, Kenya Medical Research)
* This might mean that the disease is taken more seriously locally but probably also means that the media bias has begun to address the medical opinion of local authorities
* Later (late 80s) news coverage addresses more "family planning" and "women's" associations as aids is viewed more in the context of prevention as opposed to hysteria and accusation


-------------------
##Updates for Mass Cleaning (4/28/14)
Python script to wrap file content in json can be found in the `fellowship/projects/[IN]HIV/` folder. This script uses Python in stead of sed/terminal hacks because I need to wrap each .txt file in text:{} or a JSON wrapper for Chambua, and encoding contend to be valid JSON is complicated, moreso than wrapping the file contents with a string. 

###Process:  

* Make a copy of all your files. 
* To execute the file, simple place it in your directory with all your txt files, execute with this command:
./wrap_json
* Make sure that the file has the right permissions to execute, if not, re-permission with `chmod` in Terminal.


-------------
##Updates for Mass Processing (5/12/14)
Edited the python scripts to wrap .txt files in a json object ({text:''})
Updated script to run chambua via curl on all files in a directory

###Process
* Make a copy of all your files (just in case)
* You should have a directory of .docx extension files with names like 32DN08022013.docx; we want to convert these to .txt, date-sortable files
* Navigate into the desired directory in terminal: `cd ~/Desktop/HIVat30/1980s`    

1.  #####CONVERT EXTENSION  
`textutil -convert txt /Users/aurelia/Desktop/rename-test/*.docx`
2. #####RESTRUCTURE FILE NAMES
In this case, I am reading into a directory (paty/to/files) and piping it to a sed script which will rename them according to a set structure.
To test the script in terminal:
`ls ~/Desktop/rename-batch | sed 's/\(....\)\(..\)\(..\)\(..\)/\4\3\2\1/'`
To execute the tested script once satisfied with the results:
`ls *.txt | sed -e 's/\(....\)\(..\)\(..\)\(..\)/mv \1\2\3\4.txt \4\3\2\1/' | sh`
* #####ELIMINATE HYPHENS IN TEXT BODY
Column layout for articles inserts a lot of unnecessary hyphens in our text
Edit files in place (-i) replace '-' with space (//) globally (g) in all .txt files.

`sed -i s/-//g' .txt`

`ls *.txt | sed -i 's/-//g'| sh` 

`for file in *.txt; do sed -i '' 's/-/ /g' $file; done`[^2]

[^2] Using a new method for a few reasons: First, on mac, sed errors out with the sed: 1: "...": invalid command code. I think it's expecting an extension or something, so we just pass it an empty string ''.

Second, it wanted a file name to write to, the only way I could make it work was by using a for loop instead of an ls and piping the output. We do the for loop and get a handle to the filename; do for file in *.txt, we are storing the name in the variable file, and then we can reference it by appending the $ sign, $file.  

* #####RUN CHAMBUA FOR TAG EXTRACT
Make another directory for the output files: `mkdir output`  
Download [scripts from github](https://github.com/internews-ke/hiv-30/tree/master/Sentiment_Analysis/python) and add them to your folder/directory  
Run script to wrap files in a json text object (required for Chambua to process them):  `python wrap_json.py`
Run script to go over each file in the directory and output files   
`python send_json.py -o output/`

What results is a list of extracted people/places/institions from each of the articles in each of the directories (or in this case, decades) analyzed.

###Observations







