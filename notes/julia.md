---
author:
- Chris Rackauckas
- Vasken Dermardiros
categories: note
draft: false
lastmod: 2020-12-29 13:16:11-05:00
slug: julia
tags:
- julia
- programming
- physics-based
- model
- reference
- reinforcement-learning
title: Julia
---


## 18.337J/6.338J: Parallel Computing and Scientific Machine Learning {#18-dot-337j-6-dot-338j-parallel-computing-and-scientific-machine-learning}

MIT Course by @ChrisRackauckas Chris Rackauckas
<https://github.com/mitmath/18337>

### Lecture 1 {#lecture-1}

### Lecture 2: Optimizing Serial Code in Julia 2: Type inference, function specialization, and dispatch {#lecture-2-optimizing-serial-code-in-julia-2-type-inference-function-specialization-and-dispatch}

Vectorization is preferred in Python because vectorization will use pre-compiled
C-code that runs faster than pure Python. Vectorization doesn't necessarily mean
faster in Julia.

In Julia, use @Static types to pre-allocate memory and make things faster. Use .
notation too. A .+ B for elemental operation.

@btime
: check low level code -> assembly

@code\_llvm
: check low level code -> assembly

@code\_typed
: check julia interpreted code, one step before low level translation

@code\_warntype
: check type information for function, make sure the types
    don't change to Any

<!--list-separator-->

- Multiple Dispatch

    Julia does this internally, so why not keep this open for the user?

    ff (x::Int, y::Int) = 2x + y
    ff (x::Float64, y::Float64) = x/y

### Lecture 3: Neural Networks with PINNs {#lecture-3-neural-networks-with-pinns}

### Lecture 4: Discrete Dynamical Systems -> Loops {#lecture-4-discrete-dynamical-systems-loops}

video
: <https://www.youtube.com/watch?v=GhBARuHEydM>

Get an output, stick it back in, do it again, stick it again -> will lead to a
chaotic system! Simplest example is the AR model.

Neural networks are dynamical models.

If a derivative is smaller than one, by taking in many iterations from that
starting areas, you will converge to a fixed point. Stability. Derivative is
basically a linear model/approximation around that small point.

![[2020-12-23_12-44-53_screenshot.png]]

D: eigenvalue decomposition
P: eigenvector

Px\_n+1 = D P x\_n
is basically a projection

![[2020-12-23_12-46-38_screenshot.png]]

In this coordinate system, the dynamics are decoupled and so we can write the
solution in analytical form.

\\[ x\_{n+1} = \lambda\_{1}^n v\_1 + \lambda\_2^n v\_2 \\]

![[2020-12-23_12-52-00_screenshot.png]]

<!--list-separator-->

- Delayed Dynamical System

    A delayed dynamical system is handled similarly except that the lagged terms
    are represented as an augmented dimensional problem. Solve with same methods
    as before.

    ![[2020-12-23_13-03-04_screenshot.png]]

<!--list-separator-->

- Periodicity and Chaos

    x\_n+1 = -x\_n
    x\_0 = 1
    x\_1 = -1
    x\_2 = 1

<!--list-separator-->

- Problems to solve...

    video
    : <https://www.youtube.com/watch?v=AXHLyHfyEuA&feature=youtu.be>

    <~/Documents/Repos/18337/lecture4/dynamical_systems.jmd>

    To go from vectors of vectors to a matrix:

    ```julia
    reduce(hcat, a)
    ```

    it's not better to just build a matrix and populate it -> slices

    Matrices aren't more efficient because matrices are internally vectors and magic
    happens internally that screws things internally because of pre-cacheing things
    internally that won't ever be used.

## Learn Julia in X minutes {#learn-julia-in-x-minutes}

Share this page
Select theme: light dark
Learn X in Y minutes
Where X=Julia
Get the code: learnjulia.jl

Julia is a new homoiconic functional language focused on technical computing.
While having the full power of homoiconic macros, first-class functions, and
low-level control, Julia is as easy to learn and use as Python.

This is based on Julia 1.0.0

