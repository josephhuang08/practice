#include <iostream>
#include <string>
using namespace std;

class Node {
    public:
    int Val;
    Node *Next; 

    Node(int val) {
        Val = val;
    }
};

class LinkedList {
    public:
    Node *Root = 0;

    void insertToStart(int val) {
        Node *n = new Node(val);
        n->Next = Root;
        Root = n;
    }

    void insertToEnd(int val) {
        Node *n = new Node(val);
        n->Next = 0;

        if (Root == 0) 
            Root = n;
        else {
            Node *header = Root;
            while (header->Next != 0)
                header = header->Next;
            header->Next = n;
        }
    }

    void insertAfterX(int x, int val) {
        Node *n = new Node(val);
        Node *header = Root;

        while (header != 0 && header->Val != x)
            header = header->Next;

        if (header == 0)
            cout << x << " is not in linked list" << endl; 
        else {
            n->Next = header->Next;
            header->Next = n;
        }
    }

    void insertBeforeX(int x, int val) {
        if (Root != 0 && Root->Val == x) {
            insertToStart(val);
            return;
        }
        Node *n = new Node(val);
        Node *header = Root;
        Node *prev;

        while (header !=0 && header->Val != x) {
            prev = header;
            header = header->Next;
        }

        if (header == 0)
            cout << x << " is not in linked list" << endl; 
        else {
            n->Next = header;
            prev->Next = n; 
        }
    }

    void insertAtIndex(int x, int val) { 
        if (x == 0) {
            insertToStart(val);
            return;
        }
        
        Node *n = new Node(val);
        Node *header = Root;
        Node *prev;
        int i;

        for (i = 0; i < x && header != 0; i++) {
            prev = header;
            header = header->Next;
        }

        if (i < x)
            cout << "index out of bound" << endl;
        else {
            n->Next = header;
            prev->Next = n;
        }
    }

    bool search(int x) {
        Node *header = Root;

        while (header != 0) {
            if (header->Val == x)
                return true;
            header = header->Next;
        }
        return false;
    }

    int length() {
        Node *header = Root;
        int count = 0;
        while (header != 0) {
            header = header->Next;
            count++;
        }

        return count;
    }

    void deleteX(int x) {
        if (Root->Val == x) {
            Root = Root->Next;
            return;
        }

        Node *header = Root;
        Node *prev;

        while (header != 0 && header->Val != x) {
            prev = header;
            header = header->Next;
        }

        if (header == 0)
            cout << x << " is not in linked list" << endl;
        else 
            prev->Next = header->Next;
    }

    void reverse() {
        Node *header = Root;
        Node *prev = 0;
        Node *next;

        while (header != 0) {
            next = header->Next;
            header->Next = prev;
            prev = header;
            header = next;
        }
        Root = prev;
    }

    void traverse() {
        Node *header = Root;
        while (header != 0) {
            cout << header->Val << ' ';
            header = header->Next;
        }
        cout << '\n';
    }
};

int main() {
    LinkedList mylist = LinkedList();

    mylist.insertToEnd(1);
    mylist.insertToEnd(2);
    mylist.insertToEnd(5);
    mylist.insertToEnd(7);
    mylist.insertToEnd(10);

    mylist.reverse();
    mylist.traverse();
    return 0;
}