#include "lists.h"
/**
 * check_cycle - checks is a list has a cycle or not
 * @list: list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *listcpy1, *listcpy2;

	if (list == NULL || list->next == NULL)
		return (0);

	listcpy1 = list;
	listcpy2 = list;
	listcpy1 = listcpy1->next;
	listcpy2 = listcpy2->next->next;
	while (listcpy2)
	{
		if (listcpy1 == listcpy2)
			return (1);
		listcpy1 = listcpy1->next;
		listcpy2 = listcpy2->next->next;
	}
	return (0);
}
