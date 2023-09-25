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
	Py_ssize_t size, list_count, i;
	const char *obj_type;

	size = ((PyVarObject *)p)->ob_size;
	list_count = ((PyListObject *)p)->allocated;
	fflush(stdout);
	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list_count);
	for (i = 0; i < size; i++)
	{
		obj_type = ((PyListObject *)p)->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, obj_type);
		if (strcmp(obj_type, "bytes") == 0)
			print_python_bytes(((PyListObject *)p)->ob_item[i]);
		else if (strcmp(obj_type, "float") == 0)
			print_python_float(((PyListObject *)p)->ob_item[i]);
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

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", ((PyBytesObject *)p)->ob_sval);
	if (((PyVarObject *)p)->ob_size >= 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;
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
	fflush(stdout);
	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	double value = ((PyFloatObject *)p)->ob_fval;

	printf("  value: %lf\n", value);
}
