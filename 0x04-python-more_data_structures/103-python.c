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
	
	Py_ssize_t size = ((PyVarObject *)p)->ob_size; // Get the size of the list
	Py_ssize_t i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);

	for (i = 0; i < size; i++)
	{
		PyObject *item = ((PyListObject *)p)->ob_item[i]; // Get the item at index i
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - prints python bytes
 * @p: Python object
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

	Py_ssize_t size = ((PyVarObject *)p)->ob_size; // Get the size of the bytes object
	Py_ssize_t i;

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", ((PyBytesObject *)p)->ob_sval);

	if (size > 10)
	{
		printf("  first 10 bytes: ");
		for (i = 0; i < 10; i++)
		{
			printf("%02x ", (unsigned char)((PyBytesObject *)p)->ob_sval[i]);
		}
		printf("\n");
	}
	else
	{
		printf("  first %ld bytes: ", size);
		for (i = 0; i < size; i++)
		{
			printf("%02x ", (unsigned char)((PyBytesObject *)p)->ob_sval[i]);
		}
		printf("\n");
	}
}

