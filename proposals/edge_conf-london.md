EDGE CONF NOTES
===========
###Schedule - Session notes
10:00
###**COMPONENTS**
We’ve see the future, and it’s looking modular. Corporations with large numbers of sites increasingly build complex reusable components, and we’ve seen frameworks emerge to organise these components on a page (e.g. Facebook’s React or FT’s Fruit Machine). At the same time, web standards are evolving to give us a native solution in the form of web components. How do we get there from here? And for smaller organisations and single developers, will there be a market in components? What standard will drive that?

----------------
####Intro web components rehabstudio.com
Java Applets -> Dynamic DRive > OOCSS (obj oriented css)> BEM >
jquery ui /bootstrop > React Fruitmachine --> WEB COMPONENTS
Let's make an easier wasy to do this
Goal: reusability
* custom elements (everything is an element)
* html imports (using html markup make it reusable)
* shadow dom (dom inside the dom, hidden from user, powering its simplicity)
- template element (hold on reder)
- mutation observers
- scoped styles (apply css selectively)
- decorators dropped

--chrome + opera (based on same blink engine)
--firefox
--microsoft - hipsters of component scene

#####Libs: 
polymer - core + polymer elements (google)
xtags - xtag core + brick (firefox)

-- both have platform polyfill

----
`** = defined things`  

`* = important things`

**isomorphic js** = server render or client render (performance is fasted) BUT you can disable blocking with an atribute
* choosing a balance between server and client side rendering for mobile
* the browser should've solved those same 50 issue that all these libraries tackle (tabs, carousel)

native apps kick ass at performance and widgets behave differently
not the same on browser - mobile

tab atkins - reponsive components (not for viewport)

shadow dom does not profide security boundary

* Node forces you to by async

Aria (stopgap solution working toward standarad)
* HTML imports can do de-duping so multiple components don't pull in different versions of da


###**DEVELOPER TOOLING**    

First there was Firebug, now Chrome DevTools, but recently IE’s developer tools have taken a quantum leap forward in version 11, and Mozilla has some unique new features to their built in tools. Tools outside of the browser now integrate far more intelligently, and it’s even possible to use one browser’s devtools to inspect a different browser. Are we still looking for the best tool workflow, or is there room for all these different tools?  

----------------
History of dev tooling
html parsing tool - hixie
live dom viewer <http://software.hixie.ch/utilities/js/live-dom-viewer/>
venkman in firefox (js debugger 2001)
#####Basic tools
FIREFOX
- webglshader editor - realtime feedback on validation errors
- memory tooling in firefox dev tools
- scopes in action can be seen in a hierarchy
- audio breakpoints - hearing hwen different points in your code are hit
? splitting web console in two : js has its own portion?

CHROME
- screencasting (mirroring activity on phone in browser emulator)
- flame chart visualization of js profiler (histagram)
- async call stacks

IEF12 Dev Tools
- waterfall
- memory heap snapshotting and profiling
- ui responsiveness panel

#####Other tools
BRACKETS <http://brackets.io/>
NOFLO <http://noflojs.org/>
- flow based visual peradigm for writing js applications
SPYJS: <http://spy-js.com/> 
React Dev Tools extension <https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi?hl=en>
Ember extension: <https://chrome.google.com/webstore/detail/ember-inspector/bmdblncegkenkacieihfhpjfppoconhi?hl=en>

* way forward to do it from a js api
* listing unfulfilled prmises in tags in dev tools
* why consol.log instead of debugger
** omniscent debugging ** = https://en.wikipedia.org/wiki/Debugger
* phantom js from the browser? to do testing /regression/performance
slimer js (not headless, nearly headless)




12:00
BREAK
Grab a coffee and recharge for the next session.

12:15
###**BUILD PROCESS**
Everyone has a compile step these days, whether it’s CSS preprocessing, bundling, minification, linting, testing, or optimisation, we all want to make our lives easier by automating build and deploy. But to some, the more complex the build gets, the more we get away from the fundamental motivations for many of the web technologies we love to use. Should we fix this in tooling, or by just making build processes even more sophisticated, or with browser developments like HTTP 2.0 which negate the need for some or all of the build step?

----------------
your a softwar developer: css preprocessing, templating, bundling, minification, linkting
- gulp
- grunt
Make is 37

* can we share entire pipelines as well as tools we use to build them
Node popularity a problem for build process dependencies --> need to make solutions for averable people (guis)
npm = protocol (way to get own repository)
* use git not github; use npm protocol not the company
Node task spec?

Extensible web manifesto: <http://extensiblewebmanifesto.org/>
Fez <http://fez.github.io/>
**Unix Philosophy** = pipes from text, thought he ease of small tools chained together to build together for a common philosophy --powershell
Yeoman - opinionated workflows


