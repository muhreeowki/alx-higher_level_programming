#include <stdio.h>
#include <Python.h>
#include <listobject.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 *
 * @p: python object
 */
void print_python_list_info(PyObject *p)
{
	int size, i;
	PyListObject *list;
	PyObject *item;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);

	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
