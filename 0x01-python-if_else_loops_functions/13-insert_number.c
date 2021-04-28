#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: balbla
 * @number: balblab
 * Return: return next node
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = NULL;
	listint_t *new_node = NULL;

	/* Check if exist the head */
	if (!head)
		return (NULL);
	/* Create new node*/
	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	/* Check the split node */
	tmp = *head;
	/* Insert node in the list */
	if (!tmp || tmp->n >= number)
	{
		new_node->next = tmp;
		*head = new_node;
		return (new_node);
	}
	for (; tmp->next && tmp->next->n < number;)
	{
		tmp = tmp->next;
	}
	new_node->next = tmp->next;
	tmp->next = new_node;
	return (tmp->next);
}
