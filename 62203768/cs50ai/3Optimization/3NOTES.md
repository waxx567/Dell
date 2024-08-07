# CS50AI 2024 Lecture 3 Optimization notes
`https://learning.edx.org/course/course-v1:HarvardX+CS50AI+1T2020/block-v1:HarvardX+CS50AI+1T2020+type@sequential+block@f8f74d9a8adb41718b022a7769fcca46/block-v1:HarvardX+CS50AI+1T2020+type@vertical+block@6ee0d651416642f599f473a04af13200`

Optimization is choosing the best option from a set of options

## Local search

search algorithms that maintain a single node and searches by moving to a neighbouring node

And the first of the algorithms that we'll take a look at
is known as a "local search."
And local search differs from search algorithms we've seen before
in the sense that the search algorithms we've looked at so far,
which are things like breadth-first search or A* search, for example,
generally maintain a whole bunch of different paths that
we're simultaneously exploring, and we're looking at a bunch of different
paths at once trying to find our way to the solution.
On the other hand, in local search, this is
going to be a search algorithm that's really
just going to maintain a single node and looking at a single state,
and we'll generally run this algorithm by maintaining that single node
and then moving ourselves to one of the neighboring
nodes throughout this search process.
And this is generally useful in contexts not like these problems,
which we've seen before, like a maze-solving situation where we're
trying to find our way from the initial state to the goal
by following some path.
But local search is most applicable when we really don't care about the path
at all, and all we care about is what the solution is.
And in the case of a solving a maze, the solution was always obvious.
You could point to the solution.
You know exactly what the goal is.
And the real question is, what is the path to get there?
But local search is going to come up in cases
where figuring out exactly what the solution is,
exactly what the goal looks like is actually the heart of the challenge.
And to give an example of one of these kinds of problems,
we'll consider a scenario where we have two types of buildings, for example,
and we have houses and hospitals.
And our goal might be, in a world that's formatted as this grid where
we have a whole bunch of houses, a house here, a house here,
two houses over there, maybe we want to try and find
a way to place two hospitals on this map, so maybe a hospital here
and a hospital there.
And the problem now is we want to place two hospitals on the map,
but we want to do so with some sort of objective.
And our objective in this case is to try and minimize
the distance of any of the houses from a hospital.
So you might imagine, all right, what's the distance from each
of the houses to their nearest hospital?
There are a number of ways we could calculate that distance,
but one way is using a heuristic we've looked at before,
which is the `Manhattan distance` (3:30), this idea of how many rows and columns would
you have to move inside of this grid layout in order to get to a hospital,
for example.
And it turns out if you take each of these four houses
and figure out, all right, how close are they to their nearest hospital,
you get something like this where this house is three away from a hospital.
This house is six away, and these two houses are each four away.
And if you add all those numbers up together, you get a total cost of 17,
for example.
So for this particular configuration of hospitals, a hospital here
and a hospital there, that state, we might say, has a cost of 17.
And the goal of this problem now that we would
like to apply a search algorithm to figure out
is, can you solve this problem to find a way to minimize that cost,
minimize the total amount if you sum up all of the distances from all
the houses to the nearest hospital?
How can we minimize that final value?
And if we think about this problem a little bit more
abstractly, and abstracting away from this specific problem,
and thinking more generally about problems like it,
you can often formulate these problems by thinking about them
as a `state-space landscape` (4:21), as we'll soon call it.
Here in this diagram of a state-space landscape, each of these vertical bars
represents a particular state that our world could be in.
So for example, each of these vertical bars
represents a particular configuration of two hospitals.
And the height of this vertical bar is generally
going to represent some function of that state, some value of that state.
So maybe, in this case, the height of the vertical bar
represents what is the cost of this particular configuration of hospitals
in terms of, what is the sum total of all
of the distances from all of the houses to their nearest hospital?
And generally speaking, when we have a state-space landscape,
we want to do one of two things.
We might be trying to maximize the value of this function,
trying to find a `global maximum` (5:10), so to speak, of this state-space landscape,
a single state whose value is higher than all of the other states
that we could possibly choose from.
And generally, in this case, when we're trying to find a global maximum,
we'll call the function that we're trying
to optimize them some `objective function` (5:23),
some function that measures for any given state
how good is that state such that we can take any state,
pass it into the objective function, and get a value for how good that state is.
And ultimately, what our goal is is to find
one of these states that has the highest-possible value
for that objective function.
An equivalent but reverse problem is the problem
of finding a `global minimum` (5:49), some state that has a value after you passed it
into this function that is lower than all of the other possible values
that we might choose from.
And generally speaking, when we're trying to find a global minimum,
we call the function that we're calculating a `cost function` (5:55).
Generally, each state has some sort of cost,
whether that cost is a monetary cost, or a time cost,
or, in the case of the houses and hospitals
we've been looking at just now, a distance
cost in terms of how far away each of the houses is from a hospital.
And we're trying to minimize the cost, find the state that has
the lowest possible value of that cost.
So these are the general types of ideas that we
might be trying to go for within a state-space landscape,
trying to find a global maximum or trying to find a global minimum.
And how exactly do we do that?
We'll recall that in local search, we generally
operate this algorithm by maintaining just a single state,
just some `current state` (6:34) represented inside of some node,
maybe inside of a data structure where we're keeping
track of where we are currently.
And then, ultimately, what we're going to do
is, from that state, move to one of its `neighbor` (6:52) states,
so in this case represented in this one-dimensional space
by just the state immediately to the left or to the right of it.
But for any different problem, you might define
what it means for there to be a neighbor of a particular state.
In the case of a hospitals, for example, that we were just looking at,
a neighbor might be moving one hospital one space to the left, or to the right,
or up, or down, some state that is close to our current state
but slightly different and, as a result, might
have a slightly different value in terms of its objective function
or in terms of its cost function.
So this is going to be our general strategy in local search,
to be able to take a state, maintaining some current node,
and move where we're looking at in this state-space landscape in order
to try to find a global maximum or a global minimum somehow.
And perhaps the simplest of algorithms that we
could use to implement this idea of local search
is an algorithm known as `hill climbing`.

### Hill climbing

