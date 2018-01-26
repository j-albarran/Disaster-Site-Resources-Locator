from flask import jsonify
from dao.dashboards import DashBoardsDAO


class DashBoardHandler:
    def build_need_dict(self, row):
        result = {}
        if row[0]:
            result['value'] = int(row[0])
        else:
            result['value'] = 0
        result['label'] = 'Need'
        return result

    def build_available_dict(self, row):
        result = {}
        if row[0]:
            result['value'] = int(row[0])
        else:
            result['value'] = 0
        result['label'] = 'Available'
        return result


    def build_theme_available(self):
        result = {}
        result['caption'] = 'Available Today'
        result['subCaption'] = 'Resource App'
        result['xAxisName'] = 'Today'
        result['yAxisName'] = 'Quantity'
        return result

    def build_theme_need(self):
        result = {}
        result['caption'] = 'In Need Today'
        result['subCaption'] = 'Resource App'
        result['xAxisName'] = 'Today'
        result['yAxisName'] = 'Quantity'
        return result

    def build_theme_availableW(self):
        result = {}
        result['caption'] = 'Available Since 7 Days Ago'
        result['subCaption'] = 'Resource App'
        result['xAxisName'] = '7 Days'
        result['yAxisName'] = 'Quantity'
        return result

    def build_theme_needW(self):
        result = {}
        result['caption'] = 'In Need For 7 Days'
        result['subCaption'] = 'Resource App'
        result['xAxisName'] = '7 Days'
        result['yAxisName'] = 'Quantity'
        return result

    def getResourcesNeedsDaily(self):
        dao = DashBoardsDAO()
        need_list = dao.getResourcesNeedsDaily() #Select cid, card_number, security_code, cname, exp_date from Credit_Card
        result_list = []
        for row in need_list:
            result = self.build_need_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Result Not Found"), 404
        else:
            return jsonify(chart=self.build_theme_need(),data=result_list), 200

    def getResourcesAvailablesDaily(self):
        dao = DashBoardsDAO()
        need_list = dao.getResourcesAvailablesDaily()  # Select cid, card_number, security_code, cname, exp_date from Credit_Card
        result_list = []
        for row in need_list:
            result = self.build_available_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Result Not Found"), 404
        else:
            return jsonify(chart=self.build_theme_available(), data=result_list), 200

    def getResourcesAvailablesWeekly(self):
        dao = DashBoardsDAO()
        need_list = dao.getResourcesAvailablesWeekly() #Select cid, card_number, security_code, cname, exp_date from Credit_Card
        result_list = []
        for row in need_list:
            result = self.build_available_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Result Not Found"), 404
        else:
            return jsonify(chart=self.build_theme_availableW(),data=result_list), 200

    def getResourcesNeedsWeekly(self):
        dao = DashBoardsDAO()
        need_list = dao.getResourcesNeedsWeekly() #Select cid, card_number, security_code, cname, exp_date from Credit_Card
        result_list = []
        for row in need_list:
            result = self.build_need_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Result Not Found"), 404
        else:
            return jsonify(chart=self.build_theme_needW(),data=result_list), 200