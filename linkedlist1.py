class LinkedList:
    def __init__(self):
        self.head = None
        self.previous = None
        pass

    def insert(self, element, pos):
        """
            Insert an element into this list
            element: The element to insert
            pos: The position to insert (0 being the start)
            return: The modified LinkedList
            raise: IndexError if pos is outside of the list
        """
        if pos < 0:
          raise IndexError("position cannot be negative")
        
        if pos == 0:
          element.next = self.head
          if self.head:
            self.head.previous = element
          self.head = element
          return self

        current = self.head
        index = 0

        while current and index < pos - 1:
          current = current.next
          index += 1

        element.next = current.next
        if current.next:
          current.next.previous = element
        current.next = element
        element.previous = current

        return self


    def remove(self, pos):
        """
            Remove an element from this list
            pos: The position of the element to remove
            returns: The modified LinkedList
            raise: IndexError if pos is outside of the list
        """
        if pos < 0:
            raise IndexError("Error")

        if pos == 0:
            if not self.head:
                raise IndexError("IndexError, pos is outside of the list")
            self.head = self.head.next
            if self.head:
                self.head.previous = None
            return self.head

        current = self.head
        index = 0

        while current and index < pos -1:
            current = current.next
            index += 1
        if current or current.next is None:
            raise IndexError("IndexError, pos is outside of the list")

        to_remove = current.next
        current.next = to_remove.next
        if to_remove.next:
            to_remove.next.previous = current

        return self


    def find(self, value):
        """
            Find an element in this list
            value: The value of the element to find
            returns: The position of the first occurrence of such an element or -1 if not found
        """
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1


    def __getitem__(self, pos):
        """
            Return an element at a specific position in the list
            pos: The position of the element to return (0 being the first)
            return: The element 
            raise: IndexError if pos is outside of the list
        """
        if pos < 0:
            raise IndexError("pos cannot be negative ")

        current = self.head
        index = 0

        while current:
            if index == pos:
                return current 
            current = current.next
            index += 1
        raise IndexError(" pos is outside of the list")


class LinkedListElement:
    # Pointer to next element in LinkedList
    next = None
    
    # Pointer to previous element in LinkedList
    previous = None

    def __init__(self, value):
        """
            Create a new LinkedListElement with value "value"
        """
        self.value = value
        self.next  = None
        self.previous = None

    def remove(self):
        """
            Remove this item from a LinkedList
        """
        if self.previous:
            self.previous.next = self.next
        if self.next:
            self.next.previous = self.previous

    def insert(self, element):
        """
            Insert an element after this element
            element: The element to insert
        """
        element.next = self.next
        element.previous = self
        if self.next:
            self.next.previous = element
        self.next = element


if __name__ == "__main__":
    # Create a new LinkedList
    l = LinkedList()


    # Create a new LinkedListElement
    e1 = LinkedListElement(23)
    assert e1.value == 23, "LinkedListElement e1 does have the wrong value."


    # Insert LinkedListElement to beginning of l
    l.insert(e1, 0)

    assert l.find(23) >= 0, "Cannot find element with value '23' in l"
    assert l[0] == e1, "Element l[0] is not e1"

    # Insert another LinkedListElement at the start
    e2 = LinkedListElement(42)
    l.insert(e2, 0)
    assert l.find(42) >= 0, "Cannot find element with value '42' in l"
    assert l[0] == e2, "Element l[0] is not e2"
    assert l[1] == e1, "Element l[1] is not e1"

    # Remove e1 from LinkedList
    e1.remove()
    assert l.find(42) >= 0, "Cannot find element with value '42' in l"
    assert l.find(23) < 0, "Element with value '23' is still in l"
    assert l[0] == e2, "Element l[0] is not e2"
    try:
        assert l[1] == e1
    except IndexError:
        pass
    else:
        raise RuntimeError("Reading out of bounds should raise IndexError!")
