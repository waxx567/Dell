# Notes on Lecture 5: Language
[Lecture](https://video.cs50.io/QAZc9xsQNjQ?screen=ieuSvyhRv6o)
[Notes](https://cs50.harvard.edu/ai/2024/notes/6/)
[Slides](https://cdn.cs50.net/ai/2023/x/lectures/6/lecture6.pdf)

So far in the course, we needed to shape tasks and data such that an AI will be able to process them. Today, we will look at how an AI can be constructed to process human language.

Natural Language Processing spans all tasks where the AI gets human language as input. The following are a few examples of such tasks:

    automatic summarization, where the AI is given text as input and it produces a summary of the text as output.

    information extraction, where the AI is given a corpus of text and the AI extracts data as output.

    language identification, where the AI is given text and returns the language of the text as output.

    machine translation, where the AI is given a text in the origin language and it outputs the translation in the target language.

    named entity recognition, where the AI is given text and it extracts the names of the entities in the text (for example, names of companies).

    speech recognition, where the AI is given speech and it produces the same words in text.

    text classification, where the AI is given text and it needs to classify it as some type of text.

    word sense disambiguation, where the AI needs to choose the right meaning of a word that has multiple meanings (e.g. bank means both a financial institution and the ground on the sides of a river).

[MUSIC PLAYING] BRIAN YU: Welcome back, everybody, to our final class in an Introduction to Artificial Intelligence with Python. Now, so far in this class, we've been taking problems that we want to solve intelligently and framing them in ways that computers are going to be able to make sense of. We've been taking problems and framing them as search problems or constraint satisfaction problems or optimization problems, for example. In essence, we have been trying to communicate about problems in ways that our computer is going to be able to understand. 

Today, the goal is going to be to get computers to understand the way you and I communicate naturally, via our own natural languages. Languages like English. But natural language contains a lot of nuance and complexity that's going to make it challenging for computers to be able to understand. So we'll need to explore some new tools and some new techniques to allow computers to make sense of natural language. 

So what is it exactly that we're trying to get computers to do? Well, they all fall under this general heading of 
# natural language processing, 
getting computers to work with natural language. And these tasks include tasks like `automatic summarization`. Given a long text, can we train the computer to be able to come up with a shorter representation of it? 

`Information extraction`. Getting the computer to pull out relevant facts or details out of some text. `Machine translation`, like Google translate, translating some text from one language into another language. `Question answering`. If you've ever asked a question to your phone or had a conversation with an AI chatbot where you provide some text to the computer, the computer is able to understand that text and then generate some text in response. 

`Text classification`, where we provide some text to the computer and the computer assigns it a label, positive or negative, inbox or spam, for example. And there are several other kinds of tasks that all fall under this heading of natural language processing. 

But before we take a look at how the computer might try to solve these kinds of tasks, it might be useful for us to *think about language in general*. What are the kinds of challenges that we might need to deal with as we start to think about language and getting a computer to be able to understand it? So one part of language that we'll need to consider is the syntax of language. 

## Syntax 
is all about the structure of language. Language is composed of individual words, and those words are composed together in some kind of structured whole. And if our computer is going to be able to understand language, it's going to need to understand something about that structure. So let's take a couple of examples. 

Here, for instance, is a sentence. "Just before nine o'clock Sherlock Holmes stepped briskly into the room." That sentence is made up of words, and those words together form a structured whole. This is syntactically valid as a sentence. But we could take some of those same words, rearrange them, and come up with a sentence that is not syntactically valid. 

Here, for example, "Just before Sherlock Holmes nine o'clock stepped briskly the room" is still composed of valid words, but they're not in any kind of logical whole. This is not a syntactically well-formed sentence. Another interesting challenge, is that some sentences will have multiple possible valid structures. 

Here's a sentence, for example. "I saw the man on the mountain with a telescope." And here, this is a valid sentence, but it actually has two different possible structures that lend themselves to two different interpretations and two different meanings. 

Maybe I, the one doing the seeing and the one with the telescope, or maybe the man on the mountain is the one with the telescope. And so natural language is ambiguous. Sometimes the same sentence can be interpreted in multiple ways. And that's something that we'll need to think about, as well. 

`Syntax is sentence structure. As native speakers of some human language, we don’t struggle with producing grammatical sentences and flagging non-grammatical sentences as wrong. For example, the sentence “Just before nine o’clock Sherlock Holmes stepped briskly into the room” is grammatical, whereas the sentence “Just before Sherlock Holmes nine o’clock stepped briskly the room” is non-grammatical. Syntax can be grammatical and ambiguous at the same time, as in “I saw the man with the telescope.” Did I see (the man with the telescope) or did I see (the man), doing so by looking through the telescope? To be able to parse human speech and produce it, the AI needs to command syntax.`

And this lends itself to another problem within language that we'll need to think about, which is 
### semantics. 
While syntax is all about the structure of language, semantics is about the meaning of language. It's not enough for a computer just to know that a sentence is well-structured if it doesn't know what that sentence means. And so semantics is going to concern itself with the meaning of words and the meaning of sentences. 

So if we go back to that same sentence as before, "Just before nine o'clock Sherlock Holmes stepped briskly into the room." I could come up with another sentence. Say the sentence, "A few minutes before nine, Sherlock Holmes walked quickly into the room." 

And those are two different sentences, with some of the words the same and some of the words different, but the two sentences have essentially the same meaning. And so ideally, whatever model we build, we'll be able to understand that these two sentences while different, mean something very similar. 

Some syntactically well-formed sentences don't mean anything at all. A famous example from linguist, Noam Chomsky, is the sentence, "Colorless green ideas sleep furiously." This is a syntactically, structurally well-formed sentence. We've got adjectives modifying a noun, ideas, we've got a verb and an adverb in the correct positions. But when taken as a whole, the sentence doesn't really mean anything. 

`Semantics is the meaning of words or sentences. While the sentence “Just before nine o’clock Sherlock Holmes stepped briskly into the room” is syntactically different from “Sherlock Holmes stepped briskly into the room just before nine o’clock,” their content is effectively identical. Similarly, although the sentence “A few minutes before nine, Sherlock Holmes walked quickly into the room” uses different words from the previous sentences, it still carries a very similar meaning. Moreover, a sentence can be perfectly grammatical while being completely nonsensical, as in Chomsky’s example, “Colorless green ideas sleep furiously.” To be able to parse human speech and produce it, the AI needs to command semantics.`

And so if our computers are going to be able to work with natural language and perform tasks in natural language processing, these are some concerns we'll need to think about. We'll need to be thinking about syntax and we'll need to be thinking about semantics. *So, how could we go about trying to teach a computer how to understand the structure of natural language?* 

Well, one approach we might take is by starting by thinking about the rules of natural language. Our natural languages have rules. In English, for example, nouns tend to come before verbs. Nouns can be modified by adjectives, for example. And so if only we could `formalize those rules`, then we could give those rules to a computer, and the computer would be able to make sense of them and understand them. 

And so, let's try to do exactly that. We're going to try to define a formal grammar, where a formal grammar is some system of rules for generating sentences in a language. This is going to be a rule-based approach to natural language processing. We're going to give the computer some rules that we know about language, and have the computer use those rules to make sense of the structure of language. 

And there are a number of different types of formal grammars, each one of them has slightly different use cases. 
`Formal Grammar is a system of rules for generating sentences in a language. In Context-Free Grammar, the text is abstracted from its meaning to represent the structure of the sentence using formal grammar.`
But today, we're going to focus specifically on one kind of grammar known as a 
# context-free grammar. 
*So how does the context-free grammar work?* Well, here is a sentence that we might want a computer to generate. 

She saw the city. And we're going to call each of these words a `terminal symbol`. A terminal symbol, because once our computer has generated the word, there's nothing else for it to generate. Once it's generated the sentence, the computer is done. We're going to associate each of these terminal symbols with a `nonterminal symbol` that generates it. 

So here we've got N, which stands for noun, like she or city. We've got V as a nonterminal symbol, which stands for a verb. And then we have D, which stands for determiner. A determiner is a word like the or a or an in English, for example. So each of these nonterminal symbols can generate the terminal symbols that we ultimately care about generating. 

But how do we know, or *how does the computer know which nonterminal symbols are associated with which terminal symbols?* Well, to do that, we need some kind of rule. Here are some what we call rewriting rules, that have a nonterminal symbol on the left-hand side of an arrow, and on the right side is what that nonterminal symbol can be replaced with. 

So here, we're saying the nonterminal symbol N, again, which stands for noun, could be replaced by any of these options separated by vertical bars. N could be replaced by she or city or car or Harry. D for determiner, could be replaced by the, a, or an, and so forth. Each of these nonterminal symbols could be replaced by any of these words. 
`7:40`

We can also have nonterminal symbols that are replaced by other nonterminal symbols. Here's an interesting rule. NP arrow N bar D N. *NP -> N | D N* So what does that mean? Well, NP stands for a noun phrase. Sometimes when we have a noun phrase in a sentence, it's not just a single word, it could be multiple words. And so here, we're saying a noun phrase could be just a noun, or it could be a determiner followed by a noun. 

So we might have a noun phrase that's just a noun, like she. That's a noun phrase. Or we could have a noun phrase that's multiple words, something like the city. Also acts as a noun phrase, but in this case, it's composed of two words, a determiner, the, and a noun, city. 

We could do the same for verb phrases. A verb phrase, or VP, might be just a verb, or it might be a verb followed by a noun phrase. So we could have a verb phrase that's just a single word, like the word, walked, or we could have a verb phrase that is an entire phrase, something like saw the city, as an entire verb phrase. 
`8:43`

`A sentence, meanwhile, we might then define as a noun phrase followed by a verb phrase.` And so this would allow us to generate a sentence like, she saw the city, an entire sentence made up of a noun phrase, which is just the word she, and then a verb phrase, which is saw the city. Saw, which is a verb, and then, the city, which itself, is also a noun phrase. 

And so if we could give these rules to a computer, explaining to it what nonterminal symbols could be replaced by what other symbols, then a computer could take a sentence and begin to understand the structure of that sentence. 

And so let's take a look at an example of how we might do that. And to do that, we're going to use a python library called 
## NLTK, or the Natural Language Toolkit, 
which we'll see a couple of times today. It contains a lot of helpful features and functions that we can use for trying to deal with and process natural language. 

So here, we'll take a look at how we can use NLTK in order to parse a context-free grammar. So let's go ahead and open up `cfg0.py`, cfg standing for `context-free grammar`. And what you'll see in this file, is that I first import NLTK, the Natural Language Toolkit. 
`9:51`

And the first thing I do, is define a context-free grammar, saying that a sentence is a noun phrase followed by a verb phrase. I'm defining what a noun phrase is, defining what a verb phrase is. And then giving some examples of what I can do with these nonterminal symbols, D for determiner, N for noun, and V for verb. We're going to use NLTK to parse that grammar. 

Then we'll ask the user for some input in the form of a sentence, and split it into words. And then, we'll use this context-free grammar parser to try to parse that sentence and print out the resulting syntax tree. So let's take a look at an example. We'll go ahead and go into my cfg directory and we'll `run cfg0.py`. And here, I'm asked to type in a sentence. Let's say I type in, she walked. 

And when I do that, I see that she walked is a valid sentence, where she is a noun phrase, and walked is the corresponding verb phrase. I could try to do this with a more complex sentence, too. I could do something like, she saw the city. And here, we see that she is the noun phrase, and then saw the city, is the entire verb phrase that makes up this sentence. 
`11:02`

So that was a very simple grammar. Let's take a look at a slightly more complex grammar. Here is `cfg1.py`, where a sentence is still a noun phrase followed by a verb phrase, but I've added some other possible nonterminal symbols, too. I have *AP for adjective phrase*, and *PP for prepositional phrase*. 

And we specified that we could have an adjective phrase before a noun phrase, or a prepositional phrase after a noun, for example. So lots of additional ways that we might try to structure a sentence and interpret and parse one of those resulting sentences. So let's see that one in action. We'll go ahead and `run cfg1.py` with this new grammar. 

And we'll try a sentence like, she saw the wide street. Here, pythons NLTK is able to parse that sentence and identify that she saw the wide street has this particular structure, a sentence with a noun phrase and a verb phrase, where that verb phrase has a noun phrase that within it, contains an adjective. And so it's able to get some sense for what the structure of this language actually is. 
`12:06`

Let's try another example. Let's say, she saw the dog with the binoculars. And we'll try that sentence. And here, we get one possible syntax tree. She saw the dog with the binoculars. But notice that this sentence is actually a little bit `ambiguous` in our own natural language. Who has the binoculars? Is it she who has the binoculars, or the dog who has the binoculars? 

And NLTK is able to identify both possible structures for the sentence. In this case, the dog with the binoculars is an entire noun phrase. It's all underneath this NP here, so it's the dog that has the binoculars. But we also got an alternative parse tree, where the dog is just the noun phrase. And with the binoculars, is a prepositional phrase modifying saw. So she saw the dog, and she used the binoculars in order to see the dog, as well. 
`13:01`

So this allows us to get a sense for the structure of natural language, but it relies on us writing all of these rules. And it would take a lot of effort to write all of the rules for any possible sentence that someone might write or say in the English language. Language is complicated, and as a result, there are going to be some very complex rules. 

So what else might we try? We might try to take a statistical lens towards approaching this problem of natural language processing. If we were able to give the computer a lot of existing data of sentences written in the English language. What could we try to learn from that data? Well, it might be difficult to try and interpret long pieces of text all at once. 

So instead, what we might want to do, is break up that longer text into smaller pieces of information instead. In particular, we might try to create *n-grams* out of a longer sequence of text. `An n-gram is just some contiguous sequence of n items from a sample of text.` It might be n characters in a row, or n words in a row, for example. 

So let's take a passage from Sherlock Holmes and let's look for all of the *trigrams*. `A trigram is an n-gram where n is equal to three.` So in this case, we're looking for sequences of three words in a row. So the trigrams here would be phrases like, how often have. That's three words in a row. Often have I, is another trigram. Have I said. I said to. Said to you. To you that. These are all trigrams, sequences of three words that appear in sequence. 
`14:25`

And if we could give the computer a large corpus of text and have it pull out all of the trigrams in this case, it could get a sense for what sequences of three words tend to appear next to each other in our own natural language. And as a result, get some sense for what the structure of the language actually is. So let's take a look at an *example* of that. How can we use NLTK to try to get access to information about n-grams. 

So here we're going to open up `ngrams.py`. And this is a python program that's going to load a corpus of data, just some text files, into our computer's memory. And then we're going to use NLTK's n-gram's function, which is going to go through the corpus of text, pulling out all of the n-grams for a particular value of n. And then by using python's counter class, we're going to figure out what are the most common n-grams inside of this entire corpus of text. 

And we're going to need a dataset in order to do this, and I've prepared a dataset of some of the stories of Sherlock Holmes. So it's just a bunch of text files, a lot of words for it to analyze. And as a result, we'll get a sense for what sequences of two words or three words tend to be most common in natural language. 
`15:41`

So let's give this a try. We'll go into my n-grams directory and we'll `run ngrams.py`. We'll try an n value of two. So we're looking for sequences of two words in a row. And we'll use our corpus of stories from Sherlock Holmes. And when we run this program, we get a list of the most common n-grams where n is equal to two, otherwise known as a *bigram*. 

`An n-gram is a sequence of n items from a sample of text. In a character n-gram, the items are characters, and in a word n-gram the items are words. A unigram, bigram, and trigram are sequences of one, two, and three items.`

So the most common one is, of the. That's a sequence of two words that appears quite frequently in natural language. Then, in the, and, it was. These are all common sequences of two words that appear in a row. Let's instead now try running n-grams with n equal to three. 

Let's get all of the trigrams and see what we get. And now we see the most common trigrams are, it was a, one of the, I think that. These are all sequences of three words that appear quite frequently. And we were able to do this, essentially via a process known as tokenization. 
### Tokenization 
is the process of splitting a sequence of characters into pieces. In this case, we're splitting a long sequence of text into individual words, and then looking at sequences of those words to get a sense for the structure of natural language. 
`16:48`

`Tokenization is the task of splitting a sequence of characters into pieces (tokens). Tokens can be words as well as sentences, in which case the task is called word tokenization or sentence tokenization. We need tokenization to be able to look at n-grams, since those rely on sequences of tokens. We start by splitting the text into words based on the space character. While this is a good start, this method is imperfect because we end up with words with punctuation, such as “remains,”. So, for example, we can remove punctuation. However, then we face additional challenges, such as words with apostrophes (e.g. “o’clock”) and hyphens (e.g. “pearl-grey). Additionally, some punctuation is important for sentence structure, like periods. However, we need to be able to tell apart between a period at the end of the word “Mr.” and a period in the end of the sentence. Dealing with these questions is the process of tokenization. In the end, once we have our tokens, we can start looking at n-grams.`

So once we've done this, once we've done the tokenization, once we've built up our corpus of n-grams, what can we do with that information? Well, the one thing that we might try, is we could build a 
#### Markov chain, 
which you might recall from when we talked about probability. Recall that a Markov chain is some sequence of values where we can predict one value based on the values that came before it.

And as a result, if we know all of the common n-grams in the English language, what words tend to be associated with what other words in sequence, we can use that to predict what word might come next in a sequence of words. And so we could build a Markov chain for language in order to try to generate natural language that follows the same statistical patterns as some input data. 
`17:31`

So let's take a look at that and build a Markov chain for natural language. And as input, I'm going to use the works of William Shakespeare. So here, I have a file, `shakespeare.txt`, which is just a bunch of the works of William Shakespeare. It's a long text file, so plenty of data to analyze. And here in `generator.py`, I'm using a third-party python library in order to do this analysis. 

We're going to read in the sample of text, and then we're going to train a Markov model based on that text. And then we're going to have the Markov chain generate some sentences. We're going to generate a sentence that doesn't appear in the original text, but that follows the same statistical patterns, that's generating it based on the n-grams, trying to predict what word is likely to come next that we would expect based on those statistical patterns. 
`18:21`

So we'll go ahead and go into our Markov directory, `run this generator` with the works of William Shakespeare as input. And what we're going to get, are five new sentences, where these sentences are not necessarily sentences from the original input text itself, but just that follow the same statistical patterns. It's predicting what word is likely to come next, based on the input data that we've seen and the types of words that tend to appear in sequence there, too. And so we're able to generate these sentences. 

`As discussed in previous lectures, Markov models consist of nodes, the value of each of which has a probability distribution based on a finite number of previous nodes. Markov models can be used to generate text. To do so, we train the model on a text, and then establish probabilities for every n-th token in an n-gram based on the n words preceding it. For example, using trigrams, after the Markov model has two words, it can choose a third one from a probability distribution based on the first two. Then, it can choose a fourth word from a probability distribution based on the second and third words. To see an implementation of such a model using nltk, refer to generator.py in the source code, where our model learns to generate Shakespeare-sounding sentences. Eventually, using Markov models, we are able to generate text that is often grammatical and sounding superficially similar to human language output. However, these sentences lack actual meaning and purpose.`

Of course, so far, there's no guarantee that any of the sentences that are generated actually mean anything or make any sense. They just happen to follow the statistical patterns that our computer is already aware of. So we'll return to this issue of how to generate text in perhaps a more accurate or more meaningful way a little bit later. 

So, let's now turn our attention to a slightly different problem, and that's the problem of text classification. 
##### Text classification 
is the problem where we have some text, and we want to put that text into some kind of category. We want to apply some sort of label to that text. And this kind of problem shows up in a wide variety of places. 
`19:26`

A common place might be your email inbox, for example. You get an email and you want your computer to be able to identify whether the email belongs in your inbox, or whether it should be filtered out into spam. So we need to classify the text. Is it a good email or is it spam? Another common use case is `sentiment analysis`. We might want to know whether the sentiment of some text is positive or negative. And so how might we do that? 

This comes up in situations like product reviews, where we might have a bunch of reviews for a product on some website. "My grandson loved it! So much fun." "Product broke after a few days." "One of the best games I've played in a long time." And "Kind of cheap and flimsy, not worth it." Here's some example sentences that you might see on a product review website. 

And you and I could pretty easily look at this list of product reviews and decide which ones are positive and which ones are negative. We might say the first one and the third one, those seem like positive sentiment messages, but the second one and the fourth one seem like negative sentiment messages. *But how did we know that?* And how could we train a computer to be able to figure that out, as well? 
`20:27`

Well, you might have clued your eye in on particular key words, where those particular words tend to mean something positive or negative. So you might have identified words like loved, and fun, and best, tend to be associated with positive messages. And words like broke, and cheap, and flimsy tend to be associated with negative messages. 

So if only we could train a computer to be able to learn what words tend to be associated with positive versus negative messages, then maybe we could train a computer to do this kind of sentiment analysis, as well. So we're going to try to do just that. We're going to use a model known as the `bag-of-words model`, which is a model that represents text as just an unordered collection of words. 

For the purpose of this model, we're not going to worry about the sequence and the ordering of the words, which word came first, second, or third, we're just going to treat the text as a collection of words in no particular order. And we're losing information there, right? The order of words is important, and we'll come back to that a little bit later. But for now, to simplify our model, it'll help us tremendously just to think about text as some unordered collection of words. 
`21:31`

`Bag-of-words is a model that represents text as an unordered collection of words. This model ignores syntax and considers only the meanings of the words in the sentence. This approach is helpful in some classification tasks, such as sentiment analysis (another classification task would be distinguishing regular email from spam email). Sentiment analysis can be used, for instance, in product reviews, categorizing reviews as positive or negative.`

And in particular, we're going to use the bag-of-words model to build something known as a 
# Naive Bayes classifier. 
So what is a Naive Bayes classifier? Well, it's a tool that's going to allow us to classify text based on Bayes rule. Again, which you might remember from when we talked about probability, Bayes rule says that the probability of b given a, is equal to the probability of a given b multiplied by the probability of b divided by the probability of a. 

`Naive Bayes is a technique that’s can be used in sentiment analysis with the bag-of-words model. In sentiment analysis, we are asking “What is the probability that the sentence is positive/negative given the words in the sentence?”`

So how are we going to use this rule to be able to analyze text? Well, what are we interested in? We're interested in the probability that a message has a positive sentiment and the probability that a message has a negative sentiment, which I'm here for simplicity, going to represent just with these emoji, happy face and frown face, as positive and negative sentiment. 

And so if I had a review, something like, my grandson loved it, then what I'm interested in, is not just the probability that a message has positive sentiment, but the conditional probability that a message has positive sentiment given that this is the message, my grandson loved it. *But how do I go about calculating this value, the probability that the message is positive given that the review is this sequence of words?*
`22:41` 

Well, here's where the bag-of-words model comes in. Rather than treat this review as a string of a sequence of words in order, we're just going to treat it as an unordered collection of words. We're going to try to calculate the probability that the review is positive, given that all of these words, my grandson loved it, are in the review in no particular order. Just this unordered collection of words. 

And this is a conditional probability, which we can then apply Bayes rule to try to make sense of. So according to Bayes rule, this conditional probability is equal to what? It's equal to the probability that all of these four words are in the review, given that the review is positive multiplied by the probability that the review is positive divided by the probability that all of these words happen to be in the review. 
`23:29`

So this is the value now that we're going to try to calculate. Now, one thing you might notice, is that the denominator here, the probability that all of these words appear in the review, doesn't actually depend on whether or not we're looking at the positive sentiment or negative sentiment case. 

So we can actually get rid of this denominator. We don't need to calculate it. We can just say that this probability is proportional to the numerator. And then at the end, we're going to need to normalize the probability distribution to make sure that all of the values sum up to the value one. 

So now, how do we calculate this value? Well, this is the probability of all of these words given positive times probability of positive. And that, by the definition of joint probability, is just one big joint probability. The probability that all of these things are the case. That it's a positive review, and that all four of these words are in the review.
`24:21` 

But still, it's not entirely obvious how we calculate that value. And here is where we need to make one more assumption. And `this is where the Naive part of Naive Bayes comes in`. We're going to make the assumption that all of the words are independent of each other. And by that, I mean that if the word, grandson, is in the review, that doesn't change the probability that the word, loved, is in the review or that the word it is in the review, for example. 

And in practice, this assumption might not be true. It's almost certainly the case that the probability of words do depend on each other. But it's going to simplify our analysis, and still give us reasonably good results, just to assume that the words are independent of each other and they only depend on whether it's positive or negative. 

You might, for example, expect the word, loved, to appear more often in a positive review than in a negative review. So, what does that mean? Well, if we make this assumption, then we can say that this value, the probability we're interested in, is not directly proportional to, but it's `naively proportional` to this value. 
`25:21`

The probability that the review is positive times the probability that my is in the review, given that it's positive, times the probability that grandson is in the review, given that it's positive, and so on for the other two words that happen to be in this review. And now this value, which looks a little more complex, is actually a value that we can calculate pretty easily. 

So how are we going to estimate the probability that the review is positive? Well, if we have some training data, some example data of example reviews where each one has already been labeled as positive or negative, then `we can estimate the probability that a review is positive just by counting the number of positive samples and dividing by the total number of samples that we have in our training data`. 

And `for the conditional probabilities, the probability of loved, given that it's positive, well, that's going to be the number of positive samples with loved in it divided by the total number of positive samples`. So let's take a look at an actual example to see how we could try to calculate these values. Here, I've put together some sample data. The way to interpret the sample data, is that based on the training data, 49% of the reviews are positive, 51% are negative. 
`26:28`

And then over here in this table, we have some conditional probabilities. We have if the review is positive, then there's a 30% chance that my appears in it. And if the review is negative, there's a 20% chance that my appears in it. And based on our training data among the positive reviews, 1% of them contain the word grandson. And among the negative reviews, 2% contain the word grandson. 

So, using this data, let's try to calculate this value, the value we're interested in. And to do that, we'll need to multiply all of these values together. The probability of positive, and then all of these positive conditional probabilities. And when we do that, we get some value. And then we can do the same thing for the negative case. We're going to do the same thing. Take the probability that it's negative, multiply it by all of these conditional probabilities, and we're going to get some other value. 
`27:19`

And now these values don't sum to one. They're not a probability distribution yet. But I can `normalize` them and get some values, and that tells me that we're going to predict that my grandson loved it. We think there's a 68% chance. Probability is 0.68 that that is a positive sentiment review. And 0.32 probability that it's a negative review. 

So, *what problems might we run into here?* What could potentially go wrong when doing this kind of analysis in order to analyze whether text has a positive or negative sentiment? Well, a couple of problems might arise. One problem might be, what if the word grandson never appears for any of the positive reviews? 

If that were the case, then when we try to calculate the value, the probability that we think the review is positive, we're going to multiply all these values together and we're just going to get 0 for the positive case. Because we're going to ultimately multiply by that 0 value. And so we're going to say that we think there is no chance that the review is positive, because it contains the word grandson. And in our training data, we've never seen the word grandson appear in a positive sentiment message before. 
`28:25`

And *that's probably not the right analysis*, because in cases of rare words, it might be the case that in nowhere in our training data did we ever see the word grandson appear in a message that has positive sentiment. So, what can we do to solve this problem? Well, one thing we'll often do, is some kind of `additive smoothing`, where we add some value alpha to each value in our distribution just to smooth out the data a little bit. 

And a common form of this is 
## Laplace smoothing, 
`adding 1 to each value in our distribution: pretending we've seen each value one more time than we actually have`
where we add 1 to each value in our distribution. In essence, we pretend we've seen each value one more time than we actually have. If we've never seen the word grandson for a positive review, we pretend we've seen it once. If we've seen it once, we pretend we've seen it twice, just *to avoid the possibility that we might multiply by 0, and as a result, get some results we don't want in our analysis*. 

So let's see what this looks like in practice. Let's try to do some Naive Bayes classification in order to classify text as either positive or negative. We'll take a look at `sentiment.py`. And what this is going to do, is load some sample data into memory, some examples of positive reviews and negative reviews. And then we're going to train a Naive Bayes classifier on all of this training data. 

Training data that includes all of the words we see in positive reviews and all of the words we see in negative reviews. And then we're going to try to classify some input. And so we're going to do this based on a corpus of data. I have some example positive reviews. Here are some positive reviews. "It was great! So much fun," for example. And then some negative reviews. "Not worth it." "Kind of cheap." These are some examples of negative reviews. 

So now, let's try to run this classifier and see how it would classify particular text as either positive or negative. We'll go ahead and run our sentiment analysis on this corpus. And we need to provide it with a review. So I'll say something like, "I enjoyed it." And we see that the classifier says there's about a 0.92 probability that we think that this particular review is positive. 

Let's try something negative. We'll try "kind of overpriced." And we see that there is a 0.96 probability now that we think that this particular review is negative. And so our Naive Bayes classifier has learned what kinds of words tend to appear in positive reviews and what kinds of words tend to appear in negative reviews. And as a result of that, we've been able to design a classifier that can predict whether a particular review is positive or negative. 
`30:53`

And so this definitely is a useful tool that we can use to try and make some predictions. But we had to make some assumptions in order to get there. *So what if we want to now try to build some more sophisticated models, use some tools from machine learning to try and take better advantage of language data, to be able to draw more accurate conclusions and solve new kinds of tasks and new kinds of problems?* 

Well, we've seen a couple of times now, that when we want to take some data and take some input, put it in a way that the computer is going to be able to make sense of, it can be helpful to take that data and turn it into numbers ultimately. And so what we might want to try to do, is come up with some `word representation`, some way to take a word and translate its meaning into numbers. 

### Word Representation

    We want to represent word meanings in our AI. As we’ve seen before, it is convenient to provide input to the AI in the form of numbers. One way to go about this is by using One-Hot Representation, where each word is represented with a vector that consists of as many values as we have words. Except for a single value in the vector that is equal to 1, all other values are equal to 0. How we can differentiate words is by which of the values is 1, ending up with a unique vector per word.

Because, for example, if we wanted to use a neural network to be able to process language, give our language to a neural network and have it make some predictions or perform some analysis there, a neural network takes as input and produces as output a `vector of values`, a vector of numbers. And so what we might want to do, is take our data and somehow take words and convert them into some kind of numeric representation.
`31:55` 

So, how might we do that? *How might we take words and turn them into numbers?* Let's take a look at an example. Here's a sentence, "He wrote a book." And let's say I wanted to take each of those words and turn it into a vector of values. 

Here's one way I might do that. We'll say he is going to be a vector that has a 1 in the first position, and the rest of the values are 0. Wrote will have a 1 in the second position, and the rest of the values are 0. A has a 1 in the third position with the rest of the values 0. And book has a 1 in the fourth position, with the rest of the values 0. 

So each of these words now has a distinct vector representation. And this is what we often call a *one-hot representation*,
`representation of meaning as a vector with a single 1, and with other values as 0`
 a representation of the meaning of a word as a vector with a single 1 and all of the rest of the values are 0. And so when doing this, we now have a numeric representation for every word, and we could pass in those vector representations into a neural network or other models that require some kind of numeric data as input.
`32:54`

But this `one-hot representation actually has a couple of problems, and it's not ideal for a few reasons`. One reason is, here, we're just looking at four words. But if you imagine a vocabulary of thousands of words or more, these vectors are going to get quite long in order to have a distinct vector for every possible word in our vocabulary. 

And as a result of that, these `longer vectors are going to be more difficult to deal with, more difficult to train` and so forth, and so that might be a problem. Another problem is a little bit more subtle. If we want to represent a word as a vector, and in particular, the meaning of a word as a vector, then ideally, it should be the case that *words that have similar meanings should also have similar vector representations, so that they're close to each other together inside a vector space*.
`33:41` 

But that's not really going to be the case with these one-hot representations, because if we take some similar words, say the word wrote and the word authored, which mean similar things, they have entirely different vector representations. Likewise book and novel. Those two words mean somewhat similar things, but they have entirely different vector representations, because they each have a 1 in some different position. And so that's not ideal either. 

So what we might be interested in instead, is some kind of *distributed representation*.
`representation of meaning distributed across multiple values.`
A distributed representation is the representation of the meaning of a word distributed across multiple values, instead of just being one-hot with a 1 in 1 position. Here is what a distributed representation of words might be. Each word is associated with some vector of values, with the meaning distributed across multiple values, ideally in such a way, that similar words have a similar vector representation.
`34:36` 

But *how are we going to come up with those values? Where do those values come from? How can we define the meaning of a word in this distributed sequence of numbers?* Well, to do that, we're going to draw inspiration from a quote from British linguist JR Firth, who said, *"You shall know a word by the company it keeps."* 

In other words, we're going to define the meaning of a word based on the words that appear around it, the context words around it. Take for example, this context. For blank he ate. You might wonder, what words could reasonably fill in that blank. Well, it might be words like breakfast, or lunch, or dinner. All of those could reasonably fill in that blank. 

And so what we're going to say, is because does the words breakfast and lunch and dinner appear in a similar context, that they must have a similar meaning. And that's something our computer could understand and try to learn. A computer could look at a big corpus of text, look at what words tend to appear in similar contexts to each other, and use that to identify which words have a similar meaning. And should therefore, appear close to each other inside a vector space. 
`35:39`

And so one common model for doing this is known as the `word2vec model`. It's a model for generating word vectors, a vector representation for every word by looking at data and looking at the context in which a word appears. The idea is going to be this.

#### word2vec
`word2vec is an algorithm for generating distributed representations of words. It does so by Skip-Gram Architecture, which is a neural network architecture for predicting context given a target word. In this architecture, the neural network has an input unit for every target word. A smaller, single hidden layer (e.g. 50 or 100 units, though this number is flexible) will generate values that represent the distributed representations of words. Every unit in this hidden layer is connected to every unit in the input layer. The output layer will generate words that are likely to appear in a similar context as the target words. Similar to what we saw in last lecture, this network needs to be trained with a training dataset using the backpropagation algorithm.`

If you start out with all of the words just in some random position in space and train it on some training data, what the word2vec model will do, is start to learn what words appear in similar contexts. And it will move these vectors around in such a way that hopefully, words with similar meanings, breakfast, lunch, and dinner, book, memoir, novel, will hopefully appear to be near to each other as vectors, as well. 

So, let's now take a look at what word2vec might look like in practice when implemented in code. What I have here inside of `words.txt` is a pre-trained model where each of these words has some vector representation trained by word2vec. Each of these words has some sequence of values representing its meaning, hopefully in such a way, that similar words are represented by similar vectors. 
`36:42`

I also have this file, `vectors.py`, which is going to open up the words and form them into a dictionary. And we also define some useful functions, like distance, to get the distance between two word vectors. And closest words define which words are nearby in terms of having close vectors to each other. And so let's give this a try. 

We'll go ahead and open a python interpreter. And I'm going to import these vectors. 
`from vectors import *` 
And we might say, all right, what is the vector representation of the word book. 
`words["book"]` 
And we get this big long vector that represents the word book as a sequence of values. And this sequence of values by itself is not all that meaningful. But it is meaningful in the context of comparing it to other vectors for other words. 

So we could use this `distance function`, which is going to get us the distance between two word vectors. And we might say, what is the distance between the vector representation for the word book and the vector representation for the word novel. 
`distance(words["book"], words["novel"])` 
And we see that it's 0.34. You can kind of interpret 0 as being really close together, and 1 being very far apart. 
`37:50`

And so now, what is the distance between book and let's say, breakfast? 
`distance(words["book"], words["breakfast"])` 
Well, book and breakfast are more different from each other than book and novel are, so I would hopefully, expect the distance to be larger. And in fact, it is. 0.64 approximately. These two words are further away from each other. And what about now, the distance between let's say, lunch and breakfast?
`distance(words["lunch"], words["breakfast"])` 
Well, that's about 0.2. Those are even closer together. They have a meaning that is closer to each other. 

Another interesting thing we might do is calculate the closest words. We might say, what are the closest words according to word2vec to the word book, and let's say, let's get the 10 closest words. 
`closest_words(words["book"])[:10]`
What are the 10 closest vectors to the vector representation for the word book? And when we perform that analysis, we get this list of words. 
`38:40`

The closest one is book itself. But we also have books plural, and then essay, memoir, essays, novella, anthology, and so on. All of these words mean something similar to the word book, according to word2vec, at least, because they have a similar vector representation. So it seems like we've done a pretty good job of trying to capture this kind of vector representation of word meaning. 

One other interesting side effect of word2vec is that it's also able to capture something about the relationships between words, as well. Let's take a look at an example. Here, for instance, are two words, man and king. And these are each represented by word2vec as vectors. So what might happen if I subtracted one from the other, calculated the value king minus man? 

Well, that will be the vector that will take us from man to king, somehow represent this relationship between the vector representation of the word man, and the vector representation of the word king. And that's what this value, king minus man, represents. So what would happen if I took the vector representation of the word woman and added that same value, king minus man, to it? What would we get as the closest word to that, for example?
`39:54`

Well, we could try it. Let's go ahead and go back to our python interpreter and give this a try. I could say, what is the closest word to the vector representation of the word king minus the representation of the word man, plus the representation of the word woman?
`closest_word(words["king"] - words["man"] + words["woman"])`
And we see that the closest word is the word queen. We've somehow been able to capture the relationship between king and man, and then we apply it to the word woman, we get as the result, the word queen. 

So word2vec has been able to capture not just the words and how they're similar to each other, but also something about the relationships between words and how those words are connected to each other. So now that we have this vector representation of words, what can we now do with it? Now we can represent words as numbers, and so we might try to pass those words as input to say, a neural network. Neural networks, we've seen, are very powerful tools for identifying patterns and making predictions.
`40:49`

Recall that a neural network you can think of as all of these units. But really what the neural network is doing, is taking some input, passing it into the network, and then producing some output. And by providing the neural network with training data, we're able to update the weights inside of the network, so that the neural network can do a more accurate job of translating those inputs into those outputs. 

And now that we can represent words as numbers that could be the input or output, you could imagine passing a word in as input to a neural network and getting a word as output. And so when might that be useful? One common use for neural networks is in *machine translation*. When we want to translate text from one language into another. 

Say, translate English into French, by passing English into the neural network and getting some French output. You might imagine, for instance, that we could take the English word for lamp, pass it into the neural network, get the French word for lamp as output. But in practice, when we're translating text from one language to another, we're usually not just interested in translating a single word from one language to another, but a sequence. Say, a sentence or a paragraph of words. 
`41:55`

Here, for example, is another paragraph, again taken from Sherlock Holmes written in English, and what I might want to do, is take that entire sentence, pass it into the neural network, and get as output, a French translation of the same sentence. But recall that a neural network's input and output needs to be of some fixed size. And a sentence is not a fixed size, it's a variable. You might have shorter sentences and you might have longer sentences. 

So somehow, we need to solve the problem of translating a sequence into another sequence by means of a neural network. And that's going to be true not only for machine translation, but also for other problems, problems like question answering. If I want to pass as input a question, something like, what is the capital of Massachusetts, feed that as input into the neural network, I would hope that what I would get as output is a sentence like, the capital is Boston. Again, translating some sequence into some other sequence. 
`42:48`

And if you've ever had a conversation with an AI chatbot or have ever asked your phone a question, it needs to do something like this. It needs to understand the sequence of words that you, the human, provided as input, and then the computer needs to generate some sequence of words as output. So how can we do this? 

Well, one tool that we can use, is the `recurrent neural network`, which we took a look at last time, which is a way for us to provide a sequence of values to a neural network by running the neural network multiple times. And each time we run the neural network, what we're going to do, is we're going to keep track of some hidden state. And that hidden state is going to be passed from one run of the neural network to the next run of the neural network, keeping track of all of the relevant information. 

And so let's take a look at how we could apply that to something like this. And in particular, we're going to look at an architecture known as an *encoder decoder architecture*, where we're going to encode this question into some kind of hidden state, and then use a decoder to decode that hidden state into the output that we're interested in. 
`43:50`

So what's that going to look like? We'll start with the first word, the word what. That goes into our neural network. And it's going to produce some hidden state. This is some information about the word what that our neural network is going to need to keep track of. Then when the second word comes along, we're going to feed it into that same encoder neural network, but it's going to get as input that hidden state, as well. 

So we pass in the second word, we also get the information about the hidden state, and that's going to continue for the other words in the input. This is going to produce a new hidden state. And so then when we get to the third word, the, that goes into the encoder, it also gets access to the hidden state. 

And then it produces a new hidden state that gets passed in to the next run when we use the word capital. And the same thing is going to repeat for the other words that appear in the input. So of, Massachusetts, that produces one final piece of hidden state. 
`44:45`

Now somehow, we need to signal the fact that we're done. There's nothing left in the input. And we typically do this by passing some kind of special token, say an *end token*, into the neural network. And now the decoding process is going to start. We're going to generate the word, the. But in addition to generating the word, the, this decoder network is also going to generate some kind of hidden state. 

And so what happens the next time? Well, `to generate the next word, it might be helpful to know what the first word was`. So we might pass the first word, the, back into the decoder network. It's going to get as input this hidden state, and it's going to generate the next word, capital. And that's also going to generate some hidden state. And we'll repeat that, passing capital into the network to generate the third word, is, and then one more time, in order to get the fourth word, Boston. 
`45:36`

And at that point, we're done. But how do we know we're done? Usually we'll do this one more time. Pass Boston into the decoder network and get as output some end token to indicate that that is the end of our input. And so this then is how we could use a recurrent neural network to take some input, encode it into some hidden state, and then use that hidden state to decode it into the output we're interested in. 

To visualize it in a slightly different way, we have some input sequence. This is just some sequence of words. That input sequence goes into the encoder, which in this case, is a recurrent neural network generating these hidden states along the way, until we generate some final hidden state, at which point, we start the decoding process. 

Again, using a recurrent neural network. That's going to generate the output sequence, as well. So we've got the encoder, which is encoding the information about the input sequence into this hidden state. And then the decoder, which takes that hidden state and uses it in order to generate the output sequence. 
`46:35`

But there are some problems. And for many years, this was the state of the art. The recurrent neural network and variants on this approach were some of the best ways we knew in order to perform tasks in natural language processing. But there are some problems that we might want to try to deal with, and that have been dealt with over the years to try and improve upon this kind of model. 

And one problem you might notice happens in this encoder stage. We've taken this input sequence, the sequence of words, and encoded it all into this final piece of hidden state. And that final piece of hidden state needs to contain all of the information from the input sequence that we need in order to generate the output sequence. 

And while that's possible, it becomes increasingly difficult as the sequence gets larger and larger. For larger and larger input sequences, it's going to become more and more difficult to store all of the information we need about the input inside this single hidden state piece of context. That's a lot of information to pack into just a single value. 
`47:32`

It might be useful for us when generating output, to not just refer to this one value, but to all of the previous hidden values that have been generated by the encoder. And so that might be useful. But how could we do that? We've got a lot of different values. We need to combine them somehow. So you could imagine adding them together, taking the average of them, for example. But doing that would assume that all of these pieces of hidden state are equally important. 

But that's not necessarily true either. Some of these pieces of hidden state are going to be more important than others, depending on what word they most closely correspond to. This piece of hidden state very closely corresponds to the first word of the input sequence. This one very closely corresponds to the second word of the input sequence, for example. And some of those are going to be more important than others. 

To make matters more complicated, depending on which word of the output sequence we're generating, different input words might be more or less important. And so what we really want, is some way to decide for ourselves which of the input values are worth paying attention to at what point in time. And this is the key idea behind a mechanism known as Attention. 
# Attention 
is all about letting us decide which values are important to pay attention to when generating, in this case, the next word in our sequence. 
`48:50`

So let's take a look at an example of that. Here's a sentence. What is the capital of Massachusetts. Same sentence as before. And let's imagine that we were trying to answer that question by generating tokens of output. So what would the output look like? Well, it's going to look like something like the capital is. And let's say we're now trying to generate this last word here. What is that last word? How is the computer going to figure it out? 

Well, what it's going to need to do, is decide which values it's going to pay attention to. And so the Attention mechanism will allow us to calculate some Attention scores for each word, some value corresponding to each word, determining how relevant is it for us to pay attention to that word right now. 

And in this case, when generating the fourth word of the output sequence, the most important words to pay attention to might be capital and Massachusetts, for example, that those words are going to be particularly relevant. And there are a number of different mechanisms that have been used in order to calculate these attention scores. 
`49:52`

It could be something as simple as a dot product to see how similar two vectors are, or we could train an entire neural network to calculate these Attention scores. But the key idea, is that during the training process for our neural network, we're going to learn how to calculate these Attention scores. Our model is going to learn what is important to pay attention to in order to decide what the next word should be. 

So the result of all of this, calculating these Attention scores, is that we can calculate some value, some value for each input word, determining how important is it for us to pay attention to that particular value. And recall that each of these input words is also associated with one of these hidden state context vectors, capturing information about the sentence up to that point, but primarily focused on that word in particular. 

And so what we can now do, is if we have all of these vectors and we have values representing how important is it for us to pay attention to those particular vectors, is we can take a `weighted average`. We can take all of these vectors, multiply them by their Attention scores, and add them up to get some new vector value, which is going to represent the context from the input, but specifically paying attention to the words that we think are most important. 
`51:08`

And once we've done that, that context vector can be fed into our decoder in order to say that the word should be, in this case, Boston. So Attention is this very powerful tool that allows any word when we're trying to decode it, to decide which words from the input should we pay attention to in order to determine what's important for generating the next word of the output. 

And one of the first places this was really used, was in the field of machine translation. Here's an example of a diagram from the paper that introduced this idea `51:40`, which was focused on trying to translate English sentences into French sentences. So we have an input English sentence up along the top, and then along the left side, the output French equivalent of that same sentence. 

And what you see in all of these squares are the Attention scores visualized, where a lighter square indicates a higher Attention score. And what you'll notice, is that there's a strong correspondence between the French word and the equivalent English word. That the French word for agreement is really paying attention to the English word for agreement in order to decide what French word should be generated at that point in time. 

And sometimes you might pay attention to multiple words. If you look at the French word for economic, that's primarily paying attention to the English word for economic, but also paying attention to the English word for European, in this case, too. And so Attention scores are very easy to visualize to get a sense for what is our machine learning model really paying attention to. What information is it using in order to determine what's important and what's not in order to determine what the ultimate output token should be. 
`52:45`

And so when we combine the Attention mechanism with a recurrent neural network, we can get very powerful and useful results, where we're able to generate an output sequence by paying attention to the input sequence, too. But there are other problems with this approach of using a recurrent neural network, as well. In particular, notice that *every run of the neural network depends on the output of the previous step*. 

And that was important for getting a sense for the sequence of words and the ordering of those particular words. But we can't run this unit of the neural network until after we've calculated the hidden state from the run before it, from the previous input token. And what that means, is that it's very difficult to parallelize this process. 

That as the input sequence get longer and longer, we might want to use parallelism to try and speed up this process of training the neural network and making sense of all of this language data. But it's difficult to do that and it's slow to do that with a recurrent neural network, because all of it needs to be performed in sequence. And that's become an increasing challenge as we've started to get larger and larger language models.
`53:47`

The more language data that we have available to us to use to train our machine learning models, the more accurate it can be, the better representation of language it can have, the better understanding it can have, and the better results that we can see. And so we've seen this growth of large language models that are using larger and larger datasets, but as a result, they take longer and longer to train. 

And so this problem, that recurrent neural networks are not easy to parallelize, has become an increasing problem. And as a result of that, that was one of the main motivations for a different architecture for thinking about how to deal with natural language. And that's known as the 
## Transformer architecture. 

And this has been a significant milestone in the world of natural language processing for really increasing how well we can perform these kinds of natural language processing tasks, as well as how quickly we can train a machine learning model to be able to produce effective results. There are a number of different types of Transformers in terms of how they work, but what we're going to take a look at here, is the basic architecture for how one might work with a Transformer to get a sense for what's involved and what we're doing. 
`54:51`

So let's start with the model we were looking at before, specifically at this encoder part of our encoder decoder architecture, where we used a recurrent neural network to take this input sequence and capture all of this information about the hidden state and the information we need to know about that input sequence. 

Right now, it all needs to happen in this linear progression. But what the Transformer is going to allow us to do, is process each of the words independently in a way that's easy to parallelize. Rather than have each word wait for some other word, each word is going to go through this same neural network and produce some kind of encoded representation of that particular input word. And all of this is going to happen in parallel. 

Now it's happening for all of the words at once, but we're really just going to focus on what's happening for one word to make it clear. But know that whatever you're seeing happen for this one word, is going to happen for all of the other input words, too. So what's going on here? Well, we start with some input word. That input word goes into the neural network, and the output is hopefully, some encoded representation of the input word, the information we need to know about the input word that's going to be relevant to us as we're generating the output. 
`56:02`

And because we're doing this each word independently, it's easy to parallelize. We don't have to wait for the previous word before we run this word through the neural network. But what did we lose in this process by trying to parallelize this whole thing? Well, we've lost all notion of word ordering. The order of words is important. The sentence, Sherlock Holmes gave the book to Watson, has a different meaning than Watson gave the book to Sherlock Holmes. 

And so *we want to keep track of that information about word position*. In the recurrent neural network, that happened for us automatically, because we could run each word one at a time through the neural network, get the hidden state, pass it on to the next run of the neural network. But that's not the case here with the Transformer, where each word is being processed independent of all of the other ones. 

So what are we going to do to try to solve that problem? One thing we can do, is add some kind of positional encoding to the input word. The positional encoding is some vector that represents the position of the word in the sentence. This is the first word, the second word, the third word, and so forth. We're going to add that to the input word. 
`57:06`

And the result of that is going to be a vector that captures multiple pieces of information. It captures the input word itself, as well as where in the sentence it appears. The result of that, is we can pass the output of that addition, the addition of the input word and the positional encoding, into the neural network. 

That way the neural network knows the word and where it appears in the sentence, and can use both of those pieces of information to determine how best to represent the meaning of that word in the encoded representation at the end of it. 

In addition to what we have here, in addition to the positional encoding and this feed forward neural network, we're also going to add one additional component, which is going to be a *Self-Attention step*. This is going to be Attention where we're paying attention to the other input words. Because the meaning or interpretation of an input word might vary depending on the other words in the input, as well. 

And so we're going to allow each word in the input to decide what other words in the input it should pay attention to in order to decide on its encoded representation. And that's going to allow us to get a better encoded representation for each word, because words are defined by their context, by the words around them and how they're used in that particular context. 
`58:20`

This kind of Self-Attention is so valuable in fact, that oftentimes, the Transformer will use multiple different Self-Attention layers at the same time to allow for this model to be able to pay attention to multiple facets of the input at the same time. We call this *Multi-Headed Attention*, where each attention head can pay attention to something different. And as a result, this network can learn to pay attention to many different parts of the input for this input word all at the same time. 

`And in the spirit of deep learning, these two steps, this Multi-Headed Self-Attention layer, and this neural network layer, that itself can be repeated multiple times, too, in order to get a deeper representation, in order to learn deeper patterns within the input text, and ultimately, get a better representation of language, in order to get useful and coded representations of all of the input words.`

And so this is the process that a transformer might use in order to take an input word and get it as encoded representation. And the key idea, is to really rely on this Attention step in order to get information that's useful in order to determine how to encode that word. And that process is going to repeat for all of the input words that are in the input sequence. 
`59:33`

We're going to take all of the input words, encode them with some kind of positional encoding, feed those into these Self-Attention and feed forward neural networks in order to ultimately get these encoded representations of the words. That's the result of the encoder. We get all of these encoded representations that will be useful to us when it comes time then to try to decode all of this information into the output sequence we're interested in. 

And again, this might take place in the context of machine translation, where the output is going to be the same sentence in a different language. Or it might be an answer to a question, in the case of an AI chatbot, for example. And so *now let's take a look at how that decoder is going to work*. Ultimately, it's going to have a very similar structure. 

Any time we're trying to generate the next output word, we need to know what the previous output word is, as well as its positional encoding, where in the output sequence are we. And we're going to have these same steps. Self-Attention, because we might want an output word to be able to pay attention to other words in that same output, as well as a neural network. And that might itself repeat multiple times. 
`1:00:41`

But in this decoder, we're going to add one additional step. We're going to add an additional Attention step, where instead of Self-Attention, where the output word is going to pay attention to other output words, in this step, we're going to allow the output word to pay attention to the encoded representations. 

So recall that the encoder is taking all of the input words and transforming them into these encoded representations of all of the input words. But it's going to be important for us to be able to decide which of those encoded representations we want to pay attention to when generating any particular token in the output sequence. And that's what this additional Attention step is going to allow us to do. 

It's saying that every time we're generating a word of the output, we can pay attention to the other words in the output, because we might want to know, what are the words we've generated previously. And we want to pay attention to some of them to decide what word is going to be next in the sequence. But we also care about paying attention to the input words, too. 
`1:01:40`

And we want the ability to decide which of these encoded representations of the input words are going to be relevant in order for us to generate the next step. And so these two pieces combine together. We have this encoder that takes all of the input words and produces this encoded representation. And we have this decoder that is able to take the previous output word, pay attention to that encoded input, and then generate the next output word. 

And this is one of the possible architectures we could use for a transformer, with the key idea being these attention steps, that allow words to pay attention to each other. During the training process here, we can now much more easily parallelize this, because we don't have to wait for all of the words to happen in sequence. 

And we can learn how we should perform these attention steps. The model is able to learn what is important to pay attention to, what things do I need to pay attention to in order to be more accurate at predicting what the output word is. And this has proved to be a tremendously effective model for conversational AI agents, for building machine translation systems. 

And there have been many variants proposed on this model, too. Some transformers only use an encoder. Some only use a decoder. Some use some other combination of these different particular features. But the key ideas ultimately remain the same. This real focus on trying to pay attention to what is most important. 
`1:03:01`

And the world of natural language processing is fast-growing and fast-evolving. Year after year, we keep coming up with new models that allow us to do an even better job of performing these natural language-related tasks, all in the service of solving the tricky problem, which is our own natural language. 

We've seen how the syntax and semantics of our language is ambiguous and introduces all of these new challenges that we need to think about if we're going to be able to design AI agents that are able to work with language effectively. 

So as we think about where we've been in this class, all of the different types of artificial intelligence we've considered, we've looked at artificial intelligence in a wide variety of different forms now. 

We started by taking a look at search problems, where we looked at how AI can search for solutions, play games, and find the optimal decision to make. We talked about knowledge, how AI can represent information that it knows and use that information to generate new knowledge, as well. 

Then we looked at what AI can do when it's less certain, when it doesn't know things for sure, and we have to represent things in terms of probability. 

We then took a look at optimization problems. We saw how a lot of problems in AI can be boiled down to trying to maximize or minimize some function. And we looked at strategies that AI can use in order to do that kind of maximizing and minimizing. 

We then looked at the world of machine learning, learning from data in order to figure out some patterns and identify how to perform a task by looking at the training data that we have available to it. And one of the most powerful tools there was the neural network, the sequence of units whose weights can be trained in order to allow us to really effectively go from input to output and predict how to get there by learning these underlying patterns. 

And then today, we took a look at language itself, trying to understand how can we train the computer to be able to understand our natural language, to be able to understand syntax and semantics, make sense of and generate natural language, which introduces a number of interesting problems, too. And we've really just scratched the surface of artificial intelligence. 

There is so much interesting research and interesting new techniques and algorithms and ideas being introduced to try to solve these types of problems. So I hope you enjoyed this exploration into the world of artificial intelligence. A huge thanks to all of the course's teaching staff and production team for making the class possible. This was an introduction to Artificial Intelligence with Python. 