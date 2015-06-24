import b3
import unittest

class A(b3.Composite): pass
class B(b3.Decorator): pass
class C(b3.Condition): pass
class D(b3.Action): pass

names = {'A':A, 'B':B, 'C':C, 'D':D}
data = {
    "title": "Custom Name BT",
    "description": "description =)",
    "root": "50352f51-c3f3-4a95-bd9b-4721bcd7e315",
    "display": {
        "camera_x": 492,
        "camera_y": 430.5,
        "camera_z": 1,
        "x": 0,
        "y": 0
    },
    "properties": {
        "a": 2
    },
    "nodes": {
        "50352f51-c3f3-4a95-bd9b-4721bcd7e315": {
            "id": "50352f51-c3f3-4a95-bd9b-4721bcd7e315",
            "name": "Sequence",
            "title": "Sequence2",
            "description": "",
            "display": {
                "x": 208,
                "y": 0
            },
            "parameters": {},
            "properties": {
                "b": "cv"
            },
            "children": [
                "09d0b3d8-c858-4985-b541-24af164b3132",
                "ed0251a1-605c-4b1e-b43e-3d9d7ea0512a"
            ]
        },
        "09d0b3d8-c858-4985-b541-24af164b3132": {
            "id": "09d0b3d8-c858-4985-b541-24af164b3132",
            "name": "MemSequence",
            "title": "MemSequence",
            "description": "",
            "display": {
                "x": 416,
                "y": -80
            },
            "parameters": {},
            "properties": {},
            "children": [
                "30c7361c-6d3a-4385-9b4d-6b8eedbd547a",
                "26dde02e-7bda-4c54-94e8-28f052fbf016"
            ]
        },
        "ed0251a1-605c-4b1e-b43e-3d9d7ea0512a": {
            "id": "ed0251a1-605c-4b1e-b43e-3d9d7ea0512a",
            "name": "A",
            "title": "A",
            "description": "",
            "display": {
                "x": 416,
                "y": 80
            },
            "parameters": {},
            "properties": {},
            "children": [
                "b2364dc1-d251-44c9-b3ba-80fc0c96aa55",
                "8a1cff9f-9d1c-48db-ba7f-4543544506df",
                "53374d73-b5c6-4aca-8891-853b2cd18c57"
            ]
        },
        "b2364dc1-d251-44c9-b3ba-80fc0c96aa55": {
            "id": "b2364dc1-d251-44c9-b3ba-80fc0c96aa55",
            "name": "B",
            "title": "B",
            "description": "",
            "display": {
                "x": 624,
                "y": 16
            },
            "parameters": {},
            "properties": {},
            "child": "ec40a510-f558-41a6-92ab-726be25715b4"
        },
        "26dde02e-7bda-4c54-94e8-28f052fbf016": {
            "id": "26dde02e-7bda-4c54-94e8-28f052fbf016",
            "name": "C",
            "title": "C",
            "description": "",
            "display": {
                "x": 624,
                "y": -48
            },
            "parameters": {},
            "properties": {}
        },
        "ec40a510-f558-41a6-92ab-726be25715b4": {
            "id": "ec40a510-f558-41a6-92ab-726be25715b4",
            "name": "D",
            "title": "D",
            "description": "",
            "display": {
                "x": 832,
                "y": 16
            },
            "parameters": {},
            "properties": {}
        },
        "a01d941b-c248-4ef5-870d-cc58b913fe3d": {
            "id": "a01d941b-c248-4ef5-870d-cc58b913fe3d",
            "name": "Failer",
            "title": "Failer",
            "description": "",
            "display": {
                "x": 832,
                "y": -112
            },
            "parameters": {},
            "properties": {}
        },
        "8a1cff9f-9d1c-48db-ba7f-4543544506df": {
            "id": "8a1cff9f-9d1c-48db-ba7f-4543544506df",
            "name": "Error",
            "title": "Error",
            "description": "",
            "display": {
                "x": 624,
                "y": 80
            },
            "parameters": {},
            "properties": {}
        },
        "53374d73-b5c6-4aca-8891-853b2cd18c57": {
            "id": "53374d73-b5c6-4aca-8891-853b2cd18c57",
            "name": "Error",
            "title": "Error",
            "description": "",
            "display": {
                "x": 624,
                "y": 144
            },
            "parameters": {},
            "properties": {}
        },
        "30c7361c-6d3a-4385-9b4d-6b8eedbd547a": {
            "id": "30c7361c-6d3a-4385-9b4d-6b8eedbd547a",
            "name": "Inverter",
            "title": "Inverter",
            "description": "",
            "display": {
                "x": 624,
                "y": -112
            },
            "parameters": {},
            "properties": {},
            "child": "a01d941b-c248-4ef5-870d-cc58b913fe3d"
        }
    },
    "custom_nodes": [
        {
            "name": "A",
            "title": "A",
            "category": "composite"
        },
        {
            "name": "B",
            "title": "B",
            "category": "decorator"
        },
        {
            "name": "C",
            "title": "C",
            "category": "condition"
        },
        {
            "name": "D",
            "title": "D",
            "category": "action"
        }
    ]
}

