
##TO DO
* setup crowdataapp/templates for translation
* use ugettext util in django
* add comments for translators
* make messages file django-admin.py makemessages -l de



####: crowdataapp/admin.py:50
####, fuzzy
msgid "Document Set Description"
msgstr "Conjuntos de documentos"



Example:
fieldsets = (
        (_('Document Set Description'), {
            'fields': ('name', 'description', 'header_image', 'tosum_field', 'published')
        }),

####: crowdataapp/admin.py:50
####, fuzzy
msgid "Document Set Description"
msgstr "Conjuntos de documentos"

======================================================================

JSORRERY
========
The result was satisfactory, except for one thing. In my Solar System, I included the orbit of Halley's comet. As you may know, its orbit is in the shape of an elongated ellipse : it is highly eccentric. Eccentricity is the parameter that describes the shape of the orbit, with 0 being circular and augmenting towards 1 for flatter ellipses. One of the effects of having an eccentric orbit is that the calculations of the orbital elements become less accurate. It's not a big problem when you want an approximate position, but velocities cannot be inferred from inacurrate positions. So Halley's comet was'nt giving a damn about its trajectory, getting the hell out away in the universe.

Fortunately, there is a principle of physics that was on my side, and permits the calculation of the speed of an orbiting body from its position only : the vis-viva equation (http://en.wikipedia.org/wiki/Vis-viva_equation). But speed is a scalar, whereas velocity is a vector, so with vis-viva I had the length of the velocity, not its orientation. Further calculations were needed to get the orientation as well, and I ended up with a pretty good system for calculating all the initial parameters to launch the simulation.

Im pretty sure he is just doing an approximation and is calculating the speed as for any other celestial bodies by tweaking the values of the parameters used to define the comet itself

Woudl like to use artificial satellites and apollo js to track free range trajectories:
free range trajectory: http://lab.la-grange.ca/en/showing-an-apollo-mission-free-return-trajectory-in-jsorrery

Algo in algorithms/OrbitalElements.js
scenario/SolarSystem.js
scenario/ArtificialSatellites.js


Ephemeris data from nasa: http://ssd.jpl.nasa.gov/horizons.cgi?find_body=1&body_group=sb&sstr=1P%20[]


Experiments in Planetary Emphemerata
====================================

As a librarian, I've worked with a lot of ephemera in my time, objects and items with impermanence as a probable characteristic worth impeding for posterity. Part of your job as a taxonomist and or developer of cataloging schema is often to finds ways to graph the chaos in a colection of ephemera, and somehow compose it to a unified and navigable cosmic whole. This will be a post about data, astronomic erraticisms and the ephemeral cosmos. Whoohooo, adventures!

In the Preservation Division of my previous library gigs, we cataloged ornate objects, pages from old books, or otherwise hard-to-characterize media as "emphemera;" a favorite collection was the victorian valentines that we had in archival boxes at the Art Institute of Chicago. In the context of space mapping, the intent of the word still holds.

"ephemeris" is a term in astronomy  for "a table or data file giving the calculated positions of a celestial object at regular intervals throughout a period" and for the visulization of orbiting space objects as well as the metadata mapping of mutable materials, it's significant. So for our hackweek we (Brian Jacobs, Ben ? and I ) decided to explore a little topical ephemera. For about two days we processed data from nasa around the orbital trajectory of an "ephemeral" comet that enters earthly view in the month of October 2014, after a 6.5 million year potential trajectory! So dope.

So part of the process was data cleaning and prepping otherwise complicated series of AU numbers (my numbers! as an AUre ;) which Brian took the lead on, and then part of it was exploring existing visualization libraries that might provide a 3D view. 

The planetary metaphor for organizing information is a popular one. You may note it in many organizational schema as it's shopped around about as often as the 'periodic table' when it comes to organizing collections of things. More recently you might have noticed it in the iWatch ads, but there are a few awesome libraries I got to check out with with project, and hopefully will explore more as I boot fluency in 3.js. 

So, to run through the basic info here, our comet is a cutie on a hyperbolic orbital trajectory through space. 3D viz was important for this application, as the comet operates on a tangential orbit to the typical one in our universe (you may remember this being part of the reason why Pluto is in planet exile: its strange orbit vis-à-vis the other planets). So a simple 2D vis won't do, our visualization had to represent the scale of Sidign Spring's orbit, and it's strange and weakly documented plan for rotation around other extra-earthly bodies. We wanted to build something that would truely represent the best comment data from NASA for Sliding Spring's trajectory matched to the best planet data. 

Of these, we settled on JSOrrery to prototype, as it had an existing representation of elliptical planetary orbits (like plutos) and comets (like Halley's) on a separate plane. Quick mathcing of the numbers from NASA had us with an Orerry clone that illustrated the epic orbit of our comet as an ellipse, where the e ("eccentricity") level was less-than 0, as a hyperbolic requires a >0 number. We still need to work a bit on making it render without that elliptical dependency, but hopefully we can explore those kinks in the coming weeks, and get something not-too-emphermal but super-topical up for perusal pre-october. 

[IWATCH AD]
/**

mass : kg
dist : km
apeed : km/s
radius: km

/*
Epoch : J2000
a 	Semi-major axis
   e 	Eccentricity
   i 	Inclination
   o 	Longitude of Ascending Node (Ω)
   w 	Argument of periapsis (ω)
E 	Eccentric Anomaly
   T 	Time at perihelion
   M	Mean anomaly
   l 	Mean Longitude
   lp	longitude of periapsis
   r	distance du centre
   v	true anomaly
   P	Sidereal period (mean value)
Pw	Argument of periapsis precession period (mean value)
Pn	Longitude of the ascending node precession period (mean value)


my data: 1 au=149597870.700 km


====SIDING SPRING DATA====
http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=C%2F2013%20A1;orb=1;cov=0;log=0;cad=0#phys_par

e (for comet): 1.000647997621514
a (AU): -2158.550296435509
q (NASA) = perihelion distance: 1.398735458008349
i : 129.0274045575442
node (NASA, deg) = o (Ω) : 300.9765309370206
peri = argument of perihelion ~w (ω) : -.003620146756019953
M (deg): -.003620146756019953
tp (JED) = T : 129.0274045575442

n (NASA, deg) = mean motion ??

=====HALLEY's COMET =======
 Element	Value	Uncertainty (1-sigma) 	 Units
e	0.967142908462304	5.035e-09
a	17.8341442925537	3.8913e-08	AU
q	0.585978111516909	8.8924e-08	AU
i	162.262690579161	6.7791e-06	deg
node	58.42008097656843	9.0539e-06	deg
peri	111.3324851045177	1.1714e-05	deg
M	38.3842644764388	1.4226e-07	deg
tp	2446467.395317050925
(1986-Feb-05.89531705)	4.7896e-06	JED
period	27509.1290731861
75.32	9.0034e-05
2.465e-07	d
yr
n	.01308656479244564	4.2831e-11	deg/d
Q	35.08231047359043	7.6546e-08	AU



###Links
* [threex.planets repo](https://github.com/jeromeetienne/threex.planets/)
* [demo threes modeling](http://jeromeetienne.github.io/threex.planets/examples/select.html#Mars)
* [Our Comet](http://en.wikipedia.org/wiki/C/2013_A1)
* [Simulating Solar System in JS Wiki](https://github.com/oluckyman/js-planets/blob/master/part1.md)
* [Planning Etherpad](https://etherpad.mozilla.org/HHpHzhb7tC)
* [Nasa Orbital Diagram for Our Comet](http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=C%2F2013%20A1;orb=1;cov=0;log=0;cad=0#phys_par)
* [JSOrrery](https://github.com/auremoser/jsorrery)
* [Planets scenario for jsorrery](https://github.com/mgvez/jsorrery/blob/187479fe4973fb6b33bc3eb9ae8fe725e1be9fe5/js/jsorrery/scenario/CommonCelestialBodies.js)
* [JSOrrery blogpost](http://lab.la-grange.ca/en/building-jsorrery-a-javascript-webgl-solar-system)
* [Apollo Mission Free Trajectory](http://lab.la-grange.ca/en/showing-an-apollo-mission-free-return-trajectory-in-jsorrery)
* [Math for Apollo 11 Translunar Trajectory](http://www.braeunig.us/apollo/apollo11-TLI.htm)
* [Vis-Viva Equation](http://en.wikipedia.org/wiki/Vis-viva_equation)
* [Point Data with JSOrrery](http://lab.la-grange.ca/en/building-jsorrery-a-javascript-webgl-solar-system#show-last-Point)
* [Halley’s Comet NASA Data](http://ssd.jpl.nasa.gov/sbdb.cgi?ID=c00001_0)
* [NASA Horizon’s System](http://ssd.jpl.nasa.gov/sbdb.cgi?ID=c00001_0)
* z