And the basic idea of hill climbing is, let's say,
I'm trying to maximize the value of my state.
I'm trying to figure out where the global maximum is.
I'm going to start in the state.
And generally, what hill climbing is going to do
is it's going to consider the neighbors of that state, that from this state
I could go left, or I could go right.
And this neighbor happens to be higher, and this neighbor happens to be lower.
And in hill climbing, if I'm trying to maximize the value,
I'll generally pick the highest one I can.
Between the state to the left and right of me, this one is higher.
So I'll go ahead and move myself to consider that state instead.
And then I'll repeat this process, continually
looking at all of my neighbors and picking the highest neighbor,
doing the same thing, looking at my neighbors,
picking the highest of my neighbors until I get to a point like right here (8:14)
where I consider both of my neighbors, and both of my neighbors
have a lower value than I do.
This current state has a value that is higher than any of its neighbors.
And at that point, the algorithm terminates.
And I can say, all right, here I have now found the solution (8:28).
And the same thing works in exactly the opposite way
for trying to find a global minimum, but the algorithm
is fundamentally the same.
If I'm trying to find a global minimum and, say, my current state starts here (8:38),
I'll continually look at my neighbors, pick the lowest value
that I possibly can until I eventually, hopefully,
find that global minimum, a point at which (8:46), when
I look at both of my neighbors, they each have a higher value,
and I'm trying to minimize the total score, or cost,
or value that I get as a result of calculating some sort of cost function.
So we can formulate this graphical idea in terms of pseudocode.
And the pseudocode for hill climbing might look like this (9:03).
We define some function called "hill climb" that takes as input
the problem that we're trying to solve.
And generally, we're going to start in some sort of initial state (9:12).
So I'll start with a variable called "current"
that is keeping track of my initial state,
like an initial configuration of hospitals.
And maybe some problems lend themselves to an initial state,
some place where you begin.
In other cases, maybe not, in which case we might just randomly generate
some initial state just by choosing two locations for hospitals at random,
for example, and figuring out from there how we might be able to improve.
But that initial state, we're going to store inside of "current."
And now here comes our loop, some repetitive process
we're going to do again and again until the algorithm terminates.
And what we're going to do is first say, let's figure out all
of the neighbors of the current state.
From my state, what are all of the neighboring states for some definition
of what it means to be a neighbor?
And I'll go ahead and choose the highest valued of all of those neighbors
and save it inside of this variable called "neighbor," so keep
track of the highest-valued neighbor.
This is in the case where I'm trying to maximize the value.
In a case where I'm trying to minimize the value,
you might imagine here you'll pick the neighbor with the lowest
possible value.
But these ideas are really fundamentally interchangeable.
And it's possible, in some cases, there might be multiple neighbors
that each have an equally high value or an equally low value
in the minimizing case.
And in that case, we can just choose randomly from among them.
Just choose one of them, and save it inside of this variable "neighbor."
And then the key question to ask is, is this neighbor
better than my current state?
And if the neighbor, the best neighbor that I was able to find
is not better than my current state, well, then the algorithm is over,
and I'll just go ahead and return the current state.
If none of my neighbors are better, then I may as well stay where I am
is the general logic of the hill-climbing algorithm.
But otherwise, if the neighbor is better,
then I may as well move to that neighbor.
So you might imagine setting "current" equal to "neighbor"
where the general idea is if I'm at a current state
and I see a neighbor that is better than me, then I'll go ahead and move there.
And then I'll repeat the process, continually moving to a better neighbor
until I reach a point at which none of my neighbors are better than I am.
And at that point, we'd say the algorithm can just terminate there.
So let's take a look at a real example of this
with these houses and hospitals.
So we've seen now that if we put the hospitals in these two locations,
that has a total cost of 17.
And now we need to define, if we're going
to implement this hill-climbing algorithm,
what it means to take this particular configuration of hospitals,
this particular state and get a neighbor of that state.
And a simple definition of "neighbor" might be just let's
pick one of the hospitals and move it by one square to the left, or right,
or up, or down, for example.
And that would mean we have six possible neighbors
from this particular configuration.
And we could take this hospital and move it
to any of these three possible squares, or we take this hospital
and move it to any of those three possible squares (11:50).
And each of those would generate a neighbor.
And what I might do is say, all right, here
is the locations and the distances between each
of the houses and their nearest hospital.
Let me consider all of the neighbors and see if any of them
can do better than a cost of 17.
And it turns out there are a couple of ways that we could do that,
and it doesn't matter if we randomly choose among all the ways
that are the best.
But one such possible way is by taking a look at this hospital
here and considering the directions in which it might
move if we hold this hospital constant (12:18).
If we take this hospital and move it one square up, for example,
that doesn't really help us.
It gets closer to the house up here, but it gets further away from the house
down here, and it doesn't really change anything
for the two houses along the left-hand side.
But if we take this hospital on the right and move it one square down,
it's the opposite problem.
It gets further away from the house up above, and it gets closer to the house
down below.
The real idea, the goal should be to be able to take this hospital
and move it one square to the left (12:47).
By moving it one square to the left, we move
it closer to both of these houses on the right
without changing anything about the houses on the left.
For them, this hospital is still the closer one, so they aren't affected.
So we're able to improve the situation by picking a neighbor that results
in a decrease in our total cost.
And so we might do that, move ourselves from this current state to a neighbor
by just taking that hospital and moving it.
And at this point, there's not a whole lot that
can be done with this hospital, but there's still
other optimizations we can make, other neighbors we can move to that
are going to have a better value.
If we consider this hospital, for example (3:19),
we might imagine that right now it's a bit far up, that both of these houses
are a little bit lower, so we might be able to do better
by taking this hospital and moving it one square down,
moving it down so that now, instead of a cost of 15, we're down (13:33) to a cost of 13
for this particular configuration.
And we can do even better by taking the hospital
and moving it one square to the left.
Now, instead of a cost of 13, we have a cost of 11
because this house is one away from the hospital.
This one is four away.
This one is three away, and this one is also three away.
So we've been able to do much better than that initial cost
that we had using the initial configuration just
by taking every state and asking ourselves the question,
can we do better by just making small, incremental changes,
moving to a neighbor, moving to a neighbor, and moving to a neighbor
after that?
And now, at this point, we can potentially see that, at this point,
the algorithm is going to terminate (14:10).
There's actually no neighbor we can move to that is
going to improve the situation, get us a cost that is less than 11.
Because if we take this hospital and move it up or to the right, well,
that's going to make it further away.
If we take it and move it down, that doesn't really change the situation.
It gets further away from this house but closer to that house.
And likewise, the same story was true for this hospital.
Any neighbor we move it to, up, left, down, or right,
is either going to make it further away from the houses and increase the cost,
or it's going to have no effect on the cost whatsoever.
And so the question we might now ask is, is this the best we could do? (14:45)
Is this the best placement of the hospitals we could possibly have?
And it turns out the answer is "no" because there's a better way that we
could place these hospitals.
And in particular, there are a number of ways you could do this.
But one of the ways is by taking this hospital (14:58) here and moving it
to this square, for example, moving it diagonally by one square,
which was not part of our definition of "neighbor."
We could only move left, right, up, or down.
But this is, in fact, better.
It has a total cost of 9.
It is now closer to both of these houses.
And as a result, the total cost is less.
But we weren't able to find it.
Because in order to get there, we had to go
through a state that actually wasn't any better than the current state
that we had been on previously.
And so this appears to be a limitation or a concern
you might have as you go about trying to implement
a hill-climbing algorithm is that it might not always
give you the optimal solution.
If we're trying to maximize the value of any particular state,
we're trying to find the global maximum, a concern
might be that we could get stuck at one of the `local maxima` (15:48),
highlighted here in blue, where a local maxima is any state whose value is
higher than any of its neighbors.
If we ever find ourselves at one of these two states
when we're trying to maximize the value of the state,
we're not going to make any changes.
We're not going to move left or right.
We're not going to move left here because those states are worse.
But yet we haven't found the global optimum.
We haven't done as best as we could do.
And likewise, in the case of the hospitals, what we're ultimately
trying to do is find a global minimum, find a value
that is lower than all of the others.
But we have the potential to get stuck at one of the local minimum, any
of these states whose value is lower than all of its neighbors
but still not as low as the local minimum.
And so `the takeaway here is that it's not always going to be the case that when we run this naive, hill-climbing algorithm that we're always going to find the optimal solution`.
There are things that could go wrong.
If we started here, for example, and tried
to maximize our value as much as possible,
we might move to the highest possible neighbor,
move to the highest possible neighbor, move to the highest possible neighbor,
and stop, and never realize that there is actually
a better state way over there that we could have gone to instead.
And other problems you might imagine just
by taking a look at this state-space landscape
are these various different types of plateaus, something
like this `flat local maximum` (17:00) here where all six of these states each
have the exact same value.
And so, in the case of the algorithm we showed before, none of the neighbors
are better, so we might just get stuck at this flat local maximum.
And even if you allowed yourself to move to one of the neighbors,
it wouldn't be clear which neighbor you would ultimately move to,
and you could get stuck here as well.
And there's another one over here.
This one is called a `shoulder` (17:22).
It's not really a local maximum because there's still
places where we can go higher--
not a local minimum because we can go lower.
So we can still make progress, but it's still
this flat area where if you have a local search algorithm,
there is potential to get lost here, unable to make
some upward or downward progress depending on whether we're trying
to maximize or minimize and, therefore, another potential for us
to be able to find a solution that might not actually be the optimal solution.
And so because of this potential, the potential
that hill climbing has to not always find us the optimal result,
it turns out there are a number of different varieties and variations
on the hill-climbing algorithm that help to solve the problem better
depending on the context.
And depending on the specific type of problem, some of these variants
might be more applicable than others.
What we've taken a look at so far is a version of hill climbing generally
called "steepest-ascent hill climbing" where the idea of steepest-ascent hill
climbing is we are going to choose the highest-valued neighbor in the case
where we're trying to maximize or the lowest-valued neighbor in cases where
we're trying to minimize.
But generally speaking, if I have five neighbors
and they're all better than my current state,
I will pick the best one of those five.
Now, sometimes, that might work pretty well.
It's sort of a greedy approach of trying to take the best
operation at any particular time step.
But it might not always work.There might be cases where actually I want
to choose an option that is slightly better than me
but maybe not the best one because that, later on, might
lead to a better outcome ultimately.
So there are other variants that we might consider
of this basic hill-climbing algorithm.
One is known as
#### "stochastic hill climbing." (18:47)
And in this case, we choose randomly from all
of our higher-valued neighbors.
So if I'm at my current state and there are five neighbors that
are all better than I am, rather than choosing the best
one as steepest ascent would do, stochastic will just choose randomly
from one of them, thinking that if it's better, then it's better,
and maybe there's a potential to make forward progress
even if it is not locally the best option I could possibly choose.
First-choice hill climbing ends up just choosing
the very first highest-valued neighbor, but it
follows behaving on a similar idea.
Rather than consider all of the neighbors,
as soon as we find a neighbor that is better than our current state,
we'll go ahead and move there, so maybe some efficiency improvements
there and maybe has the potential to find
a solution that the other strategies weren't able to find.
And with all of these variants, we still suffer
from the same potential risk, this risk that we might end up
at a local minimum or a local maximum.
And we can reduce that risk by repeating the process multiple times.
So one variant of hill climbing is `random-restart` (19:45) hill
climbing where the general idea is we'll conduct hill climbing multiple times.
If we apply a steepest-ascent hill climbing, for example,
we'll start at some random state, try and figure out
how to solve the problem, and figure out what is the local maximum
or local minimum we get to.
And then we'll just randomly restart and try again,
choose a new starting configuration, try and figure out
what the local maximum or minimum is, and do this some number of times.
And then after we've done it some number of times,
we can pick the best one out of all of the ones that we've taken a look at.
So there's another option we have access to as well.
And then, although I said the generally local search will usually
just keep track of a single node and then move to one of its neighbors,
there are variants of hill climbing that are known as `local beam searches` (20:27)
where, rather than keep track of just one current best state,
we're keeping track of k highest-valued neighbors, such
that rather than starting at one random initial configuration,
I might start with three, or four, or five,
randomly generate all the neighbors, and then pick like the three, or four,
or five best of all of the neighbors that I find and continually
repeat this process with the idea being that now I
have more options that I'm considering and more ways
that I could potentially navigate myself to the optimal solution that
might exist for a particular problem.
So let's now take a look at some actual code
that can implement some of these kinds of ideas, something
like steepest-ascent hill climbing, for example, for trying
to solve this hospital problem.
So I'm going to go ahead and go into my hospital's directory
where I've actually set up the basic framework for solving
this type of problem.
I'll go ahead and go into hospitals.py (21:16), and we'll take a look
at the code we've created here.
I've defined `a class that is going to represent the state space.`
So `the space has a height, and a width, and also some number of hospitals`.
So you can configure, how big is your map?
How many hospitals should go here?
We have a function for adding a new house to the state space and then
some functions that are going to get me all of the available spaces for if I
want to randomly place hospitals in particular locations.
And here now is the `hill-climbing algorithm` (21:44).
So what are we going to do in the hill-climbing algorithm?
Well, we're going to start by randomly initializing
where the hospitals are going to go.
We don't know where the hospitals should actually be,
so let's just randomly place them.
So here, I'm running a loop for each of the hospitals that I have.
I'm going to go ahead and add a new hospital at some random location.
So I basically get all of the available spaces,
and I randomly choose one of them as where I would
like to add this particular hospital.
I have some logging output and generating some images, which we'll
take a look at a little bit later.
But here is the key idea.
So I'm going to just keep repeating this algorithm.
I could specify a maximum of how many times I want it to run,
or I could just run it up until it hits a local maximum or a local minimum.
And now, we'll basically consider all of the hospitals that could potentially
move, so consider each of the two hospitals or more hospitals
if there are more than that, and consider all of the places
where that hospital could move to, some neighbor
of that hospital that we can move the neighbor to and then see,
is this going to be better than where we were currently?
So if it is going to be better, then we'll
go ahead and update our best neighbor and keep track of this new best
neighbor that we found.
And then afterwards, we can ask ourselves
the question, if best neighbor cost is greater
than or equal to the cost of the current set of hospitals, meaning
if the cost of our best neighbor is greater than the current cost,
meaning our best neighbor is worse than our current state,
well, then we shouldn't make any changes at all.
And we should just go ahead and return the current set of hospitals.
But otherwise, we can update our hospitals
in order to change them to one of the best neighbors.
And if there are multiple that are all equivalent,
I'm here using random.choice to say, go ahead and choose one randomly.
So this is really just a Python implementation
of that same idea that we were just talking about,
this idea of taking a current state, some current set of hospitals,
generating all of the neighbors, looking at all
of the ways we could take one hospital and move it one square to the left,
or right, or up, or down, and then figuring out,
based on all of that information, which is the best
neighbor or the set of all the best neighbors, and then choosing from one
of those.
And each time, we go ahead and generate an image in order to do that.
And so now what we're doing is if we look down in the bottom,
I'm going to randomly generate a space with height 10 and width 20.
And I'll say, go ahead and put three hospital somewhere in the space.
I'll randomly generate 15 houses that I just go ahead
and add in random locations.
And now I'm going to run this hill-climbing algorithm in order
to try and figure out where we should place those hospitals.
So we go ahead and `run this program` (24:20) by running "python hospitals."
And we see that we started-- our initial state had a cost of 72,
but we were able to continually find neighbors
that were able to decrease that cost, decrease to 69, 66, 63,
so on and so forth, all the way down to 53 as the best neighbor
we were able to ultimately find.
And we can take a look at what that looked
like by just opening up these files.
So here, for example, was the initial configuration.
We randomly selected a location for each of these 15 different houses
and then randomly selected locations for 1,
2, 3 hospitals that were just located somewhere inside of the state space.
And if you add up all the distances from each of the houses
to their nearest hospital, you get a total cost of about 72.
And so now the question is, what neighbors can we
move to that improve the situation?
And it looks like the first one the algorithm found
was by taking this house that was over there on the right
and just moving it to the left.
And that probably makes sense.
Because if you look at the houses in that general area,
really these five houses look they're probably
the ones that are going to be closest to this hospital over here (25:24).
Moving it to the left decreases the total distance at least
to most of these houses, though it does increase that distance for one of them.
And so we're able to make these improvements to the situation
by continually finding ways that we can move these hospitals around
until we eventually settle at this particular state that has a cost of 53.
Or we figured out a position for each of the hospitals, and now none
of the neighbors that we can move to are actually
going to improve the situation.
We can take this hospital, and this hospital, and that hospital
and look at each of the neighbors, and none of those
are going to be better than this particular configuration.
And again, that's not to say that this is the best we could do.
There might be some other configuration of hospitals that is a global minimum.
And this might just be a local minimum, that
is, the best of all of its neighbors but maybe not
the best in the entire possible state space.
And you could search through the entire state space
by considering all of the possible configurations for hospitals.
But ultimately, that's going to be very time intensive,
especially as our state space gets bigger
and there might be more and more possible states.
It's going to take quite a long time to look through all of them.
And so being able to use these sort of local search algorithms
can often be quite good for trying to find the best solution we can do.
And especially if we don't care about doing the best possible
and we just care about doing pretty good and finding
a pretty good placement of those hospitals,
then these methods can be particularly powerful.
But of course, we can try and mitigate some of this concern by instead
of using hill climbing to use `random restart`, this idea of
rather than just hill climb one time, we can hill climb multiple times
and, say, try hill climbing a whole bunch of times on the exact same map
and figure out, what is the best one that we've been able to find?
And so I've here implemented a `function` for random restart
that `restarts some maximum number of times`.
And what we're going to do is repeat that number of times this process
of just go ahead and run the hill-climbing algorithm,
figure out what the cost is of getting from all the houses to the hospitals,
and then figure out, is this better than we've done so far?
So I can try this exact same idea where instead of running hill climbing,
I'll go ahead and run random_restart.
And I'll randomly restart maybe 20 times, for example.
And we'll go ahead, and now I'll remove all the images
and then rerun the program.
And now we started by finding a original state.
When we initially ran hill climbing, the best cost we were able to find was 56.
Each of these iterations is a different iteration
of the hill-climbing algorithm.
We're running hill climbing not one time but 20 times here,
each time going until we find a local minimum, in this case.
And we look and see each time, did we do better than we
did the best time we've done so far?
So we went from 56 to 46.
This one was greater, so we ignored it.
This one was 41, which was less, so we went ahead and kept that one.
And for all of the remaining 16 times that we
tried to implement hill climbing and we tried
to run the hill-climbing algorithm, we couldn't do any better than that 41.
Again, maybe there is a way to do better that we just didn't find,
but it looks like that way ended up being
a pretty good solution to the problem.
That was attempt number 3 starting from counting at zero.
So we can take a look at that, open up number 3,
and this was the state that happened to have a cost of 41,
that after running the hill-climbing algorithm
on some particular, random initial configuration of hospitals,
this is what we found was the local minimum in terms
of trying to minimize the cost.
And it looks like we did pretty well, that this hospital is
pretty close to this region.
This one is pretty close to these houses here.
This hospital looks about as good as we can
do for trying to capture those houses over on that side.
And so these sorts of algorithms can be quite useful for trying
to solve these problems.
But the real problem with many of these different types
of hill climbing, steepest ascents, stochastic, first choice, and so forth
is that they never make a move that makes our situation worse.
They're always going to take ourselves in our current state,
look at the neighbors, and consider, can we do better than our current state,
and move to one of those neighbors.
Which of those neighbors we choose might vary
among these various different types of algorithms,
but we never go from a current position to a position that
is worse than our current position.
And ultimately, that's what we're going to need
to do if we want to be able to find a global maximum or a global minimum.
Because sometimes if we get stuck, we want
to find some way of dislodging ourselves from our local maximum or local minimum
in order to find the global maximum or the global minimum
or increase the probability that we do find it.
And so the most popular technique for trying
to approach the problem from that angle is a technique
known as `"simulated annealing,"` (29:50) simulated
because it's modeling after a real physical process of annealing where you
can think about this in terms of physics, a physical situation
where you have some system of particles.
And you might imagine that when you heat up a particular physical system,
there's a lot of energy there.
Things are moving around quite randomly.
But over time, as the system cools down, it eventually
settles into some final position.
And that's going to be the general idea of simulated annealing.
We're going to simulate that process of some high-temperature system
where things are moving around randomly quite frequently but, over time,
decreasing that temperature until we eventually
settle at our ultimate solution.
And the idea is going to be if we have some state-space landscape that
looks like this and we begin at its initial state
here, if we're looking for a global maximum
and we're trying to maximize the value of the state,
our traditional hill-climbing algorithms would just take the state,
and look at the two neighbor ones, and always pick
the one that is going to increase the value of the state.
But if we want some chance of being able to find the global maximum,
we `can't always make good moves`.
We `have to sometimes make bad moves` and allow ourselves
to make a move in a direction that actually seems, for now, to make
our situation worse such that later we can find our way up
to that global maximum in terms of trying to solve that problem.
Of course, once we get up to this global maximum,
once we've done a whole lot of the searching,
then we probably don't want to be moving to states
that are worse than our current state.
And so this is where this metaphor for annealing
starts to come in where we want to start making more random moves
and, over time, start to make fewer of those random moves
based on a particular `temperature` schedule.
So the basic outline looks something like this.
Early on in simulated annealing, we have a higher temperature state.
And what we mean by a "higher temperature state"
is that we are more likely to accept neighbors
that are worse than our current state, that we might look at our neighbors,
and if one of our neighbors is worse than the current state,
especially if it's not all that much worse,
if it's pretty close but just slightly worse,
then we might be more likely to accept that and go ahead and move
to that neighbor anyways.
But later on as we run simulated annealing,
we're going to decrease that temperature.
And at a lower temperature, we're going to be less likely to accept neighbors
that are worse than our current state.
Now, to formalize this and put a little bit of pseudocode to it,
here is what that algorithm might look like.
And we have a function called "simulated annealing" that
takes as input the problem we're trying to solve
and also potentially some maximum number of times
we might want to run the `simulated annealing` (32:17)
process, how many different neighbors we're going to try and look for.
And that value is going to vary based on the problem you're trying to solve.
We'll again start with some current state
that will be equal to the initial state of the problem.
But now, we need to repeat this process over and over for max number of times,
repeat some process some number of times where we're first
going to calculate a temperature.
And this temperature function takes the current time t,
starting at 1 going all the way up to max,
and then gives us some temperature that we can use in our computation
where the idea is that this temperature is going to be higher early on,
and it's going to be lower later on.
So there are a number of ways this temperature function could often work.
One of the simplest ways is just to say it is like the proportion of time
that we still have remaining.
Out of max units of time, how much time do we have remaining?
You start off with a lot of that time remaining.
And as time goes on, the temperature is going
to decrease because you have less and less of that remaining time still
available to you.
So we calculate a temperature for the current time.
And then we pick a random neighbor of the current state.
No longer are we going to be picking the best neighbor that we possibly can
or just one of the better neighbors that we can.
We're going to pick a random neighbor.
It might be better.
It might be worse.
But we're going to calculate that.
We're going to calculate delta E, "E" for "energy" in this case, which
is just, how much better is the neighbor than the current state?
So if delta E is positive, that means the neighbor
is better than our current state.
If delta E is negative, that means the neighbor
is worse than our current state.
And so we can then have a condition that looks like this.
If delta E is greater than 0, that means the neighbor state
is better than our current state.
And if ever that situation arises, we'll just
go ahead and update "current" to be that neighbor.
Same as before, move where we are currently
to be the neighbor because the neighbor is better than our current state.
We'll go ahead and accept that.
But now the difference is that whereas before we never,
ever wanted to take a move that made our situation worse,
now we sometimes want to move, [? go ?] make
a move that is actually going to make our situation worse.
Because sometimes we're going to need to dislodge ourselves
from a local minimum or a local maximum to increase the probability that we're
able to find the global minimum or the global maximum a little bit later.
And so how do we do that?
How do we decide to sometimes accept some state that
might actually be worse?
Well, we're going to accept a worse state with some probability.
And that probability needs to be based on a couple of factors.
It needs to be based, in part, on the temperature where if the temperature is
higher, we're more likely to move to a worse neighbor,
and if the temperature is lower, we're less
likely to move to a worse neighbor.
But it also, to some degree, should be based on delta
E. If the neighbor is much worse than the current state,
we probably want to be less likely to choose that
than if the neighbor is just a little bit worse than the current state.
So again, there are a couple of ways you could calculate this.
But it turns out one of the most popular is just
to calculate E to the power of delta E over t where E is just a constant.
Delta E over t are based on delta E and t here.
We calculate that value, and that'll be some value between 0 and 1,
and that is the probability with which we should just say, all right,
let's go ahead and move to that neighbor.
And it turns out that if you do the math for this value when delta E is such
that the neighbor is not that much worse than the current state, that's
going to be more likely that we're going to go ahead and move to that state.
And likewise, when the temperature is lower,
we're going to be less likely to move to that neighboring state as well.
So now this is the big picture for `simulated annealing` (35:37),
this process of taking the problem and going ahead and generating
random neighbors.
We'll always move to a neighbor if it's better than our current state.
But even if the neighbor is worse than our current state,
we'll sometimes move there depending on how much worse it is and also based
on the temperature.
And as a result, the hope, the goal of this whole process
is that as we begin to try and find our way to the local-- the global maximum
or the global minimum, we can dislodge ourselves
if we ever get stuck at a local maximum or a local minimum
in order to eventually make our way to exploring the part of the state space
that is going to be the best.
And then as the temperature decreases, eventually we
settle there without moving around too much
from what we've found to be the globally best thing that we can do thus far.
So at the very end, we just return whatever
the current state happens to be.
And that is the conclusion of this algorithm.
And we've been able to figure out what the solution is.
And these types of algorithms have a lot of different applications.
Anytime you can take a problem and formulate it as something
where you can explore a particular configuration and then ask,
are any of the neighbors better than this current configuration,
and have some way of measuring that, then there
is an applicable case for these hill-climbing, simulated-annealing
types of algorithms.
So sometimes it can be for facility location-type problems,
like for when you're trying to plan a city
and figure out where the hospitals should be.
But there are definitely other applications as well.
And one of the most famous problems in computer science
is the `traveling salesman problem` (37:04).
Traveling salesman problem generally is formulated like this.
I have a whole bunch of cities here indicated by these dots.
And what I'd like to do is find some route
that takes me through all of the cities and ends up back where I started,
so some route that starts here, goes through all these cities,
and ends up back where I originally started.
And what I might like to do is minimize the total distance
that I have to travel in order to-- or the total cost of taking
this entire path.
And you can imagine this is a problem that's
very applicable in situations like when delivery companies are
trying to deliver things to a whole bunch of different houses.
They want to figure out, how do I get from the warehouse
to all these various different houses and get back
again all using as minimal time, and distance, and energy as possible?
So you might want to try to solve these sorts of problems.
But it turns out that solving this particular kind of problem
is very computationally difficult and is a very computationally expensive task
to be able to figure it out.
And this falls under the category of what are known as "NP-complete
problems," problems that there is no known efficient way to try and solve
these sorts of problems.
And so what we ultimately have to do is come up
with some approximation, some ways of trying to find a good solution even
if we're not going to find the globally best solution that we possibly can,
at least not in a feasible or tractable amount of time.
And so what we could do is take the traveling salesman problem,
and try to formulate it using local search,
and ask a question like, all right, I can
pick some state, some configuration, some route between all of these nodes.
And I can measure the cost of that state, figure out what the distance is.
And I might now want to try to minimize that cost as much as possible.
And then the only question now is, what does it
mean to have a neighbor of this state?
What does it mean to take this particular route
and have some neighboring route that is close to it but slightly different
in such that it might have a different total distance?
And there are a number of different definitions
for what a neighbor of a traveling salesman configuration might look like.
But one way is just to say, a neighbor is
what happens if we pick two of these edges between nodes and switch them,
effectively.
So for example, I might pick these two edges here,
`these two` (39:11) that just happen across-- this node goes here.
This node goes there--
and go ahead and switch them.
And what that process will generally look
like is removing both of these edges from the graph, taking this node,
and connecting it to the node it wasn't connected to,
so connecting it up here instead.
We'll need to take these arrows that were originally going this way
and reverse them, so move them going the other way, and then just fill
in that last remaining blank, add an arrow that goes in that direction
instead.
So by taking two edges and just switching them,
I have been able to consider one possible neighbor
of this particular configuration.
And it looks like this neighbor is actually better.
It looks like this probably travels a shorter distance in order
to get through all the cities through this route than the current state did.
And so you could imagine implementing this idea
inside of a hill-climbing or simulated-annealing algorithm
where we repeat this process to try and take a state of this traveling salesman
problem, look at all of the neighbors, and then move to the neighbors
if they're better, or maybe even move to the neighbors
if they're worse until we eventually settle upon some best solution
that we've been able to find.
And it turns out that these types of approximation algorithms,
even if they don't always find the very best solution,
can often do pretty well at trying to find solutions that are helpful too.
So that then was a look at local search, a particular category of algorithms
that can be used for solving a particular type of problem where
we don't really care about the path to the solution.
I didn't care about the steps I took to decide where the hospitals should go.
I just cared about the solution itself.
I just care about where the hospitals should be
or what the route through the traveling salesman journey really ought to be.
Another type of algorithm that might come up
are known as these categories of linear-programming types of problems.
And
##### linear programming (40:57)
often comes up in the context
where we're trying to optimize for some mathematical function.
But oftentimes, linear programming will come up
when we might have real real numbered values so that it's not
just like discrete, fixed values that we might have
but any decimal values that we might want to be able to calculate.
And so linear programming is a family of types
of problems where we might have a situation that
looks like this where the goal of linear programming
is to minimize a cost function.
And you can invert the numbers and, say, try and maximize it,
but often we'll frame it as trying to minimize the cost function that
has some number of variables, x1, x2, x3,
all the way up to xn, just some number of variables that are involved,
things that I want to know the values to.
And this cost function might have coefficients
in front of those variables.
`(41:37)`
And this is what we would call a "linear equation" where we just
have all of these variables that might be multiplied by a coefficient
and then added together.
We're not going to square anything or cube anything
because that'll give us different types of equations.
With linear programming, we're just dealing
with linear equations in addition to `linear constraints` where
a constraint is going to look something like if we sum up
this particular equation that is just some linear combination of all
of these variables, it is less than or equal to some bound b.
And we might have a whole number of these various different constraints
that we might place onto our linear programming exercise.
And likewise, just as we can have constraints
that are saying this linear equation is less than or equal to some bound b,
it might also be equal to something.
But if you want some sum of some combination of variables
to be equal to a value, you can specify that.
And we can also maybe specify that each variable has lower and upper balance,
that it needs to be a positive number, for example,
or it needs to be a number that is less than 50, for example.
And there are a number of other choices that we
can make there for defining what the bounds of a variable are.
But it turns out that if you can take a problem
and formulate it in these terms, formulate the problem
as your goal is to minimize a cost function,
and you're minimizing that cost function subject to particular constraints,
subjects to equations that are of the form like this,
of some sequence of variables is less than a bound
or is equal to some particular value, then
there are a number of algorithms that already exist
for solving these sorts of problems.
So let's go ahead and take a look at an example.
Here's an `example of a problem that might come up in the world of linear programming`.
Often, this is going to come up when we're trying to optimize for something,
and we want to be able to do some calculations,
and we have constraints on what we're trying to optimize.
And so it might be something like this.
In the context of a factory, we have 2 machines, x1 and x2.
x1 costs $50 an hour to run.
x2 costs $80 an hour to run.
And our goal, what we're trying to do, our objective
is to minimize the total cost.
So that's what we'd like to do.
But we need to do so subject to certain constraints.
So there might be a labor constraint that X1
requires 5 units of labor per hour.
x2 requires 2 units of labor per hour, and we
have a total of 20 units of labor that we have to spend.
So this is a constraint.
We have no more than 20 units of labor that we can spend,
and we have to spend it across x1 and x2, each of which
requires a different amount of labor.
And we might also have a constraint like this
`(44:02)`
that tells us x1 is going to produce 10 units of output per hour.
x2 is going to produce 12 units of output per hour.
And the company needs 90 units of output.
So we have some goal, something we need to achieve.
We need to achieve 90 units of output, but there are some constraints
that x1 can only produce 10 units of output per hour.
x2 produces 12 units of output per hour.
These types of problems come up quite frequently.
And you can start to notice patterns in these types of problems, problems where
I am trying to optimize for some goal, minimizing cost, maximizing
output, maximizing profits, or something like that.
And there are constraints that are placed on that process.
And so now we just need to formulate this problem
in terms of linear equations.
And so let's start with this first point.
Two machines, x1 and x2, x costs $50 an hour. x2 costs $80 an hour.
Here we can come up with an objective function that might look like this.
`50x1 + 80x2`
This is our cost function, rather--
50 times x1 plus 80 times x2 where x1 is going
to be a variable representing how many hours we run machine x1 for.
x2 is going to be a variable representing how many hours
are we running machine x2 for.
And what we're trying to minimize is this cost function,
which is just how much it costs to run each of these machines per hour
summed up.
This is an example of a linear equation, just some combination
of these variables plus coefficients that are placed in front of them.
And I would like to minimize that total value,
but I need to do so subject to these constraints--
x1 requires 50 units of labor per hour, x2 requires two,
and we have a total of 20 units of labor to spend.
And so that gives us a constraint of this form--
5 times x1 plus 2 times x2 is less than or equal to 20.
20 is the total number of units of labor we have to spend.
And that's spent across x1 and x2, each of which
requires a different number of units of labor per hour, for example.
And finally, we have this constraint here.
x1 produces 10 units of output per hour, and x2 produces 12,
and we need 90 units of output.
And so this might look something like this, that 10x 1 plus 12x 2,
this is amount of output per hour.
It needs to be at least 90.
If we can do better, great, but it needs to be at least 90.
And if you recall from my formulation before, I
said that generally speaking in linear programming,
we deal with equals constraints or less-than or equal-to constraints.
So we have a greater-than or equal-to sign here.
That's not a problem.
Whenever we have a greater-than or equal-to sign,
we can just multiply the equation by negative 1,
and that will flip it around to a less than or equals negative 90,
for example, instead of a greater than or equal to 90.
And that's going to be an equivalent expression that we
can use to represent this problem.
So now that we have this cost function and these constraints
that it's subject to, it turns out there are
a number of algorithms that can be used in order to solve
these types of problems.
And these problems go a little bit more into geometry and linear algebra
than we're really going to get into.
But the most com-- popular of these types of algorithms
are simplex, which was one of the first algorithms discovered
for trying to solve linear programs.
And later on, a class of interior-point algorithms
can be used to solve this type of problem as well.
The key is not to understand exactly how these algorithms work
but to realize that these algorithms exist for efficiently finding solutions
anytime we have a problem of this particular form.
And so we can take a look, for example, at the production directory
here where here we have a file called production.py
`(47:33)`
where here I'm using scipy, which is just
a library for a lot of science-related functions within Python.
And I can go ahead and just run this optimization function
in order to run a linear program.
.linprog here is going to try and solve this linear program for me where I
provide to this expression, to this function call all of the data about
my linear program.
So it needs to be in a particular format, which
might be a little confusing at first, but this first argument
to scipy.optimize.linprog is the cost function,
which is, in this case, just an array or a list
that has 50 and 80 because my original cost function was
50 times x1 plus 80 times x2.
So I just tell Python, 50 and 80, those are the coefficients
that I am now trying to optimize for.
And then I provide all of the constraints.
So the constraints-- and I wrote them up above in comments--
is the constraint 1 is 5x_1 plus 2x_2 is less than or equal to 20.
And constraint 2 is negative 10x_1 plus negative 12x_2 is less than
or equal to negative 90.
And so scipy expects these constraints to be in a particular format.
It first expects me to provide all of the coefficients
for the upper-bound equations. "ub" is just for "upper bound"
where the coefficients of the first equation are 5 and 2
because we have 5x_1 and 2x_2.
And the coefficients for the second equation
are negative 10 and negative 12 because I have
negative 10x_1 plus negative 12x_2.
And then here we provide it as a separate argument
just to keep things separate what the actual bound is.
What is the upper bound for each of these constraints?
Well, for the first constraint, the upper bound is 20.
That was constraint number 1.
And then for constraint number 2, the upper bound is -90.
So a bit of a cryptic way of representing it.
It's not quite as simple as just writing the mathematical equations.
What really is being expected here are all of the coefficients
and all of the numbers that are in these equations
by first providing the coefficients for the cost function,
then providing all the coefficients for the inequality constraints,
and then providing all of the upper bounds for those inequality
constraints.
And once all of that information is there,
then we can run any of these interior-point algorithms
or the simplex algorithm.
Even if you don't understand how it works, you can just run the function
and figure out what the result should be.
And here, I said, if the result is a success,
we were able to solve this problem, go ahead and print out
what the value of x1 and x2 should be.
Otherwise, go ahead and print out no solution.
And so if I run this program by running python production.py,
it takes a second to calculate.
But then we see here is what the optimal solution should be.
x1 should run for 1.5 hours.
x2 should run for 6.25 hours.
And we were able to do this by just formulating
the problem as a linear equation that we were
trying to optimize, some cost that we were trying to minimize,
and then some constraints that were placed on that.
And many, many problems fall into this category of problems
that you can solve if you can just figure out
how to use equations and use these constraints to represent
that general idea.
And that's a theme that's going to come up a couple of times
today where we want to be able to take some problem,
and reduce it down to some problem we know how to solve in order
to begin to find a solution, and to use existing methods that we
can use in order to find the solution more effectively or more efficiently.
And it turns out that these types of problems where we have constraints
show up in other ways too.
And there is an entire class of problems that's
more generally just known as "constraint satisfaction" problems.
And we're going to now take a look at how you might formulate a constraint
satisfaction problem and how you might go about solving a constraint
satisfaction problem.
But the basic idea of a constraint satisfaction problem
is we have some number of variables that need to take on some values.
And we need to figure out what values each of those variables should take on.
But those variables are subject to particular constraints
that are going to limit what values those variables can actually take on.
So let's take a look at a `real-world example`, for example.
Let's look at `exam scheduling`, that I have four students here,
students 1, 2, 3, and 4.
Each of them is taking some number of different classes.
Classes here are going to be represented by letters.
So student 1 is enrolled in courses A, B,
and C. Student 2 is enrolled in courses B, D, and E, so on and so forth.
And now, say, university, for example, is trying to schedule exams
for all of these courses.
But there are only three exam slots on Monday, Tuesday and Wednesday.
And we have to schedule an exam for each of these courses.
But the constraint now, the constraint we have to deal with the scheduling
is that we don't want anyone to have to take two exams on the same day.
We would like to try and minimize that or eliminate it if at all possible.
So how do we begin to represent this idea?
How do we structure this in a way that a computer with an AI algorithm
can begin to try and solve the problem?
Well, let's in particular just look at these classes
that we might take and represent each of the courses
as some node inside of a graph.
And what we'll do is we'll create an edge between two nodes in this graph
if there is a constraint between those two nodes.
So what does this mean?
Well, we can start with student 1 who's enrolled
in courses A, B, and C. What that means is that A and B can't
have an exam at the same time.
A and C can't have an exam at the same time.
And B and C also can't have an exam at the same time.
And I can represent that in this graph by just drawing edges,
one edge between A and B, one between B and C, and then one between C and A.
And that encodes now the idea that between those nodes
there is a constraint.
And in particular, the constraint happens
to be that these two can't be equal to each other.
So there are other types of constraints that
are possible depending on the type of problem you're trying to solve.
And then we can do the same thing for each of the other students,
that for student 2 who's enrolled in courses B, D, and E, well,
that means B, D, and E, those all need to have
edges that connect each other as well.
Student 3 is enrolled in courses C, E, and F.
So we'll go ahead and take C, E, and F and connect those
by drawing edges between them too.
And then, finally, student 4 is enrolled in courses E, F, and G.
And we can represent that by drawing edges between E, F, and G
although E and F already had an edge between them.
We don't need another one because this constraint is just encoding the idea
that course E and course F cannot have an exam on the same day.
So this then is what we might call the `"constraint graph` (53:59)."
There's some graphical representation of all of my variables, so to speak,
and the constraints between those possible variables where,
in this particular case, each of the constraints represents an inequality
constraint, that an edge between B and D means whatever value the variable B
takes on cannot be the value that the variable D takes on as well.
So what then, actually, is a constraint satisfaction problem?

