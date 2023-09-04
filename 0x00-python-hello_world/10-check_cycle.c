#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: A singly-linked list.
 *
 * Return: 0if no cycle else 1
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list)
		return (0);

	slow = list;
	fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (fast == slow)
			return (1);
	}
	return (0);
}
