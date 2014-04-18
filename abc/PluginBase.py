#! /usr/bin/env python
import abc
from cStringIO import StringIO

class PluginBase(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def load(self, input):
		"""Retrieve data from the input source and return"""
		return

	@abc.abstractmethod
	def save(sefl, output, data):
		"""save the data object to the output."""
		return

	@abc.abstractmethod
	def retrieve_values(self, input):
		print 'base class reading data'
		return input.read()

class RegisterdImplementation(object):
	def load(self, input):
		return input.read()

	def save(self, output, data):
		return output.write(data)

class SubclassImplementation(PluginBase):

	def load(self, input):
		return input.read()

	def save(self, output, data):
		return output.write(data)

	def retrieve_values(self, input):
		base_data = super(SubclassImplementation, self).retrieve_values(input)
		print 'subclass sorting data'
		response = sorted(base_data.splitlines())
		return response


PluginBase.register(RegisterdImplementation)
input = StringIO("""line one
	line two
	line three
	""")

if __name__=='__main__':
	print 'Subclass: ', issubclass(RegisterdImplementation, PluginBase)
	print 'Instance: ', isinstance(RegisterdImplementation(), PluginBase)

	print 'Subclass: ', issubclass(SubclassImplementation, PluginBase)
	print 'Instance: ', isinstance(SubclassImplementation(), PluginBase)

	for sc in PluginBase.__subclasses__():
		print sc.__name__

	reader = SubclassImplementation()
	print reader.retrieve_values(input)