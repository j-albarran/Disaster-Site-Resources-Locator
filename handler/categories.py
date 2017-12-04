from flask import Flask, jsonify

class CategoryHandler:
    def getAllCategories(self):
        return jsonify(Categories = "All categories")

    def getCategoryByName(self, name):
        return jsonify(Categories = "Category with name " + name)