```julia
# Single line comments start with a hash (pound) symbol.
#= Multiline comments can be written
   by putting '#=' before the text  and '=#'
   after the text. They can also be nested.
=#

####################################################
## 1. Primitive Datatypes and Operators
####################################################

# Everything in Julia is an expression.

# There are several basic types of numbers.
typeof(3)       # => Int64
typeof(3.2)     # => Float64
typeof(2 + 1im) # => Complex{Int64}
typeof(2 // 3)  # => Rational{Int64}

# All of the normal infix operators are available.
1 + 1      # => 2
8 - 1      # => 7
10 * 2     # => 20
35 / 5     # => 7.0
10 / 2     # => 5.0  # dividing integers always results in a Float64
div(5, 2)  # => 2    # for a truncated result, use div
5 \ 35     # => 7.0
2^2        # => 4    # power, not bitwise xor
12 % 10    # => 2

# Enforce precedence with parentheses
(1 + 3) * 2  # => 8

# Julia (unlike Python for instance) has integer under/overflow
10^19      # => -8446744073709551616
# use bigint or floating point to avoid this
big(10)^19 # => 10000000000000000000
1e19       # => 1.0e19
10.0^19    # => 1.0e19

# Bitwise Operators
~2         # => -3 # bitwise not
3 & 5      # => 1  # bitwise and
2 | 4      # => 6  # bitwise or
xor(2, 4)  # => 6  # bitwise xor
2 >>> 1    # => 1  # logical shift right
2 >> 1     # => 1  # arithmetic shift right
2 << 1     # => 4  # logical/arithmetic shift left

# Use the bitstring function to see the binary representation of a number.
bitstring(12345)
# => "0000000000000000000000000000000000000000000000000011000000111001"
bitstring(12345.0)
# => "0100000011001000000111001000000000000000000000000000000000000000"

# Boolean values are primitives
true
false

# Boolean operators
!true   # => false
!false  # => true
1 == 1  # => true
2 == 1  # => false
1 != 1  # => false
2 != 1  # => true
1 < 10  # => true
1 > 10  # => false
2 <= 2  # => true
2 >= 2  # => true
# Comparisons can be chained
1 < 2 < 3  # => true
2 < 3 < 2  # => false

# Strings are created with "
"This is a string."

# Character literals are written with '
'a'

# Strings are UTF8 encoded. Only if they contain only ASCII characters can
# they be safely indexed.
ascii("This is a string")[1]
# => 'T': ASCII/Unicode U+0054 (category Lu: Letter, uppercase)
# Julia indexes from 1
# Otherwise, iterating over strings is recommended (map, for loops, etc).

# String can be compared lexicographically
"good" > "bye" # => true
"good" == "good" # => true
"1 + 2 = 3" == "1 + 2 = $(1 + 2)" # => true

# $ can be used for string interpolation:
"2 + 2 = $(2 + 2)" # => "2 + 2 = 4"
# You can put any Julia expression inside the parentheses.

# Printing is easy
println("I'm Julia. Nice to meet you!") # => I'm Julia. Nice to meet you!

# Another way to format strings is the printf macro from the stdlib Printf.
using Printf
@printf "%d is less than %f\n" 4.5 5.3  # => 5 is less than 5.300000


####################################################
## 2. Variables and Collections
####################################################

# You don't declare variables before assigning to them.
someVar = 5  # => 5
someVar  # => 5

# Accessing a previously unassigned variable is an error
try
    someOtherVar  # => ERROR: UndefVarError: someOtherVar not defined
catch e
    println(e)
end

# Variable names start with a letter or underscore.
# After that, you can use letters, digits, underscores, and exclamation points.
SomeOtherVar123! = 6  # => 6

# You can also use certain unicode characters
☃ = 8  # => 8
# These are especially handy for mathematical notation
2 * π # => 6.283185307179586

# A note on naming conventions in Julia:
#
# * Word separation can be indicated by underscores ('_'), but use of
#   underscores is discouraged unless the name would be hard to read
#   otherwise.
#
# * Names of Types begin with a capital letter and word separation is shown
#   with CamelCase instead of underscores.
#
# * Names of functions and macros are in lower case, without underscores.
#
# * Functions that modify their inputs have names that end in !. These
#   functions are sometimes called mutating functions or in-place functions.

# Arrays store a sequence of values indexed by integers 1 through n:
a = Int64[] # => 0-element Array{Int64,1}

# 1-dimensional array literals can be written with comma-separated values.
b = [4, 5, 6] # => 3-element Array{Int64,1}: [4, 5, 6]
b = [4; 5; 6] # => 3-element Array{Int64,1}: [4, 5, 6]
b[1]    # => 4
b[end]  # => 6

# 2-dimensional arrays use space-separated values and semicolon-separated rows.
matrix = [1 2; 3 4] # => 2×2 Array{Int64,2}: [1 2; 3 4]

# Arrays of a particular type
b = Int8[4, 5, 6] # => 3-element Array{Int8,1}: [4, 5, 6]

# Add stuff to the end of a list with push! and append!
# By convention, the exclamation mark '!'' is appended to names of functions
# that modify their arguments
push!(a, 1)    # => [1]
push!(a, 2)    # => [1,2]
push!(a, 4)    # => [1,2,4]
push!(a, 3)    # => [1,2,4,3]
append!(a, b)  # => [1,2,4,3,4,5,6]

# Remove from the end with pop
pop!(b)  # => 6
b # => [4,5]

# Let's put it back
push!(b, 6)  # => [4,5,6]
b # => [4,5,6]

a[1]  # => 1  # remember that Julia indexes from 1, not 0!

# end is a shorthand for the last index. It can be used in any
# indexing expression
a[end]  # => 6

# we also have popfirst! and pushfirst!
popfirst!(a)  # => 1
a # => [2,4,3,4,5,6]
pushfirst!(a, 7)  # => [7,2,4,3,4,5,6]
a # => [7,2,4,3,4,5,6]

# Function names that end in exclamations points indicate that they modify
# their argument.
arr = [5,4,6]  # => 3-element Array{Int64,1}: [5,4,6]
sort(arr)   # => [4,5,6]
arr         # => [5,4,6]
sort!(arr)  # => [4,5,6]
arr         # => [4,5,6]

# Looking out of bounds is a BoundsError
try
    a[0]
    # => ERROR: BoundsError: attempt to access 7-element Array{Int64,1} at
    # index [0]
    # => Stacktrace:
    # =>  [1] getindex(::Array{Int64,1}, ::Int64) at .\array.jl:731
    # =>  [2] top-level scope at none:0
    # =>  [3] ...
    # => in expression starting at ...\LearnJulia.jl:180
    a[end + 1]
    # => ERROR: BoundsError: attempt to access 7-element Array{Int64,1} at
    # index [8]
    # => Stacktrace:
    # =>  [1] getindex(::Array{Int64,1}, ::Int64) at .\array.jl:731
    # =>  [2] top-level scope at none:0
    # =>  [3] ...
    # => in expression starting at ...\LearnJulia.jl:188
catch e
    println(e)
end

# Errors list the line and file they came from, even if it's in the standard
# library. You can look in the folder share/julia inside the julia folder to
# find these files.

# You can initialize arrays from ranges
a = [1:5;]  # => 5-element Array{Int64,1}: [1,2,3,4,5]
a2 = [1:5]  # => 1-element Array{UnitRange{Int64},1}: [1:5]

# You can look at ranges with slice syntax.
a[1:3]  # => [1, 2, 3]
a[2:end]  # => [2, 3, 4, 5]

# Remove elements from an array by index with splice!
arr = [3,4,5]
splice!(arr, 2) # => 4
arr # => [3,5]

# Concatenate lists with append!
b = [1,2,3]
append!(a, b) # => [1, 2, 3, 4, 5, 1, 2, 3]
a # => [1, 2, 3, 4, 5, 1, 2, 3]

# Check for existence in a list with in
in(1, a)  # => true

# Examine the length with length
length(a)  # => 8

# Tuples are immutable.
tup = (1, 2, 3)  # => (1,2,3)
typeof(tup) # => Tuple{Int64,Int64,Int64}
tup[1] # => 1
try
    tup[1] = 3
    # => ERROR: MethodError: no method matching
    # setindex!(::Tuple{Int64,Int64,Int64}, ::Int64, ::Int64)
catch e
    println(e)
end

# Many array functions also work on tuples
length(tup) # => 3
tup[1:2]    # => (1,2)
in(2, tup)  # => true

# You can unpack tuples into variables
a, b, c = (1, 2, 3)  # => (1,2,3)
a # => 1
b # => 2
c # => 3

# Tuples are created even if you leave out the parentheses
d, e, f = 4, 5, 6  # => (4,5,6)
d # => 4
e # => 5
f # => 6

# A 1-element tuple is distinct from the value it contains
(1,) == 1 # => false
(1) == 1  # => true

# Look how easy it is to swap two values
e, d = d, e  # => (5,4)
d # => 5
e # => 4

# Dictionaries store mappings
emptyDict = Dict()  # => Dict{Any,Any} with 0 entries

# You can create a dictionary using a literal
filledDict = Dict("one" => 1, "two" => 2, "three" => 3)
# => Dict{String,Int64} with 3 entries:
# =>  "two" => 2, "one" => 1, "three" => 3

# Look up values with []
filledDict["one"]  # => 1

# Get all keys
keys(filledDict)
# => Base.KeySet for a Dict{String,Int64} with 3 entries. Keys:
# =>  "two", "one", "three"
# Note - dictionary keys are not sorted or in the order you inserted them.

# Get all values
values(filledDict)
# => Base.ValueIterator for a Dict{String,Int64} with 3 entries. Values:
# =>  2, 1, 3
# Note - Same as above regarding key ordering.

# Check for existence of keys in a dictionary with in, haskey
in(("one" => 1), filledDict)  # => true
in(("two" => 3), filledDict)  # => false
haskey(filledDict, "one")     # => true
haskey(filledDict, 1)         # => false

# Trying to look up a non-existent key will raise an error
try
    filledDict["four"]  # => ERROR: KeyError: key "four" not found
catch e
    println(e)
end

# Use the get method to avoid that error by providing a default value
# get(dictionary, key, defaultValue)
get(filledDict, "one", 4)   # => 1
get(filledDict, "four", 4)  # => 4

# Use Sets to represent collections of unordered, unique values
emptySet = Set()  # => Set(Any[])
# Initialize a set with values
filledSet = Set([1, 2, 2, 3, 4])  # => Set([4, 2, 3, 1])

# Add more values to a set
push!(filledSet, 5)  # => Set([4, 2, 3, 5, 1])

# Check if the values are in the set
in(2, filledSet)   # => true
in(10, filledSet)  # => false

# There are functions for set intersection, union, and difference.
otherSet = Set([3, 4, 5, 6])         # => Set([4, 3, 5, 6])
intersect(filledSet, otherSet)      # => Set([4, 3, 5])
union(filledSet, otherSet)          # => Set([4, 2, 3, 5, 6, 1])
setdiff(Set([1,2,3,4]), Set([2,3,5])) # => Set([4, 1])

####################################################
## 3. Control Flow
####################################################

# Let's make a variable
someVar = 5

# Here is an if statement. Indentation is not meaningful in Julia.
if someVar > 10
    println("someVar is totally bigger than 10.")
elseif someVar < 10    # This elseif clause is optional.
    println("someVar is smaller than 10.")
else                    # The else clause is optional too.
    println("someVar is indeed 10.")
end
# => prints "some var is smaller than 10"

# For loops iterate over iterables.
# Iterable types include Range, Array, Set, Dict, and AbstractString.
for animal = ["dog", "cat", "mouse"]
    println("$animal is a mammal")
    # You can use $ to interpolate variables or expression into strings
end
# => dog is a mammal
# => cat is a mammal
# => mouse is a mammal

# You can use 'in' instead of '='.
for animal in ["dog", "cat", "mouse"]
    println("$animal is a mammal")
end
# => dog is a mammal
# => cat is a mammal
# => mouse is a mammal

for pair in Dict("dog" => "mammal", "cat" => "mammal", "mouse" => "mammal")
    from, to = pair
    println("$from is a $to")
end
# => mouse is a mammal
# => cat is a mammal
# => dog is a mammal

for (k, v) in Dict("dog" => "mammal", "cat" => "mammal", "mouse" => "mammal")
    println("$k is a $v")
end
# => mouse is a mammal
# => cat is a mammal
# => dog is a mammal

# While loops loop while a condition is true
let x = 0
    while x < 4
        println(x)
        x += 1  # Shorthand for x = x + 1
    end
end
# => 0
# => 1
# => 2
# => 3

# Handle exceptions with a try/catch block
try
    error("help")
catch e
    println("caught it $e")
end
# => caught it ErrorException("help")

####################################################
## 4. Functions
####################################################

# The keyword 'function' creates new functions
# function name(arglist)
#   body...
# end
function add(x, y)
    println("x is $x and y is $y")

    # Functions return the value of their last statement
    x + y
end

add(5, 6)
# => x is 5 and y is 6
# => 11

# Compact assignment of functions
f_add(x, y) = x + y  # => f_add (generic function with 1 method)
f_add(3, 4)  # => 7

# Function can also return multiple values as tuple
fn(x, y) = x + y, x - y # => fn (generic function with 1 method)
fn(3, 4)  # => (7, -1)

# You can define functions that take a variable number of
# positional arguments
function varargs(args...)
    return args
    # use the keyword return to return anywhere in the function
end
# => varargs (generic function with 1 method)

varargs(1, 2, 3)  # => (1,2,3)

# The ... is called a splat.
# We just used it in a function definition.
# It can also be used in a function call,
# where it will splat an Array or Tuple's contents into the argument list.
add([5,6]...)  # this is equivalent to add(5,6)

x = (5, 6)  # => (5,6)
add(x...)  # this is equivalent to add(5,6)


# You can define functions with optional positional arguments
function defaults(a, b, x=5, y=6)
    return "$a $b and $x $y"
end
# => defaults (generic function with 3 methods)

defaults('h', 'g')  # => "h g and 5 6"
defaults('h', 'g', 'j')  # => "h g and j 6"
defaults('h', 'g', 'j', 'k')  # => "h g and j k"
try
    defaults('h')  # => ERROR: MethodError: no method matching defaults(::Char)
    defaults()  # => ERROR: MethodError: no method matching defaults()
catch e
    println(e)
end

# You can define functions that take keyword arguments
function keyword_args(;k1=4, name2="hello")  # note the ;
    return Dict("k1" => k1, "name2" => name2)
end
# => keyword_args (generic function with 1 method)

keyword_args(name2="ness")  # => ["name2"=>"ness", "k1"=>4]
keyword_args(k1="mine")     # => ["name2"=>"hello", "k1"=>"mine"]
keyword_args()              # => ["name2"=>"hello", "k1"=>4]

# You can combine all kinds of arguments in the same function
function all_the_args(normalArg, optionalPositionalArg=2; keywordArg="foo")
    println("normal arg: $normalArg")
    println("optional arg: $optionalPositionalArg")
    println("keyword arg: $keywordArg")
end
# => all_the_args (generic function with 2 methods)

all_the_args(1, 3, keywordArg=4)
# => normal arg: 1
# => optional arg: 3
# => keyword arg: 4

# Julia has first class functions
function create_adder(x)
    adder = function (y)
        return x + y
    end
    return adder
end
# => create_adder (generic function with 1 method)

# This is "stabby lambda syntax" for creating anonymous functions
(x -> x > 2)(3)  # => true

# This function is identical to create_adder implementation above.
function create_adder(x)
    y -> x + y
end
# => create_adder (generic function with 1 method)

# You can also name the internal function, if you want
function create_adder(x)
    function adder(y)
        x + y
    end
    adder
end
# => create_adder (generic function with 1 method)

add_10 = create_adder(10) # => (::getfield(Main, Symbol("#adder#11")){Int64})
                          # (generic function with 1 method)
add_10(3) # => 13


# There are built-in higher order functions
map(add_10, [1,2,3])  # => [11, 12, 13]
filter(x -> x > 5, [3, 4, 5, 6, 7])  # => [6, 7]

# We can use list comprehensions
[add_10(i) for i = [1, 2, 3]]   # => [11, 12, 13]
[add_10(i) for i in [1, 2, 3]]  # => [11, 12, 13]
[x for x in [3, 4, 5, 6, 7] if x > 5] # => [6, 7]

####################################################
## 5. Types
####################################################

# Julia has a type system.
# Every value has a type; variables do not have types themselves.
# You can use the `typeof` function to get the type of a value.
typeof(5)  # => Int64

# Types are first-class values
typeof(Int64)     # => DataType
typeof(DataType)  # => DataType
# DataType is the type that represents types, including itself.

# Types are used for documentation, optimizations, and dispatch.
# They are not statically checked.

# Users can define types
# They are like records or structs in other languages.
# New types are defined using the `struct` keyword.

# struct Name
#   field::OptionalType
#   ...
# end
struct Tiger
    taillength::Float64
    coatcolor  # not including a type annotation is the same as `::Any`
end

# The default constructor's arguments are the properties
# of the type, in the order they are listed in the definition
tigger = Tiger(3.5, "orange")  # => Tiger(3.5,"orange")

# The type doubles as the constructor function for values of that type
sherekhan = typeof(tigger)(5.6, "fire")  # => Tiger(5.6,"fire")

# These struct-style types are called concrete types
# They can be instantiated, but cannot have subtypes.
# The other kind of types is abstract types.

# abstract Name
abstract type Cat end  # just a name and point in the type hierarchy

# Abstract types cannot be instantiated, but can have subtypes.
# For example, Number is an abstract type
subtypes(Number)  # => 2-element Array{Any,1}:
                  # =>  Complex
                  # =>  Real
subtypes(Cat)  # => 0-element Array{Any,1}

# AbstractString, as the name implies, is also an abstract type
subtypes(AbstractString)  # => 4-element Array{Any,1}:
                          # =>  String
                          # =>  SubString
                          # =>  SubstitutionString
                          # =>  Test.GenericString

# Every type has a super type; use the `supertype` function to get it.
typeof(5) # => Int64
supertype(Int64)    # => Signed
supertype(Signed)   # => Integer
supertype(Integer)  # => Real
supertype(Real)     # => Number
supertype(Number)   # => Any
supertype(supertype(Signed))  # => Real
supertype(Any)      # => Any
# All of these type, except for Int64, are abstract.
typeof("fire")      # => String
supertype(String)   # => AbstractString
# Likewise here with String
supertype(SubString)  # => AbstractString

# <: is the subtyping operator
struct Lion <: Cat  # Lion is a subtype of Cat
    maneColor
    roar::AbstractString
end

# You can define more constructors for your type
# Just define a function of the same name as the type
# and call an existing constructor to get a value of the correct type
Lion(roar::AbstractString) = Lion("green", roar)
# This is an outer constructor because it's outside the type definition

struct Panther <: Cat  # Panther is also a subtype of Cat
    eyeColor
    Panther() = new("green")
    # Panthers will only have this constructor, and no default constructor.
end
# Using inner constructors, like Panther does, gives you control
# over how values of the type can be created.
# When possible, you should use outer constructors rather than inner ones.

####################################################
## 6. Multiple-Dispatch
####################################################

# In Julia, all named functions are generic functions
# This means that they are built up from many small methods
# Each constructor for Lion is a method of the generic function Lion.

# For a non-constructor example, let's make a function meow:

# Definitions for Lion, Panther, Tiger
function meow(animal::Lion)
    animal.roar  # access type properties using dot notation
end

function meow(animal::Panther)
    "grrr"
end

function meow(animal::Tiger)
    "rawwwr"
end

# Testing the meow function
meow(tigger)  # => "rawwwr"
meow(Lion("brown", "ROAAR"))  # => "ROAAR"
meow(Panther()) # => "grrr"

# Review the local type hierarchy
Tiger   <: Cat  # => false
Lion    <: Cat  # => true
Panther <: Cat  # => true

# Defining a function that takes Cats
function pet_cat(cat::Cat)
    println("The cat says $(meow(cat))")
end
# => pet_cat (generic function with 1 method)

pet_cat(Lion("42")) # => The cat says 42
try
    pet_cat(tigger) # => ERROR: MethodError: no method matching pet_cat(::Tiger)
catch e
    println(e)
end

# In OO languages, single dispatch is common;
# this means that the method is picked based on the type of the first argument.
# In Julia, all of the argument types contribute to selecting the best method.

# Let's define a function with more arguments, so we can see the difference
function fight(t::Tiger, c::Cat)
    println("The $(t.coatcolor) tiger wins!")
end
# => fight (generic function with 1 method)

fight(tigger, Panther())  # => The orange tiger wins!
fight(tigger, Lion("ROAR")) # => The orange tiger wins!

# Let's change the behavior when the Cat is specifically a Lion
fight(t::Tiger, l::Lion) = println("The $(l.maneColor)-maned lion wins!")
# => fight (generic function with 2 methods)

fight(tigger, Panther())  # => The orange tiger wins!
fight(tigger, Lion("ROAR")) # => The green-maned lion wins!

# We don't need a Tiger in order to fight
fight(l::Lion, c::Cat) = println("The victorious cat says $(meow(c))")
# => fight (generic function with 3 methods)

fight(Lion("balooga!"), Panther())  # => The victorious cat says grrr
try
    fight(Panther(), Lion("RAWR"))
    # => ERROR: MethodError: no method matching fight(::Panther, ::Lion)
    # => Closest candidates are:
    # =>   fight(::Tiger, ::Lion) at ...
    # =>   fight(::Tiger, ::Cat) at ...
    # =>   fight(::Lion, ::Cat) at ...
    # => ...
catch e
    println(e)
end

# Also let the cat go first
fight(c::Cat, l::Lion) = println("The cat beats the Lion")
# => fight (generic function with 4 methods)

# This warning is because it's unclear which fight will be called in:
try
    fight(Lion("RAR"), Lion("brown", "rarrr"))
    # => ERROR: MethodError: fight(::Lion, ::Lion) is ambiguous. Candidates:
    # =>   fight(c::Cat, l::Lion) in Main at ...
    # =>   fight(l::Lion, c::Cat) in Main at ...
    # => Possible fix, define
    # =>   fight(::Lion, ::Lion)
    # => ...
catch e
    println(e)
end
# The result may be different in other versions of Julia

fight(l::Lion, l2::Lion) = println("The lions come to a tie")
# => fight (generic function with 5 methods)
fight(Lion("RAR"), Lion("brown", "rarrr"))  # => The lions come to a tie


# Under the hood
# You can take a look at the llvm  and the assembly code generated.

square_area(l) = l * l  # square_area (generic function with 1 method)

square_area(5)  # => 25

# What happens when we feed square_area an integer?
code_native(square_area, (Int32,), syntax = :intel)
    #         .text
    # ; Function square_area {
    # ; Location: REPL[116]:1       # Prologue
    #         push    rbp
    #         mov     rbp, rsp
    # ; Function *; {
    # ; Location: int.jl:54
    #         imul    ecx, ecx      # Square l and store the result in ECX
    # ;}
    #         mov     eax, ecx
    #         pop     rbp           # Restore old base pointer
    #         ret                   # Result will still be in EAX
    #         nop     dword ptr [rax + rax]
    # ;}

code_native(square_area, (Float32,), syntax = :intel)
    #         .text
    # ; Function square_area {
    # ; Location: REPL[116]:1
    #         push    rbp
    #         mov     rbp, rsp
    # ; Function *; {
    # ; Location: float.jl:398
    #         vmulss  xmm0, xmm0, xmm0  # Scalar single precision multiply (AVX)
    # ;}
    #         pop     rbp
    #         ret
    #         nop     word ptr [rax + rax]
    # ;}

code_native(square_area, (Float64,), syntax = :intel)
    #         .text
    # ; Function square_area {
    # ; Location: REPL[116]:1
    #         push    rbp
    #         mov     rbp, rsp
    # ; Function *; {
    # ; Location: float.jl:399
    #         vmulsd  xmm0, xmm0, xmm0  # Scalar double precision multiply (AVX)
    # ;}
    #         pop     rbp
    #         ret
    #         nop     word ptr [rax + rax]
    # ;}

# Note that julia will use floating point instructions if any of the
# arguments are floats.
# Let's calculate the area of a circle
circle_area(r) = pi * r * r     # circle_area (generic function with 1 method)
circle_area(5)  # 78.53981633974483

code_native(circle_area, (Int32,), syntax = :intel)
    #         .text
    # ; Function circle_area {
    # ; Location: REPL[121]:1
    #         push    rbp
    #         mov     rbp, rsp
    # ; Function *; {
    # ; Location: operators.jl:502
    # ; Function *; {
    # ; Location: promotion.jl:314
    # ; Function promote; {
    # ; Location: promotion.jl:284
    # ; Function _promote; {
    # ; Location: promotion.jl:261
    # ; Function convert; {
    # ; Location: number.jl:7
    # ; Function Type; {
    # ; Location: float.jl:60
    #         vcvtsi2sd       xmm0, xmm0, ecx     # Load integer (r) from memory
    #         movabs  rax, 497710928              # Load pi
    # ;}}}}}
    # ; Function *; {
    # ; Location: float.jl:399
    #         vmulsd  xmm1, xmm0, qword ptr [rax] # pi * r
    #         vmulsd  xmm0, xmm1, xmm0            # (pi * r) * r
    # ;}}
    #         pop     rbp
    #         ret
    #         nop     dword ptr [rax]
    # ;}

code_native(circle_area, (Float64,), syntax = :intel)
    #         .text
    # ; Function circle_area {
    # ; Location: REPL[121]:1
    #         push    rbp
    #         mov     rbp, rsp
    #         movabs  rax, 497711048
    # ; Function *; {
    # ; Location: operators.jl:502
    # ; Function *; {
    # ; Location: promotion.jl:314
    # ; Function *; {
    # ; Location: float.jl:399
    #         vmulsd  xmm1, xmm0, qword ptr [rax]
    # ;}}}
    # ; Function *; {
    # ; Location: float.jl:399
    #         vmulsd  xmm0, xmm1, xmm0
    # ;}
    #         pop     rbp
    #         ret
    #         nop     dword ptr [rax + rax]
    # ;}
```

