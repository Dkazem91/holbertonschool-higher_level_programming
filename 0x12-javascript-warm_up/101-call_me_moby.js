#!/usr/bin/node
exports.callMeMoby = function call (x, theFunction) {
  if (x) {
    theFunction();
    return call(x - 1, theFunction);
  }
};
