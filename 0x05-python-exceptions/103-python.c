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
	const char *obj_type;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		PyErr_SetString(PyExc_TypeError, "Invalid List Object");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *element = ((PyListObject *)p)->ob_item[i];

		obj_type = element->ob_type->tp_name;
		printf("Element %ld: %s\n", i, obj_type);
		if (strcmp(obj_type, "bytes") == 0)
			print_python_bytes(element);
		else if (strcmp(obj_type, "float") == 0)
			print_python_float(element);
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

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		PyErr_SetString(PyExc_TypeError, "Invalid Bytes Object");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", ((PyBytesObject *)p)->ob_sval);

	if (size >= 10)
		size = 10;

	printf("  first %ld bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", ((PyBytesObject *)p)->ob_sval[i]);
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - Prints basic info about Python float objects.
 * @p: A PyObject float object.
 *
 * Return: Void
 */
void print_python_float(PyObject *p)
{
	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		PyErr_SetString(PyExc_TypeError, "Invalid Float Object");
		return;
	}

	double value = ((PyFloatObject *)p)->ob_fval;

	printf("  value: %f\n", value);
}

