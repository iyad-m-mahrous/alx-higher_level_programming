#include "lists.h"

/**
 * mid_list - get the middle of the linked list
 * @head: pointer to the linked list head
 *
 * Return: address of the middle linked list item
 */

listint_t *mid_list(listint_t *head)
{
	listint_t *slow, *fast;

	slow = head;
	fast = head;
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	return (slow->next);
}

/**
 * reverse_list - reversing a list
 * @head: linked list to be reversed
 *
 * Return: pointer to the reversed list
 */

listint_t *reverse_list(listint_t *head)
{
	listint_t *temp, *new, *old;

	old = head;
	new = NULL;

	while (old)
	{
		temp = old;
		old = old->next;
		temp->next = new;
		new = temp;
	}
	return (new);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to the linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *mid, *rev, *t_head;

	if (*head == NULL)
		return (1);
	mid = mid_list(*head);
	rev = reverse_list(mid);
	t_head = *head;
	while (rev)
	{
		if (t_head->n != rev->n)
			return (0);
		t_head = t_head->next;
		rev = rev->next;
	}
	return (1);
}