## MATLAB–Python–Julia cheatsheet {#matlab-python-julia-cheatsheet}

<https://cheatsheets.quantecon.org>

## JuliaCon 2019 | The Unreasonable Effectiveness of Multiple Dispatch | Stefan Karpinski {#juliacon-2019-the-unreasonable-effectiveness-of-multiple-dispatch-stefan-karpinski}

<https://www.youtube.com/watch?v=kc9HwsxE1OY>

## SciML Scientific Machine Learning Software {#sciml-scientific-machine-learning-software}

<https://sciml.ai>

SciML is an open source software organization created to unify the packages for
scientific machine learning. This includes the development of modular scientific
simulation support software, such as differential equation solvers, along with
the methodologies for inverse problems and automated model discovery. By
providing a diverse set of tools with a common interface, we provide a modular,
easily-extendable, and highly performant ecosystem for handling a wide variety
of scientific simulations.

### Core Components {#core-components}

- High Performance and Feature-Filled Differential Equation Solving. The library
    DifferentialEquations.jl is a library for solving ordinary differential
    equations (ODEs), stochastic differential equations (SDEs), delay differential
    equations (DDEs), differential-algebraic equations (DAEs), and hybrid
    differential equations which include multi-scale models and mixtures with
    agent-based simulations. The templated implementation allows arbitrary array
    and number types to be compatible, giving compatibility with arbitrary
    precision floating point numbers, GPU-based computations, unit-checked
    arithmetic, and other features. DifferentialEquations.jl is designed for both
    high performance on large-scale and small-scale problems, and routinely
    benchmarks at the top of the pack.
