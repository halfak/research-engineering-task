# Research engineering task

This project contains code and instructions for completing the Wikimedia
Foundation's task for the Research Software Engineer position (see
[the job description](https://boards.greenhouse.io/wikimedia/jobs/96659)).

To complete the task, read the following problem description and implement a
solution.  Please submit your solution (the code and a one-page description
how you approached this problem and why) to ahalfaker@wikimedia.org.

## The problem

The research team at the Wikimedia Foundation builds computationally intensive
applications that need to work in production environments at the scale of
Wikipedia.  One of these algorithms processes edits to pages in realtime.  
Edits are saved roughly 1.2 times per second, but the algorithm can take
anywhere between 0.1 and 10 seconds to process an edit.  As you might expect,
processing these edit events in sequence is not an option since the computation
takes too long.  Yet, the researchers need the result of this computation to be
output in-order.

## The task

Your task is to develop an architectural strategy that allows this computation
to happen as close to realtime as possible while **preserving the order of
events**. In a real-world environment, edit events would be produced from our
[RCStream](https://wikitech.wikimedia.org/wiki/RCStream) service.  For this
task, we provide a 5 minute recording of events in `sampled_rc.json`.  We also
provide a functions (defined in python, java, javascript and C++) that
implement a 1-10 seconds processing time. (**TODO:** *WHERE ARE THEY??*)

If your solution works as we intend, you should be able to process the 5
minute recording in less than 5 minutes and the output file will match the
order of the input file.

## Questions

Please direct your questions to ahalfaker@wikimedia.org.
