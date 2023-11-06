#include "lists.h"

/**
 * reverseList - Reverses a linked list
 * @head:  pointer to the head of the linked list
 *
 * Return: Pointer to the new head of the reversed list
 */
listint_t *reverseList(listint_t **head)
{
	listint_t *previouse = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = previouse;
		previouse = current;
		current = next;
	}

	*head = previouse;
	return (*head);
}

/**
 * compareLists - Compares two linked lists
 * @list1: Pointer to the head of the first list
 * @list2: Pointer to the head of the second list
 *
 * Return: 1 if the lists are identical, 0 otherwise
 */
int compareLists(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
			return (0);

		list1 = list1->next;
		list2 = list2->next;
	}

	return (list1 == NULL && list2 == NULL);
}

/**
 * is_palindrome - Checks if a linked list is a palindrome
 * @head: Double pointer to the head of the linked list
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev_slow = *head;
	listint_t *mid = NULL;
	listint_t *secondHalf = NULL;
	int palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (palindrome);
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}
	if (fast != NULL)
	{
		mid = slow;
		slow = slow->next;
	}
	secondHalf = slow;
	prev_slow->next = NULL;
	reverseList(&secondHalf);
	palindrome = compareLists(*head, secondHalf);
	reverseList(&secondHalf);
	if (mid != NULL)
	{
		prev_slow->next = mid;
		mid->next = secondHalf;
	}
	else
		prev_slow->next = secondHalf;
	return (palindrome);
}