- Physics-Informed Model Discovery and Learning. SciML contains a litany of
    modules for automating the process of model discovery and fitting. Tools like
    DiffEqParamEstim.jl and DiffEqBayes.jl provide classical maximum likelihood
    and Bayesian estimation for differential equation based models, while
    DiffEqFlux.jl enables the training of embedded neural networks inside of
    differential equations (neural differential equations or universal
    differential equations) for discovering unknown dynamical equations,
    DataDrivenDiffEq.jl estimates Koopman operators (DMD) and utilizes methods
    like SInDy to turn timeseries data into LaTeX for driving differential
    equations, and ReservoirComputing.jl for Echo State Networks that learn to
    predict the dynamics of chaotic systems.
- A Polyglot Userbase. While the majority of the tooling for SciML is built
    using the Julia programming language, SciML is committed to ensure that these
    methodologies can be used throughout the greater scientific community. Tools
    like diffeqpy and diffeqr bridge the DifferentialEquations.jl solvers to
    Python and R respectively, and we hope to see many more developments along
    these lines in the near future.
- Compiler-Assisted Model Analysis and Sparsity Acceleration. Scientific models
    generally have structures like locality which leads to sparsity in the program
    structures that can be exploited for major performance acceleration. The SciML
    builds a set of interconnected tools for generating numerical solver code
    directly on the models that are being simulated. SparsityDetection.jl can
    automatically detect the sparsity patterns of Jacobians and Hessians from
    arbitrary source code, while ModelingToolkit.jl can rewrite differential
    equation models to re-arrange equations for better stability and automatically
    parallelize code. These tools then connect with affiliated packages like
    SparseDiffTools.jl to accelerate solving with DifferentialEquations.jl and
    training with DiffEqFlux.jl.