# Constraint Satisfaction Problem (54:30)

    - Set of variables {X1, X2, ..., Xn}
    - Set of domains for each variable {D1, D2, ..., Dn}
    - Set of constraints C

## Constraint classification

    - A Unary constraint is a constraint that involves only one variable
    - A Binary constraint is a constraint that invvolves two variables

Well, a constraint satisfaction problem is just some set of variables,
x1 all the way through xn, some set of domains for each of those variables.
So every variable needs to take on some values.
Maybe every variable has the same domain,
but maybe each variable has a slightly different domain.
And then there's a set of constraints.
So we'll just call a set C that has some constraints that
are placed upon these variables, like x1 is not equal to x2,
but there could be other forms too, like maybe x1 equals x2 plus 1 if you--
if these variables are taking on numerical values in their domain,
for example.
The types of constraints are going to vary based on the types of problems.
And constraint satisfaction shows up all over the place
as well in any situation where we have variables that
are subject to particular constraints.
So one popular game is `Sudoku` (55:11), for example,
this 9-by-9 grid where you need to fill in numbers in each of these cells,
but you don't want to make sure there's--
you want to make sure there is never a duplicate number in any row,
or in any column, or in any grid of 3-by-3 cells, for example.
So what might this look like as a constraint satisfaction problem?
Well, my variables are all of the empty squares in the puzzle,
so represented here is just like an x, y-coordinate, for example,
as all of the squares where I need to plug in a value
where I don't know what value it should take on.
The domain is just going to be all of the numbers from 1 through 9, any value
that I could fill in to one of these cells.
So that is going to be the domain for each of these variables.
And then the constraints are going to be of the form like this cell can't
be equal to this cell, can't be equal to this cell, can't be--
and all of these need to be different, for example,
and same for all of the rows, and the columns, and the 3-by-3 squares
as well.
So those constraints are going to enforce
what values are actually allowed.
And we can formulate the same idea in the case of this exam scheduling
problem where the variables we have are the different courses, A up through G.
The domain for each of these variables is going
to be Monday, Tuesday, and Wednesday.
Those are the possible values that each of the variables
can take on that, in this case, just represent,
when is the exam for that class?
And then the constraints are of this form--
A is not equal to B. A is not equal to C,
meaning A and B can't have an exam on the same day.
A and C can't have an exam on the same day.
Or more formally, these two variables cannot take on the same value within
their domain.
So that then is this `formulation of a constraint satisfaction problem` (56:48)
that we can begin to use to try and solve this problem.
And constraints can come in a number of different forms.
There are `hard constraints`, which are constraints that must
be satisfied for a correct solution.
So something like in the Sudoku puzzle, you cannot have this cell and this cell
that are in the same row take on the same value.
That is a hard constraint.
But problems can also have `soft constraints`
where these are constraints that express some notion of preference,
that maybe A and B can't have an exam on the same day,
but maybe someone has a preference that A's exam is earlier than B's exam.
It doesn't need to be the case, but some expression
that some solution is better than another solution.
And in that case, you might formulate the problem
as trying to optimize for maximizing people's preferences.
You want people's preferences to be satisfied as much as possible.
In this case though, we'll mostly just deal with hard constraints,
constraints that must be met in order to have a correct solution to the problem.
So we want to figure out some assignment of these variables
to their particular values that is ultimately
going to give us a solution to the problem
by allowing us to assign some day to each of the classes
such that we don't have any conflicts between classes.
So it turns out that we can classify the constraints in a constraint
satisfaction problem into a number of different categories.
The first of those categories are perhaps
the simplest of the types of constraints,
which are known as `"unary constraints"` (58:13) where
a unary constraint is a constraint that just involves a single variable.
For example, a unary constraint might be something like,
A does not equal Monday, meaning course A cannot have its exam on Monday.
If for some reason the instructor for the course isn't available on Monday,
you might have a constraint in your problem
that looks like this, something that just has a single variable A in it,
and maybe says, A is not equal to Monday, or A is equal to something,
or, in the case of numbers, greater than or less than something.
A constraint that just has one variable we consider to be a unary constraint.
And this is in contrast to something like a `binary constraint` (58:49), which
is a constraint that involves two variables, for example.
So this would be a constraint like the ones we were looking at before.
Something like A does not equal B is an example of a binary constraint
because it is a constraint that has two variables involved in it, A and B.
And we represented that using some arc or some edge that
connects variable A to variable B.
And using this knowledge of, OK, what is a unary constraint, what
is a binary constraint, there are different types
of things we can say about a particular constraint satisfaction problem.
And one thing we can say is we can try and make the problem node consistent.
So what does "node consistency" mean?

