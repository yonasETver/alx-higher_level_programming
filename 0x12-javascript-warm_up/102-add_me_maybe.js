#!/usr/bin/node
// Executes x times a function.

exports.addMeMaybe = function (number, theFunction) {
  number++;
  theFunction(number);
};
