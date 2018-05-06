#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if False in [isinstance(listx, list) for listx in m_a]:
        raise TypeError("m_a must be a list of lists")
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    if False in [isinstance(listx, list) for listx in m_b]:
        raise TypeError("m_b must be a list of lists")
    if not len(m_a) or 0 in [len(listx) for listx in m_a]:
        raise ValueError("m_a can't be empty")
    if not len(m_b) or 0 in [len(listx) for listx in m_b]:
        raise ValueError("m_b can't be empty")
    if any(False in x for x in [[isinstance(ele, (int, float))
                                 for ele in listx] for listx in m_a]):
        raise TypeError('m_a should contain only integers or floats')
    if any(False in x for x in [[isinstance(ele, (int, float))
                                 for ele in listx] for listx in m_b]):
        raise TypeError('m_b should contain only integers or floats')
    if len(set(len(listx) for listx in m_a)) > 1:
        raise TypeError('each row of m_a must should be of the same size')
    if len(set(len(listx) for listx in m_b)) > 1:
        raise TypeError('each row of m_b must should be of the same size')
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    return([[sum(a*b for a, b in
                 zip(colA, colB)) for colB in zip(*m_b)] for colA in m_a])