### Node Consistency

    - When all the values in a variable's domain satisfy the variables unary constraints

Node consistency means that we have all of the vari-- values in a variable's
domain satisfying that variable's unary constraints.
So for each of the variables inside of our constraint satisfaction problem,
if all of the values satisfy the unary constraints
for that particular variable, we can say that the entire problem is node
consistent, or we can even say that a particular variable is
node consistent if we just want to make one node consistent within itself.
So what does that actually look like?
Let's look at now a simplified example where
instead of having a whole bunch of different classes,
we just have two classes, A and B,
`(1:00:00)`
each of which
has an exam on either Monday, or Tuesday, or Wednesday.
So this is the domain for the variable A.
And this is the domain for the variable B.
And now let's imagine we have these constraints--
A not equal to Monday, B not equal to Tuesday,
B not equal to Monday, A not equal to B. So those
are the constraints that we have on this particular problem.
And what we can now try to do is enforce node consistency.
And node consistency just means we make sure
that all of the values for any variable's domain
satisfy its unary constraints.
And so we can start by trying to make node A node consistent,
like is it consistent?
And does every value inside of A's domain satisfy it's unary constraints?
Well, initially, we'll see that Monday does not satisfy A's unary constraints.
Because we have a constraint, a unary constraint here
that A is not equal to Monday.
But Monday is still in A's domain.
And so this is something that is not node consistent because we
have Monday in the domain, but this is not
a valid value for this particular node.
And so how do we make this node consistent?
Well, to make the node node-consistent, what we'll do
is we'll just go ahead and remove Monday from A's domain.
Now A can only be on Tuesday or Wednesday
because we had this constraint that said A is not equal to Monday.
And at this point now, A is node consistent.
For each of the values that A can take on, Tuesday and Wednesday,
there is no constraint that is a unary constraint that
conflicts with that idea.
There is no constraint that says that A can't be Tuesday.
There is no unary constraint that says that A cannot be on Wednesday.
And so now we can turn our attention to B. B also has the domain Monday,
Tuesday, and Wednesday.
And we can begin to see whether those variables satisfy
the unary constraints as well.
Well, here is a unary constraint--
B is not equal to Tuesday.
And that does not appear to be satisfied by this domain of Monday, Tuesday,
and Wednesday.
Because Tuesday, this possible value that the variable B could take on,
is not consistent with this unary constraint
that B is not equal to Tuesday.
So to solve that problem, we'll go ahead and remove Tuesday from B's domain.
Now B's domain only contains Monday and Wednesday.
But as it turns out, there's yet another unary constraint
that we placed on the variable B, which is here, B is not equal to Monday.
That means that this value, Monday inside of B's domain,
is not consistent with B's unary constraints because we have
a constraint that says that B cannot be Monday.
And so we can remove Monday from B's domain.
And now we've made it through all of the unary constraints.
We've not yet considered this constraint, which
is a binary constraint, but we've considered
all of the unary constraints, all of the constraints
that involve just a single variable.
And we've made sure that every node is consistent
with those unary constraints.
So we can say that now we have enforced node consistency,
that for each of these possible nodes, we
can pick any of these values in the domain,
and there won't be a unary constraint that is violated as a result of it.
So node consistency is fairly easy to enforce.
We just take each node, make sure the values in the domain
satisfy the unary constraints.
And where things get a little bit more interesting
is what we consider different types of consistency, something
like arc consistency, for example.

