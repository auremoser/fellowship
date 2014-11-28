##Upcycling Interactives
there's a part in Bret Ellis's talk about Inventing on Principle, where he sites a primary need of creative coders, that they see the effects of their code in the immediate: http://vimeo.com/36579366
about 4:42 he illustrates what happens when you change a parameter and the drawn result is so out of scope with what you project. Maybe that isn't useful to you now, but in the science of strange matter and code, it's actually pretty freaking fascinating what you can discover by play.

Original proposal for reference:
========================
 https://github.com/auremoser/fellowship/blob/master/proposals/mozfest_2014-london.md

Title:
====
Upcycling Interactives: A Recyclic Approach to the Half-Lives of Interactives 

(or something equally science/program-y)


Not too long ago a movie called "Interstellar" came it out and a bunch of people didn't like it. Some folks got pretty sassy about the film's approach to tough astrophysics questions toggling relativity and quantum theory. This month, [Wired](http://www.wired.com/2014/10/astrophysics-interstellar-black-hole/) wrote a piece on "The Physics of Interstellar"" with Christopher Nolan (Director) and Kip Thorne commenting on now they handled some of the science in the film; [Discovery](http://news.discovery.com/space/how-the-lhc-makes-interstellar-physics-real-141124.htm) recently published a legit science approach with comments from physicists working at the LHC and conducting experiments to test the open conjectures in Interstellar. Much of the praise for the film came from those who appreciated the suggestion of such science to broader audience, and in many ways, that's not unlike the work of most journalists these days...weaving complex concepts, code and components together in some more approachable cosmic soup, "[y]ou always have to cheat in cinematic narrative, but you try to do it as little as possible and in a way that doesn't violate the pact with the audience. "This got me thinking about building new approaches to infor, discovery also 
Abstract:
=======
In my pleasant post-MozFest chill lull, I've had some time to think about the slurry of sessions I proposed and how they all fit to gether in some cosmic plan of science and data journalism. And I think the intersection is in experimentation and spooky matter. Originally, I pitched a session on Upcycling Interactives (recycling old code for new projects!) and Timezones with Julian Burgess. What happened was a session on Data Smells with Jake Harris, a session on Coding Education for Libraries with Dave Riordan and Jenni Rose Halperin, a session on Pirate Box with Marcos Vanetta and another on OpSec for Journalists with Mike Tigas and Harlo Holmes. While the schedule was full, I think back with a twinge of regret that I didn't get to tackle my proposed topics (related, scientifically I suppose, to time[zone] dilation and relativity). What happened was fine, of course, a series of collaborative presentations made better because I wasn't my own insular atomic unit, but rather a compound with other intelligent folk building solutions and thoughts in ensemble. Still, the idea of recycling code for interactive journalism stories is still one that appeals to the sustainable hippie in me, so it's the one I'll defrag now.

I've noted in my own code adventures that sometimes fumbling through new libraries, languages or POCs, you arrive at some funny and anomalous realizations about your language or objective. Not all of these are peculiarities of the dataset or subject matter of your work, but some of them reveal interesting easter eggs in the type of code you're writing. I wanted to assemble a loosely structured repository of references to these kind of glitchy discoveries in code; maybe something to partner with Jacob Harris' Data Smells repo and recently published Source guide on the topic. In any case, 

Outline:
======
I. A Brief History of Interaction
Introduction to the intrigue in the form of a discussion of interactives à la a brief history of time:  code anomalies as related to quantum anomalies in the peculiarity of the physics they implicate, and the potential those anomalous discoveries have to further the conversation around universal learning and programming paradigms. In many ways, the internet is our tech universe as news apps developers; we work to combat the strange physics and spooky matter of the web such that we can bring more information to our global audience. I usually like to start out with some broader theme, and for this one, a particle/pixel physics comparison suits.

II. Petri-Dish Particle Physics: an Atomic Anecdote
I thought of this idea while working on the HIV@30 project (Zoomable Viz, Static Petri dish Viz) and experimenting the the D3 Zoom pack structure for displaying hierarchical vocab data. The original Bostockian code base was suited for a unilateral tree structure, but when I decided to split the dataset into small multiples for my own narrative purposes, I broke the zoom functionality epically and needed to retool to get it to work. 
Images intégrées 4
Clicking on one small multiple resulted in strange inside-out zooms:
Images intégrées 3
Clicking on multiple bubbles resulted in the occasionally explosive vomit below:
Images intégrées 2

In the process, I made some pretty hilarious and at the time, inexplicably explosive f'ups with the visualization. My first thought was that I needed to power through and fix the issue for the purpose of pushing a production-ready and legible version of the code. Secondarily, I thought, I might want to document the fix to that I could later reproduce the explosion when, say, I made a friend's birthday card, or built an art project/interactive dependent on an illustration of chaos from clicks. Most code stores could operate as choose-your-own adventure archives of the many worlds possibilities in any given approach to interactive news. It seems wasteful to sacrifice that potential 

III. Why Universal Upcycling?
Open Source is riddled with new projects, new libraries and approaches to similar visualization problems, but we seldom take the time to re-appreciate the utility of peripheral branches, failed tests, and other diver In the spirit of flâneur-ish coding practice, blending the recycling and the open source coding communities at least on the basis of 

IV. Upcycle-worthy Interactives
Go through some examples of quirks and anomalous code discoveries in various interactive projects, like my anecdote above or the general "spooky matter" behaviors of interacting languages and libraries on the internet. Like this Highcharts/Bootstrap glitch that I discovered, and never managed to correct when building a visualization of sensor data in Tanzania; or this weird IE-8 flattened world theory discovered while attempting to build a 2D representation of the universe for a comet-tracking project with the other Open News fellows, or even this network visualization that I built to display OSM tags and inexplicably changes color when I try to show/hide the nodes on click (not sure how that happened).
Images intégrées 1


I'm sure every newsroom's past projects are riddled with other quantanomolies and "spooky matter" in the pixel/particle-pushing interactive space. I'd like to highlight and crowdsource those. What can be done to correct these issues or reuse the broken code to productive ends. Many of the worlds most interesting discoveries were accidents; what are some choice examples of how this same principle applies in web code.

V. Contributions Welcome!
Reproducibility and peer review are part of the Scientific Method, and are no-less relevant to our own study of programmer problems and stack overflow submissions as devs. Progress for individuals often depends on that kind of collaboration and feedback framework. Please fill out the form below if you have an example of your own interactives worth upcycling (can be a google form that ports to a spreadsheet that I can then post/submodule or reference in a github repo.
Form Fields:
Name of Project:
Brief Description:
Link to github:
Link to resulting interactive (if available):
Spooky Matter: [describe the conditions of the quirk, and how you moved on]


=>=Context =<=
I planned to host a collaborative session to collect any strange and awesome discoveries made during the interactive coding process that are maybe passed up or removed during the path to a final interactive/visualization/news app. You can read more about the concept here in my MozFest pitch doc. 

I wanted to collect them with comments and links in a git repo and offer them up to other people for reuse or just general learning. 
I'm thinking along the lines of Brett Victor's lecture (around 4:44), when he talks about how changing a parameter can lead to surprising or inexplicable things in code.
Or, in Robert Hodgin's Eyeo Talk (around 27:28), where he admits that he doesn't know how he did something and is afraid to touch the code now, but wants to preserve it just the same.
There are so many great MozFest talks, that they asked me to write mine as a blogpost instead of a session, so that's why I need your help, crowdsourcing more examples of this kind of coding phenomenon so that others can profit from the strange and interesting things you've learned from your projects (hence the upcycling) I've made a little form for this, and I would love if you could submit one of your own projects or suggest another one so I could pre-seed the repository with examples from some of the smartest coders I know.


Original proposal for reference:
========================
 https://github.com/auremoser/fellowship/blob/master/proposals/mozfest_2014-london.md

Title:
====
Upcycling Interactives: A Recyclic Approach to the Half-Lives of Interactives 

(or something equally science/program-y)

Abstract:
=======
I've noted in my own code adventures that sometimes fumbling through new libraries, languages or POCs, you arrive at some funny and anomalous realizations about your language or objective. Not all of these are peculiarities of the dataset or subject matter of your work, but some of them reveal interesting easter eggs in the type of code you're writing. I wanted to assemble a loosely structured repository of references to these kind of glitchy discoveries in code.

Outline:
======
I. A Brief History of Interaction
Introduction to the intrigue in the form of a discussion of interactives à la a brief history of time:  code anomalies as related to quantum anomalies in the peculiarity of the physics they implicate, and the potential those anomalous discoveries have to further the conversation around universal learning and programming paradigms. In many ways, the internet is our tech universe as news apps developers; we work to combat the strange physics and spooky matter of the web such that we can bring more information to our global audience. I usually like to start out with some broader theme, and for this one, a particle/pixel physics comparison suits.

II. Petri-Dish Particle Physics: an Atomic Anecdote
I thought of this idea while working on the HIV@30 project (Zoomable Viz, Static Petri dish Viz) and experimenting the the D3 Zoom pack structure for displaying hierarchical vocab data. The original Bostockian code base was suited for a unilateral tree structure, but when I decided to split the dataset into small multiples for my own narrative purposes, I broke the zoom functionality epically and needed to retool to get it to work. 
Images intégrées 4
Clicking on one small multiple resulted in strange inside-out zooms:
Images intégrées 3
Clicking on multiple bubbles resulted in the occasionally explosive vomit below:
Images intégrées 2

In the process, I made some pretty hilarious and at the time, inexplicably explosive f'ups with the visualization. My first thought was that I needed to power through and fix the issue for the purpose of pushing a production-ready and legible version of the code. Secondarily, I thought, I might want to document the fix to that I could later reproduce the explosion when, say, I made a friend's birthday card, or built an art project/interactive dependent on an illustration of chaos from clicks. Most code stores could operate as choose-your-own adventure archives of the many worlds possibilities in any given approach to interactive news. It seems wasteful to sacrifice that potential 

III. Why Universal Upcycling?
Open Source is riddled with new projects, new libraries and approaches to similar visualization problems, but we seldom take the time to re-appreciate the utility of peripheral branches, failed tests, and other diver In the spirit of flâneur-ish coding practice, blending the recycling and the open source coding communities at least on the basis of 

IV. Upcycle-worthy Interactives
Go through some examples of quirks and anomalous code discoveries in various interactive projects, like my anecdote above or the general "spooky matter" behaviors of interacting languages and libraries on the internet. Like this Highcharts/Bootstrap glitch that I discovered, and never managed to correct when building a visualization of sensor data in Tanzania; or this weird IE-8 flattened world theory discovered while attempting to build a 2D representation of the universe for a comet-tracking project with the other Open News fellows, or even this network visualization that I built to display OSM tags and inexplicably changes color when I try to show/hide the nodes on click (not sure how that happened).
Images intégrées 1

I'm sure every newsroom's past projects are riddled with other quantanomolies and "spooky matter" in the pixel/particle-pushing interactive space. I'd like to highlight and crowdsource those. What can be done to correct these issues or reuse the broken code to productive ends. Many of the worlds most interesting discoveries were accidents; what are some choice examples of how this same principle applies in web code.

V. Contributions Welcome!
Reproducibility and peer review are part of the Scientific Method, and are no-less relevant to our own study of programmer problems and stack overflow submissions as devs. Progress for individuals often depends on that kind of collaboration and feedback framework. Please fill out the form below if you have an example of your own interactives worth upcycling (can be a google form that ports to a spreadsheet that I can then post/submodule or reference in a github repo.
Form Fields:
Name of Project:
Brief Description:
Link to github:
Link to resulting interactive (if available):
Spooky Matter: [describe the conditions of the quirk, and how you moved on]

