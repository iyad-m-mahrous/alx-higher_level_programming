#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 *
 * Return: Void
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	const char *type;

	if (!PyList_Check(p))
	{
		printf(" [ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_GET_SIZE(p);

	fflush(stdout);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);

	for (i = 0; i < size; i++)
	{
		type = Py_TYPE(PyList_GET_ITEM(p, i))->tp_name;
		printf("Element %ld: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(PyList_GET_ITEM(p, i));
		else if (strcmp(type, "float") == 0)
			print_python_float(PyList_GET_ITEM(p, i));
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 *
 * Return: Void
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;

	if (!PyBytes_Check(p))
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_GET_SIZE(p);

	fflush(stdout);

	printf("[.] bytes object info\n");
	printf(" size: %ld\n", size);
	printf(" trying string: %s\n", PyBytes_AS_STRING(p));

	if (size >= 10)
		size = 10;
	else
		size++;

	printf(" first %ld bytes: ", size);
	for (i = 0; i < size; i++)
		printf("%02hhx", PyBytes_AS_STRING(p)[i]);
	printf("\n");
}

/**
 * print_python_float - Prints basic info about Python float objects.
 * @p: A PyObject float object.
 *
 * Return: Void
 */
void print_python_float(PyObject *p)
{
	char *buffer = NULL;

	if (!PyFloat_Check(p))
	{
		printf(" [ERROR] Invalid Float Object\n");
		return;
	}

	fflush(stdout);

	printf("[.] float object info\n");
	printf(" value: %s\n", PyOS_double_to_string(PyFloat_AS_DOUBLE(p), 'r', 0,
				Py_DTSF_ADD_DOT_0, NULL));
}