13:15
LUNCH
14:15
**PAGE LOAD PERFORMANCE**
This is a perennial topic but one that is changing rapidly as browsers constantly tweak their behaviour and major advances like HTTP 2 threaten to completely disrupt the received wisdom. Today’s best practices may be tomorrow’s anti patterns. Tools such as WebPageTest and the NavigationTiming API give us more data than we’ve ever had before; how can developers best harness this new wealth of information?

----------------
page load test (best testing)

Make sites fast:
- minimize latency
- minimize round trips
-- divide page load into content, enhancements, leftovers (adverts, analytics)
- minimize blocking

* http not really good on tcp (**http 2** coming)
* sitespeed.io <http://www.sitespeed.io/>
* web page performance test <http://www.webpagetest.org/>

* "performance is a facet of user experience"

- concatenation + spriting == Antipatterns? in http2
- page onload event 
* SPDY <http://www.chromium.org/spdy/spdy-whitepaper>
- wbp jpeg



15:15
**POINTERS AND INTERACTIONS**
Web UIs are getting better at detecting and optimising for touch, but it continues to be a struggle, with much lower level primitives to work with than in the native world. Should we be aiming to abstract all spacial interaction into a ‘pointer’? How can more complex spacial interactions like gestures and 3D motion be handled without extraordinary amounts of effort?

----------------
Challenges
Performance > Richness > Rationality

Improvements
threaded scrolling fast paths
* iscroll = <http://cubiq.org/iscroll-4>
Touch-action  manipulation without delay

"TouchEvents" community group
"PointerEvents" working group

Hammer library for gestures <http://eightmedia.github.io/hammer.js/>
IndieUI= intent rather than actual gesture <http://www.w3.org/TR/indie-ui-events/>

*Click events (just fire or generating these for something that always are accessible), rather than touchevents or specialized events for device-specific event handlers -> focus, blur, click

Leap Motion, MyO? How to do gestures in 3D space

* Pointer events extend mouse events




16:30
**ACCESSIBILITY**
The web is changing fast. Are accessibility standards keeping pace? What should developers of single page apps do to help users of assistive technologies? How do we anticipate assistive technologies developing in future? To what extent do new web technologies such as canvas and the web audio API either help or hinder those with accessibility needs? How much can we afford to invest in accessibility?

--------------
Other idea of accessibility: speech (cerebral palsy, stutters)
vestibular issues.

Color oracle tool <>
Aria = accessible rich internet applications
give divs "roles" like "button
do you work with speech pathologists"

17:30
**FUTURE WEB**
“Responsive” currently seems to mostly mean that your website adapts to a changing viewport width. But there are so many other factors to which web interfaces can respond - time of day, geolocation, battery level, connection speed, viewport height, distance from user to screen, existence and type of pointing device, existence and type of text entry device, pixel density and colour depth of the screen. The list is virtually endless. There’s a compromise to be made, between ease of measurement, cost and impact of being responsive. What are the right factors to invest in for the next few years?

--------------
Jeni Tennison

Let's ask Timbl (AMA)
- More Sensitivity (personal info)
- More data (available) - what does a native data borwser looks like?
- More devices

DEVICES
diffs in ...
size, resolution, connectivity, processing power, modes of interaction, contexts of use

PRIVACY
Unhosted web apps <https://unhosted.org/>
redecentralize.org <http://redecentralize.org/>

* WEB = use of http and resources defined by urls (semantic web def)

18:30
CLOSING REMARKS AND THANKS
Linda Sandvik, co-founder of CodeClub, explains what CodeClub is doing and how your money is being put to good use.


###QUESTIONS

####BUILD PROCESS

Gulp and Fez imperitive style you doefine what you want and it figures it out


####ACCESSIBILITY

What are the best tools for testing web accessibility?

Is there a hierarchy of accessibility standards, a baseline that covers basic web accessibility issues and degrades to higher level concerns orned in browser?
Who is doing cross platform accessibility well? And why? And how?


####DEV TOOLS

How do cloud ide's (koding etcet) feature in this discussion. If you're developing on a chrome book to what extent is the IDE/Dev Tool disjoint minified?

Is is more important that the IDE and debugging of dev tools are closely coupled? or that the IDE and versioning system (like github + atom) are closely connected? How do modern dev tools hope to negotiate all three?

What's the deal with workspaces and can they be integrated into everything: https://developers.google.com/chrome-developer-tools/docs/settings#workspace


####FUTURE WEB

Where do you see the web going as languages get more intelligent? Like, what about Wolfram Language and Computable document format (like a pdf)?