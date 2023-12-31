#include "lists.h"

/**
 * insert_node - adds a new node to a sorted linked list
 *
 * @head: pointer to the head of the linked list
 * @number: number to add to new node
 *
 * Return: address of new element
 * return NULL if failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr, *prev, *new_node = malloc(sizeof(listint_t));

	if (head == NULL || new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}

	if (number <= (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	curr = (*head)->next;
	prev = *head;

	while (curr)
	{
		if (curr->n >= number)
		{
			new_node->next = curr;
			prev->next = new_node;
			return (new_node);
		}
		prev = curr;
		curr = curr->next;
	}

	prev->next = new_node;
	return (new_node);
}
