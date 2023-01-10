#include <stdio.h>
#include <Python.h>

/**
 *  print_python_list_info - funtion name
 *  @p: pointer to a python object
 */
void print_python_list_info(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *element;

	size = Py_SIZE(P);
	printf("[*] Size of the Python List = %ld\n", size);

	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		element = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
	}
}
