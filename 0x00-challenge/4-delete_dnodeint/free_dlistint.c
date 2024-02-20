
#include <string.h>
#include <stdlib.h>
#include "lists.h"

/**
 * free_dlistint - It frees a list
 *
 * @head: A reference to initial element of the list
 */
void free_dlistint(dlistint_t *head)
{
	dlistint_t *node;

	while (head)
	{
		node = head;
		head = head->next;
		free(node);
	}
}
