#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - prints python list
 * @p: Python object
 *
 * Return: None
 */

void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf("[*] Python list info\n");
		fprintf(stderr, "  [ERROR] Invalid List Object\n");
		return;
	}
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n", i
				, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}

/**
 * print_python_bytes - prints python bytes
 * @p: Python object
 *
 * Retuen: None
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		printf("[.] bytes object info\n");
		fprintf(stderr, "  [ERROR] Invalid Bytes Object\n");
		return;
	}
	Py_ssize_t size = PyBytes_Size(p);
	Py_ssize_t i;

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", PyBytes_AsString(p));
	if (size > 10)
	{
		printf("  first 10 bytes: ");
		for (i = 0; i < 10; i++)
		{
			printf("%02x ", (unsigned char)PyBytes_AsString(p)[i]);
		}
		printf("\n");
	}
	else
	{
		printf("  first %ld bytes: ", size);
		for (i = 0; i < size; i++)
		{
			printf("%02x ", (unsigned char)PyBytes_AsString(p)[i]);
		}
		printf("\n");
	}
}