class TestPriority(unittest.TestCase):
    def test_load(self):
        tree = b3.BehaviorTree()
        tree.load(data, names)

        self.assertEqual(tree.title, 'Custom Name BT')
        self.assertEqual(tree.description, 'description =)')
        self.assertEqual(tree.properties['a'], 2)

        self.assertNotEqual(tree.root, None)
        self.assertEqual(tree.root.name, 'Sequence')
        self.assertEqual(tree.root.title, 'Sequence2')
        self.assertEqual(tree.root.description, '')
        self.assertEqual(len(tree.root.properties), 1)
        self.assertEqual(tree.root.properties['b'], 'cv')
        self.assertEqual(len(tree.root.children), 2)

    def test_dump(self):
        tree = b3.BehaviorTree()
        class Custom(b3.Condition):
            title = 'custom'

        tree.properties = {
            'prop': 'value',
            'comp': {'val1': 234, 'val2': 'value'}
        }

        node5 = Custom();
        node5.id = 'node-5';
        node5.title = 'Node5';
        node5.description = 'Node 5 Description';

        node4 = b3.Wait();
        node4.id = 'node-4';
        node4.title = 'Node4';
        node4.description = 'Node 4 Description';

        node3 = b3.MemSequence([node5]);
        node3.id = 'node-3';
        node3.title = 'Node3';
        node3.description = 'Node 3 Description';

        node2 = b3.Inverter(node4);
        node2.id = 'node-2';
        node2.title = 'Node2';
        node2.description = 'Node 2 Description';

        node1 = b3.Priority([node2, node3]);
        node1.id = 'node-1';
        node1.title = 'Node1';
        node1.description = 'Node 1 Description';
        node1.properties = { 'key' : 'value' }

        tree.root = node1;
        tree.title = 'Title in Tree';
        tree.description = 'Tree Description';
        
        data = tree.dump();

        self.assertEqual(data['title'], 'Title in Tree');
        self.assertEqual(data['description'], 'Tree Description');
        self.assertEqual(data['root'], 'node-1');
        self.assertEqual(data['properties']['prop'], 'value');
        self.assertEqual(data['properties']['comp']['val1'], 234);
        self.assertEqual(data['properties']['comp']['val2'], 'value');

        self.assertNotEqual(data['custom_nodes'], None);
        self.assertEqual(len(data['custom_nodes']), 1);
        self.assertEqual(data['custom_nodes'][0]['name'], 'Custom');
        self.assertEqual(data['custom_nodes'][0]['title'], 'Node5');
        self.assertEqual(data['custom_nodes'][0]['category'], b3.CONDITION);

        self.assertNotEqual(data['nodes']['node-1'], None);
        self.assertNotEqual(data['nodes']['node-2'], None);
        self.assertNotEqual(data['nodes']['node-3'], None);
        self.assertNotEqual(data['nodes']['node-4'], None);
        self.assertNotEqual(data['nodes']['node-5'], None);

        self.assertEqual(data['nodes']['node-1']['id'], 'node-1');
        self.assertEqual(data['nodes']['node-1']['name'], 'Priority');
        self.assertEqual(data['nodes']['node-1']['title'], 'Node1');
        self.assertEqual(data['nodes']['node-1']['description'], 'Node 1 Description');
        self.assertEqual(data['nodes']['node-1']['children'][0], 'node-3');
        self.assertEqual(data['nodes']['node-1']['children'][1], 'node-2');
        self.assertEqual(data['nodes']['node-1']['properties']['key'], 'value');

        self.assertEqual(data['nodes']['node-2']['name'], 'Inverter');
        self.assertEqual(data['nodes']['node-2']['title'], 'Node2');
        self.assertEqual(data['nodes']['node-2']['description'], 'Node 2 Description');
        self.assertNotEqual(data['nodes']['node-2']['child'], None);

        self.assertEqual(data['nodes']['node-3']['name'], 'MemSequence');
        self.assertEqual(data['nodes']['node-3']['title'], 'Node3');
        self.assertEqual(data['nodes']['node-3']['description'], 'Node 3 Description');
        self.assertEqual(len(data['nodes']['node-3']['children']), 1);

        self.assertEqual(data['nodes']['node-4']['name'], 'Wait');
        self.assertEqual(data['nodes']['node-4']['title'], 'Node4');
        self.assertEqual(data['nodes']['node-4']['description'], 'Node 4 Description');

        self.assertEqual(data['nodes']['node-5']['name'], 'Custom');
        self.assertEqual(data['nodes']['node-5']['title'], 'Node5');
        self.assertEqual(data['nodes']['node-5']['description'], 'Node 5 Description');