#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: A singly-linked list.
 *
 * Return: 0if no cycle else 1
 */

int check_cycle(listint_t *list)
{
	listint_t *node, *next;

	if (!list)
		return (0);

	node = list;
	next = list->next;

	while (next)
	{
		if (next == next->next)
			return (1);
		while (node != next)
		{
			if (node == next->next)
				return (1);
			node = node->next;
		}
		node = list;
		next = next->next;
	}
	return (0);
}
