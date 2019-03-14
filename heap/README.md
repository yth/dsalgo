# Heap Implementation

## Rationale

I could not find a heap implementation with decrease/increase key.

The few instances where increase/decrease key was found, it required the
programmer to know the index of the object that you want to increase/
decrease key for.

This version just require you to know the object that you want to perform
increase or decrease key on.

## Implementation

This is a binary min-heap with four operations: insert, peek, delete_min, and decrease_key.

There are a few simple test included in the file.

## Usage

The heap should be able to work with any objects that can be compared with each other and that can be hashed. If you intend to use the heap on an object type of your own design, you need to implement \__hash__, \__eq__, and \__lt__ (or another magical comparison method).
