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
	printf("[*] Size of the Python List = %ld\n", ((PyVarObject *)p)->ob_size);

	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (Py_ssize_t i = 0; i < ((PyVarObject *)p)->ob_size; i++)
	{
		printf("Element %ld: %s\n", i,
			   ((PyObject *)((PyListObject *)p)->ob_item[i])->ob_type->tp_name);
		if (!strcmp(Py_TYPE(((PyListObject *)p)->ob_item[i])->tp_name, "bytes"))
			print_python_bytes(((PyObject *)((PyListObject *)p)->ob_item[i]));
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
	printf("  trying string: %s\n", ((PyBytesObject *)p)->ob_sval);

	printf("  first %ld bytes: ",
		       ((PyVarObject *)p)->ob_size + 1 >
		      10 ? 10 : ((PyVarObject *)p)->ob_size + 1);
	for (Py_ssize_t i = 0; i < 10 && i <= ((PyVarObject *)p)->ob_size; i++)
	{
		printf("%02x", (unsigned char)(((PyBytesObject *)p)->ob_sval[i]));
		if (i < ((PyVarObject *)p)->ob_size)
			printf(" ");
	}
	printf("\n");
}

