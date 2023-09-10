#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info -  prints some basic info about Python lists
 * @p: python objects pointer (list)
 *
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	PyObject *item;
	long int l_size, i;

	l_size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", l_size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < l_size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
