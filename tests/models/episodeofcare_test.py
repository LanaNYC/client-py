#  Generated from FHIR 4.0.1-9346c8cc45, SMART Health IT.

import os
import io
import unittest
import json
from fhirclient.models import episodeofcare
from fhirclient.models.fhirdate import FHIRDate
from fhirclient.models.fhirdatetime import FHIRDateTime
from fhirclient.models.fhirinstant import FHIRInstant
from fhirclient.models.fhirtime import FHIRTime


class EpisodeOfCareTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.path.join(os.path.dirname(__file__), '..', 'data', 'examples')
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("EpisodeOfCare", js["resourceType"])
        return episodeofcare.EpisodeOfCare(js)
    
    def testEpisodeOfCare1(self):
        inst = self.instantiate_from("episodeofcare-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a EpisodeOfCare instance")
        self.implEpisodeOfCare1(inst)
        
        js = inst.as_json()
        self.assertEqual("EpisodeOfCare", js["resourceType"])
        inst2 = episodeofcare.EpisodeOfCare(js)
        self.implEpisodeOfCare1(inst2)
    
    def implEpisodeOfCare1(self, inst):
        self.assertEqual(inst.diagnosis[0].rank, 1)
        self.assertEqual(inst.diagnosis[0].role.coding[0].code, "CC")
        self.assertEqual(inst.diagnosis[0].role.coding[0].display, "Chief complaint")
        self.assertEqual(inst.diagnosis[0].role.coding[0].system, "http://terminology.hl7.org/CodeSystem/diagnosis-role")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "http://example.org/sampleepisodeofcare-identifier")
        self.assertEqual(inst.identifier[0].value, "123")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.period.start.datetime, FHIRDateTime("2014-09-01").datetime)
        self.assertEqual(inst.period.start.as_json(), "2014-09-01")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.statusHistory[0].period.end.datetime, FHIRDateTime("2014-09-14").datetime)
        self.assertEqual(inst.statusHistory[0].period.end.as_json(), "2014-09-14")
        self.assertEqual(inst.statusHistory[0].period.start.datetime, FHIRDateTime("2014-09-01").datetime)
        self.assertEqual(inst.statusHistory[0].period.start.as_json(), "2014-09-01")
        self.assertEqual(inst.statusHistory[0].status, "planned")
        self.assertEqual(inst.statusHistory[1].period.end.datetime, FHIRDateTime("2014-09-21").datetime)
        self.assertEqual(inst.statusHistory[1].period.end.as_json(), "2014-09-21")
        self.assertEqual(inst.statusHistory[1].period.start.datetime, FHIRDateTime("2014-09-15").datetime)
        self.assertEqual(inst.statusHistory[1].period.start.as_json(), "2014-09-15")
        self.assertEqual(inst.statusHistory[1].status, "active")
        self.assertEqual(inst.statusHistory[2].period.end.datetime, FHIRDateTime("2014-09-24").datetime)
        self.assertEqual(inst.statusHistory[2].period.end.as_json(), "2014-09-24")
        self.assertEqual(inst.statusHistory[2].period.start.datetime, FHIRDateTime("2014-09-22").datetime)
        self.assertEqual(inst.statusHistory[2].period.start.as_json(), "2014-09-22")
        self.assertEqual(inst.statusHistory[2].status, "onhold")
        self.assertEqual(inst.statusHistory[3].period.start.datetime, FHIRDateTime("2014-09-25").datetime)
        self.assertEqual(inst.statusHistory[3].period.start.as_json(), "2014-09-25")
        self.assertEqual(inst.statusHistory[3].status, "active")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type[0].coding[0].code, "hacc")
        self.assertEqual(inst.type[0].coding[0].display, "Home and Community Care")
        self.assertEqual(inst.type[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/episodeofcare-type")

