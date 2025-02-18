from sage.combinat.words.word import Word
from sage.matrix.special import identity_matrix
from sage.modules.free_module_element import vector

def return_words(s, w=None, verb=0):
    """
    Find return words on w for sustitution s,
    where w is a prefix of a fixed point of s.
    If w is None, take first letter of a fixed point.

    A word u is a return word for w if
    - uw is in the language of s,
    - w is a prefix of u, and there is no other occurence of w in u

    INPUT:
        - ``s`` - WordMorphism - the substitution
        - ``w`` - Word (default: ``None``) - a prefix of a fixed point of s
        - ``verb`` - int (default: 0) - If > 0, print informations

    OUTPUT:
        A set of return words.

    EXAMPLES::
        sage: from eigenmorphic import *
        sage: s = WordMorphism('1->112,2->2321,3->12')
        sage: return_words(s, '1')
        {word: 1, word: 12, word: 12232, word: 1232}
    """
    if w is None:
        w = s.fixed_points()[0][:1]
        if verb > 0:
            print("w = " + str(w))
    else:
        w = Word(w, alphabet=s.domain().alphabet())
    to_see = set([w])
    res = set(to_see)
    while len(to_see) > 0:
        to_see2 = set()
        for r in to_see:
            r2 = s(r)
            ri = 0
            for i in range(1,len(r2)-len(w)+1):
                if r2[i:i+len(w)] == w:
                    r3 = r2[ri:i]
                    if r3 not in res:
                        res.add(r3)
                        to_see2.add(r3)
                    ri = i
            r3 = r2[ri:]
            if r3 not in res:
                res.add(r3)
                to_see2.add(r3)
        to_see = to_see2
    return res

def is_balanced(u,v, pv=None):
    """
    Test if a couple of words is balanced for projection pv.

    INPUT:
        - ``u`` - Word
        - ``v`` - Word
        - ``pv`` - (default: ``None``) - vector or matrix - projection

    OUPTUT:
        A bool.

    EXAMPLES::
        sage: from eigenmorphic.balanced_pair_algo import is_balanced
        sage: w = Word('1221', alphabet=list('123'))
        sage: is_balanced(w[:2], w[2:], vector((1,1,1)))
        True
        sage: is_balanced(w[:2], w[2:])
        True
    """
    if pv is None:
        pv = identity_matrix(u.parent().alphabet().cardinality())
    return pv*(vector(u.abelian_vector()) - vector(v.abelian_vector())) == 0

def decompose(u, v, pv=None):
    """
    Decompose a balanced pair into irreducible pairs, for a projection pv.

    INPUT:
        - ``u`` - Word
        - ``v`` - Word
        - ``pv`` - (default: ``None``) - vector or matrix - projection

    OUTPUT:
        List of irreducible balanced pairs (list of couples of words)

    EXAMPLES::
        sage: from eigenmorphic.balanced_pair_algo import decompose
        sage: s = WordMorphism('a->ab,b->ac,c->a')
        sage: decompose(s('ab'), s('ba'))
        [(word: a, word: a), (word: bac, word: cab)]
    """
    if pv is None:
        pv = identity_matrix(u.parent().alphabet().cardinality())
    r = []
    ri = 0
    for i in range(1,len(u)+1):
        u1, v1 = u[ri:i], v[ri:i]
        if is_balanced(u1, v1, pv):
            r.append((u1, v1))
            ri = i
    return r

def first_balanced_pairs(s, w, pv, verb=0):
    """
    First set of balanced pairs in the balanced pair algorithm.

    INPUT:
        - ``s`` - WordMorphism - the substitution, assumed to have a fixed point
        - ``w`` - Word - prefix of a fixed point of s
        - ``pv`` - (default: ``None``) - vector or matrix - projection
        - ``verb`` - int (default: 0) - If > 0, print informations

    OUTPUT:
        A set of balanced pairs (couples of words).

    EXAMPLES::
        sage: from eigenmorphic.balanced_pair_algo import first_balanced_pairs
        sage: s = WordMorphism('1->112,2->2321,3->12')
        sage: first_balanced_pairs(s, Word('1', alphabet=list('123')), identity_matrix(3))
        {(word: 1, word: 1),
         (word: 12, word: 21),
         (word: 12232, word: 22321),
         (word: 1232, word: 2321)}
    """
    lr = return_words(s, w, verb-1)
    lb = [(u, u[len(w):]+w) for u in lr]
    lb2 = set()
    for u,v in lb:
        lb2.update(decompose(u, v, pv))
    return lb2

