#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    void insertNode(ListNode **root, ListNode *newNode) {
        if (*root == 0)
            *root = newNode;
        else {
            ListNode *header = *root;   
            while (header->next != 0)
                header = header->next;
            header->next = newNode;
        }

        newNode->next = 0;
    }

    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode mergedList;
        ListNode *head = &mergedList;
        
        while (l1 != 0 && l2 != 0)
        {   
            if (l1->val < l2->val) {
                head->next = l1;
                l1 = l1->next;
            }
            else {
                head->next = l2;
                l2 = l2->next;
            }
            head = head->next;
        } 
            
        if (l1 == 0) 
            head->next = l2;
        else 
            head->next = l1;
            
        return mergedList.next;
    }

    void traverse(ListNode *root) {
        if (root == 0)
            cout << "list is empty" << endl;
        while (root != 0)
        {
            cout << root->val << ' ';
            root = root->next;
        }
    }
};

int main() {
    ListNode *l1root = 0;
    ListNode *l1n1 = new ListNode(1);
    ListNode *l1n2 = new ListNode(5);
    ListNode *l1n3 = new ListNode(7);

    ListNode *l2root = 0;
    ListNode *l2n1 = new ListNode(2);
    ListNode *l2n2 = new ListNode(4);
    ListNode *l2n3 = new ListNode(6);

    Solution s = Solution();

    s.insertNode(&l1root, l1n1);
    s.insertNode(&l1root, l1n2);
    s.insertNode(&l1root, l1n3);
    s.insertNode(&l2root, l2n1);
    s.insertNode(&l2root, l2n2);
    s.insertNode(&l2root, l2n3);

    ListNode *mergedList = s.mergeTwoLists(l1root, l2root);

    s.traverse(mergedList);
    return 0;
}