#### Arc Consistency (1:03:09)

    - To make X arc-consistent with respect to Y, remove elements from X's domain until every choice for X has a possible choice for Y

And arc consistency refers to when all of the values in a variable's domain
satisfy the variable's binary constraints.
So when we're looking at trying to make A arc-consistent,
we're no longer just considering the unary constraints
that involve A. We're trying to consider all of the binary constraints that
involve A as well, so any edge that connects A
to another variable inside of that constraint graph
that we were taking a look at before.
Put a little bit more formally, arc consistency-- and "arc"
really is just another word for like an edge that connects two of these nodes
inside of our constraint graph--
we can define "arc consistency" a little more precisely like this.
In order to make some variable x arc-consistent with respect
to some other variable y, we need to remove any element from x's domain
to make sure that every choice for x, every choice in x's domain
has a possible choice for y.
So put another way, if I have a variable x
and I want to make x an arc-consistent, then
I'm going to look at all of the possible values
that x can take on and make sure that, for all of those possible values,
there is still some choice that I can make for y,
if there's some arc between x and y to make sure
that y has a possible option that I can choose as well.
So let's look at an example of that going back to this example from before.
We enforced node consistency already by saying
that A can only be on Tuesday or Wednesday
because we knew that A could not be on Monday.
And we also said that B's only domain only
consists of Wednesday because we know the B does not equal Tuesday,
and also B does not equal Monday.
So now let's begin to consider arc consistency.
Let's try and make A arc-consistent with B.
And what that means is to make A arc-consistent with respect to B means
that for any choice we make in A's domain,
there is some choice we can make in B's domain that is going to be consistent.
And we can try that.
For A, we can choose Tuesday as a possible value for A.
If I choose Tuesday for A, is there a value for B
that satisfies the binary constraint?
Well, yes, B-- Wednesday would satisfy this constraint
that A does not equal B because Tuesday does not equal Wednesday.
However, if we chose Wednesday for A, well,
then there is no choice in B's domain that satisfies this binary constraint.
There is no way I can choose something for B that satisfies A does not equal B
because I know B must be Wednesday.
And so if ever I run into a situation like this
where I see that here is a possible value for A such
that there is no choice of the value for B that satisfies the binary constraint,
well, then this is not arc-consistent.
And to make it arc-consistent, I would need to take Wednesday and remove it
from A's domain.
Because Wednesday was not going to be a possible choice I
can make for A because it wasn't consistent with this binary constraint
for B. There was no way I could choose Wednesday for A
and still have an available solution by choosing something for B as well.
So here now, I've been able to enforce arc consistency.
And in doing so, I've actually solved this entire problem.
They've given these constraints where A and B
can have exams on either Monday, or Tuesday, or Wednesday.
The only solution, as it would appear, is that A's exam must be on Tuesday,
and B's exam must be on Wednesday.
And that is the only option available to me.
So if we want to apply our consistency to a larger graph,
not just looking at one particular pair of arc consistency,
there are ways we can do that too.
And we can begin to formalize what the pseudocode would
look like for trying to write an algorithm that
enforces arc consistency.
And we'll start by defining a function called `"revise."` (1:06:51)
Revise is going to take as input a csp, otherwise known
as a "constraint satisfaction problem," and also two variables, X and Y.
And what revise is going to do is it is going
to make X arc-consistent with respect to Y,
meaning remove anything from X's domain that doesn't
allow for a possible option for Y.
And `how does this work`?
Well, we'll go ahead and first keep track of
whether or not we've made a revision.
Revise is ultimately going to return true or false.
It'll return true in the event that we did make a revision to X's domain.
It'll return false if we didn't make any change to X's domain.
And we'll see in a moment why that's going to be helpful.
But we start by saying "revised equals false."
We haven't made any changes.
Then we'll say, all right, let's go ahead
and loop over all of the possible values in X's domain,
so loop over X's domain for each little x in X's domain.
I want to make sure that for each of those choices,
I have some available choice in Y that satisfies the binary constraints that
are defined inside of my csp, inside of my constraint satisfaction problem.
So if ever it's the case that there is no value y in Y's domain
that satisfies the constraint for X and Y, well, if that's the case,
that means that this value x shouldn't be in X's domain.
So we'll go ahead and delete x from X's domain.
And I'll set revised equal to true because I did change X's domain.
I changed X's domain by removing little x.
And I removed a little x because it wasn't arc-consistent,
and there was no way I could choose a value for Y that
would satisfy this XY constraint.
So in this case, we'll go ahead and set revised equal true.
And we'll do this again and again for every value in X's domain.
Sometimes it might be fine.
In other cases, it might not allow for a possible choice for Y, in which case
we need to remove this value from X's domain.
And at the end, we just return revised to indicate whether or not
we actually made a change.
So this function then, this revise function
is effectively an implementation of what you saw me do graphically a moment ago.
And it makes one variable, X, arc-consistent with another variable,
in this case Y. But generally speaking, when
we want to enforce arc consistency, we'll
often want to enforce arc consistency not just for a single arc
but for the entire constraint satisfaction problem.
And it turns out there's an algorithm to do that as well.
And that algorithm is known as AC-3.

