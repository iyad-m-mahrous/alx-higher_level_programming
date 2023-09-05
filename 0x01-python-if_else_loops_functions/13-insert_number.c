#include "lists.h"


/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: head of the linked list
 * @number: to be added
 *
 * Return: address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *pre, *after;

	new = malloc(sizeof(*new));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (!head || !(*head))
	{
		head = &new;
		return (new);
	}
	after = *head;
	while (after->next && (after->n < number))
	{
		pre = after;
		after = after->next;
	}
	if (after->n > number)
	{
		pre->next = new;
		new->next = after;
	}
	else
		after->next = new;
	return (new);
}
