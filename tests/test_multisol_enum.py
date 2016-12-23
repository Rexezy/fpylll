from fpylll import IntegerMatrix, LLL, GSO
from fpylll import Enumeration

#
# A lattice with exactly 126 shortest vectors (non zero) of square length 48
# (note, maybe one should find only half of them because of negation
# symmetry elimination in enum)
#
# There are also 5286 non zero vectors of norm <= 80 (including the one of length 48)

AA = [(1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 1, 0, 0, 0, 0, 2077664, 58758639, -60836308),
      (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 736607, 128854488, -129591099),
      (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 1, 1, 0, 1, 6270701, 303352731, -309623439),
      (0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 2, 2956191, 103100471, -106056667),
      (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 3, 1094338, 319823711, -320918056),
      (0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 1, 0, 0, 2, 1572079, 338875225, -340447311),
      (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 5155388, 360557118, -365712508),
      (0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 8162869, 193281732, -201444604),
      (0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 1, 1, 0, 1, 3613941, 258239968, -261853919),
      (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 1, 1, 0, 0, 2, 6891515, 336608680, -343500203),
      (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 4813850, 386563464, -391377318),
      (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 1, 0, 1, 0, 3, 480602, 175051670, -175532280),
      (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 1, 1, 0, 0, 2, 4968059, 351667445, -356635511),
      (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9086805, 322136220, -331223027),
      (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 3565908, 41178307, -44744220),
      (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 357731, 257708976, -258066710),
      (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 261619, 193281732, -193543354),
      (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 7350140, 268766620, -276116764),
      (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 3, 6887608, 193281732, -200169345),
      (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 835472, 64427244, -65262719),
      (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 4668024, 327081548, -331749576),
      (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 3, 1536276, 386563464, -388099746),
      (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 3675412, 193281732, -196957148),
      (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 6760718, 64427244, -71187963),
      (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4668024, 322136220, -326804248),
      (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9203892, 128854488, -138058380),
      (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 450990708, -450990708)
      ]

n, m = 27, 28


def make_integer_matrix():
    A = IntegerMatrix(n, m)
    for i in range(n):
        for j in range(m):
            A[i, j] = AA[i][j]
    return A


def test_multisol():
    A = make_integer_matrix()
    m = GSO.Mat(A)
    lll_obj = LLL.Reduction(m)
    lll_obj()

    solutions = []
    solutions = Enumeration(m, nr_solutions=200).enumerate(0, 27, 48.5, 0)
    assert len(solutions)== 126 / 2
    for sol, _ in solutions:
        sol = IntegerMatrix.from_iterable(1, A.nrows, map(lambda x: int(round(x)), sol))
        sol = tuple((sol*A)[0])
        dist = sum([x**2 for x in sol])
        assert dist==48

    solutions = []
    solutions = Enumeration(m, nr_solutions=126 / 2).enumerate(0, 27, 100., 0)
    assert len(solutions)== 126 / 2
    for sol, _ in solutions:
        sol = IntegerMatrix.from_iterable(1, A.nrows, map(lambda x: int(round(x)), sol))
        sol = tuple((sol*A)[0])
        dist = sum([x**2 for x in sol])
        assert dist==48
