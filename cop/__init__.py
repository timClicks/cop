""" 

==>  COP
     coroutines for dataflow pipelines


==>  ABOUT
     Cop is designed to make it easy
     to write readable dataflow programs.
     Speed is important, but probably
     isn't there yet.

     This library is a learning exercise.
     At this stage, it should really be
     seen as a source for you to see
     how to implement your own coroutines.

     The primary motivation for cop is
     to facilitate readable and flexible
     dataflow programming. Once the 
     project is more mature, its focus
     could shift to enhancing performance.


==>  TERMINOLOGY
     There are three basic terms that are
     used within cop: sources, steps and
     sinks.

        /sources/   Feed data to steps.
                    (cop.file, cop.web)

        /steps/     Process data, then
                    feed it to a target.

        /sinks/     Process data.


==>  USAGE
     Using cop is straight forward. Examples
     generally follow the following pattern:

       >> from cop.sources import source
       >> from cop.steps import step1, step2
       >> from cop.sinks import sink
 
       >> source(step1(step2(sink()))))

     /examples/

       >> from cop.sources import web
       >> from cop.steps import delimit 
       >> from cop.stops import grep
       >> from cop.steps import transform
       >> from cop.sinks import printer

       >> url = 'http://python.org'
       >> web(url, 
       ...   delimit("\n",
       ...   transform(lambda l: l.lower(), 
       ...   grep('monty', 
       ...   printer()))))
       <BLANKLINE>
       
     In this case, nothing comes out. That's
     basically because there's very little
     about Monty Python at python.org.


==>  BACK STORY
     The start of this whole thing is from 
     code written by David Beazley, especially
     his tutorial on coroutines[0]. That
     work is excellent and should basically
     be considered the manual for this library. 

     I read the PDF of the tutorial in the
     morning. By the end of the evening I had
     a few dozen workable functions that could
     be strung together in an almost arbitary
     function.


==>  HACKING
     If you would like to contribute to cop, 
     that's great. It's easy to do and will
     help people.

     At the moment, the plan is to use heavy
     use of doctests. Use `cop.printer` to 
     get the result:

        >> source(sink(printer())) 
        result

     [sidenote]
     I use >> as prompt when I don't want 
     doctest to claim it. I find this 
     preferable to using the skip directive.


==>  LEGAL
     /code/
     Apart from code written by David Beazley,
     which is used with with permission, the
     code the copyright of Tim McNamara[1].
     
     The code is released under the Apache 2
     license[2].

     /docs/
     All documentation is the copyright of 
     Tim McNamara. All docs are released under
     the "Creative Commons Attribution 3.0
     New Zealand (CC BY 3.0)" licence[3], in
     addition to the Apache 2 licence where it
     applies. 
     
     /trade marks/
     "cop" is an unregistered trade mark of
     Tim McNamara under New Zealand law.
     
     /Consumer Guarantees Act 1993/ 
     If you use this software for personal use,
     you have certain rights under the Consumer
     Guarantees Act 1993. They are explained by
     the Ministry of Consumer Affairs[4].
     
     Generally speaking, cop must be of 
     "acceptable" quality and be fit for the 
     purposes described.
     
     However, when judging acceptable quality, 
     please consider that you are downloading
     free software from the Internet. 
     
     [sidenote]
     I'm not entirely certain whether
     software code counts as a good or a 
     service for the purpose of the Act
     
     [sidenote]
     No, we can't opt out of these provisions.
     Irrespective of the terms of the licence. 
     

==>  REFERENCES

     [0] http://dabeaz.com/coroutines
     [1] @timClicks
         <code@timmcnamara.co.nz>
     [2] http://www.apache.org/licenses/LICENSE-2.0
     [3] http://creativecommons.org/licenses/by/3.0/nz/
     [4] http://www.consumer.org.nz/reports/consumer-guarantees-act/the-guarantees
"""

__version__ = "0.2"
__author__ = "Tim McNamara"

def coroutine(func):
    def start(*args,**kwargs):
        cr = func(*args,**kwargs)
        cr.next()
        return cr
    return start
