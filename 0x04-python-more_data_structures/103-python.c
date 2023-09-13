#include <Python.h>

void print_python_bytes(PyObject *p)
{
	printf("[.] bytes object info\n");
	if (!PyObject_IsInstance(p, (PyObject *)&PyBytes_Type))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytesObject *bytes_obj = (PyBytesObject *)p;
	Py_ssize_t size = Py_SIZE(bytes_obj);

	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", bytes_obj->ob_sval);

	printf("  first %zd bytes: ", (size + 1 < 10 ? size + 1 : 10));
	for (Py_ssize_t i = 0; i < (size + 1 < 10 ? size + 1 : 10); i++)
	{
		printf("%02x", (unsigned char)bytes_obj->ob_sval[i]);
		if (i < (size < 9 ? size : 9))
			printf(" ");
		else
			printf("\n");
	}
}

void print_python_list(PyObject *p)
{
	printf("[*] Python list info\n");
	if (!PyObject_IsInstance(p, (PyObject *)&PyList_Type))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	PyListObject *list_obj = (PyListObject *)p;
	Py_ssize_t size = Py_SIZE(list_obj);
	Py_ssize_t allocated = list_obj->allocated;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		printf("Element %zd: ", i);
		PyObject *element = list_obj->ob_item[i];

		if (PyObject_IsInstance(element, (PyObject *)&PyBytes_Type))
		{
			printf("bytes\n");
			print_python_bytes(element);
		}
		else if (PyLong_Check(element))
		{
			printf("int\n");
		}
		else if (PyFloat_Check(element))
		{
			printf("float\n");
		}
		else if (PyTuple_Check(element))
		{
			printf("tuple\n");
		}
		else if (PyObject_IsInstance(element, (PyObject *)&PyList_Type))
		{
			printf("list\n");
		}
		else if (PyUnicode_Check(element))
		{
			printf("str\n");
		}
		else
		{
			printf("[ERROR] Unknown Object Type\n");
		}
	}
}

