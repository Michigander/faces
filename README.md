# faces
Exploring the construction of a face animation api with Python

## motivation
We want to provide a set of functions for controlling a face.

Our motivation and proof of concept implementation will be using the faces api
to control the sawyer robot face - a Rethink Robotics product.

For this to work, we will need to define the facial components - in this case the
iris, eyes, and eyebrows. In particular we will need a method of obtaining the
value of those components through various animations or to have those values
explicitly defined.

The ability to detect facial components and apply animations to those components
without requiring additional images to be supplied is a wonderful goal, but not
in the first edition. For now, a component will need a base image, and every frame
image of the animations in which the component is included.

Furthermore, it may be interesting to implement a face in two layers - one being
the visible pixels and the other an underlying array of neurons. We will come
back to this idea.

### example 1 - blink
The simplest implementation of a blink is a function which applies left-eye and
right-eye image transformations in parallel on the face image. Periodically,
the image is published to the head display.

## structure

## ideas 
Here, we present some ideas on the design and implementation of our robot face. 

It seems that the face may be better implemented as an interface to be extended and implemented. For example, Sawyer would extend face and implement its low-level animation methods. 