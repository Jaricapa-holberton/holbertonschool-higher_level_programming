#include "lists.h"
/**
 * len_list - Count the elements of the list.
 * @h: The head of the linked list.
 * Return: Size of the list.
 */
size_t len_list(listint_t *h)
{
	size_t len = 0;

	for (; h; h = h->next)
		len++;
	return (len);
}
/**
 * rev_list - Revert the direction of a single list.
 * @head: A pointer to the head of the linked list.
 * Return: A head of the reverted list.
 */
listint_t *rev_list(listint_t **head)
{
	listint_t *prev = NULL, *next = NULL, *current = NULL;

	for (current = *head; current;)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
	return (*head);
}
/**
 * is_palindrome - Check if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp, *half_rev, *tmp_rev;
	size_t len = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	tmp = *head;
	len = len_list(tmp);
	/*Go to the middle*/
	tmp = *head;
	for (i = 0; i < (len / 2) - 1; i++)
		tmp = tmp->next;
	/*If the the list has exact middle: Compare the next node*/
	if ((len % 2) == 0 && tmp->n != tmp->next->n)
		return (0);
	tmp = tmp->next->next;
	/*"Reverse the second middle of the list*/
	half_rev = rev_list(&tmp);
	tmp_rev = half_rev;
	/*Compare the two middles*/
	for (tmp = *head; half_rev;)
	{
		if (tmp->n != half_rev->n)
			return (0);
		tmp = tmp->next;
		half_rev = half_rev->next;
	}
	rev_list(&tmp_rev);
	return (1);
}
