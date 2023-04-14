#include<stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
 };
 
struct ListNode* createNode(int val) {
    struct ListNode *node = (struct ListNode *) malloc(sizeof(struct ListNode));
    node->val = val;
    node->next = NULL;
    return node;
}

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    int carry = 0;
    struct ListNode *head = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode *current = head;

    while (l1 != NULL && l2 != NULL)
    {
        int sum = carry + l1->val + l2->val;
        carry = sum / 10;
        struct ListNode *new_node = createNode(sum % 10);
        current->next = new_node;
        current = current->next;
        l1 = l1->next;
        l2 = l2->next; 
    }

    while (l1 != NULL)
    {
        int sum = carry + l1->val;
        carry = sum / 10;
        struct ListNode *new_node = createNode(sum % 10);
        current->next = new_node;
        current = current->next;
        l1 = l1->next;
    }

    while (l2 != NULL)
    {
        int sum = carry + l2->val;
        carry = sum / 10;
        struct ListNode *new_node = createNode(sum % 10);
        current->next = new_node;
        current = current->next;
        l2 = l2->next;
    }

    if (carry == 1)
        current->next = createNode(1);

    return head->next;
}

int main(){
    struct ListNode *l1[3], *l2[3];

    for (int i = 0; i < 3; i++)
    {
        l1[i] = createNode(i);
        l2[i] = createNode(i);
    }

    for (int i = 0; i < 2; i++)
        {
            l1[i]->next = l1[i + 1];
            l2[i]->next = l2[i + 1];
        }

    struct ListNode* head = addTwoNumbers(*l1, *l2);
    struct ListNode* current = head;
    // print the values in the linked list
    while(current != NULL){
        printf("%d\n", current->val);
        current = current->next;
    }

    // free the allocated memory
    for (int i = 0; i < 3; i++)
    {
        free(l1[i]);
        free(l2[i]);
    }
    free(head);
    return 0;
} 