- ML-Assisted Tooling for Model Acceleration. SciML supports the development of
    the latest ML-accelerated toolsets for scientific machine learning. Methods
    like Physics-Informed Neural Networks (PINNs) and Deep BSDE methods for
    solving 1000 dimensional partial differential equations are productionized in
    the NeuralPDE.jl library. Surrogate-based acceleration methods are provided by
    Surrogates.jl.
- Differentiable Scientific Data Structures and Simulators. The SciML ecosystem
    contains pre-built scientific simulation tools along with data structures for
    accelerating the development of models. Tools like LabelledArrays.jl and
    MultiScaleArrays.jl make it easy to build large-scale scientific models, while
    other tools like NBodySimulator.jl provide full-scale simulation simulators.
- Tools for Accelerated Algorithm Development and Research. SciML is an
    organization dedicated to helping state-of-the-art research in both numerical
    simulation methods and methodologies in scientific machine learning. Many
    tools throughout the organization automate the process of benchmarking and
    testing new methodologies to ensure they are safe and battle tested, both to
    accelerate the translation of the methods to publications and to users. We
    invite the larger research community to make use of our tooling like
    DiffEqDevTools.jl and our large suite of wrapped algorithms for quickly test
    and deploying new algorithms.

## DiffEqFlux.jl – A Julia Library for Neural Differential Equations {#diffeqflux-dot-jl-a-julia-library-for-neural-differential-equations}

