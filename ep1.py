from pyeda.boolalg.bdd import bddvar

a, b = map(bddvar, 'ab')
assert isinstance(b, object)
assert isinstance(a, object)
f = (a & ~b | ~a & b | ~a & ~b | a & b)
print(f.is_one())
