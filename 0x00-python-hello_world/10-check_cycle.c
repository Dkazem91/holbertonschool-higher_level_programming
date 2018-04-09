#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - checks for cycles in loop
 * @list: list to take in
 * Return: integer value
 */
int check_cycle(listint_t *list)
{
	listint_t *first, *second;

	first = list;
	second = list;
	while (first != NULL && second != NULL)
	{
		first = first->next;
		if (second->next)
			second = second->next->next;

		if (first == second)
			return (1);
	}
	return (0);
}
