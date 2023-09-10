#define PYTHON_H
#include <Python.h>
#include <stdio.h>
#include "lists.h"

/**
 * print_python_list_info -  prints some basic info about Python lists
 * @p: python objects pointer (list)
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	PyObject *item;
	Py_ssize_t l_size, i;

	l_size = PyList_Size(p);
	printf("[*] Size of the Python List = %zd\n", l_size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < l_size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
