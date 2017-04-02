"use strict";

const Stack3 = () =>
  ({
    array: [],
    index: -1,
    push (value) {
      return this.array[this.index += 1] = value;
    },
    pop () {
      const value = this.array[this.index];

      this.array[this.index] = undefined;
      if (this.index >= 0) {
        this.index -= 1
      }
      return value
    },
    isEmpty () {
      return this.index < 0
    },
    [Symbol.iterator] () {
      let iterationIndex = this.index;

      return {
        next () {
          if (iterationIndex > this.index) {
            iterationIndex = this.index;
          }
          if (iterationIndex < 0) {
            return {done: true};
          }
          else {
            return {done: false, value: this.array[iterationIndex--]}
          }
        }
      }
    }
  });

const stack = Stack3();

stack.push(2000);
stack.push(10);
stack.push(5)

const collectionSum = (collection) => {
  const iterator = collection[Symbol.iterator]();

  let eachIteration,
      sum = 0;

  while ((eachIteration = iterator.next(), !eachIteration.done)) {
    sum += eachIteration.value;
  }
  return sum
}


const iterableSum = (iterable) => {
  let sum = 0;

  for (const num of iterable) {
    sum += num;
  }
  return sum
}

console.log(iterableSum(stack));