##### AC-3 algorithm

    - takes a constraint satisfaction problem and enforces arc consistency across the entire problem.
    - maintains a queue, a line of all the arcs it needs to make consistent
    - Over time remove things from the queue and add things we need to make arc-consistent
    - start with a queue that contains all of the edges that connect to nodes that have some sort of binary constraint between them

AC-3 takes a constraint satisfaction problem,
and it enforces arc consistency across the entire problem.
`How does it do that?` (1:09:23)
Well, it's going to basically maintain a queue or basically just
a line of all of the arcs that it needs to make consistent.
And over time, we might remove things from that queue
as we begin dealing with arc consistency.
And we might need to add things to that queue
as well if there are more things we need to make arc-consistent.
So we'll go ahead and start with a queue that
contains all of the arcs in the constraint satisfaction problem, all
of the edges that connect to nodes that have
some sort of binary constraint between them.
And now, as long as the queue is not empty, there is work to be done.
The queue is all of the things that we need to make arc-consistent.
So as long as the queue is not empty, there's still things we have to do.
What do we have to do?
Well, we'll start by dequeuing from the queue, remove something from the queue.
And strictly speaking, it doesn't need to be a queue,
but a queue is a traditional way of doing this.
We'll dequeue from the queue, and that'll
give us an arc, X and Y, these two variables where I would
like to make X arc-consistent with Y.
So how do we make X arc-consistent with Y?
Well, we can go ahead and just use that revise function
that we talked about a moment ago.
We call the revise function, passing as input the constraint satisfaction
problem, and also these variables X and Y
because I want to make X arc-consistent with Y, in other words,
remove any values from X's domain that don't leave an available option for Y.
And recall, what does revise return?
Well, it returns true if we actually made a change, if we removed something
from X's domain because there wasn't an available option for Y, for example.
And it returns false if we didn't make any change to X's domain at all.
And it turns out if revise returns false, if we didn't make any changes,
well, then there's not a whole lot more work to be done here for this arc.
We can just move ahead to the next arc that's in the queue.
But if we did make a change, if we did reduce X's domain by removing values
from X's domain, well, then what we might realize
is that this creates potential problems later on,
that it might mean that some arc that was arc-consistent with X, that node
might no longer be arc-consistent with X.
Because while there used to be an option that we could choose for X,
now there might not be because now we might have removed something
from X that was necessary for some other arc to be arc-consistent.
And so if ever we did revise X's domain, we're
going to need to add some things to the queue, some additional arcs
that we might want to check.
How do we do that?
Well, first thing we want to check is to make sure that X's domain is not 0.
If X's domain is 0, that means there are no available options for X at all,
and that means that there is no way you can solve the constraint satisfaction
problem.
If we've removed everything from X's domain,
we'll go ahead and just return false here
to indicate there's no way to solve the problem because there
is nothing left in X's domain.
`(1:12:10)`
But otherwise, if there are things left in X's domain but fewer things
than before, well, then what we'll do is we'll
loop over each variable Z that is in all of X's neighbors except for Y. Y
we already handled.
But we'll consider all X's others neighbors
and ask ourselves, all right, will that arc from each of those Zs to X--
that arc might no longer be arc-consistent.
Because while for each Z there might have been a possible option
we could choose for X to correspond with each of Z's possible values,
now there might not be because we removed some elements from X's domain.
And so what we'll do here is we'll go ahead
and enqueue, adding something to the queue, this arc,
Z, X for all of those neighbors' Zs.
So we need to add back some arcs to the queue
in order to continue to enforce arc consistency.
At the very end if we make it through all this process,
then we can return true.
But this now is AC-3, this algorithm for enforcing arc consistency
on a constraint satisfaction problem.
And the big idea is really just keep track of all of the arcs
that we might need to make arc-consistent.
Make it arc-consistent by calling the revise function.
And if we did revise it, then there are some new arcs
that might need to be added to the queue in order
to make sure that everything is still arc-consistent
even after we've removed some of the elements
from a particular variable's domain.
So what then would happen if we tried to enforce arc consistency
on a graph like this, on a graph where each of these variables
has a domain of Monday, Tuesday and Wednesday?
Well, it turns out that by enforcing arc consistency
on this graph, while it can solve some types of problems,
nothing actually changes here.
For any particular arc just considering two variables,
there's always a way for me to adjust for any
of the choices I make for one of them, make a choice for the other one
because there are three options, and I just
need the two to be different from each other.
So this is actually quite easy to just take an arc
and just declare that it is arc-consistent.
Because if I pick Monday for D, and then I
just pick something that isn't Monday for B, in arc consistency,
we only consider consistency between a binary constraint between two nodes.
And we're not really considering all of the rest of the nodes yet.
So just using AC-3, the enforcement of arc consistency,
that can sometimes have the effect of reducing
domains to make it easier to find solutions.
But it will not always actually solve the problem.
We might still need to somehow search to try and find a solution.
And we can use classical, traditional search algorithms to try to do so.
You'll recall that a search problem generally consists of these parts.

# Search Problems

    - initial state
    - actions
    - transition model
    - goal test
    - path cost function

We have some initial state, some actions,
a transition model that takes me from one state to another state,
a goal test to tell me have I satisfied my objective correctly,
and then some path cost function.
Because in the case of maze-solving, I was trying to get to my goal
as quickly as possible.
So you could formulate a csp, or a constraint satisfaction problem,
as one of these types of search problems.

## CSP's as Search Problems (1:15:42)

    - initial state: empty assignment (no variables)
    - actions: add a new {variable = value} pair to assignment
    - transition model: shows how adding an assignment changes the assignment - defines what happens when you take that action
    - goal test: check if all variables assigned and constraints all satisfied
    - path cost function is irrelevant: all paths have same cost

The initial state will just be an empty assignment
where an "assignment" is just a way for me
to assign any particular variable to any particular value.
So if an empty assignment is no variables are assigned to any values
yet, then the action I can take is adding some new variable
equals value pair to that assignment saying, for this assignment,
let me add a new value for this variable.
And the transition model just defines what happens when you take that action.
You get a new assignment that has that variable equal to that value
inside of it.
The goal test is just checking to make sure all the variables have
been assigned and making sure all the constraints have been satisfied.
And the path cost function is sort of irrelevant.
I don't really care about what the path really
is, I just care about finding some assignment that actually satisfies
all of the constraints.
So really, all the paths have the same cost.
I don't really care about the path to the goal.
I just care about the solution itself, much as we've talked about now before.
The problem here though is that if we just implement this naive search
algorithm just by implementing like breadth-first search
or depth-first search, this is going to be very, very inefficient.
And there are ways we can take advantage of efficiencies
in the structure of a constraint satisfaction problem itself.
And one of the key ideas is that we can really just order these variables.
And it doesn't matter what order we assign variables in.
The assignment A equals 2 and then B equals
8 is identical to the assignment of B equals 8 and then A equals 2.
Switching the order doesn't really change anything
about the fundamental nature of that assignment.
And so there are some ways that we can try and revise
this idea of a search algorithm to apply it specifically
for a problem like a constraint satisfaction problem.
And it turns out the search algorithm we'll generally
use when talking about constraint satisfaction problems
is something known as "backtracking search."

### Backtracking search

