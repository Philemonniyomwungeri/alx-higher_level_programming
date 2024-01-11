#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>

/* Structure definition for a linked list node */
typedef struct Node {
    int data;
    struct Node* next;
} Node;

/* Function prototypes */
Node* createNode(int data);
void freeList(Node* head);
void printList(Node* head);

#endif /* LISTS_H */

