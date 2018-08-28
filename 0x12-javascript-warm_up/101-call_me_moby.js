exports.callMeMoby = function call(a, b) {
  if (a) {
    b();
    return call(a - 1, b);
  }
  return;
}