<https://julialang.org/blog/2019/01/fluxdiffeq/>

## zygote {#zygote}

<https://fluxml.ai/Zygote.jl/latest/>

Welcome! Zygote extends the Julia language to support differentiable
programming. With Zygote you can write down any Julia code you feel like –
including using existing Julia packages – then get gradients and optimise your
program. Deep learning, ML and probabilistic programming are all different kinds
of differentiable programming that you can do with Zygote.

## Differentiable Programming and Neural ODEs for Accelerating Model Based Reinforcement Learning and Optimal Control {#differentiable-programming-and-neural-odes-for-accelerating-model-based-reinforcement-learning-and-optimal-control}

<https://medium.com/swlh/neural-ode-for-reinforcement-learning-and-nonlinear-optimal-control-cartpole-problem-revisited-5408018b8d71>

[neural ode github page](https://github.com/paulxshen/neural-ode-cartpole)

Cartpole problem where you know what the physics of the system are and would want to train a reinforcement learning algorithm.

![Cartpole problem](../attachments/2022-01-03-17-16-23.png)

The **System (Environment)** is the cartpole, while the **Controller (Agent)** dictates how to move the cart. The system state space $u$ consists of the cart position, cart velocity, pole angle, and pole angular velocity. The time derivative $f$ describes its time evolution. It’s a function of its current state $u$ and the control action which is the force applied to the cart. We make the controller a neural network $g(u, p)$ with the system state $u$ as input and parameters $p$ as the weights. We specify the system initial condition and let it run, generating a trajectory in state space. We construct a loss functional $l$ acting on the trajectory, penalizing deviations from desired behavior. Goal is to minimize $l$ wrt $p$, ie seeking the optimal weights for the neural controller.

![ODE of cartpole problem](../attachments/2022-01-03-17-18-35.png)

The loss depends on the neural network weights through a chain of functions. The chain rule as applied to the NN is called backpropagation. Now we just need to do the same for the ODE. The PDE and inverse problems literature provide the solution as the “adjoint method,” which yields a “dual” adjoint ODE which is integrated backwards in time.

# todo Print and study the cartpole problem completely:

Problem is described: [[../attachments/t8-Week13-pendulum.pdf]]

Full example: <../attachments/Cartpole.jl>

Causing errors due to NaNs...

# todo Would want to see which function comes from which library.

## Julia Computing & MIT Introduce Differentiable Programming System Bridging AI and Science {#julia-computing-and-mit-introduce-differentiable-programming-system-bridging-ai-and-science}

<https://medium.com/syncedreview/julia-computing-mit-introduce-differentiable-programming-system-bridging-ai-and-science-738c8a9eb0b9>

## Doing Scientific Machine Learning with Julia's SciML Ecosystem [4hr workshop] {#doing-scientific-machine-learning-with-julia-s-sciml-ecosystem-4hr-workshop}

- <https://www.youtube.com/watch?v=QwVO0Xh2Hbg>
- <sup id="b09d26012fb3a4a735390633f3f1e24f"><a href="#Rackauckas_DoingScientificMachine_2020" title="Rackauckas, Doing {{Scientific Machine Learning}} with {{Julia}}'s {{SciML Ecosystem}}, v(), 62 (2020).">Rackauckas_DoingScientificMachine_2020</a></sup>

### YouTube Description {#youtube-description}

Scientific machine learning combines differentiable programming, scientific
simulation (differential equations, nonlinear solvers, etc.), and machine
learning (deep learning) in order impose physical constraints on machine
learning and automatically learn biological models. Given the composibility of
Julia, many have noted that it is positioned as the best language for this set
of numerical techniques, but how to do actually "do" SciML? This workshop gets
your hands dirty.

In this workshop we'll dive into some of the latest techniques in scientific
machine learning, including Universal Differential Equations (Universal
Differential Equations for Scientific Machine Learning), Physics-Informed Neural
Networks (Physics-informed neural networks: A deep learning framework for
solving forward and inverse problems involving nonlinear partial differential
equations), and Sparse Identification of Nonlinear Dynamics (SInDy, Discovering
governing equations from data by sparse identification of nonlinear dynamical
systems). The goal is to get those in the workshop familiar with what these
methods are, what kinds of problems they solve, and know how to use Julia
packages to implement them.

The workshop will jump right into how to model the missing part of a physical
simulation, describe how universal approximators (neural networks) can be used
in this context, and show how to transform such problems into an optimization
problem which is then accelerated by specializing automatic differentiation. The
set of packages that is involved in this is somewhat intense, using many tools
from JuliaDiffEq (DiffEqFlux.jl, DifferentialEquations.jl, DiffEqSensitivity.jl,
ModelingToolkit.jl, NeuralPDE.jl, DataDrivenDiffEq.jl, Surrogates.jl, etc.)
combined with machine learning tools (Flux.jl), differentiation tooling
(SparseDiffTools.jl, Zygote.jl, ForwardDiff.jl, ReverseDiff.jl, etc.), and
optimization tooling (JuMP, Optim.jl, Flux.jl, NLopt.jl, etc.) all spun together
in a glorious soup that automatically discovers physical laws at the end of the
day. Thus this workshop has something different to offer for everyone: new users
of Julia will get a nice overview of the unique composibility of the Julia
package ecosystem, while experienced Julia users will learn how to bridge some
area that they are comfortable with (such as machine learning) to a whole new
set of phenomena. Meanwhile, even though who are only knee deep in coding can
gain a lot from learning these new mathematical advances, meaning that even a
casual observer likely has a lot to learn!

### What is scientific machine learning {#what-is-scientific-machine-learning}

Mix of scientific models with data-driven machine learning component for
data-efficient model-based decision making.

Universal approximation theorem: a neural net can map \\(R^n -> R^m\\) to \\(\epsilon\\)
within a domain since it acts as a fancy Taylor expansion.

The major advances in machine learning were due to encoding more structure into
the model -> more prior knowledge (CNN = encodes shift/rotation invariance).

We can utilize neural networks to figure out the missing parts of a physical
problem -> solve the last mile.

### Universal ODE {#universal-ode}

Replacing parts unknown of a model with a neural network.

![[2020-12-28_10-43-41_screenshot.png]]

Universal ODE -> Internal Sparse Regression

- Sparse identification on only the missing term
- Go from neural network to polynomial regression -> verifiability

![[2020-12-28_10-52-01_screenshot.png]]

### Discretized PDE operators are convolutions {#discretized-pde-operators-are-convolutions}

![[2020-12-28_11-00-51_screenshot.png]]

### Live Coding time! {#live-coding-time}

<https://youtu.be/QwVO0Xh2Hbg?t=4578>

<~/Documents/Repos/julia_demo/juliacon_2020_sciml.jl>

### Modelling {#modelling}

- ModelingToolkit.jl: symbolic-numerics for accelerated modelling
- PowerSimulationsDynamics.jl: dynamics of power grids
- JuSDL.jl: causal modelling that can mix the various differential equations

### SciML tutorials {#sciml-tutorials}

tutorials.sciml.ai -> exercises

### Bayesian methods {#bayesian-methods}

<https://turing.ml/dev/>

### Universal differential equations {#universal-differential-equations}

- <sup id="d3b76e5769504c5ba7300f0fa658c1fc"><a href="#Rackauckas_UniversalDifferentialEquations_2020" title="Rackauckas, Ma, Martensen, Warner, Zubov, Supekar, Skinner, Ramadhan \&amp; Edelman, Universal {{Differential Equations}} for {{Scientific Machine Learning}}, {arXiv:2001.04385 [cs, math, q-bio, stat]}, v(), (2020).">Rackauckas_UniversalDifferentialEquations_2020</a></sup>
- <https://github.com/ChrisRackauckas/universal%5Fdifferential%5Fequations>

Example in video: <https://github.com/ChrisRackauckas/universal%5Fdifferential%5Fequations/blob/master/DelayLotkaVolterra/VolterraExp.jl>

ModelingToolkit.jl -> to then transform the neural network into an equation,
handled symbolically
along with DataDrivenDiffEq.jl

Neural networks not extrapolating very well is when the neural network has to do
the full job. If you add in more information on the structure of the problem,
the neural network part would be more confined and would do much better. To
reduce overfitting, the sparsification of the neural network through
transforming it into equations based on a basis.

### NeuralPDE.jl: Automated PDE Solving via Neural Networks {#neuralpde-dot-jl-automated-pde-solving-via-neural-networks}

## Julia Cheat Sheet {#julia-cheat-sheet}

</ox-hugo/Julia-cheatsheet.pdf>

# Instantiate a new environment

If there's a `Manifest.toml` and `Project.toml`..

``` julia
pkg activate .  # activate current project, else `pkg activate project_name`
pkg instantiate  # install all the packages
pkg status  # to see what we have
```

basically use the `]` in the cli.


[//begin]: # "Autogenerated link references for markdown compatibility"
[[2020-12-23_12-44-53_screenshot.png]: ../attachments/18.337J/6.338J__Parallel_Computing_and_Scientific_Machine_Learning/2020-12-23_12-44-53_screenshot.png "2020-12-23_12-44-53_screenshot.png"
[[2020-12-23_12-46-38_screenshot.png]: ../attachments/18.337J/6.338J__Parallel_Computing_and_Scientific_Machine_Learning/2020-12-23_12-46-38_screenshot.png "2020-12-23_12-46-38_screenshot.png"
[[2020-12-23_12-52-00_screenshot.png]: ../attachments/18.337J/6.338J__Parallel_Computing_and_Scientific_Machine_Learning/2020-12-23_12-52-00_screenshot.png "2020-12-23_12-52-00_screenshot.png"
[[2020-12-23_13-03-04_screenshot.png]: ../attachments/18.337J/6.338J__Parallel_Computing_and_Scientific_Machine_Learning/2020-12-23_13-03-04_screenshot.png "2020-12-23_13-03-04_screenshot.png"
[../attachments/t8-Week13-pendulum.pdf]: ../attachments/t8-Week13-pendulum.pdf "t8-Week13-pendulum.pdf"
[[2020-12-28_10-43-41_screenshot.png]: ../attachments/Doing_Scientific_Machine_Learning_with_Julia's_SciML_Ecosystem_[4hr_workshop]/2020-12-28_10-43-41_screenshot.png "2020-12-28_10-43-41_screenshot.png"
[[2020-12-28_10-52-01_screenshot.png]: ../attachments/Doing_Scientific_Machine_Learning_with_Julia's_SciML_Ecosystem_[4hr_workshop]/2020-12-28_10-52-01_screenshot.png "2020-12-28_10-52-01_screenshot.png"
[[2020-12-28_11-00-51_screenshot.png]: ../attachments/Doing_Scientific_Machine_Learning_with_Julia's_SciML_Ecosystem_[4hr_workshop]/2020-12-28_11-00-51_screenshot.png "2020-12-28_11-00-51_screenshot.png"
[//end]: # "Autogenerated link references"


[//begin]: # "Autogenerated link references for markdown compatibility"
[[2020-12-23_12-44-53_screenshot.png]: ../attachments/18.337J/6.338J__Parallel_Computing_and_Scientific_Machine_Learning/2020-12-23_12-44-53_screenshot.png "2020-12-23_12-44-53_screenshot.png"
[[2020-12-23_12-46-38_screenshot.png]: ../attachments/18.337J/6.338J__Parallel_Computing_and_Scientific_Machine_Learning/2020-12-23_12-46-38_screenshot.png "2020-12-23_12-46-38_screenshot.png"
[[2020-12-23_12-52-00_screenshot.png]: ../attachments/18.337J/6.338J__Parallel_Computing_and_Scientific_Machine_Learning/2020-12-23_12-52-00_screenshot.png "2020-12-23_12-52-00_screenshot.png"
[[2020-12-23_13-03-04_screenshot.png]: ../attachments/18.337J/6.338J__Parallel_Computing_and_Scientific_Machine_Learning/2020-12-23_13-03-04_screenshot.png "2020-12-23_13-03-04_screenshot.png"
[../attachments/t8-Week13-pendulum.pdf]: ../attachments/t8-Week13-pendulum.pdf "t8-Week13-pendulum.pdf"
[[2020-12-28_10-43-41_screenshot.png]: ../attachments/Doing_Scientific_Machine_Learning_with_Julia's_SciML_Ecosystem_[4hr_workshop]/2020-12-28_10-43-41_screenshot.png "2020-12-28_10-43-41_screenshot.png"
[[2020-12-28_10-52-01_screenshot.png]: ../attachments/Doing_Scientific_Machine_Learning_with_Julia's_SciML_Ecosystem_[4hr_workshop]/2020-12-28_10-52-01_screenshot.png "2020-12-28_10-52-01_screenshot.png"
[[2020-12-28_11-00-51_screenshot.png]: ../attachments/Doing_Scientific_Machine_Learning_with_Julia's_SciML_Ecosystem_[4hr_workshop]/2020-12-28_11-00-51_screenshot.png "2020-12-28_11-00-51_screenshot.png"
[//end]: # "Autogenerated link references"

[//begin]: # "Autogenerated link references for markdown compatibility"
[[2020-12-23_12-44-53_screenshot.png]: ../attachments/18.337J/6.338J__Parallel_Computing_and_Scientific_Machine_Learning/2020-12-23_12-44-53_screenshot.png "2020-12-23_12-44-53_screenshot.png"
[[2020-12-23_12-46-38_screenshot.png]: ../attachments/18.337J/6.338J__Parallel_Computing_and_Scientific_Machine_Learning/2020-12-23_12-46-38_screenshot.png "2020-12-23_12-46-38_screenshot.png"
[[2020-12-23_12-52-00_screenshot.png]: ../attachments/18.337J/6.338J__Parallel_Computing_and_Scientific_Machine_Learning/2020-12-23_12-52-00_screenshot.png "2020-12-23_12-52-00_screenshot.png"
[[2020-12-23_13-03-04_screenshot.png]: ../attachments/18.337J/6.338J__Parallel_Computing_and_Scientific_Machine_Learning/2020-12-23_13-03-04_screenshot.png "2020-12-23_13-03-04_screenshot.png"
[../attachments/t8-Week13-pendulum.pdf]: ../attachments/t8-Week13-pendulum.pdf "t8-Week13-pendulum.pdf"
[[2020-12-28_10-43-41_screenshot.png]: ../attachments/Doing_Scientific_Machine_Learning_with_Julia's_SciML_Ecosystem_[4hr_workshop]/2020-12-28_10-43-41_screenshot.png "2020-12-28_10-43-41_screenshot.png"
[[2020-12-28_10-52-01_screenshot.png]: ../attachments/Doing_Scientific_Machine_Learning_with_Julia's_SciML_Ecosystem_[4hr_workshop]/2020-12-28_10-52-01_screenshot.png "2020-12-28_10-52-01_screenshot.png"
[[2020-12-28_11-00-51_screenshot.png]: ../attachments/Doing_Scientific_Machine_Learning_with_Julia's_SciML_Ecosystem_[4hr_workshop]/2020-12-28_11-00-51_screenshot.png "2020-12-28_11-00-51_screenshot.png"
[//end]: # "Autogenerated link references"