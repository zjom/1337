from arr import DynamicArray


def test_arr():
    arr = DynamicArray(1)
    assert arr.getSize() == 0
    assert arr.getCapacity() == 1

    arr.pushback(1)
    assert arr.getSize() == 1
    assert arr.getCapacity() == 1

    arr.pushback(2)
    assert arr.getSize() == 2
    assert arr.getCapacity() == 2
    assert arr.get(1) == 2

    arr.set(1, 3)
    assert arr.get(1) == 3

    assert arr.popback() == 3
    assert arr.getSize() == 1
    assert arr.getCapacity() == 2
