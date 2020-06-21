def has_cycle(head):
    if not head:
        return 0
    cur = head
    data = []
    while(True):
        if not cur.next:
            return 0
        if cur.data in data:
            return 1
        data.append(cur.data)
        cur = cur.next
    return 0