And the big idea of backtracking search is
we'll go ahead and make assignments from variables to values.
And if ever we get stuck, we arrive at a place
where there is no way we can make any forward progress while still preserving
the constraints that we need to enforce, we'll
go ahead and backtrack and try something else instead.
So the very basic sketch of what backtracking search looks like is it
looks like this, a function called "backtrack" that takes as input
an assignment and a constraint satisfaction problem.
So initially, we don't have any assigned variables.
So when we begin backtracking search, this assignment
is just going to be the empty assignment with no variables inside of it.
But we'll see later this is going to be a recursive function.
So backtrack takes as input the assignment and the problem.
If the assignment is complete, meaning all of the variables
have been assigned, we just return that assignment.
That of course won't be true initially because we
start with an empty assignment.
But over time, we might add things to that assignment.
So if ever the assignment actually is complete, then we're done.
Then just go ahead and return that assignment.
But otherwise, there is some work to be done.
So what we'll need to do is select an unassigned variable
for this particular problem.
So we need to take the problem, look at the variables that
have already been assigned, and pick a variable that has not yet
been assigned.
And I'll go ahead and take that variable.
And then I need to consider all of the values in that variable's domain.
So we'll go ahead and call this "domain-values" function--
we'll talk a little more about that later--
that takes a variable and just gives me back
an ordered list of all the values in its domain.
So I've taken a random, unselected variable.
I'm going to loop over all of the possible values.
And the idea is, let me just try all of these values
as possible values for the variable.
So if the value is consistent with the assignment so far,
it doesn't violate any of the constraints, well, then let's go ahead
and add variable equals value to the assignment
because it's so far consistent.
And now let's recursively call backtrack to try and make
the rest of the assignments also consistent.
So we'll ahead and call backtrack on this new assignment
that I've added this newest-- the variable equals value to.
`(1:19:05)`
And now I recursively call backtrack and see what the result is.
And if the result isn't a failure, well, then let me just return that result.
And otherwise, what else could happen?
Well, if it turns out the result was a failure, well,
then that means this value was probably a bad choice
for this particular variable.
Because when I assigned this variable equal to that value,
eventually, down the road, I ran into a situation where I violated constraints.
There was nothing more I could do.
So now I'll remove variable equals value from the assignment,
effectively backtracking to say, all right, that value didn't work.
Let's try another value instead.
And then at the very end, if we were never
able to return a complete assignment, we'll
just go ahead and return failure `(1:19:51)` because that means that none of the values
worked for this particular variable.
This now is the idea for backtracking search, to take each of the variables,
try values for them, and recursively try backtracking search, see
if we can make progress.
And if ever we run into a dead end, we run into a situation
where there is no possible value we can choose
that satisfies the constraints, we return failure, and that propagates up.
And eventually, we make a different choice
by going back and trying something else instead.
So let's `put this algorithm into practice`.
Let's actually try and use backtracking search to solve this problem now where
I need to figure out how to assign each of these courses to an exam slot
on Monday, or Tuesday, or Wednesday in such a way that it satisfies these
constraints, that each of these edges mean those two classes cannot have
an exam on the same day.
So I can start by just like starting at a node.
It doesn't really matter which I start with.
But in this case, we'll just start with A.
And I'll ask a question like, all right, let me loop
over the values in the domain.
And maybe, in this case, I'll just start with Monday and say, all right,
let's go ahead and assign A to Monday.
We'll just go in order, Monday, Tuesday, Wednesday.
And now let's consider node B. All right, so I've made an assignment to A,
so I've recursively called backtrack with this new part of the assignment.
Now I'm looking to pick another unassigned variable like B.
And I'll say, all right, maybe I'll start with Monday because that's
the very first value in B's domain.
And I ask, all right, does Monday violate any constraints?
And it turns out, yes, it does.
It violates this constraint here between A and B
because A and B are now both on Monday.
And that doesn't work because B can't be on the same day as A.
So that doesn't work, so we might instead try Tuesday, try the next value
in B's domain.
And is that consistent with the assignment so far?
Well, yeah, B-Tuesday, A-Monday.
That is consistent so far because they're not on the same day.
So that's good.
Now we can recursively call backtrack.
Try again.
Pick another unassigned variable, something like D and say,
all right, let's go through its possible values.
Is Monday consistent with this assignment?
Well, yes it is.
B and D are on different days, Monday versus Tuesday.
And A and B are also on different days, Monday versus Tuesday.
So that's fine so far too.
We'll go ahead and try again.
Maybe we'll go to this variable here, E, say, can we make that consistent?
Let's go through the possible values.
We've recursively called backtrack.
We might start with Monday and say, all right,
that's not consistent because D and E now have exams on the same day.
So we might try Tuesday instead, going to the next one, ask,
is that consistent?
Well, no, it's not because B and E, those have exams on the same day.
And so we try, all right, is Wednesday consistent?
And it turns out, all right, yes it is.
Wednesday is consistent because D and E now have exams on different days.
B and E now have exams on different days.
All seems to be well so far.
I recursively call backtrack, select another unassigned variable,
we'll say maybe to a C this time and say, all right,
let's try the values that C could take on.
Let's start with Monday.
And it turns out that's not consistent because now A and C both have
exams on the same day.
So I try Tuesday and say, that's not consistent either because B and C now
have exams on the same day.
And then I say, all right, let's go ahead and try Wednesday.
But that's not consistent either because C and E each have exams on the same day
too.
So now we've gone through all of the possible values for C, Monday, Tuesday
and Wednesday, and none of them are consistent.
There is no way we can have a consistent assignment.
Backtrack, in this case, will return a failure.
And so then we'd say, all right, we have to backtrack back to here.
Well, now for E, we've tried all of Monday, Tuesday, and Wednesday,
and none of those work.
Because Wednesday, which seemed to work, turned out to be a failure.
So that means there's no possible way we can assign E. So that's a failure too.
We have to go back up to D, which means that Monday
assignment to D, that must be wrong.
We must try something else.
So we can try, all right, what if D is Tue--
what if instead of Monday, we try Tuesday?
Tuesday, it turns out, is not consistent because B and D now
have an exam on the same day.
But Wednesday, as it turns out, works.
And now we can begin to make some forward progress again.
We go back to E and say, all right, which of these values works?
Monday turns out to work by not violating any constraints.
Then we go up to C now.
Monday doesn't work because it violates a constraint.
It violates two actually.
Tuesday doesn't work because it violates a constraint as well.
But Wednesday does work.
Then we can go to the next variable, F, and say, all right, does Monday work?
Well, no, it violates a constraint.
But Tuesday does work.
And then, finally, we can look at the last variable, G,
recursively calling backtrack one more time.
Monday is inconsistent, and that violates a constraint.
Tuesday also violates a constraint.
But Wednesday, that doesn't violate a constraint.
And so now, at this point, we recursively
call backtrack one last time.
We now have a satisfactory assignment of all of the variables.
And at this point, we can say that we are now done.
`(1:24:32)`
We have now been able to successfully assign a variable or a value
to each one of these variables in such a way
that we're not violating any constraints.
We're going to go ahead and have classes A and E have their exams on Monday.
Classes B and F can have their exams on Tuesday.
And classes C, D, and G can have their exams on Wednesday,
and there's no violated constraints that might come up there.
So that then was a graphical look at how this might work.
Let's now take a look at some code we could use to actually try and solve
this problem as well.
So here, I'll go ahead and go into the scheduling directory.
`(1:25:10)`
We're here now.
We'll start by looking at schedule0.py.
We're here.
I define a list of variables, A, B, C, D, E, F, G.
Those are all of the different classes.
Then underneath that, I define my list of constraints.
So constraint A and B, that is a constraint
because they can't be on the same day, likewise A and C, B and C,
so on and so forth, enforcing those exact same constraints.
And here then is what the backtracking function might look like.
First, if the assignment is complete, if I've
made an assignment of every variable to a value,
go ahead and just return that assignment.
Then we'll select an unassigned variable from that assignment.
Then for each of the possible values in the domain, Monday, Tuesday, Wednesday,
let's go ahead and create a new assignment that
assigns the variable to that value.
I'll call this consistent function, which I'll show you in a moment.
That checks to make sure this new assignment is consistent.
But if it is consistent, we'll go ahead and call backtrack
to go ahead and continue trying to run backtracking search.
And as long as the result is not None, meaning it wasn't a failure,
we can go ahead and return that result.
But if we make it through all the values and nothing works,
then it is a failure.
There's no solution.
We go ahead and return None here.
What do these functions do? select_unassigned_variable
is just going to choose a variable not yet assigned.
So it's going to loop over all the variables.
And if it's not already assigned, we'll go ahead and just return that variable.
And what does the consistent function do?
Well, the consistent function goes through all the constraints.
And if we have a situation where we've assigned
both of those values to variables but they are the same,
well, then that is a violation of the constraint,
in which case will return False.
But if nothing is inconsistent, then the assignment
is consistent and will return True.
And then all the program does is it calls
backtrack on an empty assignment, an empty dictionary that
has no variable assigned and no values yet, save that inside a solution,
and then print out that solution.
So by running this now, I can run python schedule0.py.
And what I get as a result of that is an assignment
of all these variables to values.
And it turns out we assign A to Monday, as we would expect, B to Tuesday,
C to Wednesday, exactly the same type of thing
we were talking about before, an assignment of each of these variables
to values that doesn't violate any constraints.
And I had to do a fair amount of work in order to implement this idea myself.
I had to write the backtrack function that
went ahead and went through this process of recursively
trying to do this backtracking search.
But it turns out the constraint satisfaction problems
are so popular that there exist many libraries that
already implement this type of idea.
Again, as with before, `the specific library is not as important as the fact that libraries do exist`.
This is just one example of a Python constraint library
where now, rather than having to do all the work from scratch
inside of `schedule1.py` (1:28:05), I'm just taking advantage of a library that implements
a lot of these ideas already.
So here, I create a new problem, add variables
to it with particular domains.
I add a whole bunch of these individual constraints
where I call addConstraint and pass in a function describing
what the constraint is.
And the constraint basically says, it's a function that takes two variables,
x and y, and makes sure that x is not equal to y,
enforcing the idea that these two classes cannot have exams on the same
day.
And then for any constraint satisfaction problem,
I can call getSolutions to get all the solutions to that problem
and then, for each of those solutions, print out
what that solution happens to be.
And if I run python schedule.py, I now see
there are actually a number of different solutions
that can be used to solve the problem.
There are, in fact, six different solutions,
assignments of variables to values that will give me
a satisfactory answer to this constraint satisfaction problem.
So this then was an implementation of a very basic backtracking search
method where, really, we just went through each of the variables,
picked one that wasn't assigned, tried the possible values the variable could
take on.
And then if it was-- if it worked, if it didn't violate any constraints,
then we kept trying other variables.
And if ever we hit a dead end, we had to backtrack.
But ultimately, we might be able to be a little bit more intelligent about how
we do this in order to improve the efficiency of how
we solve these sorts of problems.
And one thing we might imagine trying to do
is going back to this idea of `inference` (1:29:33), using
the knowledge we know to be able to draw conclusions
in order to make the rest of the problem-solving process a little bit
easier.
And let's now go back to where we got stuck in this problem the first time.
When we were solving this constraint satisfaction problem, we dealt with B,
and then we went on to D. And we went ahead and just assigned D to Monday
because that seemed to work with the assignment so far.
It didn't violate any constraints.
But it turned out that, later on, that choice turned out to be a bad one,
that that choice wasn't consistent with the rest of the values
that we could take on here.
And the question is, is there anything we
could do to avoid getting into a situation like this,
avoid trying to go down a path that's ultimately not
going to lead anywhere by taking advantage of knowledge
that we have initially?
And it turns out we do have that kind of knowledge.
We can look at just the structure of this graph so far.
And we can say that, right now, C's domain, for example,
contains values Monday, Tuesday, and Wednesday.
And based on those values, we can say that this graph is not arc-consistent.
Recall that arc consistency is all about making
sure that for every possible value for a particular node
that there is some other value that we are able to choose.
And as we can see here, Monday and Tuesday are not going to be possible
values that we can choose for C. They're not going to be consistent with a node
like B, for example, because B is equal to Tuesday,
which means that C cannot be Tuesday.
And because A is equal to Monday, C also cannot be Monday.
So using that information by making C arc-consistent with A and B,
we could remove Monday and Tuesday from C's domain
and just leave C with Wednesday, for example.
And if we continued to try and enforce arc consistency,
we'd see there are some other conclusions we can draw as well.
We see that B's only option is Tuesday, and C's only option is Wednesday.
And so if we want to make E arc-consistent,
well, E can't be Tuesday because that wouldn't be arc-consistent with B.
And E can't be Wednesday because that wouldn't be arc-consistent with C.
So we can go ahead and say E, and just set that equal to Monday, for example.
And then we can begin to do this process again and again,
that in order to make D arc-consistent with B and E, then D would have to be
Wednesday.
That's the only possible option.
And likewise, we can make the same judgments for F and G as well.
And it turns out that without having to do any additional search, just
by enforcing arc consistency, we were able to actually figure out
what the assignment of all the variables should
be without needing to backtrack at all.
And the way we did that is by interleaving the search
process and the inference step by this step of trying
to enforce arc consistency.

