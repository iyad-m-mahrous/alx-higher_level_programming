#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - prints Python list info
 * @p: Python object (list)
 *
 * Return: None
 */
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		fprintf(stderr, "[*] Python list info\n");
		fprintf(stderr, "  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", PyList_GET_SIZE(p));

	for (Py_ssize_t i = 0; i < PyList_GET_SIZE(p); i++)
	{
		printf("Element %ld: %s\n", i,
			   Py_TYPE(PyList_GetItem(p, i))->tp_name);
		if (!strcmp(Py_TYPE(PyList_GetItem(p, i))->tp_name, "bytes"))
			print_python_bytes(PyList_GetItem(p, i));
	}
}

/**
 * print_python_bytes - prints Python bytes info
 * @p: Python object (bytes)
 *
 * Return: None
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		printf("[.] bytes object info\n");
		fprintf(stderr, "  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", PyBytes_GET_SIZE(p));

	printf("  trying string: %s\n", PyBytes_AsString(p));

	printf("  first %ld bytes: ",
		   PyBytes_GET_SIZE(p) + 1 < 11 ? PyBytes_GET_SIZE(p) + 1 : 10);
	for (Py_ssize_t i = 0; i < 10 && i <= PyBytes_GET_SIZE(p); i++)
	{
		printf("%02x", (unsigned char)PyBytes_AsString(p)[i]);
		if (i < PyBytes_GET_SIZE(p))
			printf(" ");
	}
	printf("\n");
}

