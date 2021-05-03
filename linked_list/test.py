from dataclasses import dataclass@dataclassclass Element:    value: int    next: any = None@dataclassclass LinkedList:    head: any = None    def append(self, new_element):        current = self.head        if self.head:            while current.next:                current = current.next            current.next = new_element        else:            self.head = new_element    def get_position(self, position):        """Get an element from a particular position.             Assume the first position is "1".             Return "None" if position is not in the list."""        current = self.head        counter = 1        if position < 1:            return None        while current and counter <= position:            if counter == position:                return current            current = current.next            counter += 1        return None    def insert(self, new_element, position):        counter = 1        current = self.head        if position < 1:            return None        elif position == 1:            new_element.next = self.head            self.head = new_element        else:            while current and counter < position:                if counter == position - 1:                    new_element.next = current.next                    current.next = new_element                current = current.next                counter += 1    def delete(self, value):        current = self.head        previous = None        while current.value != value and current.next:            previous = current            current = current.next        if current.value == value:            if previous:                previous.next = current.next            else:                self.head = current.nextif __name__ == '__main__':    e1 = Element(1)    e2 = Element(2)    e3 = Element(3)    e4 = Element(4)    ll = LinkedList(e1)    # print(ll)    ll.append(e2)    # print('====>', ll)    ll.append(e3)    #    print(ll.head.next.next.value)    print('>>>>>>', ll.get_position(3))    #    ll.insert(e4, 3)    #    print('-------<><>>>', ll.head)    print('-------<><><>', ll.get_position(3))    print('-------<><><>', ll.get_position(4))    #    ll.delete(1)    print(ll.get_position(1))    print(ll.get_position(2).value)    print(ll.get_position(3).value)