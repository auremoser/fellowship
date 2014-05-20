SED
====

THATS WHAT SHE SED: !AWK LESSONS FROM FUN[ctional] PROGRAMMING

Somewhere at the intersection of unexpected genius, linguistic mastery, and feminitiy there's a trope of compelling fiction that goes something like this: a character (ideally a woman or weakling) speaks a language that no one expects and suddenly reveals a competency or comprehension that strengthens his or her position. This kind of surprising exolingual + monolingual situation is common and interesting (http://books.google.com/books?id=hfhclpshb8UC&printsec=frontcover#v=onepage&q&f=false). I'm thinking Daenaerys Tarygarden speaking Valerian (https://www.youtube.com/watch?v=yUWR8wvqQw8), or when Nancy Travis speaks russian to her cat callers (https://answers.yahoo.com/question/index?qid=20090314224449AA3zUpd), or the opening scene in Inglorious Basterds when the audience with subtitle advantage knows the fate of certain characters before the dramatic transition to chapter 2 (https://www.youtube.com/watch?v=8uldpQpoZQM), or that scene in the Goonies when Corey Feldman, a child, gives the maid surprising instructions en espagnol(https://www.youtube.com/watch?v=CXzglCYkqVI), or those times on the subway when I can tell who the Francaises are calling a 'whore' and giggle to myself at the semantic secrets I'm privy to by virtue of closet bilingualism. It's a common and compelling scene, not one wholy relegated to spoken tongues; it has its echoes in computational languages too.

A recent and short tumble into the land of Game of Thrones led me through the wikipedian labyrinth to LCS (http://en.wikipedia.org/wiki/Language_Creation_Society), this linguistic non-prof that constructs languages (conlangs), composed of member constructors (conlangers)[http://en.wikipedia.org/wiki/List_of_language_inventors] and the responsible creators of languages like Klingon ST and Dothraki in Game of Thrones. This tangent into a trope sparked some curiousity about how we define computer languages and how we use them thereafter. Like other languages, computational tongues are often indexed by stereotypes, and unlike other conlangs which have evolved to express a multiplicity of translatable nuances, CSlangs often are more objectively restricted by a purpose, not developed to express all of the things but rather to accomplish a task. Valarian is "the only language for poetry," while Dothraki is harsh and gutteral like its speaker population; SQL is a "special purpose" query language, Objective-C is a "general purpose" object-oriented language (http://mashable.com/2014/01/21/learn-programming-languages/); but even in these stereotypical distinctions, coders contend about what these adjectively might mean, and who is best suited to speak them in such-or-such situation.

Lately, I've been investing a bit of time in the prelims of every data project, somewhere between scoring a raw pile of data and shaping it up for a visualization, always accomplished via some language/library. New projects and experiments always make me wonder if there's a better library, plugin, resource or language to articulate my objectives and otherwise get me the results I'm after, which in this case involve a bit of OCR and semantic analysis, batch processeing and cleaning and file pruning where language all-around is pretty important. For this round of tech adventures, I settled on sed, but I'm sure the operations I'll be performing in this post could be fairly accomplished by other languages. 
Further notes can be found here: https://github.com/auremoser/fellowship/blob/master/projects/%5BIN%5DHIV/sed-cleaning-notes.md
But as a quick example, say you have a batch of files who's extentions you need to change, you can do this with text utilities:
textutil -convert txt /Users/username/path/to/directory/*.docx
This converts all docx files to .txt in a given directory.

Then say you need to restructure file names in a directory so that you can sort them, as I wanted to by date, but your current file format is something like this:
23NY080214.txt
Or ##-NY-DDMMYY.txt
You can reorder characters in a set of files by running a sed script like this:
ls ~/Desktop/path/to/directory | sed 's/\(....\)\(..\)\(..\)\(..\)/\4\3\2\1/'

This tells Terminal to break up the file name by "." to represent characters and then re-order those parenthetical entities according to the numerical set order at the end of the line (4\3\2\1) where 4=YY, 3=MM, 2=DD, 1=23NY. But this script just prints the corrections in Terminal, so let's make that reorder actionable in the directory (for each *.txt file):

ls *.txt | sed -e 's/\(....\)\(..\)\(..\)\(..\)/mv \1\2\3\4.txt \4\3\2\1/' | sh

None of these applications is really what sed was "made for," but I found them pretty satisfactory implementations of the language for my immediate need. "Taken together, all this got me thinking about linguistic development and about the "meta"-languages of programmatic thinking, the classes and cases of computational articulation that lead us toward fluency in one or more languages, preference, and eventual specialty in the operations most suited to that lexicon.

While living on a continent with ~3,000+ spoken languages (http://en.wikipedia.org/wiki/Languages_of_Africa), pigeons, and regional dialects, I also started thinking about how the diversity of computer languages compares to other paroles of parlance, and how our systems for organizing and inventing new tongues might best map to eachother for optimal productivity. 

There are rough guides for this kind of crosswalk:


And expected hierarchies(http://alfredovela.files.wordpress.com/2012/09/lenguajesprogramacion.png?w=658&h=2778), rankings (http://www.tiobe.com/index.php/content/paperinfo/tpci/index.html) and schemes  of which languages are appropriate for the most hardcore hackers (http://www.quora.com/What-is-the-best-first-programming-language-to-learn), see also "Real Programmer"(https://en.wikipedia.org/wiki/Real_Programmer) fallacy.


But to redirect the conversation to a more critical and less-subjective breakdown, it seems appropriate to consider the semantics of not just the language itself but also its classification schemas. One of the beautilful things about objectively breaking down languages by purpose, is that they can be ranked according to their flexibility and utility, their merits, rather than subjective judgements about their sytax. As with most anything in code, bash, or whatever scripting, part of the learning process is absorbing typical commands and the rest is playing with how to appropriately pair them for more complex operations (roughly: what commends are possible and how to link them). Snooping through Stack Overflow can usually get you pretty far on the first one, the second comes later, when repeated compartmentalized operations become exhaustive and your frustrastion has driven you to the point of investment in some serious study or thought on how to most efficiently arrive at your goal.

For my part, I was been working on batch cleaning and processing files to analyze their content for a retrospective media analysis project and this exercise led me to consider several "data processing languages" and their comparable utilities. There's no real pretense or hierarchical system that can supercede a language preference defined by operations that work and suit your data. I've got several years worth of newspaper and journal data to convert from various file formats to one, and then rename in a batch before diving into the actual contents and cleaning and reformatting. Sed seemed appropriate for this, I could probably do it in Python or bash or JS or somesuch and mayber there's someone who's already build an online gui that automates all this...but I was looking for something that worked and something new to learn, a new dialect to surprise myself with. Maybe what's more interesting is the languages and features I uncovered in the research process. If I could build an ideal data processing language, what vague features and ambiguous classification terms might I apply?

So here are some interesting language paradigms that I'd like to adopt or consider after study:

For this project, I selected SED because I'd read about its utility for my purposes. I've got several years worth of newspaper and journal data to convert from various file formats to one, and then rename in a batch before diving into the actual contents and cleaning and reformatting. Sed seemed appropriate for this, I could probably do it in Python or bash or JS or somesuch and mayber there's someone who's already build an online gui that automates all this...but I was looking for something that worked and something new to learn, a new dialect to surprise myself with. While I felt stupidly proud when surprising others with this workflow and earning the 'hacker' merit badge du jour at work, I didn't choose it to be cool, I chose it because if fit my needs. I chose it because sed is simpler than awk an perl, syntactially and performatively, but it provides a variety of text processing and regex support operations, and suits most things I would need in combination with other commands. I'm still at the 'hello world' stage with some of the magic of stream editors, but sed had some pun promise for the title of this post so I thought I'd go with that and see how far I could get with the operations that I wanted to perform. 

And this is where I started thinking, perhaps there are other language paradigms to adapt for this purpose. Taking tips from symbollic and declarative languages might be useful, if only conceptually. I'd like to type in my desired output and allow the language to fumble through the mechanics of its implementation. When in SQL and I'm select from where'ing, I'd like to sed-ify that operation for data cleaning. Select *.csv from _ directory where _[date].csv.

In researching and polling friends about addtional "sql-ish" (pronounces "squish" please) languages, I came across a few interesting features that I have yet to test in practice but seem like pretty cool operations to incorporate in a meta-sed lang.

In the past, and via wikipedia, I've heard  "declarative" applied to XSLT. Your blocks of code are statements, declared like:
When you get to {this} w/ property {that}, do {these things}. 

You can declare them in any order and they will run in the appropriate sequence.  However, is XSLT "declarative" according to all definitions? Diving further down the rabbit hole had me questioning more of what "declarative" means in this context. Despite the overwhelming arguments you can get yourself into when defending the merits of one computer language over another, the terminology used to refer to different programmatic concepts and classification schemas can be vague, misleading and largely unhelpful if you approach them as a foreigner, with other linguistic fluencies influencing your translations. The term "declarative language" for example can referene "non-procedural", but that is also valid for the other language styles. The author in this article linked above uses "where you declare..." to define his term of "declarative language." With XSLT, you write blocks of procedural code, called in reaction to something in the source doc, otherwise unlinked to the calling procedure ("where you declare..."). If you think of lots of front-end and web prog languages, they pretty much fall into this category: small blocks of code linked to a user interaction, operation (onClick listen --> then run {this}). 

The author features a bunch of interesting language paradigms like concatenated languages, but there are other, now (perhaps) obsolute meta-languages that also address these concepts with more flourish and in many cases the same hiccupy classification semantics that can obscure their utility. Like what about languages made to describe algorthims, APL-ish toungues with general and placeholder operators, "compression functions" to apply operators pairwise to members of a vector, right to left programming execution sequencing.

Or what about REX, a shell scripting language using juxtaposition and '|' interchangeably for concatenation, using blanks as operators. Even the semantics of concatenation have been through debates about the appropriateness of the term to "co-chain" vs. just catenate ("chain").

Both conlangs seem to require quite a bit of syntactical adjustment but have features I've never seem echoed in other languages. And still, the point is, no one remembers these syntactial idiosyncracies, languages are remembered for what operations they perform and how well. Are memories are operatoin-orientated. Are these lexicons appropriate for high poetry, are they gutteral and direct?

In light of all this confusion, I'm wondering if I even understand how to appropriately use and manipulate a language when I'm not sure how to best describe it. Taking a page from my spoken fluencies, those languages that I know best and feel most comfortable using in practice are always those whose grammar and constructs I can explain and justify with greatest ease. There's little mastery in the unwritten bluddering I do in Swahili or Creole, though I've spent serious time in places where they were spoken; English and French, the product of formal study and informal fumbles, I totally own like whoa. Likewise, 

There's a declarative programming and an imperative programming; likewise an imperitive mood (expressing commands; http://en.wikipedia.org/wiki/Imperative_mood) in most spoken/written languages. One might read Dothraki (http://en.wikipedia.org/wiki/Dothraki_language) or Klingon, a brutal class of LCS languages and particularly "imperitive" in their 'commanding' manner, unapologetic gutteral articulation. But what might be the meaning of declarative? Do many people know? The internet suggests not. As per uszhe, everyone has his own definition, disambiguations + citation needed, wikipedia, hint hint. 

So what's the best language to communicate what we want, when the writing about languages is indecisive and muddled? Probably, and unsuprisingly, the language you speak best. True masters can adapt languages to their purpose, but most still recognize that CS languages are freighted with an intention, and this limits their applicability to all situations. The ambiguity of classifications like "declarative" in reference to a few languages or other terms applied to and restricting language adoption crumbles when you consider languages for their ideal operations, and not their syntax or semantics. What is the purpose of the language, how to absorb typical commands and how to appropriately pair them for more complex operations? Operation-oriented language selection (python is good for... and ...) rather than grammaticentric (pythong's sytax is bloated and confusing"") might be the best approach for study; one that respects the romantic tropes of surprise, and pushes you to build a vocabulary based on the declared objectives of your goal, rather than the pretense of some predefined language hierarchy.

That, appropriately, is what she sed.

Note: I like to alliterate my titles so if you thought this would be a post about functional programming and are now dissappointed, you should check out my friend Jonathon's post on Functional programming, or this explanation series which is fairly brill IMHO: http://www.braveclojure.com/functional-programming/. 
If you wanted more stream editing and shell scripting, here are some resources you might enjoy: https://developer.apple.com/library/mac/documentation/opensource/conceptual/shellscripting/Introduction/Introduction.html
AWKWARD: https://developer.apple.com/library/mac/documentation/opensource/conceptual/shellscripting/Howawk-ward/Howawk-ward.html#//apple_ref/doc/uid/TP40004268-TP40003518-SW10


http://brikis98.blogspot.dk/2014/04/six-programming-paradigms-that-will.html
Exploring dependent types: This is the idea behind languages that support dependent types: you can specify types that can check the value of your variables at compile time.
Some resources:



------

AWK is a rule based language, setting up rules when primed by a dataset's conditions, and is among a class of scripting languages like sed. 

“APL” (A Programming Language). It had many, many operators and a number of them had placeholders for operators so they were somewhat general. As an example to sum a vector v, you would use "+/v”. The slash was a “compression” function that applied the operator pairwise to the members of the vector. If you wanted a product, you could use “x/v” (with the real mathematical times symbol) or if you had a boolean function, you could compute parity with the operator for exclusive or. It also had a rule that each line was executed from the right to the left, and I don’t remember whether they even allowed parens or not. 

It was originally conceived as a language to describe algorithms, and in fact, during the design of the S/360 mainframes (Fred Brooks was one of the key architects), they wrote an APL program the described the function of the machine. 

Eventually, there were interpreters developed to allow a computer implementation of it, and even a couple of companies that offered “time sharing” services with APL. It had a huge learning curve, but it allowed you to do things that no other language could do.

The other neat language was called “REX”. It was a shell scripting language. It is the only language I had heard of where one or more blanks were an operator. It signaled that the output would contain the thing to the left of the spaces, one space, and the thing to the right. For a language where you needed to build up commands for the shell, it was very powerful. It also had “concatenation by juxtaposition. If you wanted to put an “x” before whatever was in a variable y, you could write “x”y to indicate concatenation. (You could also use “|” as a more general concatenation operator, but the juxtaposition wound up being used a lot.)

(Dr. Fred Brooks took issue with the term “concatenation” since it means “to chain together”. He preferred “catenation” meaning to chain.}



