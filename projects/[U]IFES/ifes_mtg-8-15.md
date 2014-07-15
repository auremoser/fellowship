##IFES MEETING

###stats update:
* we don't have stats api ready at this point
* aurelia has made stub graphs to test the desired functionality of the viz (exportable charts, color coding according to theme, adding multiple series, right<>localization + translation, chart types)
* after the release this week, Woody will make a push on the stats api and we can update them next monday/tuesday instead of waiting until the 24th

###asks
* 8-12 in the IFES task spreadsheet

  
Name | Feature | Queries | Status
------------ | ------------- | ------------ | --------- |
external dataset import |	data import/export; Admin can upload external datasets to visualize in charts such as in: http://www.salonevote.com/	 |   | ?most desirable aspects of this?
cut and paste charts | dataviz	Admin can generate clean and clear charts that can be cut and pasted into Word documents  | | cut and paste works, save as a png and embed
formfield graphs | dataviz	Admin can view graphs of custom formfield values (e.g. IFES indicators)
configurable graphs | dataviz	X/Y of graphs would be adjustable and would show formfield values in Y, and time or county/location on X. Also have the ability to compare counties/locations over time. | Will clarify with customer, but basically is indicator (dropdown formfield values) vs either admin district level (also a dropdown formfield value - e.g. atoll/island) or time. | can do this with [axis_update()](http://jsfiddle.net/gh/get/jquery/1.7.2/highslide-software/highcharts.com/tree/master/samples/highcharts/members/axis-update/) and setup [dynamic updates](http://www.highcharts.com/stock/demo/dynamic-update)
visualize report data | Ability to visualize report data in the same way as indicators | What is 'the same way as indicators'? Indicators = formfield entries. They want the same visualisations for reports as formfields. There appears to be some confusion here. | clarification?
choropleths | Abiltiy to visualize report data on maps | | we can do this in [highmaps](http://www.highcharts.com/)

###basic charts
from [previous notes](https://docs.google.com/a/ushahidi.com/document/d/1oFUhsO084gAbB8VIjfNDDXWoMrBmF3XLa6QyKHRyMC8/edit)

- **time series line graph** Reports/incidents over time
- **time series** reports by type over time (combined with above, possibly separate or filterable)
- **pie chart** report counts by REGION (atoll/island/other denomination) over time
- **bar chart** report counts by region
- **pie chart** GENDER % by perp + by victim
- <grouped/standard bar chart> Political Party by perp + victim
- **grouped bar graph** VIOLENCE types by month
- **grouped bar** IMPACT types: person (violence) or property (vandalism) - counts/time

- choropleths to match?

###demos
* [original demo](http://auremoser.github.io/ifes/)
* [original repo](https://github.com/auremoser/ifes)
* [choropleth repo](http://github.com/auremoser/ifes-map)
* [choropleth demo](http://auremoser.github.io/ifes-map/)
	* added choropleth to prove functionality


###notes
* equal need for choropleths
* indicator charts (variables-perp types/)
* inside application
* pick chart types
* day level zoom (with time) - between 8am-10am - 
* get electoral districts (what format)
* 2 levels of administrative boundaries for choropleths
* array of frequently used charts would be good
* [CHART 2] visualize the data ranges - range 1/2/3
* filter by month > each chart has a date range option
* number of incidents, number of things counted in a form > on 
* choropleth: number of reports, number of incidents, number of "indicators", number risk level
* [T49](https://phabricator.ushahidi.com/T49)-[T50](https://phabricator.ushahidi.com/T50) and [T47](https://phabricator.ushahidi.com/T47)

###references

* [Phabricator Task](https://phabricator.ushahidi.com/T23)
* [DataViz in Phab](https://phabricator.ushahidi.com/T49)
* [Google Doc from previous mtgs](https://docs.google.com/a/ushahidi.com/document/d/1oFUhsO084gAbB8VIjfNDDXWoMrBmF3XLa6QyKHRyMC8/edit)
* [David's inspiration page](http://www.lracrisistracker.com/)
* [Meeting Minutes](https://docs.google.com/a/ushahidi.com/document/d/1cGG9MxDnbbzQqiuXh3Blajx2ily1aGR2-B9cV0rqDEU/edit#)