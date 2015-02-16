from __future__ import with_statement

import unittest
import flask
import flask_elasticsearch

class BasicAppTestCase(unittest.TestCase):

    def setUp(self):
        app = flask.Flask(__name__)
        app.config['ELASTICSEARCH_URL'] = 'http://localhost:9200'
        app.config['TESTING'] = True
        self.app = app


    def tearDown(self):
        pass


    def test_dummy(self):
        self.assertEqual(1, 1)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(BasicAppTestCase))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
