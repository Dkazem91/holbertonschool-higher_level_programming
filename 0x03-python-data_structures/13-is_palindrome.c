#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - checks for list is palindrome
 * @head: head of linked list
 * Return:  boolean
 */
int is_palindrome(listint_t **head)
{
	int len = 0, i = 0;
	listint_t *tmp;
	int Ns[10000];

	tmp = *head;
	if ((*head) == NULL)
		return (1);
	while (tmp != NULL)
	{
		len++;
		tmp = tmp->next;
	}
	if (len == 1)
		return (1);
	tmp = *head;
	while (tmp != NULL)
	{
		Ns[i] = tmp->n;
		tmp = tmp->next;
		i++;
	}
	for (i = 0; i <= len / 2; i++)
	{
		if (Ns[i] != Ns[len - i - 1])
		{
			return (0);
		}
	}
	return (1);
}
