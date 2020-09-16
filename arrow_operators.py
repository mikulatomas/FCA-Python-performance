def up_skip_256(input_set, context):
    result = context._Attributes.supremum
    i = 0

    while i < len(context.rows):
        if input_set:
            if not input_set & 115792089237316195423570985008687907853269984665640564039457584007913129639935:
                input_set >>= 256
                i += 256
                continue

            if not input_set & 340282366920938463463374607431768211455:
                input_set >>= 128
                i += 128
                continue

            if not input_set & 18446744073709551615:
                input_set >>= 64
                i += 64
                continue

            if not input_set & 4294967295:
                input_set >>= 32
                i += 32
                continue

            if not input_set & 65535:
                input_set >>= 16
                i += 16
                continue

            if not input_set & 255:
                input_set >>= 8
                i += 8
                continue

            if not input_set & 15:
                input_set >>= 4
                i += 4
                continue

            if input_set & 1:
                result &= context.rows[i]

            input_set >>= 1
            i += 1
        else:
            break

    return context._Attributes.fromint(result)


def up_skip_128(input_set, context):
    result = context._Attributes.supremum
    i = 0

    while i < len(context.rows):
        if input_set:

            if not input_set & 340282366920938463463374607431768211455:
                input_set >>= 128
                i += 128
                continue

            if not input_set & 18446744073709551615:
                input_set >>= 64
                i += 64
                continue

            if not input_set & 4294967295:
                input_set >>= 32
                i += 32
                continue

            if not input_set & 65535:
                input_set >>= 16
                i += 16
                continue

            if not input_set & 255:
                input_set >>= 8
                i += 8
                continue

            if not input_set & 15:
                input_set >>= 4
                i += 4
                continue

            if input_set & 1:
                result &= context.rows[i]

            input_set >>= 1
            i += 1
        else:
            break

    return context._Attributes.fromint(result)


def up_skip_64(input_set, context):
    result = context._Attributes.supremum
    i = 0

    while i < len(context.rows):
        if input_set:

            if not input_set & 18446744073709551615:
                input_set >>= 64
                i += 64
                continue

            if not input_set & 4294967295:
                input_set >>= 32
                i += 32
                continue

            if not input_set & 65535:
                input_set >>= 16
                i += 16
                continue

            if not input_set & 255:
                input_set >>= 8
                i += 8
                continue

            if not input_set & 15:
                input_set >>= 4
                i += 4
                continue

            if input_set & 1:
                result &= context.rows[i]

            input_set >>= 1
            i += 1
        else:
            break

    return context._Attributes.fromint(result)


def up_skip_32(input_set, context):
    result = context._Attributes.supremum
    i = 0

    while i < len(context.rows):
        if input_set:
            if not input_set & 4294967295:
                input_set >>= 32
                i += 32
                continue

            if not input_set & 65535:
                input_set >>= 16
                i += 16
                continue

            if not input_set & 255:
                input_set >>= 8
                i += 8
                continue

            if not input_set & 15:
                input_set >>= 4
                i += 4
                continue

            if input_set & 1:
                result &= context.rows[i]

            input_set >>= 1
            i += 1
        else:
            break

    return context._Attributes.fromint(result)


def up_skip_16(input_set, context):
    result = context._Attributes.supremum
    i = 0

    while i < len(context.rows):
        if input_set:

            if not input_set & 65535:
                input_set >>= 16
                i += 16
                continue

            if not input_set & 255:
                input_set >>= 8
                i += 8
                continue

            if not input_set & 15:
                input_set >>= 4
                i += 4
                continue

            if input_set & 1:
                result &= context.rows[i]

            input_set >>= 1
            i += 1
        else:
            break

    return context._Attributes.fromint(result)


def up_skip_8(input_set, context):
    result = context._Attributes.supremum
    i = 0

    while i < len(context.rows):
        if input_set:
            if not input_set & 255:
                input_set >>= 8
                i += 8
                continue

            if not input_set & 15:
                input_set >>= 4
                i += 4
                continue

            if input_set & 1:
                result &= context.rows[i]

            input_set >>= 1
            i += 1
        else:
            break

    return context._Attributes.fromint(result)


def up_skip_4(input_set, context):
    result = context._Attributes.supremum
    i = 0

    while i < len(context.rows):
        if input_set:
            if not input_set & 15:
                input_set >>= 4
                i += 4
                continue

            if input_set & 1:
                result &= context.rows[i]

            input_set >>= 1
            i += 1
        else:
            break

    return context._Attributes.fromint(result)


def up_skip_1(input_set, context):
    result = context._Attributes.supremum
    i = 0

    while i < len(context.rows):
        if input_set:
            if input_set & 1:
                result &= context.rows[i]

            input_set >>= 1
            i += 1
        else:
            break

    return context._Attributes.fromint(result)
