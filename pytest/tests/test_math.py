import pytest

from mathematics import *


@pytest.fixture(name="nums")
def nums():
    return [6, 3]

@pytest.fixture(name="num")
def num():
    return 16

@pytest.fixture(name="num_cbrt")
def num_cbrt():
    return 216

@pytest.mark.valids
@pytest.mark.mdas
@pytest.mark.increases
@pytest.mark.adds
def test_valid_add_nums(nums):
    a = nums[0]
    b = nums[1]
    assert add_nums(a,b) == 9


@pytest.mark.invalids
@pytest.mark.mdas
@pytest.mark.increases
@pytest.mark.adds
def test_invalid_add_nums(nums):
    a = nums[0]
    b = nums[1]
    assert add_nums(a,b) != 10


@pytest.mark.valids
@pytest.mark.mdas
@pytest.mark.decreases
@pytest.mark.subtracts
def test_valid_subtract_nums(nums):
    a = nums[0]
    b = nums[1]
    assert subtract_nums(a,b) == 3


@pytest.mark.invalids
@pytest.mark.mdas
@pytest.mark.decreases
@pytest.mark.subtracts
def test_invalid_subtract_nums(nums):
    a = nums[0]
    b = nums[1]
    assert subtract_nums(a,b) != 2


@pytest.mark.valids
@pytest.mark.mdas
@pytest.mark.increases
@pytest.mark.multiplies
def test_valid_multiply_nums(nums):
    a = nums[0]
    b = nums[1]
    assert multiply_nums(a,b) == 18


@pytest.mark.invalids
@pytest.mark.mdas
@pytest.mark.increases
@pytest.mark.multiplies
def test_invalid_multiply_nums(nums):
    a = nums[0]
    b = nums[1]
    assert multiply_nums(a,b) != 12


@pytest.mark.valids
@pytest.mark.decreases
@pytest.mark.mdas
@pytest.mark.divides
def test_valid_divide_nums(nums):
    a = nums[0]
    b = nums[1]
    assert divide_nums(a,b) == 2


@pytest.mark.invalids
@pytest.mark.decreases
@pytest.mark.mdas
@pytest.mark.divides
def test_invalid_divide_nums(nums):
    a = nums[0]
    b = nums[1]
    assert divide_nums(a,b) != 1


@pytest.mark.valids
@pytest.mark.exponents
@pytest.mark.increases
@pytest.mark.squares
def test_valid_square_num(num):
    assert square_num(num) == 256


@pytest.mark.invalids
@pytest.mark.exponents
@pytest.mark.increases
@pytest.mark.squares
def test_invalid_square_num(num):
    assert square_num(num) != 25


@pytest.mark.valids
@pytest.mark.exponents
@pytest.mark.increases
@pytest.mark.sqrts
def test_valid_sqrt_num(num):
    assert sqrt_num(num) == 4


@pytest.mark.invalids
@pytest.mark.exponents
@pytest.mark.increases
@pytest.mark.sqrts
def test_invalid_sqrt_num(num):
    assert sqrt_num(num) != 5


@pytest.mark.valids
@pytest.mark.exponents
@pytest.mark.increases
@pytest.mark.cubes
def test_valid_cube_num(num):
    a = nums[0]
    assert cube_num(num) == 4096


@pytest.mark.invalids
@pytest.mark.exponents
@pytest.mark.increases
@pytest.mark.cubes
def test_invalid_cube_num(num):
    assert cube_num(num) != 729


@pytest.mark.valids
@pytest.mark.exponents
@pytest.mark.increases
@pytest.mark.cbrts
def test_valid_cbrt_num(num_cbrt):
    assert cbrt_num(num_cbrt) == 6


@pytest.mark.invalids
@pytest.mark.exponents
@pytest.mark.increases
@pytest.mark.cbrts
def test_invalid_cbrt_num(num_cbrt):
    assert cbrt_num(num_cbrt) != 5
