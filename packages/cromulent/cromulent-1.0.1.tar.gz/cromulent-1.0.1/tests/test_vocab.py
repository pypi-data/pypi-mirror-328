import unittest 
import sys
import os

from cromulent import vocab, model
from cromulent.model import factory

class TestClassBuilder(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_class(self):
		vocab.register_aat_class("TestObject1", {"parent": model.HumanMadeObject, "id": "1", "label": "example 1"})
		from cromulent.vocab import TestObject1
		self.assertEqual(TestObject1._classification[0].id, 'http://vocab.getty.edu/aat/1')

	def test_instance(self):
		vocab.register_instance("TestMaterial2", {"parent": model.Material, "id": "2", "label": "example 2"})
		self.assertTrue('TestMaterial2' in vocab.instances)
		tm2 = vocab.instances['TestMaterial2']
		self.assertEqual(tm2.id, "http://vocab.getty.edu/aat/2")

	def test_metatype(self):
		vocab.register_instance("example", {"parent": model.Type, "id": "3", "label": "example type"}) 
		vocab.register_aat_class("TestObject2", 
			{"parent": model.HumanMadeObject, "id": "4", "label": "example typed object", "metatype": "example"})
		from cromulent.vocab import TestObject2
		self.assertEqual(TestObject2._classification[0].classified_as[0].id, 'http://vocab.getty.edu/aat/3')

	def test_multitype(self):
		from cromulent.vocab import make_multitype_obj, Painting, Drawing
		inst = make_multitype_obj(Painting, Drawing)
		self.assertTrue(isinstance(inst, Painting))
		self.assertTrue(len(inst.classified_as) == 2)
		self.assertTrue(inst.classified_as[1].id == "http://vocab.getty.edu/aat/300033973")

		from cromulent.model import HumanMadeObject

		inst = make_multitype_obj(HumanMadeObject, Painting)
		self.assertTrue(len(inst.classified_as) == 1)
		self.assertTrue(inst.classified_as[0].id == "http://vocab.getty.edu/aat/300033618")

	def test_conceptual_parts(self):
		r = model.Right()
		r2 = model.Right()
		self.assertRaises(model.DataError, r.__setattr__, 'part', r2)
		r.conceptual_part = r2
		self.assertTrue(r2 in r.conceptual_part)

		vocab.conceptual_only_parts()
		r3 = model.Right()
		r4 = model.Right()
		r3.part = r4
		self.assertTrue(r4 in r3.conceptual_part)
		self.assertTrue("part" in model.factory.toJSON(r3))
		self.assertTrue(r4 in r3.part)


	def test_art_setter(self):
		p = model.HumanMadeObject("a", art=1)
		p._label = "a"
		pj = p._toJSON(done={})
		self.assertFalse(pj.get('classified_as', None))
		vocab.add_art_setter()
		p2 = vocab.Painting("b", art=1)
		p2j = p2._toJSON(done={})

	def test_aa_check(self):

		# Make sure that some other test hasn't set it
		try:
			del model.AttributeAssignment.set_assigned_property
		except:
			pass

		t = model.Type()
		aa = model.AttributeAssignment()
		# First check that aa accepts a type
		aa.assigned_property = t
		# And will not accept a string
		self.assertRaises(model.DataError, aa.__setattr__, "assigned_property", "classified_as")

		# Check we can set anything to assigned / assigned_to
		aa.assigned_property = None
		aa.assigned = aa
		aa.assigned_to = aa
		self.assertEqual(aa.assigned[0], aa)
		self.assertEqual(aa.assigned_to, aa)

		vocab.add_attribute_assignment_check()

		# This should fail right now as can't classify as an AA
		self.assertRaises(model.DataError, aa.__setattr__, "assigned_property", "classified_as")
		aa.assigned = None
		aa.assigned_to = None
		aa.assigned = t
		aa.assigned_to = t
		aa.assigned_property = "classified_as"
		self.assertEqual(aa.assigned_property, 'classified_as')


	def test_boundary_setter(self):
		vocab.add_linked_art_boundary_check()
		p = model.Person()
		p2 = model.Person()
		n = model.Name()
		n.content = "Test"
		p2.identified_by = n
		p.equivalent = p2
		# Now, Test should not appear in the resulting JSON of p
		factory.linked_art_boundaries = True
		js = factory.toJSON(p)
		self.assertTrue(not 'identified_by' in js['equivalent'][0])
		factory.linked_art_boundaries = False
		js = factory.toJSON(p)
		self.assertTrue('identified_by' in js['equivalent'][0])		

	def test_procurement_boundary(self):
		vocab.add_linked_art_boundary_check()
		a = model.Activity()
		p = vocab.ProvenanceEntry()
		a.caused = p
		js = factory.toJSON(a)
		self.assertTrue(not 'classified_as' in js['caused'][0])		

	def test_linguistic_object_boundary(self):
		vocab.add_linked_art_boundary_check()
		jrnl = vocab.JournalText(label="journal")
		issue = vocab.IssueText(label="issue")
		issue.part_of = jrnl
		issue.referred_to_by = vocab.MaterialStatement(content="Statement")

		js = factory.toJSON(issue)
		# Have not embedded journal in issue
		self.assertTrue(not 'classified_as' in js['part_of'][0])
		# Have embedded statement in issue
		self.assertTrue('content' in js['referred_to_by'][0])
		self.assertTrue('type' in js['referred_to_by'][0]['classified_as'][0]['classified_as'][0])

