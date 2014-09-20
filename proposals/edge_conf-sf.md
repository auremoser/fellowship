LAYOUT PERFORMANCE
==================
* rendering is not being extended yet (extensible web manifesto)
* dont want to fork the web
* layout is generally really fast but layout management is not]
* there's no real smoothness api on web (like in apps)
* single threaded programming in the dom but the web has some parallelizing operations
* we have no api to measure text << BIG PROBLEM (text justification and glyph sizing)
* we have poor modes of metrics for layout performance and presenting the layout informaiotn

SECURITY AND IDENTITY
=====================
* post requests over http >> quora
n* sa slides http allows the nsa to do mass surveillance; nsa can collect your trofic
* EFF's Ecrypt the Web Reports
* Wordpress supports ssl
* webcrypto in chromium + firefox
* http public key pinning
* [certificate transparency](http://www.certificate-transparency.org/)
http2 (should encryption be the default)
* one cllick ssl setup?
* [better crypto](https://bettercrypto.org/)
* [SSL Mate](https://sslmate.com/) - does work for you; work being done by the providers (need to be done at a server lievel or a provider lvel)
* use [opportunistic security](http://tools.ietf.org/html/draft-dukhovni-opportunistic-security-00)
* [ssl labs test](https://www.ssllabs.com/ssltest/)
* [is tls fast.com](https://istlsfastyet.com/)
* behavioral trackign, 3rd party validation
* continuous authentication rather than prompting
* mozilla and google are looking at ways to discourage behaviors are bad
* http nowhere (browser refers you to ) web is encrypted by default; is there any reason to ever ask users for security?

PACKAGE MANAGERS
=================
* npm for server side package management but the web doesn't have it
* jvm has maven, node has npm, ruby has gems
* we all understand putting source code into a package
* deduplication and semantic versioning
* npm installing has multiple roles 9dev tool, a build architect - primary use, deploying to a box somwhere package of software)
* npm work in server side client side and component side javascript
npm package manager for client side stuff
* standardize metadata format and handle package json

IMAGE FORMATS
=============
