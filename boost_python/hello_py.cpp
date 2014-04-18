#include <boost/python.hpp>
#include "hello.hpp"

using namespace boost::python;

BOOST_PYTHON_MODULE(hello_py)
{
	//add reqular functions to the module
	def("greet", greet);
	def("square", square);
}
