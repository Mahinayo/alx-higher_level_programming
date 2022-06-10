#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - basic info about Python lists and Python bytes objects
 * @p: PyBytesObject
 */
void print_python_list(PyObject *p)
{
  int x, y, z;
  const char *type;
  PyListObject *list = (PyListObject *)p;
  PyVarObject *var = (PyVarObject *)p;

  x = var->ob_size;
  y = list->allocated;

  printf("[*] Python list info\n");
  printf("[*] Size of the Python List = %d\n", x);
  printf("[*] Allocated = %d\n", y);

  for (z = 0; z < x; z++)
    {
      type = list->ob_item[z]->ob_type->tp_name;
      printf("Element %d: %s\n", z, type);
      if (strcmp(type, "bytes") == 0)
	print_python_bytes(list->ob_item[z]);
    }
}

/**
 * print_python_bytes - basic info about Python lists and Python bytes objects.

 * @p: PyBytesObject
 */
void print_python_bytes(PyObject *p)
{
  unsigned char i, size;
  PyBytesObject *bytes = (PyBytesObject *)p;

  printf("[.] bytes object info\n");
  if (strcmp(p->ob_type->tp_name, "bytes") != 0)
    {
      printf("  [ERROR] Invalid Bytes Object\n");
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
