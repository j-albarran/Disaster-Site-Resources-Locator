from flask import Flask, jsonify

categories = [
    {
        'cat' : 'water'
    },
    {
        'cat': 'medications'
    },
    {
        'cat': 'baby_food'
    },
    {
        'cat': 'canned_food'
    },
    {
        'cat': 'dry_food'
    },
    {
        'cat': 'ice'
    },
    {
        'cat': 'fuel'
    },
    {
        'cat': 'medical_devices'
    },
    {
        'cat': 'heavy_equipment'
    },
    {
        'cat': 'tools'
    },
    {
        'cat': 'clothing'
    },
    {
        'cat': 'power_generators'
    },
    {
        'cat': 'batteries'
    }
]

class CategoryHandler:
    def getAllCategories(self):
        category_list = []
        for category in categories:
            category_list.append(category)
        if not category_list:
            return jsonify(Error="Not found!"), 404
        else:
            return jsonify(Categories = category_list)

    def getCategoryByName(self, name):
        result = None
        for category in categories:
            if category['cat'] == name:
                result = category
        if not result:
            return jsonify(Error="Not found!"), 404
        else:
            return jsonify(Category = result)