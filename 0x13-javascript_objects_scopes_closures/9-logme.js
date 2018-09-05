#!/usr/bin/node
exports.logMe = function (item) {
  this.counter = this.counter || 0;
  console.log(this.counter + ': ' + item);
  this.counter++;
};
