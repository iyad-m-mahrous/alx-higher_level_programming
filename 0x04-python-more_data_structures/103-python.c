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
	printf("[*] Size of the Python List = %ld\n", ((PyListObject *)p)->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (Py_ssize_t i = 0; i < ((PyListObject *)p)->ob_base.ob_size; i++)
	{
		PyObject *item = ((PyListObject *)p)->ob_item[i];

		printf("Element %ld: %s\n", i,
			   Py_TYPE(item)->tp_name);
		if (!strcmp(Py_TYPE(item)->tp_name, "bytes"))
			print_python_bytes(item);
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
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);

	printf("  trying string: %s\n", PyBytes_AsString(p));

	printf("  first %ld bytes: ",
		   ((PyVarObject *)p)->ob_size + 1 < 11
		   ? ((PyVarObject *)p)->ob_size + 1 : 10);
	for (Py_ssize_t i = 0; i < 10 &&
			i <= ((PyVarObject *)p)->ob_size; i++)
	{
		printf("%02x", (unsigned char)PyBytes_AsString(p)[i]);
		if (i < ((PyVarObject *)p)->ob_size)
			printf(" ");
	}
	printf("\n");
}
