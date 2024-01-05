#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>  // Include any necessary standard libraries

/**
 * struct Node - A structure representing a node in a linked list
 * @data: The data stored in the node
 * @next: Pointer to the next node in the list
 */
typedef struct Node
{
    int data;
    struct Node *next;
} Node;

/* Function prototypes */
void print_list(const Node *head);
int pop_list(Node **head);
Node *add_node(Node **head, int data);
void free_list(Node *head);

#endif /* LISTS_H */

