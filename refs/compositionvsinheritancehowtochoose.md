# Composition vs. Inheritance: How to Choose?

> In the Beginning...
...there was no inheritance and no composition, only code.
And the code was unwieldy, repetitive, blocky, unhappy, verbose, and tired.
Copy and Paste were the primary mechanisms of code reuse. Procedures and functions were rare, newfangled gadgets viewed with suspicion. Calling a procedure was expensive! Separating pieces of code from the main logic caused confusion!
It was a Dark Time.

### In the Beginning...

...there was no inheritance and no composition, only code.

And the code was unwieldy, repetitive, blocky, unhappy, verbose, and tired.

Copy and Paste were the primary mechanisms of code reuse. Procedures and functions were rare, newfangled gadgets viewed with suspicion. Calling a procedure was expensive! Separating pieces of code from the main logic caused confusion!

It was a Dark Time.

Then the light of object-oriented programming (OOP) shone upon the world… And the world pretty much ignored it for a few decades[1](#one). Until graphical user interfaces[2](#two), which turned out to really, really need OOP. When you click on a button in a window, what simpler way to generate appropriate responses than to send that button (or its surrogate) a Click message[3](#)?

After that, OOP took off. Numerous[4](#four) books have been written and countless5 articles have proliferated. So by now, everyone understands object-oriented programming in detail, right?

Sadly, the code (and the Internet) says no.

The biggest point of confusion and contention seems to be composition versus inheritance, often summarized in the mantra “[favor composition over inheritance](https://en.wikipedia.org/wiki/Composition_over_inheritance)”. Let’s talk about that.

### Mantras Considered Harmful

As a heuristic, ‘favor composition over inheritance’ is okay, however, I am [not a fan of mantras](http://programmers.stackexchange.com/a/65209/906). While they often contain a kernel of truth, it is far too easy for people to hear the slogan without understanding its source or context, and thus avoid thinking for themselves - and that never turns out well.

I am also not a fan of ridiculous clickbait headlines like “Inheritance is Evil”6, especially when the author attempts to back up such an outrageous claim by using inheritance inappropriately… and then blaming inheritance. Like a carpenter declaring that hammers are useless because they don’t drive screws well.

Let’s start with the basics.

### Definitions

Here is the definition of object-oriented programming that I will be using for the rest of the article: assume we have a ‘classic’ OOP language, i.e., one that supports classes with fields, methods, and single inheritance. No interfaces, no mixins, no aspects, no multiple inheritance, no delegates, no closures, no lambdas, nothing but the basics:

*   Class: a named concept in the domain space, with an optional superclass, defined as a set of fields and methods.
*   Field: a named property of some type, which may reference another object (see composition)
*   Method: a named function or procedure, with or without parameters, that implements some behavior for a class.
*   Inheritance: a class may inherit - use by default - the fields and methods of its superclass. Inheritance is transitive, so a class may inherit from another class which inherits from another class, and so on, up to a base class (typically Object, possibly implicit/absent). Subclasses may override some methods and/or fields to alter the default behavior.
*   Composition: when a Field’s type is a class, the field will hold a reference to another object, thus creating an association relationship between them. Without getting into the nuances of the difference between simple association, aggregation, and composition, let’s intuitively define composition as when the class uses another object to provide some or all of its functionality.
*   Encapsulation: by interacting with objects instead of directly with the implementation of methods and fields, we hide and protect the implementation of a class. If a consumer does not know anything about an object other than its public interface, then it cannot rely on any internal implementation details.

### Inheritance is Fundamental

Inheritance is _fundamental_ to object-oriented programming. A programming language may have objects and messages, but without inheritance it is not object-oriented (merely “object-based”, but still polymorphic).

### …and so is Composition

Composition is also fundamental to _every_ language. Even if the language does not support composition (rare these days!), humans still think in terms of parts and components. It would be impossible to break down complex problems into modular solutions without composition.

(Encapsulation is fundamental too, but we’re not going to talk about it much here.)

![](moz-extension://8ed96dbf-14c5-4459-977f-168da63f6d71/content/dam/thoughtworks/images/photography/inline-image/insights/blog/microservices/blg_inline_composition_vs_inheritance_how_choose.jpg)

### So What’s the Fuss About?

Composition and inheritance are both fundamental, so what’s the big deal?

The big deal is in thinking that one can replace the other, in all cases, or that one is better or worse than the other. Like everything else in software development, there are trade-offs to be made.

Composition is fairly easy to understand - we can see composition in everyday life: a chair has legs, a wall is composed of bricks and mortar, and so on. While the definition of inheritance is simple, it can become a complicated, tangled thing when used unwisely. Inheritance is more of an abstraction that we can only talk about, not touch directly. Though it is possible to mimic inheritance using composition in many situations, it is often unwieldy to do so. The purpose of composition is obvious: make wholes out of parts. The purpose of inheritance is a bit more complex because inheritance serves two purposes, semantics and mechanics.

### Inheritance Semantics

Inheritance captures semantics (meaning) in a classification hierarchy (a taxonomy), arranging concepts from generalized to specialized, grouping related concepts in subtrees, and so on. The semantics of a class are mostly captured in its interface, the set of messages to which it responds, but a portion of the semantics also resides in the set of messages that the class sends. When inheriting from a class, you are implicitly accepting responsibility for all of the messages that the superclass sends on your behalf, not just the messages that it can receive. This makes the subclass more tightly coupled to its superclass than it would be if it merely used an instance of the superclass as a component instead of inheriting from it. Note that even in classes that don’t “do” much, the name of the class imparts significant semantic information about the domain to the developer.

### Inheritance Mechanics

Inheritance captures mechanics by encoding the representation of the data (fields) and behavior (methods) of a class and making it available for reuse and augmentation in subclasses. Mechanically, the subclass will inherit the implementation of the superclass and thus also its interface.

The dual purpose of inheritance[7](#seven) in most current OOP languages is, I believe, the cause of most confusion. Many people think that “code reuse” is the primary purpose of inheritance, but that is not its only purpose. An overemphasis on reuse can lead to tragically flawed designs. Let’s look at a couple of examples.

### How to Misuse Inheritance - Example 1

Let’s start with a simple and extremely common example of misusing inheritance:

class Stack extends ArrayList {
    public void push(Object value) { … }
    public Object pop() { … }
}

This class will function as a Stack, but its interface is fatally bloated. The public interface of this class is not just push and pop, as one would expect from a class named Stack, it also includes get, set, add, remove, clear, and a bunch of other messages inherited from ArrayList that are inappropriate for a Stack.

You could override all of the unwanted methods, and perhaps adapt some useful ones (like clear), but that’s a lot of work to cover up a modeling mistake. Three modeling mistakes, actually, one semantic, one mechanical, one both:

1.  Semantically, the statement “a Stack is an ArrayList” is not true; Stack is [not a proper subtype](https://en.wikipedia.org/wiki/Liskov_substitution_principle) of ArrayList. A stack is supposed to enforce last-in-first-out, a constraint easily satisfied by the push/pop interface, but not enforced by ArrayList’s interface.
2.  Mechanically, inheriting from ArrayList violates encapsulation; using ArrayList to hold the stack’s object collection is an implementation choice that should be hidden from consumers.
3.  Finally, implementing a Stack by inheriting from ArrayList is a cross-domain relationship: ArrayList is a randomly-accessible Collection; Stack is a queuing concept, with specifically restricted (non-random) access[8](#eight). These are different modeling domains.

The last issue is important but slightly subtle, so let’s explore it with another example.

### How to Misuse Inheritance - Example 2

Creating a domain-concept class by inheriting from an implementation class is a common misuse of inheritance. For example, suppose we want to do something with a certain segment of our customers. The easy and obvious thing to do is to subclass ArrayList<Customer>, call it CustomerGroup, and start coding, right?

Wrong. That would be a cross-domain inheritance relationship, and those should be avoided:

1.  ArrayList<Customer> is a subclass of list already, a utility collection - an _implementation_ class.
2.  CustomerGroup is another subclass - a _domain_ class.
3.  **Domain classes should _use_ implementation classes, not inherit from them.**

The implementation space should be invisible at the domain level. When we are thinking about what our software does, we are operating at the domain level; we don’t want to be distracted by details about how it does things. If we are only focused upon “code reuse” via inheritance, we will fall into this trap repeatedly.

### Single Inheritance is not the Problem

Single inheritance is still the most common OOP model; single inheritance is necessarily implementation inheritance, which can lead to strong coupling between classes. The problem would seem to be that we have only one inheritance path to use to model both our mechanical and semantic needs. If you use it for one, you can't use it for the other. So doesn’t multiple inheritance solve this problem?

_No_. Inheritance relationships should not cross domain boundaries (implementation domain vs application domain). Making CustomerGroup inherit from ArrayList<Customer> but also from (say) DemographicSegment tangles the two subdomains, confusing the taxonomy.

The preferred (at least by me!) solution is to inherit from utility classes as much as necessary to implement your mechanical structures, then use these structures in domain classes via composition, not inheritance. Let me restate that:

> Unless you are creating an implementation class, you should not inherit from an implementation class. 

This is one of the most common beginner issues — because it’s so convenient! — and the reasons why it’s wrong are not often discussed in programming literature, so I’ll say it again: your application-domain classes should _use_ implementation classes, not be one. Keep these taxonomies/domains separated.

So when and how should we use inheritance?

### Using Inheritance Well

The most common - and beneficial - use of inheritance is for _differential programming_. We need a widget that is just like the existing Widget class, but with a few tweaks and enhancements. In this case, inherit away; it is appropriate because our subclass is still a widget, we want to reuse the entire interface and implementation from the superclass, and our changes are primarily _additive_. If you find that your subclass is removing things provided by the superclass, question inheriting from that superclass.

Inheritance is most useful for grouping related sets of concepts, identifying families of classes, and in general organizing the names and concepts that describe the domain. As we delve deeper into the implementation of a system, we may find that our original generalizations about the domain concepts, captured in our inheritance hierarchies, are beginning to shred. Don’t be afraid to disassemble inheritance hierarchies into sets of complementary cooperating interfaces and components when the code leads you in that direction[9](#nine).

### How to Decide: Composition or Inheritance?

When you have a situation where either composition or inheritance will work, consider splitting the design discussion in two:

1.  The representation/implementation of your domain concepts is one dimension
2.  The semantics of your domain concepts and their relationship to one another is a second dimension

In general, inheriting within one of these dimensions is fine. The problem becomes when we forget to separate the two dimensions, and start inheriting across inter-dimensional boundaries.

If you find that you are using a component to provide the vast majority of your functionality, creating forwarding methods on your class to call the component’s methods, exposing the component’s fields, etc., consider whether inheritance - for some or all of the desired behavior - might be more appropriate.

There is no substitute for object modeling and critical design thinking. But if you must have some guidelines, consider these -

Inheritance should only be used when:

1.  Both classes are in the same logical domain
2.  The subclass is a proper subtype of the superclass
3.  The superclass’s implementation is necessary or appropriate for the subclass
4.  The enhancements made by the subclass are primarily additive.

There are times when all of these things converge:

*   Higher-level domain modeling
*   Frameworks and framework extensions
*   Differential programming

If you’re not doing any of these things, you probably won’t need class inheritance very often. The “preference” for composition is not a matter of “better”, it’s a question of “most appropriate” for your needs, in a specific context.

Hopefully these guidelines will help you notice the difference. 

Happy coding!

### Appendix

Special thanks to the following Thoughtworkers for valuable contributions and comments: [Pete Hodgson](https://www.thoughtworks.com/profiles/pete-hodgson), Tim Brown, Scott Robinson, [Martin Fowler](https://www.thoughtworks.com/profiles/martin-fowler), Mindy Or, Sean Newham, [Sam Gibson](https://www.thoughtworks.com/profiles/sam-gibson), and Mahendra Kariya.

* * *

1. The first officially object-oriented language, SIMULA 67, was born in 1967. Object-oriented programming is 48 years old!  
2. systems and applications programmers adopted C++ in the mid 1980s, but OOP ubiquity had to [wait another decade](https://en.wikipedia.org/wiki/Object-oriented_programming#History).  
3. yes, I’m oversimplifying, ignoring listeners/event delegates/etc.; trying to keep this article short!  
4\. Amazon claims 24,777 books on the topic of object-oriented programming as of this writing  
5. Google search claims ~8M results for the exact phrase “object-oriented programming” as of this writing  
6\. Google search yields an estimated 37,600 results for the exact phrase “inheritance is evil” as of this writing  
7. Semantics (interfaces) and mechanics (representation) could be separated, at the cost of additional language complexity; see for example the [D language specification](https://en.wikipedia.org/wiki/D_%28data_language_specification%29) by C. J. Date and Hugh Darwen.  
8. Note with some sadness that Java’s Stack class inherits from Vector.  
9\. Designing classes for reuse via inheritance is beyond the scope of this article. Just keep in mind that consumers of instances and subclasses have different needs, both of which must be satisfied by your class design.


[Source](https://www.thoughtworks.com/insights/blog/composition-vs-inheritance-how-choose)