def zip_lists(a, b):
    a_current = a.head
    b_current = b.head

    if not a_current or not b_current:
        if b_current:
            return b
        if a_current:
            return a

    while a_current and b_current:
        if a_current or b_current:
            a.insert_after(a_current.value, b_current.value)
            a_current = a_current.next
            b_current = b_current.next
            if a_current.next:
                a_current = a_current.next

    print(b)
    return a

