#include <Python.h>
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);


/**
 * print_python_bytes - prints Python bytes info
 * @p: Python object
 *
 * Return: None
 */
void print_python_bytes(PyObject *p)
{
        int i, size;
        PyBytesObject *bytes = (PyBytesObject *)p;

        printf("[.] bytes object info\n");
        if (strcmp(p->ob_type->tp_name, "bytes") != 0)
        {
                fprintf(stderr, "  [ERROR] Invalid Bytes Object\n");
                return;
        }

        printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
        printf("  trying string: %s\n", bytes->ob_sval);
	if (((PyVarObject *)p)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;
        printf("  first %d bytes: ", size);
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
 * print_python_list - prints Python list info
 * @p: Python object
 *
 * Return: None
 */
void print_python_list(PyObject *p)
{
	int size, allocation, i;
	const char *tpname;

	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	allocation = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocation);

	for (i = 0; i < size; i++)
	{
		tpname = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, tpname);
		if (strcmp(tpname, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
	}
}
