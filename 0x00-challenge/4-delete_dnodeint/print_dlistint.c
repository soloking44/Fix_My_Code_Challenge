#include <stdio.h>
#include "lists.h"

/**
 * print_dlistint - It displays a doubly linkedlist of integers
 *
 * @h: A reference to initial element of a list
 *
 * Return: The value of element displayed
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t n;

	n = 0;
	while (h)
	{
		printf("%d\n", h->n);
		h = h->next;
		n++;
	}
	return (n);
}
