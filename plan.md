## Workit

_created by:_ Arlo Gittings  
_created on:_ 2021-07-11  

### Description:

A simple daily task manager. The key is to make it useful and powerful while
minimizing required effort in the flow of daily events. It may take a bit to
set up initially and will provide tracking data for evaluation on a regular
basis. The first version will be all text driven. As I get deeper into testing,
I will look at the possibility of adding graphs. 

### Project layout

- database driven (mongo)
- key features
	- auto-populate regular tasks
	- track completion rate
	- track time spent
		- allow user to set timers (start/stop) 
			- only one timer at a time
			- when you start a task, all others stop
			- this provides granular tracking
			- might become more involved, but to start, start/stop
			- each task may have multiple intervals when it is active
		- inline new tasks
			- start new
			- allow tracking of ad-hoc activities
			- help ID timesucks and distractors
	- editable in post
		- might forget to put in an activity.
		- handle overlap intelligently.

### Sucess Identifiers

- Phase One 
	- create a task class
	- layout the db model documents
	- create command structure
- Phase Two
	- display existing tasks
	- allow user to input tasks
- Phase Three
	- Allow the user to interact with tasks
	- Track completion rate and time spent
	- Schedule repetitive tasks
	- Review past days
