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
	Py_ssize_t size, list_alloc, i;
	const char *obj_type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	list_alloc = list->allocated;
	fflush(stdout);
	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list_alloc);
	for (i = 0; i < size; i++)
	{
		obj_type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, obj_type);
		if (strcmp(obj_type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
		else if (strcmp(obj_type, "float") == 0)
			print_python_float(list->ob_item[i]);
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

	PyBytesObject *bytes = (PyBytesObject *)p;

	size = Py_SIZE(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", PyBytes_AsString(p));

	if (size >= 10)
		size = 10;

	printf("  first %ld bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
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
	char *buffer = NULL;

	PyFloatObject *float_obj = (PyFloatObject *)p;

	fflush(stdout);
	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	buffer = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buffer);
	PyMem_Free(buffer);
}
