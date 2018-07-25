from playLA.Vector import Vector

if __name__ == "__main__":

    vec = Vector([5, 2])
    print(vec)
    print("len(vec) = {}".format(len(vec)))
    print("vec[0] = {}, vec[1] = {}".format(vec[0], vec[1]))

    vec2 = Vector([3, 1])
    print("{} + {} = {}".format(vec, vec2, vec + vec2))
    print("{} - {} = {}".format(vec, vec2, vec - vec2))

    print("{} * {} = {}".format(vec, 3, vec * 3))
    print("{} * {} = {}".format(3, vec, 3 * vec))

    print("+{} = {}".format(vec, +vec))
    print("-{} = {}".format(vec, -vec))

    print("norm({}) = {}".format(vec, vec.norm()))
    print("norm({}) = {}".format(vec2, vec2.norm()))

    print("normalize {} is {}".format(vec, vec.normalize()))
    print("normalize {} is {}".format(vec2, vec2.normalize()))

    print(vec.normalize().norm())
    O_vector = Vector([0., 0., 0.])
    try:
        O_vector.normalize()
    except ZeroDivisionError:
        print("Cannot normalize zero vector.")

    print(vec.dot(vec2))
    print(vec @ vec2)

    e1 = Vector([0, 1])
    e2 = Vector([1, 0])
    print(e1 @ e2)