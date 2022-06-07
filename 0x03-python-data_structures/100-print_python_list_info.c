#include "Python.h"

void print_python_list_info(PyObject *p)
{
  PyListObject *list;
  Py_ssize_t size, x;
  PyObject *object;
  struct _typeobject *type;

  if (strcmp(p->ob_type->tp_name, "list") == 0)
    {
      list = (PyListObject *)p;
      size = list->ob_base.ob_size;
      printf("[*] Size of the Python List = %ld\n", size);
      printf("[*] Allocated = %ld\n", list->allocated);
      for (x = 0; x < size; x++)
	{
	  object = list->ob_item[x];
	  type = object->ob_type;
	  printf("Element %ld: %s\n", x, type->tp_name);
	}
    }
}