#### maintaining arc-consistency (1:32:14)

    - algorithm for enforcing arc-consistency every time we make a new assignment


And the algorithm to do this is often called just the "maintaining
arc-consistency algorithm," which just enforces arc consistency every time
we make a new assignment of a value to an existing variable.
So sometimes we can enforce arc consistency
using that AC-3 algorithm at the very beginning of the problem
before we even begin searching in order to limit the domain of the variables
in order to make it easier to search.
But we can also take advantage of the interleaving of enforcing
arc consistency with search such that every time in the search process
when we make a new assignment, we go ahead
and enforce arc consistency as well to make sure
that we're just eliminating possible values from domains whenever possible.
And how do we do this?
Well, this is really equivalent to just every time
we make a new assignment to a variable X,
we'll go ahead and call our `AC-3 algorithm`,
this algorithm that enforces arc consistency on a constraint
satisfaction problem.
And we go ahead and call that starting it with a queue not of all of the arcs,
which we did originally, but just have all of the arcs
that we want to make arc-consistent with X, this thing
that we have just made an assignment to, so all
arcs Y, X where Y is a neighbor of X, something that shares
a constraint with X, for example.
And by maintaining our consistency in the backtracking search process,
we can ultimately make our search process a little bit more efficient.
And so this is the revised version of this backtrack function.
Same as before-- the changes here are highlighted in yellow--
every time we add a new variable equals value to our assignment,
we'll go ahead and run this inference procedure, which
might do a number of different things.
But one thing it could do is call the maintaining arc-consistency algorithm
to make sure we're able to enforce arc consistency on the problem.
And we might be able to draw new inferences as a result of that process,
get new guarantees of this variable needs to be equal to that value,
for example.
That might happen one time.
It might happen many times.
And so long as those inferences are not a failure,
as long as they don't lead to a situation
where there is no possible way to make forward progress, well, then
we can go ahead and add those inferences, those new knowledge,
that new pieces of knowledge I know about what variables
should be assigned to what values.
I can add those to the assignment in order to more quickly make forward
progress by taking advantage of information that I can just deduce,
`information I know based on the rest of the structure of the constraint satisfaction problem`.
And the only other change I'll need to make now
is if it turns out this value doesn't work, well, then down here,
I'll go ahead and need to remove not only variable equals value but also any
of those inferences that I made, remove that from the assignment as well.
And so here then we're often able to solve the problem by backtracking less
than we might originally have needed to just by taking advantage of the fact
that every time we make a new assignment of one variable
to one value, that might reduce the domains of other variables as well.
And we can use that information to begin to more quickly draw conclusions
in order to try and solve the problem more efficiently as well.
And it turns out there are `other heuristics`
we can use to try and improve the efficiency of our search process
as well.
And it really boils down to a couple of these functions that I've talked about,
but we haven't really talked about how they're working.
And one of them is this function here, `select unassigned variable`
where we're selecting some variable in the constraint satisfaction problem
that has not yet been assigned.
So far, I've sort of just been selecting variables at random,
just like picking one variable and one unassigned variable
in order to decide, all right, this is the variable
that we're going to assign next, and then going from there.
But it turns out that by being a little bit intelligent, by following
certain heuristics, we might be able to make the search process much more
efficient just by choosing very carefully which
variable we should explore next.
So some of those heuristics include the `Minimum Remaining Values`, or MRV
heuristic, which generally says that if I
have a choice between which variable I should select,
I should select the variable with the smallest domain,
the variable that has the fewest number of remaining values left,
with the idea being if there are only two remaining values left, well,
I may as well prune one of them very quickly in order to get to the other
because one of those two has got to be the solution if a solution does exist.
And sometimes, minimum remaining values might not give a conclusive result
if all the nodes have the same number of remaining values, for example.
And in that case, another heuristic that can be helpful to look at
is the `degree heuristic`.
The degree of a node is the number of nodes
that are attached to that node, the number of nodes that are constrained
by that particular node.
And if you imagine which variable should I choose,
should I choose a variable that has a high degree that
is connected to a lot of different things or a variable
with a low degree that is not connected to a lot of different things?
Well, it can often make sense to choose the variable that
has the highest degree, that is connected
to the most other nodes as the thing you would search first.
Why is that the case?
Well, it's because by choosing a variable with a high degree, that
is immediately going to constrain the rest of the variables more,
and it's more likely to be able to eliminate
large sections of the state-space that you
don't need to search through at all.
So what could this actually look like?
Let's go back to this search problem here.
`(1:37:20)`
In this particular case, I've made an assignment here.
I've made an assignment here.
And the question is, what should I look at next?
And according to the minimum remaining values heuristic, what I should choose
is the variable that has the fewest remaining possible values.
And in this case, that's this node here, node C
that only has one variable left in this domain, which, in this case,
is Wednesday, which is a variable reas-- very reasonable choice
of a next assignment to make because I know it's the only option, for example.
I know that the only possible option for C is Wednesday.
So I may as well make that assignment and then potentially explore
the rest of the space after that.
But `meanwhile, at the very start of the problem`
when I didn't have any knowledge of what nodes should have what values yet,
I still had to pick what node should be the first one that I try and assign
a value to.
And I arbitrarily just chose the one at the top, node A, originally.
But we can be more intelligent about that.
And we can look at this particular graph.
All of them have domains of the same size, domain of size 3,
so minimum remaining values doesn't really help us there.
But we might `notice that node E has the highest degree`.
It is connected to the most things.
And so perhaps it makes sense to begin our search,
rather than starting at node A at the very top, start
with the node with the highest degree, start by searching from node
E. Because from there, that's going to much more easily allow
us to enforce the constraints that are nearby,
eliminating large portions of the search space
that I might not need to search through.
And in fact, by starting with E, we can immediately
then assign other variables.
And following that, we can actually assign the rest of the variables
without needing to do any backtracking at all even if I'm not
using this inference procedure.
Just by starting with a node that has a high degree,
that is going to very quickly restrict the values
that other nodes can take on.
So that then `(1:39:07)` is how we can go about selecting
an unassigned variable in a particular order
rather than randomly picking a variable.
If we're a little bit intelligent about how we choose it,
we can make our search process much, much
more efficient by making sure we don't have
to search through portions of the search space that ultimately
aren't going to matter.
The other variable we haven't really talked about,
the other function here is this `domain values function`, this domain values
function that takes a variable and gives me back
a sequence of all of the values inside of that variable's domain.
The naive way to approach it is what we did before, which is just go in order,
go Monday, then Tuesday, then Wednesday.
But the problem is that going in that order
might not be the most efficient order to search in, that sometimes it
might be more efficient to choose values that are likely to be solutions first
and then go to other values.
Now, how do you assess whether a value is likelier to lead to a solution
or less likely to lead to a solution?
Well, one thing you can take a look at is how many
constraints get added, how many things get removed
from domains as you make this new assignment of a variable
to this particular value.
And the heuristic we can use here is the

##### least constraining value heuristic,

which is the idea that we should return variables in order
based on the number of choices that are ruled out for neighboring values.
And I want to start with the least constraining value, the value that
rules out the lea-- fewest possible options.
And the idea there is that if all I care about doing
is finding a solution, if I start with a value that rules out
a lot of other choices, I'm ruling out a lot of possibilities
that maybe is going to make it less likely that this particular choice
leads to a solution.
Whereas on the other hand, if I have a variable
and I start by choosing a value that doesn't rule out very much,
well, then I still have a lot of space where there might be a solution
that I could ultimately find.
And this might seem a little bit counterintuitive and a little bit
at odds with what we were talking about before where I said, when you're
picking a variable, you should pick the variable that is going to have
the fewest possible values remaining.
But here, I want to pick the value for the variable that
is the least constraining.
But the general idea is that when I am picking a variable,
I would like to prune large portions of the search space
by just choosing a variable that is going to allow me to quickly eliminate
possible options.
Whereas here, within a particular variable,
as I'm considering values that that variable could take on,
I would like to just find a solution.
And so what I want to do is ultimately choose
a value that still leaves open the possibility of me finding a solution
to be as likely as possible.
By not ruling out many options, I leave open the possibility
that I can still find a solution without needing to go back later and backtrack.
So an example of that might be, in this particular situation here,
if I am trying to choose a variable for-- a value for node C here,
that C is equal to either Tuesday or Wednesday.
We know it can't be Monday because it conflicts with this domain
here where we already know that A is Monday.
So C must be Tuesday or Wednesday.
And the question is, should I try Tuesday first,
or should I try Wednesday first?
And if I try Tuesday, what gets ruled out?
Well, one option gets ruled out here.
A second option gets ruled out here.
And a third option gets ruled out here.
So choosing Tuesday would rule out three possible options.
And what about choosing Wednesday?
Well, choosing Wednesday would rule out one option here,
and it would rule out one option there.
And so I have two choices.
I can choose Tuesday that rules out three options
or Wednesday that rules out two options.
And according to the least constraining value heuristic, what I should probably
do is go ahead and choose Wednesday, the one that rules out
the fewest number of possible options, leaving open
as many chances as possible for me to eventually find
the solution inside of the state-space.
And ultimately, if you continue this process,
we will find a solution, an assignment of variables
to values that allows us to give each of these exams--
each of these classes an exam date that doesn't conflict
with anyone that happens to be enrolled in two classes at the same time.
So the big takeaway now with all of this is
that there are a number of different ways we can formulate a problem.
The ways we've looked at today are we can formulate a problem
as a local search problem, a problem where we're looking at a current node
and moving to a neighbor based on whether that neighbor is
better or worse than the current node that we are looking at.
We looked at formulating problems as linear programs
where just by putting things in terms of equations and constraints,
we're able to solve problems a little bit more efficiently.
And we saw formulating a problem as a constraint satisfaction problem,
creating this graph of all of the constraints
that connect to variables that have some constraint between them,
and using that information to be able to figure out what the solution should be.
And so the takeaway of all of this now is
that if we have some problem in artificial intelligence
that we would like to use AI to be able to solve them,
whether that's trying to figure out where hospitals should be,
or trying to solve the traveling salesman problem,
and trying to optimize productions, and costs, and whatnot,
or trying to figure out how to satisfy certain constraints,
whether that's in a Sudoku puzzle, or whether that's in trying to figure out
how to schedule exams for a university, or any number of a wide variety
of types of problems, if we can formulate that problem as one
of these sorts of problems,
then we can use these known algorithms, these algorithms
for enforcing arc consistency and backtracking search,
these hill-climbing and simulated annealing algorithms,
these simplex algorithms and interior-point algorithms that
can be used to solve linear programs, that we
can use those techniques to begin to solve a whole wide variety of problems
all in this world of optimization inside of artificial intelligence.
This was an Introduction to Artificial Intelligence with Python for today.
We will see you next time.
