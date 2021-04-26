#include "lists.h"

/**
 * check_cycle - Detect a loop in a linked list.
 * @list: Head of the list.
 * Return: 1 if there is a loop, on the contrary 0.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	for (; slow && fast && fast->next;)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