def balanced_pair_algorithm(s, w=None, pv=None, getgraph=0, verb=0):
    """
    Balanced pair algorithm, to test if the subshift of s has pure discrete spectrum.

    INPUT:
        - ``s`` - WordMorphism -- the substitution
        - ``w`` - Word -- prefix of a periodic point of s
        - ``pv`` - (default: ``None``) - vector or matrix - projection
        - ``verb`` - int (default: 0) - If > 0, print informations

    OUTPUT:
        A bool.

    EXAMPLES::
        sage: from eigenmorphic import *
        sage: s = WordMorphism('a->ab,b->ac,c->a')
        sage: balanced_pair_algorithm(s)
        True
        sage: s = WordMorphism('a->Ab,b->A,A->aB,B->a')
        sage: balanced_pair_algorithm(s)
        False
        sage: s = WordMorphism('1->31,2->412,3->312,4->412')
        sage: balanced_pair_algorithm(s)
        True
    """
    # find a power of s that have fixed point
    p = 1
    while (len((s**p).fixed_points()) == 0):
        p += 1
    s = s**p
    # define w is not
    if w is None:
        w = s.fixed_points()[0][:1]
        if verb > 0:
            print("w = " + str(w))
    else:
        w = Word(w, alphabet=s.domain().alphabet())
    # define pv if not
    if pv is None:
        m = s.incidence_matrix()
        if verb > 1:
            print("incidence matrix:")
            print(m)
        pv = max(m.eigenvectors_left())[1][0]
        if verb > 1:
            print("pv = %s" % pv)
    # compute the first set of balanced pairs
    to_see = first_balanced_pairs(s, w, pv)
    # stabilize by the substitution
    lb = {(u,v):i for i,(u,v) in enumerate(to_see)} # associate an integer to each balanced pair
    n = len(lb)
    ee = dict() # list of entering edges of the graph, for each state, labeled by integers
    while len(to_see) > 0:
        u,v = to_see.pop()
        if verb > 1:
            txt1 = "s(" + str(u) + ") = "
            txt2 = " (" + str(v) + ")   "
        for u2,v2 in decompose(s(u), s(v), pv):
            if verb > 1:
                txt1 += "(" + str(u2) + ")"
                txt2 += "(" + str(v2) + ")"
            if (u2,v2) not in lb:
                lb[(u2,v2)] = n
                to_see.add((u2,v2))
                n += 1
            if verb > 2:
                print("%s --> %s (%s --> %s)" % (lb[(u,v)], lb[(u2,v2)], (u,v), (u2,v2)))
            if lb[(u2,v2)] not in ee:
                ee[lb[(u2,v2)]] = set()
            ee[lb[(u2,v2)]].add(lb[(u,v)])
        if verb > 1:
            print(txt1)
            print(txt2)
    if verb > 0:
        print("balanced pairs =")
        print(lb)
        print("ee =")
        print(ee)
    if getgraph:
        return lb, ee
    # browse the graph to determine if every pair leads to a coincidence
    to_see = [lb[(u,v)] for u,v in lb if len(u) == 1 and u == v] # list of coincidences
    seen = set(to_see)
    while len(to_see) > 0:
        e = to_see.pop()
        if e not in ee:
            continue
        for e2 in ee[e]:
            if e2 not in seen:
                seen.add(e2)
                to_see.append(e2)
    pd = len(seen) == len(lb) # pure discreteness
    if verb > 1:
        print("Algo finished !")
    return pd

import concurrent.futures, time

def has_pure_discrete_spectrum(s, verb=0):
    """
    Test if the subshift of s has pure discrete spectrum.

    INPUT:
        - ``s`` - WordMorphism -- the substitution (assumed to be primitive)
        - ``verb`` - int (default: ``0``) -- If > 0, print informations

    OUTPUT:
        A bool.

    EXAMPLES::
        sage: from eigenmorphic import *
        sage: s = WordMorphism('a->ab,b->ac,c->a')
        sage: has_pure_discrete_spectrum(s)
        True
        sage: s = WordMorphism('a->Ab,b->A,A->aB,B->a')
        sage: has_pure_discrete_spectrum(s)
        False
        sage: s = WordMorphism('1->31,2->412,3->312,4->412')
        sage: has_pure_discrete_spectrum(s)
        True

        # non terminating example from "A generalized balanced pair algorithm" by Brian F. Martensen
        sage: s = WordMorphism('1->1234,2->124,3->13234,4->1324')
        sage: has_pure_discrete_spectrum(s)  # not tested
    """
    # compute pv
    m = s.incidence_matrix()
    if verb > 1:
        print("incidence matrix:")
        print(m)
    pv = max(m.eigenvectors_left())[1][0]
    if verb > 1:
        print("pv = %s" % pv)
    # find a power of s that have fixed point
    p = 1
    while (len((s**p).fixed_points()) == 0):
        p += 1
    s = s**p
    # create an executor of processes
    with concurrent.futures.ProcessPoolExecutor() as executor:
        if verb > 2:
            print("ProcessPoolExecutor created")
        futures = []
        for n in range(1,1000): # browse possible lengths
            if verb > 1:
                print("test with prefixes of length %s" % n)
            sw = set()
            for w in s.fixed_points():
                sw.add(w[:n])
            if verb > 1:
                print(sw)
            for w in sw:
                # submit a new task
                if verb > 0:
                    print("execute balanced_pair_algorithm with w = %s..." % w)
                futures.append(executor.submit(balanced_pair_algorithm, s, w, pv))
            for _ in range(40*n):
                time.sleep(.1)
                # test if one task has finished
                for task in futures:
                    if task.done():
                        res = task.result()
                        executor.shutdown(wait=False, cancel_futures=True)
                        return res

